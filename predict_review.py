from src.prediction.regression import predict_rating

print("\n===================================")
print("   PRODUCT REVIEW RATING PREDICTOR")
print("===================================")

while True:
    review = input("\nEnter your product review (or type 'exit' to quit): ")

    if review.lower() == "exit":
        print("Thank you for using the predictor!")
        break

    if not review.strip():
        print("Please enter a valid review.")
        continue

    rating = predict_rating(review)

    print(f"\nPredicted Rating: {rating:.2f} / 5")
    print("-----------------------------------")