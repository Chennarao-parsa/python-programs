# Example: Only fertilizer recommendation part

def recommend_fertilizer(n, p, k):
    recommendation = []

    if n < 50:
        recommendation.append("Add more nitrogen (e.g., Urea)")
    if p < 30:
        recommendation.append("Add more phosphorus (e.g., DAP)")
    if k < 40:
        recommendation.append("Add more potassium (e.g., MOP)")

    if not recommendation:
        return "Soil nutrients are balanced. No additional fertilizer needed."

    return "\n".join(recommendation)


# Example usage
n = int(input("Enter soil Nitrogen level: "))
p = int(input("Enter soil Phosphorus level: "))
k = int(input("Enter soil Potassium level: "))

print(recommend_fertilizer(n, p, k))
