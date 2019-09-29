from commons.views import BaseView
from board.pin import PIN_TABLE


class PinView(BaseView):
    def get(self, request, pin_num):
        pin_num = int(pin_num)
        if pin_num in PIN_TABLE:
            pin = PIN_TABLE[pin_num]
            pin.set_mode()
        return BaseView.json_result(data=pin_num)
