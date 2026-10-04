# 🧠 大模型相关研究 | 2026年10月05日

> 本类共 **384** 篇论文：已确认 **365** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-384](./part-08.md)

---

### 151. [OR for AI That Does OR: Routing LLMs up the Escalator inside the OSCAR Framework](https://arxiv.org/abs/2610.00912)

**<font color=#1a73e8>作者：</font>** Jinzhi Bu, Haixin Tang, Huanan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can translate business descriptions into optimization models, but executable code may misrepresent constraints or objectives. A solver can then return an optimal solution to the wrong problem. Even when the solution satisfies the intended operating rules, a better plan may exist. For organizations that repeatedly use optimization modeling, an LLM-based framework should produce accurate formulations at low cost and, ideally, run locally. We study how to verify improvements and allocate attempts across LLMs that differ in price and capability. We develop OSCAR (Optimization modeling by Simulator, Coder, And Reviewer), which uses an offline Simulator certified against labeled decision examples to compare candidates and continues searching beyond feasibility. We model the search for the next certified improvement as sequential decisions under unobserved difficulty: which LLMs to call and when to stop. In a simplified known-prior setting, we give conditions under which cost-ordered escalation is optimal. For general menus, we derive a prior-free competitive guarantee. On five benchmark problems, OSCAR achieves 95% to 100% accuracy at the reported settings using two small open-weight LLMs, each deployable locally on a single GPU. Their single-attempt accuracies average 29% and 48%. In five runs per problem, Codex and Claude Code incur average token costs 3.1 and 5.8 times OSCAR's, respectively. OSCAR supports open-weight models locally or in the cloud, depending on budget and confidentiality requirements. Firms should maintain labeled decision examples of feasible and infeasible decisions to clarify plain-language operating rules. OSCAR follows these labels when an LLM's interpretation conflicts with them. As LLM capabilities and prices change, OSCAR's simple operating rules and adjustable settings help firms adapt their model choices and benefit from these advances.

---


### 152. [Finding the Right Fit: Model-Harness Interactions across Agent Tasks](https://arxiv.org/abs/2610.00917)

**<font color=#1a73e8>作者：</font>** Yixuan Li, Yiyun Zhou, Yao Long Teng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Choosing an agent system means choosing both a language model and the harness through which it acts. We ask whether a strong model, harness, or pairing stays strong when the setting changes. We evaluate 66 configurations: four configurable harnesses (OpenHands, DeepSeek Harness, PI, and openJiuwen) paired with five models on TUA-Bench, ALE-CLI, and Terminal-Bench 4, plus the native Codex-GPT and Claude Code-Claude pairings. Model rankings reverse across harnesses. On Terminal-Bench 4, Claude leads GPT by 7.94 points in OpenHands but trails it by 30.16 points in PI. For four of the five models, the best harness changes from one benchmark to another, yet some pairings hold: openJiuwen gives Kimi its highest score on all three benchmarks, by 5.61 to 11.11 points. A model's own vendor harness is not reliably its best, and higher cost does not reliably buy a higher score. On Terminal-Bench 4, GPT scores higher under PI than under DSH at less than a quarter of the cost per task. Matched trajectories suggest why fit varies. Models start almost all repairs themselves, so much depends on whether the harness hands failures back in a form the model can use. GPT does best with PI's lean scaffold, while Kimi, which often issues malformed tool calls, does best in openJiuwen. We argue that the model, the harness, and the task should be evaluated together, and we release the harness adapters, evaluation code, and all 6,204 scored trajectories at this https URL and this https URL.

---


### 153. [Efficient Task Adaptation in Large Language Models: A Survey of Weight-Based, Prompt-Based, and Embedding-Based Adaptations](https://arxiv.org/abs/2610.00928)

**<font color=#1a73e8>作者：</font>** Jungwon Park, Changin Choi, Jimyeong Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly deployed across diverse downstream tasks, efficient task adaptation has emerged as a central challenge. In response, a wide range of task adaptation methods have been proposed, spanning parameter-efficient fine-tuning, in-context learning, and embedding-injection approaches. However, these lines of work have largely evolved within individual paradigms, leaving their cross-paradigm relationships and trade-offs underexplored, especially for recently emerging embedding-based adaptations. This survey presents a unified framework that categorizes task adaptation methods by where and how task information is encoded: model weights, input prompts, or injected task embeddings. We provide a comprehensive taxonomy that integrates these paradigms, analyze their key strengths and limitations to explain how different adaptation paradigms have evolved, clarify relationships across paradigms, and highlight open problems for future research.

---


### 154. [ReHoPER: Receding-Horizon Planning for Enhanced Reasoning](https://arxiv.org/abs/2610.00940)

**<font color=#1a73e8>作者：</font>** Saeed Ahmadnia, Cornelia Caragea  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose ReHoPER, an inference-only, zero-shot method that improves large language models' reasoning by generating and answering intermediate questions along multiple paths before the final answer. It iteratively plans a horizon of candidate intermediate questions, selects one to answer, and replans from the updated history. ReHoPER is task-agnostic, using the same generic instructions across datasets and models without labeled data or task-specific prompt design. Across multiple datasets, including iLLC, a new controlled benchmark for compositional reasoning, ReHoPER outperforms strong baselines, with the largest gains in the most compositional settings. Our implementation and the iLLC generator are publicly available to support future work.

---


### 155. [ABDA-NL: A Natural-Language Scenario Explorer for Argument-Based Reasoning](https://arxiv.org/abs/2610.00947)

**<font color=#1a73e8>作者：</font>** Shawn Bowers, Martin Caminada, Haoyang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ABDA-NL adds a natural-language interface to ABDA, a system for argument-based discussion using ASPIC- knowledge bases under grounded semantics. Users see which conclusions are accepted, rejected, or undecided, open an interactive rendering of the grounded discussion game to learn why, explore what-if alternatives by suspending assumptions and rules or changing preferences, ask questions that are answered from a scenario's reference documents, and author new facts, assumptions, and rules in plain English. A large language model provides the bridge between language and formalism: it answers questions from the documents and the current state of the scenario, and it translates plain-English edits into candidate formal statements. The deterministic ABDA engine remains the sole source of arguments, attacks, and acceptance labels, and every proposal of the model is validated and confirmed by the user before it takes effect.

---


### 156. [GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution](https://arxiv.org/abs/2610.00948)

**<font color=#1a73e8>作者：</font>** Geyi Yang, Zikun Qu, Xiang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The executable harness surrounding a GUI model determines how observations are assembled, actions are executed, and verification, recovery, and termination are controlled. Compared with harness optimization for non-GUI agents, automatically optimizing this harness poses three coupled challenges: reconciling model intent with observed visual effects, diagnosing failures under variable execution outcomes, and identifying recurrent failure patterns across tasks and translating them into reusable runtime changes. We introduce GUI-HARVEST, an automatic harness optimizer that enables self-improving GUI agents with frozen backbone models. First, to ground diagnosis in observed action effects, it aligns model outputs and executed actions with before-and-after screenshots, tying findings to specific interface transitions. Second, to account for execution variability, it treats repeated runs of the same task as a joint evidence unit, using within-task comparisons to locate outcome-relevant behavioral differences. Third, it consolidates verified findings across tasks into recurring failure patterns, maps them to bounded source-code edits with predictions recorded before evaluation, and checks the predicted behavioral effects alongside task performance through repeated execution. Experiments on OSWorld-Verified show consistent held-out gains across six general-purpose open, GUI-specialized open, and proprietary backbone models; Qwen3-VL-32B-Instruct gains 12.33 points on the full suite. Frozen-harness transfer improves GPT-5 by 13.87 percentage points on WindowsAgentArena at 50 steps without further optimization. With the same backbone and initial harness, GUI-HARVEST outperforms Self-Harness and Meta-Harness, suggesting that GUI-specific diagnosis and validation help harness improvements generalize to unseen tasks. The code is available at this https URL.

---


### 157. [PG-SFT: Balancing Capability Acquisition and Retention in Offline Agent Fine-Tuning](https://arxiv.org/abs/2610.00949)

**<font color=#1a73e8>作者：</font>** Ronghua Li, Zi Liang, Zhishan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) on offline agent trajectories is the standard approach for training specialized tool-using agents, but forcing models to imitate reasoning and actions token by token may harm other capabilities (e.g., general reasoning, tool calling, code generation) of the base model. In this work, we focus on studying \emph{how to better balance the trade-off between acquiring new capabilities and preserving existing ones during agent trace SFT}. By comparing several baselines in our setup, standard SFT improves the target benchmark while lowering several non-target benchmark scores; meanwhile, simply constraining distributional drift using KL penalty or limiting the update magnitude did not avoid this regression trend. Motivated by recent token-wise adaptive learning objectives, this work proposes \textbf{Privilege-Guided SFT (PG-SFT)} to leverage turn-level information gain of agent trajectories as an indicator to adjust supervision strength. PG-SFT yields a more favorable observed trade-off on the evaluated benchmarks, substantially reducing distributional drift and broad capability degradation at the cost of slight degradation in target-task performance. Our findings suggest that balancing the acquisition--retention trade-off depends not only on whether the model is anchored to its base behavior, but also on where and how strongly supervision should depart from that behavior.}

---


### 158. [A Matched-Budget Audit Framework for Recaptioned Image-Text Supervision Distributions](https://arxiv.org/abs/2610.00952)

**<font color=#1a73e8>作者：</font>** Giyeong Oh, Junghun Park, Yuhan Bae 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recaptioned image-text corpora are now standard for text-to-image (T2I) training, with vision--language model (VLM) captioners replacing sparse alt-text by dense descriptions. A recaptioned corpus is a supervision distribution induced by a documented captioning policy ($\pi$), captioner ($V_c$), and source corpus ($C$). Length-correlated proxies miss caption-register artifacts and downstream T2I benchmarks entangle the corpus with training choices, so this distribution is hard to audit at corpus scale. We introduce a reusable matched-budget audit framework for recaptioned supervision distributions $D_{\pi,V_c,C}$: at a fixed text budget of $B = 64$ it reports a five-axis profile spanning prompt-side coverage, image-conditioned faithfulness, and caption-surface health, with claimed controllable basic units (CBU) as the common claim unit. We instantiate the framework on seven paired comparisons over five public source corpora. Across the four cross-corpus pairs, the released surface raises supported CBU per caption by $+3.39$ to $+6.36$ under both Qwen and Gemma Judges, and on CC12M the same framework exposes a long-vs-dense frontier that is consistent across both judges and four budgets. We release the audited multi-source recap corpus ($\approx$ 490M) together with the audit-artifact bundle.

---


### 159. [Two Clocks in Diffusion MLLMs: When Answers Stabilize Before Rationales Unfold](https://arxiv.org/abs/2610.00953)

**<font color=#1a73e8>作者：</font>** Keuntae Kim, Yong Suk Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An answer candidate in a masked diffusion MLLM can stabilize while its rationale is still unfolding. We distinguish retrospective stabilization of the logged candidate from token commitment, and examine these two clocks relative to rationale generation. Analyzing our results across three visual question-answering benchmarks, we find that 89.4-98.1% of the rationale-side canvas remains unwritten at stabilization in single-block, EOS-suppressed LaViDa runs. On V*Bench, reducing block length from 128 to 8 changes this fraction from 89.4% to 1.7%, together with answer coverage and the eligible observation window. Under EOS-enabled prompting, direct instructions improve Nemotron's overall accuracy by 15.0 and 19.5 percentage points on M3CoT and ScienceQA, but reduce LaViDa/V*Bench accuracy by 11.0 points. A symmetric decomposition associates the larger absolute component of each change with coverage rather than conditional accuracy. Matched-canvas image ablations measure visual sensitivity alongside answer stabilization, separating the two temporal readouts. Together, these measurements distinguish answer stabilization, rationale unfolding, and visual sensitivity, and identify coverage as the larger component of the prompting differences.

---


### 160. [Beyond Leaderboards: Tokenomics of Agentic Small Language Model Ensembles](https://arxiv.org/abs/2610.00954)

**<font color=#1a73e8>作者：</font>** Alexei N. Skurikhin, Emily M. Taylor, Nathan A. DeBardeleben  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) move from standalone assistants into agentic workflows, evaluation must extend beyond scalar leaderboard accuracy to account for operational reliability, cost, latency, and token efficiency. We use an agentic ensemble of small language models (SLMs) with an SLM-judge-mediated feedback loop as a case study for such beyond-leaderboard evaluation. On the 541-prompt IFEval benchmark, the best ensemble achieves 97.34% strict prompt accuracy, exceeding the strongest standalone LLM baseline, gpt-5.4, by 5.81 percentage points while operating in a lower-cost regime. We then analyze the tokenomics and operational behavior behind this gain, including cost per sample, token composition, useful-output goodput, feedback-loop recovery, latency decomposition, and performance across instruction categories and constraint counts. Our results show that agentic SLM ensembles can trade additional test-time tokens and orchestration overhead for improved instruction-following fidelity, motivating multi-dimensional evaluation protocols for future agentic AI systems.

---


### 161. [Role-aware Heuristic Episodic Attention for Conversational LLMs](https://arxiv.org/abs/2610.00958)

**<font color=#1a73e8>作者：</font>** Wanyang Hong, Zhaoning Zhang, Yi Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often lose track of persistent instructions and relevant information as multi-turn conversations grow. We study this cumulative contextual decay through three related failure modes: attention pollution, dilution, and drift. We propose REA (Role-aware Heuristic Episodic Attention), a context-management framework that assigns different persistence and representation policies to instructions and episodic interactions. Instructional Memory retains identified global constraints in a dedicated prefix. Episodic Memory preserves user inputs and compresses model replies, while heuristic retrieval selects raw text, compressed representations, or omission for each historical turn. On Long-MT-Bench+, REA improves the judge score from 6.32 to 7.36 on a 10-point scale, a 16.5% relative gain over the Vanilla baseline, and reduces average latency by 2.91$\times$. Additional evaluations show aggregate gains on three backbones spanning 1.7B-7B parameters and on Chinese and English role-playing tasks. These results support role-aware context management as a practical approach to maintaining conversational continuity and instruction adherence.

---


### 162. [Video-Index: A Curated Meta-Benchmark for Video Understanding](https://arxiv.org/abs/2610.00960)

**<font color=#1a73e8>作者：</font>** Enxin Song, Yinuo Xu, Shusheng Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A video benchmark should reward the capability it claims to measure, yet models can exploit answer options, question text, or partial visual evidence. We introduce the attack pyramid, five levels of shortcut attacks with increasing access to each item, and audit 115 video benchmarks with it. On 35 benchmarks, attackers that never see a frame approach full-video accuracy. On 51 benchmarks with temporal probes, shuffled frames keep a median 96% of full-video accuracy. Near-duplicate questions make up at least half the items in 63 benchmarks. We screen 505,518 question-answer pairs from 112 of them into an audited pool. Agents turn evaluation requests into specifications, and a deterministic selector with a red-team gate composes reproducible benchmarks. We release Video-Index, the 210 hardest verified items under these attacks in each of four capability groups, 840 items from 76 sources. With the same fixed input, Claude Opus 5 outscores every open-source model by over 37 percentage points, and agent tools add about 20 more, yet all systems leave room to improve efficiency and accuracy. Blog: this https URL GitHub: this https URL Hugging Face: this https URL

---


### 163. [A Citation-Grounded Benchmark for Trustworthy Earnings Call Transcript Analysis with Large Language Models](https://arxiv.org/abs/2610.00969)

**<font color=#1a73e8>作者：</font>** Yingzhu Zhao, Vlad Pandelea, Han Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been increasingly used for financial document analysis, including earnings call transcripts (ECTs). Beyond generating standalone claims, users increasingly prefer grounded analyses that pair claims with verifiable citations from source documents to enable independent validation. However, evaluating such analytical claims typically requires extensive expert annotation, which is costly and difficult to scale, and real-world financial analysis commonly involves long context-question-answer triplets, further increasing task complexity. To address these challenges and benchmark the current landscape of grounded analysis by LLMs, we propose a numeric evidence evaluation method that enables groundedness assessment without reliance on expert annotation. We also introduce an automated dataset construction pipeline and construct ECTs-100 from the top 100 constituents of the S&P 500 to support benchmark of both groundedness and correctness. In addition, we examine conscious incompetence, a practical failure mode in financial analysis in which LLMs must detect when available evidence is insufficient and refrain from producing unsupported hallucinations. Empirical results show that LLMs perform well in groundedness but face notable limitations in correctness, with informational insufficiency presenting an additional challenge.

---


### 164. [RelationVGGT: Visual Geometry Transformers for 3D Spatial Relation Segmentation](https://arxiv.org/abs/2610.00970)

**<font color=#1a73e8>作者：</font>** Minsu Kim, Jaesung Choe, Jiwoo Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D reconstruction have progressed from per-scene optimization to feed-forward inference, and semantic scene understanding has followed suit -- yet existing methods remain confined to object-centric perception, neglecting spatial relations between objects. We formulate 3D spatial relation segmentation in a feed-forward, pose-free multi-view setting: given a visually specified subject and a relational text query, the model segments the target across views without receiving its category name. To this end, we propose RelationVGGT, a novel feed-forward framework that integrates semantic features from a visual foundation model with geometry-aware representations from a 3D geometry foundation model and leverages a relation transformer for subject-conditioned, cross-view relation prediction -- requiring neither per-scene optimization nor known camera poses. We additionally provide a fully automated annotation pipeline built on ScanNet++ with VLMs and LLMs, enabling scalable training data generation for this new task.

---


### 165. [VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks](https://arxiv.org/abs/2610.00972)

**<font color=#1a73e8>作者：</font>** Caiqi Zhang, Rujun Han, Zifeng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents undertake increasingly complex, long-horizon tasks, verifying their outputs becomes increasingly challenging. We study how verification capability can be strengthened with a fixed base model, without access to reference answers or grading rubrics at test time. Repeated sampling yields multiple rollouts that can contain complementary correct claims, but we need a reliable verification mechanism to determine which claims to trust. We first find that disagreement often exposes correct alternatives, while consensus can conceal errors. These observations motivate VeriHarness, which turns the underlying LLM a generator uses into an agentic verifier by giving it a workspace, evidence tools, and reusable verification skills. A disagreement resolver checks competing claims against environmental evidence, while a consensus challenger tests shared claims and searches for omitted requirements. Their findings guide the selection and revision of the final artifact. Across five long-horizon workspace benchmarks and two frontier models, VeriHarness achieves the highest selection scores among the evaluated baselines. Evidence-backed revision further improves average performance, bringing gains over a single rollout to 6.2 points with Gemini 3.5 Flash and 6.4 points with Claude Opus 4.8. We further show that verification skills can self-improve from failure feedback, demonstrating VeriHarness as a novel and critical approach for scaling long-horizon agentic verification. We release the full pool of approximately 26,000 rollouts across all five benchmarks and both models, produced at a cost of over $100,000, to support future research on agentic verification.

---


### 166. [Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack](https://arxiv.org/abs/2610.00973)

**<font color=#1a73e8>作者：</font>** Haiming Zhao, Tai Wang, Kun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Science teachers frequently search for documentary excerpts not by describing what appears on screen, but by querying the abstract concepts they intend to teach. This use case exposes a limitation of existing language-based video moment retrieval methods, which typically assume that queries describe observable events, whereas instructional search requires retrieving concrete visual phenomena that instantiate an underlying scientific principle. We study this setting as concept-to-example video retrieval, an abstract-needle-in-a-haystack problem where compact curriculum concepts must be grounded in temporally sparse documentary evidence. To bridge this abstraction gap, we propose Concept-Driven Domain Adaptation (CDDA), a three-stage framework for adapting two-tower vision-language models to concept-level retrieval. CDDA treats concepts as intermediate semantic anchors: it first structures the textual embedding space with textbook and teacher-handbook example-concept pairs, then transfers this concept-aware geometry to documentary visuals under a frozen visual encoder, and finally jointly adapts both encoders with sparse visual concept supervision. From a geometric perspective, this staged alignment reduces text-concept and vision-concept angular gaps, thereby encouraging concept-level adaptation while preserving the pretrained model's concrete image description alignment. On a curated middle-school physics retrieval benchmark, CDDA achieves stronger pedagogically oriented concept retrieval than several competitive multimodal baselines, including Qwen3-VL-Embedding-2B, while maintaining concrete image-text matching after adaptation.

---


### 167. [ABSENTIA: Detecting Broken Access Control Vulnerabilities in Web Applications](https://arxiv.org/abs/2610.00977)

**<font color=#1a73e8>作者：</font>** André V. Duarte, Aditya Oke, Rui Melo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Broken access control, the failure of authorization, is one of the most prevalent web security risks. Unlike injection, a flow of untrusted input into a dangerous operation, authorization is a relation: who may act on what, not how data moves. Each application decides that relation for itself, so no rule written in advance carries to the next. An LLM agent can infer it from the code, but with no systematic way to cover the application and prioritize what to inspect, its search stays undirected and access-control flaws go undetected.
We present ABSENTIA, a security scaffolding that turns general LLM agents into systematic vulnerability detectors for the backend of web applications, run as an audit by the developers and security engineers who maintain the code. Under its direction, the agents build a graph that maps the application's routes to the code behind them. ABSENTIA then works route by route, applying invariant falsification: it infers the properties the code is meant to satisfy, and where one is not enforced, reports the route for maintainer review.
We also release BAC-Bench, a benchmark of 30 broken access control advisories across 25 repositories, 3 languages, and 9 frameworks, each published in 2025 or later, verified by a human auditor, and paired with its fixing commit, so credit requires flagging the vulnerable version and not the fixed one. ABSENTIA recalls 19 of them, 17 under paired credit, and an LLM verifier confirms 51% of its findings. CodeQL and Semgrep recall none, and an unstructured agent on the same model recalls 3. In the OWASP Benchmark injection categories, ABSENTIA leads the dedicated analyzers in Python and trails only CodeQL and IRIS in Java.

---


### 168. [RISED: RubrIcs for agentic multi-environment Selection and sElf-Distillation](https://arxiv.org/abs/2610.00979)

**<font color=#1a73e8>作者：</font>** Jingtan Wang, Sirajul Salekin, Young mok Jung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training a single LLM agent jointly across diverse interactive environments has attracted increasing attention as a route to generalist agents. Existing curriculum and data-selection strategies often allocate training at the environment level or prioritize local reward-based signals, without explicitly considering relationships between current rollouts across environments for prompt-group selection. Meanwhile, as environments are learned at different rates, all-failure and all-success rollout groups can coexist within a batch, leaving those data without group-relative reward signals. Both challenges highlight limitations of relying solely on scalar rewards in multi-environment RL: they provide limited information about cross-environment relationships and no within-group reward contrast when rewards are identical. This motivates richer textual feedback, such as rubrics describing rollout behaviours, to guide learning. Beyond rubrics' usage as reward, we repurpose rubrics to guide both online data selection and policy supervision. An LLM judge tags each rollout using a predefined rubric vocabulary shared across environments. The resulting profiles guide the selection of data that aligns with the overall behavioural composition of the mixed-environment batch while limiting overlap with already-selected data. Available positive rubrics (describing desired behaviours) provide privileged context for an on-policy self-distillation teacher, supplying additional token-level supervision, while negative rubrics (describing undesired behaviours) guide subsequent rollout generation away from recurring failure modes. Together, these components form RISED. Across model backbones, RISED achieves the highest mean pass rate across environments and ranks first or second in every individual environment. Rubric-based analysis of RISED can further characterize the behavioural changes accompanying these gains.

---


### 169. [The Devil Is in the Reconstruction Loss Scale: Rethinking Optimization in LLM Quantization](https://arxiv.org/abs/2610.00983)

**<font color=#1a73e8>作者：</font>** Chao Li, Shigeng Wang, Anbang Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) methods typically use sequential quantization that partitions a pre-trained LLM into a series of units (e.g., transformer blocks), with one unit quantized at each stage. State-of-the-art PTQ methods are predominantly learning-based, optimizing auxiliary quantization parameters (e.g., scaling factors, rotation matrices, clipping thresholds, and adapters) via gradient descent to minimize a reconstruction loss. A common practice is to use mean squared error (MSE) as the reconstruction loss function, yet its induced optimization behavior remains largely unexplored. In this work, we take a holistic view of sequential quantization and systematically investigate how optimization evolves from the first quantization stage to the last, aiming for a deep understanding of optimization in learning-based PTQ schemes. Through extensive empirical studies spanning representative learning-based PTQ methods, LLM families, model scales, architectures, quantization settings and various tasks, we consistently uncover Optimization Imbalance: reconstruction loss magnitudes vary dramatically across stages, accompanied by highly uneven gradient magnitudes and parameter updates under MSE. We term the cross-stage range of loss magnitudes the reconstruction loss scale, and reveal that MSE translates the unexpectedly large reconstruction loss scale into highly uneven gradient magnitudes, which in turn lead to uneven optimization strength across quantization stages. This finding suggests a general principle for improving learning-based PTQ: optimization strength across stages should be decoupled from the reconstruction loss scale. Theoretically, we show that root mean squared error (RMSE) variants defined at the sample, channel, token, and element levels naturally realize this principle through implicit gradient normalization, outperforming MSE significantly as a drop-in replacement.

---


### 170. [HADRec: A Hierarchy-Aware Drug Recommendation Framework by Fusing Molecular Knowledge and Electronic Health Record](https://arxiv.org/abs/2610.00984)

**<font color=#1a73e8>作者：</font>** Junke Wang, Hongshun Ling, Li Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate medication recommendation is central to clinical decision-making, directly determining therapeutic efficacy and patient safety. However, existing methods suffer from two key limitations: drugs are often abstracted as discrete tokens, ignoring their molecular structures and pharmacological mechanisms, and the commonly used "flat" recommendation paradigm fails to leverage the hierarchical logic of the internationally standardized Anatomical Therapeutic Chemical (ATC) classification system. To address these issues, we propose HADRec, a Hierarchy-Aware Drug Recommendation framework that integrates molecular knowledge with electronic health records (EHRs). HADRec employs LLaMA-7B to encode clinical notes for rich patient representations and ChemBERTa to encode drug Simplified Molecular Input Line Entry System strings, building a global molecular knowledge base. A cross-attention mechanism then performs deep multimodal fusion between patient states and drug features. The framework further incorporates a hierarchical predictor and a novel consistency constraint loss to enforce strict adherence to ATC logical dependencies. Extensive experiments on MIMIC-III demonstrate that HADRec achieves state-of-the-art performance across Jaccard, F1, and PR-AUC. External validation on MIMIC-IV confirms strong generalization under distribution shifts, and calibration analysis shows well-calibrated predictive confidence on MIMIC-IV with ECE = 0.04, and Brier = 0.06. Counterfactual evaluation reveals clinically aligned reasoning, disentangling disease-specific treatments from general care. Together, these results establish HADRec as a high-performance, interpretable, and clinically grounded pathway toward safe and reliable AI-driven medication recommendation.

---


### 171. [Auditable Algebraic Counting Field for Cryptic-Pocket Detection from Apo Structures](https://arxiv.org/abs/2610.00988)

**<font color=#1a73e8>作者：</font>** Shan Yu, Xuening Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cryptic ligand-binding pockets are not apparent in experimentally determined apo structures, making them difficult to identify from unbound receptor geometry. A complementary challenge is to make the structural measurements and learned evidence behind each prediction directly inspectable. We introduce a supervised algebraic counting field (ACF) for predicting cryptic-pocket residues from apo structures. ACF compiles explicit geometric, physicochemical, and topological features into compact, integer-weighted lookup tables. Each prediction score can be reconstructed from feature values, training counts, table weights, and spatial aggregation, without sequence search, structural-template transfer, or a protein language model at inference. We evaluate ACF on CryptoBench and two locked external collections, separating ranking performance from the effects of residue-calling budgets. On an external set of 57 post-CryptoBench apo-holo units, ACF exceeded P2Rank by +0.044 in mean paired ROC-AUC (multiplicity-adjusted 95% CI [+0.010, +0.079]). The advantage was dataset-dependent: official-fold ROC-AUC and matched-budget F1 differences against P2Rank remained unresolved, and a second external evaluation did not confirm gains from added structural features. ACF thus provides a compact predictor with externally validated signal and an inspectable path from structural measurements and training counts to residue scores.

---


### 172. [VIEScore2: Unified Image Evaluation with Spatially Grounded Explanations](https://arxiv.org/abs/2610.00994)

**<font color=#1a73e8>作者：</font>** Xianda Du, Max Ku, Weiming Ren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing synthetic image evaluators typically provide only a scalar quality score and do not identify the image regions that support it. We introduce VIEScore2, a unified evaluator for image generation and editing tasks with optional conditioning images. VIEScore2 represents an image as an N x N grid and jointly predicts quality scores and defect locations in a single model pass. Its text-native grid representation provides a common interface for heterogeneous spatial supervision and enables directly verifiable post-training objectives. We train on 38K examples spanning score-only, localization-only, and joint supervision across generation and editing tasks. Starting from supervised fine-tuning, we further apply GRPO to improve defect localization using rewards that combine cell-level Dice overlap, score accuracy, and output-format validity. A parameter-free parser converts the structured predictions into readable explanations. On the primary suite, VIEScore2 achieves an overall-score SRCC of 0.601, compared with 0.491 for Gemini-3-Flash, the strongest zero-shot general-purpose VLM baseline under matched inputs. For defect localization, VIEScore2 outperforms both general-purpose VLMs and specialized spatial evaluators on three of six benchmarks in per-image grid IoU and ranks among the top three on five, including datasets beyond its training sources.

---


### 173. [Distilling Directional Verification](https://arxiv.org/abs/2610.00997)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Sugyeong Eo, Seongtae Hong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation aims to transfer the factual knowledge of large language models to smaller models for efficient deployment. Yet a teacher may recall a relation in one direction while failing to generate the answer in the reverse direction. Distillation from its generated answers can therefore propagate this directional limitation to the student. The same teacher can nevertheless recognize such an answer by scoring the relation in the direction it knows. We introduce directional label distillation, in which frozen teachers score candidate answers in that known direction and the best-scoring candidate becomes the student's training target. On facts about parents and their children, known-direction scoring yields more accurate labels than scoring the requested direction, even after tuned corrections for name priors. With prior-corrected scores, the better direction depends on the facts rather than the template, and reverses on mined facts whose notable entity is the parent rather than the child. With the evaluated children's forward facts withheld, students trained on known-direction labels improve open-ended accuracy on their trained queries by 13 to 15 points over students trained on prior-corrected reverse labels. After generated answers are matched to a fixed name list by lexical similarity, students reproduce nearly all selected labels. Their accuracy largely follows label quality. The label advantage holds on unscreened queries and when candidates are retrieved without inserting correct answers. Our findings show that directional verification mitigates the transfer of errors from teacher-generated answers to students by providing more accurate training targets. Code is available at this https URL.

---


### 174. [Evaluating LLM-Generated Preference Distributions](https://arxiv.org/abs/2610.01000)

**<font color=#1a73e8>作者：</font>** Fan Huang, Minsuk Kim, C. Tyler Diggans 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used as probabilistic generators for simulation, synthetic data generation, and decision support in settings where real-world data are unavailable. Yet, the structure and reliability of the distributions they produce remain understudied. Here, we systematically analyze LLM-generated distributions of preferences for air travel, restaurants, and consumer products. Encouragingly, all models considered in our analysis exhibit self-coherence, with the most probable outcomes stabilizing rapidly under repeated sampling. At the same time, we observe substantial discordance across both model families and scales, with little consensus even among their most probable outcomes. These patterns hold across nine open-weight models, three choice domains, and show robustness under temperature changes, greedy decoding, and perturbations of prompt and ordering. Our findings indicate that outcomes are influenced more by the choice of model than by the wording of the prompt, challenging the common assumption that sufficiently capable LLMs produce similar preference distributions when used as stand-ins for survey respondents.

---


### 175. [From Discovery to Decision: Finite-Budget Recoverability in LLM Voting](https://arxiv.org/abs/2610.01014)

**<font color=#1a73e8>作者：</font>** Shaoang Li, Jian Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Voting over multiple LLM responses is a common primitive in test-time scaling and ensemble inference. Collecting more responses can expand the candidate pool and increase the chance that a correct answer is discovered. Under a fixed call budget, a discovered answer still needs to accumulate enough support within the remaining calls to become the final plurality winner, creating a discovery-to-decision gap. In this work, we characterize this gap through the realized vote state and remaining call budget. We derive a sharp recoverability threshold and show that, as sampling proceeds, the observed candidate set can only expand while the set of reachable endpoint winners can only contract, inducing a candidate-level conversion window. Under a specified iid response law, the same state yields exact finite-horizon endpoint probabilities. We further show that merging wrong-answer identities preserves single-call correctness and cannot improve plurality accuracy, and that the effect of redistributing wrong-answer probability depends on the realized vote state. Singleton reachability yields a gold-free exact locking certificate. For a known answer universe, its first trigger is the earliest prefix at which all admissible continuations yield the same fixed-budget output. Empirically, most discovered-but-unselected correct answers lose reachability only after discovery. In a controlled Word16 study, input permutation improves raw-plurality accuracy by 21.1 points with essentially unchanged single-call correctness. Exact locking saves 28-30% of calls at a 16-call budget while preserving every fixed-budget output.

---


### 176. [Scaling and Distilling Text Embeddings for Better Diffusibility](https://arxiv.org/abs/2610.01016)

**<font color=#1a73e8>作者：</font>** Zekai Zhang, Yunjie Tian, Yanjin He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) offer a promising alternative to autoregressive (AR) language generation. Recent advances in continuous DLMs, which apply latent diffusion to continuous text embeddings, raise a practical question: which embedding makes the best latent space, i.e., the most diffusible? To answer this, we search through different embeddings and find that scaling the embedding model to stronger ones within the same family (T5 to T5Gemma-1 to T5Gemma-2) greatly improves generative performance. But the raw T5Gemma-2 embeddings are still not optimal. They are so discriminative that even the embeddings of plausible alternative words are separated, which makes the generation vulnerable to imperfect sampling. Consequently, continuous diffusion often fails to reach any of them and ends up at an invalid embedding instead. To address this, we distill T5Gemma-2 into a student encoder that learns the teacher's decoded probabilities as soft labels. Learning from such soft labels makes the student pull the alternative embeddings closer while maintaining the encoding-decoding mechanism. The distilled embeddings form a more connected and diffusible latent space, improving over the vanilla T5Gemma-2 embeddings. As a result, our medium-sized DLM achieves Gen. PPL 17.8 (against real-text PPL 15.4) at real-text entropy on OpenWebText, outperforming GPT-2-M on Gen. PPL.

---


### 177. [Pay for the Fault, Not the Flow: Label-Free In-Flow Multi-Agent Workflow Optimization](https://arxiv.org/abs/2610.01017)

**<font color=#1a73e8>作者：</font>** Xuehang Guo, Haoyu Wang, Shengyu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly construct multi-agent workflows that decompose a complex task and assign specialist agents from a pool. However, building such a workflow well remains challenging: how finely to divide the task, which agent to trust with each subtask, and when to create a new specialist are all critical decisions a workflow constructor needs to settle up front. Thus, whether each subtask succeeds remains unknown until the workflow runs. Yet, improving a workflow is costly. Locating a fault usually requires a reference answer, a graded outcome, or a trained assessor, and the fix is applied to the whole workflow through re-execution, re-search, or retraining. We propose InFlowOp, which prices every decision in one label-free cost that weighs how well an agent's competence meets what a subtask demands against how much that agent takes to run. Before execution, InFlowOp bidirectionally determines the granularity of task decomposition and agent assignment following from the cost rather than from a fixed template. During execution, InFlowOp corrects a fault with the cheapest move via the same cost that serves the workflow both as it is built and as it runs. Facing the workflow-level evaluation challenge, we introduce Braid, a benchmark whose tasks require multi-agent coordination beyond single-agent capability. Across various domains and backbones, InFlowOp outperforms single agent baselines by up to $+11.97\%$, achieving $+9.64\%$ with in-flow optimization. Our project page: this https URL.

---


### 178. [Towards Automatic Video Annotation with ASH: Zero-Shot Open-Vocabulary Multi-Object Tracking and Segmentation](https://arxiv.org/abs/2610.01022)

**<font color=#1a73e8>作者：</font>** Arash Rocky, Q. M. Jonathan Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memory-attention-based Video Instance Segmentation (VIS) methods have demonstrated strong zero-shot tracking capability, yet their substantial memory requirements confine them to short video clips and their single-prompt inference design makes multi-category open-vocabulary tracking computationally prohibitive. This work introduces two contributions toward fully automated tracking annotation of arbitrary video. The Generalized Presence Token (GPT) reformulates SAM3's inference pipeline to process N text prompts simultaneously via virtual prompt batching, reducing image encoding cost from O(N) to O(1) with no modifications to any learned component. The Annotation and Segmentation Handler (ASH) extends any memory-attention VIS tracker to sequences of arbitrary length through overlapping temporal chunks with IoU-based inter-chunk identity matching, requiring no dataset-specific training. Instantiated on SAM3, the resulting pipeline -- SAM3-ASH -- achieves state-of-the-art HOTA on MOTS20 under fully zero-shot conditions and remains competitive with trained specialists across seven additional benchmarks, while peak GPU memory consumption stays below 25 GB, establishing a practical baseline for scalable, training-free automated video annotation.

---


### 179. [It Takes Workflows to Evolve Better Workflows](https://arxiv.org/abs/2610.01026)

**<font color=#1a73e8>作者：</font>** Xuehang Guo, Haoyu Wang, Haifeng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tackling complex real-world tasks can exceed the capabilities of a single large language model (LLM), motivating the use of multi-agent workflows that coordinate specialized agents to work together on these tasks. Recent methods train LLMs to construct better workflows from execution outcomes, but they optimize only the workflow generator, while the other agents that build or execute each workflow remain fixed even though every outcome depends on all of them. However, extending training beyond the generator is challenging: the agents are coupled, and a workflow's outcome is a single sparse score that cannot tell which agent causes a failure. We propose FloWright, which leverages the workflow as a harness to optimize workflows. By introducing a hierarchical, structure-aware reward paradigm, FloWright enables one role to self-evolve and two or more roles to co-evolve, with no additional models, labels, or executions. Considering the limitation that workflows are commonly trained and evaluated on data that a single agent can already handle, we further propose DataWright, an adaptive data hardening approach that converts existing datasets into workflow-level tasks with increased difficulty. Across document, slide, chart, code, math, and finance tasks, small open models trained with FloWright achieve improved performance by up to $+7.41\%$, with co-evolving ($+5.03\%$) more roles gaining more than optimizing one of them alone ($+2.83\%$). Our project page: this https URL.

---


### 180. [LawCompass: Navigating from Legal QA to Multi-Agent Deep Research with Grounded Evidence](https://arxiv.org/abs/2610.01027)

**<font color=#1a73e8>作者：</font>** Xiaoxia Cheng, Linnan Wang, Jiahao Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) have significantly democratized access to legal information. Nevertheless, most existing legal assistants remain confined to multi-turn conversational QA, failing to support complex legal tasks that require systematic evidence retrieval, multi-step reasoning, and report-level synthesis. In this paper, we present LawCompass, an evidence-grounded legal assistant that navigates the transition from standard Legal QA to multi-agent deep research. LawCompass provides three task-oriented functions: Legal QA, which delivers precise, evidence-backed answers to legal questions; Professional Retrieval, which enables structured exploration of statutes and judicial cases via query rewriting; and Deep Research, which employs a multi-agent workflow to decompose complex legal tasks and synthesize comprehensive research reports. Crucially, LawCompass maintains explicit citation links across all modules, empowering users to directly verify system outputs against original legal sources. Evaluation results demonstrate that LawCompass provides a practical and scalable paradigm for transforming conversational AI into trustworthy and evidence-grounded legal research assistance.

---


### 181. [SLIM: Simplex-Lattice Interpolation Merging](https://arxiv.org/abs/2610.01037)

**<font color=#1a73e8>作者：</font>** Seongcheol Jeong, Masahiro Suzuki, Yutaka Matsuo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing merging coefficients for large language models can require many costly benchmark evaluations. We propose \textbf{Simplex-Lattice Interpolation Merging (SLIM)}, which constructs a quadratic surrogate of aggregate performance on the coefficient simplex using a classical mixture design. Evaluations of individual experts and equal-weight pairs determine the surrogate with the minimum number of measurements needed to identify a general quadratic on this domain. SLIM then optimizes the surrogate without further target-metric evaluations. Experiments on two model architectures demonstrate accurate prediction of unseen multi-expert mixtures and competitive merge performance under limited evaluation budgets. Matched-budget comparisons show that structured evaluation points improve prediction fidelity over random designs, including those using regularized fitting.

---


### 182. [Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems](https://arxiv.org/abs/2610.01042)

**<font color=#1a73e8>作者：</font>** Shixuan Li, Wei Yang, Peiyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent communication aims to help agents benefit from one another's information. Yet improvements in system performance leave a fundamental ambiguity: do they reflect effective communication, a favorable agent architecture, or simply additional reasoning? Because communication methods are commonly evaluated within the systems they were designed for, these factors are difficult to disentangle. Final accuracy further merges corrected errors and corrupted answers into a single outcome, obscuring how communication changes decisions. We introduce Independent--Communicate--Revise (ICR), a controlled framework that evaluates communication as answer revision following independent reasoning. ICR fixes initial reasoning trajectories, measures correction and preservation conditional on both agents' initial correctness, and uses a no-message revision control to quantify gains beyond additional reasoning. Across four reasoning benchmarks, our audit of textual and latent communication reveals that similar aggregate accuracy can conceal substantially different revision behaviors. Compared with transmitting answers alone, full reasoning increases correction while reducing preservation on all four benchmarks, so richer messages amplify beneficial and harmful influence alike. Receiver-policy comparisons on MedQA and GPQA-D further show that a structured verification policy shifts every channel toward greater preservation and lower correction, while its effect on selectivity varies across channels and tasks. These findings challenge treating communication quality as an intrinsic property of a channel. ICR therefore recenters evaluation on selective revision, providing a unified framework for examining how message content and receiver policies jointly produce benefits and harms.

---


### 183. [Sentence Specificity Scores for Collaborative Technical Documentation: A Domain-Transfer Study](https://arxiv.org/abs/2610.01046)

**<font color=#1a73e8>作者：</font>** Rocker D'Antonio, Thomas Benton Townsend, Dimitrios Michael Manias  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Collaboration depends on shared context, and technical documentation is one way that context persists across people and AI teammates. Specificity, the amount and exactness of detail expressed in language, shapes what information documentation captures and how precisely that information is communicated. This work audits sentence-specificity scoring artifacts on technical documentation and tests whether scores applied only after generation help choose among fixed LLM-generated revisions. Across Wikipedia and three technical-documentation corpora, the fixed general-domain predictor SpeciTeller and the pinned post-publication author-repository implementation of Ko et al.'s target-adapted predictor produce different corpus orders and same-sentence rank agreement from -0.066 to 0.510. Strict filtering and token-length adjustment change these patterns without reconciling them. In the Gemma set, SpeciTeller ranking raises direction-valid selection from 71.7% to 83.3% (+11.7 points; 95% source-case bootstrap interval +1.7 to +21.7); in the GPT-OSS-120B set, SpeciTeller ranking raises direction-valid selection from 51.7% to 56.7% (+5.0 points; 95% source-case bootstrap interval -6.7 to +16.7), and every primary single-score GPT-OSS-120B interval includes zero. These findings tie score interpretation and decision value to the predictor and candidate set.

---


### 184. [Network World Models as Environments for Algorithm Design on Complex Systems](https://arxiv.org/abs/2610.01048)

**<font color=#1a73e8>作者：</font>** Rishab Alagharu, Hongji Pu, Zeeshan Memon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models, which simulate an environment and predict how it changes under actions, are increasingly used in real-world applications such as robotics. Complex systems call for the same tool because the effect of an action is not immediate. Seeding nodes for a campaign, or immunizing nodes against an epidemic, changes little on its own; what matters is the outcome that unfolds over the steps that follow. Designing an algorithm that selects such actions to maximize expected performance on a task is inherently iterative, and every candidate must be scored by the outcome it produces. Obtaining that outcome has relied on simulation, whose cost becomes a bottleneck when candidates are evaluated over many sampled trajectories. We propose an action-conditioned Network World Model that learns a network's diffusion dynamics under interventions over time, applies each action to the network, and predicts the outcome that follows. It serves as a fast evaluator inside an algorithm design loop in which a coding agent designs and refines executable algorithms using feedback from full rollouts, action-level credit, and counterfactual probes over alternative interventions. Across eight network tasks and five diffusion models, the designed algorithms match or exceed the strongest reported baseline in 138 of 141 settings while enabling up to 14.5 times faster rollouts than Monte Carlo simulation. Code will be released upon acceptance.

---


### 185. [Capturing In-Context Learning Dynamics with Task Operators](https://arxiv.org/abs/2610.01054)

**<font color=#1a73e8>作者：</font>** Guangzhi Xiong, Zhenghao He, Bohan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) enables language models to perform new tasks from demonstrations without weight updates. However, every ICL inference requires processing the full set of examples, resulting in inefficient deployments, and how ICL works mechanistically is not fully understood. Prior work compresses ICL into fixed activation vectors extracted from specific layers or positions, but these input-independent interventions fail on complex tasks where the output depends on fine-grained interactions with the input. By analyzing the ICL forward pass, we show that each attention head's output is an affine transformation of its context-masked counterpart, and that the parameters of this transformation are empirically stable across samples for a given task. Building on this, we introduce Task Operator (TO), which replays this transformation as an analytically derived update to the attention output projection. Across lexical, algorithmic, and reasoning tasks, TO achieves the best overall performance among prior methods and substantially narrows the gap between zero-shot inference and ICL. We further show that the extracted knowledge concentrates in a task-specific sparse circuit across layers and positions, and that averaging operators from disjoint demonstration batches enables effective many-shot scaling without expanding the context window. Our code is available at this https URL.

---


### 186. [Kernelized Activation Steering](https://arxiv.org/abs/2610.01062)

**<font color=#1a73e8>作者：</font>** Laziz U. Abdullaev, Minh-Hieu Pham, Bach Do 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering provides a simple, training-free mechanism for controlling attributes of generative models such as sentiment, style, and helpfulness. However, standard approaches such as Difference-in-Means apply a single input-independent steering vector across all activations, limiting expressivity and ignoring the local geometry of the activation space. We propose Kernelized Activation Steering (KAS), a unifying framework that lifts activation steering into a reproducing kernel Hilbert space. KAS formulates steering as an optimization problem expressed purely via kernel evaluations, yielding an implicit, activation-dependent steering score without constructing explicit feature maps. Unlike DiM, KAS induces locally adaptive steering: each activation is modified according to its relative position with respect to source and target reference sets, producing a nonlinear steering field over the representation space. Importantly, DiM is recovered as a special case under a linear kernel, while richer kernels enable geometry-aware interventions. Across standard activation steering tasks, including jailbreaking LLMs and image style control, KAS outperforms or is on par with the existing methods.

---


### 187. [Probe with Participation Trophies: Random-Reward RL as a Probe of LLM Capability](https://arxiv.org/abs/2610.01066)

**<font color=#1a73e8>作者：</font>** Yu Mao, Lei Yu, Zining Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We connect the spurious-reward paradox to a model's reachability and propose random-reward reinforcement learning (RL) as a useful tool for the probing enterprise, addressing a decade-long debate over what probing performance actually reveals about a model. There are two prevailing explanations for the surprising finding that even random rewards can improve the performance of large language models (LLMs): one attributes the gains to particular mechanisms within RL training; the other to data contamination. Our results motivate a different view: spurious-reward RL can probe a model's reachability, or what further training can attain from its current state under specified constraints, beyond what is reflected in its current performance. Two OLMo checkpoints with the same accuracy on synthetic arithmetic (3.5%), for example, reach 8.5% and 55% in their best runs under the same correctness-rewarded RL. Examining OLMo checkpoints across pre-training and mid-training reveals three distinct regimes of training response: early on, RL produces little improvement even when correct answers are rewarded; later in pre-training, rewarding correct answers becomes effective while random rewards remain weak; and, upon entering mid-training, even random rewards can produce large gains. A similar ordering appears in a number-masked supervised fine-tuning (SFT) analysis of these checkpoints, suggesting that the pattern is not specific to a particular RL mechanism. Moreover, RL with random rewards offers a distinctive perspective on what training can make an LLM do, since its reward signal supplies no information about which answers are correct. By asking what training can attain without correctness feedback, it addresses the label-leakage side of a central problem in decodability-based probing: whether a successful probe reveals the model's capabilities or learns the task itself.

---


### 188. [GLoC-EHR: Evidence-Cited Clinical Reasoning over Global Context and Local EHR Events](https://arxiv.org/abs/2610.01076)

**<font color=#1a73e8>作者：</font>** Chaiho Shin, Kwangsoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured electronic health records (EHRs) contain a patient's clinical trajectory as a sequence of clinical codes. Answering clinical questions from such records requires both the context of the whole trajectory and the specific events that support the answer. We introduce GLoC-EHR, a multimodal language model that reads a contextual encoding of the record through a fixed-size global memory of the trajectory and a local memory of selected events. The model learns to generate hospital-course summaries from the global memory and descriptions of masked concepts from the local memory, aligning both with clinical text. It is then trained to cite evidence before answering, through rationale fine-tuning followed by group relative policy optimization (GRPO) with rewards for correct answers and record-supported evidence. On three MIMIC-IV outcome tasks, GLoC-EHR attains the highest macro AUROC among the compared models when it answers directly, whereas zero-shot LLMs reading the serialized record fall far behind. With evidence-cited reasoning, it stays close to its direct multi-task counterpart in macro AUROC, and the evidence terms of the objective reduce unsupported evidence at a similar macro AUROC. The local memory adds distinct supported findings, particularly under strict matching, without a detectable change in macro AUROC. Without retraining, GLoC-EHR transfers to EHRSHOT on par with EHR-BERT and answers two unseen laboratory questions better than zero-shot prompting of its own backbone.

---


### 189. [Jev-IDS: System One Models for Network Intrusion Detection](https://arxiv.org/abs/2610.01079)

**<font color=#1a73e8>作者：</font>** Paulo Severo, Silvio E. Quincozes, Amanda Dias  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine-learning Network Intrusion Detection Systems (IDS) depend on substantial labeled datasets and task-specific training, whereas Large Language Models (LLMs) detection can analyze flow records directly but incurs higher inference cost and latency, with less constrained outputs. This paper presents JEV-IDS, an open experimental general NIDS based on the Jev System One Model (SOM) to detect zero day intrusions Under label scarcity. JEV-IDS serializes one flow per request and asks JEV two questions: a binary attack probability and a finite-choice traffic category. Our results show that, at k=1, JEV was 4.8 times faster and 3.8 times cheaper than GPT-5.6 Luna, with 1.5 times higher novel-attack recall; it also produced 15 times fewer false alarms than a low-data Random Forest. Across 5,400 decisions on a 300-flow NSL-KDD pilot split, JEV achieved F1-Score 0.859, precision 0.941, recall 0.790, and novel-attack recall 0.838. Increasing k to 2 reduced its F1-Score to 0.839.

---


### 190. [Improving Math Reasoning through Value-guided Informative Search](https://arxiv.org/abs/2610.01080)

**<font color=#1a73e8>作者：</font>** Shaohuai Liu, Yuning Wu, Haoran Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has substantially improved the mathematical reasoning capabilities of large language models. Recent work introduces search into RLVR rollouts to increase trajectory diversity, but diversity alone does not ensure that the search-induced rollout policy improves upon the current policy. To address this gap, we propose APIVIS, a training-time framework that adapts finite-budget Gumbel search to chunk-level mathematical reasoning. APIVIS combines direct and searched responses within each rollout group, allowing improvements found by search to produce informative relative rewards. It further applies selective supervision to search-improved tokens, preserving a learning signal when uniform group rewards render GRPO ineffective. We show that exact value-guided selection improves the expected verifier reward at each searched state and that this guarantee extends to the complete rollout policy, with a corresponding approximate guarantee under bounded value-estimation error. Experiments on widely recognized mathematical reasoning benchmarks and different model scales demonstrate substantial improvements over competitive search-based methods, validating the effectiveness of APIVIS.

---


### 191. [AgSpec: Pushing the Limits of Retrieval-Based Speculative Decoding in Coding Agent Pipelines](https://arxiv.org/abs/2610.01108)

**<font color=#1a73e8>作者：</font>** Sumin Lee, Sukmin Cho, Suengjae Lim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-based speculative decoding (SD) drafts tokens by copying continuations from existing text, which suits coding agents that repeatedly reproduce code, logs, and earlier attempts. Yet existing methods fall short in agent pipelines: much of the reusable text is missing from their corpora or stored in a form that differs from what the agent emits, and their draft lengths ignore that accept length varies across agents and drifts over turns. We present AgSpec, a framework that supplies the corpus and draft-length policies that existing retrieval engines lack in coding-agent pipelines. AgSpec retrieves from session, workspace, and global corpora, retaining the ongoing session trajectory and indexing opened files in the agent's emission format. It bounds each agent's draft length with an offline-profiled cap and adapts the length online from verification feedback. On two repository-level multi-agent coding benchmarks, AgSpec outperforms five retrieval-based drafters and EAGLE-3 in most evaluated settings, raising generation throughput over autoregressive decoding up to 4.37$\times$ at batch size 1 and 4.76$\times$ at batch size 16. AgSpec also remains effective on benchmarks without a repository or a multi-agent pipeline, showing that its gains generalize to coding agents broadly.

---


### 192. [How Much Can Language Models Gain from Test-Time Computation?](https://arxiv.org/abs/2610.01110)

**<font color=#1a73e8>作者：</font>** Bangji Yang, Jingyuan Li, Jiajun Fan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How much can test-time computation improve a language model, and at what cost? Test-time scaling is widely proposed as a substitute for larger models, but existing comparisons mostly evaluate one domain at a time and rarely charge selection to the budget. We introduce SELF-POT, a benchmark and evaluation framework that measures the test-time potential of a model across competition mathematics, competitive programming, and agentic workflows. SELF-POT separates candidate coverage from final accuracy on static tasks, tracks correctness transitions under revision, and measures protocol completion alongside task success in agentic environments. Under a unified budget rule, it compares Direct inference with parallel sampling and self-revision under fixed multiples of the Direct budget, and charges every model call, including selection and critique, in dollars. This design supports two kinds of comparison: the gain a model obtains from additional inference, and a lower-cost model with additional inference against a stronger model. Across five low-cost reasoning models on 350 sealed tasks, with Claude Opus 5.5 Direct as the reference, the returns depend on the domain, the selection rule, and failure handling. When we replay the retained programming candidate pools, public-example selection raises correct submissions from 376 to 453 of 500 scheduled cells while saving 12-49% of logical API cost across models, and simply retaining an available candidate when judging fails recovers 61 submissions at unchanged cost. On identical mathematics pools, judging with fallback yields 186 correct submissions versus 182 for voting, while voting saves 12-21% of logical API cost. These controlled replays show how selection and failure handling change the gains realized from the same generated candidates, and they quantify the marginal value of a model judge.

---


### 193. [Beyond State-of-the-Art: Standardising Environmental Impact Metrics for AI Research](https://arxiv.org/abs/2610.01116)

**<font color=#1a73e8>作者：</font>** Lachlan McGinness, Dan Pagendam, Robert Offner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the capabilities and ubiquity of Large Language Models (LLMs) grow, so does their environmental footprint. Despite calls for responsible AI, the machine learning community lacks standardised practices for carbon accounting. Our automated literature review of the 5,285 papers accepted to NeurIPS 2025 reveals that reporting of environmental impact is nearly non-existent. To catalyse a shift toward sustainable AI, we define standardised sustainability metrics for evaluating model training efficiency, accompanied by simple heuristics to estimate the carbon cost of LLM inference. We implement these metrics in carbonbenchmark, a drop-in software solution for tracking and reporting emissions.
Finally, to combat the pursuit of marginal accuracy gains at disproportionate environmental costs, we formalise the `Smallest Model that Achieves the Job' (SMAJ), a framework which challenges the field to prioritise computational efficiency and environmental accountability alongside traditional `State-of-the-Art' (SotA) accuracy.

---


### 194. [Madeleine: Learning Involuntary Recall for Conversational Memory from Simulated Lives](https://arxiv.org/abs/2610.01118)

**<font color=#1a73e8>作者：</font>** Zhiyun Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A long-term conversational assistant must recall the right memory at the right moment, yet the memory that matters most is often not similar to what the user says now. Current systems recover such associations by letting an LLM reason at write or read time, at a cost of hundreds to over a thousand LLM calls per memory bank and up to several thousand context tokens per query. We argue that association is a learnable relevance: the pointwise mutual information of memories under how human lives unfold. We introduce Madeleine, which learns amortized association: offline, an LLM life simulator writes simulated lives, whose cue-trigger pairs teach a query encoder a residual association on top of frozen similarity; online, it calls no LLM and plugs into any vector memory by replacing only the query encoder. On LoCoMo-Plus under the official protocol, Madeleine (I) reaches 66.6 when plugged into HyperMem, the highest among all systems evaluated under this protocol; (II) used alone, reaches the score of HyperMem as released (52.4 vs. 52.9) with zero LLM calls and about 1/21 of its answer context; and (III) lifts T-Mem by 26.2 points, significantly outperforms the same untrained backbone inside both systems, and leaves ordinary QA intact on the 4B backbone.

---


### 195. [AbsorbEvo: An Agentic Framework for Autonomous Inverse Design of Microwave Absorbers](https://arxiv.org/abs/2610.01119)

**<font color=#1a73e8>作者：</font>** Zhicheng Feng, Yubo Zhao, Xuefeng Yao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing high-performance microwave absorbers requires specialized expertise in electromagnetic theory, materials science and simulation programming, and entails time-consuming optimization. Here, we present AbsorbEvo, an agentic framework for autonomous inverse design that translates natural-language performance objectives into designs verified by full-wave simulations. Its candidate evolution strategy integrates language reasoning, physics-based prediction and historical feedback. A large language model proposes the directions and magnitudes of parameter adjustments based on task objectives and computational history. The system combines directed increments with global sampling to generate candidates and uses a low-cost predictive model as a physics prior to rank them. Only high-ranking designs undergo full-wave simulation. Results passing physical validity checks are used to evaluate performance and guide subsequent search. Experience from training tasks is further distilled into textual skills, which are independently validated before use in new tasks. Under identical proposal budgets on held-out AbsorbBench-36 tasks, AbsorbEvo achieved a task success rate of 79.17%, versus 25.00% for a generic agent and 12.50% for random search. Its mean best coverage was 0.7816, compared with 0.6434 and 0.6448, respectively. By integrating language reasoning and physics-based feedback into design decisions, AbsorbEvo provides a methodological foundation for natural-language-driven autonomous inverse design of microwave absorbers.

---


### 196. [Counting and Min-Cost Encoding for Tokenization in Large Language Models](https://arxiv.org/abs/2610.01127)

**<font color=#1a73e8>作者：</font>** Shuming Shi, Xiang Zhang, Hao Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mainstream large language models rely on a tokenizer to encode text into a token sequence. Different tokenizers may yield token sequences of substantially different lengths for the same text. With a fixed model architecture, shorter token sequences correspond to lower inference time. We propose a tokenizer training approach named Counting and Filtering (CNF) and a text encoding algorithm called Min-Cost Encoding (MCE). MCE defines a cost function over a text segment, and determines the best segmentation by globally minimizing the overall segmentation cost. CNF builds a raw vocabulary by directly counting valid substrings, and then constructs the final vocabulary through a filtering step based on actual token usage when segmenting the training corpus with MCE. The CNF-MCE conbination offers several advantages over BPE, including higher token efficiency, greater scalability, and lower dependency. Across six text categories and two vocabulary-size groups, CNF-MCE consistently achieves better compression than the evaluated BPE tokenizers. With a 250K vocabulary, CNF-MCE increases compression rate by 26% and 30% on English web text over the o200k_base and qwen250k tokenizers. Experiments scaling the vocabulary to 1M entries on English web text demonstrate sustained improvements over BPE, with a token efficiency improvement of over 60% and vocabulary utilization rising from 52.9% to 96.9%. The MCE algorithm does not depend on a merge list (as in BPE) or token probability (as in UnigramLM), making it applicable to a wide range of vocabularies, including those built from BPE, UnigramLM, CNF, and others. Language models trained from scratch at the 1.8B and 8B scales achieve comparable average performance to models using the BPE tokenizers across 11 benchmarks. These results demonstrate that CNF-MCE can improve token efficiency significantly while maintaining competitive downstream performance.

---


### 197. [Grounding Large Language Models in DSGE Simulators for Policy Generation and Forecasting](https://arxiv.org/abs/2610.01128)

**<font color=#1a73e8>作者：</font>** Aditya Dubey, Namah Gupta, Vinti Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can produce economic policy responses that sound reasonable, but this does not show that their actions are consistent with economic dynamics. We test this by placing an instruction-tuned language model inside six Snowdrop-backed dynamic stochastic general equilibrium (DSGE) simulators. At each turn, the model observes the economy and a change in economic discourse, selects a bounded policy action, and receives the next simulated state and an economic reward. We implement a common Python interface for repeated rollouts, persistent shocks, state cloning, and rolling-horizon simulation.
This setting creates a long-horizon credit-assignment problem. Policy effects may appear several quarters after an action is taken. PPO has a learned value function that can propagate delayed reward to earlier tokens through generalized advantage estimation. GRPO has no learned value function and instead assigns a group-relative advantage from complete rollout returns. It therefore cannot distinguish which earlier turn caused the outcome; if every rollout receives the same return, the normalized advantage is zero. We use PPO as the primary method and GRPO as a matched critic-free baseline. The experiments also test directional semantic signals, reward horizon, trajectory warm starts, cross-simulator transfer, and historically anchored pandemic and monetary-policy shocks. The objective is to judge policy actions by their simulated economic consequences rather than by plausible language alone.

---


### 198. [Does Scaling Reinforcement Learning Really Require More Training?](https://arxiv.org/abs/2610.01133)

**<font color=#1a73e8>作者：</font>** Bangji Yang, Jiajun Fan, Hongba Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling reasoning typically spends more compute on reinforcement learning (RL) or on inference. We show that a completed RL training history can yield policies stronger than the checkpoints visited by its optimizer. We call this policy-space scaling: expanding the deployable policy set accessible from a fixed RL history, without extending training or increasing per-query inference computation. We instantiate it with SURGE (Scaling Up RL Gradient-free via Eigenspace fusion). SURGE combines two checkpoints from the same RL run: a high-accuracy anchor and a competitive donor that generates shorter responses. It expresses both checkpoints as changes from their shared initialization, then spectrally decomposes the anchor's update to retain its dominant component and incorporate the donor's complementary component. With a fixed target for how much of the anchor update to retain, SURGE determines the block size from the weights without testing candidate policies. We evaluate two 1.5B mathematical-reasoning histories, DeepSeek and Nemotron, and one 7B coding history, OLMo. SURGE improves benchmark-average accuracy over both input checkpoints while using fewer reasoning tokens than the anchor. It reaches 54.17% on DeepSeek AIME24 against a measured native maximum of 50.83%, and 83.7% on OLMo HumanEval+ against 82.8%. These gains exceed the observed training curves. Geometric controls support the importance of RL-update structure beyond weight displacement or token reduction alone. Each constructed model runs as a single policy. Our findings identify stored RL history as a reusable scaling resource: the capability available from a training run need not end at its best checkpoint.

---


### 199. [Auditing Action Settlement in LLM Agent Environments: Order, Progress, and Replay](https://arxiv.org/abs/2610.01138)

**<font color=#1a73e8>作者：</font>** Haotian Chen, Bowen Ye, Yuning Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Concurrent actions in large language model (LLM) agent environments require arbitration even when each proposal is individually valid. We implement a typed snapshot-settlement contract and audit three distinct properties: order sensitivity, useful progress, and replay consistency. Five settlement policies are tested in 28,800 exhaustive permutation trials and 2,160 scripted multistep episodes. Joint policies are spatially order-invariant conditional on fixed priorities, yet conservative rejection completes only 31.25% of agents in a six-agent doorway task versus 90.28% for random tickets; the paired improvement is 59.03 percentage points (95% bootstrap interval: 50.00-68.06). All policies preserve the tested spatial constraints, and priority arbitration still misses the independent small-instance optimum. A separate full-state journal audit exactly replays 156 checkpoints and rejects 1,332 constructed corruptions with a retained terminal anchor. The evidence concerns execution semantics, not human realism or long-run fairness.

---


### 200. [Looping Beyond Twice: A Scalable Recipe for Looped Mixture-of-Experts](https://arxiv.org/abs/2610.01153)

**<font color=#1a73e8>作者：</font>** Di He, Pengxiang Li, Da Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers introduce recurrent depth as a new scaling axis for LLMs: by repeatedly applying shared Transformer blocks, they increase effective depth without increasing parameter count. However, the benefits of looping remain unclear for large MoE LLMs under FLOPs-matched comparisons. The main reason is that the gains from additional iterations diminish quickly and can even turn into degradation, so the extra FLOPs spent on looping yield little substantial improvement. Consequently, prior work typically settles on two loops. We identify two main obstacles to scaling looped MoE. First, looping inherits and amplifies the curse of depth: hidden-state variance grows with each iteration as residual updates accumulate, which destabilizes deep recurrence and causes representations to drift. Second, looped MoE suffers from expert selection collapse: routers repeatedly select the same experts across loops, so extra iterations add computation without adding computational diversity. Guided by this diagnosis, we propose LOOM, built on a single principle: each loop should contribute new computation while keeping the recurrent state stable. LOOM stabilizes recurrence by scaling residual updates to bound variance growth and re-injecting the input embedding at every loop, and diversifies it through per-loop routers that engage different experts and a Looping Residual that carries earlier outputs forward. Experiments across 100M-1.7B models show stable scaling to 9-12 loops. Under near-iso-FLOP, the 700M model performs best at 5 loops, reducing perplexity from 18.36 to 16.54 and improving average zero-shot accuracy from 38.84% to 39.53% over the non-looped baseline. Without FLOP matching, the 1.7B model trained on 60B tokens peaks at 9 loops, reducing perplexity from 9.62 to 7.77 and improving average zero-shot accuracy from 42.4% to 47.7%. Code is available this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-384](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
