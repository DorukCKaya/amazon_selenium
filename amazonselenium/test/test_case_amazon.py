from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.list_page import ListPage
from test.base_test import BaseTest


 """2. Login ekranını açıp, bir kullanıcı ile login olunacak (daha önce siteye üyeliği varsa o olabilir)
3. Ekranın üstündeki search alanına 'samsung' yazıp ara butonuna tıklanacak,
4. Gelen sayfada samsung için sonuç bulunduğunu onaylayacak,
5. Arama sonuçlarından 2. sayfaya tıklayacak ve açılan sayfada 2. sayfanın şu an gösterimde oldugunu onaylayacak,
6. Üstten 3. ürünün içindeki 'Add to List' butonuna tıklayacak,
7. Ekranın en üstündeki 'List' linkine tıklayacak, içerisinden wishlisti seçecek,
8. Açılan sayfada bir önceki sayfada izlemeye alınmış ürünün bulunduğunu onaylayacak,
9. Favorilere alınan bu ürünün yanındaki 'Delete' butonuna basarak favorilerimden çıkaracak,
10. Sayfada bu ürünün artık favorilerde olmadığını onaylayacak."""


class TestCaseAmazon(BaseTest):

    def test_steps(self):
        base_page = BasePage(self.driver)
        home_page = HomePage(self.driver)
        sign_in_page = SignInPage(self.driver)
        search_page = SearchPage(self.driver)
        product_page = ProductPage(self.driver)
        list_page = ListPage(self.driver)

        #anasayfanın açıldığını assertion ile onaylar
        assert self.locator.BASE_URL  == base_page.get_url()
        #signin sayfasına gider.
        home_page.navigate_to_sign_in()
        #giriş yapar.
        sign_in_page.sign_in()
        #keyword'ü arar.
        home_page.search_keyword()
        #keyword'e dair sonuç geldiğini assert ile kontrol eder.
        search_page.keyword_control()
        #2. sayfaya gider.
        search_page.navigate_to_second_page()
        #3. ürünün sayfasına gider.
        search_page.navigate_to_third_product()
        #ürünü listeye ekler.
        product_page.add_to_list()
        #doğru ürünün listeye eklendiğini assert ile kontrol eder.
        product_page.is_product_added_to_list()
        #liste sayfasına gider.
        product_page.navigate_to_list()
        #ürünü listeden siler.
        list_page.remove_product_from_list()
        #ürünün listeden silindiğini onaylar.
        list_page.is_item_removed()