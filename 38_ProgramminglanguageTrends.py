
# programming languages Ranking 2015-2024
import matplotlib.pyplot as plt

languages = ['Python', 'JavaScript', 'Java', 'C', 'C++']
years = list(range(2015, 2025))  # 2015 to 2024

rankings = [
    [5, 4, 3, 3, 2, 2, 1, 1, 1, 1],  # Python
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],  # JavaScript
    [1, 1, 1, 1, 1, 1, 2, 3, 3, 3],  # Java
    [2, 2, 2, 2, 2, 2, 3, 4, 4, 4],  # C
    [3, 3, 4, 4, 4, 4, 4, 5, 5, 5]   # C++
]

colors = ['red', 'magenta', 'purple', 'orange', 'lime']

plt.figure(figsize=(10, 6))

for i, (language, ranking) in enumerate(zip(languages, rankings)):
    plt.plot(years, ranking, label=language, color=colors[i], linewidth=2)

plt.gca().invert_yaxis()  # Invert the y-axis so rank 1 is at the top
plt.xticks(years, fontsize=10)
plt.yticks(range(1, 13), fontsize=10)
plt.title('Programming Language Trends (2015-2024)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Rank', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()

plt.show()
