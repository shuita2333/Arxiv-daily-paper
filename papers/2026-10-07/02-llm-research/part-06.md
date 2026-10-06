# 🧠 大模型相关研究 | 2026年10月07日

> 本类共 **505** 篇论文：已确认 **467** 篇，待复核 **38** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

---

### 251. [Answer with Evidence: Consistency-Aware Grounded Visual Question Answering for Roadside Traffic Scenes](https://arxiv.org/abs/2610.05274)

**<font color=#1a73e8>作者：</font>** Runwei Guan, Rongsheng Hu, Shangshu Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Roadside traffic reasoning requires every free-form textual claim to be backed by visual evidence. Existing grounded multimodal large language models (MLLMs) frequently exhibit say-point mismatch, in which the textual answer contradicts the bounding boxes the model localizes. Evaluation metrics that score answers and boxes separately leave this failure unpenalized. We trace the mismatch to the conventional answer-then-ground factorization, which commits to a numerical claim before any object is enumerated. To measure it, we build RoadSceneVQA-G, a benchmark of 34.7K question-answer pairs in which every free-form answer is linked to the set of boxes that witnesses it, and we propose the Answer-Grounding Consistency (AGC) evaluation suite. To address it, we introduce Enumerate-then-Answer (EtA), which reverses the generation order so that answer-evidence agreement becomes a property of the output structure, and Enumeration-Consistent Policy Optimization (ECPO), a reinforcement learning stage that uses the union of multiple rollouts as a recall teacher without ground-truth boxes. EtA raises say-point consistency from 26.6\% to 93.7\% and grounding F1 from 52.2\% to 73.0\%, and ECPO further increases F1 to 75.6\% without per-box supervision. On gRefCOCO, the same framework outperforms the strongest compared method, indicating that it transfers beyond traffic scenes. The project is available at \url{this https URL}.

---


### 252. [Inductive Claims Extraction at Scale](https://arxiv.org/abs/2610.05275)

**<font color=#1a73e8>作者：</font>** Sandrine Chausson, Björn Ross  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A large part of political discourse on social media is built and expressed at a level of claims: i.e. declarative, typically single-clause statements, which convey a particular interpretation of reality and can range from factual to evaluative. Moreover, rather than occurring randomly, claims coalesce, recur in patterns, and come to be associated with different world views. When paired with structural computational tools such as Social Network Analysis, claims can be a powerful unit of analysis to study political phenomena such as echo chambers or polarisation. In this paper, we present a pipeline that uses a large language model (LLM) to inductively extract and catalogue claims from large social media corpora, and apply it to two different Twitter datasets: one relating to the 2020 US presidential election and the other to the 2022 FIFA World Cup. We comprehensively evaluate the approach by measuring the pipeline's recall and precision against manually annotated samples, run ablation studies isolating the contribution of its various components, and perform a qualitative error analysis. We discuss the value of the approach in the context of Computational Social Science research, and illustrate its capabilities by presenting the claims catalogue obtained from each dataset.

---


### 253. [Fusion is the New Mutation: Bandit-Guided Evolution on Workflow Graphs](https://arxiv.org/abs/2610.05284)

**<font color=#1a73e8>作者：</font>** Zhiwei Shang, Jiahang Sun, Mingrong Gong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated agentic workflow optimization relies on costly evaluations, making it essential to allocate a limited evaluation budget effectively. Multi-parent fusion can reuse designs from previously discovered workflows, but identifying promising parent combinations requires learning from limited fusion feedback. We introduce DAGO (Directed Acyclic Graph Optimization), a contextual-bandit-guided framework that learns which parent workflows to fuse under a limited evaluation budget. DAGO formulates each candidate parent combination as an arm, represented by pretrained embeddings of its constituent workflows' code and prompts. A diagonal LinUCB policy learns a shared reward model across arms and balances exploitation of arms with high predicted offspring quality against uncertainty-driven exploration. After an arm is selected, an LLM generates a child workflow through summary-guided fusion, and the child's validation score serves as the reward for updating the bandit. A shared directed acyclic graph maintains discovered workflows and their multi-parent lineage, providing an expanding pool of parents for subsequent arm proposals. Across six benchmarks covering mathematical reasoning, code generation, and question answering, DAGO achieves the highest macro-average score among the evaluated baselines. Under matched validation-evaluation budgets, it improves over AFlow from 80.3 to 81.7 while reducing aggregate search expenditure by 11.2%. Ablation studies show that LinUCB-guided arm selection outperforms both random selection and its exploration-free variant, supporting the value of feedback-driven selection and exploration-exploitation balance.

---


### 254. [Erased, Rerouted, or Rescaled? Post-Training and the Causal Quotient of a Language Model's Belief State](https://arxiv.org/abs/2610.05292)

**<font color=#1a73e8>作者：</font>** Weihan Li, Tianshi Zheng, Junhao Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What happens to information a pretrained model already encodes when post-training no longer rewards using it? The common language of representation compression conflates three fates: information may be erased, rerouted away from the decision while still represented, or rescaled to occupy less variance while still represented and used. We make these fates identifiable in models whose pretraining recovers Bayesian belief states. A reward that reads only a coarse function of the hidden state defines an exact reward-null kernel. The kernel lets us separately measure whether the information remains recoverable, whether decisions causally depend on it, and how much activation variance it occupies. Theory says what is protected: KL-anchored reinforcement learning preserves the reference policy's log-odds among equally rewarded outputs, supervised and unanchored objectives carry no such constraint, and spectral compression implies neither erasure nor loss of use. In controlled worlds, post-training mostly reroutes or rescales reward-null information and leaves it decodable. Without an anchor decisions can stop using it although the representation survives, and with one they keep using it. Erasure appears only under prolonged weight decay, for distinctions that neither reward nor next-token prediction can see. Open language models show the same dissociation: in-context belief geometry stays decodable under late-layer spectral compression, and within-class behavior depends on the anchor. Post-training thus selects a causal quotient of the pretrained belief state: the reward defines decision-equivalence, the anchor and the state update protect part of what it ignores, and optimization decides whether the rest is erased, rerouted, or rescaled.

---


### 255. [MESH-Harness: Self-Improving Agent Harnesses via Bandit-Guided Compositional Evolution](https://arxiv.org/abs/2610.05300)

**<font color=#1a73e8>作者：</font>** Zhiwei Shang, Yu Huo, Mingrong Gong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent harness is the code that organizes context, maintains state, and coordinates tool calls for a language model. We study how to improve the harness under a limited evaluation budget while keeping model weights fixed. Our method, MESH-Harness, organizes each harness into functional modules with explicit role-specific interfaces, allowing alternative implementations of each module to be substituted and recombined. It uses shared module representations and full-covariance LinUCB to score candidate combinations based on predicted performance and exploration value. Mixed-start coordinate ascent selects complete configurations for evaluation without enumerating the combinatorial space. Validation traces then guide local code edits, and the resulting candidates are incorporated into fixed-capacity role-specific pools for subsequent recombination. On text tasks, retrieval-augmented mathematical reasoning, code generation, and interactive scientific tasks, MESH-Harness outperforms Meta-Harness by 5.70, 7.01, 2.00, and 5.00 points, respectively, under matched candidate-evaluation budgets. Iterative harness optimization improves MESH-Harness by 5.63-7.79 points over its first-round configurations. For the reported configurations, aggregate test-time cost is 44.2% lower than that of Meta-Harness, while total cost including search is 14.6% lower. These results show that combining module-level design reuse with feedback-driven compositional search can systematically improve agent harnesses while keeping overall optimization cost under control.

---


### 256. [ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience](https://arxiv.org/abs/2610.05303)

**<font color=#1a73e8>作者：</font>** Haodong Lu, Dong Gong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination. Deployed agents face streams of related tasks, making their trajectories a natural resource for improvement. In-context adaptation agents store reflections, memories, or skills as text, so reuse depends on retrieving the right experience and on a frozen policy executing it. We study Online Agentic Test-Time Training (OaTTT), which trains the LLM's weights on its own execution trajectories during deployment. The agent executes each task once, in one pass over the stream, and the executed trajectory with its verification result is the only learning signal for weight updates that persist across tasks. Directly imitating or reinforcing the generated tokens of this single attempt destabilizes the policy. We introduce ASCENT (Agentic Self-distillation for Cross-task EvolutioN at Test-time), which instead self-distills verified experience. A stable version of the LLM, its frozen initial copy, receives the verified trajectory as privileged information and predicts next-token distributions along it with this hindsight. Distilling them into persistent LoRA fast weights updates the agent for later tasks, without an external reference solution or stronger teacher. By further removing invalid-action turns, ASCENT distills enhanced privileged experience for more efficient execution. We characterize its population target and the limits of sparse outcome selection. Across ALFWorld, WebShop, and AppWorld at varied model scales, ASCENT improves task success and interaction efficiency as experience accumulates, outperforms online adaptation methods, and transfers to held-out scenes, showing that an agent can consolidate verified experience into its weights without a separate training phase or memory retrieval. Project page: this https URL

---


### 257. [RubricArmor: Adversarial Evolution Improves LLM-Based Rubric Generation](https://arxiv.org/abs/2610.05308)

**<font color=#1a73e8>作者：</font>** Haocheng Yang, Yuchao Zhang, Licheng Pan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning (RL) provides interpretable rewards for aligning large language models (LLMs) by evaluating responses against query-specific evaluation criteria. To construct rubrics at scale, a straightforward approach to LLM-based rubric generation is to prompt an LLM to generate a rubric directly from the query. However, rubrics directly generated by LLMs are vulnerable to reward hacking, since omitted or underspecified criteria allow the policy to obtain high rubric rewards with low-quality responses. Existing LLM-based rubric generation methods improve the granularity and coverage of the generated criteria but do not proactively guard against reward hacking. To address this limitation, we propose RubricArmor, an adversarial framework that exposes and mitigates potential reward hacking at the rubric generation stage before it occurs in subsequent RL. Specifically, RubricArmor performs adversarial evolution, in which an attack step and a repair step alternate over multiple rounds. The attack step simulates the reward hacking of the policy by constructing adversarial responses that satisfy the current rubric but fail to properly complete the task. The repair step then revises the rubric to detect the response defects exposed by the attack step while preserving other valid criteria. Extensive experiments demonstrate that RubricArmor outperforms competitive rubric generation baselines and translates into more effective downstream rubric-based RL.

---


### 258. [Robust Parameter-Efficient LLM Adaptation on Analog Hardware](https://arxiv.org/abs/2610.05318)

**<font color=#1a73e8>作者：</font>** Jindan Li, Zhaoxian Wu, Tianyi Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analog in-memory computing is a promising platform for on-device execution of large language models because it performs matrix--vector multiplications (MVMs) in memory and in parallel, reducing data movement. However, limited digital-to-analog converter precision, input noise, and finite conductance states can degrade model accuracy, while full-model retraining to address these effects can be costly. We develop an optimizer-agnostic, parameter-efficient adaptation method based on Low-Rank Adaptation (LoRA), keeping the pretrained weights stored on analog arrays fixed while training the LoRA weights to adapt to downstream tasks and hardware non-idealities. Reliable adaptation requires handling errors in both forward and backward MVMs and physical weight updates. We use input reshaping to reduce input-induced MVM errors and update accumulation to retain small updates before programming them to finite-state analog devices. Across Llama-3.2-1B-Instruct and Llama-3-8B with both Muon and AdamW, input reshaping improves analog LoRA fine-tuning under noisy MVM computation. Update accumulation separately preserves sub-threshold updates and substantially improves adaptation under finite-resolution programming, including configurations with as few as 20 conductance states. Additional experiments show consistent held-out negative log-likelihood improvements across noisy analog settings.

---


### 259. [When Does Longer Reasoning Help? Predicting Mathematical Reasoning Through Discovery and Execution](https://arxiv.org/abs/2610.05322)

**<font color=#1a73e8>作者：</font>** Adib Hasan, Lay Jain, Thanic Nur Samin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time compute can improve mathematical reasoning, but can short-budget runs predict how mathematical reasoning scales with additional compute? We introduce a Discovery--Execution (DE) framework that predicts the aggregate held-out scaling curves through a convolution of strategy discovery and conditional execution. From independent short-budget attempts and oracle-sketch-conditioned runs, the framework estimates cumulative success along held-out reasoning trajectories under alternate compute allocations. We evaluate four models on 35 fresh Olympiad problems and non-geometry problems from IMO-ProofBench Advanced. Under the DE framework, near-saturated execution predicts geometric scaling, as observed for the GPT models. For Claude Opus 4.8, incorporating measured execution substantially improves held-out forecasts over geometric extrapolation across one- and two-arm allocations. As a secondary application, regularized DE (R-DE) decisions to continue or restart yield lower average regret than the best model-specific retrospective policy. Together, these results show that measuring conditional execution provides information about longer reasoning that short-budget success rates do not always capture.

---


### 260. [Understanding the Weight Averaging Mechanism in LLM Training for Post-Training Quantization](https://arxiv.org/abs/2610.05329)

**<font color=#1a73e8>作者：</font>** Hanzhang Wang, Tianqi Shen, Zonglin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are typically pretrained in high precision but increasingly deployed with low-precision post-training quantization (PTQ). Recent studies have shown that using weight averaging during pretraining can improve PTQ performance compared with learning-rate decay, suggesting that it might provide a simple way to improve the pretraining-to-quantization transition. But the mechanism behind weight averaging remains insufficiently explained. This leads to inconsistent and fragile performance gains, thereby preventing practitioners from applying such a technique confidently. As a response, we formulate weight averaging as a trade-off between retaining training progress and improving robustness under perturbation. We further derive a continuous family of averaging kernels that unifies conventional strategies and achieves the Pareto frontier between the two competing goals. Critically, a theoretical framework for performing weight averaging under PTQ is developed. It can be shown that coarser quantization is more susceptible to perturbations, whereas finer quantization could be less affected. Thus, our results could provide unified theoretical guidance for performing weight averaging under different PTQ conditions. Experiments validate both the predicted behavior and the proposed averaging strategy. Code is available at this https URL.

---


### 261. [AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding](https://arxiv.org/abs/2610.05334)

**<font color=#1a73e8>作者：</font>** Mahdi Farahbakhsh, Ilan Sela, Fatemeh Doudi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frameworks that use large language models for scientific discovery typically rely on a fixed, human-designed algorithm that decides what the model sees at each step, leaving the model only the role of proposer. The model knows nothing of the search beyond what it is shown. As models grow more capable, a question arises: does a search strategy chosen by a human before the run scale better than promoting the model from proposer to planner and letting it own the search? The Bitter Lesson suggests that choosing the strategy in advance is the kind of hand-designed structure that general methods eventually outscale. We introduce AgentDiscover, in which a coding agent plans the search using its context as working memory, runs experiments, and records every attempt in a database of ideas, candidates, and their relations. This database serves as the agent's long-term memory and is structured so that the selection rules of classical algorithms such as MAP-Elites and Monte Carlo tree search each reduce to a single query, which the agent is free to use, combine, or replace. A server maintains the database and steers the agent after every submission, keeping it on course over long runs. In our experiments, AgentDiscover is more cost-efficient than existing frameworks, reaching better scores at lower cost. On tasks in kernel engineering, biology, algorithm design, and mathematics, AgentDiscover outperforms prior discovery frameworks. Its programs would have placed first among human competitors in seven past AtCoder heuristic contests, and on eleven mathematical and systems optimization tasks it matches or exceeds every baseline that uses the same model. Our code is available at this https URL.

---


### 262. [IRSTD-Agent: Agentic Infrared Small Target Detection via Zoom-Guided Interaction Learning](https://arxiv.org/abs/2610.05342)

**<font color=#1a73e8>作者：</font>** Jiawen Xi, Yu Zhang, Tianyi Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small-target detection plays an important role in maritime monitoring and aerial surveillance. Although multimodal large language models (MLLMs) offer promising capabilities for visual understanding, existing MLLM-based approaches struggle to precisely localize infrared small targets. In this paper, we propose IRSTD-Agent, an agentic framework for infrared small target detection through dynamic visual search. The framework enables an MLLM to adaptively determine where and at what scale to inspect an image and progressively gather fine-grained visual evidence for precise target localization. Five complementary visual tools (PROPOSAL, ZOOM, DETECT, DROP and REFINE) support object candidate discovery, adaptive observation, target localization, hypothesis rejection, and target extent refinement, together enabling a coordinated search process over original-resolution images. To teach the MLLMs to conduct this search, we introduce Zoom-guided Interaction Learning, which uses annotation-derived interaction trajectories to supervise tool selection and the corresponding arguments. Through extensive experiments on WideIRSTD-Full and IRSTD-1k datasets, we demonstrate that IRSTD-Agent outperforms the evaluated vision-language models and enhances the precise localization capabilities of MLLMs in IRSTD tasks.

---


### 263. [MemStrata: 95% and 90.91% Source-Aware Accuracy on LongMemEval-500 and LoCoMo-1540 with a Local Qwen 3.8 27B Q4_K_M Reader](https://arxiv.org/abs/2610.05343)

**<font color=#1a73e8>作者：</font>** Neeraj Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An adequate conversational answer may differ from a short or incomplete benchmark reference. To measure adequacy against the recorded history we prefer source-aware grading, in which the judge checks the reference against the full source before assessing system-blinded answers; original reference-only grading is reported alongside. With a local Qwen 3.8 27B Q4_K_M reader and a 24,000-token evidence ceiling, MemStrata CL1 scores 475/500 (95.0%) on LongMemEval-S and 1,400/1,540 (90.91%) on LoCoMo categories 1-4 under source-aware GPT-5.5 adjudication, against 463/500 (92.6%) and 1,205/1,540 (78.25%) under reference-only grading of the same answers. It preserves a retrieval backbone and adds nonduplicated, dated, speaker-attributed source spans. A same-reader full-history control with about 4.7 times the evidence scores 464/500 reference-only and 470/500 (94.0%) source-aware; neither difference is decisive. Keyword-only selection at the same budget scores 425, and a matched-reader Letta arm 438. On LongMemEval-M, where the packet holds about 1.6% of each history, MemStrata CL1 scores 427/500, with losses concentrated in multi-session and temporal questions. On 300 BEAM-1M questions it outscores dense retrieval, 0.738 to 0.706 (Wilcoxon p = 0.011). A same-seed replay of unchanged requests changed 1.5-2.3% of labels. On identical packets GLM 5.3 flash is non-inferior within 3 points (462 versus 463); Muse Spark 1.3 did not show non-inferiority on 269 questions. None of four pre-registered interventions met all of its registered advancement or feasibility criteria. Signed read-side artifacts support inspection but do not regenerate the private retrieval pipeline. The superiority of source-aware grading to human adjudication is not established, and development exposure, automated-judge dependence and the absence of held-out data preclude an independent-replication or leaderboard claim.

---


### 264. [Optimizing AI-Driven Messaging for Type 2 Diabetes Management: Insights from Patient Preference Elicitation](https://arxiv.org/abs/2610.05357)

**<font color=#1a73e8>作者：</font>** Angela Mastrianni, Defne Levine, Katerina Andreadis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) allows for improved user experience within conversational agents for diabetes management by supporting dynamic, context-aware conversations. In this study, we elicited patient preferences for the communication style of a GenAI-based conversational agent (uMatter) developed to support diabetes management. We conducted an online survey with 125 individuals with type 2 diabetes. The survey included a discrete choice experiment to evaluate participant preferences for different types of messaging attributes. The survey also elicited participant perceptions and feedback on the messages from uMatter. We found significant preference heterogeneity for the inclusion of emojis within the messages. Additionally, qualitative findings indicated that participants had different desired personas and communication styles for the conversational agent. We propose strategies from recent human-computer interaction and natural language processing research that can be used to design GenAI-based conversational agents that align with the communication preferences of patients.

---


### 265. [AutoDP-LLM: Automating Data Pre-processing for Intrusion Detection Systems using Large Language Models](https://arxiv.org/abs/2610.05369)

**<font color=#1a73e8>作者：</font>** Bao-Phong Nguyen, Gia-Khanh Pham, Thai-Duong Do 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing complexity and scale of modern cyber-attacks demand intelligent and computationally efficient Intrusion Detection Systems (IDS). However, designing effective data pre-processing pipelines traditionally involves substantial trial-and-error effort and repeated evaluation of alternative configurations. For large, high-dimensional network traffic data, this process can create a significant computational burden. In this work, we propose AutoDP-LLM, an automated pre-processing framework designed to reduce manual pipeline development and computational overhead. Specifically, AutoDP-LLM leverages Large Language Models (LLMs) to autonomously generate and validate executable data pre-processing pipelines. The framework combines deterministic host-side planning with LLM-based specialist agents to formulate data-processing strategies, synthesize executable code, and adaptively determine retained feature sets using semantic reasoning and training-derived statistical evidence, without requiring a predefined feature budget. Focusing on multiclass intrusion detection, we evaluate AutoDP-LLM on the UNSW-NB15 and NSL-KDD benchmark datasets using multiple downstream classifiers. Comparative experiments against conventional feature-selection methods show that AutoDP-LLM achieves competitive detection performance while automating the generation of compact and executable pre-processing pipelines. Component-level ablation experiments further demonstrate the complementary contributions of the semantic and statistical feature-reduction components. The repeated generation, validation, execution, and assessment of candidate pipelines are amenable to parallel execution, highlighting the potential of scalable computing environments, including high-performance computing (HPC) systems, to support automated IDS pipeline development.

---


### 266. [EnGRICH: Enhancing Generative Reward Modeling with Critiques from Humans](https://arxiv.org/abs/2610.05370)

**<font color=#1a73e8>作者：</font>** Xuancheng Li, Beining Wang, Haitao Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative reward models (GRMs) are important for LLM optimization. Unlike scalar reward models, GRMs generate natural-language critiques alongside preference judgments, providing finer-grained evaluation signals. Their effectiveness depends heavily on critique reliability. However, existing GRM training typically uses final preference correctness as outcome supervision. Because the preference outcome space is highly constrained, unreliable critiques can still yield correct outcomes and thus be reinforced. Recent work leverages human critiques for process supervision, but such critiques are scarce and are often reduced to scalar rewards, leaving their fine-grained evaluative information underutilized. We argue that evaluative criteria learned from human critiques can be generalized to broader outcome-only preference data. To this end, we propose \textbf{EnGRICH}, a GRM training framework that pairs the GRM with a training-time MetaCritic learned from a small set of human critiques. MetaCritic constructs response-specific rubrics and uses them to evaluate the evidence coverage and correctness of generated critiques. The resulting signals provide both process rewards for fine-grained credit assignment and structured guidance for exploring better critiques. During GRM training, MetaCritic is further optimized to generalize human-grounded evaluative criteria to outcome-only data. At inference, the trained GRM operates independently. Experiments across seven reward-model benchmarks show that EnGRICH consistently improves over competitive baselines, while further analyses validate the effectiveness of its core mechanisms.

---


### 267. [Towards Unbiased On-Policy Distillation for Block Diffusion Language Models](https://arxiv.org/abs/2610.05373)

**<font color=#1a73e8>作者：</font>** Zaiquan Yang, Fei Wei, Yong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has emerged as an effective post-training paradigm for language models, with recent efforts extending it to block diffusion language models (BDLMs). However, existing studies focus almost exclusively on small block sizes, leaving distillation into student models with larger blocks underexplored. In this work, we investigate this regime and reveal two critical optimization biases that induce severe training instability. First, mismatched block boundaries between teacher and student cause \textbf{\textit{context misalignment}}, providing distorted supervisory signals that misguide student decoding. Second, even under aligned contexts, an \textbf{\textit{intrinsic optimization bias}} in OPD, where the student tends to rapidly absorb high-support signals while lagging on low-support updates, drives a premature confidence surge that traps weaker students in catastrophic overconfidence collapse. To resolve these, we propose \mbox{\textbf{Un-OPD}}, an unbiased on-policy distillation framework with two novelties for stabilizing BDLM training. First, Un-OPD introduces a boundary-aware step filtering strategy that eliminates context-misaligned decoding steps. Second, Un-OPD proposes moderating optimization intensity at high-support positions via a support-rebalanced confidence calibration, thereby bypassing overconfidence collapse. Beyond stability, we also introduce a rollout reuse mechanism to reduce rollout generation overhead. Extensive experiments on math reasoning and code generation benchmarks show that Un-OPD consistently stabilizes training and delivers superior performance while reducing wall-clock training time by approximately half.

---


### 268. [Distributed Subliminal Learning: Replacing Model Updates with Random-Carrier Outputs](https://arxiv.org/abs/2610.05378)

**<font color=#1a73e8>作者：</font>** Dario Fenoglio, Gabriele Dominici, Martin Gjoreski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborative learning typically exchanges model parameters: federated clients communicate updates, while independently adapted foundation models are combined by exchanging adapters or checkpoints. This makes communication scale with model size and requires local specializations to be reconciled in weight space, where interference is common. We ask whether knowledge can instead be shared through model behavior on task-unrelated inputs. We introduce Distributed Subliminal Learning (DSL), a collaborative learning primitive in which participants adapt a common model locally, probe it with task-unrelated inputs, and transmit only the resulting carrier outputs. A coordinator pools these outputs and distills them into a shared model. The primitive supports one-shot foundation-model composition through carrier completions and iterative federated learning through carrier logits, without transmitting model updates or requiring task-related proxy data. In LLM composition, compared with LoRA averaging, DSL achieves higher preference retention (94.56% vs. 87.76%) and a larger GSM8K gain over the base model (22.0 vs. 0.6 points), while reducing upload by 30.6-49.0$\times$. In federated classification, DSL reaches 96.83% on MNIST with 8.9$\times$ less uplink than FedAvg and provides lower-communication operating points on CIFAR-10 and Tiny ImageNet. These results establish random-carrier outputs as a practical communication primitive for knowledge sharing across distinct collaborative learning paradigms.

---


### 269. [Harness-Search: Guiding Long-Horizon Search through Multi-Agent Coordination](https://arxiv.org/abs/2610.05382)

**<font color=#1a73e8>作者：</font>** Shanyong Wang, Zhenwen Ji, Lei Jin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon search requires agents to gather evidence across multiple steps and synthesize it into well-supported answers. The recent agent harnesses provide a natural and promising framework to support such long-running search processes. As interaction histories grow, one single agent in harnesses might get stuck and cause the policy to lose track of unresolved questions, overlook useful evidence, or terminate before sufficient support has been collected. One of promising way is to decouple three distinct responsibilities of proposing retrieval actions, updating persistent state, and deciding when to stop rather than concentrating them within a single policy. Targeted at it, we introduce Harness-Search, a multi-agent search harness to reduce the local errors propagating across subsequent exploration, evidence curation, and termination decisions. In particular, Harness-Search assigns these responsibilities to three permission-bounded authorities: a Retrieval Policy that proposes search operations, a Memory Operator that validates and commits persistent-state updates, and a Summary Auditor that accepts or rejects termination based on the sufficiency of the curated evidence. Together, these roles form a Propose-Commit-Audit loop in which actions are proposed, persistent evidence is selectively committed, and stopping decisions are subjected to an explicit sufficiency check. Across seven long-horizon search benchmarks, Harness-Search improves both retrieval and answer generation under the same policy backbone, increasing Recall by 4.60-27.92 points and Final-Answer Recall by 12.34-30.13 points over the strongest harness-based baseline on each evidence-retrieval benchmark. Moreover, trajectory-level analyses show that Harness-Search continues to accumulate useful evidence and expand evidence coverage with less redundant retrieval as the search history grows.

---


### 270. [Sibyl: An Efficient Small-large Model Collaboration Framework for Long-horizon Tasks](https://arxiv.org/abs/2610.05383)

**<font color=#1a73e8>作者：</font>** Zhewei Fang, Yuxin Zhang, Zhenwei Shao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) offer a promising foundation for on-device agents through low-latency, resource-efficient inference, yet limited reasoning and planning capabilities constrain their performance on long-horizon tasks requiring multi-step interaction with the environment. Step-level collaboration between SLMs and larger cloud-hosted models can bridge this gap, but identifying states that warrant cloud assistance remains challenging: the contribution of each cloud call is entangled with subsequent actions and can be assessed only from the final task outcome. Compounding this challenge, the SLM must balance two competing objectives: maximizing task success and minimizing cloud calls. To address this, we propose Sibyl, an algorithm that trains SLM agents to selectively consult cloud models at the step level and internalize their guidance for subsequent decisions, achieving strong task performance with minimal cloud reliance. Sibyl follows a three-stage training pipeline that (1) builds a robust base policy through consultation-free self-evolving reinforcement learning (RL); (2) cold-starts consultation behavior via decisive-disagreement state mining; and (3) jointly optimizes consultation decisions and guidance internalization through consultation-aware RL. Experiments on ALFWorld and WebShop demonstrate that Sibyl, using only a 0.6B-parameter model, outperforms state-of-the-art baselines, including agent training and routing methods, by 95.2% and 80.4% in success rate while averaging only 0.8 and 3.9 cloud calls per trajectory, respectively.

---


### 271. [GNN-CB: A Graph Neural Network Competition Benchmark for Human and LLM Evaluation](https://arxiv.org/abs/2610.05387)

**<font color=#1a73e8>作者：</font>** Murad Hossen, Tasneem Selim, Gurur Gamgam 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong performance on coding and reasoning benchmarks; however, their ability to solve graph-structured machine learning problems remains largely unexplored. In particular, no benchmark currently evaluates whether LLMs can autonomously solve end-to-end Graph Neural Network (GNN) coding tasks under realistic competition settings. To address this gap, this paper introduces GNN-CB, the first competition-based benchmark for evaluating both humans and LLMs on GNN coding tasks. GNN-CB consists of 18 curated competitions spanning node-, edge-, and graph-level prediction across diverse graph categories, domains, and difficulty tiers. All submissions are evaluated through a unified automated pipeline with hidden test sets and standardized scoring. Human participants solve tasks under controlled competition constraints, while LLMs are evaluated using a frozen zero-shot prompting protocol based on a plan-then-code paradigm with bounded execute-and-repair loops. The benchmark additionally supports both non-agent and autonomous agent-based evaluation within the same protocol. Under our evaluated protocol, LLMs rarely match Human Top performance and show less stable performance across competitions. No single model dominates: a few competitions are won by LLMs, yet humans still hold the top score on most tasks. We release GNN-CB as a living benchmark with automated evaluation infrastructure, dynamic leaderboards, and reproducible execution pipelines. Beyond benchmarking, GNN-CB provides a practice-oriented resource for studying GNN implementation across progressively diverse graph-learning tasks. The benchmark and evaluation framework are publicly available at this https URL.

---


### 272. [The Hidden States Cookbook: A Large-Scale Ablation Study for Noise-Robust Conversational Intent Classification in Industry](https://arxiv.org/abs/2610.05394)

**<font color=#1a73e8>作者：</font>** Bogdan Bogachov, Nikita Letov, Yaoyao Fiona Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational database interfaces face a critical challenge: users naturally embed queries in conversational noise (greetings, politeness, off-topic remarks), which degrades intent classification accuracy and wastes computational resources. Despite advances in orchestration and retrieval strategies, a fundamental question remains unanswered: which pooling strategy maximizes intent classification accuracy under realistic conversational noise in production language models? This work addresses this gap through 360 controlled experiments spanning four pooling configurations (mean, max, last-token, attention, and FFT-augmented variants) using Llama-3.2-1B-Instruct on BANKING77 and CLINC150 datasets under clean/noisy conditions with ten random seeds. Key findings reveal that attention pooling consistently outperforms alternative strategies under noisy conditions (~+2.6-2.8 F1 over the default), while mean pooling degrades performance by up to ~5 F1 points. Frequency-domain filtering does not produce consistent accuracy improvements and functions primarily as a structural variation rather than an accuracy-enhancing component. These results provide concrete, evidence-based guidance for building noise-robust conversational classifiers: attention pooling is recommended for noisy interfaces, mean pooling should be avoided, and last-token pooling is appropriate for clean-query scenarios.

---


### 273. [MMPostTrainBench: Benchmarking Autonomous Research for Multimodal Post-Training](https://arxiv.org/abs/2610.05398)

**<font color=#1a73e8>作者：</font>** Yuxin Liu, Yuxuan Wang, Zhenxin Lei 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous research seeks sustained model improvements through iterative experimentation and feedback. LLM agents show promise in automating machine learning and language-model post-training, but their ability to sustain multimodal improvement remains unclear. We introduce MMPostTrainBench, a benchmark spanning eight tasks in image, audio, video, and joint audio-video understanding and image-grounded software repair. Agents operate from a common base model within fixed budgets, using development feedback before independent evaluation of their submitted models. Evaluation covers target and non-target model outcomes, iterative model improvement and selection, and research integrity. Across all eight tasks, 52.1% of model--task means fall below the base, and evaluated submissions also exhibit non-target regressions. Model performance does not consistently improve across research iterations, and agents do not reliably select the best evaluated candidate for submission; final submissions trail that candidate by up to 5.38 percentage points. Extending autonomous research from text-only to multimodal tasks introduces additional sources of error in perception, cross-modal alignment, and temporal grounding. The observed regressions and selection gaps highlight the need to balance targeted improvements with non-target capability preservation and to retain gains across research iterations. These requirements motivate MMResearch, a multimodal research framework that connects media-grounded evidence to hypotheses and interventions, carries findings across rounds through hierarchical memory, and retains candidates using development evaluation. Added to existing code-agent runtimes, it improves submitted-model accuracy by up to 7.75 percentage points for Claude Opus 4.8 with Claude Code and 2.33 points for GPT-5.6-sol with Codex.

---


### 274. [CASE: Cost-Aware Stopping for Efficient Long-Video Agents](https://arxiv.org/abs/2610.05400)

**<font color=#1a73e8>作者：</font>** Yiming Du, Chenghao Liu, Zhiyuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-video agents can actively gather question-relevant evidence, but they typically leave a central decision implicit: when has the agent seen enough to answer? We propose CASE, a plug-in termination framework that frames this decision as policy-conditioned sequential stopping. At each causal checkpoint, CASE combines an auxiliary multiple-choice assessment of accumulated evidence with the host agent's execution state. From complete native trajectories, we construct a cost-aware target that compares answering now with stopping later along the same search path, accounting jointly for answer correctness and the full cost of continued reasoning. A lightweight Ridge regressor learns this decision gap and produces STOP/CONTINUE decisions. We evaluate three vision-language models with VideoSeek and AVP. On Video-MME, end-to-end accuracy changes by +0.67 percentage points on average while CASE reduces model-token use by 53.63%. The same frozen policies then transfer zero-shot to LongVideoBench and MLVU, with end-to-end accuracy changes of +3.38 and +4.58 points while saving 58.78% and 51.28% of model tokens, respectively. Across all agent-model-benchmark combinations, CASE attains the highest accuracy-efficiency Pareto-frontier coverage among the compared stopping methods (83.3%) at the selected operating points. Online execution preserves this favorable accuracy-efficiency trade-off and additionally reduces measured runtime by 54.1% on average. CASE provides a plug-in termination framework for long-video reasoning agents, enabling them to decide when further evidence acquisition is no longer worthwhile.

---


### 275. [Task Vector Descent: Learning from Non-IID Batches](https://arxiv.org/abs/2610.05402)

**<font color=#1a73e8>作者：</font>** Anton Baumann, Jonas Hübotter, Zeynep Akata 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central challenge in continual learning is to acquire new knowledge without forgetting what the model has already learned. This challenge appears in language model training when training data comes from various domain-, user-, or task-specific distributions that are encountered unevenly over time. In such settings, successive minibatches are temporally clustered by distribution instead of being sampled i.i.d. from the overall data mixture. Training on temporally clustered data induces a stability-plasticity tradeoff. Adapting the model to the active distribution can improve the model on the active distribution but may lead to a performance degradation on data it previously trained on. We find that this tradeoff intensifies with longer exposure to the same distribution. We therefore ask if the parameter displacement produced by such a sequence (the task vector) should be fully retained or applied partially. We compare applying the full displacement ($\lambda=1$) with partial integration, which scales the task vector by $\lambda$ before applying it to the continuing model and scales the optimizer state by the same coefficient. Across continual pretraining, pretraining from random initialization, supervised post-training, and reinforcement post-training, we find that intermediate values of $\lambda$ often improve average continuing-model performance relative to full integration, particularly after longer same-distribution sequences. In continual-pretraining experiments with both controlled streams and naturally defined adaptation sequences, task-vector scaling outperforms full integration at the matched learning rate, showing that its benefits are not reproduced by learning-rate scaling alone.

---


### 276. [A Strong Baseline for Evaluating Vision Encoders in Multimodal Large Language Models](https://arxiv.org/abs/2610.05413)

**<font color=#1a73e8>作者：</font>** Yilin Yang, Jun-Tao Tang, Kengyi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating vision encoders requires metrics that reliably predict their downstream performance in multimodal large language models (MLLMs). Although recent studies have shown that cross-modal metrics can better capture such performance, unimodal metrics remain the dominant choice in practice. In this work, we revisit cross-modal evaluation of vision encoders through large-scale experiments. We identify important limitations in both the experimental design and methodological formulation of prior approaches. After addressing these limitations and introducing simple improvements, we propose RAVEL, a training-free method based on cross-modal nearest-neighbor retrieval. Despite its simplicity, RAVEL achieves state-of-the-art performance across our experiments, outperforming prior methods by a substantial margin. Our results demonstrate that simple cross-modal metrics, when evaluated under a careful and comprehensive setup, can provide a strong basis for evaluating vision encoders for MLLMs.

---


### 277. [Render to Reason: Novel-View Semantic Prediction Improves Spatial Understanding in VLMs](https://arxiv.org/abs/2610.05417)

**<font color=#1a73e8>作者：</font>** Yuqun Wu, Yao Xiao, Chuhang Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent works augment Vision-Language Models with geometry features from pretrained 3D models, expecting that the geometric signal will boost spatial reasoning. However, we find that simply fusing geometry features and training on standard spatial QA yields only marginal improvements on high-level multi-hop tasks. We attribute this gap to a training-signal problem: standard spatial QA can be largely answered from visual features and language priors, so the geometry pathway receives weak gradients and fails to integrate with the visual features. To provide a training signal that requires geometry, we propose \textbf{novel-view semantic rendering} as an auxiliary training task that requires the model to predict the semantic layout of an unobserved viewpoint, inspired by humans' ability to mentally simulate novel viewpoints during spatial reasoning. This task encourages joint use of both pathways: geometry provides pose-dependent visibility, while vision provides semantic content. Our auxiliary task yields consistent improvements over the geometry-augmented baseline across all three benchmarks (up to +1.6 on VSI-Bench, +2.2 on ReVSI, +2.9 on our 3D-Point-QA dataset) and our full model surpasses prior open-source methods on VSI-Bench and on ReVSI. Project page: this https URL.

---


### 278. [Unmentioned Checklist Findings Change How Reinforcement Learning Appears to Improve Chest Radiograph Report Checking](https://arxiv.org/abs/2610.05425)

**<font color=#1a73e8>作者：</font>** Ali Vosoughi, Akhil Kasturi, Chenliang Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated checks of radiology reports may rely on AI-generated checklists that leave findings unmentioned. We used reinforcement learning to train a vision-language model to fill in a 12-finding checklist from a chest radiograph without seeing the sentence under test; a separate checking model judged the sentence from the checklist. On held-out patients, a rule-based check and an independent medical checker, neither used in training, measured discrimination gains (Youden index) of 12.6% and 11.8%; only the rule-based check met the prespecified false-alarm criterion. Switching to the training format, which fixes finding order and enters unmentioned findings as absent, raised the training checker's measured gain and lowered the independent checker's, a prespecified comparison that yielded 6.2% (95% interval 2.0% to 10.5%) and, post hoc on held-out patients, 7.7%. Across 8 checking models, acceptance of a label-consistent negative statement about an unmentioned finding ranged from 1.0% to 97.0%. Labels were report-derived, not radiologist-adjudicated.

---


### 279. [PharmAgent: Constraint-Aware Search with Frozen Language Models for Molecular Optimization](https://arxiv.org/abs/2610.05431)

**<font color=#1a73e8>作者：</font>** Nihui Shao, Guanxing Chen, Jilong Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Molecular optimization must improve target activity and satisfy developability constraints within limited evaluation budgets. Classical methods require tailored rules or training to incorporate chemical instructions and property feedback. Frozen language models can condition edits on this information, but need explicit constraint control and relevant experience. We therefore present PharmAgent, a constraint-aware molecular search method driven by adaptive external state. Its Lagrangian controller translates violations in accepted states into accumulated constraint pressure, keeping this history separate from current property measurements. Structure-indexed replay complements this feedback with relevant evaluated transitions that guide subsequent proposals. As a curriculum progressively activates constraints, candidates and the incumbent are compared under the same current objective, and the accepted state determines the next multiplier update. We derive an exact identity that characterizes how accepted-state violations accumulate in the controller's multipliers. Across five tasks with five independent runs, PharmAgent achieves a summed area under the target-score curves (AUC) of 3.9208 in target-only search, improving over MOLLEO by 37.3%. With online constraints, it achieves a property-adjusted AUC of 0.7076, improving over the strongest online baseline, ExLLM, by 53.8%. These results rank first among all evaluated methods in both target-only and constraint-aware search. The online comparison covers all five baseline frameworks. The full system leads every ablation variant in target quality, property-adjusted performance, and Pareto hypervolume. All five molecular cases reach feasible final states, documenting target gains and trade-offs.

---


### 280. [TeleTune: Evolving Agent Skills From Offline Telemetry](https://arxiv.org/abs/2610.05437)

**<font color=#1a73e8>作者：</font>** Justin Chih-Yao Chen, Elias Stengel-Eskin, Yan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents need to capture procedural knowledge of how people use software. User telemetry offers a scalable source of this knowledge. However, learning reusable skills from these logs requires addressing three challenges: (1) Goal Underspecification, since logs do not record the goal behind each action; (2) Non-Replayability, since past activity cannot be replayed to evaluate skill updates; and (3) Interleaved Trajectories, since logs may mix several tasks without marking their boundaries. To address these, we introduce TeleTune, a framework for learning a textual skill library from offline logs without recorded goals, cannot be replayed during optimization, and may interleave tasks. TeleTune uses action-prediction errors on logged trajectories to propose library edits and keep only those that improve held-out action-prediction accuracy, which we call skill-guided progress. The learned workflows also enable retrieval of demonstrations that cover the subgoals of a new task. At test time, the agent is provided with the learned library and the workflow-based retrieved demonstrations. Experiments on WorkArena and Online-Mind2Web show that TeleTune outperforms random retrieval, Agent Workflow Memory (AWM), and their combination. We find that the best baseline varies by setting, whereas TeleTune achieves average success rates of 77.1% and 80.6%, respectively, improving over the strongest baseline on each benchmark by 6.7% and 7.7%. Under the heaviest perturbation of the WorkArena training data,TeleTune keeps the highest average success rate at 68.5%, 6.3% above the strongest baseline. Our analyses show (1) skill optimization and workflow-based retrieval are complementary, (2) optimizing on fixed logs costs 5 to 75 times fewer tokens than validating the same edits with live episodes, (3) skill-guided progress tracks the live success rate.

---


### 281. [Groupwise Distortion Guarantees for Preference-Based Alignment](https://arxiv.org/abs/2610.05450)

**<font color=#1a73e8>作者：</font>** Jacob Brodkey, Roberto Tamez, Aaron Roth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference-based alignment methods such as reinforcement learning from human feedback (RLHF) and Nash learning from human feedback (NLHF) aggregate pairwise preferences to learn an LLM policy, but a natural goal is maximizing social welfare (average cardinal utility), which comparisons alone need not identify. Gölz, Haghtalab, and Yang (GHY) measure the gap by distortion: the worst-case ratio between the welfare of the best fixed lottery (distribution over responses) and of the learned lottery. They show NLHF is optimal when every user receives the same lottery. Account-based LLMs, however, have information about their users and can serve different lotteries to different people. We give an efficient algorithm, GLHF, that learns a single group-conditioned policy from one comparison per user. Under individual Bradley--Terry comparisons, GLHF asymptotically matches GHY's optimal population distortion bound simultaneously on every group in a prespecified, possibly overlapping collection, with sample complexity growing logarithmically in the number of groups and inversely with the smallest group mass. A sharper guarantee for groups with similar preferences approaches distortion of one when members share a feasible favorite response. In experiments using human coffee ratings and synthetic LLM-generated ratings, GLHF lowers distortion in every evaluated group and substantially reduces worst-group distortion relative to NLHF and other group-agnostic baselines.

---


### 282. [VERA: Verdict-Conditioned Reliability for Adaptive LLM Judges](https://arxiv.org/abs/2610.05452)

**<font color=#1a73e8>作者：</font>** Qiushui Xu, Syamil Mohd Razak, Tao Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately estimating judgment reliability is a central challenge in adapting LLM judges to newly verified feedback while preserving previously learned behavior. However, existing approaches often rely on output-level confidence, which can be overconfident and poorly aligned with judgment correctness. We propose VERA, a VErdict-conditioned Reliability Axis that estimates reliability from hidden activations by distinguishing correct from incorrect judgments within each predicted-verdict group. Using VERA as a control signal, we develop a VERA-guided periodic adaptation framework that integrates reliability-ranked corrective updates, reliability-residual replay, and periodic refresh of the reliability directions. After VERA-guided adaptation on Chatbot Arena, 8B- and 14B-parameter judges outperform the strongest baseline on each of four held-out public benchmarks, with relative gains of up to 23.01%. The framework also improves focal-class recall by up to 16.1% relative to the strongest adaptive baselines on a separate proprietary temporal auditing task.

---


### 283. [Measuring and Reducing Cross-Vendor Mismatch in Language Models](https://arxiv.org/abs/2610.05458)

**<font color=#1a73e8>作者：</font>** Erland Hilman Fuadi, Chong Tian, Xiaosong Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Running the same language model on different graphics processing unit (GPU) vendors can produce different logits, even when the model weights and inputs are the same. We analyze cross-vendor mismatch in two dense and two mixture-of-experts (MoE) models with five metric families, namely bitwise equality, logit differences, top-K consistency, token agreement, and task accuracy. We trace one source of the mismatch to accumulation order inside vendors' matrix instructions. Upcasting to FP32 reduces the dense model's logit error by 43% at three times the runtime, yet keeping only the MLPs in BF16 retains 94% of this gain at 1.3 times the runtime, so most of the cost of full upcasting buys little. In the MoE models, FP32 and FP16 both lower the probability error but raise the logit error and change expert selection, and FP16 fails in the dense model. An output-head low-rank adapter (LoRA) does not help either, since the final hidden state does not predict the mismatch. The mismatch also carries into training. With every seed fixed, a student distilled from a teacher running on AMD answers 431 MMLU questions differently from one distilled from the same teacher on NVIDIA. Under FP32 upcasting, bitwise equality barely changes while the output distributions move most of the way to the reference, so judging cross-vendor agreement by a single measure misreads both its cost and its gains. Code is available at this https URL.

---


### 284. [AI Safety via Debate is Compromised by Cognitive Biases](https://arxiv.org/abs/2610.05461)

**<font color=#1a73e8>作者：</font>** Gefei Liu, Sonya Rashkovan, Sophia Lloyd George 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) has played a central role in making large language models responsive to human instructions. However, human evaluators often favor flattering or persuasive responses over truthful ones, creating incentives for models to appeal to evaluators at the expense of accuracy. AI safety via debate has been proposed as a way to improve the supervision of language models: in this paradigm, two agents argue opposing positions and challenge each other's claims, potentially exposing falsehoods to the adjudicator. A central premise of AI safety via debate is that truthful arguments are easier to defend than false ones under adversarial scrutiny. In this work, we investigate whether this advantage persists when debaters use rhetorical strategies that exploit biases in human judgment. Inspired by competitive debate, we construct 68 LLM-generated dialogues about detective mysteries with known culprits, spanning four interventions: anchoring, fallacy oversight, pro-jargon, and verbosity. We apply each intervention to either the side advocating for the true culprit or the side advocating for an innocent suspect, allowing us to distinguish influence on adjudication from correctness. In a study with 369 participants, we find that, pooled across bias types, these interventions significantly shift judgments toward the manipulated side. These findings expose a vulnerability in debate-based supervision: human adjudication is sensitive to manipulative rhetorical strategies.

---


### 285. [Human-Like Attention? A Psychophysical Comparison of Visual Search in Humans and MLLMs](https://arxiv.org/abs/2610.05463)

**<font color=#1a73e8>作者：</font>** Renchi Zhang, Joost C. F. de Winter, Dimitra Dodou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual search is a fundamental cognitive ability. This study investigates whether Multimodal Large Language Models (MLLMs) exhibit human-like difficulty signatures in visual search tasks. We compared search performance of humans (n = 1,250) and MLLMs using identical 2D and 3D stimuli across different set sizes. Both groups showed efficient performance in feature searches, most clearly when the target had a unique color, but performance degradation in conjunction searches as set sizes increased. Additionally, we found strong correlations between human and MLLM error rates ($\rho = 0.82$), which suggests that MLLMs are sensitive to similar objective complexities, such as stimulus heterogeneity. However, differences were found as well: whereas humans invested extra search time to respond accurately on target-absent trials, MLLMs exhibited extreme present/absent response biases in complex searches. We conclude that MLLMs replicate high-level human performance signatures, yet their underlying computations differ significantly.

---


### 286. [Hallucination Across the Reasoning Lifecycle: Interface Visibility, Causal Evidence, and Release Control in Large Reasoning Models](https://arxiv.org/abs/2610.05472)

**<font color=#1a73e8>作者：</font>** Zhe Yu, Mohan Li, Lei Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning errors can propagate into later decisions and memory. This survey synthesizes 312 papers and first-party reports on text-based reasoning hallucinations around three questions: what evidence is observable, what study designs establish, and which corrective actions the evidence supports. UIPCA records unsupported premises (U), invalid inferences (I), dependent reuse (P), visible answer-trace consistency (C), and action-policy failures (A). Across 58 reviewed sources, no comparison establishes that a specified intervention improves reasoning while reducing factual reliability under matched conditions. The synthesis connects diagnosis to verification, repair, selective release, and persistent-state control across memory, tools, and training feedback.

---


### 287. [Hierarchical Reinforcement Learning with Stable Temporal Abstraction for Language Model Agents](https://arxiv.org/abs/2610.05473)

**<font color=#1a73e8>作者：</font>** Shayan Mohajer Hamidi, Yize Cheng, Yuanda Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hierarchical reinforcement learning improves long-horizon control by organizing primitive actions around persistent subgoals and assigning credit at multiple temporal scales. Recent hierarchical language agents bring these benefits to interactive tasks by explicitly separating subgoal planning from action execution. We observe, however, that an explicit hierarchy does not by itself determine how stable the resulting temporal abstraction is: the learned boundary policy may replace the subgoal almost every turn, making it effectively transient, or retain a subgoal after it has stopped being appropriate. We call this temporal abstraction instability. We propose Stable Temporal Abstraction via Constrained Optimization (STAC), a constrained boundary-policy optimization method that represents premature replanning and stale persistence as constraint costs. STAC applies the resulting Lagrangian costs only to the sampled boundary decision, leaving the underlying algorithm's rewards, critic targets, subgoal advantages, and primitive-action advantages unchanged. Across two backbones and two benchmarks, STAC improves success over a strong hierarchical baseline by $8.1$ and $7.9$ points on ALFWorld and WebShop with Qwen3-0.6B, and by $23.5$ and $15.8$ points with Llama-3.2-1B-Instruct.

---


### 288. [CodeForge-MA: Execution-Verified Multi-Agent Learning with Language-Conditioned LoRA for Multilingual Code Generation](https://arxiv.org/abs/2610.05481)

**<font color=#1a73e8>作者：</font>** Zhizhou Gu, Xianting Wu, Siyu Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models for code generation often fail on execution, multilingual coverage, and contamination control, especially under frozen backbone constraints. We present CodeForge-MA, a unified framework that improves code synthesis through a multi-agent data forge, execution verified reinforced instruction tuning, and a language conditioned mixture of LoRA adapters. Four specialized agents, Composer, Reviewer, Executor, and Curator, iteratively refine instruction code pairs, validate them with tests, and filter duplicates and benchmark leakage. During training, we combine masked supervised fine tuning with a test driven reinforcement objective to align generations with executable correctness. For the larger model, we use sparse expert routing over low rank adapters to improve cross language transfer while keeping the base model unchanged at inference. Experiments show that joint data, objective, and adapter design yields robust gains across programming languages.

---


### 289. [When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models](https://arxiv.org/abs/2610.05492)

**<font color=#1a73e8>作者：</font>** Zixuan Liu, Joris Köster, Zizhan Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models have shown strong potential as generalist robot policies, but adapting them to unseen tasks often requires costly parameter updates. Recent work such as RICL introduces in-context adaptability by retrieving expert demonstrations based on the current VLA observation and providing them as additional context at test time. The effectiveness of this adaptation therefore depends critically on the retrieval mechanism. In this work, we systematically study how different retrieval methods affect both retrieval quality and task performance within the RICL framework. Specifically, we compare four different methods: image-based retrieval, retrieval augmented with VLA's state, retrieval using features from the VLA backbone, and random retrieval. Our experiments yield three main findings. First, no retrieval method consistently dominates the others in task success, while surprisingly, random retrieval achieves a non-trivial success rate. Second, standard retrieval-quality diagnostics do not reliably reflect downstream VLA performance. Third, demonstrations from different but related tasks can provide useful transferable information. Together, these results provide an initial step toward understanding how retrieval mechanisms shape the in-context learning capability of VLA models and their downstream task performance, while highlighting the need for more careful design and evaluation of retrieval mechanisms for reliable test-time adaptation.

---


### 290. [The Functional Structure of Post-Compression Recovery in Low-Rank LLMs](https://arxiv.org/abs/2610.05504)

**<font color=#1a73e8>作者：</font>** Zishan Shao, Liang Tian, Georgiy Zemlevskiy 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Different low-rank compression methods can produce compressed LLMs that respond differently to the same post-compression recovery procedure, and relative advantages observed between methods at the compression endpoint may shrink, grow, or even reverse after recovery. We ask whether this recovery heterogeneity reflects functional structure beyond scalar loss evolution, and how that structure evolves throughout recovery. Our results establish that this heterogeneity reflects a reproducible compression-induced functional structure, which we formalize as recovery pressure. To characterize this structure consistently throughout recovery, we develop a standardized functional characterization within each backbone that is applicable across heterogeneous low-rank methods. The primary backward characterization reveals reproducible module-wise structure across independent probes, while a complementary forward-only characterization recovers related structure without loss or backpropagation. We further find that recovery pressure measured at the endpoint is associated with subsequent recovery response; during recovery, its module-wise structure is reorganized non-uniformly, and localized updates induce distributed responses beyond directly updated modules. Further evidence indicates that tracking this evolving structure provides a complementary functional view of recovery progress alongside scalar loss.

---


### 291. [Have I Scene This Before? Spatially Grounded Conversational Memory for Complex Queries in Egocentric Assistants](https://arxiv.org/abs/2610.05526)

**<font color=#1a73e8>作者：</font>** Jiazhou Liang, Liam Gallagher, Kiko Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Egocentric assistants must connect what users say with what they see across long interaction histories. We formalize this challenge as Spatially grounded Conversational Reasoning (SpaCR): cross-scene, recall-oriented, and counterfactual spatial queries that combine user-stated facts with geometric evidence. Direct vision-language models incur high inference costs and context limits as histories grow, while keyframe selection and retrieval can omit objects or evidence needed for complete recall. We propose Spatially grounded Conversational Memory (SpaC-MEM), an object-centric working memory that uses 3D reconstruction and segmentation to ground conversational information in persistent physical objects. It compresses multimodal histories while preserving spatial evidence and allowing object-specific facts to be updated through dialogue. We also introduce Ego-SpaCR, a benchmark comprising 620 ScanNet video sessions augmented with 95 task-oriented conversations and 3,100 evaluation queries. SpaC-MEM achieves the highest overall answer accuracy among the evaluated methods and improves object recall while requiring substantially fewer reference input tokens than native-video baselines. Removing 3D spatial information substantially degrades performance, highlighting the importance of preserving spatial and conversational evidence together.

---


### 292. [Dataset Signatures in Human-LLM Interactions and User Modeling](https://arxiv.org/abs/2610.05534)

**<font color=#1a73e8>作者：</font>** Joseph Suh, Serina Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human--LLM interaction datasets shape our understanding of AI use and provide a foundation for downstream research, including training and evaluation of user models. In recent years, a growing number of datasets have sought to capture a representative picture of human--LLM interactions. But how different are the pictures these datasets provide, and what do those differences mean for research built on them? We study these questions across seven conversation datasets, spanning in-the-wild chat logs and human preference data. We begin by revisiting the dataset classification experiment of Torralba & Efros and find that neural network classifiers identify the source of a conversation from user messages alone well above chance, indicating distinctive dataset signatures. This separability persists after matching datasets on the dimensions of human-designed taxonomies, implying subtle differences that these taxonomies do not capture. We then examine the implications for user modeling: how dataset signatures propagate to the outputs of user models trained on these datasets; how dataset choice influences evaluations of user model quality and subsequent evaluations of LLM assistants paired with these user models; and how dataset classifiers can guide data selection for training user models. While each dataset is meant to capture a slice of 'real-world' interactions, our findings reveal the extent to which these slices diverge, and the consequences of those differences for research built on these foundations.

---


### 293. [Don't Judge an LLM Only by Its Activations: Discovering Suppressed Safety Features via Counterfactual Activation Potential](https://arxiv.org/abs/2610.05541)

**<font color=#1a73e8>作者：</font>** Swadesh Swain, Sanghamitra Dutta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability has emerged as the primary means to understand safety behavior of LLMs. However, existing tools primarily focus on the activating neurons or features of a model. The role of the remaining large set of inactive components is invisible to such methods. This work demonstrates that the inactive set contains safety-critical features that are causally relevant for refusal of harmful prompts. Suppressing such features could turn refusals into compliance, while passing undetected by prevalent interpretability tools. We introduce the Counterfactual Activation Potential (CAP), a metric that quantifies a suppressed feature's latent activation tendency as the product of its encoder alignment (how strongly the input drives it), suppression strength (how strongly active features inhibit it), and safety criticality (how much refusal depends on it). To find suppressed safety features at scale, we propose CAP-guided Safety Feature Discovery (CSFD), a two-stage filtering algorithm that identifies candidate safety features from hundreds of thousands of transcoder features without exhaustive ablation. A significant fraction of trials turn compliant with harmful prompts when a candidate feature is ablated. Under natural jailbreaks, the suppression acting on the highest-CAP features rises 2-4x, and their activation correspondingly falls by up to 80%. Amplifying a feature's suppressors pushes its activation down and raises harmful compliance with prompts related to the suppressed feature, with no such effect for random features. Our experiments span five Gemma, Qwen, and Llama models across various parameter sizes. Our findings indicate that jailbreaks could operate in part by suppressing safety-critical features rather than solely activating harmful ones, and that suppressed features are a necessary complement to activation-focused interpretability of safety behavior.

---


### 294. [An equality condition for the Dobrushin bound on attention rollout and how often it holds in trained transformers](https://arxiv.org/abs/2610.05558)

**<font color=#1a73e8>作者：</font>** Przemysław Rola  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Dobrushin coefficient of each attention-rollout factor satisfies $\kappa(\frac12(I+A))\le\frac12(1+\kappa(A))$, and multiplying these inequalities over layers bounds the coefficient of the whole rollout. We characterise exactly when the layerwise bound is tight: equality holds if and only if some token pair attaining $\kappa(A)$ is mutually self-dominant - each of the two attends to itself at least as strongly as the other attends to it. The condition is far from automatic: uniformly random stochastic matrices satisfy it only 24-30% of the time.
When tested on the head-averaged attention of each individual input and restricted to content tokens - image patches, words or tabular features, excluding cls, register and separator tokens - the condition holds for essentially every input at every layer of DINOv2 (three model sizes), RoBERTa and DistilBERT. In the supervised models DeiT-B and ViT-B/16 it holds for 91% and 64% of input-layer pairs respectively, with all failures occurring late in depth. In FT-Transformer trained on two standard tabular benchmarks it holds for only 11-44% of input-layer pairs. The special tokens account for almost all failures in DINOv2 and the language models: when they are included, the condition holds for only 82-97% of input-layer pairs.

---


### 295. [Cut Binary Cross Entropy: Efficient Large-Vocabulary Loss and Gradient Kernels for Sequential Recommendation](https://arxiv.org/abs/2610.05559)

**<font color=#1a73e8>作者：</font>** Yaoyiran Li, Haowen Ning, Mohamed Hammad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial sequential recommender systems operate over massive item catalogs (e.g., 10^5--10^7 items). Multi-label recommendation models are trained with Binary Cross-Entropy (BCE) loss over the full vocabulary, but standard BCE materializes a dense [B, N, V] logits tensor in High Bandwidth Memory (HBM), incurring prohibitive $O(BNV)$ memory and fatal Out-Of-Memory (OOM) errors. While chunked loss optimizations exist for Softmax Cross-Entropy in LLMs, large-scale multi-label BCE optimization remains unexplored across deep learning ecosystems.
We propose CutBCE, an exact, hardware-accelerated BCE loss and gradient operator implemented in JAX and Pallas for large-vocabulary workloads. CutBCE introduces (1) an exact fused reformulation evaluating dense background loss and sparse target corrections; (2) a custom Vector-Jacobian Product (VJP) with a dedicated Pallas TPU backward kernel computing logit tiles on-chip in both passes so logits and their gradients never reside in HBM; (3) dynamic VMEM budgeting and sharding-aware collective hoisting for distributed meshes; and (4) count-based zero-overhead training metrics. On single-chip TPU v5e/v6e mini-benchmarks, CutBCE eliminates OOM errors with up to 91.9% speedup. On 8-chip TPU slice training for multi-label SASRec with 876k items (Yambda-50M), CutBCE reduces peak HBM by 65.7% (>14 GiB saved per chip) and increases training speed by 225.9% with comparable accuracy. CutBCE is open-sourced at this https URL.

---


### 296. [Lend Me Your Eyes: Instruction-Aware Text Embeddings via Attention Relay](https://arxiv.org/abs/2610.05564)

**<font color=#1a73e8>作者：</font>** Yiyuan Luo, Vaggos Chatziafratis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text embedding models trained with contrastive learning learn to follow task instructions from instruction-paired data, while instruction-tuned LLMs already know how to follow them. We show that this instruction-following ability can carry over from an LLM to a Transformer-based embedder without any training. We propose Attention Relay, which passes the attention weights an LLM produces to the embedder's own attention. Across six instruction-tuned LLMs from the Qwen3, Llama 3.1 and OLMo 3 families and ten widely used embedding models that differ in tokenizer, size and pooling type, Attention Relay makes nearly every combination instruction-aware. Experiments that break the method down into its parts show that the LLM's attention weights track the instruction in its later layers and come largely from instruction tuning. They also show that relaying these weights selects which content in the text matters: it makes the aspect of the text that the instruction asks about dominant in the embedding, or restores that aspect where averaging had diluted it.

---


### 297. [Disentangling Task Difficulty from Run-Level Failure in Agent Failure Prediction](https://arxiv.org/abs/2610.05572)

**<font color=#1a73e8>作者：</font>** Mohsen EsfandyariDoulabi, Lawrence Arkoh, Biruk Tadesse 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting whether an LLM agent will fail has emerged as a promising direction for supporting intervention during execution. Recent approaches report strong predictive performance, often with AUROC values between 0.85 and 0.94. However, predictors are typically trained by pooling runs from many tasks. We hypothesize that part of this performance comes from recognizing that some tasks are harder than others, rather than detecting whether a particular run is heading toward failure. This distinction matters because task-level difficulty supports decisions about where to allocate computation, while run-level prediction is needed to decide whether to intervene in an ongoing trajectory. We study benchmarks with repeated attempts of the same task by the same agent and separate cross-unit comparisons from comparisons between successful and failed runs of the same model-task unit. Across the evaluated corpora, more than 99.93% of the positive-negative pairs underlying pooled AUROC are cross-unit. Accordingly, predictors that never observe the current run can achieve high pooled performance, including a difficulty oracle with AUROC up to 0.945, while remaining at chance within task. Early run-level discrimination is consistently weak across trajectory predictors, released monitors, and hidden-state probes, although it improves later in execution and is stronger for weaker agents. Under fixed token budgets, task-level allocation outperforms abort-only strategies, while early stopping becomes beneficial only when within-task AUROC reaches about 0.84-0.93, far above the 0.50-0.55 range observed for early monitors. These results show that failure prediction should be evaluated not only by outcome accuracy, but by whether the captured signal supports the intended deployment decision.

---


### 298. [Expanding LLM Reasoning](https://arxiv.org/abs/2610.05584)

**<font color=#1a73e8>作者：</font>** Rian Atri, Evan Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extra inference compute is usually spent on sampling more reasoning chains. We study where inside an existing chain an additional continuation should begin. We define expansion utility, the change in correctness from restarting a chain at a stored step, and measure it at every eligible step for nine models on six benchmarks (41 model and benchmark cells). Restart position matters: steps selected on one set of continuations beat uniform placement when scored on disjoint ones, in held-out audits on 5, 16, and 38 cells (+4.25 points [+2.51, +6.63] in a fresh five-cell audit). A fixed rule that restarts from the last eligible steps, always-last, is a strong baseline: our learned router beats uniform placement but shows no detected gain over it, and on DeepSeek-R1-Distill-Qwen-14B/MATH-500 always-last exceeds the exact self-consistency frontier at matched aggregate generated output by +0.052 [+0.008, +0.098], using 0.774x the aggregate generated output of four-sample self-consistency. Cross-fitted oracle selection still finds held-out headroom beyond declared positional classes, a target for future selectors. Finally, breaking step-label ties by earliest index flips the sign of a pointwise selector's gain over uniform placement in every seed of a five-seed diagnostic with four rollouts per step; randomized ties remove the bias.

---


### 299. [AgentDoxx: Agentic Re-identification of Anonymized Text with Web Search](https://arxiv.org/abs/2610.05586)

**<font color=#1a73e8>作者：</font>** Jianing Wen, Tianshi Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) gain tool use capabilities such as web search, they can retrieve and cross-reference public information, creating privacy risks beyond memorization. One manifestation is re-identification: linking an anonymized interview transcript to a named individual. Yet without ground-truth identities, the coverage of such attacks and the protection offered by a defense cannot be reliably measured. We introduce AgentDOXX, an evaluation suite of 822 synthetic interview transcripts grounded in public information about real individuals with known identities. We evaluate fifteen configurations of open-weight and proprietary models, isolating the effect of web search, and analyze their search trajectories to distinguish retrieval-driven from parametric identifications. Ground-truth identities reveal that re-identification risk is distributed across an agent's execution: retrieval and parametric recall both contribute, with open-weight models identifying 15-28% of transcripts without search; identification succeeds in over 88% of cases once the target appears in a retrieved result; entity masking leaves at least one attacker successful on 85.3% of a stratified sample; and privacy instructions suppress naming but not retrieval, with configurations scoring 0% accuracy yet retrieving the subject in up to 62% of transcripts. We further show that observed attack trajectories can provide supervision for localizing identifying spans, offering a path toward attack-informed anonymization.

---


### 300. [ColdDDI: Evaluating Knowledge Utilization in Cold-Start Drug-Drug Interaction Prediction](https://arxiv.org/abs/2610.05590)

**<font color=#1a73e8>作者：</font>** Jiheng Liang, Chen Zhao, Di Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cold-start drug-drug interaction (DDI) prediction tests whether models can identify clinically significant interactions for drugs without training-time interaction history. Existing benchmarks mostly report aggregate edge-prediction scores, leaving a key evaluation question unanswered: when models receive molecular, textual, or knowledge-graph (KG) evidence, do they actually use the evidence that pharmacologically supports the interaction? We introduce ColdDDI, a reconstructible diagnostic benchmark built from DrugBank 5.1.13, with 1,900 approved small-molecule drugs and 565,731 positive DDI pairs. ColdDDI evaluates pairs with zero, one, or two unseen drugs. It also annotates each interaction by whether it changes drug exposure or drug effect, and by whether the biomedical knowledge graph contains shared enzymes, transporters, or targets that can plausibly mediate the interaction. These annotations separate evidence availability from predictive dependence. We evaluate eight conventional DDI methods and 13 LLMs; for open-weight LLMs, we test five prompt patterns and use masking, drug replacement, and channel-sensitivity metrics to probe knowledge utilization. ColdDDI exposes that, in the hardest split where both drugs are unseen, the main performance divide is mediator availability. A fine-tuned 1B LLM recovers 89-93% of interactions with a shared enzyme, transporter, or target, but only 40-62% without such a mediator. More importantly, KG-provided evidence is not always used; several KG-augmented baselines change little when the shared mediator is masked or disrupted, whereas fine-tuned LLMs respond strongly to this intervention. Thus, ColdDDI evaluates knowledge utilization rather than knowledge access alone, showing where cold-start DDI models rely on mechanistic evidence and where they fail despite receiving it. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
