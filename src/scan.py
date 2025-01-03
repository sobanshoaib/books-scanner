import cv2

def get_image():
    detect_code = cv2.barcode.BarcodeDetector() 
    capture = cv2.VideoCapture(0)
    print("----Searching for Barcode----")

    while True:
        _, frame = capture.read()
        result, decoded_info, _, _ = detect_code.detectAndDecode(frame)

        if result:
            print(f"Barcode: {decoded_info[0]}")
        
        cv2.imshow("Barcode Scanner", frame)

        if cv2.waitKey(1) == ord('q'):
            print("Scan Cancelled")
            result = 'Cancelled'
            break

    capture.release()
    cv2.destroyAllWindows()

    return result

def main():
    get_result = get_image()
    print(f"Result: {get_result}")
