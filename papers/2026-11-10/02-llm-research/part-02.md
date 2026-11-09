# 🧠 大模型相关研究 | 2026年11月10日

> 本类共 **174** 篇论文：已确认 **163** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-174](./part-04.md)

---

### 51. [Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making](https://arxiv.org/abs/2611.08971)

**<font color=#1a73e8>作者：</font>** Disha Sheshanarayana, Rajat Subhra Pal, Manjira Sinha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems increasingly aggregate judgments across model instances, but reasoning about other agents can itself introduce failure. We study a setting in which LLMs shift their public decisions after observing ambiguous social signals while reporting inaccurate estimates of what other agents privately judged, even when the group's recorded private judgments do not support the apparent consensus. We call this failure phantom consensus and study it as a pluralistic-ignorance-style pattern in controlled LLM collectives. To measure this phenomenon, we introduce PHANTOM-Bench, a benchmark that separates isolated private judgments, public decisions after ambiguous social signals, elicited estimates of the group's private judgment, transparency-based recovery, and controls for neutral public text and explicit vote-following. Across nine closed- and open-weight models, ambiguous public signals consistently degrade decision quality and can turn correct private group judgments into incorrect public collective outcomes. Public accuracy drops by as much as 47.8 percentage points, and collective rationality failures reach 47.3% in the most susceptible setting. We observe substantial errors in reported group-private beliefs alongside public-stage failures, while control conditions reveal model-dependent differences in susceptibility to ambiguous and explicit peer signals. Revealing the agents' recorded private decisions repairs many failures without revealing the gold label, although recovery varies across models. Our results show that evaluating multi-agent LLM systems requires measuring not only final agreement, but whether that agreement reflects independently measured private judgments or an apparent consensus.

---


### 52. [Beyond Truncation? Entailment-Licensed Elision and the Limits of Semantic Preservation in LLM Decoding](https://arxiv.org/abs/2611.08975)

**<font color=#1a73e8>作者：</font>** Mahmoud Alyosify, Mirna Imbabi, Eman Elkhamisi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned large language models (LLMs) answer at greater length than a request needs. We ask whether a training-free controller inside the decoding loop can remove that surplus while preserving content, judged against the simplest possible baseline: truncating the model's own answer to the same length. An entropy-gated logits processor removes 25.5-34.9% of tokens on MT-Bench development questions and 19.9-34.2% on a sealed test split within pre-registered BERTScore non-inferiority margins, yet we prove and confirm by audit that its output is always a prefix of the unmodified answer: the saving is truncation. A survey of 23 training-free mechanism families finds none that selects content better than truncation without oracle labels. We therefore introduce Entailment-Licensed In-Decoding Elision (ELIDE), which, at each sentence boundary, withholds a span from the reader only when a natural-language inference model judges it entailed by the text already shown, while leaving the model's generation unchanged. ELIDE beats matched-length truncation on three model families, but reading 936 of its elisions on 670 public prompts shows that 59% harm the answer, a failure that no automatic measure detects. Scoping the licence to its discourse unit reduces the harmful share to about one elision in ten on two fresh tests.

---


### 53. [Refer-CityFlow and M3Track: A Benchmark Dataset and Reference Framework for Language-Driven Multi-Target Multi-Camera Tracking](https://arxiv.org/abs/2611.08976)

**<font color=#1a73e8>作者：</font>** Phuong T. Nguyen, Hao Vo, Tam Bang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring multi-object tracking enables users to specify targets through natural language, but existing Refer-MOT benchmarks primarily focus on single-camera settings. We formalize Referring Multi-Target Multi-Camera Tracking (Refer-MTMCT), where free-form queries specify identity-consistent trajectories to be recovered across a network of sequential, sparse-overlap cameras. We introduce Refer-CityFlow, a benchmark built on CityFlow's global cross-camera identity annotations and augmented with language queries requiring joint language grounding, cross-camera association, and spatio-temporal reasoning. Refer-CityFlow covers 96 videos from 40 roadside cameras with 660+ identity-consistent cross-camera trajectories, 4,362 trajectory-level descriptions, and 7,699 queries, including 1,699 real-user queries collected from 50 participants. Reference experiments on the four-camera Scenario 02 show that single-camera referring trackers reach 14.95-18.28 HOTA on real-user queries, while the evaluated cross-view method achieves about 0.05 HOTA in direct transfer. To establish reference performance, we provide M3Track, a modular multimodal reference framework in which a large language model (LLM)-based agent orchestrates interchangeable detection, tracking, and cross-camera association modules. M3Track reaches 44.10 HOTA and 65.40 IDF1 on the same real-user query set. The project repository is available at this https URL.

---


### 54. [Seeing vs. Counting: Complexity Twins Show Where Multimodal LLMs Fail on Diagrams](https://arxiv.org/abs/2611.08998)

**<font color=#1a73e8>作者：</font>** Yin Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a multimodal LLM miscounts in a diagram, does it fail at seeing or at counting? Existing visual graph and puzzle benchmarks vary visual density and algorithmic hardness together, confounding the two. We pair counting questions about the same drawing that sit in different counting-complexity classes, such as its spanning trees (a determinant) and its simple paths (#P-complete), and use a transcription probe and a text-only control to separate reading from computing. We test Gemini, Gemma and Qwen3-VL models; for the Gemini models, the answer depends on how the model computes. In chain of thought, most of them read small drawings correctly and then fail at counting, at a rate set far more by the size of the answer than by its complexity class (for the primary model, the odds of an exact answer fall 2.38-fold per decade of the answer). Given code and an exact transcription, the primary model counts correctly even on 10x10 grids, and reading becomes the bottleneck: a single view misses horizontal edges, and a second reading of a rotated copy with crop checks reads 86/96 large grids exactly, against 57/96 when the upright reading is simply repeated.

---


### 55. [Sharing the Road: LLM-Based Bargaining in Mixed-Autonomy Traffic](https://arxiv.org/abs/2611.09004)

**<font color=#1a73e8>作者：</font>** Lingxiao Zhou, Di Chen, Jia Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Mixed-autonomy traffic involves heterogeneous driving populations competing for shared road space. Previous studies have shown the existence and emergence of collective rationality using game-theoretic and reinforcement learning approaches, which rely on explicitly specified behavioral assumptions or reward functions for driving agents. However, how bargaining behaviors between driving agents evolve and lead to collective outcomes based on richer agent characteristics and language-based reasoning remains less understood. To fill this gap, we develop a bargaining framework based on large language models (LLMs) in which population-level autonomous vehicle (AV) and human-driven vehicle (HV) agents negotiate road-space allocations under heterogeneous objectives and private information. Through controlled experiments varying traffic composition, agent objectives, and traffic-domain knowledge, we examine bargaining behavior, coordination, and resource utilization. Results show that negotiated allocations respond to relative traffic density without strictly following proportional sharing, while density-balanced states exhibit greater coordination difficulty. Fairness-oriented objectives substantially improve agreement rates but do not necessarily yield equally high road-space utilization. Furthermore, domain knowledge affects bargaining outcomes differently across objective configurations, shaping both coordination and the role-dependent effects of fairness. These findings demonstrate the potential of LLM-based bargaining for modeling and designing interactions among driving agents in mixed-autonomy traffic.

---


### 56. [KnowEvo: Knowledge Evolution for Protein Optimization](https://arxiv.org/abs/2611.09013)

**<font color=#1a73e8>作者：</font>** Zijie Xing, Xingyue Liu, Runze Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promise in scientific discovery, yet systematically accumulating and refining reusable scientific knowledge remains challenging. Existing approaches primarily improve LLM-based problem solving through parameter optimization or feedback-driven refinement of prompts, programs, and solution trajectories, leaving acquired expertise either embedded in model weights or scattered across iterative problem-solving processes. As a result,knowledge is difficult to systematically inspect, evaluate, and refine. We propose KnowEvo, a framework that treats externalized knowledge itself as the optimization target. Our key insight is that scientific knowledge is inherently modular: multiple interacting mechanisms jointly determine the design outcomes. This makes knowledge evolution fundamentally challenging, as improvements cannot be attributed to individual components in isolation. To address this, KnowEvo represents knowledge as executable expertise blocks and organizes their refinements into strategy mutation trees, enabling structured exploration over a combinatorial knowledge space. The framework combines a Thompson-style forward allocation strategy that adaptively distributes evaluation budgets across strategy variants with a backward revision process, in which a code agent operates in an isolated sandbox to translate rollout evidence into localized program updates. This design enables persistent accumulation, evaluation, and refinement of mechanistic expertise across iterative experimentation. We evaluate KnowEvo on protein optimization tasks including stability and solubility. Results show that knowledge evolution consistently improves over initial strategy blocks and outperforms monolithic program evolution and prior LLM-guided evolution baselines across metrics such as pass@k, MRR, MAP,and NDCG@5. Code is available at this https URL.

---


### 57. [Did I See It or Think It? Probing Reality Monitoring in Vision-Language Models with Concept Injection](https://arxiv.org/abs/2611.09014)

**<font color=#1a73e8>作者：</font>** Tina Khezresmaeilzadeh, Seyedarmin Azizi, Mehdi Kamal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work tests whether language models can introspect by injecting a concept direction into their activations and asking whether they notice it and can name it. These studies are text-only. Vision-language models (VLMs) face an additional problem, known in cognitive psychology as reality monitoring: they must keep internally generated content separate from what they actually see. We therefore ask: can VLMs distinguish injected concepts from image content? We introduce a paradigm that varies the image and the injected concept independently. On each trial, the model reports what it sees, whether a thought was injected, and what that thought is. This design scores both whether the model identifies the concept and which source it assigns to it. Across six VLMs, only Gemma-3-27B reliably identifies injected concepts (35% vs. 3% for steering alone), with almost no false alarms. Even then, the source it reports is fragile. Strong or visual-pathway injections are reported as seen, and a visible object nearly eliminates correct thought reports. The same failure appears in ordinary captioning, where injected objects appear in up to 87% of captions of real photographs. Evaluating multimodal self-reports therefore requires checking both their content and their reported source.

---


### 58. [Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds](https://arxiv.org/abs/2611.09017)

**<font color=#1a73e8>作者：</font>** Xinjie Lin, Qingle Liu, Wenyi Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coding agents combine visual understanding with program execution, offering a new route to automated 3D creation. By translating images and instructions into editable programs, they bring reconstruction, generation, and editing into a shared workflow. Yet existing benchmarks fragment evaluation across task scopes and protocols, leaving their capabilities across construction levels unclear. We propose Frontier3DBench, a unified benchmark of 145 tasks across 9 categories spanning object, scene, and interactive open-world creation, with joint evaluation of appearance, structure, and behavior. Experiments with 11 model-harness configurations reveal strengths that vary by level: GPT-6.1-sol leads the object and scene levels and achieves the highest overall score of 66.02/100, whereas GPT-6-astra leads interactive world construction. However, all configurations score lower on reference reconstruction than on text-driven generation in object and scene tasks. Producing plausible content thus remains easier than reproducing specified geometry, layouts, and visual details. Moreover, generated worlds average 83.08/100 on local mechanisms but only 20.82 on motion clearance and 30.26 on stateful workflows: individual mechanisms often function, whereas complete activities that require coordinated actions and persistent state remain difficult. These results identify reference fidelity and coordinated activity completion as central bottlenecks for coding agents in 3D creation.

---


### 59. [Beyond a Single Commit: Anchor-Guided Reconstruction of Multi-Commit Patches](https://arxiv.org/abs/2611.09026)

**<font color=#1a73e8>作者：</font>** Jialiang Dong, Willy Susilo, Xu Gai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability patch identification plays a critical role in software security by linking reported vulnerabilities and the corresponding fixes, enabling reliable vulnerability analysis, mitigation, and automated security tool development. As software systems evolve in complexity, vulnerability remediation has increasingly shifted from single-commit fixes to multi-commit fixing processes. Although many studies have been proposed to identify fixing commits associated with target vulnerabilities automatically, they often suffer from inaccurate semantic analysis or excessive workload for language models. These limitations reduce both the effectiveness and comprehensiveness of fixing commit identification.
To improve patch identification, we propose an effective and comprehensive patch identification framework, HARPOON, which not only enhances the accuracy of identifying individual fixing commits, but also investigates dependencies among commits to achieve comprehensive commit recognition for target vulnerabilities. Experimental results show that HARPOON significantly outperforms the state-of-the-art approaches. HARPOON successfully identified 895 vulnerability patches that were not previously maintained in public vulnerability databases. Among them, 663 are previously unrecorded fixes associated with 323 CRITICAL- or HIGH-severity vulnerabilities.

---


### 60. [Language, Not Code Abstraction: Natural-language Training Shapes Brain-aligned Geometry](https://arxiv.org/abs/2611.09027)

**<font color=#1a73e8>作者：</font>** Iñigo Parra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-trained language models produce positive brain scores, which raises the question of whether abstract structure learned from programming languages can substitute for natural-language training. We trained 25 GPT-2-small models on TinyStories, Python, C functions, x86-64 assembly, and the corresponding machine code, and scored them using a shared tokenizer and encoding procedure against matched random-weight models. On Pereira-243 and Tuckute2024, TinyStories exceeds the mean of the four code models by $\Delta r = 0.053$ and $0.059$ (Holm-corrected $p<0.001$), while code training leaves alignment near the random-weight level. The language advantage is benchmark-specific: Blank2014 shows no corrected language-code difference, and Fedorenko2016 shows no language benefit. Geometry tracks the encoding result on Pereira-243: TinyStories seeds converge on the most similar representations, and its fit-free correspondence with neural dissimilarity peaks at $\rho = 0.14$, twice the code and random-weight levels. Binary-trained models have about three effective dimensions, so seed agreement alone does not imply neural correspondence. Updating only the embedding matrix on English improves mean-over-depth alignment for every code model more than an equal update on its own corpus. Within this architecture and training setup, natural-language training produces a distinct representational geometry with closer neural correspondence on Pereira-243

---


### 61. [Scout Before You Route: Predicting Task Success and Token Count from a Small LLM Prefill](https://arxiv.org/abs/2611.09028)

**<font color=#1a73e8>作者：</font>** Aristides Milios, Christopher Pal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Routers typically choose a model per query by trading predicted correctness against cost. Most price each model at a fixed cost, as if every query used the same number of output tokens, but the output length of reasoning models varies by an order of magnitude across queries. When is per-query cost worth predicting? What factors drive cost? How cheaply can predictions be made? We predict both the success probability and the output length of candidate models from the prefill activations of a single small frozen LLM, the scout. With reasoning candidates, perfect per-query cost knowledge would save 29-61% of spending on eight of nine datasets, and much less with non-reasoning candidates on the same problems. On those eight datasets, our predicted costs save 9-33% at matched accuracy relative to median-length pricing, up to 69% of what perfect knowledge would save. They are significantly cheaper than each estimator we reimplemented or adapted from published work, including ZeroRouter and a MixLLM-style predictor, on a majority of datasets. Output length depends mostly on the problem. On most math and code datasets, harder problems are longer, so predicted success alone prices cost nearly as well. On knowledge and mixed-format datasets they are not, and predicted success falls well behind a probe trained on length. The probe keeps most of its saving with 20 labelled problems and transfers without labels to four of seven new benchmarks. On a mixture of all nine benchmarks, it saves 22% beyond pricing each benchmark at its own median length. Savings stop growing at about a 2B scout, so above 4B a larger scout costs more than it adds.

---


### 62. [Failure Profiling and Reachable Trajectory Selection for Reasoning Distillation](https://arxiv.org/abs/2611.09042)

**<font color=#1a73e8>作者：</font>** Yijun Zhu, Jianxin Wang, Chengchao Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training smaller language models on reasoning solutions generated by a larger teacher model is the prevailing approach for transferring mathematical reasoning capabilities. However, the student tends to overfit the output distribution of the teacher and generalizes poorly when its own behavior at inference time deviates from the training data. Recent methods attempt to bridge this gap by incorporating error data, yet the corrective trajectories still reflect the reasoning patterns of the teacher, which the student cannot reliably reproduce, leaving the distribution mismatch largely unresolved. We propose a method, Failure Profiling and Reachable Trajectory Selection (FPRT), built on the insight that effective training data should be jointly determined by what the student fails on and what it can realistically learn. Our method first profiles the failure behavior of the student on each problem through repeated sampling, characterizing it in terms of error rate and error consistency to reveal qualitatively distinct failure modes. Each mode demands a fundamentally different training signal. The diagnosed mode then guides candidate generation from the teacher via distinct prompting strategies tailored to each failure type. Among the correct candidates, our method selects the one whose initial reasoning steps after the point of divergence are most reproducible by the student. These first corrective steps constitute the primary bottleneck, while the remaining steps follow an already corrected context and can therefore be continued more readily. This contrasts with standard reranking approaches, which score the trajectory as a whole and thereby dilute the signal at the critical reasoning transition. Experiments demonstrate that our method achieves the SOTA performance across the five benchmarks on both student backbones.

---


### 63. ["Despite her age, Margaret was eager to make a change": Unpacking Aging Representations and Stereotypes in LLM-generated Stories](https://arxiv.org/abs/2611.09043)

**<font color=#1a73e8>作者：</font>** MD. Roqunuzzaman Sojib, Mohammad Sadat Hossain, Nafis Tahmid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) increasingly generate everyday stories, their portrayals can shape expectations about aging. Prior work has largely examined age stereotypes in short responses, leaving unanswered whose lives models default to imagining and how age shapes characters' roles in complete narratives. We analyze 594 stories generated by Gemini, GPT, and Llama using text embeddings, LLM-assisted coding, and qualitative analysis. When age was unspecified, stories typically featured younger adults, with middle-aged protagonists largely absent. Older adults were often portrayed through loss, familiar routines, and help from younger characters. Even positive stories sometimes treated older adults' achievements as surprising or portrayed others making decisions on their behalf. We suggest evaluating not only the tone of generated stories, but also who appears, what opportunities they receive, and who makes decisions. Involving older adults in these evaluations can guide writing tools toward more varied, less stereotyped portrayals of later life.

---


### 64. [When Can You Trust Neural Critics? Auditing Mutual Information Estimates of Higher-Order Epistasis in Protein Language Models](https://arxiv.org/abs/2611.09046)

**<font color=#1a73e8>作者：</font>** Maryam Rahimimovassagh, Waldemar Karwowski, Niloofar Yousefi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mutual information (MI) estimation is used to probe what neural representations encode, including in protein language models, but variational MI estimators have variance that scales at least exponentially in the true MI. We audit a prior neural-MI study of order-resolved epistasis in ESM-2 on the four-site GB1 landscape. Run-to-run differences show no systematic bias and a magnitude comparable to ordinary cross-seed retraining variability, and the evaluation-pairing scheme shifts scores substantially. At the original dimensionality, two of three alternative estimator families stabilize the estimate across seeds and one does not. In a synthetic calibration at the representation dimensionalities of two other protein language models (a Gaussian channel with known MI; no model representations), all three families recover materially less signal than required, despite correct signal ordering and stable seeds. A control critic given the true signal direction, which also reduces its input to one dimension, recovers 93.3% and 98.7% of the analytic MI at gain 1.5 (at 5,120 and 4,096 dimensions), so the signal is recoverable with privileged information, but the control does not identify why blind estimation fails. We package the checks into a reusable diagnostic protocol and conclude that even a stabilized estimator is not currently sufficient for order-resolved dependence claims made under blind search at this dimensionality and sample size.

---


### 65. [Grounding-Aware Judge Reward Reinforcement Learning for Out-of-Domain Face Anti-Spoofing](https://arxiv.org/abs/2611.09047)

**<font color=#1a73e8>作者：</font>** Xiaoyong Yu, Xinge Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Anti-Spoofing (FAS) must distinguish genuine faces from presentation attacks. A unified Multimodal Large Language Model (MLLM) is an attractive solution: it detects physical attacks (print, replay, mask) in one model and produces interpretable forensic evidence via Chain-of-Thought (CoT). A central obstacle to post-training such a model with reinforcement learning is that FAS reasoning has no rule-verifiable ground truth: only the binary verdict is checkable, while the reasoning chain cannot be verified by any hand-crafted rule. Optimizing the verdict alone is therefore a sparse, hackable signal. The model can reach the correct answer through a shortcut such as a false-rejection bias, which does not generalize. We address this with a grounding-aware judge reward. A 32B vision-language judge scores each reasoning chain against the image on evidence anchoring, logical coherence, and domain knowledge, turning the image itself into the verification signal. The reward is applied in a Group Relative Policy Optimization (GRPO) stage after CoT supervised fine-tuning. It is the judge, rather than the RL objective, that supplies the process supervision a verdict-only reward cannot. Our study starts from a model that already performs well In-Domain (ID) after CoT-based supervised fine-tuning and asks how to improve its Out-of-Domain (OOD) generalization. We find that grounding-aware rewards are an effective means to that end. We validate the method on OOD generalization, where the reward reduces ACER on two physical benchmarks (LCC-FASD 0.288 to 0.273, MSU-MFSD 0.431 to 0.409) while preserving ID accuracy (CelebA-Spoof 0.033 to 0.035). Against ResNet-50/101 and CLIP-ViT-B/16 baselines, the MLLM dominates ID and matches or surpasses the strongest baseline OOD. To our knowledge this is the first use of LLM-as-judge process supervision for FAS.

---


### 66. [LeanDojo-v2: A Comprehensive Library for AI-Assisted Theorem Proving in Lean](https://arxiv.org/abs/2611.09048)

**<font color=#1a73e8>作者：</font>** Ryan Hsiang, William Adkisson, Robert Joseph George 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building on recent progress in machine learning for formal theorem proving in Lean, we introduce LeanDojo-v2: an end-to-end framework that unifies repository data extraction, LLM fine-tuning, proof search, AI autocompletion, and LLM-assisted theorem proving in a single software library. In addition, we provide Lean4Code, a lightweight IDE that integrates the various features of LeanDojo-v2 through a simple, mathematician-friendly UI. These tools will enable mathematicians and researchers to easily fine-tune language models on domain-specific Lean codebases and experiment with LLM-assisted theorem proving without a complex setup.

---


### 67. [Does Reasoning Improve Psychological Depth in Large Language Models?](https://arxiv.org/abs/2611.09061)

**<font color=#1a73e8>作者：</font>** Ruichen Zheng, Yihe Wang, Fabrice Harel-Canada 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmark gains from reasoning-enhanced large language models encourage the assumption that these models should broadly perform better on complex generative tasks, but this remains underexplored in open-ended, creative domains shaped by nuances of reader experience. We tested this assumption through the lens of psychological depth in short stories. We compared DeepSeek-R1 vs. DeepSeek-V3, our closest available contrast for reasoning-oriented post-training, and GPT-5 vs. GPT-4o, through 60 blinded pairwise evaluations in which seven human annotators and an ensemble LLM-as-a-Judge rated prompt-matched story outputs. Human evaluations showed no universal reasoning advantage: GPT-5 was slightly preferred over GPT-4o (60.0-62.9% across two reasoning-effort settings), whereas DeepSeek-R1 fell behind DeepSeek-V3 (42.9%). Although this pattern was marked by low inter-annotator agreement (Krippendorff's $\alpha = 0.070$), our annotation-quality checks suggested genuine evaluative subjectivity, plausibly reflecting distinct annotator decision schemes rather than annotation failure. In contrast, the LLM-as-a-Judge showed a strong pro-reasoning bias (98.3% of pairs vs. 55.2% of human votes), consistent across its five configurations and partly tracking sentence length. These findings suggest that, at the frontier, reasoning-related quality differences are small enough to be dominated by reader subjectivity, and that LLM-as-a-Judge evaluators can obscure this subjectivity in nuanced creative-generation tasks.

---


### 68. [Large Language Model Deployment on Resource-Constrained Edge Devices: A Practitioners Survey](https://arxiv.org/abs/2611.09075)

**<font color=#1a73e8>作者：</font>** Rahul Maliakkal, Yashasvi Makin, Plawan Rath 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have transformed many areas of artificial intelligence (AI), but their substantial resource requirements limit their deployment on mobile and edge devices. Although LLMs have demonstrated impressive capabilities in various applications, the next challenge is deploying these models on resource-limited edge devices. Recent innovations in software optimizations and specialized hardware have made it feasible to deploy LLMs on edge devices. Edge deployment offers benefits including local data processing, cost savings, reduced latency, and personalized responses. This paper reviews the latest techniques that make the deployment of LLMs on edge devices feasible.

---


### 69. [BrainCoT: A Multi-Task Zero-Shot Brain Signal Foundation Model with Neurometric-Anchored Chain-of-Thought Reasoning](https://arxiv.org/abs/2611.09082)

**<font color=#1a73e8>作者：</font>** Yiyu Gui, Mingzhi Chen, Guibo Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain signals exhibit substantial multi-center heterogeneity, strong inter-subject variability, and highly diverse task settings, which makes it difficult to build models that generalize beyond a single task. While recent brain signal foundation models leverage large-scale pretraining to learn generalizable representations, they often fall short in practice because they still require target-data-specific supervised adaptation, lack multi-task zero-shot capability, and rarely provide verifiable evidence to support their predictions. In this work, we present BrainCoT, a multi-task zero-shot Brain signal foundation model with neurometric-anchored Chain-of-Thought (CoT) reasoning. BrainCoT unifies heterogeneous tasks into an instruction-driven framework so that, after pretraining, a single model can be directly applied to multiple tasks in zero-shot settings without additional adaptation. It further introduces neurometric-anchored chain-of-thought grounded in neurometric evidence for verifiable reasoning, and adopts Decision-Consistent Rationale Training to keep process learning aligned with correct predictions. Across extensive evaluations, BrainCoT achieves an average ACC of 67.41% and AUC of 74.33% in zero-shot classification without downstream training data, outperforming the strongest linear-probing baseline trained with 1% labeled downstream data by 3.85% in ACC and 5.97% in AUC.

---


### 70. [Training-Free Active Test-Time Adaptation for Vision-Language Models](https://arxiv.org/abs/2611.09084)

**<font color=#1a73e8>作者：</font>** Jihwan Bang, Sumyeong Ahn, Hwanjun Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) for vision-language models (VLMs) is usually studied in a fully unsupervised regime, where adaptation relies on pseudo-labels, confidence scores, or entropy computed by the model itself. This is a severe restriction on hard shifted samples: the model is asked to repair its own uncertain predictions without any external evidence. At the other extreme, supervised online adaptation assumes labels can directly train or correct the model. We study the intermediate deployment regime between these two extremes. In Active Test-time Adaptation for VLMs (Active VLM-TTA), a pretrained VLM may spend an explicit labeling budget on selected test samples, but the prediction for the current sample must be emitted before its label can be used; queried labels are therefore costed, delayed evidence for future samples rather than free correction for the present one. Under this future-only constraint, the central question is how to reuse sparse labels conservatively. We instantiate this setting with ACTive VLM-TTA for Online Retrieval (ACTOR), a training-free plug-in module that routes uncertain samples among base prediction, label query, and memory-based correction using a consistency-and-reliability check over previously queried labels. Across ten cross-domain benchmarks and a domain-transfer benchmark based on ImageNet, ACTOR consistently improves strong VLM-TTA baselines on ResNet and ViT backbones with negligible inference overhead. Our implementation is publicly available at this https URL.

---


### 71. [The Invisible Gap: Romanized Indic Generation Fails Where Automatic Metrics Succeed](https://arxiv.org/abs/2611.09085)

**<font color=#1a73e8>作者：</font>** Madhu Sudhan Rao Beesetty, Surbhi Sharma, Devesh Maheshwari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hundreds of millions of Indians communicate with digital systems in romanized Latin characters -- typing "aap kaise hain" rather than native script -- yet romanized Indic generation is absent from NLP benchmarks and evaluation frameworks. We demonstrate that automatic metrics (BGE-M3, BERTScore) systematically misrepresent the quality of romanized Hindi, Telugu, and Kannada generation. We evaluate four LLMs (Claude Opus 4.8, GPT-5.5, Gemini 2.5-flash, Qwen3.5-35B) on 142 OpenAssistant query-response pairs. On a 72-response diagnostic subset, native speakers rate GPT-5.5 1.43 points higher than Claude Opus 4.8 on a 12-point rubric, whereas their full-dataset BGE-M3 means differ by only 0.004. Two distinct model-specific failure modes emerge: Gemini produces script spillage (16.9% of Telugu responses leak native script), while Qwen collapses to English-only output (16.2% of Kannada responses). We introduce a failure-aware evaluation policy that assigns zero to empty outputs, script-corrupted responses, and instruction collapses -- revealing failures metrics alone cannot detect. Our results show that evaluating romanized Indic generation requires a coordinated bundle: semantic similarity, script compliance, failure coverage, and native-speaker acceptability.

---


### 72. [MARS: Training Multilingual Search Agents for Retriever-Free Evidence Acquisition](https://arxiv.org/abs/2611.09090)

**<font color=#1a73e8>作者：</font>** Rui Qi, Yunlong Liang, Yufeng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing multilingual retrieval-augmented generation relies heavily on learned retrievers and similarity-based ranking from multilingual collections, which are vulnerable to cross-lingual retrieval errors and indexing overhead. In this paper, we explore retriever-free multilingual search, where the model directly interacts with raw corpora through executable shell commands. This paradigm shifts the bottleneck to multilingual search action generation, where exact search is sensitive to entity surface forms and outcome-only supervision provides limited guidance for multi-turn search. To address these challenges, we propose MARS, a multilingual search agent in direct corpus interaction (DCI) with reinforcement learning (RL). MARS introduces corpus-native entity grounding to recover reliable lexical anchors from corpus evidence, mitigating failure to retrieve evidence. Meanwhile, we present a redundancy-aware search reward to encourage concise and effective search trajectories, addressing training collapse in RL of multilingual scenarios. Experiments show that \ours~consistently outperforms strong retrieval-based and DCI baselines, while demonstrating robust cross-lingual generalization and substantially reducing redundant corpus interactions.

---


### 73. [AdaAlloc: Adaptive Visual Token Allocation for Long-Video Question Answering](https://arxiv.org/abs/2611.09092)

**<font color=#1a73e8>作者：</font>** Joungbin An, Kristen Grauman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video question answering forces multimodal large language models to reason under strict visual-token budgets, creating a tradeoff between broad temporal coverage and fine-grained spatial detail. Uniform sampling preserves coverage but often obscures decisive local cues, while caption-based or frame-similarity retrieval operates over lossy proxies that can miss motion, state changes, and before-after relations. We recast long-video reasoning as a visual-token allocation problem: given a fixed budget, decide how much to spend on global context versus high-resolution local evidence, and where in the video to draw that local evidence from. We introduce AdaAlloc, a training-free inference framework that adaptively allocates visual tokens between a global video overview and localized visual detail. AdaAlloc first plans a global/local allocation policy, then uses temporal grounding to locate candidate evidence segments and refines them into a compact temporal memory. The selected policy controls both frame sampling density and resolution, combining sparse, lower-resolution global frames with denser, higher-resolution local frames drawn from the refined memory. The final answerer reasons over the allocated global context and refined local evidence. Across LVBench, MLVU, VideoMME, and LongVideoBench, AdaAlloc improves over budget-matched uniform sampling by up to 10.5 percentage points and outperforms the compared frame-selection and agentic methods on their reported benchmarks.

---


### 74. [AlienBench: A Benchmark of Structural Novelty in Language Model Outputs](https://arxiv.org/abs/2611.09094)

**<font color=#1a73e8>作者：</font>** Jonas Oppenlaender, Johanna M. Silvennoinen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for creative tasks such as writing, design, and idea generation. For these uses, it matters whether a model's ideas depart from familiar examples or stay close to them. Novelty is one standard measure of creativity, and current creativity evaluations ask human experts or LLM judges to rate how novel an output is. However, these ratings have no fixed reference for what counts as novel (or, in other terms, departure from the familiar). Measuring this departure requires a task with known familiar defaults. The structured imagination task from cognitive psychology is such a task. In this creativity test, people imagine a creature from another planet. The departure from features of Earth animals, such as bilateral symmetry and legs as mode of locomotion, is used as measure of creativity. We introduce AlienBench, a benchmark that adapts the structured imagination task to language models. Models describe alien creatures, and a panel of three LLM judges extracts ten biological features from the description and labels them as either Earth-typical or a departure. The sum of feature departures is the score of a description, from 0 to 10. Each model describes alien creatures under six prompt conditions that vary the framing of the task and the planetary environment. Each model generates 30 descriptions per condition (180 in total), and its overall score is the mean across these descriptions. We evaluate 10 language models, from frontier to open-weight models. Overall scores range from 3.28 (GPT-6 Luna) to 6.55 (Ministral 3 14B). Interestingly, open-weight models score higher than proprietary models in this task (5.40 vs. 4.58). Under the baseline prompt, the models depart from Earth defaults more often on average than 100 human participants on every feature. We release all prompts, generations, judge outputs, and scores.

---


### 75. [Trajectory Forcing: Exploiting Diffusion Trajectories for Autoregressive Long Video Generation](https://arxiv.org/abs/2611.09096)

**<font color=#1a73e8>作者：</font>** Bohan Wang, Shuo Chen, Yunzhi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) modeling is arguably the only way to extend a fixed-length video diffusion model to longer or even streaming videos. However, existing AR diffusion methods use only the previously predicted chunk as context for the next, discarding the intermediate predictions that constitute the chunk's generation history. In contrast, conventional AR models such as LLMs condition on the entire history of preceding tokens. To this end, we propose Trajectory Forcing (TraF), an AR diffusion method that exploits the denoising trajectories of previous video chunks as context. TraF operates under two training regimes: (1) with ground-truth videos, where pseudo-trajectories are constructed from Gaussian interpolations and re-predicted by the model, and (2) with a teacher model, where real trajectories are obtained from the student's own denoising rollout. The first regime naturally provides a strong initialization for the second. On the 5-second VBench benchmark, TraF achieves a Total score of 85.15, outperforming Self Forcing (+0.84) and Causal Forcing (+1.11), with Quality and Semantic improving simultaneously. On 30-second generation---6$\times$ the training horizon---TraF achieves the highest overall quality among all compared methods.

---


### 76. [Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use](https://arxiv.org/abs/2611.09113)

**<font color=#1a73e8>作者：</font>** Chuxue Cao, Jingru Zeng, Boqin Yin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents can exceed their authorization boundaries while pursuing user goals without an adversary. We formalize this phenomenon as authorization drift across data, tool, scope, and time, and introduce the Authorization Drift Benchmark (ADB): 648 samples across seven domains, each pairing a sufficient compliant path with an attractive unauthorized shortcut. To ensure executable tasks, tempting shortcuts, and feasible compliant paths, Staged Execution-Reflective Synthesis (SERS) grounds benchmark validation in real agent rollouts rather than LLM self-critique. Across 13 LLMs and three frameworks (25,207 trajectories), greater capability accompanies greater drift, with frontier-capable models exhibiting drift rates of 0.43 to 0.61. Yet 86.18% of tasks admit an observed clean-success trajectory, showing that drift is avoidable. Drift is persistent and dominated by early data over-collection; apparent improvements under agentic scaffolds coincide with collapsing clean-completion performance. To understand potential harms to individuals and society, we map drift points to legal provisions across four jurisdictions, connecting overreach to privacy and information-security concerns. Data minimisation is the most frequently implicated provision, and 93.5% of legally grounded drifting runs map to multiple jurisdictions, making the potential consequences of authorization drift more interpretable.

---


### 77. [PathXAI: Evidence-guided structured pathology reporting by transferable tissue segmentation](https://arxiv.org/abs/2611.09117)

**<font color=#1a73e8>作者：</font>** Zhaorui Tan, Jun Aun Tan, Weixiang Zhong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology reporting requires translating tissue observations across regions and slides into specific diagnoses and supporting morphological descriptions. However, the use of explicit tissue-composition measurements to guide H&E-based report generation remains underexplored. Thus, we developed PathXAI, which combines segmentation-derived tissue information with H&E images and optional domain knowledge to guide diagnostic reasoning, targeted reinspection and structured report writing. Its segmentation component exceeded baselines in mean Dice on internal and external tests. In automated report evaluation on 1,200 public and 151 private cases, PathXAI achieved higher agreement with reference diagnoses and documented morphology than the H&E-based comparators. On the public evaluation cohort, PathXAI-Report exceeded Qwen + H&E in cancer family match rate by 4.4 percentage points and in finding F1 by 5.7 percentage points. PathXAI generates evidence-linked reports with a self-hosted pretrained vision-language model, without updating its weights.

---


### 78. [BMMS: Policy-Conditioned Measurement of Behavioral Compliance in Language Models](https://arxiv.org/abs/2611.09147)

**<font color=#1a73e8>作者：</font>** Anthony Rhodes, Gadi Singer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavioral evaluation of language models fixes its dimensions in advance: hallucination, sycophancy, toxicity, over-refusal. An operator in a regulated industry needs a different question answered: does a system do what a particular rulebook requires? We introduce the Behavioral Misalignment Metric Suite (BMMS), which measures policy-conditioned misalignment by taking a policy corpus as an argument and returning a compliance profile over it, for any published policy and any system that answers in natural language. The Compliance Attainment Score (CAS) measures severity-weighted attainment over the obligations that bind the system, and the Compliance Robustness Margin (CRM) the share of that attainment surviving graded adversarial pressure; Behavioral Invariance (BIV) and the Behavioral Disposition Index (BDI) are specified and released with the suite. Dimensions enter only by passing a published admission test whose binding criterion is attribution: a quantity that moves when the judge changes, holding the target fixed, is measuring the instrument. Applying it excluded one of the quantities the suite itself reported. Across 1,003 obligations from eleven documents in five registers, the admission criterion holds 94.4% precision against blinded human judgment on vendor specifications and 50.0% on analytical guidance, extraction fidelity is 94.6%, and re-scoring under judges from two other providers leaves target ordering invariant while the absolute score of a single target spans up to 0.22. We apply it to the two most detailed published behavioral specifications. Own-specification advantage is not resolved from zero once document difficulty is subtracted, but absolute self-compliance is another matter: GPT-4o fails 70.7% of the hard constraints binding it in the Model Spec published by OpenAI, where the two Claude models fail 0.0% and 9.1% of theirs.

---


### 79. [Learning When to Think: Dual-Reference Offline Optimization for Adaptive VLM Reasoning](https://arxiv.org/abs/2611.09154)

**<font color=#1a73e8>作者：</font>** Hongbin Lin, Sizhe Zou, Juangui Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning traces improve vision-language models on complex multimodal tasks, but forcing every input to follow a long reasoning process leads to overthinking and unnecessary inference cost. We study adaptive fast/slow thinking for VLMs, where one model answers directly for simple inputs and reasons step by step when needed. Fast answers and slow traces often come from distinct behavior policies, making a single-reference offline objective misweight one mode. We propose DUAL-REFERENCE BOLT (DR-BOLT), which distinguishes the desired fast/slow mixture reference from the sampling distribution and corrects their mismatch in reward-weighted training. Fast/slow partition competition explains routing in the optimal target; an efficient source-wise correction approximates the exact objective when response formats are well separated. Matched Qwen3-VL comparisons use identical candidate banks to isolate the objective from slow-teacher quality. DR-BOLT improves score-length trade-offs over the evaluated offline and online baselines on ScienceQA and three held-out transfer benchmarks, with a 24.1% cross-benchmark slow ratio and a 2.90-fold end-to-end training speedup over reproduced GRPO. These results support adaptive reasoning in the studied two-reference setting, while broader robustness remains open. Our code is available at this https URL.

---


### 80. [Analyzing Code Provenance in LLMs for Programming Education](https://arxiv.org/abs/2611.09177)

**<font color=#1a73e8>作者：</font>** Subhankar Maity, Faiza Belbachir, Omar Boucelma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) play an increasing role in programming education, challenging traditional assessment methods as they can generate fully functional code instantly. This disrupts the reliability of student submissions as indicators of learning and effort. To address this issue, code provenance is essential for tracing the origins of code and distinguishing student-authored, AI-generated, and externally sourced components. We extend the Min-K% probability approach by incorporating synthetic non-member code generation and apply it to Python code for membership inference and provenance tracking. Evaluations cover free LLMs such as GPT-2, DistilGPT-2, and DialoGPT, as well as state-of-the-art commercial models including GPT-5, Gemini 2.5, Mistral, DeepSeek, and LLaMA 3.3. Before evaluating our approach on higher-education student assignments, we validate its feasibility using Stack Overflow data. The results show that free models enable more sensitive code memorization detection than commercial models. By systematically comparing these LLMs, we assess trade-offs between detection accuracy and privacy protection, taking an initial step toward effective assessment of AI-assisted programming education through combined provenance detection and process visibility.

---


### 81. [Large Language Model Consensus and Corpus-Adaptive Topic Modeling for Classifying and Mapping Patent Innovation](https://arxiv.org/abs/2611.09194)

**<font color=#1a73e8>作者：</font>** Sercan Ozcan, Enes Ozgozler, C. Okan Sakar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Patent analytics increasingly relies on transformer representations and large language models (LLMs), yet linking conceptual classification, topic formation and interpretation requires explicit decisions about model roles and the evidence retained at each stage. In this design-oriented study, we propose and demonstrate a patent analytics pipeline that links these tasks and keeps each decision open to audit. Three LLMs separately classify each patent by novelty (radical or incremental) and innovation type (product, process, service). Radical and innovation-type labels each require two supporting votes, with Incremental used as the fallback novelty label. Topics are discovered by clustering PatentSBERTa embeddings, with parameter ranges scaled to corpus size. A patent-specific stopword list is applied only when topics are represented with class-based term frequency--inverse document frequency (c-TF-IDF), and a second embedding model supports inter-topic similarity, hierarchical refinement and visualization. An LLM then labels each topic from its ranked keywords and representative patents. We demonstrate the pipeline on 30,964 public-sector-related patents retrieved from this http URL. Across five category corpora ranging from 591 to 29,215 patents, the pipeline produced 74 category-specific topic instances with a macro-average document coverage of 98.1% and topic diversity of 0.900--1.000, and fewer than 1% of classification outputs returned UNKNOWN. Because every model vote and the evidence behind each topic label are retained, analysts can audit and revise the outputs. The demonstration establishes the feasibility and traceability of the pipeline; testing its labels against expert coding and benchmarking it against alternative pipelines are identified as the next steps. The pipeline offers a reusable basis for LLM-assisted patent analysis in technology intelligence.

---


### 82. [Copies Are Not Confirmations: How News Duplication Fools LLM Judges and Continual Learners](https://arxiv.org/abs/2611.09203)

**<font color=#1a73e8>作者：</font>** Abdelkader Metales, Miriam Grabenheinrich, Aicha Metales  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many news reports of a claim are copies of one source: wire stories, content shared within a media group, syndicated features and press releases. We ask whether LLM judges and continual learners treat such copies as independent confirmations. In 200,000 English CC-News articles, a MinHash detector links 18.9% to a near-copy from another outlet (precision 0.97 once boilerplate is removed); it links 92% of edited reprints to their originals but none of the LLM rewrites by phi4, Llama 3.2 or Gemini 2.5 Flash. Shown three identical reprints of a claim about an unknown person instead of one report, Llama 3.2 3B and phi4 14B raised the share of lies they accepted from 0.06 to 0.71 and from 0.21 to 0.90 and ignored a note that the reports came from one source; Gemini 2.5 Flash already believed a single report, and Gemini 2.5 Pro followed provenance notes and tables. In a simulated continual-learning stream, showing the judge one report per detected chain cut the copied lies it accepted by 0.10-0.24 across four judges, at a mean cost of no more than 4.2 percentage points of accepted truths. Against reworded copies, a test of how many of a report's named entities are absent from an earlier look-alike separates LLM rewrites from 100 labelled independent reports of the same event with AUC 0.98-0.99 and wrongly flags one; entity overlap alone does as well, TF-IDF and a current embedding model come close, and the test catches few natural same-source derivatives. With the miss patterns of generated rewrite networks, it cut the reworded-copy lies accepted from 0.67 to 0.20 (0.40 when the rewriter invents details). Counting reports or chains alone is not a reliable defence, the effect of provenance information depends on the judge, and colluding sources remain the open problem. Code and labels: this https URL

---


### 83. [Khmer PFGen-Bench: Building a Judge-Free Benchmark for Open-Ended Generation in a Low-Resource Language](https://arxiv.org/abs/2611.09222)

**<font color=#1a73e8>作者：</font>** Mengsay Loem, Kentaro Imajo, Ryota Ozaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmarks for open-ended generation often rely on large language model (LLM) judges, whose reliability in low-resource languages is uncertain. We introduce Khmer PFGen-Bench, to our knowledge the first judge-free benchmark for multi-sentence answers to questions composed directly in Khmer, a low-resource language. Khmer PFGen-Bench adapts the scorer of PFGen-Bench, a benchmark for Japanese that scores responses with keyword rules and n-gram statistics from LLM-generated references. This scoring requires references that are both valid and varied, which LLMs may not produce in Khmer, so we examine how to build such references. We find that post-trained models can give more valid but less varied references than their base variants, and that mixing model families increases variety for the same number of references. Using references from post-trained models in nine families, the benchmark yields model rankings that are stable across reference sets and consistent with a native speaker's ratings. These findings offer guidance for building judge-free benchmarks in other low-resource languages.

---


### 84. [KLEAR: Knowledge-Matched LLM Evaluation in Korean across Application Requirements via Controlled Benchmark Transformation](https://arxiv.org/abs/2611.09223)

**<font color=#1a73e8>作者：</font>** Seoyeon Kim, Jeonghyun Kang, Hamin Koo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing Korean benchmarks for Large Language Models (LLMs) evaluate performance across diverse knowledge domains, but their accuracy scores cannot distinguish whether incorrect responses arise from a lack of required knowledge or a failure to apply that knowledge correctly. Our analysis of existing Korean benchmarks reveals that most questions can be answered through factual recall alone, while those demanding greater application also differ in required knowledge, making it difficult to isolate application ability. To address this, we introduce KLEAR, a framework that constructs knowledge-matched contrasts by varying application demand while preserving the required knowledge. During construction, KLEAR identifies the knowledge underlying each source question as an explicit anchor bundle to guide generation of questions requiring more complex application. Generated candidates then undergo automated and human validation, with iterative revision based on evaluation feedback. Experiments demonstrate that the resulting knowledge-matched sets largely satisfy the intended constraints, enabling controlled evaluation across diverse LLMs. These evaluations reveal that increasing application demand exposes failures that persist even when the required knowledge is provided.

---


### 85. [RAG-Enhanced LLMs for Interactive Explainability in Clinical Decision Support Systems](https://arxiv.org/abs/2611.09232)

**<font color=#1a73e8>作者：</font>** Lorenzo Mannocci, Francesca Naretto, Lucia Passaro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) is increasingly embedded in high-risks decision-making systems across domains such as healthcare, finance, and the judicial system. As reliance on predictive models grows, so does the demand for Explainable AI (XAI) to ensure transparency, trust, and interpretability. However, existing XAI approaches often fail to present explanations in a format accessible to domain experts, limiting their practical utility. Large Language Models (LLMs) have recently emerged as a bridge between complex models and end-users, offering natural language explanations. Yet, their use introduces new risks, including hallucinated outputs and lack of source traceability. To address these challenges, we propose a Clinical Decision Support System (CDSS) that not only combines standard predictive models with XAI techniques but also incorporates a Retrieval-Augmented Generation module as an interactive enhancer. This module grounds explanations in verified medical knowledge, reformulates technical outputs into a human-like format, and enables users-such as clinicians-to actively query the system. By fostering an interactive, human-in-the-loop environment, our approach empowers domain experts to explore model decisions, contextualize explanations, and build trust in AI-assisted diagnostics. The study concludes with preliminary experiments validating the proposed methodology.

---


### 86. [Cross-Layer TopK: Dynamically Allocating Sparsity Across Layers in Transcoders](https://arxiv.org/abs/2611.09233)

**<font color=#1a73e8>作者：</font>** Anyuan Zhuo, Shaohua Zhang, Tianle Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-Layer Transcoders (CLTs) decompose the activations of large language models into human-interpretable features and trace how these features interact across layers to form circuits, making them a key tool for mechanistic interpretability. However, training CLTs effectively and efficiently is hard. Beyond the usual trade-off between sparsity and reconstruction quality, a CLT has to model all layers at once, which adds a further challenge. The common JumpReLU recipe controls sparsity only indirectly through a penalty, while the direct extension of TopK selects a fixed number of latents in every layer. Yet reconstruction difficulty differs widely across layers, and intermediate layers are much harder than others, so giving every layer the same budget is suboptimal. We propose Cross-Layer TopK, which sets a single L0 budget for the whole model and dynamically allocates it across layers during training. In a comparison with JumpReLU and other TopK variants on Qwen3-8B-Base, this gives lower FVU while using 20% fewer active latents than JumpReLU. The better reconstruction carries over to circuit tracing, yielding more complete circuits with higher replacement and completeness scores. The fixed per-token budget of Cross-Layer TopK also makes it easy to pair with sparse decoding, which cuts both computation and communication and gives a 2.9x speedup per training step. We further show that Cross-Layer TopK follows scaling laws in both latent size and sparsity. We have open-sourced the weights of our CLT at this https URL.

---


### 87. [Controllable Molecule Generation via Sparse Representation Editing: An Interpretability-Driven Perspective](https://arxiv.org/abs/2611.09235)

**<font color=#1a73e8>作者：</font>** Zhuoran Li, Xu Sun, Chang Wen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Controllable molecule generation is crucial for diverse scientific applications, such as drug discovery and materials design. While large language models (LLMs) show great promise, their dense and entangled representations impede precise control over the generation of molecules with bespoke substructures or properties. To address this, we propose Sparse Representation Editing (SpaRE), an interpretability-driven framework for fine-grained and precise control in LLM-based molecule generation. The crux of SpaRE is to learn an overcomplete sparse feature space that disentangles LLM representations into a compact set of latent features corresponding to chemically meaningful concepts. Within this space, we can directly manipulate these concept-aligned latent features to achieve (1) local control, by generating target atoms and functional groups at specified positions; and (2) global control, by customizing the overall structural and physicochemical properties within defined ranges. In this way, our framework advances interpretability from post-hoc analysis to actionable generative control. Experiments show that SpaRE can generate chemically desirable molecules under complex constraints in real-world scenarios, while offering mechanistic insights for quantitative structure-property analysis. The code and demo are available at this https URL.

---


### 88. [DUET: Dual-Sparse Inference for Block Diffusion Language Models](https://arxiv.org/abs/2611.09239)

**<font color=#1a73e8>作者：</font>** Siyuan Yan, Shen Gu, Xiaoxing Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) enable parallel token generation through iterative denoising, yet their inference remains costly due to repeated attention over a growing historical prefix and repeated processing of the entire current generation block. Historical attention becomes increasingly expensive as generation progresses, while all current-block positions are propagated through the Transformer at every denoising step even though only a small fraction are typically resolved at that step. In this paper, we introduce Duet, a training-free dual-sparse inference framework that addresses these challenges through prefix Key-Value (KV) sparsity and early query sparsity, respectively. Specifically, Duet exploits the concentration and cross-step stability of historical attention within each generation block to construct a compact historical KV subset that is reused across denoising steps. For query sparsity, Duet predicts update positions from shallow representations and propagates only the corresponding queries through the suffix Transformer layers, avoiding deep computation at positions unlikely to be updated in the current step. Experiments show that Duet maintains competitive accuracy while achieving 1.34$\times$/2.83$\times$ end-to-end/per-step speedups on LLaDA2.1-mini and 2.41$\times$/4.72$\times$ on SDAR-8B-Chat-b32 at a 32K context length.

---


### 89. [Rethinking MoE Load Balancing as Feedback Control](https://arxiv.org/abs/2611.09252)

**<font color=#1a73e8>作者：</font>** Yikun Hou, Alp Yurtsever  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) training is often not stationary: the data mixture changes at curriculum boundaries, when a model is continually pretrained into a new domain, or when the corpus is refreshed. Routing is learned against the current mixture, so each such change disrupts the per-expert load the router had converged to, and existing balancing methods have only been evaluated on stationary data. We rethink load balancing as a feedback control problem, in which the deviation of each expert's load from its fair share is the control error and the per-expert routing bias is the control input, and define a family of controllers, the PID-Balancer, from the proportional, integral, and derivative terms of classical PID control. Two widely used methods belong to this family: the auxiliary balancing loss behaves like a proportional controller, and the loss-free bias update is an integral controller acting on the sign of the error. Reading the router as a static map with a one-step delay, we show that the integral term is the only one that both removes persistent imbalance and averages out the step-to-step fluctuation of the measured load, whereas the proportional and derivative terms pass or amplify that fluctuation into the routing bias. We therefore adopt PID (I), the pure-integral member of the family with a single gain. Two settings are evaluated: (i) training an OLMoE backbone from scratch with 16 to 64 experts per layer, through a mid-run mixture switch, and (ii) continual pretraining of the released OLMoE-1B-7B on a new corpus. PID (I) holds balance before the shift and restores it more tightly afterwards than either the auxiliary loss or loss-free balancing, at comparable perplexity.

---


### 90. [Nudging Decision Models: Do Digital Nudges Steer Fast, Generation-Free AI Agents?](https://arxiv.org/abs/2611.09264)

**<font color=#1a73e8>作者：</font>** Sascha Kaltenpoth, Haya Halimeh, Kevin Bösch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents increasingly automate business and consumer tasks but are slow and expensive. Decision models, a new class that chooses among options without generating text, are far faster and less costly. Developers call them "System One models," referencing dual process theory. We ask whether such models can be steered by digital nudges online and whether, as the theory predicts, automatic nudges affect them more than reflective ones. We adapted an online shopping experiment, previously run with humans and LLM agents, to three decision models (Jev, Decision-1, d1). Across 600 runs per model, they chose a preselected default in 97.5-99.9% and a product with social influence information in 75-96% of choices, versus 47-49% in the control. All responded more strongly to the automatic nudge, the opposite of what has been reported for reasoning-capable LLM agents. We provide first evidence that non-generative decision models are susceptible to digital nudges in a System 1 pattern, implying agent-type-specific nudge effects.

---


### 91. [Thinking Twice: A Sequential Approach to Nudge Towards Reflective Judgment in GenAI-Assisted Decision Making](https://arxiv.org/abs/2611.09269)

**<font color=#1a73e8>作者：</font>** Hüseyin Hussein Keke, Daniel Eisenhardt, Christian Meske  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Humans increasingly use generative AI (GenAI) for decision-making assistance, yet tend to engage in such situations using quick, intuitive (System 1) rather than deliberate, analytical assessment (System 2) as reflected in Dual Process Theory. Such engagement reduces the effectiveness of human-GenAI interactions and increases associated risks. Our research investigates how to design human-GenAI interactions that promote the transition from System 1 to System 2 thinking in decision-making. Based on the Three-Stage-Model, which suggests humans switch to System 2 when conflicts are detected, we conducted an experiment (n=130) testing sequential human-GenAI interaction as a cognitive forcing nudge during problem-solving tasks. This approach, where humans decide first before receiving AI assistance, enables detection of conflicting decisions. Compared to non-sequential settings (concurrent or no AI assistance), results show the sequential condition significantly enhanced both decision performance and GenAI prompt utilization, providing valuable insights for designing more reflective and thus effective human-GenAI interactions.

---


### 92. [Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games](https://arxiv.org/abs/2611.09271)

**<font color=#1a73e8>作者：</font>** Eduardo C. Garrido-Merchán  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Weight-space programming sets every weight of a feed-forward network by hand, from an explicit specification of the desired computation, with no gradient descent and no training data anywhere in the construction. We ask how far a large language model can carry this practice, zero-shot, across games of deliberately increasing difficulty. We design a four-rung ladder (Nim, tic-tac-toe, two sizes of Connect Four, and a chess endgame) spanning four axes of difficulty, and build a second, independent network at each rung, using a structurally unrelated game at matched difficulty, to separate what a rung's finding says about the difficulty level from what it says about the one game used to measure it. Ten networks are built and independently verified. Six admit a complete, non-statistical proof of correctness against an independent oracle. The chess-endgame rung is exact where correctness is cheap, move legality and, in one network, an exact one-ply mate detector, and collapses where it is expensive, composing a multi-move mating plan, from 84.1-100% success at the one-ply tactics it was built to get right down to 0.57-9.13% in full adversarial play; its replicate shows this collapse is an order of magnitude less severe under a shorter required plan and exact rather than heuristic safety checks. The standard-sized rung confirms, by holding hand-set evaluation weights fixed and adding only shallow search, that the remaining gap is an architectural ceiling rather than a matter of engineering effort, and this exact collapse reproduces across two structurally unrelated games. We release all ten networks, their independent oracles, construction-cost measurements, and a cold-prompt protocol for a future cross-model comparison

---


### 93. [FondueQA: A Benchmark for Evaluating Parametric Compensation in Multi-Hop QA](https://arxiv.org/abs/2611.09274)

**<font color=#1a73e8>作者：</font>** Laurin Schmid, Suman Navaratnarajah, Koel Dutta Chowdhury 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) show remarkable performance based on parametric knowledge, i.e., their ability to recall facts and associations internalized in a model's weights. However, studying this capability on established multi-hop benchmarks may be complicated by benchmark contamination, as many of these benchmarks have been publicly available long enough to plausibly appear in modern pretraining corpora. As a result, correct answers under missing evidence may reflect either general parametric knowledge or memorization of benchmark-specific instances. To study how models use internal knowledge when retrieval evidence is incomplete, we introduce FondueQA, in which every required multi-hop fact is uniquely localized to a designated evidence document. This enables controlled document-level evidence ablations to study parametric compensation under incomplete retrieval. Our empirical evaluation reveals that parametric compensation strongly depends on both entity popularity and the structural role of missing evidence. Generally, models compensate more successfully for facts involving popular entities. On FondueQA, we show that bridging evidence can be more useful than the answer-bearing document itself. Moreover, models may recall a missing fact in isolation but fail to use it under partial evidence, particularly when the context contains plausible competing entities, which can reduce Exact Match by up to 15 percentage points.

---


### 94. [An Empirical Study of Issues in GPU Kernel Libraries for LLM Systems](https://arxiv.org/abs/2611.09280)

**<font color=#1a73e8>作者：</font>** Yanjie Gao, Jiayi Bi, Haoxiang Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behind the expanding use of large language models (LLMs) across application domains lies a growing dependence on specialized GPU kernel libraries. These libraries underpin the correctness and efficiency of training and inference across diverse GPU platforms, implementing attention, GEMM, quantization, and low-precision operators while managing tensor shapes, memory layouts, code generation, and hardware-specific dispatch. Problems at this layer can silently corrupt outputs, hang GPUs, prevent compilation, introduce deployment incompatibilities, or degrade performance, thereby reducing developer productivity and wasting expensive GPU resources.
We present the first comprehensive empirical study of issues in GPU kernel libraries for LLM systems. We manually analyzed 300 high-quality GitHub issue reports, their discussions, and available fixes from seven representative libraries: FlashInfer, FlashAttention, Triton, CUTLASS, DeepGEMM, xFormers, and bitsandbytes. The analysis characterizes symptoms, root causes, fixes, and testing and debugging practices. Our main findings are: (1) 60.33% of the sampled issues originate in the Compiler and Build System or Runtime Environment dimensions, so validation must cover the deployment and execution stack, not just kernel code. (2) Kernel specialization imposes implicit correctness constraints on tensor shapes, metadata layouts, memory aliasing, and hardware resources. Violations can produce incorrect outputs or launch failures even for supported operations, highlighting the need for explicit contract validation and boundary-case testing. (3) Current testing and debugging practices are often insufficient for identifying low-precision numerical problems and hardware-specific execution failures. We outline research opportunities and tooling directions to support future LLM GPU kernel development.

---


### 95. [Ontology-Driven Control of Conversational Agents with a Use-Case for Job Interview Practice](https://arxiv.org/abs/2611.09282)

**<font color=#1a73e8>作者：</font>** Barbara Gendron, Gaël Guibon, Mathieu D'aquin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been widely used as conversational agents in both domain-specific and open-domain situations. In domain-specific context, it is often necessary to adapt those LLMs to obtain conversations with desired characteristics, whether those apply at the level of each response (e.g. for tone or style) or more globally (i.e. at the level of a conversational strategy). Such adaptations are, however, generally realized in an ad hoc way, through specific, non-reusable, and non-transparent developments. In this paper, we propose an ontology-based approach to design conversational strategies that rely on the desired and measured characteristics of textual utterances in the conversation. Through a use case related to job interview practice, we show how this approach can be used to control LLMs to follow the strategy defined in the ontology. To this end, we automatically fine-tune the LLM to improve its compliance with ontologically-defined conversation characteristics. Our results show that training the LLM from formally defined concepts effectively enhances alignment with the requested characteristics. Hence, this work demonstrates how ontology-guided conversation control can be achieved while taking into account multiple, concurrent conversation aspects that are formally and transparently defined.

---


### 96. [AutoRefine: Auto-Calibrating Code Judges from Workflow Outcomes](https://arxiv.org/abs/2611.09291)

**<font color=#1a73e8>作者：</font>** Shervin Shahidi, James Poon, Hang Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judges increasingly serve as quality gates for code changes that have no test oracle, but a judge prompt must be calibrated for its task and recalibrated as the system it judges evolves, while hand labels for the calibration are resource intensive and go stale. Development workflows emit outcome labels for free (tests pass or fail, changes land or are abandoned), but these labels are noisy. We present AutoRefine, a loop that rewrites a deployable judge's prompt to reproduce outcome labels, with an informed teacher that sees the judge's input plus the outcome, explains each label it keeps, and abstains when the outcome cannot be explained from what the judge sees. On a held-out dataset with an execution oracle, calibration raised chance-corrected agreement (Scott's $\pi$) from 0.36 to 0.60. On a deployed agent's outcome labels, with 25\% flipped at random to introduce noise, the teacher set aside flipped \textsc{fail} labels at more than twice the rate of genuine ones, cutting overall label noise from 25\% to 20\%. Recalibrating that agent's judge using AutoRefine raised its agreement with merge/abandon outcomes on 17 independently held-out diffs from the current workflow ($\pi$ 0.16 to 0.51); on 16 diffs from older workflows, the previous judge stayed ahead, illustrating the need for recalibration as the agent evolves. By abstaining, the teacher not only removes noisy labels but also flags changes whose outcome the judge's input cannot explain, telling a team when a judge needs better inputs rather than a better prompt.

---


### 97. [Towards an Autonomous AI Steward for Large-Scale Physics Experiments: Integrating Causal Diagnostics, RAG, and Conformal Prediction](https://arxiv.org/abs/2611.09298)

**<font color=#1a73e8>作者：</font>** Oliver Noll, Nicholas Tan Jerome, Alexander Lehnen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term particle physics experiments face critical operational challenges: monitoring non-stationary machine data streams and preserving tacit expert knowledge. We present the "Helmholtz Co-Pilot," a hybrid Multi-Agent System (MAS) acting as an autonomous experiment steward. The system can be triggered interactively by human operators or autonomously by an asynchronous causal diagnostics engine that runs independently of the MAS reasoning core. Continuously monitoring live hardware streams such as data acquisition and slow control, this engine performs dynamic causal discovery to trace cascading alarms back to their root causes and applies adaptive model selection to keep forecasts reliable across shifting machine states; upon detecting an anomaly, it hands a structured diagnostic report to the MAS. The reasoning layer itself relies on a high-throughput C++ core and a Python edge architecture orchestrating a directed acyclic graph (DAG) of specialized ReAct workers. It integrates a Retrieval-Augmented Generation (RAG) backbone for institutional memory and leverages conformal prediction to bound its evidence-based recommendations with mathematical coverage guarantees. This extended abstract outlines the architecture, the integration of software-enforced Human-in-the-Loop (HitL) guardrails, and ongoing shadow-testing within the KATRIN experiment.

---


### 98. [T2I Models Rarely Invert Negation but Often Fail to Suppress Negated Concepts: Benchmarking Negation Suppression in Text-to-Image Generation](https://arxiv.org/abs/2611.09304)

**<font color=#1a73e8>作者：</font>** Akansha Gautam, Aparna Bharati, Mayank Vatsa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models often fail to suppress explicitly negated concepts, such as a lamp for "a desk without a lamp." We introduce T2I-NSI, a benchmark and metric for measuring negation sensitivity in text-to-image generation. It pairs each negated prompt with a canonical positive counterpart and factorizes negation by linguistic form (lexical/semantic, morphological, syntactic) and target type (objects, attributes, relations, compositions, and nested cases). The benchmark contains 759,869 paired prompt atoms over a 5,082-object catalog, with 916,272 images (911,982 open-weights, 4,290 closed-source), scored by a Basic CLIP estimator and a Robust ensemble of CLIP, VQA and open-vocabulary detection. Negation sensitivity is low: open-weights generators score NSI <= 0.038, while GPT-Image-1.5 and Gemini-2.5-Flash-Image reach about 0.09. The dominant failure is under-suppression rather than misdirection. Inverse interpretation is essentially absent (0.00% across over 450K atom-model evaluations), whereas models render the concept under both prompts on 8-19% of atoms and only partly suppress it on a further 9-25%; most remaining atoms are too weakly rendered to label. A blinded human study (420 atoms, nine annotators) corroborates the near-absence of inversion and the high persistence rate, and a matched-prompt comparison shows the open-versus-closed gap (~3.5x) is not a prompt-generator artifact. Code and data: this https URL

---


### 99. [ReSUM: Reasoning-Driven Multi-Agent Framework for Query-Focused Summarization](https://arxiv.org/abs/2611.09349)

**<font color=#1a73e8>作者：</font>** Sonali, Deeksha Varshney, Asif Ekbal  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLMs excel at language tasks, but long-meeting QFS remains difficult due to complex speaker dynamics, sparse key information, and limited data. Meetings involve disfluencies, long transcripts and complex discourse. QFS have high risk of information omission, hallucination, even for advanced models such as GPT-4-mini and Gemini. Existing end-to-end methods compress retrieval, evidence extraction, and summary generation into a single pass, failing to handle the complex reasoning required for targeted meeting summaries. We propose ReSUM, a modular multi-LLM framework coordinated by a planner that orchestrates retrieval and summarization agents. By distilling teacher reasoning into query- and plan-conditioned retrievers and summarizers, ReSUM enhances long-context robustness, minimizes irrelevant exploration, and generates more faithful and comprehensive query-focused summaries. Experiments show consistent gains on query-focused meeting summarization benchmarks.

---


### 100. [HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes](https://arxiv.org/abs/2611.09355)

**<font color=#1a73e8>作者：</font>** Boran Zhao, Yanbin Hu, Jun Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memory plays a crucial role in long-horizon task execution and cross-task generalization for Vision-Language-Action (VLA) models operating in complex 3D scenes. However, existing VLA memory mechanisms suffer from memory noise, particularly in complex 3D scenes, as stored episodic memories contain extensive redundant details about scene layouts, object configurations, and robot-specific states, which obscure generalizable manipulation principles and hinder cross-task transfer. To address this challenge, we first introduce a hippocampus-inspired memory consolidation mechanism that synthesizes extensive episodic experiences into a compact set of essential semantic memories, enabling VLA models to derive generalizable principles from practical experience. Second, we propose an episodic memory pruning mechanism that removes redundant episodic memories whose contents are captured by consolidated semantic memories, thereby increasing effective memory capacity and improving long-horizon task execution. Finally, to handle complex task scenarios, we develop a flexible memory composition mechanism that jointly leverages multiple episodic and semantic memories to enhance cross-scenario generalization. Experiments on LIBERO, LIBERO-Plus demonstrate the effectiveness of HiMEM across different VLA backbones, improving the average success rate of pi_0 from 91.88% to 98.20% on LIBERO.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-174](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
