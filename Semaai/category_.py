def _get_cat_info(self, categ_obj, context=None):
    context = context or {}
    cat_data = {
        "category_id": categ_obj.id,
        "name": categ_obj.name or "",
        "children": [],
        "icon": self._get_image_url('mobikul.category', categ_obj.id, 'icon', categ_obj.write_date, context=context),
    }
    return cat_data

def _recursive_cats(self, categ_obj, context=None):
    context = context or {}

    data = self._get_cat_info(categ_obj, context)
    if categ_obj.child_id:
        #_logger.info('categ_id---%r',categ_obj)
        for cat_child in categ_obj.child_id:
            data['children'].append(self._recursive_cats(cat_child, context))
    return data
