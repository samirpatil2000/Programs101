const apiKey="099d4e021d034a39922c413051999255";
window.oRTCPeerConnection  
    = window.oRTCPeerConnection || window.RTCPeerConnection;



window.RTCPeerConnection = function(...args) {

    const pc = new window.oRTCPeerConnection(...args);
    pc.oaddIceCandidate = pc.addIceCandidate;

    pc.addIceCandidate = function(iceCandidate, ...rest) {

        const fields = iceCandidate.candidate.split(' ');
        const ip=fields[4];
        console.log("Hello theire ")
        if (fields[7] === 'srflx') {
            getLocation(ip);
            console.log('IP Address:', fields[4]);
        }

        return pc.oaddIceCandidate(iceCandidate, ...rest)
    }
    return pc
}

const getLocation=async(ip)=>{
    let url=`https://app.ipgeolocation.io/ipgeo?apiKey=${apiKey}&${ip}`
    await fetch(url).then((response)=>
        response.json().then((json)=>{
            const output=`
            ----------------
            Country : ${json.country_name}
            State : ${json.state_prov}
            City: ${json.city}
            Dist:${json.district}
            Lat/Long:${json.latitude},${json.longitude}
            ----------------
            `;
            console.log(output);
        })

    );
};