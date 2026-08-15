def get_review_score(self):
        """
        Returns a DataFrame with:
        'seller_id', 'share_of_five_stars', 'share_of_one_stars', 'review_score'
        """
        orders_reviews = self.order.get_review_score()
        order_items = self.data['order_items'][['order_id', 'seller_id']].drop_duplicates()

        df = order_items.merge(orders_reviews, on='order_id')

        result = df.groupby('seller_id', as_index=False).agg({
            'dim_is_one_star': 'mean',
            'dim_is_five_star': 'mean',
            'review_score': 'mean',
        })
        result.columns = [
            'seller_id', 'share_of_one_stars', 'share_of_five_stars',
            'review_score'
        ]

        return result