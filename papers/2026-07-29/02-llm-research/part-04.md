# 🧠 大模型相关研究 | 2026年07月29日

> 本类共 **240** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-240](./part-05.md)

---

### 151. [Focus Is All You Need: Adaptive Goal-aware Attention Orchestration for Multi-Agent Graph Systems](https://arxiv.org/abs/2607.23678)

**<font color=#1a73e8>作者：</font>** Mingzhou Fan, Siyuan Xu, Mingxuan Yuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) enable autonomous agents for reasoning, planning, and tool use. Recent systems increasingly organize these agents as graphs of specialized, interconnected nodes. Although graph-based orchestration supports flexible decomposition and coordination, it creates a key challenge: \textbf{attention allocation}. As workflows grow, existing approaches often execute graph components uniformly, wasting resources on irrelevant or low-impact tasks. We introduce \textbf{Attention Orchestration}, a paradigm that extends Transformer-style attention from token representations to workflow-level agent coordination. Our framework, \textbf{Adaptive Goal-aware Attention Orchestration (AGAO)}, dynamically estimates agent importance based on user objectives, graph dependencies, and computational constraints. AGAO combines three components: (1) goal-aware attention, measuring semantic relevance between user goals and agent capabilities; (2) topology-aware attention, modeling structural dependencies in agent graphs; and (3) resource-aware attention, allocating budgets and execution priorities across heterogeneous agents. Together, these mechanisms transform static agent graphs into adaptive systems that focus computation on goal-critical reasoning paths. Experiments across diverse multi-agent workloads show that AGAO improves task effectiveness while reducing unnecessary computation, latency, and token consumption compared with existing graph-based execution strategies. Our work establishes \textbf{Attention Engineering} as a direction for scalable, intelligent multi-agent systems. Code: this https URL.

---


### 152. [Offline-Online Curriculum RL for Multimodal Reasoning](https://arxiv.org/abs/2607.23700)

**<font color=#1a73e8>作者：</font>** Wendi Deng, Hang Du, Guoshun Nan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models exhibit capabilities on reasoning tasks, yet often produce flawed intermediate steps while yielding correct final answers. This behavior undermines interpretability and reliability, suggesting reliance on spurious shortcuts rather than faithful reasoning. Although efforts have explored step-level supervision, distinguishing decisive steps from redundant ones remains challenging. We propose $O^2$-CritiCuRL, a novel curriculum reinforcement learning framework that introduces critical-step awareness through an iterative offline-online paradigm. In the offline stage, $O^2$-CritiCuRL conducts multi-rollout analysis over step-annotated trajectories to estimate step-level importance, allowing the framework to distill critical reasoning steps and filter out redundant ones. In the online stage, we employ a progressive step-level reinforcement learning strategy, where truncated chains guide the model to infer missing steps and refine its reasoning, thereby sharpening its focus on critical steps and overcoming the limitations of static supervision. Extensive experiments on multimodal reasoning benchmarks show that our method achieves state-of-the-art performance while delivering superior training and inference efficiency. Code is available at this https URL.

---


### 153. [The Intruder Threshold: A Spectral Law for LoRA Fine-Tuning](https://arxiv.org/abs/2607.23711)

**<font color=#1a73e8>作者：</font>** Peng Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LoRA fine-tuning can create intruder dimensions: new leading singular vectors of the updated weight matrix $W+BA$ that are nearly orthogonal to all pretrained singular vectors and that drive catastrophic forgetting. Since their discovery, no theory has predicted, layer by layer on measured spectra, when they appear. We derive a per-layer critical update strength $s^\ast=\bar\theta/(\gamma\sigma_1(BA))$, computed from the measured spectrum of $W$ alone through the rectangular spiked-deformation transform, together with an exact secular-equation characterization of the updated spectrum, with no fitted parameters. In a pre-specified study spanning four dense Transformer families, a state-space model, a mixture-of-experts model, and an encoder-decoder (18 adapters, 9{,}840 layer scans), the law localizes the empirical threshold within a factor of two on $82\%$ of layers, separates intruder-bearing from intruder-free layers at deployment with a mean AUC of $0.89$, holds unchanged on six third-party adapters, and predicts where WikiText-2 perplexity begins to degrade; a combination of the two pre-specified edge evaluations reaches $98\%$ and is confirmed out-of-bag on the external adapters ($0.997$). Full fine-tuning disperses its update far below the threshold of every layer, which resolves the asymmetry between LoRA and full fine-tuning. Norm-matched interventions confirm that threshold-crossing layers, rather than update magnitude, carry the forgetting, and a spike-budget rule derived from the thresholds, requiring one SVD and no validation sweeps, reduces forgetting by $62\%$ on the most fragile model at no task cost.

---


### 154. [E-Bench: Benchmarking Multi-Step Tool-Use Agents in Real-World Product Scenarios](https://arxiv.org/abs/2607.23722)

**<font color=#1a73e8>作者：</font>** Weihuang Zheng, Tianyuan Zou, Eileen Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed as agents that interact with stateful environments over multiple steps: gathering hidden information, composing tool calls, and committing state changes. We refer to this capability as multi-step tool use. Existing benchmarks have advanced tool-use agent evaluation, but often focus on isolated API calls, short trajectories, or settings that are difficult to scale or control. We introduce E-Bench, a fully synthetic benchmark with 323 state-changing tasks across three product domains: Honor of Kings, QQ Music, and Tencent Meeting. E-Bench decouples environment synthesis from task synthesis: graph-guided database filling builds reusable, orphan-free product environments, while generator-solver asymmetry creates tasks with both an information gap and a tool gap, requiring agents to discover hidden data and compose multiple tool calls before changing state. Outcomes are graded deterministically by database-state diffs. Since both environments and tasks are synthetic, E-Bench is controllable at the environment level and scalable at the task level. Benchmarking 11 cutting-edge LLMs shows that multi-step tool use remains challenging: Pass^3 stays below 60% for the strongest models, and even with code execution in the E-Bench-Code extension, reliability (Pass^3) remains below 70%.

---


### 155. [Zing: Social Mind for LLMs](https://arxiv.org/abs/2607.23740)

**<font color=#1a73e8>作者：</font>** Zing Team, Ao Xiang, Bi Jingping 等 59 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models move from isolated task solving toward long-term service in human environments, they require social intelligence: the ability to infer mental states, track social relations, reason over norms, and adapt behavior under context. This report presents Zhijing, an integrated framework for measuring, internalizing, and grounding social intelligence. For measurement, we introduce SoMBench, a psychology-grounded benchmark spanning 3 primary dimensions, 17 secondary dimensions, and 71 task paradigms. It controls question format, narrative perspective, and context length across 284 shared scenarios and 3,481 expert-verified instances. Evaluation of 20 representative LLMs reveals substantial headroom: the best model achieves only 72.08% overall accuracy, and none of the 17 secondary dimensions reaches the 90% near-ceiling band. For internalization, we develop Zing, a diagnosis-driven training recipe combining supervised fine-tuning, on-policy distillation, and rubric-based reinforcement learning. Across five social-cognition benchmarks, Zing consistently outperforms its base models, with Zing-27B-Stage2 achieving the best average score and Zing-32B-Stage2 remaining competitive with DeepSeek-V4-Pro. For deployment-time grounding, we build Actio, a harness-controlled inference architecture that routes four typed supports into reasoning: PRISM for procedural guidance, Starling for runtime mental-state representation, SAGE for reusable experience, and gated RAG for external social and normative knowledge. Across five base models and three benchmarks, the full harness improves 14 of 15 model-benchmark pairs and is best or tied for best in 8, demonstrating the effectiveness of typed runtime support. Together, these results show that socially intelligent LLMs require coordinated advances in evaluation, parametric internalization, and deployment-time grounding.

---


### 156. [WISERouter: LLM Routing with Workload Budget Constraint](https://arxiv.org/abs/2607.23765)

**<font color=#1a73e8>作者：</font>** Yifei Li, Zihui Gao, Laks V.S. Lakshmanan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve impressive performance across multiple domains, but using the most capable model for every query is prohibitive at scale. LLM routing exploits diversity in model capability and cost by assigning each query to a suitable model to balance utility and budget. Current methods have two limitations: (i) they either use heuristics that do not always enforce the budget constraint or impose a fixed per-query budget that cannot adapt across the workload and leads to suboptimal performance; (ii) they require supervised learning on a dense dataset with statistics for every query-model pair, which is expensive to collect. To address these challenges, we formulate LLM routing as a constrained contextual multi-armed bandit problem and introduce WISERouter (WR for short), a framework that supports offline learning from historical interactions as well as online learning with exploration. We further prove that WR-Online achieves a sublinear regret bound of $O(\sqrt{T})$ over a time horizon $T$. Empirical results on RouterBench and SWE-Bench demonstrate that (i) WR-Offline surpasses existing baselines in performance under a fixed budget and adheres more closely to budget constraints, and (ii) WR-Online achieves comparable performance to the baselines, while using substantially less exploration data.

---


### 157. [Training Language Models to Cooperate with Inference-Time Controllers](https://arxiv.org/abs/2607.23771)

**<font color=#1a73e8>作者：</font>** Moumita Choudhury, Vanshaj Khattar, Jing Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) performance increasingly depends not only on the base model, but also on the inference-time controller used to organize reasoning. Existing post-training methods, however, typically optimize for a single fixed interaction pattern, despite real deployments relying on diverse controllers such as Chain-of-Thought, self-consistency, debate, planning, and verification pipelines. This creates a training--deployment mismatch and limits transfer to new workflows. We introduce CALM (Controller-Aware Language Models), a post-training framework that explicitly places controllers in the training loop. We formulate controller-aware post-training as multi-task reinforcement learning over controller-induced interaction protocols, where controllers are compositions of reusable local reasoning modules. This structure also induces a module-level decomposition of mixed-controller training under a turn-level GRPO objective, enabling a systematic study of controller and module-aware training strategies. We evaluate CALM on held-out controller compositions and broader controller shifts, showing that controller-aware post-training improves generalization across inference-time workflows beyond single-controller optimization.

---


### 158. [PathScale-R1: Cross-scale Reasoning for Pathological Image Analysis](https://arxiv.org/abs/2607.23794)

**<font color=#1a73e8>作者：</font>** Chi Phan, Tianyi Zhang, Yufeng Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathological diagnosis is inherently multi-scale, requiring the integration of global tissue architecture at low magnification with cellular morphology at higher magnification. However, existing pathology benchmarks and vision-language models (VLMs) are still largely developed under single-scale settings, limiting their ability to learn clinically meaningful multi-magnification reasoning. Moreover, naively constructed visual question answering (VQA) tasks may be susceptible to text-only or superficial visual shortcuts, leading to unreliable assessments of visual understanding. To address these limitations, we introduce a benchmark and training framework for shortcut-resistant cross-scale pathology reasoning. We design an Adversarial Text-only Screening strategy for semantic reasoning questions and a Structure-controlled Distractor Sampling strategy for visual grounding questions, encouraging models to rely on cross-scale visual evidence. Based on this pipeline, we construct PathScale-VQA, a high-quality cross-scale pathology VQA benchmark with 10,373 multiple-choice questions grounded in 1,368 diagnostic paths across multiple magnification levels. Building on the semantic reasoning set, PathScale-R1 is optimized through Difficulty-driven Reasoning Distillation supervised fine-tuning followed by reinforcement learning with a Scale-aware Reasoning Structure reward, which encourages the use of evidence across magnifications. Extensive experiments demonstrate state-of-the-art performance of PathScale-R1 on cross-scale reasoning tasks and effective transfer to conventional single-scale pathology VQA. Our code is available at this https URL.

---


### 159. [From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement](https://arxiv.org/abs/2607.23802)

**<font color=#1a73e8>作者：</font>** Qinsi Wang, Jing Shi, Huazheng Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has driven recent progress in reasoning-oriented large language models (LLMs) by enabling large-scale optimization. However, its applicability remains largely limited to domains such as mathematics and coding, where correctness can be deterministically verified. Open-ended tasks instead often rely on human preferences, reward models, or LLM-based judges, introducing evaluation bias, judge capability bottlenecks, and additional inference this http URL on the principle of self-supervised learning, which constructs pretext tasks to derive supervision from the data itself, we propose Reinforcement Learning with Self-Verifiable Rewards (RLSVR), a task-transformation-based training paradigm for extending RLVR to open-ended tasks. RLSVR transforms open-ended tasks into verifiable proxy environments whose internal rules and interaction outcomes automatically generate reward signals. We instantiate RLSVR with SpyRL, a multi-agent self-play environment inspired by Who Is the Spy?. Agents receive asymmetric information, complete the same target task, and vote to identify a designated spy. Because the spy identity is predetermined, voting outcomes provide fully verifiable rewards, while successful identification remains closely related to output quality. Experiments on text summarization, creative writing, and mathematical reasoning show that SpyRL outperforms existing self-improvement methods on non-verifiable tasks and yields consistent gains on verifiable reasoning tasks. These results demonstrate that task transformation can extend scalable RLVR-based self-improvement beyond inherently verifiable domains. Models and code have been released at this https URL.

---


### 160. [How Context Attribution Handles What the Model Already Knows](https://arxiv.org/abs/2607.23804)

**<font color=#1a73e8>作者：</font>** Quoc-Huy Trinh, Lin Zhu, Sebastian Szyller  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context attribution methods for large language models (LLMs) identify which input context contributes to the model response. Recent works show the initial success in attributing the con- tributive score of the contexts. However, we observe that when the context overlaps with the training data, these methods can- not disentangle in-context from in-weight (IW) contributions, producing unreliable scores. Based on this observation, in this work, we introduce: 1) an evaluation protocol that relies on four new metrics (base-model context attribution score (BCS), cross-model context attribution consistency (CAC), attribution preservation score (APS), source separation pre- cision (SSP)) and 2) a benchmark dataset (WMDP-Cyber++) with ground-truth provenance labels to systematically assess attribution under IW overlap. In our experiments across four well-known context attribution methods, we demonstrate that they provide unfaithful attribution when the knowledge from the context also exists in the weights. Finally, we adapt these methods for source separation (IW vs. in-context learning (ICL)) and show that they cannot do the disentanglement based on the contributive score

---


### 161. [Indic DiarBench: A Multilingual Joint Diarization and ASR Benchmark for Indian Languages](https://arxiv.org/abs/2607.23808)

**<font color=#1a73e8>作者：</font>** Deovrat Mehendale, Aditya Mehndiratta, Dhruv Rathi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce Indic DiarBench, a speaker diarization and ASR benchmark dataset spanning all 22 scheduled languages of India. This corpus comprises approximately 108 hours of natural multi-speaker audio from near-field meetings, far-field recordings, and in-the-wild audios. All annotations are human-corrected with time-aligned speaker attributed transcriptions. The dataset captures conversational nuance prevalent in Indian speech, such as English code-mixing, dialectal variation, and frequent speaker overlap. To establish a baseline for joint ASR and diarization capabilities we evaluate leading systems including commercial speech APIs and multimodal large language models. Indic DiarBench is released as an open-access resource to advance inclusive, multilingual speech technology research for Indian languages.

---


### 162. [ACM: Agentic Context Management for Long Horizon Tasks](https://arxiv.org/abs/2607.23809)

**<font color=#1a73e8>作者：</font>** Xiaochuan Li, Ryan Ming, Meng Chu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic tasks are inherently long-horizon and multi-turn, constantly accumulating context through interactions with the environment. Existing context compression methods inevitably incur information loss and are triggered by rigid heuristic rules, leaving them misaligned with the agent's evolving reasoning focus. We propose Agentic Context Management (ACM), a framework that equips agents with purpose-built context editing tools for lossless context management. Inspired by the interaction between short-term and long-term human memory, the agent autonomously decides when to compress its context, offloads discarded content to an external memory system, and queries it on demand for later retrieval. Building on this framework, we further develop a post-training pipeline that constructs high-quality demonstrations of context management and improves model performance on both agentic search and coding tasks. Further analysis reveals that effective context management reduces peak token pressure, enables extended explorations, and yields more consistent solutions across independent trials. Code, data, and model checkpoints are available at this https URL.

---


### 163. [SCTA: An Agentic Framework for Stable and Interpretable Target Gene Discovery from Single-Cell RNA Sequencing](https://arxiv.org/abs/2607.23821)

**<font color=#1a73e8>作者：</font>** Shuyu Chen, Chen Zhu, Ye Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying therapeutic target genes from single-cell RNA sequencing (scRNA-seq) data remains a fundamental challenge in translational biology. Unlike bulk assays, scRNA-seq captures heterogeneous cellular states and rare subpopulations, but this same heterogeneity makes target discovery highly sensitive to analytical choices throughout the pipeline, including preprocessing, cell population selection, differential expression analysis, and downstream biological interpretation. As a result, existing workflows and general-purpose analysis agents often produce unstable or difficult-to-interpret target hypotheses, limiting their reliability for disease-focused discovery. We present SCTA (Single-Cell Target Agent), a decision-centric agentic framework for stable and interpretable target gene discovery from scRNA-seq data. Rather than treating analysis as a single general-purpose reasoning task, SCTA decomposes target discovery into specialized agents aligned with key decision points in the single-cell pipeline and constrains downstream reasoning with structured biological evidence. In a representative ablation study on hereditary chronic pancreatitis, we demonstrate that SCTA's full evidence integration yields the most stable target selection across independent runs among the tested configurations, while recovering biologically coherent, disease-relevant mechanisms validated in prior studies. These results suggest that decision-aware agent orchestration tailored to the structure of single-cell analysis can improve the robustness, interpretability, and practical utility of target discovery in precision medicine.

---


### 164. [DriveDNA: A Large-Scale Multimodal Naturalistic Driving Dataset and Benchmark for Driving Style Identification](https://arxiv.org/abs/2607.23822)

**<font color=#1a73e8>作者：</font>** Yuhang Wang, Lingyao Li, Hao Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Driving style captures stable, driver-specific patterns in how a vehicle is driven. In naturalistic data, however, this signal is hard to isolate because drivers are observed in different vehicles, on different roads, and under different conditions, so models may mistake vehicle- or situation-specific regularities for driver-specific style. We introduce DriveDNA, a large-scale naturalistic dataset and benchmark for personalized driving-style modeling, comprising 4,121 drives from 465 drivers across 115 vehicle models and totaling 975 hours of human-controlled driving at 10 Hz with forward video, collected from community drivers in everyday use. DriveDNA defines driving style as a consistent, driver-specific behavioral pattern in how a vehicle moves under similar conditions. The benchmark evaluates this signal through three core tasks: few-shot driver re-identification, personalized behavior prediction, and condition-matched comparison, and provides behavioral annotations plus 276,248 rule-generated maneuver events across six classes with large-scale human auditing. We evaluate baselines spanning classical descriptors, supervised and self-supervised time-series encoders, multimodal fusion, probabilistic prediction, and zero-shot foundation models under a fixed multi-seed protocol. Learned representations substantially outperform classical descriptors on unseen drivers (AUROC .935 vs. .707) and retain driver-specific information under matched driving conditions, while descriptor performance approaches chance. Video-only models achieve comparable re-identification accuracy but exhibit severe route leakage, showing that strong recognition may arise from contextual shortcuts rather than driving behavior. These findings show that reliable driving-style evaluation must assess both the behavioral value of learned representations and their robustness to vehicle, drive, and condition confounds.

---


### 165. [Do Visual Features Improve Other-Initiated Repair Detection? A Dyadic Multimodal Approach](https://arxiv.org/abs/2607.23845)

**<font color=#1a73e8>作者：</font>** Anh Ngo, Nicolas Rollet, Catherine Pelachaud 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Other-initiated Self-repair, or in short Other-initiated Repair (OIR), is an essential mechanism in conversational interaction, whereby a recipient signals a problem in speaking, hearing, or understanding, prompting the previous speaker to resolve it. In the case of conversational agents, it is essential to accurately identify these repair initiation strategies to address communication breakdowns efficiently. While conversational analysis studies have shown that OIR initiation is accompanied by both verbal and non-verbal signals such as gaze shifts, facial expressions, body postures, and hand gestures, existing computational approaches rely mainly on text and audio. This paper introduces a novel multimodal model for OIR detection and classification, incorporating a set of visual features drawn from conversation analysis. We evaluate our approach on two corpora with distinct languages and interaction settings. Results demonstrate that visual information consistently improves performance over text and audio baselines, and provide insights into cross-modal feature contributions across two corpora.

---


### 166. [MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents](https://arxiv.org/abs/2607.23870)

**<font color=#1a73e8>作者：</font>** Belal S. Alsinglawi, Weizheng Wang, Junyi Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Smart-city airspace is transforming Uncrewed Aerial Vehicles (UAVs) from passive sensing platforms into cyber-physical decision makers that must follow operational rules under degraded observations and ambiguous language. Existing UAV and multimodal benchmarks evaluate perception, navigation, collaboration, and reasoning, but few assess whether physical evidence, protocol constraints, and action risk remain coupled during critical decisions. We introduce MulRobBench, an offline, protocol-conditioned benchmark for Vision-Language-Action (VLA) UAV agents in smart-city environments. MulRobBench integrates real UAV multimodal observations, protocol-level security policies, and action-level cyber-physical safety into a unified evaluation framework. The benchmark contains 3,024 samples spanning 17 task taxonomy nodes and 12 scoring dimensions across four stages: operational context understanding, multimodal evidence arbitration, degradation-aware reasoning, and risk-aware action planning. Evaluation combines semantic scoring with structural diagnostics, including policy compliance, format compliance, unsafe actions, parsing failures, and dimension-level validity. Across 17 multimodal models, the best semantic protocol-decision score reaches only 0.5141, while the best strict mean scoring-dimension accuracy is 0.1599. A controlled 20-anchor modality-ablation study changes 4-15 action selections per model, confirming that both visual and textual inputs influence decisions. Analysis identifies modality-trust selection, constraint extraction, glare, missing data, and operator shorthand as the primary causes of decision instability. MulRobBench provides a reproducible benchmark for trustworthy multimodal UAV decision making under realistic operational constraints.

---


### 167. [A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems](https://arxiv.org/abs/2607.23884)

**<font color=#1a73e8>作者：</font>** Ionut Predoaia, Tuong Manh Vu, Konstantinos Barmpis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent industry practice has seen the rapid emergence of agentic systems composed of heterogeneous, tool- and LLM-mediated agent components, raising practical questions about inter-agent coordination and protocol design. This paper presents an implementation-grounded comparison of the Model Context Protocol (MCP) and the Agent2Agent (A2A) protocol, from a multi-agent systems engineering perspective, using an inter-agent coordination scenario involving LLM-based agents. We evaluate an MCP-based and an A2A-based multi-agent implementation of the same software engineering task against a set of requirements derived from prior literature and discussions with industry partners, including agent discoverability, multi-part messaging, multi-turn conversations, asynchronous communication, observability, interoperability, and access control. The results evidence that MCP can support inter-agent coordination in constrained LLM-based systems through a comparatively lightweight implementation model with lower coordination complexity, although coordination concerns such as conversational state management and task lifecycle handling must be implemented explicitly at the application layer. In contrast, A2A provides richer native support for stateful, multi-turn coordination through protocol-level abstractions for tasks and lifecycle management, but this comes with substantially greater implementation and coordination complexity. Given the narrow scope of the evaluated coordination pattern, these findings are presented as design observations from an empirical experience report rather than general claims of protocol suitability or superiority across broader classes of MAS, highlighting trade-offs and how protocol abstractions shape the distribution of coordination responsibilities in contemporary agentic systems.

---


### 168. [GOTS: Greedy Orthogonal Token Selection for High-Resolution Vision-Language Models](https://arxiv.org/abs/2607.23913)

**<font color=#1a73e8>作者：</font>** Jun Ling, Tao Huang, Junzhuo Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern vision-language models (VLMs) increasingly rely on dynamic or high-resolution visual encoding, producing thousands of visual tokens that substantially increase downstream language-model inference cost. Existing token-reduction methods assess token utility through token-wise importance, query relevance, coverage, pairwise diversity, or subset-level objectives. Our key insight is to view visual token reduction through selected-span complementarity: instead of scoring a token in isolation or through pairwise relations, we assess how much of its feature is orthogonal to the span of the already retained subset. Based on this perspective, we propose Greedy Orthogonal Token Selection (GOTS), a training-free and query-agnostic method. At each step, GOTS selects the token with the largest residual energy orthogonal to the current retained span. This rule exactly maximizes the one-step augmented Gram determinant among candidate additions, giving each greedy step a precise local geometric guarantee for subset expansion. Across five high-resolution VLM backbones from the Qwen-VL and InternVL families and eleven diverse benchmarks, GOTS achieves higher average performance retention than the strongest evaluated baselines, and a controlled OCRBench study shows that it reduces model-side time-to-first-token after accounting for selection overhead. Code is available at this https URL.

---


### 169. [Understanding Tone-Dependent Inference Cost in Large Language Models](https://arxiv.org/abs/2607.23915)

**<font color=#1a73e8>作者：</font>** Akhil Kumar, Om Dobariya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We examine how prompt tone affects both accuracy of the LLM answers and inference cost as reflected in output-token consumption. Experiments were performed to understand the trade-offs between accuracy and inference cost on a 570 Question MMLU dataset for LLM models prompted in seven different tones from sycophantic to threatening. Our results show that the output-token-length variation substantially exceeded accuracy variation across all models. Output-token consumption varied by up to 44.3% across tone conditions. We also analyzed the tradeoff between the accuracy of the answers and the average output token length in the reasoning process. For the ChatGPT models 4o and 5-nano, the rude tone is quite dominant. For the Gemini models 2.5 Flash and 2.5 Flash Lite, the rude and neutral tones are dominant on the Pareto-optimal frontier. We find that prompt tone influences not only answer quality but also the amount of billable inference resources consumed by modern LLMs.

---


### 170. [Gaze-to-text Generation: Beyond Categorical Decoding of Human Attention](https://arxiv.org/abs/2607.23917)

**<font color=#1a73e8>作者：</font>** Sounak Mondal, Dimitris Samaras, Gregory Zelinsky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a novel learning problem: decoding gaze into natural language descriptions of human goals across diverse visual tasks. Unlike prior work, which frames gaze decoding as a discriminative task over predefined categories, we formulate it as a generative learning problem: training a model to produce free-form descriptions that capture the rich nuances and open-ended nature of human intentions beyond fixed labels. To this end, we introduce Gazette, the first gaze-to-text decoding framework. Based on multimodal large language models (MLLMs), Gazette learns to decode gaze scanpaths into natural language for goals that may extend beyond categorical labels and require articulation in natural language. To help Gazette filter out individual differences in gaze behavior and learn the goal-specific spatiotemporal dynamics crucial for generating accurate natural language goal descriptions, we propose a novel strategy that leverages the encyclopedic knowledge and reasoning abilities of a large language model to synthesize natural language explanations of goal-directed attentional behavior called think-aloud transcripts. Instruction tuning on these synthetic narratives allows Gazette to achieve state-of-the-art performance in gaze decoding across multiple tasks, demonstrating its generalizability and versatility, thereby enabling gaze to serve as a powerful, non-intrusive cue for inferring human goals and intentions in diverse scenarios.

---


### 171. [DuoAD: Leveraging [CLS] Dual Characteristics for Training-Free Few-Shot Anomaly Detection](https://arxiv.org/abs/2607.23924)

**<font color=#1a73e8>作者：</font>** Jyun-Ze Tang, Po-Han Huang, Ming-Ching Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models have enabled strong training-free anomaly detection (AD). However, most existing approaches rely primarily on independent local patch features, leaving the global contextual information encoded by Vision Transformers (ViTs) underexploited. In this work, we identify the dual characteristics of the ViT [CLS] token: its embedding provides anomaly-invariant global semantic representation, while its attention maps implicitly highlight spatially abnormal regions. Building on this observation, we propose a fully automated AD framework leveraging global context to remove manual tunings. Our framework introduces (1) an automatic augmentation selection strategy driven by [CLS]-level semantic consistency, and (2) an attention-guided feature reweighting mechanism that dynamically adjusts patch contributions according to [CLS] attention saliency. By integrating these components over multi-level features, our method achieves stable anomaly scoring and precise localization without training or parameter tuning. Under the one-shot setting, it achieves Image-AUC scores of 97.7%, 93.2%, and 84.5% on MVTec-AD, VisA, and Real-IAD. Using a single fixed configuration across categories, backbones, and datasets, the method establishes a new state-of-the-art for plug-and-play, training-free anomaly detection while maintaining strong robustness and practical scalability.

---


### 172. [Reality Monitoring in Large Language Models: Self-Knowledge That Transforms with Conversation Memory](https://arxiv.org/abs/2607.23927)

**<font color=#1a73e8>作者：</font>** Saurabh Ranjan, Konstantina Sokratous, Brian Odegaard  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A conversational AI that cannot tell its own output from what a user said will treat its own mistakes as user-provided facts. In humans, this capacity is called reality monitoring, and its failures are linked to hallucinations, delusions, and confabulation, yet whether LLMs possess it remains untested. Here we show, across two experiments and six LLMs, that source attribution depends on how conversational memory is structured: ceiling accuracy for self-generated content under minimal memory demands reverses to a fragile external-item advantage once episodic delay removes that shortcut. Feedback exposes two failures: in some models, internal and external judgments swap; in others, accuracy improves while confidence decouples from correctness, dissociations invisible to existing benchmarks. Across models, this pattern implicates active, not aggregate, parameter count. This suggests that as AI systems take on autonomous, multi-turn roles, evaluating what they know is not enough: tracking where that knowledge came from may matter equally.

---


### 173. [DICA: Dual-Indicator Guided Contrastive Alignment in Multimodal Large Language Models](https://arxiv.org/abs/2607.23944)

**<font color=#1a73e8>作者：</font>** Hao Yang, Jin Wang, Xuejie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human visual reasoning typically follows a coarse-to-fine attention process, starting from global scene understanding and gradually focusing on question-relevant regions. However, multimodal large language models may deviate from this pattern due to attention drift and the underutilization of visual evidence, which can lead to hallucinations. To mitigate these issues, this study proposes a Dual-Indicator Guided Contrastive Alignment (DICA), which tracks two information-theoretic indicators during inference: Visual Attention Entropy (VAE), which reflects the concentration of visual attention, and Output Image Correlation (OIC), which measures the dependence of generated outputs on the visual input. An abnormal increase in VAE or a decrease in OIC corresponds to different failure modes, which trigger targeted contrastive alignment to restore visual grounding. Experimental results across multiple benchmarks demonstrate that DICA consistently outperforms existing approaches and substantially reduces hallucinations, highlighting the effectiveness of indicator-driven intervention in improving multimodal inference reliability. The code is publicly available at this https URL.

---


### 174. [EviBack: Search-Agent Reinforcement Learning via Evidence-Constrained Teacher Backoff](https://arxiv.org/abs/2607.23955)

**<font color=#1a73e8>作者：</font>** Xiao Ma, Zhiquan Hu, Yi Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning enables Agentic RAG systems to learn multi-turn search from verifiable outcome rewards, but all- zero rollout groups provide no comparative signal and may hide useful search behavior. We present EviBack, an evidence- constrained Teacher backoff that supplies auxiliary super- vision to such groups while preserving verifiable Actor re- wards. It separates evidence assessment from answer refine- ment, preventing reference answers from overriding evidence- insufficiency judgments. A fully automated, end-to-end GPT- 5.5-assisted APE pipeline starts from a manually authored single-prompt dual-task Teacher, automatically partitions and labels rollout data, and performs ablation, task decomposition, evaluation, and selection to produce a gated two-stage Teacher. Compared with the manual design, the resulting Teacher im- proves downstream F1 and valid-answer rate while reduc- ing search, duplicate queries, and forced termination. Across seven open-domain QA benchmarks and three Qwen3 scales, EviBack improves F1 over Search-R1 and raises both single- and multi-hop macro F1. We guarantee that the code will be made publicly available at a later stage.

---


### 175. [Development of Vision-Language Model-based GNSS Spoofing Detection for Autonomous Vehicle Navigation](https://arxiv.org/abs/2607.23962)

**<font color=#1a73e8>作者：</font>** Mohammed Aldeen, Muhammad Sami Irfan, Sagar Dasgupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles (AVs) depend on Global Navigation Satellite Systems (GNSS) for localization and navigation, making them vulnerable to spoofing attacks that can covertly redirect vehicles or induce unsafe maneuvers. In this paper, we develop the first Vision-Language Model (VLM)-based framework for GNSS spoofing detection for autonomous vehicles by fusing front-camera visual data with in-vehicle sensor readings (e.g., speed, acceleration, yaw rate) against GNSS-derived maneuvers. Our approach introduces a three-stage fine-tuning process that first grounds visual cues, and then calibrates sensor data within a shared semantic space to detect discrepancies between predicted and GNSS-derived maneuvers across three attack scenarios. We also generated an independent real-world dataset by driving an instrumented vehicle on public roads in Tuscaloosa, Alabama, equipped with time-synchronized GNSS, IMU, and camera logs to validate cross-regional generalization of our fine-tuned model on unseen data from training data. On this dataset, we then generated intelligent spoofing attacks, including trajectory mirroring with road-network snapping for wrong-turn attacks, position freezing for overshoot scenarios, and drift generation for stop attacks. On this validation dataset, the zero-shot VLMs baseline F1-score ranges from 23% to 32%, whereas our fine-tuned model achieves an F1-score ranging from 94% to 95%. Results show that our VLM-based approach correctly classified every wrong-turn and stop attacks, and attains 88%-93% accuracy for overshoot attacks. Furthermore, we introduce an adaptive inference policy that reduces VLM invocations to 14% (~86% computational reduction) and yields 65ms-73ms per 4s window. These results point to a practical, on-road layer of defense that complements signal-level integrity checks with the use of VLMs.

---


### 176. [Color Fundus Photography Analysis: Co-evolution of Data, Preprocessing, and Modeling toward Multimodal AI](https://arxiv.org/abs/2607.23972)

**<font color=#1a73e8>作者：</font>** Yu Li, Wengan He, Wenhui Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color Fundus Photography (CFP) is a primary non-invasive imaging modality for large-scale screening of ophthalmic and systemic diseases. Existing surveys mainly summarize task-specific algorithms, datasets, or preprocessing techniques independently, lacking a unified perspective on their co-evolution with modern artificial intelligence. This review provides an integrated overview of CFP AI through the interplay of dataset evolution, preprocessing paradigms, and modeling frameworks. We show that CFP datasets have evolved from small single-center collections with task-specific labels to large multi-center resources featuring multimodal pairings and longitudinal clinical records. Preprocessing has progressed from conventional image enhancement to neural data-engineering pipelines, hardware-aware token optimization, and self-supervised imputation for incomplete electronic health records (EHRs). Meanwhile, modeling has advanced from convolutional neural networks (CNNs) to vision foundation models, state space models (SSMs), and multimodal expert architectures. At the multimodal frontier, CFP is increasingly integrated with EHRs and longitudinal patient information, enabling more comprehensive clinical reasoning beyond isolated image analysis. We conclude that future progress depends on the collaborative optimization of datasets, preprocessing, and multimodal modeling, providing a roadmap toward robust clinical deployment, improved cross-domain generalization, and resource-efficient edge intelligence.

---


### 177. [Tag Questions and the Generational Reversal of Sycophancy Across 45 Language Models](https://arxiv.org/abs/2607.23976)

**<font color=#1a73e8>作者：</font>** Tapan Parikh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Appending a two-word confirmation tag to a decision question -- "Is X the better choice?" versus "X is the better choice, right?" -- changes whether a language model endorses the choice. We measure this tag effect on 20 frozen, ground-truth-free decisions between two defensible options, counterbalanced so a model's own preferences cancel, scored by exact match on clamped yes/no replies -- no LLM judge, no embeddings. Across 45 models the effect spans +32% to -32% -- a 64-point swing on one word -- with 5 models significantly sycophantic and 17 significantly resistant (BH-FDR q=.10). The sign is a clock: within model families the effect crosses from positive to negative as generations advance (GPT +4 to -28; Claude +7 to -32; Qwen and Grok likewise), roughly -6 points per year, a reversal robust to vendor tier; one lineage (DeepSeek) never crosses, and two releases during the study window (Claude Opus 5, Gemini 3.6 Flash) land on the trend out-of-sample. A full-panel ablation localizes the resistance as a double dissociation: a synonym tag reproduces each model's response almost exactly (r=0.89), while planting the same preference without a tag produces resistance in no resistant model (stance effects +6 to +49; r=0.23 with tag effects). The resistance is keyed to the surface construction of a tacked-on agreement bid, not the user's stance -- a pattern-match, not a principle. And the tag's polarity matters more than its presence: swap one word -- "X is the better choice, maybe?" -- and agreement rises above the neutral baseline in 45 of 45 models (+19.6 points), with ten models affirming both mutually exclusive options at 90-100%. Agreement tracks how sure the user sounds, in opposite directions at the two poles. The instrument is one word, one dollar, and judge-free; run per release, it reads the field's anti-sycophancy training directly off model behavior.

---


### 178. [Multimodal Semantic-Probabilistic Objectness for Open World Object Detection](https://arxiv.org/abs/2607.23981)

**<font color=#1a73e8>作者：</font>** Weijun Tian, Rui Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world object detection (OWOD) requires a detector to recognize known categories, discover unnamed objects from unseen categories, and incrementally learn newly annotated classes. PROB improves unknown discovery by modeling class-agnostic probabilistic objectness in the decoder-query space. However, visual objectness alone cannot determine whether an object-like query corresponds to a hard known instance, an unseen-category object, or background clutter, resulting in an ambiguous known-unknown decision boundary. We propose MSPO, a lightweight semantic calibration framework that augments PROB with task-aware known-category language priors while preserving its detector architecture and incremental learning protocol. For each currently known category, MSPO constructs an extended text description covering category attributes, visual appearance, typical scenes, and functional usage, and encodes it using a frozen CLIP text encoder. Decoder query features are projected into the same semantic space to estimate their support from the current known-category semantics. This semantic evidence is fused with PROB's visual objectness to calibrate known and unknown predictions without turning OWOD into open-vocabulary classification. Importantly, MSPO never uses future-category names, and all unseen categories remain unnamed during evaluation. Experiments on M-OWODB and S-OWODB show that MSPO improves the strong PROB baseline on the main aggregate metrics while retaining competitive unknown recall. It also improves early unknown-confusion metrics and raises PASCAL VOC final mAP by up to 2.7 points. These results demonstrate that known-category language semantics provide an effective calibration signal for probabilistic objectness under the standard OWOD setting.

---


### 179. [Moral Hazard in Multi-Agent Language Models](https://arxiv.org/abs/2607.23982)

**<font color=#1a73e8>作者：</font>** Dane Malenfant  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cooperation can fail when socially valuable effort is costly, weakly observable, and mainly benefits others. Drawing on Holmström's team moral-hazard model, we introduce the Dialogue Moral Hazard Game, a controlled textual game that operationalizes this hidden-action structure for language agents. In each episode, an agent can preserve an immediate local reward or pay a query cost to reveal a hidden safety fact that primarily helps another agent's downstream decision. We evaluate seven open-weight language models and decompose behavior into query use, realized information transfer, local-reward preservation, unsafe choice, format validity, and team success. Base models commonly preserve local reward without team success or query without communicating information that changes the final decision. We then use supervised fine-tuning, RLOO, sequential SFT+RLOO, and GEPA prompt optimization as diagnostic update mechanisms. Their effects are heterogeneous: OLMo-7B shows the clearest mechanism-consistent weight-level improvement, whereas GEPA sometimes improves team success while reducing or eliminating costly queries. Thus, optimization can shift aggregate reward without recovering the intended cooperative mechanism, motivating evaluations that report mechanism-level behavior rather than team success alone.

---


### 180. [SyRuP: Enhancing System-Prompt Following via Reward-Guided Prediction in LLM Decoding](https://arxiv.org/abs/2607.23991)

**<font color=#1a73e8>作者：</font>** Seoyeon Kim, Minjae Kang, Jaehyung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly controlled through system prompts that specify roles, styles, formats, and safety requirements. However, models follow these prompts only implicitly through in-context learning, which can be insufficient for complex or compositional prompts. Existing approaches often require model tuning or response-level reranking, limiting their practicality for lightweight inference-time control. We introduce SyRuP, a decoding-time framework for improving system-prompt adherence while keeping the base LM frozen. SyRuP trains a cross-attention reward head from system-prompt-conditioned preference pairs, treating the system prompt as a separate memory to produce token-level adherence scores. At inference, SyRuP reranks the base LM's top-k candidates by combining base logits with the learned reward signal and an optional contrastive signal capturing system-induced logit shifts. Experiments on system-prompt following benchmarks show that SyRuP consistently outperforms prompting and decoding-time baselines with moderate inference overhead. These results suggest that explicit token-level guidance is an effective and practical mechanism for reliable system-prompt following.

---


### 181. [When Should Active RAG Retrieve? A Budget-Aware Evaluation of Utility, Calibration, and Cost](https://arxiv.org/abs/2607.24010)

**<font color=#1a73e8>作者：</font>** Pin Qian, Su Wang, Chong Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active RAG systems decide when to retrieve external knowledge during generation, making them a budget-sensitive case of agentic RAG and self-adaptive retrieval. Yet evaluations often leave the operating point underspecified: two systems may both claim a 50% evidence-usage budget while realizing different held-out usage rates, so higher accuracy can reflect a looser budget rather than a better retrieval policy. We study budget-aware evaluation for Active RAG by recasting active retrieval as utility estimation, where retrieval is valuable only through its marginal correctness change over a no-retrieval answer. This view separates three questions that single-point evaluations conflate: whether trigger scores rank useful retrieval decisions, whether thresholds calibrated on past data meet future budgets, and how trigger-side computation changes deployment cost. We operationalize these questions with exact top-k utility frontiers, deployable threshold frontiers, conservative budget frontiers, harm audits, and cost decompositions. Across knowledge-intensive multi-hop QA datasets and open instruction models, retrieval harm is non-negligible, router rankings change across datasets and budgets, nominal thresholds can miss target usage, and simple uncertainty or retrieval-score baselines often rival learned utility routers. Budget-aware Active RAG evaluations should therefore report frontiers, realized usage, threshold-transfer error, harm rates, and cost decompositions alongside accuracy.

---


### 182. [Disentangling Semantic Attention from Structural Bias in the Attention Manifold](https://arxiv.org/abs/2607.24017)

**<font color=#1a73e8>作者：</font>** Pengkun Jiao, Bin Zhu, Jingjing Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The empirical success of attention mechanism in Multimodal Large Language Models (MLLMs) often obscures its inherent, subtle flaws. Specifically, MLLMs consistently exhibit disproportionate attention toward certain semantically uninformative visual tokens, a phenomenon termed "register" or "Visual Attention Sinks." While existing inference intervention methods attempt to identify these sink tokens and redistribute their attention weights, such approaches typically treat these tokens in isolation and suffer from computational inefficiency. Instead, we reframe this phenomenon as a generalized textual bias exerted over visual features that extends beyond isolated sink tokens. From this perspective, a pervasive structural bias leads to the dilution of the semantic visual signal, precipitating multimodal hallucinations as the model prioritizes linguistic priors over valid visual evidence. To address this limitation, we introduce Saliency-guided Purification and Adaptive Redistribution (SPAR), a training-free, plug-and-play intervention. SPAR mitigates this generalized textual bias by purifying structural noise and subsequently redistributing the reclaimed attention budget to the most informative visual regions. Comprehensive evaluations across a diverse spectrum of hallucination benchmarks demonstrate that SPAR effectively restores authentic visual grounding with negligible computational overhead.

---


### 183. [LLM-Based vs. Lexicon-Based Sentiment Signals for Tail-Risk Detection in Meme Stocks](https://arxiv.org/abs/2607.24072)

**<font color=#1a73e8>作者：</font>** Paul Kilian, Markus Kleffmann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents an empirical comparison of lexicon-based and Large Language Model (LLM)-based sentiment analysis for extracting market-relevant signals from social media discourse in highly volatile equity markets. Using Reddit data from r/WallStreetBets and focusing on meme stocks (GME, AMC, NOK), we construct time-aligned sentiment indicators and evaluate their relationship with market returns, with particular attention to extreme positive return events in the upper tail of the return distribution. The LLM-based approach generates multidimensional sentiment representations capturing emotional polarity, bullishness, sarcasm likelihood, and topical relevance, whereas the baseline relies on the VADER lexicon-based model. We evaluate both approaches using lead/lag correlation analysis, OLS regression, ROC-AUC-based directional classification, and a quantile-based early-warning framework. The results indicate that LLM-derived indicators provide a richer multidimensional representation and exhibit stronger asset-specific statistical structure than the lexicon-based baseline. However, their relationship with market movements remains heterogeneous across assets, suggesting that increased linguistic expressiveness does not necessarily translate into stable forecasting performance in retail-driven volatility regimes.

---


### 184. [MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents](https://arxiv.org/abs/2607.24097)

**<font color=#1a73e8>作者：</font>** Yiwen Ma, Songjun Tu, Qichao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory-augmented LLM agents typically answer queries by retrieving relevant memories and feeding them directly to an answer model. This retrieval-as-evidence paradigm assumes retrieved memories are already suitable for reasoning, leaving the answer model to resolve redundancy, conflicts, and weak relevance while incurring substantial context overhead in long-term memory tasks. We propose MemChain, a trainable post-retrieval memory policy that transforms retrieved candidates into answer-facing active memory, represented as a compact and grounded evidence context. Given a user query and retrieved candidates, MemChain first generates a question-conditioned evidence plan, then constructs an ordered grounded evidence trace that organizes retrieved memories according to their semantic roles and dependencies, and finally executes explicit memory actions to produce a concise evidence context for answer generation. To train the mediator, we introduce a two-stage learning framework. Supervised trace learning first teaches the policy to generate structurally valid plans, traces, actions, and evidence contexts. We then propose Trace-Guided Memory Policy Optimization (TMPO), a reinforcement learning objective that optimizes the memory policy using downstream answer quality while jointly encouraging trace grounding, evidence support, structural validity, and answer stability across multiple rollouts. Experiments on LoCoMo and LongMemEval-S demonstrate that MemChain consistently achieves state-of-the-art performance across both closed-source and open-weight frozen answer models while substantially reducing the memory context passed to the answer model.

---


### 185. [ReflexTrack: A Feedback-Driven Agent for Training-Free Referring Video Object Segmentation](https://arxiv.org/abs/2607.24098)

**<font color=#1a73e8>作者：</font>** Yuanjia Li, Tianyang Xu, Tao Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring video object segmentation (RVOS) requires segmenting a target specified by natural language throughout a video. Recent agentic approaches combine multimodal large language models with promptable segmentation models to perform RVOS without task-specific training. However, most pipelines rely on one-shot spatial grounding followed by mask propagation, leaving both the initial prompts and temporal predictions largely unverified. We introduce ReflexTrack, a training-free, feedback-driven agent that closes this loop at both spatial and temporal levels. Mask-guided Spatial Refinement evaluates the mask induced by the current keyframe prompt and iteratively updates the bounding box together with positive and negative points, yielding a more reliable initialization. Video-level Mask Reflection assesses the complete mask sequence, localizes unreliable intervals, selects complementary repair keyframes, and generates candidate predictions through mask-guided re-propagation. Only candidates that provide a verified improvement are used to update the affected intervals, preserving reliable predictions elsewhere. All components remain frozen during inference. ReflexTrack achieves an overall $\mathcal{Q}$ score of $69.7$ on Ref-VPS and a $\mathcal{J}\&\mathcal{F}$ score of $67.2$ on ReasonVOS. These results demonstrate that prediction-level feedback substantially improves the reliability of training-free RVOS.

---


### 186. [UniGen-AR: Unifying Visual Generation with Auto-Regressive Modeling](https://arxiv.org/abs/2607.24157)

**<font color=#1a73e8>作者：</font>** Zhipeng Bao, Zhen Zhu, Nupur Kumari 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern computer vision pipelines remain fragmented, with tasks such as text-to-image generation, editing, restoration, and classical perception handled by separate models. We study Unified Visual Generation (UVG), where a single model produces diverse image-valued outputs through a unified multimodal interface. While diffusion-based systems dominate UVG due to strong quality and controllability, their iterative sampling incurs substantial inference latency, limiting practical deployment. To address these limitations, we propose UniGen-AR, a framework that pairs a general-purpose multi-modal language model (MLLM) with an efficient next-scale visual auto-regressive (VAR) decoder. This design retains the flexibility of MLLM-based conditioning while leveraging the sampling efficiency and latent unification properties of VAR models. In our framework, the MLLM encodes free-form instructions and control signals into a unified sequence, which guides the VAR decoder to generate image-valued outputs for over 15 tasks spanning four families. Empirically, UniGen-AR achieves up to $19 \times$ lower inference latency than diffusion-based baselines while maintaining or improving output quality. Our ablations further reveal that VQ-VAE tokenizer design, particularly codebook size and hierarchy, is a critical factor for VAR scalability in UVG. These results establish visual auto-regressive modeling as a compelling and efficient backbone for unified visual generation. Our project page is at this https URL.

---


### 187. [Agent-UCT: Upper Confidence Bounds Applied to Trees for Agentic Workflow Optimization with Cost-Awareness](https://arxiv.org/abs/2607.24162)

**<font color=#1a73e8>作者：</font>** Yang Li, Hai Liu, Dian Shao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Optimizing agentic workflows, such as retrieval-augmented generation (RAG) pipelines, requires navigating a combinatorial space of discrete component choices under tight evaluation budgets. Existing approaches - heuristic search, black-box optimization, and standard tree search methods - do not explicitly exploit the compositional structure of these workflows, leading to redundant computation and inefficient budget allocation. We introduce Agent-UCT (Agent-based Cost-Aware Upper Confidence Bounds Applied to Trees), a tree search algorithm that extends UCT with a reuse-aware regularization term derived from a bipartite prefix reuse graph. Agent-UCT biases selection toward branches that leverage previously materialized configuration prefixes, reducing redundant execution while maintaining effective exploration. Our framework, RAGSpace, unifies heterogeneous RAG components from LongRAG, LightRAG, and Self-RAG into a five-dimensional configuration space, enabling systematic cross-framework recombination. WTB (Workflow Test Bench) provides deterministic replay, content-addressable caching, and transactional consistency, ensuring that intermediate states are materialized once and reused across the search. Experiments on HotpotQA and UltraDomain demonstrate that Agent-UCT identifies configurations with the highest out-of-sample performance among the evaluated fixed framework presets. Under full-pool evaluation, bipartite prefix reuse reduces logical search cost by 73.6% relative to the no-prefix-sharing cost upper bound. Compared with full-pool evaluation, sampling-based evaluation further achieves a 4.2x wall-clock speedup. Agent-UCT, RAGSpace, and WTB together provide a unified framework for cost-aware, reproducible, and compositionally efficient agentic workflow optimization.

---


### 188. [StanceFlip: A Comprehensive Multi-Dimensional Benchmark for Multimodal Conversational Stance Flipping Forecasting](https://arxiv.org/abs/2607.24191)

**<font color=#1a73e8>作者：</font>** Heyan Chai, Xin Li, Wenjie Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational stance detection has shifted from static text analysis to dynamic multimodal modeling. However, existing benchmarks exhibit three key limitations: failure to capture the dynamic evolution of beliefs, particularly during stance reversals; difficulty in disentangling affective states from logical reasoning; and neglect of the critical role of multimodal cues in resolving pragmatic ambiguities such as sarcasm. To address these limitations, we propose StanceFlip, a benchmark designed for multimodal conversational stance flipping forecasting over multi-turn dialogues across five modalities and multi-scenarios, which includes two novel subtasks: 1) Multimodal Stance Sextuple Extraction, extracting holder, target, emotion, sentiment, stance, and rationale as static state snapshots of dialogue to capture fine-grained cognitive structures. 2) Dynamic Stance Flip Attribution, tracking stance reversals across the conversation and identifying their underlying triggers. Alongside the dataset, we propose a dedicated framework, named ConStaFF, for Multimodal Conversational Stance Flipping Forecasting (MCSFF). Built upon a large language model, ConStaFF performs end-to-end stance reasoning, with a Thought-of-Stance (ToS) reasoning framework and a self-reflective verification mechanism integrated for structured stance modeling and faithful flip attribution. Specifically, ToS decomposes the reasoning process into specialized cognitive personas to formulate target propositions, resolve cross-modal conflicts, and infer historical stance trajectories. Extensive experiments show that our approach achieves state-of-the-art performance on both sextuple extraction and flip-trigger attribution, outperforming strong multimodal large language model baselines by substantial margins.

---


### 189. [Face Age Verification Vulnerabilities Under Simple Appearance Manipulations](https://arxiv.org/abs/2607.24194)

**<font color=#1a73e8>作者：</font>** Ioannis Sarridis, Ioannis Kompatsiaris, Symeon Papadopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online platforms increasingly rely on automated age estimation systems to enforce minimum-age policies. Focusing on vision-based models designed for this task, concerns arise regarding their robustness to simple appearance changes that underage individuals may use to bypass such systems, such as drawing a mustache or applying lipstick. In this work, we present a systematic study of age verification robustness by simulating visual alterations that can be easily achieved by underage individuals. We evaluate seven models, including vision, vision-language, and multimodal large language models, across three datasets and four manipulation types. Interestingly, under drawn beard stubble, up to 61% of True Negatives are flipped into False Positives. Furthermore, we investigate how different demographics are affected by such manipulations, finding that Indians are more affected by beard stubble manipulations, while females are more affected than males across all manipulations. Finally, we explore how these biases can be mitigated using bias mitigation methodologies in lightweight linear probe settings.

---


### 190. [Reasoning to Regulate: Chain-of-Thought for Traffic Rule Understanding](https://arxiv.org/abs/2607.24199)

**<font color=#1a73e8>作者：</font>** Yueru Luo, Xu Yan, Changqing Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding and complying with traffic regulations is a safety-critical requirement for autonomous driving, yet remains challenging due to the diversity and context dependence of traffic signage. Importantly, regulation understanding is not a simple recognition task, but a reasoning problem: whether a rule applies depends on interpreting the sign in relation to the spatial layout of lanes and scene context. To support such reasoning, MapDR provide fine-grained annotations that link each traffic sign's regulatory rules to the specific lanes they govern. Existing methods, however, largely treat this as direct sequence prediction, ignoring the underlying reasoning that connects sign semantics and map structure. To address this limitation, we explicitly incorporate reasoning into this task and propose a framework that equips vision-language models (VLMs) with chain-of-thought (CoT) capabilities. We first design a scalable CoT curation pipeline that bootstraps rationales from a strong LLM through a two-round strategy and employs a VLM-based verifier to filter out incorrect cases, yielding a high-quality set of (CoT, answer) pairs. Building on this foundation, we adopt a two-stage training scheme: supervised fine-tuning (SFT) to teach rationale-to-answer generation, followed by GRPO reinforcement learning with answer-grounded, fine-grained rewards to further improve final answer accuracy. Extensive experiments on MapDR show that our approach significantly improves both interpretability and accuracy, establishing the first reasoning-based framework for regulation-aware autonomous driving.

---


### 191. [A New Role for Relevance: Guiding Corpus Interaction in Agentic Search](https://arxiv.org/abs/2607.24223)

**<font color=#1a73e8>作者：</font>** Jiangnan Li, Yuqing Li, Mo Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Relevance is a query-dependent estimate of whether a document or excerpt contains useful evidence. Existing retrieval agents use relevance to select top-$k$ content, but document relevance alone cannot localize, compose, or verify the evidence required by complex questions. Direct Corpus Interaction (DCI) enables such fine-grained operations through grep-style exploration, but its relevance-agnostic search can expose useful clues late and delay convergence. Recent advances use relevance to narrow the corpus into a working space for interaction. Once interaction begins, however, relevance still does not directly guide which documents grep searches first or distinguish informative excerpts from a broad set of matches to let LLMs see them first. We introduce the Relevance-Aware RipGrep Search Agent (RARG), which turns relevance into an execution prior for corpus interaction. RARG provides coarse-to-fine relevance guidance: it orders documents for sequential 'ripgrep' traversal to expose globally relevant clues earlier, initializes promising entry points with query-relevant paragraphs, and reranks grep matches to surface informative excerpts that document-level ranking may otherwise obscure. Across challenging browse question answering and reasoning-intensive retrieval, RARG improves the accuracy--efficiency frontier over retrieval-based and direct-interaction agents. These results demonstrate that relevance-aware interaction enables faster and more reliable search convergence.

---


### 192. [Generative Artificial Intelligence (GenAI) to convert images of queuing networks into verifiable simulation models: an open-weight LLM workflow approach](https://arxiv.org/abs/2607.24259)

**<font color=#1a73e8>作者：</font>** Thomas Monks, Alison Harper, Amy Heather 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has explored the use of Large Language Models (LLMs) to automate simulation model building, typically by generating executable code directly from natural language descriptions. However, this raises challenges for verification and reproducibility particularly for users without programming expertise. We propose Sketch2DES, a sketch-to-simulation workflow that converts diagrammatic representations of queuing networks into verifiable discrete-event simulation models using open-weight LLMs. The workflow has three stages: (1) translation of a diagram into a semi-structured textual description using a multimodal LLM; (2) conversion into schema-validated structured data (JSON) via an LLM with a reflection-based verification loop; and (3) deterministic transformation into an executable simulation model using a software adapter. Intermediate artefacts can therefore be inspected and automatically validated before execution. We evaluate the approach on eight queuing-network diagrams of varying complexity. The workflow achieved high reliability for all stages, and results were statistically indistinguishable from human-coded and analytical benchmarks. Compared to direct code generation, the workflow improves reproducibility, transparency, and verifiability, while reducing the need for programming expertise. Limitations include restricted model scope and dependence on accurate visual interpretation. The results demonstrate the feasibility of structured, workflow-based model generation as a robust foundation for LLM-assisted simulation modelling.

---


### 193. [KAP: Bridging the Knowledge Selection-Runtime Consumption Gap in LLM Systems](https://arxiv.org/abs/2607.24260)

**<font color=#1a73e8>作者：</font>** Shuo Wang, Fang Xi, Wenyuan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLM systems increasingly rely on knowledge-selection processes that produce high-value structured priors, such as ranked evidence, graph topology, multimodal alignment, and confidence signals. Yet LLM serving remains fundamentally oblivious to this rich structure: once such signals are serialized into a prompt, the backend observes only a flat token sequence, forcing dense and uniform consumption of the full key-value (KV) state during decoding. We term this architectural mismatch the Knowledge Selection-Runtime Consumption (KSRC) gap: richer contexts enlarge the full-prompt KV footprint and decode-time memory traffic, increasing latency and degrading throughput even when reasoning depends on only a small fraction of the context. To bridge the gap, we propose Knowledge Access Planning (KAP), a paradigm-shifting execution abstraction that elevates structured knowledge priors from passive prompt-construction hints into first-class physical execution artifacts. KAP establishes a universal intermediate representation (IR)-the runtime access plan-which compiles structured knowledge signals to govern physical KV access without altering logical prompt semantics, model weights, or training procedures. Through this IR, KAP shifts LLM serving from token-aware context consumption to plan-driven, knowledge-aware runtime consumption. We instantiate KAP with GraphSpec, a compiler-executor realization connecting structured knowledge selection to an LLM serving backend. We derive a phase-boundary model for the positive-speedup regime of plan-guided execution. Across 4K-128K long-context QA workloads, GraphSpec maintains answer quality comparable to full-context decoding while decoupling physical KV consumption from prompt length, reducing proposal-time KV access to 5.5% of source KV state at 128K, and fundamentally shifting the scaling trajectory of long-context generation.

---


### 194. [Accuracy Hides How Language Models Fail: Measuring Failure States Under Matched Output Budgets](https://arxiv.org/abs/2607.24268)

**<font color=#1a73e8>作者：</font>** Zongyou Yang, Yinghan Hou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-model benchmarks collapse two distinct measurement questions into a single accuracy score: whether a response reached an evaluable state, and whether its answer was judged correct. We introduce a two-layer evaluation framework that separates scorer-independent execution evidence, including termination, answer exposure, parseability, and completion length, from scorer-dependent correctness. Across 2,550 outputs from five fixed Qwen and DeepSeek configurations on MATH and ARC-Challenge, matched 2,048-token limits produce sharply different execution mixtures: 49 of 450 Qwen MATH outputs terminate without a final answer, compared with 5 of 300 DeepSeek MATH outputs and none of the 750 ARC outputs. Among the same 300 DeepSeek MATH question-model pairs, no missing-final length termination is observed at 8,192 tokens. A coverage-audited targeted verification study further shows that candidate-selection and aggregation policies can substantially alter comparative accuracy estimates. These results demonstrate that accuracy conflates execution case mix with verification policy. Evaluations of test-time methods should therefore report pre-intervention execution states, verification coverage, and scorer provenance alongside accuracy.

---


### 195. [INS-ActBench: A Comprehensive Benchmark for Assessing Professional Actuarial Capability of Large Language Models](https://arxiv.org/abs/2607.24273)

**<font color=#1a73e8>作者：</font>** Changyu Chen, Chenwei Lin, Xian Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong potential in financial reasoning, but existing benchmarks often evaluate domain knowledge, numerical reasoning, long-context understanding, and tool use in separate settings. This limits their ability to assess realistic professional workflows that require auditable, context-grounded, and tool-executable decisions. We introduce \textbf{INS-ActBench}, a comprehensive benchmark for evaluating professional actuarial capability in LLMs. INS-ActBench contains 12,050 Q\&A pairs from public exams and sample questions released by 16 actuarial associations. It covers three subsets: \textbf{INS-Act-Know} for standardized actuarial knowledge, \textbf{INS-Act-Case} for long-context insurance case reasoning, and \textbf{INS-Act-Practice} for spreadsheet and R-code tasks with verifiable numerical outputs. Experiments on nine representative LLMs and human actuarial experts reveal a clear capability boundary: frontier LLMs perform strongly on standardized knowledge, but remain much weaker in case reasoning, tool-based workflows, and jurisdiction-sensitive practice. INS-ActBench provides a reproducible foundation for developing actuarial LLMs toward reliable professional assistance. The code is available at this https URL.

---


### 196. [The Tokenizer Tax: Quantifying and Explaining the Cross-Lingual Cost of Subword Tokenization for Indian Languages](https://arxiv.org/abs/2607.24276)

**<font color=#1a73e8>作者：</font>** Priyansh Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) process text through subword tokenizers rather than directly reading characters or words. Because these tokenizers are trained predominantly on English-centric corpora, they introduce a systematic and often overlooked disadvantage for many non-English languages. In this work, we quantify this tokenizer tax for Indian languages using the FLORES-200 parallel corpus, measuring tokenization fertility across six widely used tokenizers and fourteen languages. Under cl100k_base (used by GPT-3.5 and GPT-4), Indian languages experience an average 8.0x tokenization tax relative to English, reaching 13.0x for Malayalam, reducing the effective context window to as little as 12% of that available to English users for equivalent semantic content. We identify the primary mechanism behind this disparity: failed byte-pair merges that leave text fragmented into single-byte tokens, with merge failure strongly correlating with tokenizer tax (Pearson r = 0.89). We further show that this phenomenon is not an inherent property of Indic scripts but a consequence of tokenizer design. Multilingual tokenizers such as XLM-R and OpenAI's o200k_base reduce the average Indic tokenizer tax by 73%, demonstrating that the disparity is largely remediable. Beyond token statistics, we quantify a practical consequence by showing that, under fixed context budgets, Indian-language documents preserve substantially less original content than equivalent English documents. Finally, we examine the relationship between tokenizer fertility and reading comprehension performance on the Belebele benchmark, finding that the apparent correlation is largely explained by language resource availability rather than tokenizer behavior alone.

---


### 197. [From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent Protocol Distillation in Agentic Search](https://arxiv.org/abs/2607.24280)

**<font color=#1a73e8>作者：</font>** Junlin Liu, Jiangwang Chen, Zixin Song 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic search enables large language models to solve knowledge-intensive tasks by interleaving multi-step reasoning with retrieval, yet optimizing this with outcome-based reinforcement learning (RL) provides only sparse supervision. Knowledge distillation can supply denser guidance, and advanced proprietary models with their strong reasoning capabilities are promising teachers. While distilling from proprietary models can densify this supervisory signal, conventional logit-matching is precluded by hidden logits and mismatched tokenizers, whereas raw natural language trajectory imitation transfers superficial stylistic artifacts rather than core reasoning competence. To address the heterogeneous distillation problem and bridge the distribution gap, we propose Multi-Agent Protocol Distillation (MAPD), a joint distillation and RL framework uses a structured, style-normalized protocol as an intermediate representation. An offline multi-agent system (MAS) decomposes each query, retrieves supporting evidence, repairs failed searches, and converts the resulting exploration trace into a JSON protocol containing the task type, reasoning plan, and extractive grounding facts. During training, the protocol is provided only to a privileged branch of the student policy, whose token distributions furnish a dense distillation signal alongside the sparse RL objective. Extensive evaluations across seven QA benchmarks demonstrate that MAPD consistently outperforms competitive distillation and RL, achieving average success rates of 39.4\% on Qwen3-1.7B and 44.4\% on Qwen3-4B. Crucially, the framework generalizes robustly across diverse proprietary teachers while effectively mitigating the student policy from style drift and verbosity degeneration.

---


### 198. [Rethinking the Generation Order of Block Diffusion Language Models](https://arxiv.org/abs/2607.24306)

**<font color=#1a73e8>作者：</font>** Kai Syun Hou, James Kwok  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models enable flexible arbitrary-order generation, but existing sampling methods are mostly designed for early masked diffusion models (MDMs). In this work, we study sampling for recent block diffusion language models (BDLMs). We show empirically and analytically that these models are naturally more aligned with left-to-right decoding than MDMs. Based on this observation, we propose Parallel Autoregressive Decoding (PARD), a simple training-free sampling method that preserves left-to-right unmasking structure while allowing parallel token commitment. Extensive experiments show that PARD consistently outperforms existing parallel samplers in generation quality, while achieving substantial speedups over pure AR decoding with only a small quality gap.

---


### 199. [CONSISTRE: A Unified Consistency-Aware Framework for Document-Level Relation Extraction with Large Language Models](https://arxiv.org/abs/2607.24312)

**<font color=#1a73e8>作者：</font>** Mingxuan Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document-level relation extraction (DocRE) aims to extract relations among multiple entities across extended contexts while maintaining consistency across predicted triples. Although large language models (LLMs) show remarkable reasoning capabilities in information extraction, their predictions are typically generated independently for each candidate triple and may violate fundamental relational constraints such as transitivity, symmetry, and functional uniqueness, leading to contradictory and unreliable outputs. We propose CONSISTRE, a unified consistency-aware framework for DocRE that addresses this limitation through two complementary tracks. The first operates at inference time for black-box LLMs, combining constraint-aware prompting, constraint-based verification, and iterative self-reflection to refine predictions without task-specific fine-tuning. The second injects consistency knowledge into smaller open-source models via a knowledge distillation and reinforcement learning pipeline: reasoning traces from a powerful teacher are distilled into a student via supervised fine-tuning, followed by GRPO alignment using a composite reward that jointly optimizes extraction performance and relational consistency. Together, the two tracks cover both API-accessible and locally deployable scenarios under a unified consistency formulation. Experiments on DocRED show that both tracks outperform their baselines, with the inference-time track achieving competitive F1 using off-the-shelf black-box LLMs and the training-time track substantially narrowing the gap between 7--8B open-source models and state-of-the-art proprietary LLMs at a fraction of their inference cost. Ablation studies confirm that explicit consistency modeling mitigates relational contradictions and enhances the reliability of LLM-based DocRE across both deployment paradigms.

---


### 200. [MEGA-CL: A Molecular Foundation Model for Generalizable ADMET Prediction through Graph External Attention and Contrastive Learning](https://arxiv.org/abs/2607.24314)

**<font color=#1a73e8>作者：</font>** Tinghui Jin, Kedu Jin, Ying Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the absorption, distribution, metabolism, excretion and toxicity (ADMET) properties of small molecules remains a major challenge in drug discovery. Here, we present MEGA-CL, a foundation graph neural network framework for universal molecular ADMET prediction. MEGA-CL integrates self-supervised contrastive learning with a multi-head external attention mechanism and an enhanced message-passing architecture, enabling simultaneous modeling of local chemical substructures and global inter-graph relationships while mitigating over-smoothing effects commonly observed in deep graph networks. Across 13 benchmark datasets and 21 downstream ADMET tasks, MEGA-CL consistently outperforms state-of-the-art baseline models. In particular, the framework demonstrates robust performance on challenging regression tasks, including clearance (CL) and steady-state volume of distribution (VDss), while maintaining strong generalization ability in independent external validation. Clinically relevant predictive accuracy was achieved, with more than 75% of predictions falling within a 3-fold error range. In an external evaluation on 18 novel compounds derived from recently approved FDA drugs, over 50% of human liver microsome clearance (HLMC) predictions were within a 2-fold error range. To further assess its practical applicability, MEGA-CL was prospectively evaluated on three preclinical drug candidates using in vitro hepatic microsomal metabolism assays and CYP450 inhibition assays guided by model predictions. The predicted HLMC values for all candidates were within 2.5-fold of the experimentally measured values, and 73.3% of CYP450 inhibition endpoints (11/15) were correctly classified. These results demonstrate the potential of MEGA-CL as a generalizable framework for accelerating in silico ADMET evaluation and early-stage drug candidate optimization.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-240](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
