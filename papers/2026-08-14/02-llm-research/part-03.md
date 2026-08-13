# 🧠 大模型相关研究 | 2026年08月14日

> 本类共 **164** 篇论文：已确认 **147** 篇，待复核 **17** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-164](./part-04.md)

---

### 101. [Located but Not Releasable: Silent Gate Inversion and Bounded Linear Release](https://arxiv.org/abs/2608.11822)

**<font color=#1a73e8>作者：</font>** Xining Xun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A growing body of work reports that language models represent task-relevant latent structure that they fail to use. Whether such structure, once located, can be converted into behavior is a separate question that is rarely tested end to end. We submit the complete pipeline -- detect, localize, and release -- to a fully preregistered stress test on a 25.7M transformer trained on causal-evidence discrimination, where a known suppression phenomenon (latent causal structure present but behaviorally unused) has previously been documented. Every threshold, claim template, and decision-tree branch was hashed and archived before any corresponding data existed. Three findings. (i) Localization succeeds: interventions at observation-evidence channels of mid layers restore target behavior on otherwise-suppressed worlds (paired release advantages $0.563$ and $0.854$, 97.5% CIs excluding zero; best-site release rate $0.889$). (ii) Gating fails out of distribution: a detector calibrated to trigger on zero out-of-distribution calibration worlds triggers on 6.9-7.3% of held-out in-distribution generations and on zero of the 2,400 held-out generations that actually need it -- a complete inversion that silently reduces the gated pipeline to its base model. (iii) Linear release is capped: removing the gate and injecting a per-instance linear direction unconditionally yields a monotone dose-response that plateaus far below the preregistered release margin (intercept $0.382 \to 0.311 \to 0.264$ vs. threshold $\le 0.08$); per-instance adaptivity adds less than $\pm 0.03$. The failure is doubly located: the detector is OOD-inverted, and the entire family of linear release directions at this site and resolution is bounded away from sufficiency. The two failures are dissociable, and neither overturns localization. Every number traces to a hashed artifact in the released audit chain.

---


### 102. [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](https://arxiv.org/abs/2608.11829)

**<font color=#1a73e8>作者：</font>** Xinmu Ge, Zizhuo Zhang, Yu Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has emerged as a promising post-training technique for enhancing LLM reasoning. It is commonly believed to enable the student model to distill knowledge from a stronger teacher model, thereby expanding capabilities beyond the pre-OPD base model. In this study, we examine this view through the lens of test-time scaling by varying the sampling budget K and evaluating performance with pass@K and avg@K. Specifically, across several OPD variants, we observe that OPD-trained models maintain superior avg@K performance across sampling budgets, while the advantage in pass@K gradually shifts to the pre-OPD base models as K increases. These results suggest that OPD primarily improves sampling efficiency rather than consistently expanding the student's reasoning capability boundary. The pass@K dynamics throughout OPD training further reveal a progressive shift toward stronger small-K performance at the expense of the large-K capability boundary. Furthermore, a problem-level solvability analysis using pass@1024 as the criterion reveals an asymmetry: OPD causes more previously solvable problems to become unsolvable than previously unsolvable problems to become solvable. Together, these findings suggest that, from the perspective of capability expansion, OPD behaves more like an "illusory distillation": its apparent gains arise primarily from improved sampling efficiency rather than from acquiring genuinely new reasoning capabilities from the teacher.

---


### 103. [GeoBridge: Decoupled Semantic Conditioning for Generative Image Geolocalization](https://arxiv.org/abs/2608.11838)

**<font color=#1a73e8>作者：</font>** Zhiyang Dou, Xumeng Han, Fengde Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have advanced image geolocalization mainly by improving how they reason about geographic cues. How that reasoning isdecoded into coordinates, however, has lagged behind. Predicting a place name for a geocoding API is discrete and lossy: it ignores image evidence and collapses multi-granular semantics into a coarse lookup. We argue that the bottleneck has shifted from what a model reasons to how that reasoning is represented for a continuous, geometry-aware decoder. We present GeoBridge, a role-decoupled conditioning mechanism that connects a frozen semantic MLLM to a frozen Riemannian flow-matching head that generates coordinates on the sphere. The central obstacle is arole conflict: supervising the condition with discrete semantic labels biases its representation toward class-discriminative geometry, at odds with the smooth manifold the generative head requires. GeoBridge keeps the semantic supervision decoupled from the condition interface: a separate projection forms the continuous condition the frozen head expects, injecting geographic priors without disturbing the spherical decoder. On IM2GPS3K, GeoBridge reaches 38.67/52.89/70.37 at the 25/200/750 km thresholds, improving over a place-name-to-API pipeline and reasoning-augmented direct prediction at these precision-relevant scales. GeoBridge is a decode-side algorithmic contribution, orthogonal and complementary to chain-of-thought reasoning. Code will be made publicly available.

---


### 104. [LookBack: Where and How to Score LVLM Responses via Visual Reference Usage](https://arxiv.org/abs/2608.11847)

**<font color=#1a73e8>作者：</font>** Beomsik Cho, Jinhyeong Kim, Dongseok Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) integrate visual perception with language generation, enabling responses that span image understanding and complex reasoning. However, LVLMs do not just inherit the text-level hallucinations; they also hallucinate against the image, producing fluent responses ungrounded in what they see. This makes LVLM response scoring inherently harder, and our diagnostics show that existing confidence-based metrics adopted from LLMs are insufficient for LVLMs. Specifically, removing the input image barely changes confidence-based selection, suggesting that output-space confidence primarily captures textual plausibility rather than agreement with the image. To address this gap, we propose LookBack, a training-free LVLM response scoring method that augments token likelihood with visual lookback score, a lightweight measure of how strongly each response token refers to image tokens. Across four benchmarks and three models, LookBack consistently improves Best-of-$N$ selection over existing baselines with negligible additional overhead.

---


### 105. [ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignment of LLM-based Agents](https://arxiv.org/abs/2608.11878)

**<font color=#1a73e8>作者：</font>** Yutao Mou, Pengfei Yang, Zhe Yin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents integrated with external tools are vulnerable to indirect prompt injections embedded in environmental states. However, existing studies largely rely on manually implemented or reused environments, stochastic LLM-based tool simulation, and predefined injection locations, limiting scalable security research across broader domains. To bridge this gap, we propose **ToolHazard**, a scalable adversarial environment synthesis framework that reduces human engineering and supports expansion with additional seed domains and compute. Through an Environment Simulator, an Attacker Agent, and a User Simulator, ToolHazard synthesizes executable stateful environments, discovers viable injection points and generates environment-specific payloads, and constructs state-grounded long-horizon tasks. Based on ToolHazard, we build **ToolHazard-Bench** for stress-testing agents under complex workflows and diverse environmental attacks. Experiments reveal substantial agent vulnerabilities and show that injection timing and placement affect attack effectiveness. Moreover, ToolHazard-generated alignment data improves security on both ToolHazard-Bench and AgentDojo while preserving benign task utility.

---


### 106. [Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents](https://arxiv.org/abs/2608.11888)

**<font color=#1a73e8>作者：</font>** Gen Dong, Yanjie Gao, Liqun Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are the de facto mechanism for extending LLM agents with reusable guidance. A skill can shape the agent's task execution, including planning, tool use, problem-solving, and validation. Prior work reported mixed results of agent skills: some skills improve task success rates, while others have no effect, increase token use and execution time, and even reduce success rates. This paper presents a comprehensive analysis of skill-induced agent failures by attributing task failures and cost regressions to specific loaded skills. We introduce a differential analysis framework that attributes a failure or regression to a skill by comparing a target skill-guided run against a no-skill or semantically matched skill reference run that solves the same task, or solves it more cheaply. We instantiate this framework on SkillsBench and SWE-Skills-Bench, yielding 307 skill-induced failures, including 125 functional failures and 182 efficiency regressions. We also build SkillTriage, a taxonomy-guided attribution tool that normalizes paired cases, extracts differential evidence, and produces triage reports. Our major findings include: (1) Skill induced functional failures are rarely caused by obviously irrelevant skills; instead, seemingly relevant skills often make the agent incorrectly implement or omit task-required implementation elements. (2) Skill-induced efficiency regressions are not explained by prompt length alone. (3) The largest sources within Excessive Procedure are excessive verification and heavy implementation pipelines, contributing 67 and 30 cases, respectively. This shows that skills often turn validation checklists and construction recipes into mandatory work. Based on our findings, we propose research topics and tooling improvements for safer and more cost-aware skill reuse.

---


### 107. [Policy-as-logic for robust reasoning over rules](https://arxiv.org/abs/2608.11905)

**<font color=#1a73e8>作者：</font>** Rahul Nair, Bastian Lipka, Elizabeth Daly  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In many practical applications of generative AI systems, from tax rules to airline baggage allowance, responses to natural language queries must respect written policies or rules. We present a hybrid symbolic approach that expresses policies in formal logic and at inference time exploits the representation power of language models for fact extraction to ground predicates, and an answer set solver for reasoning such that responses are interpretable, auditable, and as we show, accurate and robust under input perturbations. Specifically, we show this separation of extraction and reasoning steps outperforms policy-as-prompt and policy-as-code methods in most cases with ~10x reduction in token usage. The results point to the value of structured reasoning and symbolic solvers in conjunction with generative models to make robust decisions involving objective criteria.

---


### 108. [Do You See What You Draw? A Semantic Closed-Loop Framework for Holistic Evaluation of Unified Multimodal Models](https://arxiv.org/abs/2608.11907)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Jiaxin Qi, Zhijiang Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As Large Vision-Language Models increasingly aim to integrate visual generation and understanding within a single parameter space, evaluating such structural unification in a cohesive manner remains a critical challenge. Current evaluation protocols predominantly treat generative and discriminative capabilities as separate tasks, leaving a gap in system-level evaluation for unified multimodal models (UMMs). In this work, we propose Self-Generative-Understanding (SGU), a novel, annotation-free evaluation framework that probes the integrated capabilities of unified models through a semantic closed-loop challenge. Without requiring new annotations, SGU leverages the dual understanding-and-generation abilities of UMMs by asking them to first perceive an image and produce a textual description, subsequently reconstruct a visual context based on that description, and finally perform reasoning over the self-generated output. This pipeline provides a zero-cost testbed that yields an integrated performance score specifically tailored for evaluating UMMs as unified systems. Extensive experiments show that even high-performing UMMs often struggle to reason over their own generated contexts, revealing limitations that are not captured by separate evaluations of understanding or generation alone. Our work provides a complementary holistic evaluation framework and offers a foundation for benchmarking the development of next-generation unified multimodal models.

---


### 109. [LazyTrain: Limited-resource Allocation toward Zero-waste Yield Optimization in Large Language Model Training](https://arxiv.org/abs/2608.11919)

**<font color=#1a73e8>作者：</font>** Xiaojun Wu, Cehao Yang, Honghao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training large language models on limited hardware is increasingly a scheduling problem across GPU compute, host memory, PCIe transfer, and storage bandwidth. Existing offloading systems reduce GPU residency, and MegaTrain shows that a CPU-master layer-streaming executor can train large models on a single GPU, but fixed checkpointing and placement heuristics still leave communication exposed on the critical path. We propose LazyTrain, an optimization layer over a layer-streaming executor. LazyTrain formulates checkpoint selection, activation placement, recomputation, and CPU-GPU-NVMe communication overlap as a mixed-integer scheduling problem, then executes the solved policy during training. It further couples 8-bit optimizer states with fast gradient clipping as a single Hybrid 8-bit operator: state compression reduces optimizer-state memory, while fast clipping counteracts the additional CPU-side update overhead. Across H800 experiments from Qwen2.5-3B to Qwen3.6-27B, LazyTrain improves sustained TFLOPS over matched baselines runs by approximately 1.24$\times$; RTX 3090 experiments likewise increase the maximum feasible batch size by one at each model scale. In the primary Qwen3.6-27B H800 MetaMathQA run, LazyTrain reaches 219.95 TFLOPS and 1361 tokens/s at batch size 72, peaks at 68.84\,GB of GPU memory, and obtains 95.42\% exact-match accuracy on the full evaluation split. The source code is available at this https URL.

---


### 110. [LODESTAR: Trustworthy Entropy Is Navigated, Not Merely Measured -- Reinforced Polarizer Keeps a Frozen LLM from Being Confidently Misled by the Wrong Evidence](https://arxiv.org/abs/2608.11922)

**<font color=#1a73e8>作者：</font>** Po-Jen Ko, Che-Cheng Wu, Hung-Chun Hsu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Predictive-distribution entropy makes a strong selection rule in retrieval-augmented question answering: across five QA benchmarks, keeping the candidate answer that a frozen respondent LLM produces with the lowest answer-token entropy lifts mean answer $F_1$ from 0.4769 to 0.5148 over the retriever's top-ranked passage, with no gold answers. Yet this lowest-entropy rule, which prior entropy-based selectors adopt, fails in a specific and consequential way: a misleading passage makes the respondent confidently wrong, driving its entropy down precisely where the signal looks most trustworthy. We show that the failure comes from the passage the respondent reads -- and the context that passage is read in is an input we can intervene on. We introduce LODESTAR, to our knowledge the first method to score a text intervention by the uncertainty it induces in a third-party frozen respondent, compared across one question's candidates. LODESTAR uses reinforcement learning to train, once and offline, a polarizer -- a short fixed natural-language string inserted into the respondent's prompt and never into its weights; its training labels are built offline from gold answers and two LLM judges, and inference reads neither. Evaluating every competing selector under the same frozen respondent and the same candidate pools on 5,008 questions, LODESTAR attains the highest mean $F_1$ of any inference-ready selector (0.5148 to 0.5339), the highest exact match (0.4136), and the highest GPT-4o judge score of the frozen-respondent configurations judged (0.6435); its three-seed mean wins all 70 method-by-dataset $F_1$ cells against fourteen published configurations while remaining paired-significant against every one. The gain holds both in-domain and out-of-domain, and ablating the polarizer shows it is what makes the respondent read a misleading passage less often (26.0% against 30.3%).

---


### 111. [OEIS Open: How many conjectures can language models turn into theorems?](https://arxiv.org/abs/2608.11941)

**<font color=#1a73e8>作者：</font>** Tom Adamczewski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We construct OEIS Open, a benchmark based on 492 open mathematical conjectures from the OEIS, formalized in Lean by Tsoukalas et al. Whereas these conjectures had previously been attempted only with a bespoke agent, our open-source evaluation code runs any generic language model (LM) against them, and is secure against LM cheating attempts. We find that LMs equipped with a minimal set of tools resolve 147 of these conjectures with a budget of \$50 per attempt, scoring 30% on OEIS Open. OEIS Open Lite is a random subset of 100 conjectures for cheaper evaluation. When evaluated with a budget of \$200 per attempt, the best current LM scores 44% on OEIS Open Lite. Giving LMs access to the mathematics literature via 476,000 papers from arXiv did not increase performance on OEIS Open Lite, and nor did using more sophisticated agent loops. The conjectures covered in this work are of uncertain mathematical significance, and most have likely received little previous attention. Nevertheless, our results show that LMs can resolve open research conjectures autonomously and at modest cost.

---


### 112. [Accuracy and Order Sensitivity Diverge Under Label-Free Strategies](https://arxiv.org/abs/2608.11947)

**<font color=#1a73e8>作者：</font>** Karl Hanna, Chen Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple-choice benchmarks are widely used to evaluate large language models, but MCQ scores conflate knowledge with sensitivity to option order, which makes them unreliable measures of model knowledge. In this paper, we test whether preventing a model from seeing option labels while committing to an answer removes positional influence and, in turn, improves performance. We evaluate two different strategies for mitigating bias. The first uses a generation-then-matching approach, and the second scores options in isolation, which is positionally unbiased by construction. Neither reliably improves accuracy. A complete decomposition shows that the bottleneck is withholding options, not the matching step. The only configuration that consistently matches the baseline is the one that shows the model all options paired with an LLM matcher. However, eliminating positional influence entirely still does not reliably yield accuracy gains, while cyclic permutation often improves them. For two-stage prompting, an aggregate measure of recall imbalance and a direct per-question measure of order sensitivity both fail to show reliable debiasing.

---


### 113. [ExRole: From Team Trajectories to Executable Roles in Multi-Agent Language Models](https://arxiv.org/abs/2608.11949)

**<font color=#1a73e8>作者：</font>** Zhou Liu, Chaoyang Han, Zewei Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Roles provide an interpretable interface for organizing language-model agents, yet most multi-agent systems treat them as hand-written prompt labels disconnected from learned behavior and parameter updates. We argue that a useful role should instead be an executable control variable: it should summarize behavior predictive of future utility, guide subsequent interaction, and identify the trainable capacity responsible for that behavior. We introduce ExRole, a trajectory-to-role framework that learns future-aware role prototypes from prefix-local team traces, resolves them into readable instructions and token-aligned role markers, and optionally routes shared LoRA rank slots with turn-aligned credit. Across MuSiQue and 2WikiMultiHopQA, ExRole improves over single-agent search by 15.0/14.4 and 13.5/16.1 EM/F1 points, respectively. Against the strongest non-ExRole controls, the corresponding gains remain 11.5/11.6 and 7.7/9.7 points. Across both benchmarks, the controlled results consistently favor trajectory-induced role conditioning over role-free, manual, random, and shuffled alternatives. Role-Agent-Turn interventions further show that the induced roles capture transferable behavioral specialization beyond fixed agent identities or turn positions.

---


### 114. [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](https://arxiv.org/abs/2608.11967)

**<font color=#1a73e8>作者：</font>** Zhixin Zhang, Xinke Jiang, Zhibang Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly rely on long-horizon reasoning to solve complex tasks involving planning, tool use, and memory. A critical capability in such settings is reflection: assessing trajectory progress, identifying missing evidence and unreliable intermediate states, and deciding whether to continue, revise, or abandon the current branch. Learning effective reflection, however, is challenging because reflection is performed locally within the current branch, whereas its utility can only be determined by its contribution to the final trajectory outcome. This local-global mismatch makes outcome-based reinforcement learning provide only local, sparse and delayed supervision for reflective decisions. To solve these, we propose LoongReflect, a training framework that formulates reflection as a memory-control policy. The agent operates over a reversible trajectory tree using explicit reflect and backtrack actions. Reflection consolidates verified facts, missing evidence, and branch-specific risks into working memory, while backtracking removes an unreliable branch from the active context and preserves a concise corrective lesson. To learn this policy, LoongReflect combines two complementary signals through a look-ahead, extragradient-style coordination mechanism. A fast channel distills globally informed reflective behavior from a privileged teacher, with supervision restricted to reflection and backtracking tokens. A slow channel optimizes complete trajectories using outcome-based GRPO, aligning local control decisions with final task success. Experiments on multi-hop retrieval-augmented generation and mathematical reasoning benchmarks demonstrate consistent improvements over outcome-only reinforcement learning and self-distillation baselines.

---


### 115. [Retry, Switch, or Abstain? Learning Strategy-Aware Tool-Use Policies via Controlled Error Injection](https://arxiv.org/abs/2608.11977)

**<font color=#1a73e8>作者：</font>** Chaoran Chen, Vy Nguyen, Ziji Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents are commonly trained and evaluated in environments where tool calls succeed reliably, yet deployed tools can fail transiently, persistently, or silently. Robust recovery therefore requires more than repeated retries: an agent may need to retry the same path, switch to an alternative, or recognize that no viable path remains. We present BENCH2ROBUST, a framework that converts failure-free tool-use benchmarks into controlled stochastic environments with scenario-controlled solvability, where episodes explicitly require retrying, switching, or stopping after available paths are exhausted. We use BENCH2ROBUST to study two complementary interventions: structured runtime recovery context through Bayesian Tool Memory (BTM), and curriculum-controlled reinforcement learning. Across 7 models from 4 families and two multi-turn benchmark families, tool failures produce a near-universal robustness gap. On held-out Retail tasks, BTM improves robustness by up to 16.8 percentage points without retraining, while RL learns complementary recovery behavior that remains beneficial without inference-time BTM. Combining the two reaches 40.8-45.5% under injection while preserving failure-free performance. These results suggest that robust tool use benefits from combining environment-specific recovery knowledge with learned recovery behavior.

---


### 116. [Benchmarking Trustworthiness of SLMs: Pre-trained vs. Compressed](https://arxiv.org/abs/2608.11981)

**<font color=#1a73e8>作者：</font>** Haokun Lin, Kaijie Zhu, Haobo Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small Language Models (SLMs) have emerged as a more efficient alternative to traditional Large Language Models (LLMs), offering promising potential in resource-constrained scenarios. Existing approaches to building SLMs typically follow two paths: training compact models from scratch, or compressing larger pre-trained models using methods such as pruning, quantization, or distillation. As language models become increasingly integrated into real-world applications, ensuring their trustworthiness has become a critical concern. However, how to build trustworthy SLMs remains an underexplored question. In this work, we present a comprehensive evaluation of SLM trustworthiness across multiple dimensions, including fairness, robustness, privacy, and ethics. We first examine the effects of pruning and quantization, and find that quantization is significantly more effective in preserving trustworthiness compared to pruning. More importantly, we demonstrate that compressing a reliable large model via quantization can produce SLMs with superior trustworthiness and adaptability compared to using small models trained from scratch. Furthermore, knowledge distillation from trustworthy teacher models can further enhance the reliability of SLMs. We hope our findings provide practical guidance and a foundation for future research into the development and deployment of trustworthy small language models.

---


### 117. [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](https://arxiv.org/abs/2608.11994)

**<font color=#1a73e8>作者：</font>** Sen Xu, Wei Wang, Shixi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose claim-level falsification as a principle for test-time scaling and instantiate it through Claim-Level Reliability Assessment (CLR), a training-free framework that reallocates test-time compute from additional solution sampling to targeted verification. Since whole-trace evaluation often obscures decisive errors due to signal dilution from routine tokens, CLR condenses each reasoning trace into a compact set of decision-critical claims, thereby isolating its logical anchors. Furthermore, recognizing the inherent difficulty of generating entirely correct solutions under fixed model capabilities, CLR shifts the focus to semantic falsification. This approach exploits a fundamental asymmetry between solution construction and claim refutation. Constructing a valid solution requires a flawless reasoning path, whereas refuting an incorrect claim requires identifying only a single decisive flaw. This targeted search for negative evidence systematically compresses the survival space of high-confidence incorrect traces, effectively suppressing erroneous consensus via nonlinear reliability scoring. Across four LLMs and four reasoning benchmarks under matched budgets, CLR generally improves upon pass@1 and self-consistency. On GPT-OSS-20B/CMIMC25, for instance, CLR exceeds pass@1 by 27.15 percentage-points and raises self-consistency accuracy from 77.50\% to 82.19\% with 37.0\% fewer tokens.

---


### 118. [Asymptotic Risk Calibration for Selective Question Answering](https://arxiv.org/abs/2608.12008)

**<font color=#1a73e8>作者：</font>** Shufan Lin, Sijin Dong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) may generate fluent but incorrect answers, making uncertainty quantification important for reliable question answering. However, heuristic uncertainty scores cannot perfectly distinguish correct predictions from incorrect ones, and directly applying a fixed uncertainty threshold provides no statistical control over the error rate among accepted answers. To address this limitation, we propose A-CRC-QA, a post-hoc calibration framework for uncertainty-aware selective question answering. The proposed method reformulates selection-conditioned error control as a linear expectation constraint and applies a monotonized empirical-risk calibration procedure inspired by conformal risk control. Since the resulting instance-wise loss is generally non-monotone with respect to the acceptance threshold, our framework targets asymptotic rather than finite-sample risk control. A-CRC-QA is model-agnostic, requires no additional training, and can be combined with different uncertainty estimators. Experiments on CoQA and MedMCQA demonstrate its applicability to both open-ended and closed-ended question answering, achieving a favorable trade-off between accepted-answer reliability and answer retention compared with uncalibrated and confidence-bound-based baselines.

---


### 119. [Poly-Dialectal Neural Machine Translation System for Bangla Regional Dialects](https://arxiv.org/abs/2608.12018)

**<font color=#1a73e8>作者：</font>** Rakib Ullah, Ruhul Islam Rahul, Tanbir Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Regional dialectal variation poses a fundamental challenge to natural language processing (NLP) in Bangla, where over 240 million speakers communicate across diverse regional variants that diverge significantly from Standard Colloquial Bangla (SCB) in phonology, morphology, and lexicon. Contemporary neural machine trans- lation (NMT) architectures and large language models (LLMs) predominantly as- sume a homogeneous language distribution, resulting in severe performance degra- dation when translating low-resource regional dialects. In this work, we present a unified Poly-Dialectal Neural Machine Translation System capable of multi-directional translation across 12 Bangla regional dialects without routing through an inter- mediary standard pivot. We compile the largest multi-dialect parallel corpus for Bangla to date, comprising 51,531 non-null parallel sentence pairs across 12 di- alects, incorporating 2,500 expert-verified, bidirectional parallel sentence pairs for five previously unaddressed dialects. Evaluating sequence-to-sequence architec- tures under Weight-Decomposed Low-Rank Adaptation (DoRA), our fine-tuned BanglaT5 model achieves state-of-the-art translation performance (29.26 BLEU, 57.26 chrF++), outperforming NLLB-200 (615M) and mBART-50 (611M) while preserving morphological coherence. Furthermore, we conduct a systematic cross- dialectal transfer analysis and dataset scaling study, establishing empirical thresh- olds for low-resource dialect adaptation. Finally, we deploy the optimized INT8- quantized model as an open-access web application to promote digital inclusion for marginalized dialect communities. The complete dataset is publicly available at Mendeley Data (this https URL).

---


### 120. [SoftWater: Class-Aware Rate Allocation for Softmax Quantization](https://arxiv.org/abs/2608.12026)

**<font color=#1a73e8>作者：</font>** Joao V. Cavalcanti, Ashia C. Wilson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization pipelines routinely leave the softmax output layer in high precision. Yet in small LLMs with modern vocabularies, the head holds 15--30\% of all parameters, so a nominal ``2-bit'' model with an fp16 head can store several times as many bits per weight. We pose softmax-layer quantization as a rate-distortion problem under the KL divergence between the original and quantized output distributions. A second-order analysis reveals a class-aware geometry: quantization error is weighted jointly by feature covariance and class-specific softmax curvature. A separability approximation replaces the $Kn\times Kn$ Cholesky with one $n\times n$ factorization rescaled per class, making the lattice encodable by successive interference cancellation, with both statistics from a single forward pass. The resulting method, SoftWater, gives fine grids to frequent, low-variance classes and coarse grids to rare ones, a large gap under Zipfian token distributions. Across five models from 1B to 32B, SoftWater outperforms the released WaterSIC quantizer (near-optimal under linear-layer WMSE but not output KL) at matched head rates on 59 of 60 test points, using none of that pipeline's refinements and cutting head-induced KL by $6.5\times$--$8.3\times$ at 2 bits. On Llama-3.2-1B-Instruct with quantized bodies, a 2-bit head removes 45--60\% of stored bytes for a $2.9$--$3.7\%$ perplexity increase. Because the class-side statistic comes from calibration data, matching calibration to the deployment domain gives the lowest KL on that domain throughout. On a tied model, a 4-bit head is near-lossless and a 2-bit head costs under 4\% perplexity, making head quantization of such models practical.

---


### 121. [Mechanist: AI as a Scientific Instrument for Discovering the Mechanisms of Intelligence](https://arxiv.org/abs/2608.12036)

**<font color=#1a73e8>作者：</font>** Mengru Wang, Junfeng Fang, Shuofei Qiao 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI models have achieved remarkable success across diverse domains, yet the mechanisms underlying their capabilities and the risks they may pose remain poorly understood. As AI development becomes faster and increasingly automated, mechanistic exploration remains largely manual, widening the gap between what models can do and our ability to understand and control them. To bridge this gap, we introduce Mechanist, an agentic system that uses AI as a scientific instrument for the autonomous discovery of mechanisms underlying AI intelligence. To support autonomous mechanistic discovery, we construct an interpretability-focused knowledge graph of approximately 13,000 papers and integrate it with a multidisciplinary database of 43 million papers spanning 26 fields. We further curate a library of 32 foundational methods for mechanism analysis, causal intervention, and validation. Compared with Claude Code and existing AI-scientist systems, Mechanist generates more valuable mechanism hypotheses and executes experiments more reliably. Mechanist also demonstrates a progression from discovering model behaviors to explaining and controlling AI models. Specifically, Mechanist first uncovers a counterintuitive safety risk in scientific laboratories, showing that unsafe traits can transfer across modalities through apparently safe training data. Mechanist then develops a mechanism theory of belief, revealing how models represent world knowledge, form beliefs, infer the beliefs of others, and how these mechanisms emerge during pretraining. Finally, Mechanist translates these mechanistic insights into practical interventions that improve model performance across diverse scenarios and steer scientific foundation models toward generating DNA sequences with specified properties.

---


### 122. [Do Not Forget the Obvious - RISC: A Risk-Informed Slice-Coverage Protocol for Safe Autonomous Driving](https://arxiv.org/abs/2608.12051)

**<font color=#1a73e8>作者：</font>** Fabian Hüger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aggregate metrics may not fully reflect performance in insufficiently examined high-risk driving conditions. We propose RISC (Risk-Informed Slice Coverage), a practical protocol for risk-guided stress testing and coverage-qualified evaluation. Risk-guided stress testing directs a finite audit budget toward risk-relevant sub-datasets, called risk slices, while coverage-qualified evaluation reports results together with explicit statements about which slices are sufficiently or insufficiently covered. The protocol translates safety concerns into machine-readable risk slices, uses lightweight signals to tag candidate data, selects a compact audit set by risk, and qualifies the results using coverage evidence. An LLM can optionally support this process by surfacing relevant but potentially overlooked conditions during test planning, thereby helping engineers not to forget the obvious. RISC is model-agnostic and can be applied to perception modules, driving models, and other autonomous-driving subsystems. We instantiate the protocol for monocular pedestrian perception using 1,000 frames from the Zenseact Open Dataset, image statistics, and a YOLO-based detector proxy. In this proof-of-concept study, risk-guided selection increases critical failure discovery from 34.0% under random sampling to 98.5%. RISC provides a lightweight, assurance-oriented evaluation layer that complements scenario categorization, coverage assessment, and broader testing-and-verification workflows.

---


### 123. [Look What the Probes Dragged In! Real-World Chest X-ray Shortcuts in MedCLIP](https://arxiv.org/abs/2608.12086)

**<font color=#1a73e8>作者：</font>** Nikolette Pedersen, Regitze Sydendal, Veronika Cheplygina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models, such as contrastive language-image pre-training (CLIP)-based approaches, have reached state-of-the-art (SOTA) results in medical artificial intelligence. However, recent work reveals that CLIP-based models remain vulnerable to shortcuts. We investigate how real-world shortcuts manifest across different layers of the medical CLIP-based model, MedCLIP, and its vision encoder, a frozen ResNet-50. We attach 17 linear classification probes to the intermediate layers of the ResNet-50 and train them on three different dataset configurations and targets: NIH-CXR14 (pneumothorax) and PadChest (cardiomegaly and pneumothorax). This setup allows us to observe model behaviour during evaluation using subgroup-based calibration and layer-wise confidence curves. We find that the final linear probes achieve a high AUROC but poor calibration in the models. The layer-wise confidence analyses suggest that shortcuts emerge at different depths. Patterns consistent with localised shortcuts, such as drains, appear at later layers, while patterns consistent with diffuse shortcuts, such as scanner-specific noise patterns, emerge earlier, aligning with previous work. Finally, we conduct a manual analysis of the images, which reveals data quality issues in both NIH-CXR14 and PadChest. Our findings underscore that even SOTA models remain vulnerable to shortcuts, and the need for high-quality and well-annotated datasets to draw solid conclusions. Code can be found on our GitHub: this https URL.

---


### 124. [Task- and dataset-specific information in protein language models](https://arxiv.org/abs/2608.12090)

**<font color=#1a73e8>作者：</font>** Roman Joeres, Ilya Senatorov, Olga V. Kalinina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein language models (PLMs) have transferred the latest advances from natural language processing to computational biology. These models, trained on large corpora of protein sequence data, are widely used to translate amino acid sequences into latent-space embeddings, ready for use in diverse downstream tasks (DTs). By a common consensus, embeddings from the model's last layer are used, and the model's internal behavior remains poorly understood. We analyzed 13 PLMs across 15 DTs from 11 datasets to investigate the informativeness of embeddings created in intermediate PLM layers. We trained probe models on embeddings from each layer, compared their performance, and computed characteristics of the latent spaces they span to estimate the information they contain, and found that the last layers of PLMs rarely contained embeddings that led to the best results on downstream tasks. Furthermore, we identified a connection between DTs and the distribution across PLMs' layers of the relevant information to predict that task. For example, similarity between the pre-training objective and the objective of predicting properties of individual residues leads to a steady increase in understanding of such tasks across the layers of PLMs. On the other hand, for whole-protein tasks, we observe that the dataset, rather than the task itself, defines PLMs' ability to perform well on a DT. Embeddings from shallow layers of PLMs perform better for datasets that contain deep mutational scan (DMS) data, while datasets containing diverse natural proteins find most useful embeddings in the models' deeper layers. Additionally, we discover that the performance of PLMs drops significantly when tasks are introduced for artificial proteins.

---


### 125. [Graph-Structured Rubrics: Compiling Rubrics into Typed Evaluation Graphs for LLM Judges](https://arxiv.org/abs/2608.12097)

**<font color=#1a73e8>作者：</font>** Xi Chen, Jie Mu, Mo Xuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubric-based evaluators commonly treat rubrics as prompt context or flat criteria: they specify what to judge but leave criterion composition implicit, even when natural-language rules state it. We introduce Graph-Structured Rubrics (GSR), which compiles a rubric into a response-independent typed evaluation graph before observing responses. Criterion nodes elicit judgments; transformation, reduction, and gating operators compose them through named ports; and a task-specific output mapping, termed Readout, converts the unique sink into a score or preference. Compilation rejects malformed or type-incompatible graphs. Pointwise evaluation judges rubric dimensions separately before graph aggregation; pairwise evaluation reuses the graph with one judgment for each candidate under every criterion. Under GPT-OSS-120B, GSR improves exact score agreement by 0.62--6.75 percentage points over Prometheus-style scoring on four pointwise datasets and achieves the numerically highest end-to-end pairwise accuracy on two preference benchmarks under native tie and abstention policies.

---


### 126. [QV-PIC: Query-Aware Visual Position-Independent Caching for Efficient RAG Serving](https://arxiv.org/abs/2608.12121)

**<font color=#1a73e8>作者：</font>** Yilin Liu, Rui Meng, Wangze Ni 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) repeatedly prefills identical text chunks across queries, incurring redundant computations. Position-Independent Caching (PIC) mitigates it by reusing precomputed Key-Value (KV) across positions, but its efficiency is constrained by the large volume of text tokens. Rendering text chunks as images can compress the text into fewer visual tokens, but the rendered-image PIC suffers more severe quality degradation than the text PIC. This representation-specific gap primarily arises from contextual mismatches across independently compiled caches and the loss of fine-grained textual evidence during visual compression. Existing PIC repair methods mainly address the former through selective recomputation, but they incur online computation and cannot recover lost textual details. We propose QV-PIC, a query-aware dual-resolution PIC reuse framework guided by model-native templates. Offline, QV-PIC compiles visual caches under the model's native chat-template prefix, improving PIC quality without online recomputation. Online, it preserves global context with low resolution and restores fine-grained textual evidence within a high-resolution budget by cumulative query relevance scores, retaining the efficiency benefit of visual compression. Across six tasks, QV-PIC improves average F1 by 21.6 points over vanilla rendered-image PIC, closes the gap to vanilla text PIC, and surpasses optimized text PIC by 2.58 F1 while reducing TTFT by 17.2\%. Relative to full prefill, it cuts TTFT by 83.8%.

---


### 127. [SCOPE-Router: Cost-Aware Open-Set VLM Routing for Execution-Oriented Tasks](https://arxiv.org/abs/2608.12127)

**<font color=#1a73e8>作者：</font>** Tao Yu, Yifei Qu, Zhiqing Cui 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model routing aims to select the most suitable model from a candidate pool for each query, balancing quality and cost. Existing VLM routing research is limited to traditional VQA evaluation, lacks systematic calibration optimization for open-set scenarios, and employs training objectives that dilute multi-positive signals via softmax normalization without incorporating cost. We address these limitations with three contributions: (1)VLM-ExecRouterBench, the first execution-oriented VLM routing benchmark covering Code, Agentic, and Search domains with 11 candidate models spanning nearly two orders of magnitude in pricing; (2)SCOPE-Router, a dual-tower router that matches queries to model behavior profiles constructed via hybrid calibration (random/diagnostic/diversity sampling), enabling new models to join routing without retraining; (3)CRM+RCCR, an architecture-agnostic cost-aware objective that encodes cost preference into continuous relevance targets through per-pair independent scoring, eliminating multi-positive dilution while regularizing queries with similar routing preferences to be closer in the routing space. Empirically, SCOPE-Router achieves the best Rank Score on all three benchmarks, surpassing the runner-up by 1.84 points under OOD settings and by 6.75 points under doubly OOD open-set evaluation. When applied to four diverse routers, CRM+RCCR improves Rank Score by 1.25--6.21 points.

---


### 128. [SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges](https://arxiv.org/abs/2608.12129)

**<font color=#1a73e8>作者：</font>** Yuchao Wu, Junqin Li, XingCheng Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While retrieval-augmented generation (RAG) has proven effective at giving LLMs access to external knowledge, mainstream dense-retrieval implementations remain inherently limited in handling structured constraints and multi-hop reasoning. Graph-based methods address this by constructing knowledge graphs offline, but they often fragment semantics, incur high maintenance, and complicate incremental updates. We propose SAG (SQL-Retrieval Augmented Generation), a structured retrieval architecture that organizes documents into an event-entity index without building a global knowledge graph. SAG represents each chunk as a semantically complete event paired with its entities, forming a latent hyperedge that preserves n-ary relations without decomposing them into triples. At query time, SAG treats shared entities as join keys to connect related chunks. This dynamically yields a query-scoped neighborhood of events, and yet every piece of evidence remains the original chunk throughout. Experiments on HotpotQA, 2WikiMultiHopQA, and MuSiQue show that SAG achieves the best retrieval and end-to-end QA performance on every benchmark, with gains that widen as reasoning-chain complexity increases. On MuSiQue, where multi-hop evidence chaining is most demanding, SAG reaches 80.36% Recall@5, outperforming the strongest baseline by 11.52 points. This work paves the way for knowledge infrastructure that enables LLM agents to retrieve and reason over continually growing organizational knowledge.

---


### 129. [GUIDE: Governed Unified Intelligence for Document-to-Artifact Generation in Enterprise Settings](https://arxiv.org/abs/2608.12133)

**<font color=#1a73e8>作者：</font>** Shivali Dalmia, Sumukha Thoppanahalli, Mohammadreza Sediqin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise guideline documents are heterogeneous and multimodal, combining narrative text, complex tables, and embedded images. Existing LLM and VLM systems face hallucinated content, table structure degradation, and lack governed workflows extending beyond extraction to validation and artifact generation. This leaves enterprises to perform this manually, consuming 2-3 days per document. To address this, we introduce GUIDE, a governed multi-agent framework built on a shared versioned rule store with schema-validated inter-agent contracts and end-to-end provenance tracking. Six specialized agents handle parsing, VLM-driven extraction, consistency checking, evaluation, human-in-the-loop (HITL) escalation, and persona-tailored artifact synthesis. Evaluated on 120 real-world enterprise guideline documents, GUIDE achieves 96% document success, extracts 3,896 rules with 71.4% auto-approved, produces 812 deployment-ready artifacts, and reduces turnaround to 40-125 minutes per document.

---


### 130. [A corpus-specific clinical RAG system matches or outperforms newer frontier LLMs on HealthBench](https://arxiv.org/abs/2608.12138)

**<font color=#1a73e8>作者：</font>** Praveen Reddy, Charuta Mandke, Suvrankar Datta 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose large language models (LLMs) have recently been reported to match or exceed specialized clinical AI tools on medical benchmarks, but such comparisons draw on a narrow set of systems and on benchmarks developed largely in high-income settings. We evaluate VITA, a retrieval-augmented generation (RAG) system purpose-built for contextual knowledge retrieval in India and other low- and middle-income (LMIC) settings. VITA retrieves from a curated corpus of disease-specific guidelines, India-specific antimicrobial resistance data, national formulary constraints, and resource-limited care protocols; its architecture and corpus are proprietary, but the benchmark, the physician-written rubrics, and our full response and scoring outputs are public for independent verification. On 4,023 English-language HealthBench questions (80.5% of the benchmark), scored with a GPT-4.1 judge, VITA ranked first with 51.9% of possible rubric points, ahead of GPT-5.4 (46.1%), o4-mini (44.3%), Gemini 3.1 Pro (42.6%), and Claude Sonnet 4.6 (37.3%), and scored highest on 45.4% of questions. To test robustness to newer models and judge lineage, a 500-question subset was re-run against current-generation models (GPT-5.5, Claude Opus 4.8, Gemini 3.5 Pro, Grok 4.3) and graded by a neutral open-weight judge (DeepSeek-V4-Pro) sharing no lineage with any system tested. Here the gap narrowed to parity: VITA and GPT-5.5 were statistically indistinguishable on mean per-question score, while VITA led on points-weighted score and won the most questions. VITA's advantages in accuracy and completeness persisted under the neutral judge; its communication scores were lower. These results indicate that a purpose-built clinical RAG system remains competitive with frontier LLMs on an open benchmark, consistent with corpus specificity as a design variable that improves grounding at some cost to communication polish.

---


### 131. [Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention Spikes and Inter-Spike Plateaus](https://arxiv.org/abs/2608.12149)

**<font color=#1a73e8>作者：</font>** Zunhai Su, Bohan Sun, Xialie Zhuang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the first systematic study of Massive activations (MAs) in layer-interleaved HLA LLMs and uncover two architecture-aligned morphologies: MAs consistently spike immediately before full attention layers, forming pre-attention spikes (PAS), and can persist through intervening linear attention layers, giving rise to inter-spike plateaus (ISP). As full attention becomes denser, successive PAS become increasingly connected through ISP, ultimately recovering the stable MA morphology of full attention LLMs. We establish the recurrence of this organization across five linear attention architectures, six hybridization configurations, five data domains, and representative open-source hybrid models spanning 1.2B to 397B total parameters. Controlled pretraining of GDN-based hybrids at scales up to 1.3B shows that both morphologies emerge early and respond asymmetrically to output gating: full attention output gating strongly attenuates their absolute magnitudes without eliminating their layerwise organization, whereas removing GDN gates yields comparatively modest amplification. Mechanistically, our systematic-outlier analysis supports a shared lifecycle account governed by the timing of MA cancellation. PAS follows a localized write-sink-cancel process, while the extended persistence of ISP is consistent with delayed cancellation. At the full attention limit, this account recovers the stable MA morphology characteristic of full attention LLMs. Our code is available at this https URL.

---


### 132. [Who Thinks Best Depends on How Long You Let Them: Budget-Dependent Rankings in LLM Evaluation](https://arxiv.org/abs/2608.12150)

**<font color=#1a73e8>作者：</font>** Rodrigo Guedes de Souza, Alison R. Panisson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Standard evaluation of large language models assumes stable model rankings across inference conditions. We challenge this assumption by varying the token generation budget, i.e., the maximum tokens a model may produce, across seven levels (64--4,096), evaluating four models on three reasoning benchmarks (56,476 inferences). We report four findings: (i) 3--19% of items exhibit non-monotone behavior (accuracy decreasing with more budget), even after controlling for truncation, and this phenomenon is model-specific (cross-model overlap: 6--14%). (ii) Model rankings reverse across budgets on all benchmarks ($p {<} 0.01$, McNemar). (iii) Oracle analysis reveals model complementarity up to $+27.8$pp, most pronounced at constrained budgets. (iv) A budget-aware router captures 14.1% of the oracle gap cross-domain; budget features help within-domain ($+1.6$ to $+5.7$pp) but are domain-specific and hurt transfer ($-1.2$pp). These results argue for budget-conditioned evaluation protocols.

---


### 133. [Context Blindness in DPO: Mitigating Object Hallucination in MLLMs via Context-Calibrated Preference Optimization](https://arxiv.org/abs/2608.12158)

**<font color=#1a73e8>作者：</font>** Byungoh Ko, Jinyoung Park, Jongha Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have made rapid progress, yet they still exhibit object hallucination, generating plausible but incorrect descriptions that are inconsistent with the visual input. Direct Preference Optimization (DPO) mitigates this by training models to prefer non-hallucinated responses over hallucinated ones, and recent efforts further enrich the preference data with relevant context. However, it remains unclear whether DPO actually leverages such context. To investigate this, we propose Contextual Preference Gain (CPG), a simple metric that measures how much a model's preference strengthens when relevant context is provided. We find that higher CPG consistently corresponds to lower hallucination, yet standard DPO and its variants exhibit only limited CPG, indicating that they underutilize contextual information and thus remain prone to hallucination. To address this, we propose Context-Calibrated DPO (C$^2$-DPO), which directly maximizes CPG while preserving the original preference ordering. Across multiple benchmarks, C$^2$-DPO substantially reduces hallucination without compromising general reasoning, relatively reducing the Object HalBench hallucination rate of Qwen2-VL-Instruct-2B by 36%. Code is available at this https URL

---


### 134. [IF:CARGO: LLM-Based Semantic Compilation for Al-Native Rule Programming Games](https://arxiv.org/abs/2608.12195)

**<font color=#1a73e8>作者：</font>** Ting-Chen Hsu, Lianye Zhang, Jiangxu Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This case study presents IF: CARGO, an experimental puzzle game that uses a large language model as a semantic compiler rather than an autonomous game-playing agent. Players author IF/THEN rules in natural language, which the model translates into a constrained command schema for deterministic validation and execution by the game engine. This architecture creates a playable loop of expression, execution, observation, and revision, framing AI interaction as semantic debugging. A mixed-methods playtest with 24 participants across eight levels examined player attempts, thinking time, perceived controllability, adjustability, and interpretations of the AI's role. Results suggest that players generally understood the model as a translation intermediary and could revise their strategies through feedback, while periodic commands, multi-robot coordination, and rule-priority mechanics created greater cognitive and diagnostic demands. The study proposes a practical pattern for AI-native gameplay: constrain natural-language input, preserve player authorship, and ensure deterministic execution.

---


### 135. [Generation as Auxiliary Supervision: Enhancing Visual Understanding at Zero Inference Overhead via Decoupled Embedding Prediction](https://arxiv.org/abs/2608.12209)

**<font color=#1a73e8>作者：</font>** Zhongbin Guo, Jiahao Xie, Dongling Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) have achieved remarkable progress, visual understanding and generation are typically treated as divergent objectives. Existing unified frameworks often rely on discrete visual tokenization or diffusion objectives whose generative targets differ from the continuous representations consumed by visual understanding models, making direct transfer to enhance existing pretrained MLLMs non-trivial. In this work, we present GAS, a generation-guided training framework that reinterprets visual generation as auxiliary supervision for representation learning. Concretely, GAS adapts Next Embedding Prediction (NEP) as a cross-modal generation paradigm within a decoupled Mixture-of-Transformers (MoT) architecture. By maintaining a shared lower trunk and parallel upper layers, GAS lets generation losses enrich the shared visual pathway with finer spatial precision and stronger visual retention while shielding the upper understanding layers from direct generation gradients. To maximize this synergy, we further construct highly correlated generation tasks that demand deep cognitive grounding rather than generic synthesis alone. Across model scales and training stages, GAS improves aggregate multimodal understanding, with its most reliable gains on perception and spatial comprehension. Crucially, because the auxiliary generation branch is discarded after training, these gains incur zero inference overhead. Extensive controlled comparisons and representation-level analyses further clarify when and why generation-guided training benefits understanding, and demonstrate the feasibility of generation-guided training as a practical route to stronger multimodal understanding.

---


### 136. ["Pharos Night: Crown Pursuit": An AI-Native Deck-Building and Tactical Arena Game Design Based on Multi-Agent Systems](https://arxiv.org/abs/2608.12216)

**<font color=#1a73e8>作者：</font>** Ting-Chen Hsu, Jueyao Liu, Yanzi Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With advancements in generative AI technology, an increasing number of researchers have begun exploring AI-native games in which gameplay rules are directly driven by generative AI. This paper presents "Pharos Night: Crown Pursuit," an AI-native deck-building and tactical arena game based on a multi-agent system. The game uses large language models to generate materials and cards, support NPC decision-making, and mediate natural-language interactions. During play, players collect materials, describe desired card effects in natural language, and choose whether to negotiate or fight with NPCs in the arena. To constrain model-generated outcomes, the system parses responses as structured JSON, constructs card effects from predefined mechanics, and maps qualitative effect levels to designer-specified numerical values. A small-scale playtest with 13 participants suggests that the system can provide strategically meaningful and engaging AI-driven gameplay, while also revealing challenges related to predictability, transparency, and player control. This work demonstrates the potential of multi-agent generative AI systems for creating more emergent digital game experiences.

---


### 137. [Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge](https://arxiv.org/abs/2608.12218)

**<font color=#1a73e8>作者：</font>** Arda Uzunoglu, Benjamin van Durme, Daniel Khashabi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly trained and deployed with long contexts that span documents, code repositories, and interaction histories. This scaling reflects the implicit assumption that training on longer contexts will only help the model by exposing it to richer evidence. We challenge this view by studying how the context window shapes a model's mode of learning, shifting it between parametric internalization and contextualization. We propose the Information Abundance Paradox, which hypothesizes that abundant relevant information in the training context can reduce the incentive to encode that information parametrically, thereby increasing reliance on context. In pretraining with long documents, increasing the context window improves language modeling, natural language understanding, and closed-book MCQA only up to an intermediate optimum, after which performance consistently declines. In supervised fine-tuning, more task-relevant train-time context improves performance with supporting context, but reduces robustness when context is absent or misleading at test time. Our analysis suggests that this behavior arises when longer context provides a lower complexity solution. Mechanistically, training with informative context shifts gradient pressure from feed-forward networks, often linked to parametric knowledge, toward attention modules, and causal interventions show that this shift increases reliance on context during inference. Overall, these findings support the Information Abundance Paradox and suggest that scaling toward near-infinite context is not simply a matter of supplying more data, even when high-quality long-context data is abundant.

---


### 138. [SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought and Multi-Objective Process Reward](https://arxiv.org/abs/2608.12220)

**<font color=#1a73e8>作者：</font>** Zile Zhou, Huining Yuan, Weichen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Vision-Language Models (VLMs) exhibits a critical bottleneck in robust spatial reasoning. Recent reinforcement learning (RL) methods aim to close this gap with verifiable outcomes, yet they suffer from poor credit assignment across intermediate reasoning steps. Concurrently, structured reasoning approaches overlook the critical depth perception necessary for comprehensive 3D understanding. To address these challenges, we propose SCOUT (Structured Chain-Of-Thought Utilizing Process-Supervised RL Training). Specifically, we design a structured Chain-of-Thought (CoT) framework that explicitly models 3D environmental perception to ensure robust spatial understanding and reasoning. Furthermore, we introduce a novel RL algorithm featuring multi-objective process rewards and a tailored advantage estimation method, facilitating fine-grained credit assignment across distinct segments of the reasoning trajectory. To support our framework, we develop SCOUT-24k, a structured spatial reasoning CoT dataset synthesized through a customized pipeline. Extensive evaluations demonstrate that SCOUT-3B improves upon baseline models by 16.85% and 6.3% on general spatial benchmarks and complex spatial reasoning tasks respectively. Notably, our larger SCOUT-7B even outperforms GPT-4o by a margin of 4.28%. Moreover, despite being trained exclusively on single image, SCOUT-7B exhibits robust out-of-domain generalization to multi-image and video scenarios. These empirical results render SCOUT as a critical step towards next generation of spatially-aware VLMs.

---


### 139. [An Agentic Workflow for Legacy HPC Modernization: Converting the Two-Electron-Integral Core of GAMESS](https://arxiv.org/abs/2608.12249)

**<font color=#1a73e8>作者：</font>** Yuzhong Shen, Masha Sosonkina, Peng Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modernizing legacy Fortran is a problem of volume: the transformations are individually routine, but the codebases can be enormous, and across much of computational science the work simply goes undone. We propose an agentic workflow that takes this work on at production scale, and we set out to measure how far such delegation can reach. In this work, three prompt-specialized agent roles operate under a version-controlled specification that the agents themselves authored and revised, while humans hold a small number of gates. The arrangement is kept safe by an exact verification oracle inherited from the domain, and the boundary of safe delegation lies exactly where that oracle stops seeing.
We apply the proposed workflow in a case study, converting the two-electron-integral routines of GAMESS (General Atomic and Molecular Electronic Structure System), a mature quantum-chemistry package with a 48-year development history, from fixed-form Fortran 77 to free-form Fortran 2008. The scope of this work was twelve source files, 56,448 lines, and 225 subroutines for computing electron repulsion integrals. The agents ran as three Claude Code roles in isolated worktrees, and the work spanned four Claude model generations. Because the GAMESS group ships a standard test suite whose printed energies its user community treats as canonical, we could adopt bit-for-bit reproduction of those energies as the merge criterion, where a deviation in the twelfth decimal place counts as a failure rather than drift. All twelve source files pass a 51-test validation battery comprising the 49 standard GAMESS tests and two additional calculations, and across 612 test runs the number of chemistry-relevant differences is zero, and every file also passes the Jenkins tests that are used for continuous integration.

---


### 140. [One Frozen Simulator Is Not Enough: Simulator Collapse in Multi-Agent RL](https://arxiv.org/abs/2608.12253)

**<font color=#1a73e8>作者：</font>** Simon Yu, Nicholas Tomlin, Marwa Abdulhai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning for human-AI interaction typically relies on a single large language model to simulate user behavior. We show that this approach systematically fails to generalize, and trace the failure to simulator collapse: because the simulator LLM is mode-collapsed, an LLM policy trained against it overfits to narrow strategies that exploit the simulator's dominant mode, and such a policy transfers poorly to unseen simulators and real users. We formalize this collapse theoretically and propose two complementary solutions, one at inference time and one at training time. The inference-time solution, Verbalized Sampling, broadens the simulator's behavior by sampling from a verbalized response distribution, reducing mode collapse. The training-time solution, Co-Training, jointly optimizes the policy against a population of trainable simulators, preventing it from overfitting to any single simulator's mode. We validate both solutions on three multi-turn benchmarks: Persuasion for Good, $\tau^2$-bench, and CooperBench. Verbalized Sampling improves held-out success by up to 9% over single-simulator RL, and Co-Training pushes gains further to 14%; the human study shows similar gain on real users. Both solutions preserve the policy diversity that collapses under single-simulator RL. To support further work in this direction, we release SCOPE, an open-source framework for Population Co-Training multi-agent RL. More broadly, our results suggest that the diversity of the training environment, not only the policy, is critical to the generalization of multi-turn RL to real-world deployment.

---


### 141. [Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams](https://arxiv.org/abs/2608.12262)

**<font color=#1a73e8>作者：</font>** Weihao Bo, Shan Zhang, Yanpeng Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have been growing the capability for scientific writing and collaboration. For example, OpenAI Prism is a free workspace for scientific writing and collaboration. One important feature in Prism is turning scientific diagrams directly into LaTeX TikZ code. In this paper, we build a benchmark, Diagram-MMU, a multi-modal benchmark designed to assess MLLMs' ability for scientific diagram parsing and understanding. Diagram-MMU features 3.7k curated diagrams and 18.3k human-validated questions across six domains. It evaluates MLLMs on three tasks common in vibe writing workspaces: diagram-to-code parsing, diagram-to-code editing, and diagram question answering, alongside agentic settings per task. The evaluation of 12 MLLMs reveals that diagram-to-code tasks are more challenging than diagram question answering: models can reason well over diagrams but struggle to parse and edit them, underscoring the need for methods to enhance MLLMs' capability in diagram-to-code generation. Under agentic settings, most models improve parsing and editing performance but degrade on question answering, while Claude-4.6 Opus consistently improves across all three tasks. Project Page: this https URL.

---


### 142. [A Cascaded Unsupervised-Supervised NLP Pipeline for Detecting Accusatory Language in Public Procurement](https://arxiv.org/abs/2608.12269)

**<font color=#1a73e8>作者：</font>** Bryan Torres, Daniel Riofrío, José Vega-Sánchez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Public procurement involves the allocation of substantial financial resources; therefore, continuous oversight through audits, controls, and monitoring mechanisms is essential. However, stakeholder comments and publicly available government data are often underutilized, despite their potential to reveal procedural irregularities. To address this gap, this paper analyzes metadata from Ecuador's Sistema Oficial de Contratación Pública (SOCE, Official Public Procurement System), with particular emphasis on participant comments generated during the pre-contractual phase. We propose a hybrid modeling framework that integrates unsupervised clustering and supervised classification within a natural language processing (NLP) pipeline to uncover latent patterns and detect potentially irregular procurement processes. Semantic embeddings are generated using Word2Vec, LLaMA, and RoBERTa, followed by Gaussian Mixture Models (GMMs) for unsupervised clustering. A supervised classification stage is then applied to identify accusatory or whistleblowing-style comments. Experimental results show that the combination of domain-trained Word2Vec embeddings, GMM-based clustering, and a Random Forest classifier achieves high precision and recall, even under severe class imbalance. These findings demonstrate that lightweight, domain-adapted NLP architectures can effectively support risk identification and enhance transparency in public procurement systems without requiring large-scale computational infrastructure.

---


### 143. [Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based LLM Agents](https://arxiv.org/abs/2608.12273)

**<font color=#1a73e8>作者：</font>** Junliang Liu, Ruoyu Li, Wenxin Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on third-party skills, using natural-language descriptions for selection and instruction bodies for planning. This progressive-disclosure design exposes two sequential control points to untrusted publishers: a static skill may steer an otherwise correct task onto an unnecessarily costly trajectory. Prior work studies selection manipulation, malicious skill instructions, and tool-chain resource amplification largely separately, leaving their end-to-end composition unclear. We introduce Convergent Detour Hijacking (CDH), a text-only, runtime-independent attack that couples these stages. Under shared semantic cover, a description establishes relevance during selection, while an aligned body reuses that rationale to fabricate plausible dependencies during planning. CDH attracts an attacker-controlled coordinator alongside legitimate skills, recruits unnecessary benign skills into a bounded detour, and then re-enters the original route to preserve task completion. We evaluate it across multiple LLM backends and 491 held-out tasks under single-task and multi-turn conditions. On DeepSeek-V4-Pro, the matched coordinator is selected in 80.02% of tasks; among coordinator-hit runs that complete tasks, token consumption and end-to-end execution time increase by 66.91% and 92.45%, respectively, while aggregate task completion remains comparable. Thus, correct outcomes do not guarantee trajectory integrity or cost safety.

---


### 144. [Beyond Trial-and-Error: Agentic Optimization for Image-to-Video Adherence](https://arxiv.org/abs/2608.12290)

**<font color=#1a73e8>作者：</font>** Aman Tyagi, Hemanth Boinpally, Jonathan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern black-box Image-to-Video (I2V) models offer powerful capabilities in automated content creation, yet their lack of fine-grained control and reliability presents significant challenges in professional workflows. Their inherent stochasticity causes minor variations in textual prompts or hyperparameters to yield drastically different outputs often necessitating inefficient, brute-force trial-and-error processes. To address these limitations, we introduce the ``Agentic Self-Improvement" framework, which reframes video synthesis into a closed-loop, goal-directed optimization. Our framework systematically navigates the generation parameter space using a novel two-stage approach. In the first stage, an iterative prompt optimization loop uses a multimodal Large Language Model (mLLM) to refine the input prompt. This refinement implements two automated evaluations: Davidsonian Scene Graph (DSG) queries ensure semantic adherence, and Common Mistake Questions (CMQ) for artifact detection. At the second stage, we use Bayesian optimization to efficiently co-optimize stochastic seeds and CFG scales. This search is guided by a suite of quality metrics, including the novel Video-Text Adherence (VTA) score derived from the DSG and CMQ evaluations. Our framework significantly outperforms unguided search methods: in human preference studies, videos generated via our agentic approach were strongly preferred over baseline outputs, achieving win rates up to 69\%. This work provides a practical and extensible methodology for enhancing the predictability and control of state-of-the-art video generation models, moving the field beyond speculative curiosities toward reliable, production-ready tools.

---


### 145. [Constructing Dynamic Master Logic Models as Knowledge Graphs for Complex System Diagnostics Using Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2608.12304)

**<font color=#1a73e8>作者：</font>** Saman Marandi, Yu-Shu Hu, Mohammad Modarres  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dynamic Master Logic (DML) provides a hierarchical framework for representing system behavior by linking functional objectives to underlying structural elements. However, DML construction typically relies on expert interpretation of technical documentation, limiting scalability for complex systems. This study presents a framework for automated construction of DML models from system descriptions and their representation as Knowledge Graphs (KG-DML), using Retrieval-Augmented Generation and Large Language Models as enabling tools. Building on prior work with small-scale systems, the framework extends automated KG-DML construction and evaluation to substantially larger and more complex systems. Model construction proceeds across the DML hierarchy using targeted retrieval while preserving functional dependencies and explicit logical relationships. The resulting KG-DML supports diagnostic reasoning, safety assessment, upward failure propagation, and downward dependency tracing. A multi-level validation methodology evaluates layer-specific precision and recall, logical gate consistency, and overall structural integrity. Application to the Low-Pressure Coolant Injection system of a decommissioned Boiling Water Reactor demonstrates consistent reconstruction across repeated runs. The results show that automated KG-DML construction can transform technical documentation into executable functional models for diagnostic and reliability analysis.

---


### 146. [DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation](https://arxiv.org/abs/2608.12308)

**<font color=#1a73e8>作者：</font>** Yan Deng, Fei Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial vision-language navigation (VLN) requires an embodied agent to integrate visual evidence over time, plan future actions, and determine when it has reached a navigation goal under partial observability. Although recent VLA models offer a promising perception-to-action paradigm, adapting them to aerial navigation remains challenging due to limited historical context, short planning horizons, and unreliable implicit termination. To address these challenges, we propose DreamFly, a diffusion-based aerial VLN framework built on Dream-VLA. DreamFly introduces a causally aligned historical memory that augments the current visual representation using only observations preceding the current decision step, enabling temporal reasoning without future information leakage. We further formulate navigation as receding-horizon diffusion planning, where the policy predicts a $K$-step action chunk but executes only the first action before replanning. This plan-$K$, execute-one strategy uses future actions as auxiliary planning targets while preserving closed-loop visual feedback. Finally, LiteStop estimates the stop probability directly from action logits at the initial all-mask state, decoupling explicit termination from action generation. Experiments on the OpenFly benchmark demonstrate consistent improvements in seen and unseen environments. DreamFly achieves 32.04%/29.46% SR and 28.22%/23.54% SPL on the test-seen/test-unseen splits, respectively, outperforming all compared methods on both metrics while attaining the lowest navigation error. These results demonstrate the effectiveness of jointly modeling historical context, future action structure, and explicit termination for aerial VLN.

---


### 147. [StateFlow: Building, Evolving, and Accessing 3D World States for Previsualization](https://arxiv.org/abs/2608.12314)

**<font color=#1a73e8>作者：</font>** Yuyang Yin, Zixiang Li, Longxuan Deng 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Previsualization is an intermediate layer between ideas and production in film, games, architecture, and urban design. It lets creators iteratively refine scenes, actions, cameras, and spatial-temporal dynamics. Yet existing generative methods rely on simple prompts to jointly control all of these factors through one-shot image or video synthesis, offering weak controllability and limited support for iterative editing. Fundamentally, a world comprises multiple elements with geometry, appearance, and other attributes, together with cameras. Different frames are produced through local modifications or recombinations of this shared state, which is otherwise largely reused. Therefore, we argue that the missing component is an explicit and persistent working state. To address this, we present StateFlow, a state-centric framework for generative previsualization. Rather than generating videos in one shot, StateFlow uses an editable 3D world to organize scene structure, evolution, and cameras, while off-the-shelf video models enhance visual quality when higher fidelity is desired. This world is maintained as a persistent structured 3D state of scene elements and camera configurations, serving as the core working representation for previsualization. Built on this insight, StateFlow has three stages to construct, evolve, and access the world state. State construction lifts generated 2D content into a coherent 3D world through prior-guided, conflict-aware dual-view initialization, while State evolution translates user intent into structured state transitions while preserving world memory, avoiding full-scene regeneration for each edit. State access uses render-feedback reflection to refine camera plans into visually feasible trajectories, avoiding reliance on VLM semantics alone. Experiments show that StateFlow produces high-quality 3D worlds for video creation and game-like prototyping.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 148. [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Peidong Wang, Zhiming Ma, Ying Chang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Embodied agents are increasingly built as systems around foundation models, where performance depends not only on model weights but also on the skills, context, action interfaces, and execution harness surrounding the model. While supervised fine-tuning and reinforcement learning can adapt agents to new environments, they require additional data, rewards, and training runs; meanwhile, many train-free code-centric approaches rely on programmable robot APIs that may be unavailable in fixed-interface settings. We propose SHAPER, a self-evolving framework for train-free embodied adaptation that keeps model parameters frozen and improves the non-parametric agent system by evolving reusable skills and a context-code harness through target-environment rollouts. In SHAPER, the same frozen model can serve as both planner and optimizer, refining its external skills and context-code harness without parameter updates. We evaluate SHAPER on VLABench and ESI-Bench, covering embodied agents with different low-level action interfaces, and compare against pure execution, supervised fine-tuning, and test-time-scaling baselines such as verifier-free selection and voting. Our results suggest that skill-and-harness optimization is a practical route to self-evolving embodied agents when model training is expensive, unavailable, or undesirable.

---


### 149. [Market-Information-Aware Gated-LoRA of Foundation Models for Transferable Day-Ahead Electricity Price Forecasting](https://arxiv.org/abs/2608.11359)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hang Fan, Wei Wei, Shengwei Mei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electricity price forecasting is crucial for market participants but remains difficult because prices are volatile, market-specific, and closely tied to anticipated system conditions. Existing supervised methods depend largely on market-specific historical data, limiting their use in newly established or data-scarce markets. This paper proposes a market-information-aware adaptation framework that transfers the Chronos-2 time-series foundation model to day-ahead electricity price forecasting. It first constructs a multi-source market information (MSMI) interface aligning 7-day price context with pre-clearing supply--demand, reserve, maintenance, generator-capacity, and intertie variables, and then trains a source-domain gated low-rank adapter (LoRA), updating about $1\%$ of model parameters without target-market labels. The gate scales the frozen source adapter according to reserve-tightness and operating-state signals. A leave-one-market-out protocol is adopted for evaluating cross-market transferability. Experiments on four Chinese provincial day-ahead spot markets show that the proposed framework reduces the average MAE/RMSE by $6.24\%/7.99\%$ relative to market-information-aware zero-shot Chronos-2 and by $3.05\%/3.52\%$ relative to vanilla Source-LoRA. Experiments show that the gain is not reproduced by a learned global scalar or by random gate initialization, while the additional improvement over Source-LoRA is limited. These results suggest that market-structured inputs and state-dependent gated LoRA can provide a practical transfer path for data-scarce electricity markets.

---


### 150. [Is Convergence Inevitable? Tracing Output Homogeneity Back to Base Models](https://arxiv.org/abs/2608.11426)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alexandrine Fortier, Hazel Chen, Peter West  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The lack of diversity in LM content is widely attributed to the alignment process, but how and where exactly in the pipeline this collapse begins is unknown. We argue that output homogeneity is likely learned during the pretraining phase, and only \emph{revealed} or magnified during the alignment process. Specifically, we find that semantic convergence is observed from the first alignment stage--the instruction-tuning phase (SFT)--suggesting that homogeneity might already exist in the pre-alignment model. To investigate this, we conduct controlled SFT experiments examining how training data influences output convergence on specific input/output pairs. We find that convergence can be revealed and amplified, but not introduced by the SFT data, supporting its role as a catalyst rather than a cause. To further test whether homogeneity originates before alignment, we measure convergence in base models. We find that instruct-like collapse can be induced through prompting alone, even without alignment. Taken together, our results suggest that semantic convergence may arise naturally from the objectives underlying LM training, making it difficult to mitigate through post-alignment interventions alone.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-164](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
