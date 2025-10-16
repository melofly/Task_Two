from .base_element import BaseElement

class MultiWebElement(BaseElement):
    def wait_for_all_presence(self):
        return self._wait_for(EC.presence_of_all_elements_located)

    def wait_for_all_visible(self):
        return self._wait_for(EC.visibility_of_all_elements_located)