# Hyperskill data preprocessing

This module contains methods to preprocess and prepare data, collected from Hyperskill educational platform, 
for further analysis. 

To run data preprocessing, run following python scripts in stated order:

1. [preprocess_submissions.py](preprocess_submissions.py) - merges submissions with detected issues. 

    **Required arguments:**
    
    | Argument | Description                                                                                                            |
    |------------------------------------------------------------------------------------------------------------------------|-------------|
    |**submissions_path**| Path to .csv file with `submissions`.                                                                                  |
    |**preprocessed_submissions_path**| Path to .csv output file with `preprocessed submissions` with issues. If not provided `submissions_path` will be used. |

    **Optional arguments:**
    
    | Argument | Description |
    |----------|-------------|
    | **&#8209;&#8209;users-to-submissions-path** | Path to file with `user` to submission relation (if data is not presented in submissions dataset or was anonymized). |
    | **&#8209;&#8209;diff-ratio** | Ration to remove submissions which has lines change more then in `diff-ratio` times. Default is 10.0. |
    | **&#8209;&#8209;max-attempts** | Remove submissions series with more then `max-attempts` attempts. Default is 5. |

2. [preprocess_issues.py](preprocess_issues.py) - collect information about issues, which are detected in all submissions. 
   Must be invoked twice (both for raw and qodana issues).
   
    **Required arguments:**
    
    | Argument | Description |
    |----------|-------------|
    |**issues_type**| Type of issues to analyse (can be `raw_issues` or `qodana_issues`). |
    |**submissions_path**| Path to .csv file with `preprocessed submissions`. |
    |**issues_path**| Path to .csv file with submissions to issues relation. |
    |**issues_info_path**| Path to .csv file where `preprocessed issues info` will be saved. |

    **Optional arguments:**
    
    | Argument | Description |
    |----------|-------------|
    | **&#8209;&#8209;ignore-issue-classes** | List of issue classes to remove from issues list (for example 'CyclomaticComplexityCheck', 'JavaNCSSCheck' raw issues and 'JavaAnnotator', 'WrongPackageStatement' qodana issues). |
   
3. [preprocess_topics.py](preprocess_topics.py) - add information about topic depth in knowledge tree.

    **Required arguments:**
    
    | Argument | Description |
    |----------|-------------|
    |**topics_path**| Path to .csv file with `topics` info. |
    |**preprocessed_topics_path**| Path to .csv file where `preprocessed topics` will be saved. If not provided `topics_path` will be used. |


4. [preprocess_steps.py](preprocess_steps.py) - add information about steps complexity, difficulty, 
   template and assignment features.

    **Required arguments:**
   
    | Argument | Description |
    |----------|-------------|
    |**steps_path**| Path to .csv file with `steps`. |
    |**topics_path**| Path to .csv file with `preprocessed topics`. |
    |**preprocessed_steps_path**| Path to .csv file where to save `preprocessed steps`. If not provided `steps_path` will be used. |

    **Optional arguments:**
    
    | Argument | Description |
    |----------|-------------|
    | **&#8209;&#8209;complexity-borders** | Topic depth to consider steps as shallow, middle or deep. Default is 3 for shallow 7 for deep. |
    | **&#8209;&#8209;difficulty-borders** | Steps success rate to consider steps as easy, medium or hard. Default is 1/3 for easy 2/3 for hard. |
    | **&#8209;&#8209;filter-with-header-footer** | Filter steps with a header or footer. Default is True. |

5. [preprocess_users.py](preprocess_users.py) - add information about users level.

    **Required arguments:**
    
    | Argument | Description |
    |----------|-------------|
    |**users_path**| Path to .csv file with `users`. |
    |**preprocessed_users_path**| Path to .csv file where to save `preprocessed users`. If not provided `users_path` will be used. |

    **Optional arguments:**
    
    | Argument | Description |
    |----------|-------------|
    | **&#8209;&#8209;level-borders** | Passed topics count to consider user level as low, average or high. Default is 20 for low 150 for high. |

After all preprocessing stages you need to synchronize and compile all dataset. 

6. [compile_dataset.py](compile_dataset.py) - select subset of data which is presented in all datasets.

    **Required arguments:**
    
    | Argument | Description |
    |----------|-------------|
    |**submissions_path**| Path to .csv file with `preprocesssed submissions`. |
    |**steps_path**| Path to .csv file with `preprocesssed steps`. |
    |**topics_path**| Path to .csv file with `preprocesssed topics`. |
    |**users_path**| Path to .csv file with `preprocesssed users`. |
