# DFS - neetcode
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def dfs(recipe):
            # base case
            if recipe in can_cook:
                return can_cook[recipe]

            if recipe not in recipe_index:
                return False

            # this recipe is not present in can_coko
            # so now explore neighbors and try to add it to can_cook
            can_cook[recipe] = False # for detecting circular dependency
            for nei in ingredients[recipe_index[recipe]]:
                if not dfs(nei):
                    return False

            can_cook[recipe] = True
            return can_cook[recipe]         

        # make supplies hashmap
        can_cook = {supply:True for supply in supplies}         

        # make recipe index
        recipe_index = {recipe:index for index, recipe in enumerate(recipes)}

        # loop over all the recipes and pass them through DFS
        result = []
        for recipe in recipes:
            if dfs(recipe):
                result.append(recipe)

        return result        


# BFS - cracking FAANG
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # 1 - build graph
        graph = defaultdict(list) # {ingredient:recipe}
        indegree = defaultdict(int) # {recipe: # ingredients}

        for recipe, ingredient in zip(recipes, ingredients):
            indegree[recipe] = len(ingredient)

            for ingred in ingredient:
                graph[ingred].append(recipe)

        result = []
        q = deque(supplies)
        recipes = set(recipes)

        while q:
            supply = q.popleft()
            
            if supply in recipes:
                result.append(supply)

            for recipe in graph[supply]:
                indegree[recipe] -= 1

                if indegree[recipe] == 0:
                    q.append(recipe)

        return result
