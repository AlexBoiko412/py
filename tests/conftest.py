import httpx
import pytest

from api import app
from github_client import make_async_client


@pytest.fixture
def successful_summary():
    return {
        "username": "alex",
        "total_repos": 100,
        "total_stars": 456,
        "top_languages": [
            {
              "language": "Python",
              "repos_count": 26
            },
            {
              "language": "Rust",
              "repos_count": 8
            },
            {
              "language": "Go",
              "repos_count": 8
            },
            {
              "language": "CSS",
              "repos_count": 4
            },
            {
              "language": "C++",
              "repos_count": 3
            },
            {
              "language": "Ruby",
              "repos_count": 3
            },
            {
              "language": "JavaScript",
              "repos_count": 2
            },
            {
              "language": "HTML",
              "repos_count": 1
            },
            {
              "language": "Java",
              "repos_count": 1
            },
            {
              "language": "C",
              "repos_count": 1
            },
            {
              "language": "PLpgSQL",
              "repos_count": 1
            },
            {
              "language": "Shell",
              "repos_count": 1
            }
        ]
    }



@pytest.fixture
def github_response_data():
    return [
  {
    "full_name": "alex/0days-in-the-wild",
    "stargazers_count": 1,
    "name": "0days-in-the-wild",
    "html_url": "https://github.com/alex/0days-in-the-wild",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/abscissa",
    "stargazers_count": 1,
    "name": "abscissa",
    "html_url": "https://github.com/alex/abscissa",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/acme-lib",
    "stargazers_count": 1,
    "name": "acme-lib",
    "html_url": "https://github.com/alex/acme-lib",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/acme-spec",
    "stargazers_count": 1,
    "name": "acme-spec",
    "html_url": "https://github.com/alex/acme-spec",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/actions-experiments",
    "stargazers_count": 0,
    "name": "actions-experiments",
    "html_url": "https://github.com/alex/actions-experiments",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/adb",
    "stargazers_count": 1,
    "name": "adb",
    "html_url": "https://github.com/alex/adb",
    "language": "HTML",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/advisory-db",
    "stargazers_count": 0,
    "name": "advisory-db",
    "html_url": "https://github.com/alex/advisory-db",
    "language": "Rust",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/advisory-db-1",
    "stargazers_count": 0,
    "name": "advisory-db-1",
    "html_url": "https://github.com/alex/advisory-db-1",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/afl.rs",
    "stargazers_count": 0,
    "name": "afl.rs",
    "html_url": "https://github.com/alex/afl.rs",
    "language": "C++",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/alchimia",
    "stargazers_count": 102,
    "name": "alchimia",
    "html_url": "https://github.com/alex/alchimia",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/alex-gaynor-blog-design",
    "stargazers_count": 2,
    "name": "alex-gaynor-blog-design",
    "html_url": "https://github.com/alex/alex-gaynor-blog-design",
    "language": "CSS",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/alex-s-language",
    "stargazers_count": 7,
    "name": "alex-s-language",
    "html_url": "https://github.com/alex/alex-s-language",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/alpine_nodejs",
    "stargazers_count": 0,
    "name": "alpine_nodejs",
    "html_url": "https://github.com/alex/alpine_nodejs",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/ansible",
    "stargazers_count": 0,
    "name": "ansible",
    "html_url": "https://github.com/alex/ansible",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/api-serializer",
    "stargazers_count": 2,
    "name": "api-serializer",
    "html_url": "https://github.com/alex/api-serializer",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/apizza",
    "stargazers_count": 0,
    "name": "apizza",
    "html_url": "https://github.com/alex/apizza",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/arewepythonyet",
    "stargazers_count": 2,
    "name": "arewepythonyet",
    "html_url": "https://github.com/alex/arewepythonyet",
    "language": "JavaScript",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/arro3",
    "stargazers_count": 0,
    "name": "arro3",
    "html_url": "https://github.com/alex/arro3",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/asciinema",
    "stargazers_count": 1,
    "name": "asciinema",
    "html_url": "https://github.com/alex/asciinema",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/athenacli",
    "stargazers_count": 0,
    "name": "athenacli",
    "html_url": "https://github.com/alex/athenacli",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/atomiclong",
    "stargazers_count": 1,
    "name": "atomiclong",
    "html_url": "https://github.com/alex/atomiclong",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/audioipc-2",
    "stargazers_count": 1,
    "name": "audioipc-2",
    "html_url": "https://github.com/alex/audioipc-2",
    "language": "Rust",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/auditwheel",
    "stargazers_count": 1,
    "name": "auditwheel",
    "html_url": "https://github.com/alex/auditwheel",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/aws-dynamodb-encryption-python",
    "stargazers_count": 1,
    "name": "aws-dynamodb-encryption-python",
    "html_url": "https://github.com/alex/aws-dynamodb-encryption-python",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/aws-elastic-beanstalk-cli",
    "stargazers_count": 0,
    "name": "aws-elastic-beanstalk-cli",
    "html_url": "https://github.com/alex/aws-elastic-beanstalk-cli",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/aws-encryption-sdk-python",
    "stargazers_count": 2,
    "name": "aws-encryption-sdk-python",
    "html_url": "https://github.com/alex/aws-encryption-sdk-python",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/aws-lambda-go",
    "stargazers_count": 0,
    "name": "aws-lambda-go",
    "html_url": "https://github.com/alex/aws-lambda-go",
    "language": "Go",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/aws-sdk-go",
    "stargazers_count": 1,
    "name": "aws-sdk-go",
    "html_url": "https://github.com/alex/aws-sdk-go",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/aws-step-functions-data-science-sdk-python",
    "stargazers_count": 1,
    "name": "aws-step-functions-data-science-sdk-python",
    "html_url": "https://github.com/alex/aws-step-functions-data-science-sdk-python",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/azure-pipelines-docker-test",
    "stargazers_count": 2,
    "name": "azure-pipelines-docker-test",
    "html_url": "https://github.com/alex/azure-pipelines-docker-test",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/bagel",
    "stargazers_count": 21,
    "name": "bagel",
    "html_url": "https://github.com/alex/bagel",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/bazel",
    "stargazers_count": 1,
    "name": "bazel",
    "html_url": "https://github.com/alex/bazel",
    "language": "Java",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/bcode",
    "stargazers_count": 1,
    "name": "bcode",
    "html_url": "https://github.com/alex/bcode",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/bcrypt",
    "stargazers_count": 6,
    "name": "bcrypt",
    "html_url": "https://github.com/alex/bcrypt",
    "language": "C",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/beaker",
    "stargazers_count": 0,
    "name": "beaker",
    "html_url": "https://github.com/alex/beaker",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/beeline-go",
    "stargazers_count": 0,
    "name": "beeline-go",
    "html_url": "https://github.com/alex/beeline-go",
    "language": "Go",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/bitflags",
    "stargazers_count": 0,
    "name": "bitflags",
    "html_url": "https://github.com/alex/bitflags",
    "language": "Rust",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/botan",
    "stargazers_count": 0,
    "name": "botan",
    "html_url": "https://github.com/alex/botan",
    "language": "C++",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/botan-fuzzers",
    "stargazers_count": 1,
    "name": "botan-fuzzers",
    "html_url": "https://github.com/alex/botan-fuzzers",
    "language": "C++",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/boto",
    "stargazers_count": 2,
    "name": "boto",
    "html_url": "https://github.com/alex/boto",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/braid",
    "stargazers_count": 1,
    "name": "braid",
    "html_url": "https://github.com/alex/braid",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/brew",
    "stargazers_count": 0,
    "name": "brew",
    "html_url": "https://github.com/alex/brew",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/bson",
    "stargazers_count": 0,
    "name": "bson",
    "html_url": "https://github.com/alex/bson",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/buf_redux",
    "stargazers_count": 0,
    "name": "buf_redux",
    "html_url": "https://github.com/alex/buf_redux",
    "language": "Rust",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/buildevents",
    "stargazers_count": 0,
    "name": "buildevents",
    "html_url": "https://github.com/alex/buildevents",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cachecontrol",
    "stargazers_count": 1,
    "name": "cachecontrol",
    "html_url": "https://github.com/alex/cachecontrol",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/caddy",
    "stargazers_count": 1,
    "name": "caddy",
    "html_url": "https://github.com/alex/caddy",
    "language": "Go",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/caniusepython3",
    "stargazers_count": 1,
    "name": "caniusepython3",
    "html_url": "https://github.com/alex/caniusepython3",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/carbon",
    "stargazers_count": 1,
    "name": "carbon",
    "html_url": "https://github.com/alex/carbon",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/caremad.io",
    "stargazers_count": 1,
    "name": "caremad.io",
    "html_url": "https://github.com/alex/caremad.io",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cargo-audit",
    "stargazers_count": 0,
    "name": "cargo-audit",
    "html_url": "https://github.com/alex/cargo-audit",
    "language": "Rust",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cargo-edit",
    "stargazers_count": 0,
    "name": "cargo-edit",
    "html_url": "https://github.com/alex/cargo-edit",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cargo-fuzz",
    "stargazers_count": 0,
    "name": "cargo-fuzz",
    "html_url": "https://github.com/alex/cargo-fuzz",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cargo-vet",
    "stargazers_count": 0,
    "name": "cargo-vet",
    "html_url": "https://github.com/alex/cargo-vet",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/certifi",
    "stargazers_count": 1,
    "name": "certifi",
    "html_url": "https://github.com/alex/certifi",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/certlint",
    "stargazers_count": 0,
    "name": "certlint",
    "html_url": "https://github.com/alex/certlint",
    "language": "Ruby",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/certspotter",
    "stargazers_count": 0,
    "name": "certspotter",
    "html_url": "https://github.com/alex/certspotter",
    "language": "Go",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/certstore",
    "stargazers_count": 0,
    "name": "certstore",
    "html_url": "https://github.com/alex/certstore",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/certwatch_db",
    "stargazers_count": 0,
    "name": "certwatch_db",
    "html_url": "https://github.com/alex/certwatch_db",
    "language": "PLpgSQL",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cg-compliance",
    "stargazers_count": 1,
    "name": "cg-compliance",
    "html_url": "https://github.com/alex/cg-compliance",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cg-docs",
    "stargazers_count": 2,
    "name": "cg-docs",
    "html_url": "https://github.com/alex/cg-docs",
    "language": "CSS",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/chalk-log",
    "stargazers_count": 0,
    "name": "chalk-log",
    "html_url": "https://github.com/alex/chalk-log",
    "language": "Ruby",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/characteristic",
    "stargazers_count": 1,
    "name": "characteristic",
    "html_url": "https://github.com/alex/characteristic",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/chef-funnel",
    "stargazers_count": 1,
    "name": "chef-funnel",
    "html_url": "https://github.com/alex/chef-funnel",
    "language": "Ruby",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/chrome-broken-ssoi",
    "stargazers_count": 1,
    "name": "chrome-broken-ssoi",
    "html_url": "https://github.com/alex/chrome-broken-ssoi",
    "language": "JavaScript",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/chrono",
    "stargazers_count": 1,
    "name": "chrono",
    "html_url": "https://github.com/alex/chrono",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/classy",
    "stargazers_count": 1,
    "name": "classy",
    "html_url": "https://github.com/alex/classy",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/claude-experiments",
    "stargazers_count": 1,
    "name": "claude-experiments",
    "html_url": "https://github.com/alex/claude-experiments",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/client-beta",
    "stargazers_count": 2,
    "name": "client-beta",
    "html_url": "https://github.com/alex/client-beta",
    "language": "Go",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/client_python",
    "stargazers_count": 2,
    "name": "client_python",
    "html_url": "https://github.com/alex/client_python",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/clusterfuzzlite",
    "stargazers_count": 1,
    "name": "clusterfuzzlite",
    "html_url": "https://github.com/alex/clusterfuzzlite",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cockroach",
    "stargazers_count": 1,
    "name": "cockroach",
    "html_url": "https://github.com/alex/cockroach",
    "language": "Go",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/codecov-action",
    "stargazers_count": 2,
    "name": "codecov-action",
    "html_url": "https://github.com/alex/codecov-action",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/codecov-bash",
    "stargazers_count": 0,
    "name": "codecov-bash",
    "html_url": "https://github.com/alex/codecov-bash",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/codespeed",
    "stargazers_count": 3,
    "name": "codespeed",
    "html_url": "https://github.com/alex/codespeed",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/computer",
    "stargazers_count": 1,
    "name": "computer",
    "html_url": "https://github.com/alex/computer",
    "language": "CSS",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/console",
    "stargazers_count": 0,
    "name": "console",
    "html_url": "https://github.com/alex/console",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cookiecutter",
    "stargazers_count": 1,
    "name": "cookiecutter",
    "html_url": "https://github.com/alex/cookiecutter",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cookiemonster",
    "stargazers_count": 1,
    "name": "cookiemonster",
    "html_url": "https://github.com/alex/cookiemonster",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/core",
    "stargazers_count": 0,
    "name": "core",
    "html_url": "https://github.com/alex/core",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/coveragepy",
    "stargazers_count": 1,
    "name": "coveragepy",
    "html_url": "https://github.com/alex/coveragepy",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/coveralls-python",
    "stargazers_count": 2,
    "name": "coveralls-python",
    "html_url": "https://github.com/alex/coveralls-python",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cpython-1",
    "stargazers_count": 0,
    "name": "cpython-1",
    "html_url": "https://github.com/alex/cpython-1",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/crater",
    "stargazers_count": 0,
    "name": "crater",
    "html_url": "https://github.com/alex/crater",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/crossbeam",
    "stargazers_count": 2,
    "name": "crossbeam",
    "html_url": "https://github.com/alex/crossbeam",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/crossme",
    "stargazers_count": 2,
    "name": "crossme",
    "html_url": "https://github.com/alex/crossme",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/cryptography",
    "stargazers_count": 19,
    "name": "cryptography",
    "html_url": "https://github.com/alex/cryptography",
    "language": "Python",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/csv-sql",
    "stargazers_count": 213,
    "name": "csv-sql",
    "html_url": "https://github.com/alex/csv-sql",
    "language": "Rust",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/csv-to-parquet",
    "stargazers_count": 3,
    "name": "csv-to-parquet",
    "html_url": "https://github.com/alex/csv-to-parquet",
    "language": "Go",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/ct-logs",
    "stargazers_count": 0,
    "name": "ct-logs",
    "html_url": "https://github.com/alex/ct-logs",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/ct-tools",
    "stargazers_count": 16,
    "name": "ct-tools",
    "html_url": "https://github.com/alex/ct-tools",
    "language": "Rust",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/curl-rust",
    "stargazers_count": 0,
    "name": "curl-rust",
    "html_url": "https://github.com/alex/curl-rust",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/darwin-xnu",
    "stargazers_count": 0,
    "name": "darwin-xnu",
    "html_url": "https://github.com/alex/darwin-xnu",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/dataloader",
    "stargazers_count": 0,
    "name": "dataloader",
    "html_url": "https://github.com/alex/dataloader",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/dc-maps",
    "stargazers_count": 1,
    "name": "dc-maps",
    "html_url": "https://github.com/alex/dc-maps",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/der-ascii",
    "stargazers_count": 0,
    "name": "der-ascii",
    "html_url": "https://github.com/alex/der-ascii",
    "language": "Go",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/der-parser",
    "stargazers_count": 0,
    "name": "der-parser",
    "html_url": "https://github.com/alex/der-parser",
    "language": "Rust",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/developer.rackspace.com",
    "stargazers_count": 2,
    "name": "developer.rackspace.com",
    "html_url": "https://github.com/alex/developer.rackspace.com",
    "language": None,
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/devsite",
    "stargazers_count": 1,
    "name": "devsite",
    "html_url": "https://github.com/alex/devsite",
    "language": "CSS",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  },
  {
    "full_name": "alex/diff-so-fancy",
    "stargazers_count": 1,
    "name": "diff-so-fancy",
    "html_url": "https://github.com/alex/diff-so-fancy",
    "language": "Shell",
    "owner": {
      "login": "alex",
      "html_url": "https://github.com/alex"
    }
  }
]

def create_mock_client(handler, **kwargs) -> httpx.AsyncClient:
    return make_async_client(
        transport=httpx.MockTransport(handler),
        **kwargs
    )

@pytest.fixture(autouse=True)
def clear_overrides():
  yield
  app.dependency_overrides.clear()