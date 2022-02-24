from selenium.webdriver.common.by import By


class PageIndexLocators(object):
    query_top = (By.ID, 'search_query_top')
    query_button = (By.NAME, 'submit_search')
    search_results = (
        By.CLASS_NAME, 'heading-counter')
    item_link = (
        By.ID, 'color_7')
    dresses_link = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
    contact_link = (By.ID, 'contact-link')


class PageDressesLocators(object):

    colors = (By.NAME, 'layered_id_attribute_group_16')
    girly = (By.ID, 'uniform-layered_id_feature_13')
    products_sort = (By.ID, 'selectProductSort')
    first_product = (By.CSS_SELECTOR, '#center_column > ul > li.ajax_block_product.col-xs-12.col-sm-6.col-md-4.first-in-line.last-line.first-item-of-tablet-line.first-item-of-mobile-line.last-mobile-line > div > div.right-block > h5 > a')


class ItemPageLocators(object):
    plus_button = (
        By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[2]/p[1]/a[2]')
    size_dropdown = (By.ID, 'group_1')
    add_cart_button = (By.NAME, 'Submit')
    proceed_checkout = (
        By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')
    product_container = (By.CSS_SELECTOR, 'body.search.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-9 ul.product_list.grid.row:nth-child(3) li.ajax_block_product.col-xs-12.col-sm-6.col-md-4.first-in-line.last-line.first-item-of-tablet-line.first-item-of-mobile-line.last-mobile-line div.product-container div.left-block > div.product-image-container')
    quick_view = (By.XPATH, "//span[normalize-space()='Quick view']")
    product_name = (By.CLASS_NAME, 'product-name')


class CheckoutLocators(object):
    proceed_checkout_2 = (
        By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')
    user_name = (By.ID, 'email')
    password = (By.ID, 'passwd')
    sign_in_button = (By.ID, 'SubmitLogin')
    process_address = (By.CSS_SELECTOR, '#center_column > form > p > button')
    terms_service_check = (
        By.CLASS_NAME, "checker")
    terms_service = (
        By.XPATH, "//input[@id='cgv']")
    process_carrier = (By.NAME, 'processCarrier')
    bank_wire_button = (By.CLASS_NAME, 'bankwire')
    confirm_order_button = (
        By.XPATH, '//*[@id="cart_navigation"]/button')
    confirm_message = (
        By.XPATH, '//*[@id="center_column"]/div/p/strong')


class ContactFormLocators(object):
    subject_dropdown = (By.CSS_SELECTOR, '#id_contact')
    email_field = (By.ID, "email")
    attach_field = (By.ID, "fileUpload")
    message_body = (By.ID, "message")
    send_button = (By.ID, "submitMessage")
    confirm_message = (By.XPATH, '//*[@id="center_column"]/p')
