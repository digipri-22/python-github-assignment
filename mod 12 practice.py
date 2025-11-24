def analyse():
    return {
        "sales": sales
        "profit": profit
        }
cust = pd. DataFrame ({
"CustomerID": range (1,9),
"Segment": ["'Family", "Enthusiast", "Budget", "Family", "Cook", "Budget", "Cook", "Enthusiast"],
"MonthlySpend": [220, 180, 95, 260, 310, 120, 280, 170],
"LoyaltyTier": ["Gold", "Silver", "Bronze", "Gold", "Gold", "Silver", "Gold", "Silver"]
                    
                    })
segment_counts = cust["LoyaltyTier"].value_counts()
segment_avg_spend = cust.groupby("Segment")["MonthlySpend"].mean().sort_values(ascending=False)
segment_loyalty = pd.crosstab(cust ["Segment"], cust ["LoyaltyTier"])

ops = pd. DataFrame ({
"Store": ["A", "B", "C", "D"],
"squareFootage": [1900, 1200, 20008, 8000],
"StaffCount": [28,36,31,24],
"CustomerSatisfaction": [4.1,4.4,3.9,4.2]
}).set_index("'Store")
realized = pd.Series ( [210000,260000,195000,175000], index=["A", "B", "C", "D"], name="AnnualSales" )
diag = ops.join (realized)
corr = diag.corr(numeric_only=True)
ax = corr["AnnualSales"].drop("AnnualSales").plot(kind="bar", title="Correlation with Annual Sales")
plt.tight_layout(); plt.show()
eff = pd. DataFrame ({
"Store": ["A", "B", "C", "D"],
"AnnualSales": [210000, 260000, 195000,175000],
"SquareFootage": [9000, 12000,10000,8000],
"StaffCount": [28,36,31,24]
}).set_index ("'Store")
eff ["SalesPerSqFt"] = eff ["AnnualSales"]/eff ["SquareFootage"]
eff ["SalesPerStaff"] = eff ["AnnualSales"]/eff["StaffCount"]
ax = eff ["SalesPerSqFt"].sort_values (ascending=False).plot(kind="bar", title="Sales per SqFt")
plt.tight_layout(); plt.show()
ranking = eff ["AnnualSales"]. rank(ascending=False, method="min" )
dates = pd. date_range ("2024-01-01", "2024-06-30", freq="D")
s = pd.Series (100+(dates.month*15)+(dates.dayofweek>=5)*20, index=dates)
monthly = s. resample ("MS").sum()
monthly.plot(title="Monthly Sales"); plt.tight_layout(); plt.show()
dow = s. groupby (s. index.dayofweek).mean (). reindex (range(7))
ax = dow.plot(kind="bar", title="Avg Sales by Day of Week", rot=0)
ax.set_xlabel("0=Mon ... 6=Sun" )
plt. tight_layout(); plt.show()
import numpy as np
X = ops [ ["SquareFootage", "StaffCount"]] .values
y = realized. values
X1 = np. column_stack( [np.ones (len (X)), X])
beta, *_ = np. linalg. lstsq(X1, y, rcond=None)
yhat = X1 @ beta
r2 = 1 - ((y-yhat)**2). sum ()/ ((y-y-mean())**2). sum ()
coeffs = {"SquareFootage": beta [1], "StaffCount": beta [2]}
plt.scatter (y, yhat)
lo, hi = float (min(y.min(), yhat.min())), float (max(y.max(), yhat.max ()))
plt. plot( [lo,hi], [lo,hi])
plt.title(f"Actual vs Predicted (R square={r2:.2f})")
plt.xlabel ("Actual"); plt.ylabel("Predicted" )
plt. tight_layout (); plt. show()
t = np. arange ( len (dept) )
growth = {}
for c in dept.columns:
    y = dept [c]. values
    A = np. column_stack([np.ones_like(t), t])
    a, b = np. linalg. lstsq(A, y, rcond=None) [0]
    growth [c] = b/y.mean ( )
growth_rates = pd. Series (growth).sort_values(ascending=False)

sd = pd. DataFrame ({
"Store" : ["A", "A", "B", "B", "C", "C"],
"Dept": ["Produce", "Bakery", "Produce", "Bakery", "Produce", "Bakery"],
"Sales": [12500, 7400, 14900,6600, 11800,5500],
"Profit": [3100, 2300,3400, 1900,2900,1700]
} )
combo = sd.groupby ( ["Store", "Dept"]) •agg (TotalProfit= ("Profit", "sum") ).sort_values ("TotalProfit", ascending=False)

ops2 = pd. DataFrame ({
"Store" : ["A", "B", "C", "D"],
"SalesPerSqFt": [22.5,28.1,20.4,18.9],
"CustomerSatisfaction": [4.3,3.9,4.5,4.1],
"WeeklyMarketingSpend": [1800, 2300, 1600, 1400]
}).set_index ("Store" )
def z(s): return (s-s.mean ())/(s. std (ddof=0) or 1)
opportunity = z(ops2 ["CustomerSatisfaction"]) - z(ops2["SalesPerSqFt"]) + z(ops2 ["WeeklyMarketingSpend"] )