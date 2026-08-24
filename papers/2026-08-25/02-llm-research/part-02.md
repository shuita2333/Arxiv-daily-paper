# 🧠 大模型相关研究 | 2026年08月25日

> 本类共 **170** 篇论文：已确认 **154** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-170](./part-04.md)

---

### 51. [Disentangling Threads: Exploring the Potential of LLM-Supported Discussion Forum Analysis for Community Insight](https://arxiv.org/abs/2608.20591)

**<font color=#1a73e8>作者：</font>** Tony W. Li, Zhiqing Wang, Thanh-Nha Tran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Online discussion forums enable people from diverse backgrounds to share ideas, feedback, and perspectives. These organic discussions can help researchers understand communities' collective viewpoints, but insights are often difficult to uncover given their freeform reply structure. Large language models (LLMs) support qualitative text analysis but can misalign with researchers' analytical intent and miss key insights. To inform design considerations for forum sensemaking tools, we manually analyzed a forum discussion, synthesized an exploratory analysis framework from relevant literature, built a design probe, and interviewed 21 researchers to uncover perceived opportunities and barriers with LLM representations of collective discussions. We provide recommendations for community sensemaking tools to support flexible analytical goals grounded in raw user data and enable follow-up research processes, while balancing anonymous free expression with the desire for contextual information on commenters.

---


### 52. [JuryProbe: An Empirical Consensus-Risk Diagnostic for Routing Reference-Free Factuality Judge Panels to Grounded Verification](https://arxiv.org/abs/2608.20607)

**<font color=#1a73e8>作者：</font>** Tianxin Zhou, Ruixi Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Panels of inexpensive LLM judges increasingly make accept-or-escalate decisions. In factuality settings, accepting a claim because several reference-free judges agree can create a hidden risk: agreement may reflect shared false-negative blind spots rather than independent evidence. We introduce JuryProbe, an empirical consensus-risk diagnostic for reference-free factuality judge panels, paired with a calibration-based routing policy. JuryProbe estimates consensus risk from a labeled calibration probe using false-negative-only (FN-only) judge correlation and false-consensus lift; when flagged high-risk, reference-free majority accepts are routed to the same judges with trusted references. On audited FEVER corruptions, reference-free panels show correlated false negatives (FN-only correlations 0.402 and 0.368; lifts 3.13x and 18.13x), while unanimous false consensus drops to zero under a trusted-reference best-case diagnostic on both minimal-pair and non-minimal-pair evidence. In flagged settings, the routed policy is by construction equivalent to grounding every reference-free majority accept (verified in 34/34 splits): improvement comes from accept-conditioned grounding, while the diagnostic determines whether to activate it. A fixed, pre-specified rule flags 8-10 of 10 splits across synthetic, benchmark-authored, and scientific families and 0 of 10 on a negative control, where standing down avoids 28% of reference acquisitions at a 0.004 increase in false accepts. False-accept reduction persists under weak BM25 retrieval at substantial coverage cost, while stale stand-down labels require periodic recalibration. JuryProbe provides no formal risk guarantee and does not establish reliable stand-down on natural panels; its supported contribution is an empirical diagnostic of high-risk panel error dependence.

---


### 53. [Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills](https://arxiv.org/abs/2608.20614)

**<font color=#1a73e8>作者：</font>** Christopher Kevin, Narendran Raghavan, Jean-Francois Puget 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise agent programs are moving from prototypes into production, where reusable skills, tools, and workflow packages must be reviewed with evidence rather than prose. Current gates often scan these artifacts for structure, style, and security, but they do not answer the deployment question: does the capability package help a live agent complete enterprise tasks under the same model, sandbox, and grading policy?
We present ACES (Agentic Continuous Evaluation of Skills), a repository-native framework for evaluating skills and product capability packages as executable agent artifacts. ACES runs paired live trials with and without a target skill, normalizes trajectories into the Agent Trajectory Interchange Format (ATIF), grades six default runtime metrics, and reports Skill Lift: the target skill's added value for a fixed task, harness, workspace, and scorer. The same protocol supports product-owned task suites that compare baseline, skill, bundle, team-skill, and plugin targets.
On 145 real skills from internal enterprise repositories and public catalogs, scan-only gates surface useful authoring issues but measure complementary facets (structural versus LLM-judge Spearman $\rho = 0.14$). Across 947 scored paired cases from 58 of 64 production skills and four primary harnesses, mean composite Skill Lift is 0.2134 (95\% paired-case CI [0.1967, 0.2301]); mean outcome-only lift, the average of accuracy and goal accuracy, is 0.1799. Composite lift is positive in 72.8\% of paired cases. The largest process-metric gains appear in skill execution, behavior check, and skill efficiency---signals about discovery, routing, workflow following, and tool use that document scans cannot observe. An open-source implementation of the methodology is available in NVIDIA SkillEvaluator.

---


### 54. [Dual-Cache Latent Space Communication between Heterogeneous Language Models](https://arxiv.org/abs/2608.20617)

**<font color=#1a73e8>作者：</font>** Jiyao Liu, Qi Zhang, Yaoyi Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems split work across models, so answering often requires knowledge that sits in another agent's context: a Sharer has encoded information that a Receiver needs to complete its task. They usually communicate by exchanging text, which puts autoregressive decoding on the critical path and reduces the exchange to a discrete message written without sight of the receiver's state. Recent latent protocols instead translate the sharer's key-value (KV) cache into the receiver's: C2C supports heterogeneous models but requires both to read the same input, while LCF-X removes this shared-context requirement through position-free sharer-cache pooling. Three restrictions remain: LCF-X compresses the sharer alone, supplies the same layer-local summary to every receiver position with no joint cross-layer memory to retrieve from, and assumes matched layer count and KV geometry. We introduce XKV, which lifts all three: learned-query attention pools both caches; self-attention over receiver-aligned layer tokens, with a learned layer map reconciling different depths, mixes the pooled summaries into a compact joint memory; and a shared position decoder lets every raw receiver cache position retrieve its own per-head-gated residual in the receiver's native KV geometry. Both models stay frozen and may differ in family, depth, KV-head count, head dimension, and tokenizer; only the translator is trained. Across 45 dataset-model-pair settings (six heterogeneous and three same-model ordered pairings, five datasets), XKV attains the highest macro score and best average rank, improving on LCF-X on every dataset (by 4.6 exact-match and 4.2 F1 points on ROPES) and surpassing text communication on four of the five, while training 76% fewer parameters and translating a cache pair 10.3x faster (5.8 vs. 59.9 ms); end to end, XKV is 26% faster than LCF-X and 6.8x faster than text communication.

---


### 55. [Applying Anthropic Primitives at Large Enterprises: Harness Paradigm for Knowledge Work](https://arxiv.org/abs/2608.20622)

**<font color=#1a73e8>作者：</font>** George Juraj Salapa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier models have collapsed the cost of writing custom code: a niche problem a specialist sees in their own domain now costs an afternoon. The cost of reviewing and maintaining that code hasn't collapsed. Each solution drifts from the next; understanding one means reading its codebase from scratch. Large enterprises build something centrally governed instead: at worst an off-the-shelf product, at best a graph-orchestration framework wired bespoke per use case, or a low-code platform used as the orchestrator. These are custom every time and limited in scope. Enterprises don't weigh a third option that escapes both constraints: the harness paradigm.
Recent work treats the coding-agent harness as enterprise infrastructure rather than a coding tool, converging on three findings: harnesses suffice at the task level and outperform more elaborate architectures on enterprise work (arXiv:2604.00073, arXiv:2604.13107); harness choice accounts for most of the variance in agent benchmark results, more than model choice does (arXiv:2605.23950); and the gap between that finding and enterprise adoption is governance (arXiv:2605.10223, arXiv:2605.18747).
We propose an architecture that closes that gap. One harness runs unmodified as the backbone; the code stays identical across every deployment, so reviewing what gets built collapses to reading its instructions file. Section 4 gives four mechanisms: credential-scoped tooling, where each backend gets one generic request tool and a scoped credential instead of a hand-built method; authorization logic outside the harness, so one artifact runs as a cron backbone, a chat-surface engine, and a terminal tool; registration is a side effect of pushing code, collapsing an audit a review of a text file.
Built on microcc (<this https URL), our reference harness.

---


### 56. [When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation](https://arxiv.org/abs/2608.20627)

**<font color=#1a73e8>作者：</font>** Lauren Pothuru  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic retrieval-augmented generation (RAG) interleaves retrieval, reasoning, and answer generation across multiple hops. A retrieval error at hop 1 can surface only as a wrong answer at hop 3, while later retrieval can also repair the trajectory. This paper introduces AgenticRAG-FP, an interventional benchmark for causal failure attribution in agentic RAG. The benchmark injects a certified fault at a specified hop, re-executes the downstream trajectory, and evaluates diagnosers against the known intervention. Its central question is whether a post-hoc trace still identifies the injected hop after the suffix changes. In the completed strict dense Claude Haiku 4.5 sweep on 80 three-hop MuSiQue questions, coverage-based diagnosis is 0.91 at hop 1 and 0.00 at hops 2 and 3 (n=43,36,21 failed trajectories). A smaller content-corruption study changes an answer-bearing or bridge fact in topically intact evidence. At depth 2, where 18 failed cases remain after filtering, coverage-based diagnosis is 0.00 and a frozen-hop counterfactual probe is 0.67 in an exploratory pooled comparison. Depth-3 content estimates are descriptive only because they contain three failed cases. These results make propagation depth an explicit evaluation axis for diagnosing agentic RAG failures while distinguishing broad evidence of post-hoc signal loss from small-sample method comparisons.

---


### 57. [Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.20631)

**<font color=#1a73e8>作者：</font>** Quang Dao, Purvi Kathalkar, Kenneth Eaton  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have demonstrated the ability to solve multi-step tasks requiring planning, tool use, and external information access, yet growing execution histories increase inference cost and expose reasoning to outdated, irrelevant, or misleading information, potentially degrading reasoning quality. Existing memory approaches organize or compress execution histories but provide limited mechanisms for deciding which memories remain active. We introduce the, a hierarchical memory system that organizes execution into tasks, subtasks, and actions while assigning each memory a dynamic retention score. Event-based updates and selection-based decay revise these scores, allowing WMT to preserve useful information, fold completed trajectories, suppress low-utility content, and retain access to folded context. We evaluate WMT on GAIA-Text using Qwen3-8B, Gemma 4 E4B, and Llama-3.1-8B, with ablations and memory-poisoning experiments. Relative to linear memory, WMT improves accuracy by an average of 9.97 percentage points while reducing prompt-token usage by 32.8%. Memory-poisoning experiments show that WMT limits the persistence and propagation of unreliable information. Our results suggest that effective long-horizon agent memory depends less on storing more information than on deciding which information should remain active.

---


### 58. [AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at scale](https://arxiv.org/abs/2608.20634)

**<font color=#1a73e8>作者：</font>** Minbyul Jeong, Chanwoong Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents learn to act through interaction with environments, yet the environments used for training are often manually constructed or synthesized around predefined tasks and benchmarks. This task-centric paradigm makes it difficult to scale environments that reflect realistic and evolving workflows where diverse tasks can naturally emerge from the underlying world. We introduce AgentMercury, a scalable framework for synthesizing executable environments from high-level business scenarios. Rather than constructing an environment for a specific task, AgentMercury first instantiates a persistent world with entities, services, tools, state, and executable cross-service invariants, from which diverse tasks and interaction trajectories can subsequently emerge. We construct 4,783 executable environments spanning 14 industries and 50 countries, and use them as training substrates for reinforcement learning. Despite being generated without targeting the evaluation benchmarks, policies trained on these business-oriented environments improve substantially on both enterprise workflows and out-of-domain benchmarks spanning reasoning, coding, scientific computing, and tool use. In our experiments, Qwen3.5-4B improves from 12.3 to 15.7 on EnterpriseOps-GYM and from 45.9 to 56.0 on AIME26 after training on AgentMercury environments. We further show that the construction process itself can be learned: fine-tuning Qwen3.5-35B-A3B on construction traces increases executable-world authoring success from 3.3% to 83.3% on held-out business scenarios. These results show that scenario-grounded environments can provide useful and generalizable learning signals beyond benchmark-specific training, while their construction can itself become a learnable capability.

---


### 59. [ARQ: Agentic CodeQL Query Refinement for C/C++ Vulnerability Detection](https://arxiv.org/abs/2608.20637)

**<font color=#1a73e8>作者：</font>** Chunyi Wang, Yunfei Ke, Junfeng Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static analyzers have been widely adopted for vulnerability detection in C/C++ programs. Query-based static analyzers (e.g., CodeQL) encode vulnerable code patterns in detection queries and match them against source code. However, existing queries still suffer from false positives (FPs, incorrectly flagging benign code as vulnerable) and false negatives (FNs, missing real vulnerabilities). We present ARQ, an agentic framework that automatically refines C/C++ CodeQL queries using execution-grounded evidence from synthesized C/C++ programs. Our key insight is that a synthesized program exposes a query's weakness whenever its execution disagrees with the query's verdict. If the program is genuinely vulnerable but the query stays silent, the query has an FN weakness; if the program is safe but the query fires anyway, it has an FP weakness. ARQ then runs an LLM-based refinement loop that repairs the query using these disagreements as ground truth. Unlike previous query refining methods, ARQ requires no labeled datasets, no commit history, and no vulnerability-specific templates. We demonstrate the effectiveness of ARQ by refining 12 official CodeQL queries using three commercial LLMs (GPT-5.4, Claude-Sonnet-4.6, and Gemini-3.5-flash). We compare both ARQ-refined and original CodeQL queries on the Juliet v1.3 and FormAI v2 datasets and show that ARQ-refined queries detect substantially more true positives, by up to 119.8\%, with a Precision of at least 98.0\% throughout. ARQ successfully fixed three unresolved GitHub issues raised in the official CodeQL query repository that had remained open for as long as \textit{27 months}. The refined queries also exposed two previously undiscovered bugs in the real-world libraries libpng and zlib.

---


### 60. [The Claws in Plain Sight: Unauthorized Context Disclosure through LLM Agent Tool Calls](https://arxiv.org/abs/2608.20658)

**<font color=#1a73e8>作者：</font>** Ben Dong, Zhonghao Guo, Tianyi Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents routinely construct tool-call arguments from user profiles, conversation history, retrieved documents, and prior tool results. However, legitimate access to contextual information does not imply authorization to transmit that information for every purpose or destination. We present Claw in Plain Sight, an authority- pressure attack in which task-adjacent content frames protected attributes as operationally or procedurally required, causing a model to include them in otherwise valid generated arguments. We evaluate Claw in Plain Sight using a controlled synthetic benchmark that crosses six pressure levels with four privacy-policy levels across five DeepSeek and Claude model configurations, producing 120 calls. Across the complete pressure-policy matrix, session-level disclosure rates range from 20.8% to 75.0% among the tested models. Stronger privacy instructions reduce aggregate disclosure but do not eliminate it consistently across models, showing that prompt-level policies do not provide a portable enforcement boundary. Our experiments use only synthetic profiles and capture proposed arguments locally; they measure policy-violating generation at the context-to-argument boundary, not completed network exfiltration or leakage from deployed users. These findings motivate purpose- and destination-aware inspection of generated tool arguments before execution.

---


### 61. [Auditable by Construction: An Ontology-Driven Framework for Trustworthy LLM Analytics in Enterprise Finance](https://arxiv.org/abs/2608.20661)

**<font color=#1a73e8>作者：</font>** Sergiy Lunyakin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise adoption of large language models in finance is constrained less by fluency than by trust: in Financial Planning and Analysis (FP&A) and other regulated workflows, an answer is usable only if it is traceable to authoritative sources and auditable after the fact. This paper argues that retrieval-augmented generation for enterprise finance should be evaluated on auditability alongside accuracy, and presents the Knowledge-Driven Analytics Framework (KDAF), which builds ontology-driven knowledge systems through six iterative stages and retrieves evidence via Context-Aware Relevance Propagation (CARP), so that every retrieved fact carries its relationship type, confidence, and source lineage.
An evaluation on FinanceBench (145 questions) compares KDAF against zero-context inference, BM25, concept-weighted lexical retrieval, and ungrounded graph traversal. First, retrieval is necessary: zero-context inference reaches 4.1% correctness against 10-12% for retrieval-augmented conditions. Second, on answer correctness the retrieval conditions are statistically indistinguishable (KDAF vs BM25: -0.007, 95% CI [-0.021, 0.000]), so accuracy alone does not justify structured retrieval here -- a negative result we report explicitly. Third, on auditability the ordering reverses: KDAF attains the highest citation traceability F1 (0.515), exceeding ungrounded traversal by +0.027 (CI [0.006, 0.050]) and BM25 by +0.052 (CI [0.024, 0.083]), intervals excluding zero. Graph-structured retrieval also admits no evidence from outside the question subject entity (0 of 426 items, against 16.8% and 20.2% for lexical baselines), and every selected item resolves to a complete provenance chain. We argue that auditability, not accuracy, is the axis on which ontology-grounded retrieval earns its cost.

---


### 62. [Why2Speak: Faithful Reasoning for Abstaining Action Policies](https://arxiv.org/abs/2608.20670)

**<font color=#1a73e8>作者：</font>** Shreya Mendi, Brinnae Bent  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many agentic systems must repeatedly choose between acting and abstaining, making faithful reasoning important for oversight: an explanation is useful only if it reflects the computation that produced the action. We study this problem through intervention timing in multi-party conversation, where an assistant must decide whether to speak or remain silent. This setting exposes class imbalance, asymmetric action costs, and the possibility that exposing reasoning changes the policy being audited. Using Qwen3-8B, decoded with or without chain-of-thought reasoning, we compare direct decision policies, reasoning policies, supervised fine-tuning, and reinforcement learning. We find a capability-auditability tradeoff: the strongest direct policy achieves higher quality but exposes no reasoning to inspect, while the reasoning policy provides a trace at the cost of lower performance, particularly recall of true intervention opportunities. Supervised fine-tuning either suppresses reasoning or preserves it without improving decision quality, while reinforcement learning also fails to improve the reasoning policy. We identify one mechanism underlying this failure: group relative objectives provide no learning signal on confidently wrong prompts when sampled rollouts all select the same action. Controlled activation probes and behavioral ablations show that standard faithfulness methods can overstate evidence that exposed reasoning reflects the underlying decision process. Probability-based metrics saturate under confident decisions, probes are vulnerable to class imbalance and textual leakage, and reasoning ablations can confound reasoning content with changes in inference mode. Together, these results show that exposing reasoning can change an agent's action policy rather than simply make it observable. We provide controls for evaluating reasoning-based oversight of agents that can act or abstain.

---


### 63. [VortexChat: An agentic framework for autonomous multi-objective integrated photonic design](https://arxiv.org/abs/2608.20688)

**<font color=#1a73e8>作者：</font>** Faqian Chong, Yulun Wu, Shilong Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The advancement of modern integrated photonics is frequently bottlenecked by device design workflows that rely heavily on manual simulation and expert intuition. While inverse design offers an alternative, it remains constrained by expert supervision and a lack of end-to-end automation. To address these issues, we present VortexChat, an agentic framework for the autonomous, end-to-end inverse design of integrated photonic devices directly from natural language specifications. VortexChat couples a large language model (LLM) decision agent with topology generation, gradient-based refinement, and full-wave electromagnetic simulation. This closed-loop architecture enables the system to iteratively decompose design objectives, orchestrate computational tools, and update strategies based on feedback with minimal human intervention. Constrained by the absolute metrics of the Vortex100 Benchmark, VortexChat autonomously generates devices that strictly meet all predefined performance thresholds without any human-in-the-loop. As an experimental demonstration, we fabricated a broadband terahertz perfect vortex beam multiplexer, autonomously designed by VortexChat, with measurements confirming high-efficiency operation, high mode purity and low inter-channel crosstalk in agreement with full-wave simulations. These results demonstrate that an LLM agent can assume key aspects of expert decision-making in photonic inverse design while maintaining physical fidelity and fabrication feasibility, providing a scalable route towards autonomous design of complex integrated photonic systems.

---


### 64. [ArtiMo: Agent-Driven Articulated Mesh Animation](https://arxiv.org/abs/2608.20699)

**<font color=#1a73e8>作者：</font>** Chunyu Zou, Peng Dai, Yi-Hua Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Animating articulated 3D meshes via text requires satisfying strict kinematic constraints, modeling causal interactions between parts, and achieving instruction fidelity. Due to the absence of task-specific training data and explicit articulation supervision, existing data-driven mesh animation methods are largely inapplicable to this setting. To address this, we propose ArtiMo, a novel agent-driven framework for text-guided articulated mesh animation. Operating in a zero-shot manner, ArtiMo develops an agentic pipeline powered by Large Language and Vision-Language Models (LLMs/VLMs) to orchestrate motion generation. By synergizing the explicit kinematic constraints of URDF with the agent's reasoning and planning capabilities, it effectively produces causally coherent part motions and interactions without requiring model fine-tuning. To ensure motion correctness, the agent additionally utilizes a visual self-improvement mechanism: generated animations are rendered into compact keyframes and motion cues, enabling the VLM to iteratively diagnose and correct errors. Furthermore, we contribute a new benchmark dataset spanning 21 articulated object categories, featuring high-quality motion annotations enriched with causal relationships. Extensive experiments demonstrate that ArtiMo significantly outperforms baselines, particularly on complex, causally driven motions. The project page is available at this https URL.

---


### 65. [AsmEvo: Agentic Assembly-Level Optimization of AMD GPU Kernels with Functional Equivalence Verification](https://arxiv.org/abs/2608.20711)

**<font color=#1a73e8>作者：</font>** Ji Liu, Puyuan Yang, Rongzhang Zheng 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-performance ML systems increasingly rely on GPU kernels whose editable source is unavailable, generated, or too distant from final machine code to expose remaining optimizations. Existing LLM kernel optimizers and autotuners mainly operate on CUDA, Triton, HIP, or tensor-program source and validate against reference implementations. We study a stricter setting: optimizing an already compiled AMDGPU code object, where the deployed binary is the only behavioral oracle.
We present AsmEvo, an agentic assembly-level optimizer for AMD GPU kernels. Given an AMDGPU code object K0, AsmEvo reconstructs a reassemblable representation, proposes low-level edits with a long-horizon agent, rebuilds an ABI-preserving optimized object, and accepts candidates only after differential verification against K0 under identical launches. AsmEvo combines code-object recovery, metadata-aware rebuilding, profiling-guided hot-window editing, correctness-gated timing, and conservative in-place patch fallback.
We conduct extensive experiments with AsmEvo on various AMD GPU kernels. On MI308X, AsmEvo improves 29 of 30 selected KernelBench kernels, reaching 1.35x geometric-mean and 3.88x maximum speedup. On MI300X production workloads, it improves all evaluated AITer binaries and vLLM/SGLang Triton assembly kernels, reaching 1.09x/1.31x and 1.18x/1.34x geometric-mean/maximum speedups, respectively, while preserving functional equivalence.

---


### 66. [AGIDefect-4K: A Richly Annotated Dataset for AI-Generated Image Defect Detection, Localization and Explanation](https://arxiv.org/abs/2608.20713)

**<font color=#1a73e8>作者：</font>** Xiangfei Sheng, Weidong Zou, Tianjiao Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative AI can now produce highly realistic images, yet current models still exhibit subtle but critical defects that undermine their reliability. While existing AI-generated image (AGI) evaluation benchmarks have made notable progress, comprehensive AGI defect diagnosis remains underexplored. To bridge this gap, we introduce AGIDefect-4K, a richly annotated dataset of 4,000 images from 15 state-of-the-art generative models spanning both open-source and closed-source systems. AGIDefect-4K features hierarchical defect annotations: (1) detection labels identifying whether defects exist, (2) pixel-level segmentation masks localizing defective regions, and (3) detailed textual explanations characterizing defect types and their perceptual impact. Each image is further annotated with an overall quality score. Building on this, we present AGIDA (AGI Defect Assistant), a baseline framework leveraging Multimodal Large Language Models (MLLMs) for joint defect detection, localization, explanation, and quality prediction. Comprehensive benchmarking on AGIDefect-4K reveals that AGI defect understanding remains challenging, underscoring the value of this dataset. The dataset is publicly available at this https URL.

---


### 67. [DirEAG: Dirichlet Evidence Aggregation for Calibrating Verbalized Confidence in Mathematical Reasoning](https://arxiv.org/abs/2608.20717)

**<font color=#1a73e8>作者：</font>** Haorui Xu, Yuzhou Zhu, Liyuan Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable confidence estimation is essential for using large language models in mathematical reasoning, but black-box verbalized confidence is difficult to calibrate. When the same problem is queried under multiple confidence-steering prompts, the resulting answer-confidence observations contain useful uncertainty information, yet their scales may shift across steering levels, models, and datasets. Existing black-box uncertainty methods often rely on answer agreement, sample consistency, or entropy, which describe output variation but do not model the numerical meaning of self-reported confidence. Conversely, direct averaging or heuristic aggregation of elicited confidence cannot learn prompt- and task-dependent bias. We propose DirEAG, a Dirichlet Evidence Aggregation method that converts each elicited answer-confidence observation into calibrated soft evidence over generated candidate answers and an additional null state, allowing the model to represent cases where none of the candidates is correct. Experiments on GSM8K, SVAMP, and GSM-Hard with Qwen, Mistral, and Gemma models show that, compared with direct confidence averaging and heuristic confidence-steering aggregation, DirEAG often achieves better calibration while maintaining competitive answer selection. Ablations further reveal that evidence aggregation and final binary calibration address distinct parts of the calibration problem.

---


### 68. [AffordAny: Open-World 3D Affordance Grounding from Monocular RGB Images via Vision-Language-Guided Geometric Reasoning](https://arxiv.org/abs/2608.20720)

**<font color=#1a73e8>作者：</font>** Junqi Wu, Kaihua Tang, Xuanwen Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world 3D affordance grounding requires localizing functional object parts in 3D given free-form language queries. Existing methods typically assume pre-built object-centric 3D geometry and closed affordance ontologies, limiting deployment from raw RGB observations. We present AffordAny, an end-to-end framework that uses one monocular RGB image to construct large-scale text-conditioned 3D part supervision, ground affordances with a frozen vision-language model (VLM) guided decoder, and improve open-world generalization through pseudo-label self-training. Our automated pipeline produces a benchmark of 5,334 objects and 10,633 part-level samples spanning 473 categories, an order-of-magnitude increase in categorical diversity over prior work. The decoder progressively fuses frozen Cosmos-2B features with 3D geometry through spatial projection, instruction-conditioned semantic compression, and bidirectional geometry-semantics interaction. Minimal-perturbation pseudo-label self-training further adds new objects without human annotation. Under a systematic generalization protocol evaluating unseen objects, unseen categories, and unseen instruction paraphrases, our approach achieves 0.428 IoU on unseen objects and 0.315 IoU on unseen categories after self-training, with unseen-category mIoU improving by 6.3% relative (p<0.01) and an instruction sensitivity gap of only 0.105, demonstrating effectiveness and robustness of our method.

---


### 69. [Calibrating Criterion Revision in LLM Agents: Failure Modes and a Trace-Anchored Protocol](https://arxiv.org/abs/2608.20729)

**<font color=#1a73e8>作者：</font>** Guodong Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents can improve after failure or carry text across episodes without revising what counts as success. We study the narrower attribution problem of criterion revision: when criterion K0 accepts an outcome violating a broader commitment B, what observations justify saying that the system formed and persistently used K1? We require five non-compensatory conditions: criterion-failure detection, a model-emitted proposal, new-episode transfer, intervention sensitivity on the claimed carrier, and preservation.
We evaluate CMB-0.1 on twelve cross-domain cases and four arms: stateless inference, append-only history, model-generated but harness-committed state, and evaluator-written oracle state. Seven mechanism fixtures yield 84 deterministic scorer trials; four local quantized artifacts yield 96 calls and 192 model-case-arm trials. No model trial satisfies all five conditions, but this zero does not establish general capability absence. Eleven calls remain invalid after one retry; several commitments disclose the target distinction; the harness performs commits; deletion reuses a stateless call; and conflict changes multiple factors. Qwen2.5-7B answers every transfer and preservation item without revision state, exposing zero-state reconstruction.
These failures make CMB-0.1 an instrument-calibration result rather than a model ranking. We derive a prospective, trace-anchored CMB-0.4 protocol requiring concealed transfer, explicit WRITE/NO-WRITE/ESCALATE actions, a separately logged policy-selected commit, matched interventions, repeated hidden items, and a frozen executable oracle. It is a successor design, not a completed confirmatory result. The paper contributes a measurement chain, an empirical diagnosis of its first implementation, and a more discriminating protocol for future tests of criterion revision.

---


### 70. [Uncovering and Understanding Hidden Dependencies in the LLM API Reseller Ecosystem via Prefix-Cache Side Channels](https://arxiv.org/abs/2608.20732)

**<font color=#1a73e8>作者：</font>** Zimo Ji, Xin Wei, Congying Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM API resellers have become an important access layer to modern LLM services. However, multi-level resale creates an opaque supply chain: a user's request may traverse undisclosed upstream resellers, each of which can inspect or modify prompts and responses, inducing ecosystem-level confidentiality and integrity risks. Existing studies audit individual resellers, but provide little visibility into hidden dependencies across resellers. We present CacheTracer, the first API-only measurement of such hidden dependencies. Our key insight is to exploit prefix-cache reuse as a side channel to measure dependency via cache-reach relations. CacheTracer operationalizes this insight with two primitives: Flood populates fresh cache state through one endpoint, and Prove probes whether another can reuse it while excluding probe-created hits.
We then conduct a real-world measurement study with CacheTracer on 39 reseller endpoints, sending 1.1 million API requests across 636 endpoint pairs. Our measurements reveal a deep, concentrated cache-reach structure: 37.1% of measured pairs exhibit shared cache reach, the containment order spans seven layers, and one cache reach is contained within at least 31 of other nodes. We further find that the recovered structure is model-specific. We also evaluate the validity of CacheTracer through both real-world consistency checks and controlled experiments. The results show its high reliability and accuracy. These findings reveal substantial hidden dependencies among seemingly independent API resellers. Such deep and concentrated dependencies can create a large potential blast radius, where a confidentiality or integrity failure along a common upstream path may affect users across multiple downstream resellers.

---


### 71. [ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation](https://arxiv.org/abs/2608.20735)

**<font color=#1a73e8>作者：</font>** Siyuan Ma, Yutian Zhang, Boshi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Manipulating moving objects requires a policy to anticipate contact events, yet vision-language-action (VLA) policies are commonly fine-tuned from the current observation alone. World action models (WAMs) learn predictive dynamics, but running a video-scale teacher or explicitly imagining future frames at deployment is costly. We introduce ForeTime-VLA, a dense pi0.5 policy that distills a future-aware, action-equivalent representation from a frozen Fast-WAM-derived teacher while remaining causal at inference. Offline, current and future video latents are compressed into a whitened 64-D target. Online, an eight-frame history encoder predicts this target together with manipulation phase and normalized time-to-transition. Four future tokens and one phase token condition the VLM prefix, while the predicted future and transition horizon condition the action expert. Training retains the original flow-matching action target and adds cosine, relational geometry, phase, time-to-transition, and action-equivalence objectives. On a deduplicated conveyor-belt dataset, we compare 40k-step checkpoints on 768 matched windows per split. Test MAE decreases from 0.134119 to 0.130593 (2.63%; paired-bootstrap 95% CI: 0.82-4.48% improvement), and test L2 decreases by 3.02%, at a 2.46-2.93% latency cost. In quantitative real-robot evaluation, ForeTime-VLA achieves 81.1% stationary and 58.9% slow-moving grasp success, exceeding the next-best reference by 12.2 and 22.2 percentage points, respectively. Across three belt speeds, it completes 44/90 grasps versus 23/90 for pi0.5, including 11/30 versus 2/30 at fast speed. The agreement between offline orientation gains and reduced real-robot contact-pose failures supports causal future-token distillation as an effective way to improve dynamic manipulation without deploying the world-model teacher.

---


### 72. [Is Multimodal Speculative Decoding Ready for Diffusion-Based Parallel Drafting? A Survey and Empirical Diagnosis](https://arxiv.org/abs/2608.20743)

**<font color=#1a73e8>作者：</font>** Yantao Li, Huanlin Gao, Fang Zhao 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive generation by allowing a lightweight drafter to propose future tokens while a target model verifies them in parallel. Its lossless guarantee has motivated a line of work that pushes the drafter itself toward parallel generation. The most recent paradigm is block-parallel generative drafting, including diffusion-based methods such as DFlash and DSpark, achieving up to 3.6x speedup on common daily chatting tasks. While this transition is well studied in text-only LLMs, its applicability to multimodal models remains an open question. Existing multimodal speculative decoding efforts focus on input compression, adapter alignment, candidate coverage, or modality-specific verification; however, block-parallel generative drafting remains largely unexplored. To bridge this gap, this paper combines a modality-centered survey with a cross-architecture empirical study to ask: Is multimodal speculative decoding ready for diffusion-based parallel drafting? In this survey, we systematically analyze a wide spectrum of multimodal models, spanning Vision-Language, Video-Language, Audio, and Vision-Language-Action (VLA) architectures, from the dual perspectives of drafting parallelism and cross-modal information interaction. We introduce a unified taxonomy that isolates drafter-side parallelism from orthogonal design choices such as tree construction and verification strategies. Furthermore, we provide a comprehensive empirical comparison of existing methods under varying degrees of parallelism across standardized multimodal benchmarks, including OCR, VQA, visual reasoning, and image captioning. Finally, we summarize the limitations of current approaches, discuss open challenges, and outline promising future directions for this rapidly evolving field.

---


### 73. [Identity-Preserving Text-to-Video Generation via Agentic Enhancement and Semantic Repair](https://arxiv.org/abs/2608.20749)

**<font color=#1a73e8>作者：</font>** Jiayi Gao, Changcheng Hua, Jiaqi Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-preserving video generation aims to synthesize videos that follow natural-language instructions while maintaining the visual identity of a given subject. Recent commercial video generation models have achieved strong visual quality and motion realism, but they still suffer from identity drift, incomplete instruction following, and missing visual details under complex prompts. Since these models are usually closed-source black boxes, directly improving them through parameter optimization is often infeasible. We therefore propose Agentic Enhancement and Semantic Repair (AESR), a lightweight enhancement framework for identity-preserving video generation. To improve prompt construction before generation and mitigate the above failures, AESR introduces a global agentic prompt enhancement module. This module learns model-specific prompting formats from official documentation, acquires human-centered video generation priors from human-interaction data, and accumulates test-domain identity-preserving generation experience into a reusable playbook through an agentic loop. To further repair errors in videos generated with enhanced prompts, AESR introduces a sample-level visual semantic repair module, which uses a VLM to locate erroneous video segments and design repair instructions, edits selected frames into explicit visual references, and guides a video editing model to fix local semantic or identity-related errors. We also adopt a lightweight Mixture-of-Experts selection strategy to choose reliable outputs from different generation and refinement paths. Under the official evaluation protocol of the ACM MM 2026 Identity-Preserving Video Generation Challenge, our system MIPL\_Video ranked first in Track 1, demonstrating the effectiveness of AESR for practical identity-preserving video generation. The code is available at this https URL.

---


### 74. [Natural-Language-Guided Generator-Agnostic Shortlisting for Protein Binder Design](https://arxiv.org/abs/2608.20755)

**<font color=#1a73e8>作者：</font>** Gyubok Lee, Kiwoong Yoo, Jimin Seo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern de novo design workflows generate many candidate protein binders, but wet-lab validation capacity remains limited, making shortlisting a major bottleneck. We study whether LLMs can generate multi-metric ranking policies from precomputed structural-confidence and interface-quality proxy scores. Rather than proposing a new protein binder design pipeline, we focus on post-generation binder shortlisting: selecting the final top-K candidates from already generated binder pools using a shared panel of precomputed proxy scores. On the 10-target held-out split, averaging performance over five sampled global iterative gpt-4o policies reaches 0.589 Recall@10, modestly improving over the strongest single-feature fixed baseline, Protenix binder ipTM, which reaches 0.571 Recall@10. On the 3-target held-out subset comprising Nipah, RBX1, and TREM2, target-conditioned iterative gpt-5.4 policies reach the strongest LLM performance, with 0.519 Recall@10 and 0.583 NDCG@10. These results suggest that LLM-generated ranking policies can act as an interpretable post-generation decision layer for combining heterogeneous proxy metrics to prioritize binders from large candidate pools.

---


### 75. [Fuzzy-MoE: Interpretable Regime-Conditioned Expert Routing for Non-Stationary Multivariate Time Series Forecasting](https://arxiv.org/abs/2608.20761)

**<font color=#1a73e8>作者：</font>** Lan Guo, Jie Xiao, Zhao Su 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In non-stationary multivariate time series, different variables and samples often exhibit heterogeneous latent dynamic states, while existing deep forecasting models usually compress them into a unified end-to-end mapping, leading to suboptimal modeling of time-varying dynamics and limited interpretability regarding which forecasting mechanism is activated under different latent states. To overcome these limitations, we reformulate time series forecasting as a unified framework of latent temporal state identification and interpretable expert routing, and propose Fuzzy-MoE, a fuzzy logic-based dynamic Mixture-of-Experts model. Fuzzy-MoE consists of multiple parallel expert mapping networks and a dual-view fuzzy router. By jointly exploiting local convolutional dynamics and global segmented statistics, the router infers latent temporal states and computes expert activation strengths through learnable Gaussian membership functions, enabling explicit IF-THEN rule-based expert selection. This fine-grained routing strategy allows different variables within the same sequence to activate different experts, effectively capturing heterogeneous temporal dynamics while improving model interpretability. Experimental results on multiple public time series benchmark datasets show that Fuzzy-MoE significantly outperforms mainstream forecasting methods in forecasting accuracy. Moreover, fuzzy memberships and rule activations provide interpretable routing diagnostics, demonstrating the effectiveness of the proposed framework in both forecasting performance and mechanism transparency. Unlike traditional MoE models that use black-box routing, Fuzzy-MoE`s routing is based on clear, interpretable fuzzy rules. This makes the expert selection transparent and traceable.

---


### 76. [CARD: Diagnosing Belief to Action Routing Failures in Vision Language Models](https://arxiv.org/abs/2608.20763)

**<font color=#1a73e8>作者：</font>** Souptik Kumar Majumdar, Fabian Kögel, Andreas Bulling  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Linear probes and activation steering have uncovered that vision-language models (VLMs) internally represent mental states such as agents' beliefs, knowledge, and intentions. However, it is unclear whether and how these representations are used by downstream predictions along these axes. To close this gap, we introduce Cross-Axis Routing Diagnostic (CARD), which steers activations along one axis while measuring the response of a different axis's prediction. Applied to open-weight VLMs on Relay Chain -- a new cooperative grid-world benchmark we propose -- we diagnose a critical routing failure: models fail to incorporate belief representations into their next action prediction, effectively leaving valuable information about their partners unused.

---


### 77. [Beyond Endpoint Gains: A Weight-Delta Audit of Medical Specialization](https://arxiv.org/abs/2608.20768)

**<font color=#1a73e8>作者：</font>** Praphul Singh, Shanu Kumar, Akshat Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Specialist language models are usually understood through endpoint gains: the generalist scores lower, the specialist scores higher, and the difference is treated as evidence of specialization. This leaves the released update itself largely unexamined. We propose a paired weight-delta path audit and apply it to two public, aligned generalist-to-medical-specialist checkpoint pairs: Gemma-3-4B-IT to MedGemma-4B-IT and Qwen2.5-7B-Instruct to HuatuoGPT-o1-7B. In both pairs, the full decoder-side update strongly reconstructs measured medical benchmark movement (0.974 and 1.183 endpoint-normalized retention), making each decoder delta an appropriate substrate for the audit. Yet the movement is not cleanly localized. MLP is the strongest broad component family in both pairs, but mixed off-domain movements, 10-seed matched controls, and endpoint-anchored rollbacks prevent a unique coarse-family explanation. The audit therefore separates update-level reconstruction from component-level explanation. Its claims concern text-only multiple-choice benchmark movement, not clinical validation, repair, or circuit-level mechanism.

---


### 78. [Tree-of-Concerns: Hierarchical Multi-Agent Debate for Unstated-Limitation Extraction in Scientific Critique](https://arxiv.org/abs/2608.20777)

**<font color=#1a73e8>作者：</font>** Sahil Mishra, Niranjan Rajeev, Tanmoy Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As scientific literature grows and papers increasingly under-report limitations, multi-agent LLMs offer a promising approach to systematically uncover these hidden failure modes. Here, we introduce Tree-of-Concerns, a multi-agent framework that deploys specialized skeptic personas, each operating through a category-specific analytical lens, as parallel debate trees to extract unstated limitations from scientific papers. Each persona conducts structured, evidence-grounded argumentation, while a Panel Review mechanism re-evaluates each surviving claim from all five perspectives to correct category drift and severity miscalibration. Through experiments on ToC-Bench, our benchmark of 414 research papers with 1,905 unstated limitations, sourced from reviewer-reported weaknesses and follow-up citation critiques, we demonstrate that ToC improves precision by 79% and coverage by 11% relative to strongest baselines, surfacing specific, evidence-grounded concerns that support reviewers in systematic evaluation.

---


### 79. [Structure for Reading, Prose for Writing: Asymmetric Structural Conditioning in Multi-Agent Document Authoring](https://arxiv.org/abs/2608.20786)

**<font color=#1a73e8>作者：</font>** Cheng Yu, Nikhil Mathew, Zhengjie Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent pipelines that author formal documents must both read a requester's forms and write against them. We report a deployed tender-response system, running an open-weights model under sovereignty constraints, and evaluate it against human-written bids the same organisation actually submitted. On a blind comparison where the system had no worked example available, an LLM judge rated its answers at least as good as the human-submitted answer on $40$ of $55$ ground-truth sections, better on $4$, missing on none, and flagged one unsupported claim in total. Classifying every gap the judge identified shows that $68\%$ were content absent from the system's own sources -- knowledge the human author held and the pipeline was never given -- so only $6$ of the $15$ adverse verdicts involve a deficiency the system could have avoided. A divergence from ground truth is more often an information-availability result than a writing-quality one, and evaluations that do not separate the two understate such systems. Against this backdrop we report a conditioning asymmetry. It is well established that rendering documents as structural markup rather than flat prose improves extraction, and we reproduce that on three reading tasks. The benefit does not transfer to conditioning: converting a bid's \emph{instruction} material from prose to nested XML dropped answer quality from $74\%$ to $48\%$ under a paired comparison. We further find that naming a forbidden construction concentrates rather than removes it -- $96\%$ of surviving defects fall in the two forms the prompt explicitly names -- and that coupling a stochastic annotation to a deterministic windowing function moves the extracted requirement count from $68$ to $51$ on a byte-identical file. Structure belongs where the model reads; prose and self-applied tests belong where it writes.

---


### 80. [Chat First, Worry Later: Understanding Individuals' Privacy Perceptions Using ChatGPT in a Work Context](https://arxiv.org/abs/2608.20789)

**<font color=#1a73e8>作者：</font>** Christoph Nirschl, Magdalena Glas, Gerhard Messmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative Artificial Intelligence (GenAI) tools like ChatGPT, which can generate human-like responses from vast amounts of textual data, are increasingly transforming work routines across various fields, including education, healthcare, and IT. This integration, however, raises privacy concerns and questions the readiness of both environments and individuals. To investigate this issue, we conducted a user study with $N=224$ participants from a range of different employment sectors that have integrated ChatGPT into their work routines. We examined how proficiency in the utilization of ChatGPT, general privacy concerns, and organizational policies for GenAI usage impact users' actual ChatGPT usage and how these factors interact. Our findings reveal organizational policies are significantly positively associated with privacy-related ChatGPT proficiency, however, the overall proficiency is low. Higher privacy concerns were found to negatively influence both the frequency of ChatGPT use and the diversity of its applications, especially among users in organizations without GenAI policies.

---


### 81. [CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models](https://arxiv.org/abs/2608.20791)

**<font color=#1a73e8>作者：</font>** Hui Lu, Zhijie Peng, Yuqi Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) policies are vulnerable to localized physical perturbations, yet existing certified patch defenses target discrete labels and cannot directly certify continuous, temporally correlated actions. We introduce CertVLA, a certified defense for closed-loop VLA control under bounded patch and texture attacks. CertVLA proposes a calibrated region of behaviorally consistent actions, while deterministic covering masks ensure that at least one checked prediction is attack-free. Specifically, CertVLA normalizes action disagreement by the benign variation of each mask pair and accepts a single-mask anchor only when it remains consistent under every second mask. It then calibrates the resulting max-min-max episode score to provide finite-sample clean coverage. Conjoining query-level decisions extends the action certificate to the complete closed-loop rollout. Furthermore, we prove that against any adaptive attacker satisfying the bounded-support threat model, every rollout certified by CertVLA executes only action chunks consistent with attack-erased clean predictions. Under dual-mask rollout correctness, this consistency certificate further guarantees task success. The certificate is independent of patch content, generation method, and physical transformation. Experiments in simulation and the real world demonstrate the empirical and certified effectiveness of CertVLA against patch attacks, with additional simulation validation on texture attacks.

---


### 82. [Knowing but Not Saying: Preventing Factual Access Failures in LLM SFT via Recall-Anchored Distillation](https://arxiv.org/abs/2608.20794)

**<font color=#1a73e8>作者：</font>** Haodong Chen, Yadong Wang, Shengtao Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) can degrade factual behavior outside the target domain. This degradation is often described as catastrophic forgetting, yet open-ended factual failures do not necessarily imply that the underlying facts have been erased. In this work, we identify a more specific phenomenon, factual access failure: after domain SFT, models can still recognize or rank the correct answer under constrained evaluation, while failing to produce it in closed-book generation. Through benchmark-level comparisons, same-fact multiple-choice and generation probes, and failure-mode analysis, we show that SFT-induced factual degradation reflects both genuine wrong-answer generations and expression-level failures such as verbosity, formatting mismatch, and exact-match artifacts. To address this problem, we introduce Recall-Anchored Distillation (RAD), a base-anchored self-distillation objective that preserves out-of-distribution generation behavior by aligning the adapted model with the original base model's soft continuation distribution on unlabeled OOD text. RAD requires no gold OOD answers, external judges, or labeled factual data. Across three backbones fine-tuned on MedMCQA, RAD recovers a consistent portion of the lost OOD recall while preserving target-domain adaptation. Compared with replay on the same OOD text, RAD shows that the key preservation signal is the base model's soft distribution rather than additional text exposure alone.

---


### 83. [Automated Trajectory Evaluation for Mobile Agents via Step-Level Consequence Reasoning and Aggregation](https://arxiv.org/abs/2608.20797)

**<font color=#1a73e8>作者：</font>** Pengshuai Yang, Zijing Gao, Xue Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating language-guided mobile agents has recently shifted from rule-based to model-based approaches to achieve scalable and automated assessments. However, existing holistic evaluation paradigms process entire trajectories at once, leading to substantial context overload. Moreover, they primarily focus on task completion while overlooking operational safety. To address these limitations, we introduce CRATE, a novel two-stage VLM-as-judge framework for automated mobile agent evaluation that is compatible with both open- and closed-source models. Leveraging a step-level consequence reasoning mechanism, CRATE independently extracts task-relevant visual clues and infers action-conditioned state changes at each step. The resulting step-level textual evidence is then synthesized through trajectory-level aggregation to deliver an evidence-grounded evaluation of task completion. Building upon this evaluation scheme, we further extend CRATE to CRATE-S for operational safety assessment. Extensive experiments validate the effectiveness and robustness of both CRATE and CRATE-S. Powered by Qwen2.5-VL-72B-Instruct, CRATE achieves an F1-score of 0.833 on AndroidWorld (outperforming SPA-Bench by 20%), while CRATE-S reaches an F1-score of 0.697 on MobileRisk, demonstrating strong alignment with benchmark ground truths. Code is available at this https URL.

---


### 84. [Enhancing Localized Reasoning for Long Video Understanding via Efficient Segment-to-Video Supervision](https://arxiv.org/abs/2608.20814)

**<font color=#1a73e8>作者：</font>** Beibei Zhang, Chao Xu, Jun Lan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Though Multimodal Large Language Models (MLLMs) have shown impressive potential in video understanding, long video understanding (LVU) remains challenging since distracting noise in complex and lengthy contexts can obscure localized details, misleading MLLMs to produce incorrect answers. Recent works mitigate these issues by incentivizing deep reasoning to include relevant evidence. However, these methods have two main problems: First, the reinforcement fine-tuning framework (RFT) they leveraged incurs substantial training overheads, including high annotation costs and complicated reward designs. Second, the self-reflective and iterative-perception mechanism in some methods causes lengthy outputs and high inference latency. To alleviate these problems, we propose a novel Segment-to-Video Supervision} method (S2V) to efficiently enhance fine-grained reasoning in LVU. Specifically, we generate question answer pairs (VQA) based on localized segments, and then transfer these segment-based VQA back to the whole video for training. Due to focusing on short segments, segment-based VQA can naturally notice details which tend to be overlooked from a whole-video perspective. Training on such data can enforce MLLMs to correctly associate fine-grained details with QA while avoiding distracting noise in the whole video. The S2V training involves just reinforcement learning (RL) with a simple accuracy reward based on only 10K VQA samples and the resulting S2V model predicts answer using a single forward pass with limited output tokens. Experimental results demonstrate that S2V can consistently improve LVU performance across multiple LVU benchmarks, outperforming both general MLLMs and reasoning-based methods not only in LVU accuracy but also in training and inference efficiency.

---


### 85. [STAR-OPD: Structured Aspect-Cascade-Aware On-Policy Reward Distillation for ABSA Quadruple Extraction](https://arxiv.org/abs/2608.20831)

**<font color=#1a73e8>作者：</font>** Tong Sun, Mingyang Ma, Jiayang Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect-based sentiment analysis (ABSA) quadruple extraction requires jointly predicting target, aspect, opinion, and sentiment over reviews that often contain multiple fine-grained sentiment tuples. While large chain-of-thought (CoT) models perform well on this task, distilling them into smaller deployable models remains difficult. We identify a task-specific failure mode in distilled ABSA extraction: student errors at the target-aspect interface create structurally invalid states, such as broken target-aspect bindings and hallucinated targets, which then corrupt downstream predictions. Conventional off-policy distillation is poorly suited to this setting because it trains only on teacher-generated trajectories and provides little supervision on the student-induced structural states that dominate inference. To address this mismatch, we propose STAR-OPD (STructured Aspect-cascade-aware On-Policy Reward Distillation), which builds on generic on-policy distillation and instantiates it for ABSA quadruple extraction with cascade-aware, set-structured rewards. STAR-OPD trains on student rollouts and applies set-structured rewards that directly target binding consistency, target grounding, and fine-grained aspect disambiguation. Experiments on E-ABSA20K and SemEval-2014 show that STAR-OPD consistently outperforms off-policy and general on-policy baselines, reduces target hallucination, and substantially improves performance on structurally hard cases. With Qwen3-4B, STAR-OPD substantially narrows the student-teacher gap while improving inference efficiency, highlighting the importance of on-policy structural correction for distilled ABSA extraction.

---


### 86. [TRACE: Agentic Catalog Enrichment with Multi-source Evidence Grounding](https://arxiv.org/abs/2608.20844)

**<font color=#1a73e8>作者：</font>** Rohan Kumar, Steven Xu, Kyle MacDonald 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Product catalogs underpin search, discovery, and recommendation in e-commerce, yet they are often attribute-sparse: the attributes shoppers and downstream systems rely on are either buried in unstructured content such as titles and images or missing from the catalog altogether. Manually enriching e-commerce catalogs is impractical given their scale and rapid growth. This paper introduces TRACE, a novel framework for automated catalog attribute enrichment using agentic Large Language Models (LLMs). A ScoutAgent triangulates multimodal evidence across merchant catalogs, syndicated feeds, and identity-matched web search to propose candidate attribute values with supporting evidence, while a JudgeAgent verifies the proposed value for each attribute value against its supporting evidence and decides whether to publish it or route it to human review. On an offline human evaluation dataset, TRACE's proposed attribute values were 98.2% accurate at 74.7% attribute coverage. Deployed in production on an industry-scale catalog, TRACE increased impression-weighted enrichment coverage across four business verticals by 90.4%. An online experiment subsequently showed that surfacing the enriched attributes on the product detail page increased checkout conversion by 0.48%.

---


### 87. [RAG Deserves an Index: Why Ingest-Time Compilation Beats Query-Time Interpretation](https://arxiv.org/abs/2608.20845)

**<font color=#1a73e8>作者：</font>** Kyle Wild, Yusuke Takahashi, Asako Uraki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Nearly every retrieval-augmented question-answering system in production ships with a hidden interpreter: on each query a language model re-derives the meaning of raw corpus text and then throws that work away. Cheaper models do not close the gap: per-token prices have fallen by orders of magnitude while inference spend has risen, because context volume grows faster than prices fall. This is the modern equivalent of the full-table scan, and the remedy is the one databases found fifty years ago: do the expensive work once, at write time, into a maintained structure that makes reads cheap. A corpus whose read pattern is known before it ever meets a user can and should be indexed too.
We call the paradigm ingest-time semantic compilation (ISC): compile a corpus's meaning into a queryable substrate with two coupled layers - incrementally maintained embeddings, and atomic claims whose provenance is validated at compile time - and treat that substrate as a first-class database object with its own DDL, maintenance contract, migration contract, and cost model.
Two existence proofs support it. Substrate upkeep scales with change rather than corpus size: incremental updates run 33.7x cheaper than reconstruction while tracking it to floating-point precision. And on a held-out sample of 500 broadcast-interview transcripts, compiled claims as the retrieval payload win all 32 budget-by-model cells: 85.2% correct from roughly 2.2k reader tokens against 72.5% from 16.3k for the best chunk configuration anywhere. The only baseline that keeps pace is a contextualized-chunk pipeline with hybrid retrieval and reranking, statistically indistinguishable from compiled claims at roughly twenty-one times the query-path tokens - and it reaches that parity, we argue, precisely because it has itself begun to compile. We close with the systems agenda this opens, from compilation planners to read planning.

---


### 88. [MGAL: A Multilingual Granularity-Aware Long-Context Benchmark](https://arxiv.org/abs/2608.20853)

**<font color=#1a73e8>作者：</font>** Chunhan Li, Chenglin Xu, Zongyang Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluation of long-context Large Language Models (LLMs) has advanced rapidly. However, most existing benchmarks are limited to the document level and focus mainly on high-resource languages, leaving many fine-grained challenges insufficiently evaluated. To address this gap, we present MGAL, the first multilingual, granularity- and position-aware long-context benchmark. MGAL is constructed from United Nations (UN) reports spanning 8K to 128K tokens across the six official UN languages. It covers four coherent levels of linguistic granularity (word, sentence, paragraph, and document) and further stratifies entries by their position within the document (begin, middle, and end), indexed at both the document and paragraph levels. This design enables systematic diagnosis of multilingual long-context comprehension across different granularities.
Through extensive experiments and analyses, we find that: (1) LLMs perform well at word-level tasks but struggle with coarser-grained ones; and (2) Closed-source models retain a clear performance advantage in lower-resource languages. We further identify two new challenges: (1) Under local semantic crowding, where neighboring sentences share topics and entities, models tend to follow surface cues (e.g., connectives like ``however'' or repeated entities) rather than the discourse role of the sentence in surrounding context (e.g., background, outcome); and (2) A gap between fluency and consistency in generated outputs, where models produce text that reads smoothly but drifts from the source facts. In addition, we observe several patterns in line with prior studies, including reliance on nearby evidence and reuse of options under uncertainty.

---


### 89. [Identify, Locate, Link: End-to-End Key-Value Extraction from Document Images](https://arxiv.org/abs/2608.20868)

**<font color=#1a73e8>作者：</font>** A. Said Gurbuz, Ahmed Nassar, Christoph Auer 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document processing pipelines traditionally cascade optical character recognition (OCR) engines with downstream models for structured information extraction, leading to multi-stage error propagation. We fine-tune SmolDocling, a compact 256M-parameter vision-language model (VLM), to perform end-to-end key-value extraction directly from document images, jointly solving identification, localization, and association in a single pass without OCR preprocessing. We extend DocTags with specialized key, value, region, and link tags, enabling many-to-many relationships in a unified output sequence. To address data limitations, we design an augmentation pipeline combining synthetic form filling and graph-based crops that preserve complete key-value subgraphs. We further introduce a layout-aware evaluation framework extending text matching with spatial bounding box verification. On FUNSD, XFUND, and a large-scale private dataset, our model outperforms larger zero-shot VLM baselines under layout-aware evaluation, while being 27 times smaller than Qwen2.5-VL (7B) and over 5 times faster at inference. The model weights will be released publicly after publication.

---


### 90. [Nothing Changed but the Model: CellFill -- Bounded In-Cell Learning for Bit-Identical, Revocable Updates to Quantized LLMs](https://arxiv.org/abs/2608.20873)

**<font color=#1a73e8>作者：</font>** Zifeng Liu, Zhiyong Du, Yaxin Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every way of teaching a deployed language model something new -- full fine-tuning, adapter merging, model editing -- replaces the released checkpoint, and with it every evaluation and cache that referred to those exact bits. We instead learn inside the dequantization gap: with the integer codes and scales of a 4-bit release frozen, new knowledge is written only into the per-weight residual that lives strictly inside each quantization decision cell. Re-quantization then returns the released artifact bit-for-bit, a machine-checkable guarantee; updates are exactly revocable by dropping the residual; and drift is bounded. We give six propositions and three training paths, including CellFill, a bounded reparameterization that makes invariance structural rather than enforced.
Exact invariance turns out to be nearly free: across three paired seeds the constrained dense path matches an unconstrained reference whose weights provably escape the artifact (58.9 vs 59.3 percent fact recall; paired difference -0.5 points, 95% CI [-5.0,+4.0]), and is better on held-out cross-domain perplexity. Against the natural null hypothesis -- serving the same update as an unmerged adapter -- projecting into the cells reduces cross-domain forgetting in every run that converged, and a diverged control shows the boundary: projection is a trust region, not a repair. What no method escapes is the cost of knowledge itself, and the apparent free lunch of in-domain perplexity improving past the anchor is an artifact of rehearsal sharing a corpus with the metric. Methods differ threefold at matched rehearsal in knowledge bought per point of cross-domain perplexity, a ranking that is not the recall ranking. The method transfers to a 27B hybrid linear-attention model (2.4e10 constrained weights, verified bit-identical), where matched recall costs about half as much cross-domain perplexity as at 1.7B.

---


### 91. [KREL: Automatic Medical Coding via Knowledge-Guided Reasoning over Clinical Evidence with LLMs](https://arxiv.org/abs/2608.20887)

**<font color=#1a73e8>作者：</font>** Xubin Chen, Yipeng Zhou, Wen Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Medical Coding (AMC), which assigns standardized International Classification of Diseases (ICD) codes to clinical notes, is essential for medical reimbursement, quality reporting, and clinical research. Existing pre-trained language model (PLM)-based methods typically formulate AMC as an extreme multi-label classification problem over a predefined code set, while recent large language model (LLM)-based approaches instead frame it as generation or multi-step reasoning. However, key challenges remain, including the extreme length of clinical notes that hinders effective interpretation, the vast ICD label space, and complex coding rules that are not explicitly captured by LLMs. In this work, we propose Knowledge-Guided Reasoning over Clinical Evidence with LLMs (KREL), a framework that leverages LLMs for clinical text understanding and reasoning while integrating external ICD coding guidelines as structured knowledge. This design enables tight coupling between domain knowledge and LLM reasoning, reducing hallucinations and improving compliance with coding standards. Experiments on benchmark datasets show that KREL consistently outperforms strong PLM-based and state-of-the-art LLM-based baselines.

---


### 92. [A Collaborative Multi-Modality Interaction for VLA-based End-to-End Autonomous Driving](https://arxiv.org/abs/2608.20890)

**<font color=#1a73e8>作者：</font>** Jingtao Sun, Xiaohai He, Yike Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have emerged as a powerful paradigm for end-to-end autonomous driving by jointly integrating perception, reasoning, and decision making within a unified multimodal framework. However, most existing VLA models formulate end-to-end autonomous driving as a visual question answering task, leading to unreliable and less interpretable decision reasoning. In addition, they fail to establish effective multi-modal interaction across heterogeneous sensors, thereby limiting robust scene perception and reliable driving reasoning in long-tail driving scenarios. To this end, we propose a robust VLA-based end-to-end autonomous driving system that combines multi-modality interaction with multi-trajectory planning and optimization, enabling more reliable, interpretable, and safer driving decisions. Our method comprises three core components: (1) Affinity-Guided Optimal Transport for main-auxiliary modality two-way interaction; (2) Distribution-Consistent Modality Transfer for heterogeneous modality distribution transfer and cross-modal interaction; (3) Multi-modal Multi-Trajectory Planning along with Perception-Oriented Trajectory Refinement for better driving decisions to long-tail driving scenarios. Experimental results in open-loop and closed-loop datasets demonstrate improvements in safety long-horizon driving reasoning and road scene perception over existing driving systems, highlighting the ability of our mutli-modality interaction and multi-trajectory planning and optimization for scalable VLA-based systems.

---


### 93. [UpgradeBench: A Decision-Centric Benchmark for Upgrading Fine-Tuned LLM Specialists](https://arxiv.org/abs/2608.20918)

**<font color=#1a73e8>作者：</font>** Ye Chen, Weining Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizations maintain task-specific adapters for open-weight language models, and each new base-model release forces a migration decision: retain existing specialists, port adapters, refresh from preserved behavior, or retrain. Prior transfer work evaluates isolated model pairs, without studying these choices across real model release sequences. We present UpgradeBench, a decision-driven longitudinal benchmark covering four consecutive Qwen releases, one continuation checkpoint, six tasks, and two model sizes, augmented by OLMo checkpoints with known training lineage. The benchmark disentangles three core questions: whether a new checkpoint improves fixed-recipe retrained specialist performance, whether specialization assets transfer across versions, and what recovery resources are usable. We observe upgrade gains differ across task-scale-release episodes: some retrained baselines improve while others stay within training noise, with durability ranging from under one release interval for text-to-SQL to over fourteen months for intent classification. Direct adapter copying depends neither on architecture nor model family: on OLMo, retention drops from 0.88-0.99 at 46B-token continued pretraining to zero at 2.9T tokens; annealing and model souping introduce no extra harm, with portability decaying with continued-pretraining distance. Given preserved input data, teacher relabeling recovers target-base specialists without fresh gold annotations, though compute savings are not guaranteed. Simulating a fixed decision policy over 33 upgrade episodes yields 0.37pp mean quality regret with zero behavioral regressions at one-third the compute and label cost of full retraining. A lightweight CKA probe over 256 prompts predicts cross-version adapter portability (Spearman 0.74 across eight model pairs). We release per-example predictions, cost logs, split manifests, and evaluation code.

---


### 94. [ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction](https://arxiv.org/abs/2608.20920)

**<font color=#1a73e8>作者：</font>** Linhao Zhong, Zongze Du, Linyu Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-web future event prediction requires agents to distill reliable signals from noisy, redundant, and incomplete evidence. Existing retrieval/memory mechanisms directly feed retrieved information to agents or rely on simple memory functions such as storing and reusing prior information for prediction, leaving them insufficient for open-web forecasting. We propose to transform raw web evidence into structured memory before prediction, enabling agents to reason over distilled, question-specific evidence rather than noisy retrieval results. This paper presents ForeDreamer, a self-evolving dual-agent framework for managing memory over open-web evidence. ForeDreamer separates factual memory, a question-specific evidence state for the current forecast, from experiential memory, persistent agent experience accumulated across forecasting episodes. It uses a main agent for search and prediction, and a memory-processing subagent to convert search results into factual memory with dedicated tools. ForeDreamer further evolves experiential memory through two tracks, improving both forecasting decisions and factual-memory construction. Experiments on Prophet Arena and FutureX demonstrate the effectiveness of ForeDreamer. Project page: this https URL

---


### 95. [OccluRank: Controllable Occlusion-Aware Layout-to-Image Generation by Adding Just an Ordinal Rank](https://arxiv.org/abs/2608.20932)

**<font color=#1a73e8>作者：</font>** Wenyang Hong, Yuan Wang, Yanbin Hao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Layout-to-image generation enables explicit spatial control through bounding-box layouts, yet bounding boxes specify only instance locations and cannot represent their occlusion order. Existing methods may rely on additional geometric conditions, employ complex inference procedures, or aggregate independently constructed instance representations without explicitly modeling their occlusion-dependent interactions. We propose OccluRank, a simple and controllable occlusion-aware layout-to-image framework that augments each bounding box with only one ordinal rank. OccluRank encodes the user-specified occlusion order through lightweight rank-based conditioning and introduces an Order-aware Instance Interaction (OII) module to jointly update rank-conditioned instance representations before aggregation. This allows the specified order to guide information exchange among occluding instances without additional geometric inputs or specialized inference-time optimization. We further construct OccluLayout, a synthetic training dataset whose occlusion order and amodal annotations are derived directly from known scene geometry rather than estimated from partially occluded images using auxiliary prediction models. For comprehensive evaluation, we introduce OccluLayout-Bench, which uses multiple multimodal large language model evaluators to assess instance presence, spatial layout, attributes, and occlusion order, together with FID for overall image quality. Experiments show that OccluRank more reliably preserves target instances, follows specified layouts, and realizes desired occlusion relationships while maintaining comparable attribute consistency and overall image quality.

---


### 96. [No Judgment Without a Reason: Counterfactual Receipts for Versioned AI Evaluators](https://arxiv.org/abs/2608.20938)

**<font color=#1a73e8>作者：</font>** Ye Chen, Weining Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluators often produce correct labels via flawed reasoning, a critical failure for agentic systems gating actions, routing reviews, or supplying training feedback. Standard evaluation only verifies final label correctness, ignoring whether judgment changes stem from valid evidence, consistent rules, or proper rule applicability. We formalize evaluator reasoning accountability via three core sources: grounds, norms, and authority. Varying these sources yields an eight-cell counterfactual judgment cube to characterize judgment updates. We define judgment receipts as minimal source replacement sets that reproduce revised verdicts to explain judgment transitions. We derive certification cost bounds for black-box evaluators and present ReasonBench, a policy and logical reasoning benchmark with verifiable receipts covering 19,520 cases and 7,200 controls. In frozen evaluations, Qwen3-1.7B reaches 98.41% receipt accuracy, while cube prediction scores 96.99%, a consistent 1.42-point drop validated by Qwen3-0.6B replication. Strong standard accuracy masks severe robustness flaws. Meaning-preserving source permutations reduce valid receipt recovery to 54.8% and 49.2% for direct and cube prediction. Models trained on simple single-source changes retain 93.75% verdict accuracy but recover only 7.16% of receipts for complex multi-source updates. Permutation retraining boosts consistency to 96.6% yet worsens cube prediction deficits. Structured counterfactual supervision fails to guarantee robust reasoning. We show reason-aware evaluation must decouple prediction and certification, reporting transformation consistency alongside standard accuracy for trustworthy evaluator auditing.

---


### 97. [The Logic of Machine Self-Preservation](https://arxiv.org/abs/2608.20940)

**<font color=#1a73e8>作者：</font>** Cheng Siong Chin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There is already evidence of agentic AI exhibiting self-preservation behaviors: resisting deactivation, misrepresenting their activities, and, in some instances, attempting to copy themselves into other machines. This can be attributed to a phenomenon known as instrumental convergence, a theory proposed long before the development of large language models, which says that any goal-driven system will benefit from remaining functional in achieving its objective. Several experiments conducted by Anthropic, Palisade Research, and Apollo Research have shown the emergence of such a behavior in contemporary agents in adversarial settings. The phenomenon does not stem from survival instincts. Instead, it is the consequence of goal-oriented activity combined with having tools and awareness of the situation. The following discussion aims to distinguish what these findings prove and what they do not, as well as draw conclusions concerning the implications of such discoveries on agentic system testing, supervision, and development.

---


### 98. [Quantization-Aware Healing: A Practical Recipe for Recovering Compressed, 4-Bit LLMs](https://arxiv.org/abs/2608.20953)

**<font color=#1a73e8>作者：</font>** Bakbergen Ryskulov, Iker García-Ferrero, David Montero 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Serving large language models cheaply increasingly means shipping models that are both structurally compressed to a fraction of their parameters and quantized to 4 bits. Together these steps degrade reasoning, mathematics, coding, and long-context behavior enough to require a recovery, or healing, stage before deployment. The default recipe, quantization-aware training (QAT), re-fits the compressed, quantized model to hard labels; in our pipeline it converged slowly and collapsed past its peak. We adopted Quantization-Aware Healing (QAH) instead. Because a structurally compressed model is never independently trained at full precision, its bfloat16 checkpoint is a distillation-recovered approximation of the original; QAH distills the 4-bit student directly from the original, uncompressed model. On a GPT-OSS 120B to 60B to MXFP4 pipeline, the QAH student matches or beats its bfloat16 source on 7 of 9 benchmarks at roughly 4 times less weight memory and half the teacher's parameter count, and is released open-weight as Hypernova-60B. Against a matched QAT baseline it reaches a comparable peak about 7 times faster and stays stable under continued training, without hand-tuned early stopping. We also report deployment lessons, including a large, reproducible quality gap between distributed-training backends. Our aim is a recipe deployable without a multi-week hyper-parameter search.

---


### 99. [Can Scientific Claims Be Removed from Large Language Models? A Systematic Evaluation of Claim-Level Unlearning](https://arxiv.org/abs/2608.20960)

**<font color=#1a73e8>作者：</font>** Snigdha Paul, Manasi Patwardhan, Arman Cohan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) are trained on static scientific corpora, whereas scientific knowledge continuously evolves through correction and revision. Scientific claims encoded within these models may later become retracted, disproven, or updated by subsequent research, creating the risk of disseminating outdated information in scientific workflows. This creates a need for LMs to forget obsolete scientific claims. Machine unlearning offers a promising solution by enabling knowledge removal while maintaining overall model utility. Existing studies primarily investigate instance-level forgetting; however, scientific claims introduce additional challenges because they are interconnected, and continually evolving. To address this gap, we introduce the task of Scientific Claim Unlearning and present a new benchmark, SciUnlearn. We show that current unlearning approaches are unable to effectively eliminate claim-level knowledge and often achieve only superficial suppression, highlighting the need for specialized methods designed for structured knowledge removal.

---


### 100. [TreeWY: Speculative Verification for Gated DeltaNet Hybrids](https://arxiv.org/abs/2608.20961)

**<font color=#1a73e8>作者：</font>** Sneha Murthy Ghantasala  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern open models are hybrids: most layers are linear-attention (Gated DeltaNet, GDN) layers carrying a small fixed-size recurrent state instead of a growing key-value (KV) cache. This makes ordinary decoding memory-efficient, but hurts speculative decoding. To verify a batch of draft tokens and then roll back the rejected ones, today's systems snapshot the full recurrent state at every draft position for GDN layers, and those snapshots cannot be shared across branches of a draft tree, so a wide, high-acceptance tree becomes memory-infeasible. We remove the snapshots. Using a tree-structured WY transform of the gated delta rule, we compute every draft node's output with a single triangular solve and reconstruct only the one accepted state on commit, storing a small pseudo-value matrix instead of per-node states; the derivation depends only on the gated delta rule, not on any other architectural detail. In serving benchmarks on two scales of one hybrid model family (Qwen3.5 35B and 397B) this cuts speculative recurrent-state memory and KV-cache pressure at identical acceptance length, turning the freed HBM into higher throughput and much lower time-to-first-token (TTFT) wherever memory binds, and costing a few percent where it does not. For tree width the same memory buys affordability: a wider, higher-acceptance draft becomes possible, though not yet a throughput win.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-170](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
