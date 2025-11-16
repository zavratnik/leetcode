class Problem71:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split("/"):
            if part == "." or part == "":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    solution = Problem71()
    print(solution.simplifyPath("/home/"))                # "/home"
    print(solution.simplifyPath("/a/./b/../../c/"))       # "/c"
    print(solution.simplifyPath("/../"))                  # "/"
    print(solution.simplifyPath("/home//foo/"))           # "/home/foo"
