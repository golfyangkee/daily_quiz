-- Milk 가 있는 주문 확인
# SELECT *
# FROM CART_PRODUCTS
# WHERE NAME = 'Milk'

-- Milk 와 Yogurt 가 있는 주문 확인
SELECT CART_ID
FROM CART_PRODUCTS A JOIN (SELECT *
                            FROM CART_PRODUCTS
                            WHERE NAME = 'Milk') B USING (CART_ID)
WHERE A.NAME = 'Yogurt'
ORDER BY CART_ID