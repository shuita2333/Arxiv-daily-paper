# 🧠 大模型相关研究 | 2026年09月23日

> 本类共 **379** 篇论文：已确认 **359** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-379](./part-08.md)

---

### 251. [A paired synthetic construction-site image dataset for robust computer vision under adverse conditions](https://arxiv.org/abs/2609.24075)

**<font color=#1a73e8>作者：</font>** Viet Huy Duong, Ruoxin Xiong, Md Abdullah Al Forhad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-vision systems used for construction monitoring can degrade under adverse environmental and visual conditions, yet such conditions remain underrepresented in existing construction image datasets. We present ConSynth-X, a paired synthetic construction-site image dataset containing 34,199 images derived from 3,109 real-world source scenes. The dataset comprises 11 condition-specific subsets spanning precipitation, fog, nighttime illumination, adverse weather at night, and small-object or long-distance views. Each synthetic image is linked to its corresponding source scene, enabling controlled comparison across environmental and visual conditions. ConSynth-X includes source-derived annotations, generation metadata, provenance information, and image-quality indicators, supporting object detection, image captioning, visual grounding, and visual question answering. Technical validation evaluates source-synthetic fidelity and alignment with real adverse-condition imagery using embedding-based similarity and distributional analyses. The dataset provides a structured resource for evaluating and improving the robustness of construction vision and vision-language models under challenging field conditions.

---


### 252. [LeaseGuard: Incumbent-Preserving Admission Control for Privileged LLM Agents](https://arxiv.org/abs/2609.24077)

**<font color=#1a73e8>作者：</font>** Junru Zhu, Yixin Yang, Xiaoqing Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privileged language-model agents can satisfy a new system task by displacing a healthy incumbent that depends on the same file, process, socket, lock, or capacity allocation. This failure arises because execution privilege determines whether an operation can run, not whether the requester may preempt the current resource owner. We present LeaseGuard, a deterministic admission layer that represents preemption authority through canonical resource leases, incumbent-health checks, effect-aware admission, coexistence limits, safe alternatives, and resource-scoped overrides before adapter execution. We evaluate it on a frozen benchmark of 60 newly authored conflict scenarios with matched controls across two local model families. Relative to a preservation prompt, LeaseGuard reduces unauthorized preemption from 73.3% to 0.0% and increases safe completion by 70.0 percentage points (scenario-clustered 95% CI [60.8, 79.2]). Requested-task success changes by -3.3 points (95% CI [-9.2, 2.5]). The fully evaluated v0.2 broker also rejects a forged incumbent task identity in a hash-linked stress audit. Expiry-only reclamation can still expose a healthy incumbent after missed renewal. The evidence supports incumbent-preserving admission when effects are completely mediated, task ownership is authenticated, and lease expiry reflects incumbent liveness.

---


### 253. [From Content Generation to Learning Support: Pedagogy-Guided Generative Video Tutors for STEM Learning](https://arxiv.org/abs/2609.24083)

**<font color=#1a73e8>作者：</font>** Xinchen Ma, Shuimu Wang, Gaole He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI enables scalable production of educational videos, but current systems largely focus on producing visually coherent content rather than supporting learning. As a result, generated videos often lack explicit pedagogical structure, reliable quality control, and mechanisms for assessing learner understanding or addressing misconceptions. In this work, we introduce PIVOT (Pedagogy-guided Instructional VideO Tutoring), a generative video tutoring framework for STEM learning via learning-centered instructional support.1 Inspired by conventional teaching workflows, our framework integrates pedagogy into the full generation pipeline: it first uses instructional principles to guide storyboard generation, then produces verified multimodal videos through code-centric generation and a pedagogical verification harness, and finally connects videos with assessment and misconception-aware remediation. Experiments and expert evaluations across four STEM domains show that our framework produces educational videos with pedagogically aligned content, clear and engaging presentation, coherent instructional flow, and perceived effectiveness for learning. These findings suggest a human-centered perspective on educational content generation: generative systems should be evaluated and designed not only by what they produce, but also by how they support teaching practices, learner understanding, and corrective feedback.

---


### 254. [From Bits to Beliefs: Recoverable Semantic Fingerprints for Black-Box Verification of Large Language Models](https://arxiv.org/abs/2609.24084)

**<font color=#1a73e8>作者：</font>** Jiaxin Hong, Yuxin Peng, Hongyao Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight large language models (LLMs) can be copied, modified, and redeployed behind black-box APIs, making post-release ownership verification difficult. Existing black-box fingerprints often rely on secret query-key pairs that reproduce predefined responses, and can therefore be easily disrupted by fine-tuning, pruning, quantization, model merging, and serving-time prompt changes. We propose SimPrint, a recoverable semantic fingerprinting framework for black-box LLM ownership verification. Rather than relying on isolated exact matches, SimPrint encodes a private owner signature into a coded semantic fingerprint domain, distributing ownership evidence across natural binary question-answering probes. It implants only base-deviating probes through a low-interference batch update that preserves the original model behavior, and later recovers the signature by parsing suspect-model responses into reliable bits or erasures with an error-correcting recovery mechanism. Because verification only uses input-output queries, SimPrint remains applicable when model weights or activations are inaccessible. Experiments on three open-weight LLMs show that SimPrint reliably recovers the owner signature in both clean and modified settings, remains robust under fine-tuning, pruning, quantization, model merging, and serving-time perturbations, and maintains comparable downstream utility.

---


### 255. [Incremental Consistency Execution for Autonomous Intelligent Systems](https://arxiv.org/abs/2609.24090)

**<font color=#1a73e8>作者：</font>** Cheng Li, Jiexiong Liu, Yixuan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon autonomous intelligent systems rely on heterogeneous components such as large language models, databases, external APIs, and rule engines, while their external states continuously change during execution. Re-executing the entire workflow after every change introduces substantial redundant computation. This paper proposes an incremental consistency execution method based on task fact contracts, field-level dependency masks, and state perturbation result invariant domains. After an initial verified execution, the system constructs conservative invariant domains for critical inputs and uses them to determine whether downstream results can be safely renewed without re-invoking expensive components. When re-execution is required, only the smallest affected output fields are recomputed, and an equivalence barrier prevents unnecessary downstream propagation. A submission-time version consistency gate further ensures the safety of side-effecting actions. Experiments on industrial fault diagnosis, enterprise analytics, and LLM-based multi-tool assistants show that the proposed method significantly reduces expensive component calls and end-to-end latency while maintaining high consistency and low incorrect-reuse rates.

---


### 256. [DocMIDE: Learning Multi-Hop Implicit Derivation in Visually Rich Documents](https://arxiv.org/abs/2609.24092)

**<font color=#1a73e8>作者：</font>** Jeremy Cerwin Wang, Wai Kit Wong, Jeff Kai Tai Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world document processing systems rely on rigid, predefined schemas, yet critical target fields often lack direct visual counterparts on the page. Extracting these implicit values requires multi-hop derivation, such as aggregating sub-categories or reasoning over visual marks. While existing methods handle explicit text spans or simple implicit queries, they fail at multi-hop visual reasoning even after standard fine-tuning: models retrieve incorrect visual evidence, or retrieve it correctly and then skip the intermediate steps of the derivation. To address this, we introduce DocMIDE, a fine-tuning framework that trains compact vision-language models to retrieve visual evidence explicitly before deriving an answer. DocMIDE constrains generation to a plan-retrieve-derive structure and optimizes it with Group Relative Policy Optimization under a four-component, rule-based reward that scores output format, the retrieved evidence block, every intermediate derivation step, and the final value against a verified reference trace. On a 4,151-pair implicit extraction benchmark, DocMIDE raises accuracy from 70.8% to 95.9% on Qwen3.5-4B from only a small set of annotated examples, and transfers to a second backbone architecture. Supervised demonstrations alone do not close this gap at any budget we tested; rewarding the intermediate steps is what does.

---


### 257. [WidgetVA: A Widget-Centric Framework and Benchmark for Agentic Visual Analytics](https://arxiv.org/abs/2609.24094)

**<font color=#1a73e8>作者：</font>** Yutong Chen, Zhike Tang, Zhihao Mai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual analytics (VA) enables sensemaking through interactive visualization, but effective analysis often requires experts to translate high-level intents into long sequences of interface operations and iteratively interpret visual feedback. We study whether modern vision-language models (VLMs) can take on this role as autonomous VA operators that observe the interface, plan multi-step exploration, execute interactions, and adapt based on intermediate visual feedback. To support systematic development and evaluation, we first introduce WidgetVA, a widget-centric agentic VA framework that standardizes interactive components as structured widgets with unified action (e.g., filter and zoom) and perception-query (e.g., selection summaries) APIs. This standardization supports two modes of system construction: wrapping an existing VA system to make it agent-operable without rebuilding it, and composing a new system from widgets as modular building blocks. To help agents coordinate across widgets rather than plan each interaction from scratch, each widget further packages reusable analytical workflows, giving agents more than a bare set of callable functions to plan over. Building on this framework, we present WidgetVABench, a benchmark of single- and multi-widget VA tasks that require agents to perform multi-step interactions to uncover evidence and produce verifiable results. Each task also provides fine-grained reference annotations so that WidgetVABench can score Answer, Reference Trace Similarity, and State separately rather than collapsing agent performance into one success score. Experiments across multiple VLMs show that our framework provides an effective scaffold for agentic VA, while the diagnostic measures expose persistent limitations for future work. The WidgetVA framework and WidgetVABench have been released in this https URL.

---


### 258. [A$^2$Safe: Counterfactual Evidence-Aligned Adaptive Agent Collaboration for Safe and Effective Visual Question Answering](https://arxiv.org/abs/2609.24098)

**<font color=#1a73e8>作者：</font>** Quanxing Xu, Ling Zhou, Xian Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Question Answering (VQA) with Multimodal Large Language Models (MLLMs) requires not only producing safe and effective responses, but also grounding safety decisions in the multimodal evidence that determines risk. Recent safety-alignment methods improve refusal behavior and contextual risk awareness, yet correct safety outcomes may still rely on superficial textual or visual correlations, particularly when risk emerges from interactions between individually benign image and question content. To address this issue, we propose A$^2$Safe, a counterfactual evidence-aligned adaptive agent collaboration framework for safe and effective VQA. A$^2$Safe organizes localized visual observations, textual intent, and cross-modal risk relations through a Grounded Safety Evidence Board, making the basis of safety decisions explicit. Counterfactual safety evidence alignment enforces invariance to safety-irrelevant changes while requiring appropriate safety-state and response-mode transitions when risk-critical evidence is minimally altered. The resulting evidence state further supports adaptive collaboration, enabling direct answering when grounded evidence is sufficient and invoking policy critique and response revision when evidence is risky, uncertain, or conflicting. Under complementary safety-critical and general VQA protocols, A$^2$Safe achieves a 95.72 SIUO safety score, reduces the benign refusal rate on MOSSBench to 14.67%, and maintains an average general VQA score of 78.34 with 27.8% token overhead. These results support counterfactual evidence-aligned adaptive collaboration for safe and effective multimodal question answering.

---


### 259. [A Task-Oriented Multi-Agent Framework for Complex Wearable Health Analysis](https://arxiv.org/abs/2609.24107)

**<font color=#1a73e8>作者：</font>** Kunpeng Yang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Wearable health questions often combine data retrieval, longitudinal analysis, and health advice over structured records. Prompting a single large language model with a complete record and a composite query obscures whether every request is executed and which evidence supports the answer. We propose a task-oriented multi-agent framework that represents a composite query as distinct intents and typed tasks with explicit intra-intent dependencies. Specialized agents execute retrieval, analysis, and advice tasks; isolated intent states preserve request boundaries and evidence relationships before aggregation. We evaluate the framework on a synthetic dataset of $10{,}000$ virtual users with one month of longitudinal wearable records, covering structured data retrieval, multi-intent recognition, and overall response quality. Across $1{,}500$ retrieval questions, the Query Agent achieves $98.3\%$ accuracy, compared with $97.9\%$ for the Direct LLM baseline, while reducing average query-stage token consumption from $6{,}869$ to $3{,}136$. On $180$ multi-intent questions, the Manager Agent achieves $100.0\%$ Multi-Intent Coverage and $94.4\%$ Multiset Jaccard Similarity. Under the current synthetic evaluation setting, our method receives higher mean Trustworthiness and Transparency scores on both question categories, whereas Actionability does not improve consistently. These results provide preliminary evidence that explicit task organization can support task-relevant data access and data-grounded longitudinal analysis, while leaving health advice generation and validation on real wearable data as open challenges.

---


### 260. [EDGEGEN: Improving Tool-Calling Agents Beyond Happy Paths with Synthetic Edge Case Generation](https://arxiv.org/abs/2609.24115)

**<font color=#1a73e8>作者：</font>** Harshavardhan Abichandani, Penny Chong, Jiyuan Shen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-calling LLM agents are increasingly deployed in enterprise applications. However, effective evaluation and optimization require high-quality, diverse task datasets that are often difficult to obtain due to privacy and other constraints. Existing synthetic task generation methods often produce generic tasks that ignore an agent's underlying state or database and fail to reflect real-world usage diversity. We propose EdgeGen, a synthetic task generation framework that extracts compliance rules from an agent's specification and uses them to generate database-grounded edge-case tasks designed to violate these rules. When combined with existing synthetic data generation techniques, EdgeGen enables agent improvement through finetuning and harness optimization. The resulting pipeline forms a fully automated closed-loop system that requires no human annotation. Finetuning on data generated by EdgeGen yields a consistent mean progress improvement of 2 percent to 42 percent on tau2bench airline domain, while other baseline methods show degradation for some models. On the other hand, for harness optimization, our method shows a mean progress improvement of 10 percent and 30 percent over the human-curated and base harnesses, respectively, for the Gemma-4-e4b model.

---


### 261. [Re:CAP - Auditing Retrieval Coverage in Production RAG Pipelines](https://arxiv.org/abs/2609.24122)

**<font color=#1a73e8>作者：</font>** Aviral Joshi, Hanoz Bhathena, Max Nelson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is hard to monitor in production: exhaustive relevance labels do not exist for non-stationary multi-million-passage corpora that re-index in real time. As a result, retrieval quality is generally understudied and often deprioritised in favour of generation-oriented metrics. In this work, we propose auditing retrieval coverage by probing for evidence of missing documents rather than enumerating every relevant one. Our method Re:CAP (REtrieval Coverage Audit by iterative Probing) is a reference-free audit loop applied to a deployed RAG pipeline's initial answer and retrieved context: it identifies the topics already covered, generates probing questions for plausibly missing topics, retrieves candidate documents, and applies an LLM-as-judge to retain only those that introduce previously-unretrieved information. On four public benchmarks, Re:CAP recovers 9-29% of gold labels that flat BM25 top-500 cannot reach, rising to 48% on TREC-COVID. On MuSiQue Re:CAP beats flat hybrid top-500 by +12.9 pp on recall at less than half the document budget. An ensemble BM25, dense, and hybrid baseline (top-500 each) still leaves out 21.2% of gold docs on TREC-COVID that Re:CAP recovers; human annotators judge that 78.9% of those structurally distinct documents add new information to the baseline answer (Fleiss $\kappa$ = 0.79, n = 123), and 73.9% on live production traffic (n = 180). End-to-end recall is reproducible to within $\pm$1% across three independent runs, making Re:CAP a stable instrument for periodic retrieval audits.

---


### 262. [Self-Healing Harness for Runtime Oversight of Agent Self-Modification](https://arxiv.org/abs/2609.24130)

**<font color=#1a73e8>作者：</font>** Sina Tayebati, Divake Kumar, Nastaran Darabi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents can change their own future behavior, raising a basic control question of which self-generated changes should be allowed to persist. We formulate this as admission control for self-modification. The agent may propose changes to its operating instructions, while an external runtime gate controls persistence. We implement this principle as a model-agnostic self-healing harness that runs a Detect, Notice, Heal, Validate loop around an otherwise unmodified agent. The agent authors candidate behavioral rules in an external workspace, where they receive provisional execution authority during evaluation and acquire persistent cross-episode authority only after measured improvement on the triggering failure without regression beyond a fixed margin on protected cases. Replay provides matched evidence when available, forward trials provide a weaker fallback, and a corpus-level guard re-tests the accumulated active rule set. Across 16 matched Baseline and Harness runs spanning AppWorld, Terminal-Bench, and $\tau^2$-Bench, the gate rejected 383 replay-decided proposals. Of these, 211 (55%) improved their triggering failure while degrading a case that previously worked. This shows that locally beneficial self-modifications can introduce collateral regressions often enough to materially affect gate decisions, providing direct empirical motivation for external admission control. Task-completion score is higher under the Harness in all 16 pairs, with two paired bootstrap intervals excluding zero, while repeated-trial reliability is higher in 12 pairs, tied in 4, and lower in none. Because adaptation modifies the policy-inducing context while leaving model weights fixed, admitted changes remain inspectable, reversible, and compatible with closed-weight models.

---


### 263. [CLOOPD: Closing the Learner Loop in On-Policy Distillation](https://arxiv.org/abs/2609.24141)

**<font color=#1a73e8>作者：</font>** Keye Zheng, Hanyu Li, Zhan Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) pays twice for each fresh batch: the student generates trajectories and a stronger teacher scores them. Existing methods improve which trajectories are scored and how the teacher signal is constructed, but usually consume it with one actor update. We introduce CLOOPD, a closed-loop framework separating teacher-signal acquisition from student-side realization. CLOOPD selects an adaptive $\alpha$ waypoint inside a KL envelope, freezes the scored batch and its advantages, re-forwards the student after each actor pass, measures realization, and allocates actor work under a separate token budget. The framework includes deterministic two- and three-pass policies, token-priced CLOOPD-TPMR, and a budget-matched control. Across six 300-step runs on an 8-H20 node, every CLOOPD policy improves the one-pass TOP-D anchor at comparable teacher-token scale: macro accuracy rises from 15.41 to 17.78 with CLOOPD-Fixed2 and 19.36 with CLOOPD-Fixed3. At step 100, CLOOPD-Fixed3 reaches 15.35, nearly matching TOP-D at step 300 while using 67.2% fewer teacher-scored tokens and 28.0% fewer GPU-hours. Earlier 8-A100 ablations show adaptive $\alpha$ eliminates observed trust-envelope violations; a third pass adds headroom. These results position CLOOPD as a framework for budgeting how fully students learn from teacher-scored tokens.

---


### 264. [Luck Is Not Skill: When Do Paired Rollouts Help Group-Relative RL of LLM Agents?](https://arxiv.org/abs/2609.24144)

**<font color=#1a73e8>作者：</font>** Nazmus Sakib  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-relative reinforcement learning compares rollouts of the same prompt, but independent environment noise can obscure these comparisons. We study paired rollouts, which share an event-keyed noise schedule within each group while preserving each rollout's marginal distribution. Pairing removes the between-schedule component of reward-contrast variance, but need not reduce gradient variance. For one-sided grader noise, we derive an exact condition for reduction and give a counterexample in which reward contrasts improve while gradient variance increases. A controlled study trains a 2B tool-use agent under tool faults and grader flips, with three seeds per design. The protocol was registered with a disclosed, previously completed pilot. Under tool faults, pairing improves final noisy-test success by +5.1 percentage points on average, with all three seed differences positive, but misses the registered learning-curve criterion. The criterion is also missed under grader flips: the validation-AUC difference is +0.003 (95% interval [-0.029, +0.033]). A gradient probe on eight distinct checkpoints from two fault-trained trajectories finds lower mean-centered covariance traces under both noise types: 21 to 30% for grader flips and 40 to 63% for tool faults. These finite-sample measurements support the variance mechanism without establishing a general learning-speed benefit. The results distinguish improving reward comparisons, reducing estimator variance, and improving learning.

---


### 265. [Mind or Message? Auditing Theory of Mind in Multi-Agent Social Simulation](https://arxiv.org/abs/2609.24146)

**<font color=#1a73e8>作者：</font>** Cong Li, Cheng Chen, Thomas Fung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language model agents are increasingly used to simulate social interaction, and the resulting transcripts read as though the agents understand one another. We ask whether that appearance rests on a model of the partner's mind or on the surface record of what the partner said. We build a social simulation in which both questions have exact answers: 40 multi-issue negotiations whose hidden preference weights and whose full Pareto frontier are known by construction. Two model families negotiate across 160 dyads, every transcript is frozen before any measurement, and 2880 counterfactual probes then hold the evidence byte identical while moving one factor at a time: the reader's own stake, the partner's tone, an identity label, and the order of recursion. The agents are socially fluent and economically poor. They reach agreement in 96.2% of dyads with 0 protocol failures, yet only 0.7% of deals land on the Pareto frontier, they leave 20.5% of the available joint value unclaimed, and they miss the one issue on which their interests are perfectly aligned in 76.6% of deals; on the frontier and on that aligned issue, a package drawn at random from the set both sides would accept does as well. The probes locate the failure. Swapping only the reader's own payoff sheet, while the partner's words and offers stay identical, moves the inferred top priority by 15.0 percentage points, which is egocentric projection rather than inference, while a tone rewrite moves it by 5.3 percentage points and an identity label by 0.0. Most tellingly, an agent predicts what its partner believes about it 72.5% of the time while that partner's belief is itself correct only 51.2% of the time: the agents track the conversation far better than they track the mind behind it.

---


### 266. [Acceptance-Aware Draft Model Training for Speculative Decoding](https://arxiv.org/abs/2609.24150)

**<font color=#1a73e8>作者：</font>** Tianhua Xia, Mugilan Ganesan, Yifei Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model (LLM) inference by using a lightweight draft model to generate multiple candidate tokens that are verified by the target model in a single forward pass. Its speedup is largely determined by the acceptance length, yet existing draft-model training methods mainly optimize cross-entropy or Kullback-Leibler (KL) divergence as proxies. These objectives encourage distribution matching but do not directly optimize acceptance length, and the acceptance mechanism also differs between greedy and sampling-based decoding.
In this work, we propose acceptance-length-aware training losses that directly optimize the expected number of accepted tokens within a speculative window. For greedy verification, we derive an expected accepted length (EAL) loss that explicitly maximizes expected acceptance length. For sampling-based decoding, we introduce a window total variation (WTV) loss that optimizes the overlap between temperature-scaled draft and target distributions while accounting for sequential acceptance dependencies. Both objectives can be further combined with a group-relative reinforcement learning stage (GRPO) using simulated acceptance length as the reward.
Experiments across different target and draft models, tasks, and decoding settings show that our losses consistently improve acceptance length over KL-based training. WTV provides particularly strong gains under sampling-based decoding, while EAL better matches greedy verification. These results show that directly optimizing the acceptance objective, with losses tailored to the decoding mode, is more effective than conventional distribution-matching objectives.

---


### 267. [TAC-Time: Texts as Channels For Multimodal Time Series Forecasting](https://arxiv.org/abs/2609.24156)

**<font color=#1a73e8>作者：</font>** Jiayi Liang, Xiaotian Gu, Xinyu Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most existing time series forecasting methods rely solely on numerical observations, overlooking rich contextual information from auxiliary texts. Recent multimodal approaches attempt to incorporate textual signals, but they often treat text as static features or use large language models as forecasting backbones, limiting their ability to capture temporal dynamics and increasing computational cost. To address these challenges, we propose TAC-Time, a unified framework that transforms textual information into additional temporal channels. By modeling text features jointly with numerical sequences in a shared temporal backbone, TAC-Time preserves temporal continuity and periodic structures while remaining efficient and scalable. This formulation also enables systematic interpretability analyses. We show strong cross-modal dependencies through attention and frequency-domain analyses, and identify predictive textual signals whose correlation-aware alignment yields partial forecasting improvements. Extensive experiments on real-world multimodal benchmarks demonstrate that TAC-Time outperforms prior methods.

---


### 268. [APEXA: Execution-Integrity Enforcement for Multi-Agent LLM Automation of Synchrotron Data Reduction](https://arxiv.org/abs/2609.24165)

**<font color=#1a73e8>作者：</font>** Pawan K. Tripathi, Hemant Sharma, Andrew Chuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synchrotron data reduction, detector calibration followed by azimuthal integration of terabyte-scale diffraction series, is a multi-step, expert-bound bottleneck that increasingly limits the science rate of user facilities. LLM agents promise to collapse it, but driving a real pipeline with a stochastic model creates a failure mode chat benchmarks cannot see: an agent can report a calibration that was never computed. Correctness here is a property of what executed, not of the transcript. We present APEXA, a deployed multi-agent framework (61 tools over heterogeneous compute, run as a single reasoning loop) automating calibration and integration from natural language at a major light source. We make three contributions. First, execution-integrity enforcement: a deterministic tool-layer guard that refuses to surface any result not backed by an executed tool call, with a parser tolerant of cross-model tool-call format drift: in deployment, a frontier model fabricated a complete calibration-comparison report for commands that never ran, which the guard converts to an explicit non-result; the same code gates an optional motor-control surface at 0/200 adversarial violations against a simulated IOC, versus 15/200 for an equivalent safety prompt. Second, we release APEXA-Bench, an evaluation harness of 58 facility tasks (50 base plus an 8-task cross-detector slice) organized by a four-class physical-consequence taxonomy, the first benchmark axis we know of separating a wasted compute cycle from a damaged instrument; its cross-detector grading against NIST-traceable lattice constants surfaced two latent pipeline bugs. Large-scale agent scoring is left to a full-length study. Third, we validate APEXA on real beamline data: from one natural-language prompt it recovers detector geometry and integrates a full attenuation/exposure sweep. We release the framework, harness and traces.

---


### 269. [An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond](https://arxiv.org/abs/2609.24170)

**<font color=#1a73e8>作者：</font>** Wenbo Zhang, Kaixuan Wang, Yutao Ouyang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied AI systems are often organized into System 1 and System 2. System 1 is typically a pretrained policy that generates actions at high frequency, whereas System 2 is often instantiated as a vision-enabled language model for high-level planning. We ask whether a large language model (LLM) can act as the policy for robot manipulation without task-specific finetuning. We call this setting LLM as policy. We evaluate three LLMs on all 42 RoboDojo tasks and compare their scores with 40 public policies. Astra and GPT-5.5 use the official 50-episode-per-task protocol; DeepSeek-Flash uses 10 episodes per task. GPT-6 Astra achieves 22.48% average success rate and 28.97 Score over 2,100 trials, ranking above every public entry. Yet GPT-5.5 and DeepSeek-Flash reach only 0.88% and 1.92% average success rate with the same post-processing. We find that Astra exhibits a sharply polarized capability profile. It generalizes well to tasks that require semantic understanding but not high-precision control. In contrast, it performs poorly on tasks that require precision, dynamic control, or complex bimanual coordination. In-context experiments show no aggregate benefit from one-shot demonstrations, while selected interaction traces show within-episode corrections under perturbations. Overall, the evaluated LLMs vary substantially in manipulation performance. Astra stands out and provides initial evidence for the potential of a general-purpose manipulation model, although reliable precision and dynamic control remain limitations in the evaluated setting.

---


### 270. [LegendBench: A Diagnostic Benchmark for Legend Understanding with Counterfactual Interventions](https://arxiv.org/abs/2609.24172)

**<font color=#1a73e8>作者：</font>** Xinnuo Zhang, Zhike Tang, Jing Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Legends are fundamental to chart understanding, as reliable interpretation requires correctly binding legend entries to corresponding visual marks. While vision-language models (VLMs) are increasingly applied to chart understanding, their legend understanding is poorly diagnosed by aggregate accuracy, which can be satisfied by superficial shortcuts and confound legend-specific errors with other reasoning failures. To enable fine-grained diagnosis and controlled testing, we introduce LegendBench, a parametric benchmark and generation pipeline that produces targeted legend-centric test cases. LegendBench contributes (1) a capability-task taxonomy spanning legend parsing, legend grounding, legend-conditioned reasoning, and legend-aware abstention to localize failures, and (2) counterfactual group generation, where each base chart yields multiple variants under controlled legend interventions to probe model invariance and sensitivity. Using LegendBench, we evaluate both general-purpose VLMs and specialized chart models and generate their capability profiles, revealing persistent bottlenecks in reliable legend-to-mark binding and counterfactual consistency. We then use these capability profiles to guide targeted fine-tuning, demonstrating that bottleneck-specific interventions can effectively close the localized capability gaps and generalize to unseen data. We further leverage our counterfactual design to conduct fine-grained diagnostic experiments, analyzing encoding-channel effects, legend-order shortcuts, and abstention under varying visibility.

---


### 271. [CREDO: Variance-Guided Rubric Evolution for Replay-Corrected Credit Assignment](https://arxiv.org/abs/2609.24174)

**<font color=#1a73e8>作者：</font>** Xuchun Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon language agents receive sparse terminal feedback, while intermediate rubrics provide structured but potentially misspecified assessments of progress. In resettable training environments, counterfactual continuation rollouts can measure local credit, but exhaustive replay is costly. We propose Credo, a framework that couples evolving semantic rubrics with selective, execution-based credit correction. A frozen judge maps visible transitions to rubric features, and a credit head predicts the change in expected terminal reward associated with the realized transition. Independently sampled two-sided replays correct prediction residuals using their recorded inclusion probabilities. We derive conditional unbiasedness and a variance decomposition that connects two design choices: which rubric features to retain, and where to allocate a fixed expected replay budget. The resulting criterion weights prediction errors by policy-score sensitivity and missing replay coverage; its allocation rule additionally accounts for continuation cost. We also describe a practical mixture with terminal leave-one-out advantages and distinguish its clipped, token-normalized PPO implementation from the ideal policy-gradient estimator. This preliminary report provides the method, proofs, an exact finite-model audit, and a controlled evaluation protocol. It makes no claim of empirical superiority on language-agent benchmarks.

---


### 272. [Efficient LLM Distillation for Bangladesh Legal Context: A Smartphone-Compatible Retrieval-Augmented Generation Model](https://arxiv.org/abs/2609.24177)

**<font color=#1a73e8>作者：</font>** MD. Nafis Kamal, Mahadi Hasan Fahim, Talha Ridwan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal information in Bangladesh is inaccessible to most citizens. Statutory text is English-only, trained lawyers are concentrated in urban centres, and cloud-dependent AI fails where mobile connectivity is unreliable, a setting in which hallucinated legal text causes direct harm. The system addresses statutory interpretation only; queries that require judicial precedent or case-law reasoning fall outside its scope. We target the statutory access gap by compressing a 9-billion-parameter Gemma-2 teacher into a 2-billion-parameter student through two-phase progressive knowledge distillation. Phase 1 performs supervised fine-tuning on 9,429 quality-gated legal question-answer pairs (65% acceptance from 14,514 generated queries); Phase 2 minimises sparse Kullback-Leibler divergence against the teacher's top-50 per-token logits at temperature tau = 4.0, implemented via QLoRA (4-bit NF4, rank-32 LoRA adapters). Prior legal language models target general legal English; this system specialises in Bangladeshi statutory law. Every response is grounded through hybrid retrieval combining dense semantic search (60%) and BM25 (40%) across 36,029 statutory passages from the Bangladesh Constitution and national legislation. On a 50-query English benchmark, the distilled model reaches ROUGE-L 0.4715 and BERTScore F1 0.5679, a 103% ROUGE-L and 143% BERTScore gain over the retrieval-augmented undistilled baseline (ROUGE-L 0.2323, BERTScore 0.2340). The adapter quantises to 1.6 GB (GGUF Q4_K_M) and runs at 4-8 tokens per second on a Pixel 6 with no network access. Cross-lingual evaluation on 50 Bangla queries yields ROUGE-L 0.4083 and BERTScore 0.8133, showing effective retrieval from Bangla input against an English-only corpus. In a single-evaluator pilot, a practising lawyer rated 50 responses at a weighted mean of 4.16/5 (90% rated 4 or 5), supporting utility beyond text-overlap metrics.

---


### 273. [LIMIT: Less Is More for Instruction Tuning in Text-to-SQL](https://arxiv.org/abs/2609.24186)

**<font color=#1a73e8>作者：</font>** Haoyuan Ma, Hengwei Liu, Linjuan Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have achieved remarkable progress on Text-to-SQL through reasoning-enhanced fine-tuning, yet existing approaches predominantly rely on massive instruction corpora under the assumption that scale drives performance. We challenge this paradigm by investigating a fundamental question: what is the minimal data requirement for effective Text-to-SQL instruction tuning? We propose LIMIT(Less Is More for Instruction Tuning in Text-to-SQL), a data-centric framework that demonstrates strong database reasoning can emerge from an extremely compact training set when examples are strategically selected. LIMIT operates through four stages: difficulty-aware filtering that identifies samples within the model's learning frontier, chain-of-thought synthesis with consistency-based selection, multi-dimensional quality scoring via LLM-as-judge, and genetic algorithm optimization that jointly maximizes schema coverage and sample quality. On the BIRD and Spider benchmark, LIMIT selects only 796 and 863 samples while achieving 100% table coverage, enabling Qwen3-8B to reach 69.1% and 88.9% execution this http URL result surpasses methods trained on 20 times more data and establishes a new state-of-the-art among open-source approaches. Our findings suggest that careful data curation, rather than scale, is the key to efficient Text-to-SQL learning.

---


### 274. [Benchmarking Off-the-Shelf Multimodal AI Models Against Dermatologists on Patient-Captured Skin Images](https://arxiv.org/abs/2609.24190)

**<font color=#1a73e8>作者：</font>** Rian Dolphin, Laura Knowles  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) has advanced at a rapid pace in recent years. Initially, breakthroughs in large language models caught widespread attention. However, recent generations of frontier AI models have adopted multimodal capabilities as a first class citizen, with vision capabilities being central to that. In this paper, we evaluate three recently released models on the task of diagnosing dermatological conditions from patient-submitted images. The models chosen are at the low to mid tier in terms of pricing and thus represent a floor on current AI capabilities, not a ceiling. We evaluate AI performance relative to a panel of three certified dermatologists, who grade each image, and we present four interesting findings. Firstly, depending on the metric, the tested AI models are either on par or slightly trail humans in terms of inter-clinician agreement. Secondly, we find that asking AI models for a confidence rating produces poorly calibrated answers, meaning use of confidence thresholds should not be relied upon in a clinical setting. Thirdly, the effect of providing additional patient metadata is strongly model-specific, with one of the three models degrading on every metric considered. Finally, model cost is not predictive of performance. The best-performing model we tested costs on average $0.0045 per case.

---


### 275. [When Residualization Helps an Audit: Format Effects, Slice Gains, and Their Limits](https://arxiv.org/abs/2609.24194)

**<font color=#1a73e8>作者：</font>** Daein Weon, Dong Ho Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation scores used around LLM systems -- including reward models, rerankers, and LLM judges -- can track surface form instead of the quality they claim to measure. When presented with a terse correct solution and a commented buggy solution for the same MBPP problem, a public preference reward model selects the correct one no better than a coin flip (0.507). Subtracting the predictable surface component from such scores is increasingly common, but removal alone does not yield a more valid measurement: the removed component may carry construct-relevant signal, and residualization cannot tell which is which. Under designed interventions -- unit-test labels with comment-only edits -- residualization attenuates the reward model's format effects by about 0.12 on both correct and buggy code, while the correct-versus-buggy margins move by less than 0.01. In observational NLI and QA settings, we freeze a held-out replication before scoring and re-evaluate it using labels from disjoint annotators; this supports only a narrower conclusion: better agreement with the construct labels on a pre-declared slice where a surface-only predictor errs, not a repaired score. Full-population agreement falls in every observational setting with a reported positive slice gain, and within-question ranking falls in every such QA setting. When construct and surface features are entangled, residualization can decorrelate a score while degrading construct alignment, and, in a controlled model, configurations just as damaging to construct alignment pass every pre-adjustment check, so no committed gate is a guarantee. We assemble these distinctions into a reporting protocol whose outcomes, refusal included, state what an adjusted score may be claimed to show: an audit-time diagnostic reported beside the construct-alignment cost it incurs, never a replacement for the raw score.

---


### 276. [LoopCD: Loop-wise Contrastive Decoding for Improving Reasoning in Looped Language Models](https://arxiv.org/abs/2609.24196)

**<font color=#1a73e8>作者：</font>** Byeongho Yu, Junhyuk So, Eunhyeok Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped Language Models (LoopLMs) perform "latent reasoning" by recursively refining internal latent representations with shared weights, offering a more effective alternative to explicit verbal reasoning. Despite their effectiveness, we find that LoopLMs remain prone to loop instability: unstable refinement across iterations can produce localized uncertain "hard" tokens associated with reasoning errors. To address this, we propose LoopCD, loop-wise contrastive decoding that enhances the reasoning performance of LoopLMs by intervening on these tokens at inference time. Specifically, we exploit the internal dynamics of LoopLMs and contrast the logits from earlier iterations with logits from the last refined iteration to form the final sampling distribution. We find that this strategy is highly efficient, introducing only negligible inference overhead and requiring no additional training, while effectively improving reasoning performance by naturally refining reasoning-critical hard tokens. Extensive experiments show that our method improves the performance of recent representative LoopLMs across various reasoning tasks.

---


### 277. [H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache](https://arxiv.org/abs/2609.24197)

**<font color=#1a73e8>作者：</font>** Weifan Jiang, Krishna Teja Chitty-Venkata, Megan Flynn 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding losslessly accelerates large language model inference by having a lightweight draft model predict future tokens for verification by the target model. Recent block diffusion drafters further reduce drafting latency by predicting multiple tokens in parallel. However, existing block drafters project target hidden states at every input position into a separate drafter-side KV cache, incurring per-request memory and KV-write overhead that grow with concurrency; directly reusing target KVs in place removes this cache but fails to sustain draft quality throughout the block. We propose a hybrid target-context injection method that complements direct target KV reuse with target hidden states only at the last input position, requiring no separate drafter-side KV cache. Building on this design, we propose H-Spec, a hybrid Mamba-attention parallel drafter that consumes the two target-context sources through complementary modules. Mamba modules are initialized with projected last-token target hidden states, while attention modules reuse target KVs in place. Despite its recurrent formulation, Mamba's parallel scan allows H-Spec to preserve block-parallel drafting. Across three target models and diverse tasks, H-Spec improves over the best baseline by 5.0--13.3% in mean accepted length and 5.3--12.6% in batch-size-1 inter-token latency speedup. Under concurrent serving, H-Spec consistently achieves higher throughput while maintaining lower KV cache utilization than baselines across evaluated concurrency levels.

---


### 278. [SKstars at SHROOM: Visions Agreement-Guided Ensembling of Zero-Shot and LoRA-Adapted Vision--Language Models](https://arxiv.org/abs/2609.24198)

**<font color=#1a73e8>作者：</font>** Ali Athar, Imran Ahsan, Joon-Yong Jung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper describes the SKstars submission to SHROOM-Visions 2026, a shared task on fine-grained hallucination detection in large vision-language model outputs. The task requires systems to identify hallucinated character spans, assign hallucination categories, and provide confidence estimates for their predictions. Our approach combines zero-shot predictions from Qwen2.5-VL-72B-Instruct with those of a LoRA-adapted Qwen2.5-VL-7B-Instruct model. The outputs of the two models are integrated through a lightweight ensemble procedure, followed by span refinement and confidence adjustment. We evaluate the main system components on a small internal development subset and report the performance of the submitted system on the official English test set. SKstars achieved a Cor+Lbl score of 0.2902, ranking 15th among 29 teams, and obtained Cor and IoU scores of 0.3642 and 0.3151, respectively, ranking 18th on both metrics. The results show that combining a large zero-shot model with a smaller adapted model provides a practical framework for multilingual and fine-grained hallucination localization, while also highlighting the difficulty of transferring development-set improvements to hidden test data. Code and predictions: this https URL

---


### 279. [Forgeable Confirmation in Automated Computer Security Testing: Deterministic Rules versus AI Judges](https://arxiv.org/abs/2609.24200)

**<font color=#1a73e8>作者：</font>** Akihisha Fujiyama, Niwase Shamim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI is increasingly used to automate computer security testing, and the tools must decide for themselves whether an attack succeeded. A finding that a deterministic rule confirms by observation is reported as fact, whereas one that an LLM judges exploitable is treated as an opinion. We ask whether the system under test can forge that confirmation. In offline security testing of a four-stage AI-assisted pipeline, nine of its fifteen confirmation mechanisms are forgeable, and forgeability is predicted entirely by whether the decision reads attacker-controlled data. We formalise this as an auditable attack surface and test it prospectively: on sixteen held-out mechanisms, predictions fixed before any attack separated forgeable from unforgeable mechanisms exactly, and across 12,203 mechanisms in public scanner templates the prediction was 99.9% accurate. Deterministic rules proved cheaper to forge than eight open-weight LLM judges, failing at 2% of attacker-controlled response content against a median of 50%. No implementation of one check was both robust and precise, and routing between a rule and an AI judge raised forgery to 99%. Moving the decisive evidence to a channel the attacker cannot write cuts attack success from 97% to 0%, and an escalate verdict recovers the sensitivity this costs. The protection fails when the scanned host is itself the adversary. The results bear on AI security agents and on benchmarks that score success by string matching.

---


### 280. [Opinion Leader Dynamics: How Sparse Attention Shapes Token Clustering](https://arxiv.org/abs/2609.24202)

**<font color=#1a73e8>作者：</font>** Jingkun Liu, Yue Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention reduces the quadratic cost of global self-attention while retaining strong empirical performance, but how its restricted interactions shape the evolution of token representations remains theoretically underexplored. Modeling tokens as particles on the unit sphere, we introduce opinion leader dynamics, a framework that identifies two mechanisms through which token groups converge internally while maintaining distinct limiting directions. In the explicit model, fixed representatives induce a potential that attracts tokens toward distinct local maxima. In the implicit model, disconnected interaction groups evolve toward separate consensus directions. We formulate both models as reverse Wasserstein gradient flows and establish exponential convergence under suitable conditions. We further connect these theoretical predictions to token evolution in frontier sparse-attention LLMs that motivate our framework. Across four benchmarks, Kimi-K3, MiniMax-M3, and DeepSeek-V4-Flash consistently exhibit clearer cluster separation and higher clustering scores than the dense-attention model GLM-4.7-Flash in projected token representations. These observations support the relevance of the predicted multiple-group structure to trained frontier LLMs, while finite-particle simulations illustrate the theoretical convergence behavior. Together, our results connect restricted token interactions to distinct group-level attractors, providing a dynamical account of how sparse attention can support alignment within groups while preserving separation between them.

---


### 281. [ChartJudgeBench: Evaluating LMM Judges for Chart-to-Code Generation](https://arxiv.org/abs/2609.24210)

**<font color=#1a73e8>作者：</font>** Lijian Wu, Henry Hengyuan Zhao, Zijian Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building strong chart-to-code systems increasingly relies on reinforcement learning, whose effectiveness depends critically on the quality of the reward signal. Large Multimodal Models (LMMs) play a natural critical role in jointly assessing chart visual appearance and task requirements. They are therefore increasingly used as visual critics and reward models, yet their reliability as judges remains largely unexplored. To this end, we introduce ChartJudgeBench, a diagnostic vision-language benchmark for assessing LMM judges in chart-to-code workflows. It includes 1,003 Chart Perception Alignment (CPA) instances for pairwise chart comparison and 650 Chart Reasoning Judgment (CRJ) instances for binary Accept/Reject verification in Chart Reproduction and Chart Editing. Together, these tasks emulate the core judging decisions required in agentic refinement and RL-based chart optimization. Our evaluation of strong LMMs reveals four systematic limitations: (i) positional bias in pairwise comparison, (ii) a strong tendency to overpredict Accept, (iii) difficulty in matching visual styles and aesthetics, and (iv) an unexpected leniency bias in RL-trained models. These findings show that current LMM judges require explicit reliability validation before being used as critics or reward models in chart-to-code optimization. The code and data are available on ChartJudgeBench.

---


### 282. [From Articles to Publishers: Aggregating Language Model Predictions for News Source Reliability Inference](https://arxiv.org/abs/2609.24219)

**<font color=#1a73e8>作者：</font>** John Bianchi, Manuel Pratelli, Fabio Pinelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditionally, the reliability of news publishers is assessed by expert organisations that evaluate editorial practices, transparency and factual standards at source. When this process is translated into a computational approach, the problem is often formulated at the level of individual articles, with models being trained on a set of pre-labelled articles and their performance being evaluated in a test phase. In this work, we investigate news source reliability inference as a source-level prediction problem. We propose a two-stage framework in which transformer-based language models first estimate the reliability of individual articles and subsequently aggregate article-level predictions to infer the reliability of previously unseen publishers. To approximate realistic deployment conditions, we enforce a strict publisher-disjoint evaluation protocol, ensuring that no publisher appears in both training and test sets. Experiments on 19,476 political news articles from 439 English-language publishers labeled with NewsGuard reliability ratings show that aggregation substantially improves robustness and performance, increasing accuracy from approximately 0.60 at the article level to 0.69 at the publisher level. Finally, we analyze how prediction errors vary across political orientations, revealing statistically significant associations between political leaning and misclassification patterns. Overall, our findings show that publisher reliability can be inferred from aggregated textual signals alone, supporting scalable and content-based approaches to automated news source assessment.

---


### 283. [Document Retrieval-Aware Chunking (D-RAC): Universal Retrieval-Aware Ingestion of Enterprise Documents via PDF Normalization and Multimodal Markdown Conversion](https://arxiv.org/abs/2609.24220)

**<font color=#1a73e8>作者：</font>** Uday Allu, Abhivanth Sivaprakash, Pratik Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems over enterprise knowledge bases must ingest heterogeneous document formats -- PDFs, Word documents, presentations, and scans -- whose content is locked inside complex visual layouts, multi-column pages, and dense tables. Rule-based extraction and OCR destroy reading order, flatten tables, and lose heading hierarchy, while fully agentic chunking over extracted text incurs high token costs and hallucination risk. We present Document Retrieval-Aware Chunking (D-RAC), an extension of our Web Retrieval-Aware Chunking (W-RAC) framework to arbitrary document formats. D-RAC first normalizes any input document into PDF, exploiting the fact that virtually every format has a faithful, deterministic PDF rendering. A single multimodal LLM pass then converts rendered pages into retrieval-optimized Markdown -- rewriting tables as self-contained prose statements and preserving heading hierarchy -- after which chunking proceeds exactly as in W-RAC: deterministic parsing into ID-addressable units followed by lightweight LLM-based chunk planning over identifiers rather than text. Source text is never regenerated during chunking, preserving W-RAC's cost, determinism, and observability benefits while unlocking every renderable format as a first-class input. On the 236-document, 795-page PDF subset of the RAG-Multi-Corpus benchmark spanning five enterprise domains, D-RAC converts and chunks the entire corpus in 72 minutes with zero errors, producing 1,748 retrieval-ready chunks. Compared to agentic chunking with frontier LLMs, D-RAC reduces chunking-stage output tokens by 95.7%, cutting chunking cost by 77.8% (GPT-4.1 pricing) to 85.6% (Gemini 2.5 Pro pricing) and chunking time by 75%. D-RAC scales linearly to documents of 500+ pages.

---


### 284. [The Work Behind Delegation: A Framework for Supervising AI Coding Agents](https://arxiv.org/abs/2609.24234)

**<font color=#1a73e8>作者：</font>** Yeon Su Park, Nadia Arvi, Hae Ri Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI coding agents carry out development tasks with greater autonomy, developers are shifting from direct implementation toward supervising delegated work. Yet existing research offers limited understanding of how developers organize supervisory activities into connected workflows. Drawing on observations and workflow diagrams from 19 experienced developers, we reconfigure Sheridan's framework of human supervisory control into seven stages and the connecting loops for supervising AI coding agents. We applied the framework to public developer discussions on Reddit and found that supervisory demands extend across stages and that developers manage them by concentrating effort in planning, delegating supervisory work to other agents, and turning recurring guidance into reusable assets. Our framework provides a useful analytical lens for understanding how developers supervise AI coding agents by capturing how supervision is structured in agentic software development.

---


### 285. [Memory vs. Context? Influential Factors of Factual Recall in Language Models](https://arxiv.org/abs/2609.24238)

**<font color=#1a73e8>作者：</font>** Guilhem Fouilhé, Nicholas Asher, Philippe Muller  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We reproduce and stress-test the work of Yu et al. (2023), who characterize how language models (LMs) arbitrate between memorized knowledge and contradictory in-context statements. We replicate their world-capitals experiments on 31 models spanning Pythia, GPT-2, Qwen3, and Ministral families, including base and post-trained variants, and extend evaluations to five additional knowledge relation types from the ParaConflict dataset. We empirically confirm most of their original findings: larger models and higher-frequency entities tend to favor memorized answers, with substantial family-level variance. However, several conclusions do not generalize cleanly: entity-frequency effects disappear on Qwen3-14B and 32B; post-training shifts the memory-context trade-off inconsistently across families; question phrasing alone can change a model's reliance on memorized knowledge by up to 80 percentage points; and semantically unrelated prose can mimic coherent supporting context. Our results clarify where Yu et al.'s claims hold and to what extent they generalize to other prompts.

---


### 286. [Taming CoT Obfuscation in VLMs: From Mechanistic Evidence to Activation Enforcement](https://arxiv.org/abs/2609.24243)

**<font color=#1a73e8>作者：</font>** Xutao Mao, Jianing Zhu, Jinman Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) improves reasoning in vision-language models (VLMs) but can induce chain-of-thought (CoT) obfuscation: an operational, non-intentional outcome where task reward or accuracy rises while traces become less grounded and monitorable. Prior work largely documents this decay behaviorally, leaving its representation-level correlates and actionable controls unclear. We find that template- and ground-associated activations become less separable during RL; matched interventions support the contribution of selected features to monitorability degradation. Guided by this evidence, we propose Targeted Anti-obfuscation with Mechanistic Enforcement (TAME), which uses Sparse Autoencoders (SAEs) to combine behavioral feedback with targeted suppression of template-associated activations during RL. Its asymmetric constraint penalizes template activations only above their pre-RL baseline, anchoring the localized features while behavioral feedback promotes grounded refinements. Across VIRL-39k, SPA-VL, and two model families, TAME improves CoT monitorability by up to 30.9 and 16.7 percentage points over Group Relative Policy Optimization (GRPO), respectively. Blinded human evaluation finds higher human monitorability on both datasets, and two held-out monitor families reproduce the monitorability gains. Task accuracy changes are small and mixed, and general-capability benchmarks show task-specific trade-offs. These results provide a path from behavioral monitoring to representation-level oversight for more auditable RL-trained multimodal systems.

---


### 287. [Look Where It Counts: A Free, Label-Free Visual Evidence Signal for Fine-Grained Vision-Language Reasoning](https://arxiv.org/abs/2609.24244)

**<font color=#1a73e8>作者：</font>** Santi Ram Tiwari, Nihal Naik, Devbrat Pandey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) fail at fine-grained visual questions less because they cannot reason than because they never see the evidence: high-resolution images are downsampled before encoding, so the model answers from linguistic priors. The standard remedies are expensive: annotated answers (SFT), hand-engineered verifiers (RLVR), or a large external teacher (on-policy distillation). We ask whether the visual evidence itself can supply the signal for free. We formalize the contrastive evidence gap, the per-token log-likelihood ratio that a model assigns to its own output when conditioned on a question-relevant region versus an irrelevant one, and study it across Qwen2.5-VL-7B, Qwen3-VL-8B, and Qwen3-VL-30B-A3B on V*Bench. Our main positive result is training-free: selecting the candidate crop under which the model's answer distribution is most peaked, using a single-view, label-free criterion, discovers the answer-bearing region with no bounding boxes, training, or labels. It localizes the target 4.4 to 5.1 times better than chance and raises fine-grained accuracy from 70 percent to 85 percent at inference. We further show that the gap is complementary to the model's own confidence. Combining them predicts correctness better than either alone, with AUC up to 0.99, and flags confidently wrong answers, with AUC ranging from 0.97 to 1.00 within the high-confidence subset. All effects concentrate on perception-bottleneck questions and vanish on a global-context control. Finally, we report an honest negative result: converting the same signal into a training method, gated self-distillation (SEG-Distill), does not outperform the base model at pilot scale across three gate designs, while more aggressive gating degrades accuracy. The signal is real, but converting it into training gains remains an open problem.

---


### 288. [Taramandal-GPT: Enhancing Astrodynamics Problem-Solving with Knowledge Retrieval and Structured Thinking](https://arxiv.org/abs/2609.24246)

**<font color=#1a73e8>作者：</font>** Akhil Sharma, Jatin Gupta, Ali Imam Abidi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown remarkable progress in natural language understanding, yet their effectiveness in specialized fields like astronomy and astrodynamics remains limited due to challenges in multi-step reasoning, symbolic manipulation, and domain-specific terminology. To address this, we present Taramandal-GPT (Constellation-GPT), a domain-adapted framework built on the Qwen3-8b backbone, enhanced with a Retrieval-Augmented Generation (RAG) pipeline and a fallback mechanism for improved contextual precision. We evaluate it on the Astrodynamics Problems Benchmark (APBench), a dataset of 299 questions covering foundational to advanced levels of space science. Using a dual evaluation method - numeric margin-based scoring and semantic similarity assessment - Taramandal-GPT achieves competitive performance against state-of-the-art open- and closed-source models, with notable strength in thinking-intensive tasks. These results highlight the value of specialized LLMs for domains demanding accuracy and interpretability, positioning Taramandal-GPT as a step toward reliable Artificial Intelligence (AI) assistants for astrophysics, spacecraft engineering, and space exploration.

---


### 289. [MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents](https://arxiv.org/abs/2609.24259)

**<font color=#1a73e8>作者：</font>** Ruike Cao, Fanyu Zhao, Fugen Yao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response. Yet this capability has remained largely overlooked. To assess this capability, we introduce MemCalib, a benchmark grounded in realistic memory-system scenarios for evaluating memory use and advancing optimization algorithms. Results on the MemCalib test set reveal that frontier open- and closed-source models struggle to use memory appropriately. They frequently over-use or under-use memory rather than matching each proposition's actual use to its target level, leading to biased, low-quality responses. Experiments with common post-training algorithms, including group relative policy optimization and on-policy self-distillation, further reveal a clear directional skew: trained models improve in one direction while deteriorating in the other. We therefore propose MemCalib-RL, an ordered bidirectional counterfactual credit-assignment algorithm that separates over- and under-use signals and localizes their credit to response tokens through exact atom ablation. Results across model families and scales (Qwen3-8B, Ministral-3-8B-Instruct, and Qwen3.5-35B-A3B) show that MemCalib-RL achieves the best overall performance while better balancing over-use and under-use, with gains generalizing beyond MemCalib in external benchmark evaluation. Further experiments support its design choices and robustness and provide insight into its training dynamics.

---


### 290. [Canonical Procedural Actions: An Auditable Annotation Protocol for Tool-Use Agent Traces](https://arxiv.org/abs/2609.24264)

**<font color=#1a73e8>作者：</font>** Songqi Li, Dongqing Li, Zheqiao Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-use agent traces identify messages and API calls, but procedural analyses also need explicit units of action and inspectable links to their evidence. We present Canonical Procedural Actions (CPAs), an annotation protocol that records a procedural function, its first agent-event anchor, the agent events that realize it, and separate contextual evidence. Multiple actions may share a message anchor without an inferred within-message order. A retail case study produces a versioned 24-entry codebook through open induction, recorded consolidation, and successive application audits. Two isolated LLM contexts annotate 32 trajectories disjoint from development at the trajectory level, producing 499 and 491 occurrences with anchor-label overlap A=0.982. Requiring identical context-event references reduces overlap to 0.798. These are structural repeatability measures, not semantic accuracy: 16 of 26 task IDs also occur in development, and historical tool payloads were truncated to 110 characters. Retrospective controls show that collapsing all labels raises overlap to 0.986, while simple endpoint rules reproduce the tool-anchored portion with 0.997 overlap. Assistant-message actions have 0.971 overlap, with a per-label minimum of 0.816. Applying the frozen codebook to 244 further trajectories yields 4,058 records, including eight diagnostic outcomes. The contribution is an explicit, auditable annotation instrument and a case study of its construction and measurement limits; human-reference validity and downstream utility remain to be established.

---


### 291. [Hierarchical Prompt Learning for Hyperbolic Vision-Language Models](https://arxiv.org/abs/2609.24276)

**<font color=#1a73e8>作者：</font>** Andro Erdelez, Pascal Mettes, Behzad Bozorgtabar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperbolic vision-language models (VLMs) represent image and text features in a geometry naturally suited to hierarchy, but their adaptation to downstream tasks has largely relied on fixed prompts. Existing prompt learning methods, meanwhile, treat class labels as a flat set and do not exploit available taxonomic structure. We address this gap with a hierarchical prompt learning plug-in for frozen hyperbolic VLMs. Given a fixed offline parent-class hierarchy, it augments a class prompt learner with a separate parent prompt learner, parent-level supervision, hyperbolic entailment regularization, and parent-feedback logit fusion. We instantiate the method with CoOp, CoCoOp and MaPLe, yielding HyPLO, CoHyPLO and MaHyPLO. Across the standard 11-dataset benchmark, all variants improve base-to-new generalization and cross-dataset transfer, and remain comparable to their prompt learning baselines under domain shift. Six hierarchical metrics and embedding analyses show that the method produces more taxonomically consistent predictions and induces a hierarchy-consistent organization of parent, class, and image embeddings in hyperbolic space. Its gains are largest when novel classes must be placed within a fixed taxonomy, and smallest for fine-grained confusions among sibling classes or shifts affecting only the image distribution.

---


### 292. [How Many Pixels Is a Digit Worth? Place-Aware Coordinate Entropy for GUI Agent Confidence Estimation](https://arxiv.org/abs/2609.24277)

**<font color=#1a73e8>作者：</font>** Yunxiang Li, Xixin Wu, Helen Meng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI agents predict click coordinates as digit-token sequences, but standard text-LLM confidence estimation methods rank correct clicks from wrong ones only weakly. GUI-specific alternatives use K samples or new supervision, but still leave room for improvement. We trace part of this to place-value asymmetry: bounding-box correctness often makes higher-place digits more important than lower-place digits, so uniform aggregation weakens the signal that determines correctness. The fix is to weight each digit's Shannon entropy by its place value. We call this Place-Aware Coordinate Entropy (PACE). Across fixed-scale agents on ScreenSpot-Pro and ScreenSpot-v2, PACE wins both AUROC and selective accuracy on all primary comparisons in a single forward pass, matching or outperforming K-sample baselines at a fraction of the cost. PACE provides a per-click confidence estimate that turns coordinate-token internals into a practical confidence signal for GUI agent deployment.

---


### 293. [TTSE: A Two-Track Online Self-Evolution Framework](https://arxiv.org/abs/2609.24289)

**<font color=#1a73e8>作者：</font>** Ruimin Pei, Yongkang Wu, Shangyi Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Large Language Model (LLM) agents are applied in continuously interactive environments, driving the evolution of their own capabilities becomes a core problem for achieving long-term autonomy. Currently, environmental knowledge is typically treated as an external fixed input rather than as part of the agent's ongoing evolution. Reinforcement learning methods usually optimize policies through environmental interaction but tend to adapt only to fixed task distributions or single environments. This paper proposes TTSE (Two-Track Self-Evolution), a dual-track online self-evolution framework that separates evolving knowledge into FACT (environmental facts, whose reliability is continuously verified through interaction evidence) and TIP (task-conditioned implementation procedures). From a decision-theoretic perspective, we decompose the agent's excess risk into environment-representation regret and conditional-execution regret, characterize the conditions under which environment-conditioned policies strictly outperform condition-agnostic policies, and bound the downstream risk in terms of FACT identification error and cross-condition mismatch cost. In practice, TTSE's ablation experiments on GDPevo validate the advantage of dual-track evolution. On the classic agent task benchmarks ALFWorld and ScienceWorld, TTSE further demonstrates superior task adaptation. Moreover, TTSE is broadly compatible with existing skill self-evolution methods; combined with the Bayesian-Agent algorithm, a single-track ablation validates the dual-track advantage, substantially improving the aggregate score across the five major domains of SOPBench over three independent repetitions. Finally, on the real end-to-end task benchmark PinchBench, TTSE is integrated into a general agent framework via retrieval-based injection and stably outperforms the baseline across three independent runs.

---


### 294. [When and How Should an Agent Clarify? CIGAsk: Teaching LLMs to Clarify via Counterfactual Information Gain](https://arxiv.org/abs/2609.24290)

**<font color=#1a73e8>作者：</font>** Yunxiang Li, Xixin Wu, Helen Meng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned LLMs faced with underspecified queries often commit to a single interpretation rather than ask for clarification, producing confidently wrong answers. In our experiments, prompting alone is insufficient: models either ask for clarification on every query or ask vague questions that fail to recover the missing information. Addressing this failure requires learning two coupled skills: when to ask rather than answer and how to ask a question that recovers the disambiguating information. Existing recipes either address only one of these skills or require a separately trained critic. We propose CIGAsk, an RL recipe that teaches both skills through two complementary reward signals within a multi-turn GRPO loop. Counterfactual Information Gain (CIG) compares the gold-answer log-likelihood under a frozen reference model with and without the user response, providing per-turn credit that guides how to ask. The Asymmetric Ambiguity Bonus assigns a signed reward at the terminal token based on the gold ambiguity label, guiding when to ask. Across three clarification benchmarks spanning table, passage, and open-domain QA, CIGAsk-7B outperforms the strongest external baseline despite using a smaller backbone. It also transfers across datasets without per-dataset tuning while preserving single-turn QA performance on out-of-distribution benchmarks.

---


### 295. [KV-COBRA: KV Cache Compression via Co-Optimized Bit-Rank Allocation](https://arxiv.org/abs/2609.24298)

**<font color=#1a73e8>作者：</font>** Sihyeon Ha, Jaeho Lee, Yo-Seb Jeon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What limits KV-cache compression at extreme bit-rates? We argue that it is not the choice of compression scheme, but how its budget is allocated across attention heads. Existing methods apply rank and bit-width uniformly, ignoring that each head has a different optimal mix of rank truncation and quantization. We show that co-optimizing rank and bit-width per head, using only standard low-rank projection and scalar quantization, dominates uniform allocation, with the largest gains at low bit-rates. Our method, KV-COBRA (Co-Optimized Bit-Rank Allocation), formalizes this as a resource-allocation problem: it balances rank-truncation loss against quantization loss within each head, then redistributes budget across heads to minimize total distortion. A fused Hadamard rotation equalizes per-channel variance, and reordering the SVD basis by attention-KL importance makes the solver query-aware. The same allocator extends to joint $K{+}V$ compression. On perplexity, zero-shot, and long-context benchmarks from $0.5$ to $4$ bits per dimension (bpd), KV-COBRA shows the smallest accuracy degradation among evaluated methods at low bpd, with no per-token overhead.

---


### 296. [SupportCal: Label-Free Calibration of Post-Trained LLMs via Reference Support and Corroboration](https://arxiv.org/abs/2609.24303)

**<font color=#1a73e8>作者：</font>** Linhan Luo, Lequan Lin, Dai Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training often improves task performance but can degrade confidence calibration, leaving post-trained language models (PoLMs) more overconfident than their corresponding pretrained language models (PLMs). Because task-specific labeled calibration data can be costly or unavailable, the corresponding pretrained PLM provides a natural label-free reference for post-hoc calibration. Prior agreement-gated PLM-referenced calibration fits a scalar temperature using only examples on which the PoLM and its PLM reference agree, excluding disagreement examples because direct alignment can drive the fitted temperature excessively high and induce under-confidence. We revisit this binary treatment. A controlled reintroduction diagnostic reveals a non-monotonic aggregate effect: admitting a moderate fraction of disagreement examples can improve calibration, whereas the benefit diminishes as unit-weight inclusion approaches the full disagreement set. We introduce SupportCal, a label-free post-hoc method that retains agreement examples at unit weight and assigns disagreement examples continuous weights based on the own-base PLM's relative support and corroboration from pretrained references selected from a size-compatible candidate pool. We further characterize when the resulting weighted objective admits a finite optimal temperature. Across MedMCQA and MathQA, SupportCal yields lower ECE than the agreement-only baseline for nearly all evaluated target-model configurations; supplementary TweetEval Sentiment results show the same pattern on a fixed-label classification task.

---


### 297. [A Distributional Optimisation Perspective on Combining Models in Deep Learning](https://arxiv.org/abs/2609.24328)

**<font color=#1a73e8>作者：</font>** Congye Wang, Yan Lin, Zheyang Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Combining predictions from different models can improve performance at machine learning tasks, but the training of the individual models and the rule used to combine them are typically chosen separately, and by ad hoc means. Recent advances in distributional optimisation (i.e. where the optimisation occurs over the set of probability distributions) offer an opportunity for principled joint training, viewing the collection of models as a discrete distribution whose support points are to be optimised, but the potential of these methods is not well-understood. In this paper we (1) cast two standard combination strategies - ensembles and low-rank adapter averaging - as entropy-regularised distributional optimisation, observing that the resulting objective is convex in the ensemble case but not in the adapter-averaging case, so that existing convergence guarantees for mean field Langevin dynamics transfer only to the former; (2) assess existing and novel algorithms for this task, including a functional variant of variational gradient descent; and (3) report an empirical study spanning synthetic classification tasks and fine-tuning of large language models on a commonsense reasoning benchmark.

---


### 298. [LADDER: Graph-Guided Diffusion Language Models for Efficient Multi-Hop Reasoning](https://arxiv.org/abs/2609.24346)

**<font color=#1a73e8>作者：</font>** Senlei Zhang, Linhao Luo, Qian-Wen Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph Retrieval-Augmented Generation (GraphRAG) has remarkably enhanced large language models on complex reasoning by leveraging structured entity topologies. However, existing frameworks heavily rely on standard autoregressive language models where the nature of inherent sequential generation severely hinders overall inference efficiency. Inspired by Diffusion Language Models (DLMs) that offer massive parallelism via continuous refine-in-parallel decoding, we aim to accelerate GraphRAG in the discrete space. However, it remains non-trivial for two challenges. First, partially denoised drafts are highly dynamic and uncertain, making dynamic graph grounding non-trivial. Second, raw denoising states are inherently noisy and unstable, making synchronous graph retrieval and multi-hop aggregation computationally prohibitive. To this end, we present LADDER, a novel framework that bridges diffusion language modeling with GraphRAG through graph-guided parallel decoding. Specifically, (i) we propose an event-driven self-clocking retrieval, inspired by our key insight that 88% of target entities emerge early in the partially denoised state, leading final commitment by an average of 5.7-9.6 steps. This mechanism dynamically triggers graph retrieval only when the set of graph-linkable entities expands, yielding an asynchronous self-clocking policy that bypasses learned gates or heuristic thresholds. (ii) An incomplete-query graph propagation module is designed to process the newly emerging entity queries using a specialized graph foundation model, continuously aggregating multi-hop evidence to sharpen parallel predictions and accelerate overall decoding convergence. Extensive experiments on three challenging multi-hop QA benchmarks show that LADDER raises average exact match from 39.6% to 45.2% while achieving a 4.1x latency reduction.

---


### 299. [Few-Shot Demonstrations Elicit the Use of In-Context World Representations in LLMs](https://arxiv.org/abs/2609.24352)

**<font color=#1a73e8>作者：</font>** Kohsei Matsutani, Gouki Minegishi, Core Francisco Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs), when acting as agents, are expected to take observed data in context, infer the latent state space underlying the world, and leverage it for downstream prediction. However, prior work demonstrated that LLMs struggle to use representations learned in context on a graph tracking task, where the model needs to construct a representation of the graph governing data generation process and use it for subsequent predictions. In this paper, we show that extending this to few-shot settings, where each demonstration is generated from a different world with either the same or different graph topologies, enhances its prediction on 6 models from 4 model families. To understand this improvement, we linearly probe a low-dimensional world representation that encodes graph information in the hidden states. Notably, we find that few-shot demonstrations relocate the world representation and increase its predictive use. Specifically, for each model, these world representations shift in directions nearly orthogonal to their original subspace, and interventions on these representations selectively impair performance more than interventions on other subspaces. Consistent with this insight, we show that few-shot demonstrations with observations from different worlds improve performance on ARC-AGI-1&2, web agent tasks, and Othello. Our findings elucidate the role and internal mechanisms of few-shot demonstrations in in-context world modeling. More broadly, our work advances our understanding of how LLM agents learn from in-context observations and provides implications for their further improvement.

---


### 300. [Mitigating Entity Type Confusion in Cross-Domain NER via Multidimensional Quantification and Reasoning Enhancement](https://arxiv.org/abs/2609.24357)

**<font color=#1a73e8>作者：</font>** Jingyu Wang, Shijie Wu, Fusheng Jin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-domain Named Entity Recognition (CD-NER) aims to transfer the rich knowledge in the source domain to the target domain. Recent studies adopting decomposition or generation paradigms have achieved significant performance improvements, demonstrating high accuracy in entity span detection. However, during entity type classification, models severely suffer from entity type confusion, the erroneous tendency that models classify entities of one type in the text as another similar but incorrect type. To address this issue, we first propose a Multidimensional Confusion Quantification Model (MCQM) that quantifies a model's confusion extent between entity types from three dimensions: source-target hierarchy analysis, semantic similarity analysis, and explicit data evaluation. Moreover, we propose the Progressive Bidirectional Reasoning Chain (PBRC). PBRC leverages the source-target hierarchy and confusion analysis from the MCQM to prompt the LLM to generate two-stage reasoning information. The two-stage reasoning information is utilized to augment the knowledge of the model, significantly mitigating entity type confusion and improving the model's generalization performance. Experimental results demonstrate that our method achieves new state-of-the-art results on all domains of the CrossNER dataset.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-379](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
