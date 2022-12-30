
import math

from icecream import ic

str_ = "domain,alexa_rank,aliases,alternates,android_app_id,average_product_price,brands_page_url,categories,city,collections,combined_followers,common_crawl_centrality,common_crawl_pagerank,company_ids,company_location,contact_page_url,country_code,created,currency,description,domain_count,domain_tld1,domain_url,emails,employee_count,estimated_monthly_sales,facebook,facebook_categories,facebook_followers,facebook_followers_30d,facebook_followers_90d,facebook_group,facebook_group_followers,facebook_group_followers_30d,facebook_group_followers_90d,facebook_group_url,facebook_url,favicon_url,features,financing_page_url,instagram,instagram_categories,instagram_followers,instagram_followers_30d,instagram_followers_90d,instagram_posts,instagram_url,installed_apps,installed_apps_names,ios_app_id,language_code,last_plan,last_plan_changed,last_platform,last_platform_changed,linkedin_account,linkedin_url,maximum_product_price,merchant_name,meta_description,meta_keywords,minimum_product_price,monthly_app_spend,most_recent_product_image_url,most_recent_product_title,most_recent_product_url,open_graph_image_url,phones,pinterest,pinterest_followers,pinterest_followers_30d,pinterest_followers_90d,pinterest_posts,pinterest_url,plan,platform,platform_domain,platform_rank,platform_rank_percentile,platform_version,product_images,product_images_created_30,product_images_created_365,product_images_created_90,product_variants,products_sold,rank,rank_percentile,region,retailer_url,returns_page_url,sales_channels,shipping_carriers,state,status,store_locator_url,street_address,subregion,tags,technologies,theme,theme_spend,theme_vendor,tiktok,tiktok_followers,tiktok_followers_30d,tiktok_followers_90d,tiktok_url,title,tracking_page_url,twitter,twitter_followers,twitter_followers_30d,twitter_followers_90d,twitter_posts,twitter_url,vendor_count,warranty_page_url,youtube,youtube_followers,youtube_followers_30d,youtube_followers_90d,youtube_url,zip"
class Solution:
    
    def countSquares(self, N):
        # code here 
        # ans = 1
        # for i in range(2, int(math.sqrt(N)) + 1):
        #     if i * i >= N:
        #         return ans
        #     ans = i
        # return ans
        return
    
    
# print(str_.split(","))
result = "("
for i in str_.split(","):
    result += i

    result += " string"
    result += ", "

print(result + ")")

        
            



N = 3
ic(Solution().countSquares(N))
ic(int(9.3), int(9.7))