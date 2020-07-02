import numpy as np
import cv2


def create_geometric_figure():
    """
    This fucntion create a geometric figure using opencv and numpy.
    :return: None
    """
    my_img = np.zeros((1500, 2000, 3), dtype = "uint8")
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "Geometric figure using coordinates"
    cv2.putText(my_img, text, (50, 50),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.circle(my_img, (200, 200), 40, (0, 20, 200),20)
    cv2.circle(my_img, (400, 400), 40, (0, 20, 200), 10)
    cv2.circle(my_img, (600, 600), 40, (0, 20, 200), 10)
    cv2.circle(my_img, (1400, 200), 40, (0, 20, 200), 20)
    cv2.circle(my_img, (1200, 400), 40, (0, 20, 200), 10)
    cv2.circle(my_img, (1000, 600), 40, (0, 20, 200), 10)

    # Uncomment below comments to view coordinates on screen.

    cv2.line(my_img, (230, 230), (365, 365), (0, 20, 200), 10)
    # cv2.putText(my_img, '230, 230', (230, 230),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
    # cv2.putText(my_img, '365, 365', (365, 365),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.line(my_img, (430, 430), (565, 565), (0, 20, 200), 10)
    # cv2.putText(my_img, '430, 430', (430, 430),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
    # cv2.putText(my_img, '565, 565', (565, 565),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.line(my_img, (640, 600), (955, 600), (0, 20, 200), 10)
    # cv2.putText(my_img, '640, 600', (640, 600),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
    # cv2.putText(my_img, '955, 600', (955, 600),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.line(my_img, (250, 200), (1350, 200), (0, 20, 200), 10)
    # cv2.putText(my_img, '250, 200', (250, 200),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
    # cv2.putText(my_img, '1350, 200', (1350, 200),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.line(my_img, (1370, 235), (1215, 365), (0, 20, 200), 10)
    # cv2.putText(my_img, '1370, 235', (1370, 235),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
    # cv2.putText(my_img, '1215, 365', (1215, 365),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.line(my_img, (1165, 425), (1015, 565), (0, 20, 200), 10)
    # cv2.putText(my_img, '1165, 425', (1165, 425),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
    # cv2.putText(my_img, '1015, 565', (1015, 565),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Window', my_img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    create_geometric_figure()
