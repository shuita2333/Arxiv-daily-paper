# 🧠 大模型相关研究 | 2026年08月13日

> 本类共 **184** 篇论文：已确认 **177** 篇，待复核 **7** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-184](./part-04.md)

---

### 51. [Logit-Boundary Geometric Belief Interfaces and Sparse Sheaf-Enclave Protocols: A Self-Contained Substrate for Secure Network Electronic Health Record (EHR) Interoperability](https://arxiv.org/abs/2608.10300)

**<font color=#1a73e8>作者：</font>** Alvin Spivey, Thomas Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electronic health-record interoperability is a boundary problem: legacy systems, generative models, terminology services, identity systems, and human reviewers may each expose rich internal states, while operational exchange requires a narrow shared interface of typed claims, bounded uncertainty, provenance, and explicit admission or abstention. This paper details a mathematical and engineering architecture for that interface. The organizing idea is the logit boundary: a discovery model may propose pre-threshold scores over a local categorical decision, but a deterministic judgment substrate decides whether the proposal is admissible, requires review, or must be quarantined before any Fast Healthcare Interoperability Resources (FHIR) transaction is constructed. The resulting Geometric Belief Interface (GBI) combines finite boundary semantics, local Dirichlet evidence, cellular-sheaf and mapping-cone diagnostics, advisory geometric audit charts, and a Decentralized Cryptographic Sheaf-Enclave (DCSE) protocol sketch for fail-closed deployment. The framework does not establish clinical truth, global representation alignment, or end-to-end safety; it defines certificate-producing checks at a model-to-system boundary. A companion frozen synthetic benchmark, GBI BoundaryBench v0.1, evaluated Qwen3-4B-Instruct-2507 on 256 held-out tasks across three evidence modes (768 canonical executions). All executions completed, but none produced an output accepted by the benchmark contract: 369 were rejected during safe parsing and 399 during schema validation, yielding zero coverage and deterministic quarantine. This empirical result is deliberately narrow - one 4B open-weight model under one frozen interface - and is reported as evidence about the admission boundary, not as a general claim about LLM capability or clinical safety. A Julia appendix verifies numerical certificates using standard libraries.

---


### 52. [Is This Your Final Answer? Cross-Contextual Consistency as a Measure of LLM Credibility](https://arxiv.org/abs/2608.10315)

**<font color=#1a73e8>作者：</font>** Siyang Wu, Yibo Jiang, Bryon Aragam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are powerful black-box systems, making it difficult to discern whether their answers reflect stable internal beliefs or superficial pattern matching. We identify cross-contextual consistency as an underutilized behavioral property of LLMs: a credible answer should remain stable when the same task is placed under topic-aligned, content-neutral contextual variation. Building on this intuition, we operationalize Cross-Contextual Consistency (C3) by comparing model generations under original and perturbed prompts. Across 26 models and six benchmarks spanning reasoning, factuality, and code generation, we find that answers with smaller cross-contextual shifts are more likely to be correct or factual. We demonstrate that C3 provides a complementary axis of evaluation and can serve as a benchmark usefulness diagnostic, identifying which portions of a benchmark remain informative even when aggregated scores are widely considered "saturate".

---


### 53. [From Detection to Understanding: TAR and TAR-Bench for Multi-Task Traffic Anomaly Reasoning](https://arxiv.org/abs/2608.10317)

**<font color=#1a73e8>作者：</font>** Han Zhang, Yilin Zhao, Zaid Pervaiz Bhat 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present TAR (Traffic Anomaly Reasoning) and TAR-Bench datasets, resources for training and evaluating video-language models beyond anomaly detection. TAR contains 44,040 chain-of-thought training annotations across 10 tasks for 3,670 CCTV videos ($\sim$26 hours) from eight public datasets. Its evaluation component, TAR-Bench, contains 960 human-curated test annotations for 80 held-out clips trimmed from 17 public YouTube videos. TAR's training annotations are produced with MAVEN, which consolidates multi-scale video evidence into structured event descriptions before generating question-answer pairs and reasoning traces. On TAR-Bench, eleven vision-language models reveal that strong question-answering accuracy does not reliably predict temporal or scene reasoning ability. Multi-task fine-tuning on TAR yields consistent gains, with the full 10-task model improving aggregate score by 21.4 points over its zero-shot baseline. TAR and TAR-Bench provide the official training and in-domain evaluation data for AI City Challenge 2026 Track 3. The dataset is available at this https URL

---


### 54. [Toward a Theory of Value in AI Alignment](https://arxiv.org/abs/2608.10327)

**<font color=#1a73e8>作者：</font>** Andrew Smart, Shazeda Ahmed, Jackie Kay 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can AI systems be aligned to human values? The popularization of large language models (LLMs) and multi-modal foundation models has seen a rise in harms spanning from toxic speech and hallucinations to AI agents executing unauthorized actions. Within the field of AI safety, these harmful instances are often framed as the alignment problem, or of models being misaligned with human values. Researchers have responded by pursuing applied and theoretical AI value alignment efforts, often without specifying what they mean by human values. How does the field of AI value alignment conceive of human values? How are these conceptions of values technically operationalized and evaluated? What does the emergent theory of value from this field signify for the future of AI? We annotated 94 value alignment research papers to discern their implicit theory of values in AI. The majority do not define values, relying heavily on preferences as a stand in that runs the risk of reducing complex culturally situated concepts down to binary choices. As researchers dispense with using human annotators for model training and evaluation, turning instead to synthetic data and autorater approaches to aligning and evaluating models, we identify the potential to close off alternative methods for contesting and enacting values in foundation models. In making AI value alignments philosophical commitments explicit, we seek to bring great specificity and under explored perspectives in the debate on whether and how AI can address human values.

---


### 55. [Hierarchical Compositionality for An Assistive AI Agent](https://arxiv.org/abs/2608.10330)

**<font color=#1a73e8>作者：</font>** Tianyi Fu, Mohan Sridharan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly being developed to assist humans in various applications, and Large Language Models and other deep network architectures are considered to be state of the art for such agents. These methods are impressive stochastic predictors, but they are resource-hungry, opaque, and known to make arbitrary decisions in novel situations due to the narrow set of underlying representation and processing choices. Our work seeks to explore the design of architectures for such AI agents based on core principles that can be traced back to the early pioneers of AI but are not fully utilized in modern AI methods. We do so in this paper in the context of the core problem of AI agents addressing ambiguity in the objects being referred to by the human participants. Humans address such ambiguity by heuristically leveraging compositional knowledge of domain context and the preferences of the other human participants. Drawing inspiration from this observation, we describe an architecture that embeds the principle of hierarchical compositionality and uses simple heuristics to achieve the desired disambiguation. Specifically, domain objects are represented in terms of primitive attributes drawn from human-validated semantic feature norms, and a hierarchical combination of attributes and concepts automatically identified from a limited observed history of interactions of an assistive agent with specific users. The assistive agent then achieves the desired disambiguation by reasoning with knowledge of this compositional hierarchy; axioms governing domain dynamics; and models of semantic compatibility, session salience, and user-specific thematic preference, requesting human clarification when necessary. Experiments show that our approach consistently outperforms state of the art data-driven baselines, supporting adaptation to specific user profiles.

---


### 56. [MERA: Model Evolution and Routing with Skill Adaptation for Agentic Systems at Scale](https://arxiv.org/abs/2608.10333)

**<font color=#1a73e8>作者：</font>** Yuhang Yao, Zeyu Wang, Wanyi Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents execute heterogeneous sequences of model calls within a single task: some invocations require careful reasoning, while others are structured steps such as formatting or tool-argument construction. Prior routing methods exploit this asymmetry by assigning easy invocations to a cheaper small model and difficult ones to a large model. Such policies reduce inference cost, but they leave the small model's capability unchanged, so attainable savings remain bounded by the work the student can already solve. MERA instead improves the small model itself, using a single model invocation as the unit of adaptation. In each cycle, MERA replays failed student invocations to obtain execution-verified teacher demonstrations, distills recurring procedures into an iteratively updated SkillBook, and fine-tunes a student LoRA adapter via supervised learning and optional GRPO. Routing serves as supporting machinery for deployment: the improved student is served behind a cost-calibrated router with verifier-backed fallback, and a candidate SkillBook, adapter, or router is admitted only when joint replay preserves task quality. Empirically, four-cycle adaptation raises Qwen2.5-Coder-1.5B from 28.7% to 49.7% pass on held-out HumanEval+MBPP. Under verifier-backed fallback, the deployed policy retains 88.3% pass at 60.8% of always-Luna cost. On TAU-2, a fine-tuned Qwen3.5-2B improves from 14/35 to 18/35 and matches an unadapted 4B model. These results indicate that verifier-backed multi-cycle adaptation can increase small-model capability, rather than only routing around a fixed student.

---


### 57. [Narrative Keyframing for Generative Creative Writing](https://arxiv.org/abs/2608.10337)

**<font color=#1a73e8>作者：</font>** Chao Zhang, Abe Davis  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce narrative keyframing, an interaction technique for AI-assisted creative writing that lets writers specify different types of narrative constraints at selected moments in a story, then use AI to generate intervening prose. Inspired by the use of keyframing in animation, narrative keyframing offers a flexible way to connect story planning with adaptive control over generated text. We explore three types of keyframes: plot keyframes define significant events in a story, character keyframes represent how individual characters change over the narrative, and perspective keyframes capture how individual characters experience different events through first-person narratives. Plot and character keyframes offer a flexible way to adapt the type of high-level conditioning explored in previous AI writing tools to more customizable, iterative, and fine-scale control, while perspective keyframes add a new way to control characterization and focalization by using first-person narratives as an intermediary. Through a user study, we show that narrative keyframing supports a more controllable, transparent, and engaging way to use generative AI in creative writing.

---


### 58. [Efficient Reinforcement Learning for Long-Horizon Tool-Use Agentic Tasks](https://arxiv.org/abs/2608.10357)

**<font color=#1a73e8>作者：</font>** Zelei Cheng, Amritansh Mishra, Sambit Sahu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon tool-using agents must reason over user goals, domain policies, tool calls, simulator state, and delayed verifiable rewards. Reinforcement learning (RL) is a natural fit for this setting, but multi-turn on-policy rollouts create long contexts, while model-specific attention layers may require custom masks and learned sink normalization. We present SINKFLEX-RL, a modular training system for RL in dual-control tool-use environments. The system combines a Gymnasium-compatible environment wrapper, a VERL-style rollout dataflow, group-relative policy optimization without a separate value model, and a sink-aware FlexAttention path designed to preserve model-specific sink scaling under causal and sliding-window masks. In a preliminary Tau2Bench retail run, validation reward (mean@1) rises from 0.25 early in training to $0.44$ later in the observed training window, while training-score and trajectory-reward proxies also trend upward. In a fixed-configuration memory benchmark, the optimized attention path reduces peak VRAM from 28.06GB to 22.52GB at 4096 tokens, a $19.7\%$ reduction, and runs the measured 8192-token configuration using $25.53$~GB where the eager baseline runs out of memory. These results illustrate the value of integrating environment interfaces, RL dataflow, and attention-kernel design for memory-feasible long-horizon agent training.

---


### 59. [Nutrition Data Infrastructure for the AI Era: Operationalizing FAIR for Agent-Mediated Research](https://arxiv.org/abs/2608.10363)

**<font color=#1a73e8>作者：</font>** Lin Liao, Peng Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can accelerate nutrition research, but their analyses inherit the identity, semantic, and release ambiguities of the underlying data. We present Nutrition Data Service (NDS), source-preserving infrastructure that operationalizes FAIR for automated use: description resolution makes release-specific records findable; typed crosswalks connect independently released resources; machine-readable interfaces expose versioned sources and crosswalks, making analyses by AI agents replayable and auditable. On food-description benchmarks, NDS shows strong held-out accuracy and outperforms the best published language-model result on NutriBench. External and blinded crosswalk evaluations show that its typed contract favors defensible links and rejects unsupported mappings. In a person-level glycemic-index analysis, pinned NDS inputs produce identical outputs across models and repeated runs, while open-web reconstruction remains unstable. The central result is that agent-mediated nutrition research requires a new data infrastructure for data identity, search, and crosswalk.

---


### 60. [DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Computer Environments?](https://arxiv.org/abs/2608.10366)

**<font color=#1a73e8>作者：</font>** Mizanur Rahman, Mohammed Saidul Islam, Ridwan Mahbub 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world data science involves long-horizon workflows that span data wrangling, exploration, modeling, visualization, and validation, and require coordinated use of tools such as notebooks, IDEs, terminals, browsers, and databases within real operating environments. Yet existing benchmarks lack real-computer interaction and do not evaluate whether agents can execute complete end-to-end data-science workflows in realistic computing environments, failing to capture the multi-stage, multi-tool nature of data-science practice. We introduce DSAgentBench, the first benchmark to evaluate whether agents can automate full data-science workflows inside real computer environments. DSAgentBench contains 275 diverse tasks covering the entire data-science life-cycle, reflecting the complexity and tool coordination required in practice. Each task requires grounding decisions in intermediate outputs and coordinated tool use, and includes a deterministic evaluator that verifies analytical correctness, visual outputs, and model performance rather than code-only execution. Our extensive experiments with 15 closed- and open-source models show that even the strongest agent, Claude-4.6-Sonnet, achieves only 56.70% task success, while all open-source agents remain below 1%, frequently failing at tool orchestration, OS grounding, and multi-step reasoning. These results reveal a substantial capability gap between current agentic systems and real data-science workflows, positioning DSAgentBench as a foundation for developing grounded, verifiable, autonomous data-science agents. We release DSAgentBench at this https URL.

---


### 61. [Share First, Route What Remains: A Unified Framework for Token-Adaptive MoE Computation](https://arxiv.org/abs/2608.10392)

**<font color=#1a73e8>作者：</font>** Gongli Zhang, Zhulin Liu, C. L. Philip Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) models have recently moved beyond routing a fixed number of complete experts. Shared-expert designs preserve reusable knowledge, fine-grained methods vary computation within experts, and dynamic routers adapt the number of active experts. Yet these decisions are usually made independently, overlooking a basic dependency: extracting reusable computation changes both what remains and how much expert capacity the remainder needs. We study this dependency by decomposing sparsely upcycled feed-forward experts into key-value channels. Co-activated experts align at a subset of value positions; removing these positions changes expert preference; and greater shared coverage is associated with lower residual expert demand. These observations lead to one principle: share first, then route what remains. We instantiate it in UniF-MoE, a unified framework for token-adaptive MoE computation. Each expert is partitioned into aligned blocks. A shared-demand score sets the shared block count and pathway weight, key prototypes select the shared content, and the complementary demand determines the residual expert count through cumulative routing mass. A Gram regularizer separates and normalizes router embeddings, promoting diverse routing directions, sparse expert overlap, and a simple routing geometry. Experiments on DomainBed and GLUE show that this unified design improves predictive performance over representative static and dynamic MoEs while reducing activated computation, inference latency, and memory. Code is available at this https URL.

---


### 62. [Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2608.10393)

**<font color=#1a73e8>作者：</font>** Jiahui Han, Yuhui Yao, Xin Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have shown strong capabilities in controlling robots across diverse manipulation tasks. However, their adversarial robustness remains largely underexplored, and exploiting this weakness can lead to physical-world harm. Existing attacks on VLA models often rely on pixel-space perturbations or white-box access, resulting in noticeable artifacts and limited deployability in real-world robotic systems. In this work, we propose DURA, a diffusion-based unrestricted robotic attack that generates visually natural adversarial patches for VLA models. DURA supports both white-box and black-box attack settings, where the black-box setting requires only the predicted actions of the victim model. By optimizing along the latent trajectory of a pretrained diffusion model, DURA generates visually natural patches while steering the robot toward attacker-specified target actions. Extensive experiments in both simulation and the real physical world show that DURA consistently outperforms existing methods. Our findings expose a safety risk for physically deployed VLA models and call for stronger defenses.

---


### 63. [TideRL: Boosting Agentic RL Goodput with Readiness-Aware Scheduling](https://arxiv.org/abs/2608.10402)

**<font color=#1a73e8>作者：</font>** Yanyu Ren, Xizheng Wang, Xiao Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for large language models is moving toward multi-turn agentic workloads, where rollout tasks repeatedly pause for external environments, resume with growing contexts, and finish at highly variable times. In this setting, RL training goodput, measured by training throughput, matters more than raw GPU occupancy: GPU waiting and repeated prefill recomputation are pure overhead. We present TideRL, a readiness-aware elastic RL system with Continuous Task Batching, Resource-Aware Ref-Actor Pipelining, and Elastic Resource Scaling. CTB preserves useful rollout state, $\textrm{RA}^2\textrm{P}$ selects between decoupled streaming and colocated aggregation from the ready backlog and arrival interval, and ERS moves ranks between rollout and training using the same readiness signals. Across text-only and multi-modal agentic workloads, TideRL improves RL training goodput by up to 5.6$\times$ over synchronous baselines and over 33% over asynchronous baselines, while reaching similar task performance. It also improves KV cache hit rate by 1.58$\times$, reduces per-step training time by up to 44.3%, and cuts total waiting time by up to 77.6%.

---


### 64. [VisEditBench: Can Vision-Language Models Edit Visualization Code from Multimodal Feedback?](https://arxiv.org/abs/2608.10408)

**<font color=#1a73e8>作者：</font>** Mizanur Rahman, Arshia Azimlu, Shadikur Rahman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown strong capabilities in generating visualization code from textual or visual specifications. However, real-world visualization authoring is inherently iterative: users frequently revise existing visualizations to repair flawed charts or adapt them to desired styles. Existing benchmarks primarily evaluate generation from scratch, leaving visualization code editing from multimodal feedback largely unexplored. We introduce VisEditBench, a benchmark of 1,395 human-annotated visualization code-editing tasks grounded in realistic visualization workflows and failure cases. VisEditBench covers two practical settings: feedback-guided repair, where models revise visualization code using buggy or marked charts together with textual feedback, and reference-guided restyling, where models modify code to match a target chart image. Evaluating 20 state-of-the-art VLMs reveals that visualization code editing remains challenging: Claude-4.6-Sonnet achieves the best overall pass rate of 74.46%, while most open-source models remain below 50%. Performance is particularly weak on visually grounded style adaptation, where Claude-4.6-Sonnet achieves only 55.71%. To establish a strong baseline, we further propose VisEditAgent, a render-grounded editing framework that iteratively generates, executes, validates, and refines candidate edits. Built on GPT-4o, VisEditAgent improves overall pass rate from 55.75% to 67.99%, demonstrating the importance of render-grounded feedback for faithful visualization editing. We will release VisEditBench at this https URL.

---


### 65. [When the Interviewer Is a Bot: Behavior, Breakdowns, and Trust in MLLM-Led Interviews](https://arxiv.org/abs/2608.10412)

**<font color=#1a73e8>作者：</font>** He Zhang, Kambinachi Chukwuma, ChanMin Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Semi-structured interviews are a cornerstone of qualitative research but remain labor-intensive. We report an empirical study of what actually happens when the interviewer is an off-the-shelf real-time multimodal LLM (MLLM). We built InterviewBot, a voice-based interviewing system that wraps a real-time MLLM with a researcher-authored outline, and deployed it not as a novel architecture but as a research instrument for observing default MLLM interviewing behavior. In a practice study (N=15), participants completed a bot-led semi-structured interview and then a human-led reflection session about that experience. We contribute (i) a turn-level behavioral analysis of an MLLM interviewer (N_turns=428) showing that it is acknowledgment-heavy but probe-light (deepening probes account for 4.9% of all turns), and that 28.7% of question-bearing turns pack multiple questions into one turn despite an explicit one-question-at-a-time instruction; (ii) an inductive catalogue of four data-collection breakdowns (information loss, premature termination, latency, and interruption) observed in a deployed rather than simulated system; and (iii) three social dynamics from participants' reflections: disclosure calibration, where reduced social pressure coincided with shallower elaboration; institutional legitimacy, where trust tracked perceived stakes and what delegation to AI signaled about the organizer rather than conversational competence; and conversational grounding, where content-grounded paraphrase, not generic social filler, was what participants read as listening. We conclude with design implications for depth control, transparent handoffs, and non-templated listening mechanisms in human-centered interview automation.

---


### 66. [DriveVLA-M0: Failure-Aware Memory Augmentation for Autonomous Driving](https://arxiv.org/abs/2608.10413)

**<font color=#1a73e8>作者：</font>** Zebin Xing, Yupeng Zheng, Qiang Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for end-to-end autonomous driving by enabling unified reasoning across perception, language, and planning. However, existing approaches lack mechanisms to exploit past failures or adapt to distribution shifts, causing the model to persistently underperform on similar scenarios where it has previously failed. In this paper, we propose DriveVLA-M0, a retrieval-augmented VLA with failure-aware latent memory. We construct a latent memory pool that stores failure cases along with their structure scene representations and expert trajectory labels, and design a dedicated Retrieve Model that decouples static road structure and dynamic agent interactions to enable structurally grounded retrieval. At inference time, retrieved cases are injected into the model via a lightweight decoupled LoRA-based test-time training (TTT) mechanism, allowing targeted and scenario-specific correction without modifying the backbone. Extensive experiments on NAVSIMv1 and NAVSIMv2 benchmark demonstrate that our approach consistently outperforms prior methods, achieving 94.1 PDMS on Navtest and 47.0 EPDMS on Navhard with only 26.44 ms TTT backward latency overhead. Furthermore, we show that DriveVLA-M0 scales effectively with additional memory, enabling training-free performance gains through memory expansion. The code is available at this https URL.

---


### 67. [How Robust Are LLMs to Vietnamese Dialects?](https://arxiv.org/abs/2608.10414)

**<font color=#1a73e8>作者：</font>** Minh Tran, Trinh Chau, Thanh-Nhan Le 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are typically evaluated on standard written Vietnamese, yet everyday communication frequently involves regional dialects that preserve meaning but differ in surface form. Existing Vietnamese dialect work largely addresses this issue through dialect-to-standard normalization instead of measuring how the model fails under Vietnamese dialectal inputs. To address this gap, we present the first systematic evaluation of LLM robustness to Vietnamese dialect variation across multiple tasks, quantifying performance degradation and failure patterns. We introduce VialectBench (Vietnamese Dialects Benchmarking), a controlled benchmark for testing whether model decisions remain stable across six Vietnamese dialect groups. VialectBench contains 400 Standard Vietnamese source instances and 2,400 human-written dialectal rewrites spanning emotion recognition (ER), natural language inference (NLI), question answering (QA), and multiple-choice question answering (MCQA). Dataset evaluation with a fixed reference language model shows that the dialectal rewrites induce a measurable model-relative likelihood shift while remaining nearly equal in length to their Standard counterparts. Across ten instruction-tuned models, dialectal inputs reduce average performance by 2.82%, and no evaluated model is fully dialect-invariant. All four tasks are affected, with QA showing the largest average degradation. Robustness also varies substantially across dialect groups: PNT3 and PNT2 cause the largest average performance drops, at 6.17% and 4.73%, respectively, whereas PNB slightly improves average performance by 0.42%. The Central dialect group (PNT1-PNT4) also yields the highest average harmful-flip rate across all models, at 6.54%. These findings show that strong performance on Standard Vietnamese does not guarantee reliable behavior under meaning-preserving regional variation.

---


### 68. [Recovering Wasted Compute in Autoresearch Agents](https://arxiv.org/abs/2608.10424)

**<font color=#1a73e8>作者：</font>** Au Kwok Chun, Abhigyan Acherjee, Amrutha Rao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A slew of recent works develop agents for solving research problems end-to-end, a paradigm increasingly referred to as autoresearch. Such agents have inspired large industry investment, motivated by their potential to automate time-consuming human labor and customize machine learning solutions for specialized applications. In this paper, we study the modeling pipeline at the core of these autoresearch systems and identify common failure modes when they are applied to tabular datasets: (1) they waste compute resolving the same bugs over and over again; (2) they often fail to tune hyperparameters even when they have a large remaining compute budget; (3) the tree-search algorithms that power them do not explore; and (4) they perform data analysis, mimicking the humans whose data they are trained on, but do not use that analysis to make downstream decisions. We explore targeted interventions and find that a global debug consultant that shares discovered runtime constraints across all branches of the search tree, prompt- and control-level enhancements, and refined tree-search algorithms successfully recover wasted compute. Our results show that large gains in autoresearch agent performance are achievable through agentic design alone, holding the underlying language model fixed.

---


### 69. [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](https://arxiv.org/abs/2608.10430)

**<font color=#1a73e8>作者：</font>** Sanidhya Vijayvargiya, Rahul Lokesh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) deployed as AI agents frequently exhibit user specification-grounding failures, executing hallucinated, undesired actions to force a resolution rather than expressing uncertainty. Existing detection methods fail to provide actionable, real-time correction as they either do not localize the hallucinations, or incur prohibitive inference latency. We introduce the Latent Critic, a lightweight low-rank adapter (LoRA) that operates concurrently with a frozen base LLM's generation to actively restructure the transformer's residual stream---amplifying latent grounding signals and translating them into localized, natural language feedback within a single sequence. By refining the base model's native uncertainty signals, this manipulation of the latent space enables reliable, granular detection without the overhead of secondary inference loops. Mechanistic analysis via activation patching and layer-wise probing shows that this rank-invariant behavior restructures pre-existing uncertainty geometry into a linearly separable representation that transfers more reliably than base model representations alone. Using tool-calling as an instantiation of granular hallucinations, we validate the detection and downstream improvements enabled by the Latent Critic architecture across Qwen and Llama-based models. Demonstrating superior real-time efficacy, our approach significantly outperforms equivalent-scale fine-tuned external detectors, semantic entropy baselines, and passive internal probes in isolating hallucinations, achieving 0.966 AUROC and >80% accuracy in localization (e.g., ungrounded: date). When deployed in a closed-loop ReAct environment, the Critic acts as a negligible latency guardrail, intercepting hallucinations before execution to prevent undesired actions while simultaneously leveraging this specific localized feedback to enable efficient agent self-correction.

---


### 70. [Conversational versus Dashboard Explainable AI for UAV Intrusion Detection: An Empirical Study of Operator Trust and Reliance](https://arxiv.org/abs/2608.10434)

**<font color=#1a73e8>作者：</font>** Cong Chi Nguyen, Trang Mai Xuan, Vu-Duc Ngo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning-based Intrusion Detection Systems (IDS) have demonstrated superior performance in securing Unmanned Aerial Vehicle (UAV) networks. However, the 'black-box' nature of these models, combined with the high dimensionality of multimodal cyber-physical data, poses significant interpretability challenges. Static visualization dashboards may struggle to present complex relationships among multimodal cyber-physical features in a form that is easy for operators to inspect and interpret. To address this, we propose a Conversational XAI interface powered by Large Language Models (LLM) to facilitate on-demand investigation. In a controlled experiment with participants, we systematically evaluated the impact of this conversational interface versus a traditional XAI Dashboard on operator understanding, trust, and reliance during post-incident auditing tasks. Our results suggest that the conversational interface was perceived as more useful than the dashboard, potentially because it helped participants access and synthesize relevant information more easily. However, this benefit was accompanied by a lower level of appropriate self-reliance, indicating a potential risk of over-reliance. One possible interpretation is that the natural-language responses made the AI advice easier to accept, which may have reduced participants' tendency to verify the underlying evidence when the IDS was incorrect. These findings point to a potential trade-off in human-AI collaboration for UAV intrusion auditing: interaction mechanisms that improve perceived usability may also increase the risk of inappropriate reliance. We conclude by discussing design implications for future XAI systems that balance seamless interaction with cognitive forcing functions to foster appropriate reliance.

---


### 71. [MammoMix: Leveraging Mixture of Experts for Robust Mammogram Breast Detection](https://arxiv.org/abs/2608.10437)

**<font color=#1a73e8>作者：</font>** Dinh Tan Nguyen, Hoang Quan Dang, Chen Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast lesion detection in mammography remains a challenging task due to variations in image quality, lesion appearance, and population demographics across datasets. While current object detectors such as YOLO and DETR achieve strong results on individual datasets, their performance often degrades when trained on or applied across heterogeneous sources. To address this, we propose MammoMix, a novel framework based on Mixture-of-Experts (MoE) paradigm for robust and generalizable lesion detection. In MammoMix, each expert model is trained on a specific domain, allowing it to specialize in distinct characteristics of its source data. A gating mechanism adaptively weighs contributions from each expert based on input image, combining their outputs to enable domain-adaptive inference. To improve reliability, we further incorporate a calibration module, MoCAE, which adjusts confidence scores to reflect true predictive uncertainty. We evaluate MammoMix on 3 public mammography datasets: CSAW, DDSM, and DMID, covering diverse clinical settings. Results show that MammoMix outperforms baseline detectors in both average precision and reliability, particularly on datasets with greater variability. Our findings demonstrate that expert specialization and calibrated ensemble fusion significantly enhance model generalization and robustness. MammoMix offers a promising step toward dependable AI-assisted breast cancer screening across real-world clinical domains.

---


### 72. [Continuous Interaction Diffusion: A Diffusion-Native Runtime for Asynchronous Tool-Augmented Reasoning](https://arxiv.org/abs/2608.10438)

**<font color=#1a73e8>作者：</font>** Yuhang Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly rely on external tools to access up-to-date information, perform computation, and interact with the outside world. For autoregressive models, tool use naturally fits the generation process: the model emits a tool call, waits for the result, and then continues generating. Diffusion language models (dLLMs), however, reason by repeatedly refining many parts of their output in parallel, making this stop-and-resume interaction pattern unnecessarily restrictive. It can force tool decisions before the model's reasoning has stabilized, delay useful observations until a discrete call finishes, and introduce redundant refinement and tool execution, potentially hurting both task accuracy and inference efficiency.
We introduce Continuous Interaction Diffusion (CID), a diffusion-native model--runtime architecture that integrates tool interaction into iterative denoising. CID separates a model-read-only fact channel, a thought channel represented by a Typed Cognitive Tensor, and a display channel. Information needs can emerge before a textual or JSON call is fully serialized, allowing perceptual bindings to launch external reads while denoising continues. Returned results are projected into the evolving thought state and can revise earlier cognition and display regions. Persistent bindings reuse static results without repeated external execution and refresh changing sources when needed. CID is designed to expose evidence earlier, overlap tool latency with model computation, reduce duplicate external work, and preserve useful computation after new evidence arrives. We formalize the architecture, runtime, and training objectives, and define an evaluation protocol for task quality and end-to-end efficiency. This first paper focuses on read-only tools and makes no empirical performance claims.

---


### 73. [Detecting an Effect Is Not Learning to Act on It: A Reward-SNR Floor for LLM Acquisition Agents](https://arxiv.org/abs/2608.10441)

**<font color=#1a73e8>作者：</font>** Ying Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many pipelines can pay a per-example cost to acquire an auxiliary, model-derived observation -- an LLM's structured reasoning, a slow oracle, an expensive measurement -- and then must decide when the acquired signal is worth using. Our thesis is a distinction that is easy to miss: detecting that such a signal helps on average is not the same as learning to act on it per instance, and a reward-SNR floor governs when the second is even possible. Even when the signal is faithful and an in-sample oracle picking the top-b examples by realized reward shows a sizable apparent gain, no deployable policy can learn when to acquire it: across per-impression, cluster, regime, and uplift-tree granularities, learned routing never beats random, and a matched-moment noise placebo reproduces >=100% of the oracle's apparent gain -- the apparent "learnable structure" is order statistics of noise. We explain this with one distinction, detecting a mean effect vs. learning a per-instance acquisition policy, and a reward-SNR detectability floor: routing is estimable offline only if the reward SNR rho clears rho*(N) ~= 2.8/sqrt(N), with a positive control confirming a true low-SNR limit rather than a broken pipeline. As a concrete instantiation we introduce Structured Hypothesis Embeddings (SHE): a frozen LLM turns a user history into ranked, confidence-scored, evidence-grounded intent hypotheses, fused into a recommender. On three public datasets (MIND, REES46, Amazon-Beauty), SHE is faithful and calibratable, yet its value is backbone- and regime-conditional (significant over an ordered GRU, +0.0114, 95% CI [+0.0030, +0.0209], but a global redundancy gap indistinguishable from zero), and learned acquisition collapses at every granularity because all three datasets sit below the floor. The realizable unit is a design-time regime gate, not a per-instance policy. We release code and a one-command reproduction.

---


### 74. [From Reasoning Depth to Reasoning Breadth: Evaluating Multi-Point Associative Reasoning in Large Language Models](https://arxiv.org/abs/2608.10444)

**<font color=#1a73e8>作者：</font>** Si'an Xie, Jiaxun Liu, Biao Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have made substantial progress on reasoning tasks that require increasingly long and complex inferential chains. This progress primarily reflects reasoning depth. A complementary and comparatively unexamined capability is reasoning breadth: exploring multiple semantic directions in parallel and integrating the resulting clues into one coherent answer. We introduce MPAR-Bench, a bilingual English-Chinese benchmark that isolates reasoning breadth through multi-point associative reasoning. Inspired by the cooperative game Just One, each item asks a model to recover a hidden target from several independently generated, semantically diverse clues. We construct 1,000 items using a multi-agent clue-generation pipeline, embedding-based diversity filtering, and human verification. Only the answer space is drawn from public word lists, whereas every clue set is generated from scratch. Beyond exact-match accuracy, we evaluate models using accuracy, ANLS, embedding similarity, reasoning-trace verification, and four perturbations: clue masking, order shuffling, distractor injection, and multi-step clues. Across evaluated models, perturbations reduce accuracy by 9-18 percentage points in English and 5-12 percentage points in Chinese. Thinking mode improves standard-setting accuracy, especially in English, but does not consistently reduce sensitivity to perturbations. Case-level analysis also shows that extended reasoning can overturn an initially correct hypothesis. These results indicate that greater reasoning depth does not automatically confer robust reasoning breadth, and that reasoning breadth remains largely uncovered by current benchmarks.

---


### 75. [Rationale-Guided Learning for Multimodal Emotion Recognition](https://arxiv.org/abs/2608.10448)

**<font color=#1a73e8>作者：</font>** Sujung Oh, Jung Uk Kim, Sangmin Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion recognition in conversation (MERC) requires understanding complex interactions between verbal and non-verbal cues. However, most existing approaches fundamentally treat this as a direct input-output (multimodal cues-emotion labels) mapping problem, overlooking the causal reasoning that humans use when interpreting emotions. We propose rationale-guided learning (RGL), a novel framework that transforms MERC into a cognitively-inspired reasoning task. Based on dual-process theory, we decompose emotional reasoning into three facets: Intuitive (immediate perception, System 1), Contextual (situational analysis, System 2), and Integrative (synthesis of both). We leverage an MLLM offline to generate structured rationales, which are encoded as memories to guide model training via aligning internal representations with human-like reasoning patterns. Our final model operates without any MLLM overheads at inference time. Experimental results show that RGL achieves state-of-the-art performance on the IEMOCAP and MELD benchmarks. Further, for interpretation, we demonstrate that the model's internal features effectively retrieve semantically correct rationales for unseen test samples, validating its rationale reasoning capabilities.

---


### 76. [MD-ProTector: Positioning Multiple Data-Driven Prototypes for LLM-Generated Text Detection](https://arxiv.org/abs/2608.10459)

**<font color=#1a73e8>作者：</font>** Jinmo Han, Jimin Hong, Chanyeong Moon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM-generated content becomes more sophisticated, detection systems for distinguishing those texts from human-written text must operate at scale while handling diverse writing styles, domains, languages, and generator models. Input-only encoder detectors are suitable for practical deployment setting, but standard binary classification supplies only the class label and does not explicitly organize the substantial variation within either class. We propose MD-ProTector, which represents each class with multiple trainable reference vectors in the encoder embedding space, referred to as prototypes. These prototypes provide separate decision boundaries for different groups of texts within the same class. However, adding multiple prototypes alone does not determine which variation each prototype should represent. MD-ProTector addresses this problem with Prototype Positioning loss, which separates class-level structure from the within-class variation that differentiates individual prototypes. Evaluated across five settings from three large-scale benchmarks covering domain, generator, language, and adversarial variation, MD-ProTector achieves the highest AvgRec on MAGE CDCM and RAID and the highest AUROC and lowest FPR95 on RAID among the compared encoder-based methods.

---


### 77. [Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection](https://arxiv.org/abs/2608.10462)

**<font color=#1a73e8>作者：</font>** Zhen Yang, Mengqi Wang, Gengda Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are trained on massive and largely undisclosed corpora that may contain copyrighted or privacy-sensitive content. Data contamination detection (DCD) therefore aims to determine whether a given text is a member of the pre-training corpus of a target LLM. Recent state-of-the-art DCD methods follow a feature-based paradigm that derives membership features from the input text and the corresponding model output. However, most modern LLMs undergo post-training, such as instruction tuning, preference optimization, and reasoning-oriented training, which can alter model outputs and shift the corresponding membership features, thereby reducing the separability between members and non-members.
To address this problem, we propose CalibDCD, a broadly applicable calibration framework for feature-based DCD methods, comprising (1) Multi-View Shift Detection, which identifies recurring feature shifts associated with post-training, and (2) Bounded Feature Correction, which selectively mitigates their influence on membership prediction. Specifically, Multi-View Shift Detection evaluates controlled prompt variants on known non-member texts and consolidates the most informative views to identify recurring feature shifts. Bounded Feature Correction selectively adjusts feature components aligned with the detected shifts and controls the correction extent to preserve useful detection information.
Experiments show that CalibDCD consistently improves existing feature-based detectors, with gains of up to 7.0% in AUC and 15.0% in TPR@5%FPR.

---


### 78. [RLMOpt: Adaptive Prompt Optimization via Recursive Language Models](https://arxiv.org/abs/2608.10471)

**<font color=#1a73e8>作者：</font>** Subhash Bangalore Satheesha, Nirvik Pande, Deepthi Duddempudi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt optimizers automate the search for prompts that improve language-model performance, but existing methods rely on a predefined optimization procedure: the algorithm determines which candidates to explore and how the search progresses, while the language model generates or refines prompt proposals. We introduce RLMOpt, a prompt optimizer that makes the search policy itself language-model-driven through a recursive language model (RLM). The RLM agent operates over a tool-based environment, inspecting task information, analyzing failures, generating candidates, allocating evaluation budget, and deciding when to stop. A deterministic harness complements the agent by enforcing objective scoring, Pareto-based selection, and regression constraints.
We evaluate RLMOpt across four benchmarks spanning structured clinical information extraction (Chia), multi-hop question answering (HotpotQA), verifiable instruction following (IFBench-2025), and multi-turn tool-calling agents (BFCL). In a matched comparison at a single seed, RLMOpt obtains the best held-out score on all four benchmarks and leads the four-task mean (0.610 against 0.589 for GEPA). Repeating each benchmark across seeds yields 11 matched benchmark-seed comparisons, in which RLMOpt outperforms GEPA in 9 cases. Across all 11 runs, it never produced a prompt that underperformed its seed, whereas GEPA fell below its starting point twice. It is also more efficient, achieving these results with fewer search rollouts while producing prompts that are 27-79% the size of those produced by GEPA.
Our results further show that optimization gains are determined primarily by the headroom available in the seed prompt, rather than by the search budget. Efficient optimization therefore depends on reaching the available headroom reliably and with minimal search

---


### 79. [Evaluating Rational Contracting in Natural Language](https://arxiv.org/abs/2608.10475)

**<font color=#1a73e8>作者：</font>** Bhavyesh Sajja, Max Kleiman-Weiner, Roger Zimmermann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The emergence of language-based AI agents promises to transform the scope of machine economic activity. Instead of just proposing bids or following hard-coded protocols, such agents can be used to negotiate and execute agreements in open-ended natural language. However, most evaluations of these abilities have focused on one-off exchanges or simple economic games, leaving open the rich space of time-extended, contingent, and incomplete contracts made expressible by language; they also focus on raw profit, without measuring the qualities required for trustworthy contracting. We address this by formulating a rational framework for how agents should negotiate and perform natural language contracts in uncertain multi-step environments. Within this framework, we develop metrics and baselines for quantifying rational and cooperative play. To evaluate how agents perform at such contracting, we instantiate our framework in ContractSim, an evaluation suite where two players negotiate and execute a multi-turn supplier contract under environmental and inter-player uncertainty. Across six environments and three supplier settings (catering, hotel cleaning, and AI hosting) we find that current LLM-based agents reach agreement reliably, and negotiate efficient contracts when environmental uncertainty is low. However, under high uncertainty, they often fail to negotiate satisfiable, efficient, or mutually beneficial contracts. They are also frequently uncooperative when executing contracts, violating contract terms for additional profit even when contracts are easy to satisfy. These findings highlight room for improvement in the design of language agents that can negotiate, interpret, and execute contracts both rationally and cooperatively.

---


### 80. [Multi-Granular Rationale-Guided Molecular LLM for Property Prediction](https://arxiv.org/abs/2608.10480)

**<font color=#1a73e8>作者：</font>** Junwoo Park, Minyoung Shin, Cheol Soon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely applied across chemical tasks, such as molecular property prediction, which underpins drug discovery. Molecular LLMs represent a molecule through several modalities, notably a 1D SMILES sequence or a 2D molecular graph. Both encode molecular information implicitly, so the contribution of individual substructures remains opaque. Retrieval and augmentation methods add context, but from external sources. However, the cues chemists reason over are the internal substructures that drive a property up or down. We propose MR-MoL, a multi-granular rationale-guided molecular LLM that supplies this evidence directly. A fine-tuned GNN scores each substructure through masking, and the most influential ones are serialized as a ranked, direction-tagged rationale that the LLM reads alongside the SMILES sequence and molecular graph. The rationale spans three levels of granularity: Murcko scaffolds with their side chains, BRICS fragments, and functional groups. This is, to our knowledge, the first method to expose GNN-derived attributions to an LLM as evidence for property prediction. On eight MoleculeNet tasks, MR-MoL achieves the best overall results among generalist models and narrows the gap to specialist models tuned for each task. Five diagnostics further confirm that the model reads the rationale rather than merely benefiting from its presence. Its direction, rank, and substructure each shape the prediction, and its attributions reproduce known structure-property relationships.

---


### 81. [Predicting Space Groups of Double Perovskites by LLM with Dynamic Few-Shot Learning](https://arxiv.org/abs/2608.10483)

**<font color=#1a73e8>作者：</font>** Jongwon Park, Inhyo Lee, Junhyeong Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Double perovskites (DPs) offer broad compositional tunability, but predicting the space groups (SGs) of stable structures remains difficult because available datasets are often strongly imbalanced toward dominant SG classes. We refer to dominant SG classes as major SGs and underrepresented classes as minor SGs. We introduce Dynamic and Diversity-enhanced Few-shot Retrieval and Rule-Guided Inference for Space-Group Prediction (DyRIS), an LLM-agent-based framework that predicts ranked SG candidates from a given DP composition. DyRIS uses diversity-enhanced dynamic few-shot prompting to retrieve relevant in-context examples while limiting the dominance of frequently represented SGs. It further incorporates rule-guided inference based on B/B' cation ordering, quantitative indicators, and major-SG bias control to refine and rank the final Top-3 SG candidates. We evaluate DyRIS on 3,528 thermodynamically filtered DP entries and compare it with composition-based and descriptor-based baselines. At a training-data ratio of 0.5, DyRIS achieves competitive overall accuracy while obtaining the best Overall Top-1 macro-F1 score and the best performance across all Minor-SG metrics. DyRIS improves Minor-SG Top-1 accuracy by 3.26 percentage points relative to CrabNet and achieves higher Minor-SG Top-3 accuracy than the strongest PyCaret-based baseline. Ablation studies show that diversity-enhanced retrieval, quantitative indicators, major-SG bias control, and B/B' ordering information each contribute to prediction performance. Additional experiments show that the final rule-guided inference step is not easily replaced by conventional classifier- or ranker-based models. These findings demonstrate the potential of combining retrieval-based LLM reasoning with crystallographic domain knowledge for SG prediction in imbalanced materials datasets.

---


### 82. [When Vision Becomes Text: Visual Token Pruning via Cross-Modal Residual Guidance in VLMs](https://arxiv.org/abs/2608.10489)

**<font color=#1a73e8>作者：</font>** Congyang Ou, Ruike Song, Yang Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Abundant visual information strengthens vision-language model (VLM) perception, yet massive visual tokens raise inference costs. Existing visual token pruning methods rely on similarity-based guidance, which exploits pairwise text-vision and vision-vision token correlations for compression. However, such methods only capture local layer-level signals and overlook the whole inference process in VLM. In this paper, we revisit VLM inference and present a new efficient guidance scheme that complements similarity-based guidance. In particular, we identify a key observation: as LLM layers deepen, text tokens continuously aggregate visual information via self-attention and progressively absorb partial visual content into textual representations. To quantify this phenomenon, we propose Cross Modal Absorption (CMA) from a geometric representation perspective to measure how much visual information is absorbed by text, revealing that more visual tokens in deeper layers can be approximately explained by the text subspace. We accordingly propose Cross Modal Residual (CMR). It projects visual tokens onto the text subspace via Tikhonov regularized least squares and exploits reconstruction residuals to quantify visual information that cannot be explained by text. Finally, based on CMR, we present SIEVE, a training-free visual token compression method that combines CMR, text-attention relevance, and residual-space diversity to retain task-relevant and complementary tokens. Experiments on diverse VLM architectures verify the effectiveness of SIEVE. For instance, on LLaVA-NeXT-7B, SIEVE keeps only $11.1\%$ of visual tokens while preserving $97.5\%$ of the original average performance, achieving $3.62\times$ prefill speedup, $2.49\times$ end-to-end speedup, and a $6.02\times$ KV-cache reduction.

---


### 83. [INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators](https://arxiv.org/abs/2608.10492)

**<font color=#1a73e8>作者：</font>** Rose Niousha, Minwoo Kang, Narges Norouzi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based simulators often reproduce observable actions but fail to capture the underlying reasoning behind them. In education, where student simulation is increasingly used for various applications such as evaluating tutoring systems, this gap is especially pronounced. Two students may submit identical submissions for entirely different reasons. We present INTERNAL STUDENT DIALOGUE (INSIDE), a student modeling framework that fine-tunes LLMs not only to act like students but also to think like them. INSIDE generates internal dialogue grounded in Bloom's Taxonomy across cognitive, affective, and action dimensions, and fine-tunes models on paired think traces and actions. We baseline against different prompting frameworks and evaluate on two axes: fidelity of simulated actions and quality of generated internal dialogue. Our evaluations show that INSIDE improves simulation fidelity in both action fidelity, matching code generation of real students, and reasoning alignment, achieving the highest alignment across models up to 57.9%.

---


### 84. [GeoForge: Non-Parametric Self-Evolving Agents for Earth-Observation Reasoning](https://arxiv.org/abs/2608.10494)

**<font color=#1a73e8>作者：</font>** Xin Xiao, Jiang Zhong, Junnan Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Earth observation (EO) agents construct scientifically valid tool workflows and ground their conclusions in current geospatial evidence. This is challenging because EO workflows are constrained by sensing semantics, product dependencies, spatial and temporal compatibility, and parameter requirements. Existing agents often search a broad operation space for each query, while recent self-evolving systems do not fully organize heterogeneous EO trajectories into reusable knowledge across different decision levels. To solve this problem, we present GeoForge, a training-free, self-evolving framework that transforms completed trajectories into a structured nonparametric execution state. GeoForge constrains the operation space according to the sensing context, then retrieves a task-conditioned prior from three complementary memories. Workflow Graph Memory captures global operation order, Action-Level Experiences provide local corrections, and the Adapted Skill Standard Operating Procedure preserves procedural and data constraints. The retrieved prior guides tool execution, while current observations remain the basis of the final answer. After each task, a safety-gated distillation process converts grounded trajectories into reusable execution knowledge for future retrieval. This execution, distillation, and reuse loop improves planning without updating the backbone LLM. Experiments on multiple geospatial benchmarks demonstrate that GeoForge consistently improves both task accuracy and tool-use trajectory quality across diverse LLM backbones, while substantially reducing tool-planning and reasoning errors for most LLMs.

---


### 85. [SapiensID 2.0: Aligning Human Recognition Foundation Models with Human Perception](https://arxiv.org/abs/2608.10497)

**<font color=#1a73e8>作者：</font>** Yiyang Su, Jie Zhu, Feng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While foundation models have significantly advanced human recognition across diverse modalities, they predominantly rely on static, geometric feature extraction. This approach fundamentally diverges from human perception. Consequently, current models often suffer from "semantic blindness," overfitting to transient noise while failing to leverage invariant soft biometrics, and struggle to capture temporal motion signatures. To bridge this gap, we propose SapiensID 2.0, a human recognition framework enriched with both semantic and temporal awareness. To overcome the lack of soft-biometric annotations, we transfer zero-shot semantic knowledge from Multimodal Large Language Models (MLLMs) into a discriminative embedding space. We resolve the dimensional mismatch between these spaces using Invariant Trait Alignment (ITA) to distill core persistent traits, and Transient Noise Disentanglement (TND) to decouple artifacts like clothing. Furthermore, we design a Kinematic Semantic Attention Head (K-SAH) that extends spatial attention across temporal windows. By tracking semantic patches over time, K-SAH captures rich kinematic signatures without requiring large-scale video datasets. Extensive experiments demonstrate that SapiensID 2.0 achieves state-of-the-art performance across image- and video-based person re-identification and gait recognition, while maintaining robust face recognition capabilities.

---


### 86. [From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents](https://arxiv.org/abs/2608.10502)

**<font color=#1a73e8>作者：</font>** Caili Yu, Yiqi Wang, Jiaqi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory lets language-model agents reuse information across sessions, but it also makes errors durable: a poisoned, stale, or misattributed record can alter reasoning, tool use, answers, and subsequent memory writes. Existing defenses mainly detect or delete suspicious memories, or revise the current response. Deleting the source leaves already propagated claims, actions, and derived memories active, whereas resetting the store or replaying the full trace destroys benign state and repeats unnecessary computation. We therefore formulate \textbf{post-failure memory recovery: } \textit{given a failed execution and diagnosed faulty memories, recover both the answer and persistent state while retaining unaffected work.} Our \textbf{dependency-guided rollback repair} builds a typed memory-to-action graph from runtime provenance, traces explicit downstream dependencies, preserves candidates with independent trusted support, deactivates unsupported memory state, and selectively replays only answer-relevant affected computation. We evaluate this approach on a 150-case controlled benchmark spanning three tool-use domains and four memory failure types, and on a 50-case trajectory-derived stress test adapted from LongMemEval-V2. On the controlled benchmark, it achieves 85.3\% recovery versus 77.3\% for the best competing recovery method, removes all diagnosed faulty memories, preserves all benign memories, and requires only selective replay with modest LLM-call cost. On the adapted subset, it reaches 68.0\% recovery versus 54.0\% for the next best method, while also achieving the highest claim invalidation F1, 0.669 versus 0.603. Overall, the results do not imply uniformly better trace reconstruction, but show that dependency-guided rollback repair provides a strong recovery--cost trade-off while repairing faulty memory state and preserving benign memory.

---


### 87. [Every Token Counts: Exact Likert-Scale Distributions for Measuring LLM Attitudes and Biases](https://arxiv.org/abs/2608.10503)

**<font color=#1a73e8>作者：</font>** Davood Wadi, Mohsen Ghodrat, Matthew Philp  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly deployed as autonomous agents, accurately evaluating their latent values and biases is critical. The NLP community typically evaluates models using large, unstructured benchmarks. While effective for general capabilities, these datasets fundamentally conflate causal mechanisms: even when an aggregate bias is detected, unstructured evaluations cannot disentangle whether it stems from baseline traits, contextual confounders, or complex interactions. To address this, we introduce an analytically exact framework for the controlled behavioral evaluation of LLMs. We bridge human psychometrics with LLM mechanics by resolving gaps in design, measurement, and analysis. First, we replace unstructured prompting with fully crossed factorial experiments to systematically isolate causal main and interaction effects. Second, we eliminate Monte Carlo text sampling noise by operating directly on exact, token-level Probability Mass Functions (PMFs). Third, we derive a multivariate ordinal consensus metric and a distributional ANOVA to process these PMFs analytically. We validate our framework with a case study on consumer ethnocentrism across five LLMs, demonstrating how our approach isolates systemic country-of-origin biases that aggregate benchmarks otherwise obscure.

---


### 88. [MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph](https://arxiv.org/abs/2608.10504)

**<font color=#1a73e8>作者：</font>** Jung Hwan Lee, Kyu Ho Lee, Gwang Hoon Yoo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As coding agents increasingly handle implementation, the central challenge shifts from building individual agents to building an infrastructure that systematically improves them. Current approaches optimize agent systems without accumulating transferable knowledge, accumulate knowledge without compositional reasoning over it, and lack a mechanism for that knowledge to self-evolve through operational evidence. MEGA (Meta Evaluation-Grounded Adaptation) addresses these gaps as a self-evolving infrastructure: each optimization cycle produces durable assets, compositional reasoning over those assets guides subsequent optimization, and operational evidence refines both the accumulated wisdom and the reasoning that governs it. Layer 1 distills reusable wisdom from agent sessions through behavioral-pattern clustering and empirical A/B validation, transforming each process into a durable asset. Layer 2 decomposes these assets into atomic PCR (Primary-Context-Resultant) units within a typed Wisdom Graph and performs deductive, abductive, and inductive reasoning to expand implicit relations; it then assembles context-specific execution plans through compositional retrieval that surfaces bridging knowledge unreachable by embedding similarity alone. Layer 3 performs multi-agent collaborative optimization over heterogeneous agent workflows (code nodes, LLM calls, and tool-using agents), attributing improvement effects to specific strategy changes through controlled evaluation that eliminates data variance. Evidence fed back from Layer 3 drives the self-evolution of both the curation strategies that govern wisdom composition and the optimization trajectories accumulated across runs. The result is an infrastructure in which optimizing an agent system and evolving the knowledge that guides optimization are one and the same process.

---


### 89. [RadFusion: Towards Threshold-Controllable Radiology Report Generation](https://arxiv.org/abs/2608.10505)

**<font color=#1a73e8>作者：</font>** Ying Jin, Noel C. F. Codella, John Corring 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated radiology report generation is advancing rapidly in response to the shortage of radiologists, yet unlike a perception model, existing generation models offer no control over the sensitivity-specificity trade-off of their diagnostic content. Such control is essential because clinical scenarios diverge: emergency triage prioritizes sensitivity to reduce missed findings, whereas confirmatory interpretation emphasizes specificity to limit unnecessary interventions. A single fixed report can neither adapt to these scenarios nor support the ROC-based validation widely expected for regulatory clearance. We introduce RadFusion, a framework that equips report generation with threshold controllability. Our method fuses a multi-label classifier, which provides per-disease confidence scores, with a VQA-based report generator, which describes medical findings in detail; an LLM then rewrites the report so that its stated diagnoses follow the classifier's decisions at the selected threshold while staying grounded in the generator's descriptions. On MIMIC-CXR, the performance of RadFusion conforms to the classifier's ROC curve: sweeping the threshold and mapping the reports back to class labels reproduces the classifier's validated ROC performance. This conformance makes generated reports quantitatively evaluable through ROC analysis, strengthening the case for regulatory clearance, and enables operating-point selection that matches report behavior to clinical context. Moreover, combining the two model types improves diagnostic accuracy over uncontrolled generation: sensitivity increases by 6.9% at matched specificity, and specificity by 20.7% at matched sensitivity. These results show that RadFusion makes report generation clinically adaptable, quantitatively verifiable, and diagnostically more reliable.

---


### 90. [MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows](https://arxiv.org/abs/2608.10509)

**<font color=#1a73e8>作者：</font>** Yiqi Wang, Zihao Yan, Jiaqi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shared memory helps language-model agents reuse information across long workflows, yet relevant evidence may not be admissible for a particular agent or action. Because restrictions propagate through derivations, summaries can conceal private, poisoned, untrusted, or revoked sources, enabling unauthorized reads or unsafe actions. Existing approaches provide semantic retrieval, scoped access, or lineage tracking, but do not clearly separate hard authorization from graded trust or adapt evidence requirements to action risk. We introduce MAP-Graph, a provenance-aware memory layer that represents agents, sources, memories, claims, and actions in a typed execution graph. It traces ancestry, excludes permission-ineligible records, reranks eligible memories by semantic similarity and multiplicative path trust, and applies a risk-sensitive gate before action execution while retaining affected lineage for audit. On a controlled benchmark of 2,700 synthetic tasks per method across three domains, MAP-Graph achieves 94.96\% overall task success, 72.70\% exact decision accuracy, and 90.22\% in the clean setting, where success requires a correct \textsc{Allow} rather than a safe intervention. Ablations isolate the roles of permission filtering, path trust, and action gating, while transfer tests with two additional backbones preserve the exact-decision and access-control advantages. These results support provenance as an operational control signal, rather than only post-hoc audit metadata, within the evaluated setting.

---


### 91. [Unlocking the Power of Medical Tabular Data via Semantic-Aware Multimodal Pre-training](https://arxiv.org/abs/2608.10522)

**<font color=#1a73e8>作者：</font>** Yingsheng Liu, Haiming Li, Jingmin Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While vision-language models dominate medical representation learning, unstructured text lacks the dense, quantitative diagnostic phenotypes inherent in structured clinical tables. However, existing multimodal pre-training methods underutilize this potential due to semantic-agnostic designs that treat tabular inputs as flat vectors and employ unstable continuous regression objectives. To overcome this, we propose a novel semantic-aware framework explicitly modeling the intrinsic two-dimensional structure of tabular data. First, addressing the inter-feature hierarchy of varying diagnostic importance, we introduce Importance-Aware Adaptive Masking to construct a label-free curriculum prioritizing salient features. Second, addressing the intra-feature continuity-discreteness duality, we propose a Soft-Label Discretized Module that replaces unstable numerical regression with stable distribution matching, thereby mathematically preserving ordinal relationships. Extensive experiments across large-scale dermatology (SLICE-3D, HOP) and ophthalmology (EyePACS) datasets establish a new state-of-the-art (SOTA), demonstrating exceptional robustness and cross-domain generalizability.

---


### 92. [Dynamic Context Adapters: Efficiently Infusing History into Vision-and-Language Models](https://arxiv.org/abs/2608.10525)

**<font color=#1a73e8>作者：</font>** Yuhang Song, Bor-Jiun Lin, Jiaxu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Historical context integration presents a fundamental challenge for Vision-Language Models (VLMs) in sequential decision-making tasks. Current VLMs process visual inputs independently, which creates critical limitations for downstream applications that require temporal understanding. Direct incorporation of historical frames into Transformer inputs produces quadratic attention complexity and excessive memory consumption. Existing approaches suffer from significant drawbacks: computational inflation or substantial information loss through temporal compression. To address these challenges, we introduce Dynamic Context Adapter (DCA), a novel context injection approach for pretrained VLMs. Our method employs fixed-size, dynamically compressed memory to preserve historical semantics without frame concatenation. DCA bridges static VLMs and recurrent policies and enables memory capabilities in pretrained models while maintaining computational efficiency. DCA achieves over $25\%$ reduction in attention FLOPs and $13\%$ memory savings while improving performance on long-horizon tasks.

---


### 93. [On Understanding, Identifying, and Mitigating Vulnerabilities in Agentic Large Language Models](https://arxiv.org/abs/2608.10530)

**<font color=#1a73e8>作者：</font>** Md Jafrin Hossain, Mohammad Arif Hossain, Nirwan Ansari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have undergone a shift from stateless conversational interfaces to autonomous agents capable of multi-step planning, tool invocation, code execution, and maintaining persistent memory. When these agents operate with real-world privileges---calling APIs, modifying files, and querying databases---a compromised reasoning step can trigger unauthorized data access, irreversible state changes, or cascading failures, yet the security research community has not kept pace. To quantify the state of the field, we conducted a systematic literature review under PRISMA 2020 guidelines across six databases, screening 743 records and retaining 85 papers (2023--2025) on agentic LLM security. Attack research outpaces defense work by 3.9:1. Perception-layer vulnerabilities (prompt injection, jailbreaking, adversarial perturbations) dominate, accounting for 66\% of papers, while action-layer vulnerabilities (tool misuse, code injection, sandbox escape) appear in only 4.7\%, misaligned with real-world risk. Code execution security accounts for 3.5\%, and tool-augmented agents 12\%. We contribute a four-layer taxonomy mapping 13 vulnerability types across perception, brain, action, and interaction layers, and identify seven open problems centered on containment. Agentic LLM insecurity stems from architectural coupling, where weak isolation allows vulnerabilities to propagate across layers.

---


### 94. [Measuring Semantic Abstractness of SAE Features via Nonlocality](https://arxiv.org/abs/2608.10537)

**<font color=#1a73e8>作者：</font>** Chuqiao Lin, Shivaji Sondhi, Xiao-Liang Qi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have helped uncover mechanistic explanations for LLM behaviours such as reasoning, jailbreaking etc., via understanding the corresponding task-relevant and causally effective features. To evaluate such mechanistic explanations, downstream studies must distinguish surface lexical features from genuinely high-level ones. However, neither an autointerp-based semantic description nor causal steering utility fully resolves the abstraction level of a feature. To this end, we introduce \emph{Feature Nonlocality} (FNL), defined as the entropy of the normalized per-position influence on an SAE feature's activation. We report that FNL correlates with existing LLM-based proxy metrics of feature semantic abstractness, and successfully distinguishes context-dependent reasoning features from token-driven ones, correctly assigning the higher FNL to the contextual feature in $73$--$84\%$ of randomly drawn pairs that consist of one contextual and one token-level feature.
We demonstrate two downstream applications. We audit SAE-based features used for jailbreak mitigation and find surprisingly that most effective features are positional features with low FNL rather than genuinely recognizing harmful intents.
We report that steering high-FNL features in DeepSeek-R1-Distill-Llama-8B improves MATH-500 accuracy by $4.6$ points over the unsteered model and outperforms steering low-FNL features, though the gains are model-specific. We conclude that FNL provides an LLM-independent, label-free, correlational witness of the abstraction level of an SAE feature, with applications in evaluating mechanistic explanations as well as selecting features for downstream interventions.

---


### 95. [SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models](https://arxiv.org/abs/2608.10538)

**<font color=#1a73e8>作者：</font>** Chenhao Dang, Siyuan Xiong, Conghui He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills represent a standardized format for packaging procedural knowledge and domain expertise, serving within agent harness systems as an essential mechanism to continually constrain a language model's behavior space for repeatable, high-quality task execution. However, because strong closed-source models entail high inference costs, current popular agent harnesses, such as Codex and OpenClaw, remain prohibitively expensive when deploying these skills to accomplish real-world tasks. The rapid capability enhancement of open-source models deployable on consumer-grade GPUs presents a compelling opportunity to drastically reduce these costs by leveraging skill-based behavioral constraints. Nevertheless, automatically generating effective skills tailored specifically for such compact models remains a significant practical challenge. To address this, we propose SKILLER, a natural-language-driven reinforcement learning framework designed to automatically generate executor-specific skills for small models, which employs a strong model as the actor and critic, treats the small-model agent system as the environment, and propagates all reinforcement learning signals entirely via natural language. Extensive experimental evaluations across five relevant benchmarks using Qwen3.5-9B and Qwen3.5-4B demonstrate that SKILLER outperforms three open-source and one closed-source skill generation or evolution methods, achieving absolute gains ranging from 4.3 to 20.4 percentage points for the 9B model and 1.8 to 13.3 points for the 4B model, while remarkably matching the performance of strong closed-source models on single-skill tasks in SkillsBench. The project is available at this https URL.

---


### 96. [DashArena: Benchmarking LLMs on Interactive Analytic Dashboard Generation](https://arxiv.org/abs/2608.10567)

**<font color=#1a73e8>作者：</font>** Xiaotong Wang, Dazhen Deng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analytic dashboards combine coordinated views and interactions for data exploration and decision-making. Recent models can generate them from data and natural-language goals, but evaluating their usefulness remains difficult. Dashboard generation is open-ended, and neither static appearance nor successful execution alone captures analytical support and interaction quality. We introduce DashArena, to our knowledge the first benchmark for open-ended, task-grounded generation of interactive analytic dashboards. Its key innovation is to require each system to generate both a dashboard and a replayable interaction trajectory. A browser executor replays the trajectory and turns the system's intended analytical workflow into reproducible visual and execution evidence. A VLM judge compares candidates using this evidence, and Bradley--Terry aggregation produces the leaderboard. We further distill the judge into the open-weight DashJudge-8B. Human evaluations show that DashJudge-8B effectively reproduces human judgments and ablations show that interaction evidence improves judge agreement. Experiments with frontier models reveal persistent rendering, analytical, and interaction failures. Together, these results show that realistic dashboard generation remains challenging and that interaction-aware evaluation captures failures missed by static or execution-only checks.

---


### 97. [HexEval: An Evidence-Driven Hexagonal Framework for Multidimensional Scholar Assessment](https://arxiv.org/abs/2608.10584)

**<font color=#1a73e8>作者：</font>** Xiaokang Qu, Yiting Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scholar assessment plays a fundamental role in faculty recruitment, funding allocation, academic promotion, and talent discovery. Existing scholar assessment methods predominantly rely on bibliometric indicators and reputation proxies, while recent large language model (LLM)-based approaches mainly focus on evaluating individual research papers rather than comprehensively assessing scholars. We argue that scholar assessment should be formulated as an evidence-driven reasoning problem that jointly considers intrinsic research quality and externally verifiable scholarly behavior. To this end, we propose HexEval, an evidence-driven hexagonal framework for multidimensional scholar assessment. HexEval explicitly organizes scholar assessment into two complementary evidence layers. The intrinsic layer evaluates anonymized representative works along three dimensions, namely research rigor, methodological innovation, and scientific contribution, whereas the external layer characterizes scholars through knowledge translation, research coherence, and academic impact using heterogeneous evidence collected from GitHub, Lens, OpenAlex, and other publicly verifiable sources. Instead of producing opaque aggregate scores, HexEval preserves intermediate evidence, dimension-specific rationales, and verification signals throughout the evaluation process, enabling interpretable and auditable scholar profiles. Experiments across all six dimensions show dimension-dependent agreement with human or external reference criteria: structured calibration improves absolute agreement for intrinsic quality, while the external modules recover broad trajectory and ordinal impact signals. These results support evidence-driven reasoning over heterogeneous scholarly evidence as a promising paradigm for auditable AI-assisted scholar assessment, while exposing the coverage and attribution limitations of public scholarly data.

---


### 98. [Compute-Optimal Is Not Cluster-Optimal: Systems-Aware Scaling for Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.10605)

**<font color=#1a73e8>作者：</font>** Soumajyoti Sarkar, Yuxin Tang, Sheng Zha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In large-scale pretraining, the algorithm, architecture, and systems decisions are conventionally made in disconnected stages. A scaling law stage selects an architecture and training recipe, optimizing loss under compute constraints, and a separate systems stage then optimizes the implementation for hardware efficiency. In this work, we develop MOSAIC, which formulates model architecture and systems co-design as an optimization problem. MOSAIC couples a predictive scaling law with a calibrated performance model that estimates Model FLOPs Utilization (MFU), communication cost, memory footprint, and the best parallel layout. We instantiate the framework for sparse Mixture-of-Experts (MoE) language models, where expert count, routing sparsity, and other MoE layer dimensions affect both the loss and systems efficiency. We fit a scaling law on sparse MoE models trained on text data, whose scaling dimensions include the sparsity factor, which is the fraction of model parameters inactive per token in a forward pass. The scaling law sweeps in our work span active parameters from $104$ million to $2.7$ billion and total model sizes reaching $79$ billion parameters. We show that, within the calibrated sparsity range, an efficiency-agnostic model-FLOPs budget admits no interior optimal sparsity. The fitted loss decreases monotonically with sparser models and the compute optimum lies at the upper boundary of the data support. An optimal sparsity in MoE models instead emerges under the cluster's systems constraints, as captured by MOSAIC. Our results argue for a shift towards unified architecture and systems co-design for frontier language model training.

---


### 99. [ASR-Roundtrip Evaluation Can Mask Context- and Convention-Dependent Reading Errors in Chinese News TTS](https://arxiv.org/abs/2608.10606)

**<font color=#1a73e8>作者：</font>** Shijun Luo, Lizhi Wan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ASR-roundtrip evaluation is widely used as a scalable proxy for text-to-speech (TTS) intelligibility, but it can produce false negatives for reading errors perceived by listeners. We study Chinese news TTS spans whose correct reading depends on context or domain conventions, such as sports scores, aircraft models, technical units, and membership names. In these cases, Raw TTS can choose a plausible but wrong reading while ASR transcribes the audio as the intended or surface-correct text. A targeted audit over 110 high-risk MiMo TTS cases, reported with a complete denominator, confirms 46 masked false negatives, 9 exposed TTS errors, and 55 cases with no Raw TTS error. A span-isolation diagnostic re-exposes 18/46 previously masked errors. A Raw-only CosyVoice audit on the same targeted pool confirms 51 masked cases. Across the 97 TTS-specific audio files labeled confirmed masked across the two audits, Qwen3-ASR surface-recovers 40 cases, whereas Paraformer does so in only 2. The results suggest that ASR-roundtrip is useful for screening but insufficient as standalone ground truth for Chinese news reading-risk evaluation.

---


### 100. [Trigger the Straggler: Load Hijack on Mixture-of-Experts LLMs](https://arxiv.org/abs/2608.10614)

**<font color=#1a73e8>作者：</font>** Rui Zhang, Wenbo Jiang, Hongwei Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Expert parallelism (EP) is a common strategy for serving large Mixture-of-Experts (MoE) models across multiple GPUs by distributing experts among devices. Router decisions then determine both which experts process each token and which GPUs execute the resulting work. This procedure exposes a supply-chain attack surface in the serving schedule. We introduce Load Hijack, in which a malicious model provider modifies only a checkpoint's router weights, distributes the poisoned checkpoint, and retains a private trigger. When the trigger appears, the poisoned router concentrates token-to-expert assignments on experts co-located on one GPU. The resulting load makes that GPU a straggler and forces peer devices to wait, while routing on ordinary inputs remains near the clean reference. We find this conditional behavior difficult to achieve because an objective that rewards target-expert use on triggered inputs can also bias ordinary-input routing toward the same experts. To resolve this conflict, Load Hijack employs a three-stage optimization procedure that produces strong trigger-dependent concentration while keeping ordinary-input routing close to the clean reference. Across three MoE families and four corpora, Load Hijack directs 92.3% to 95.6% of triggered token assignments to the target experts. In live EP serving, triggered traffic produces 1.43x the time-to-first-token and 0.86x the throughput measured under ordinary traffic. These results show that poisoned routers can act as trigger-controlled device schedulers and motivate checkpoint audits of routing and runtime load.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-184](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
