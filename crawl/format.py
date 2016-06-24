# -*- coding: utf-8 -*-
settings_mapping = {
    # ----------------- 顶级配置 ------------------
    '_id': 'id',
    'comment': 'comment',
    'status': 'status',
    'maxExpandUrlNum': 'max_expand_url_num',
    'maxExpandUrlDepth': 'max_expand_url_depth',

    'schedulerType': 'scheduler_type',
    'scheduler': 'scheduler',
    'delay': 'delay',
    'dupFilterTime': 'dup_filter_time',
    'login': 'login',
    'startUrl': 'start_url',
    'dyStartUrl': 'dy_start_url',

    # ----------------- login -----------------------
    'userName': 'user_name',
    'userCssPath': 'user_css_path',
    'passwd': 'passwd',
    'passwdCssPath': 'passwd_css_path',
    'clickCssPath': 'click_css_path',

    # ----------------- dy_start_url ------------------
    'urlTemplate': 'url_template',
    'params': 'params',

    # ----------------- request_page_type ----------------
    'requestPageType': 'request_page_type',
    'renderJs': 'render_js',
    'contentType': 'content_type',
    'requestType': 'request_type',
    'method': 'method',
    'headers': 'headers',
    'body': 'body',
    'meta': 'meta',
    'formData': 'form_data',
    'dontFilter': 'dont_filter',

    # ----------------- selector配置 --------------------
    'selectors': 'selectors',
    'parentSelectors': 'parent_selectors',
    'type': 'type',
    'multiple': 'multiple',
    'id': 'id',
    'selector': 'css_paths',
    'tableHeaderRowSelector': 'table_header_row_selector',
    'tableDataRowSelector': 'table_data_row_selector',
    'columns': 'columns',
    'header': 'header',
    'name': 'name',
    'extract': 'extract',
    'extractAttribute': 'extract_attribute',
    'saveToDB': 'save_to_db',
    'downloadImage': 'download_image',

    'processors': 'processors',
    'context': 'context',

    # ------------------ version:2 版本 -------------------
    'urlMatches': 'url_matches',
    'urlPattern': 'url_pattern',
    'expandUrlPattern': 'expand_url_pattern',
    'notExpandUrlPattern': 'not_expand_url_pattern',
}

def format_config(json):
    def parse_value_to_we_need(parent_key, value):  # 用于调整各字段的value到我们需要的格式
        if parent_key == 'css_paths':
            value_lst = value.split(',')
            return map(str.strip if isinstance(value, str) else unicode.strip, value_lst)
        if parent_key == 'start_url':
            return [value]
        return value

    def parse_key_to_python_need(_json, parent_key):  # 用于调整各字段的key到python的命名格式
        if isinstance(_json, (list, tuple)):
            list_tmp = []
            for item in _json:
                list_tmp.append(parse_key_to_python_need(item, parent_key))
            return list_tmp
        elif isinstance(_json, dict):
            dict_tmp = {}
            for key, value in _json.items():
                if key in settings_mapping:
                    dict_tmp[settings_mapping.get(key)] = parse_key_to_python_need(value, settings_mapping.get(key))
                else:
                    dict_tmp[key] = parse_key_to_python_need(value, key)
            return dict_tmp
        else:
            return parse_value_to_we_need(parent_key, _json)

    return parse_key_to_python_need(json, '_root')
