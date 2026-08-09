type ComponentOptions<T> = {
  props: T
}

type Conditions = {
  expectedValue: string | number | boolean | object | null | undefined
  skip: boolean
  isAuthenticated: boolean
}

type TestCase = {
  title: string
} & Partial<ComponentOptions<Record<string, unknown>>> & Partial<Conditions>

type TestCases = TestCase[]

type UuidTestCase = TestCase & { uuid: string }

type UuidTestCases = UuidTestCase[]

export function defineTestCase(testCase: TestCase): UuidTestCase {
  return { ...testCase, uuid: crypto.randomUUID() }
}

class TestCaseManager {
  private cases: UuidTestCases = []

  constructor() {
    this.cases = []
  }

  get runner(): UuidTestCases {
    return this.cases
      .flatMap((testCase) => testCase)
      .filter((testCase) => !testCase.skip)
  }

  parameterize(testCase: TestCase[]): TestCaseManager {
    this.cases.push(...testCase.map((tc) => ({ ...tc, uuid: crypto.randomUUID() })))
    return this
  }

  caseForFailure<K extends keyof UuidTestCase[ 'props' ]>(fields: K[], ...args: string[]) {
    const candidates = this.cases.filter((testCase) => args.includes(testCase.title))
    candidates.forEach((testCase) => {
      this.cases.push({
        ...testCase,
        skip: true,
        props: fields.reduce((acc, field) => {
          if (testCase.props && field in testCase.props) {
            acc[ field ] = undefined
          }
          return acc
        }, {} as Record<string, unknown>)
      })
    })
    return this.runner
  }
}

export function definedTestCases(callback: (manager: TestCaseManager) => TestCaseManager): TestCaseManager {
  return callback(new TestCaseManager())
}
