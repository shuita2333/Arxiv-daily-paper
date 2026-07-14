# 🧠 大模型相关研究 | 2026年07月15日

> 本类共 **199** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-199](./part-04.md)

---

### 51. [Information-seeking failures of large language models in agentic clinical reasoning](https://arxiv.org/abs/2607.10275)

**<font color=#1a73e8>作者：</font>** Krischan Braitsch, Laura K. Schmalbrock, Theresa Weltermann 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models achieve high scores on medical knowledge assessments, yet clinical reasoning requires actively deciding what to investigate under uncertainty. We developed an agentic evaluation framework in hematologic oncology in which models must proactively request clinical data across three sequential rounds before committing to a diagnosis and treatment plan. Across 32 frontier models, the best achieved only 68% overall accuracy. Information utilization, the fraction of available data actually requested, was the strongest predictor of diagnostic accuracy (R = 0.69, P < 0.001), yet utilization collapsed from 57% to 26% in the final round, leaving molecular and cytogenetic data critical for treatment selection unexamined. Reasoning traces scored high on a clinical reasoning rubric (91% above threshold) but decorrelated from accuracy, revealing a gap between locally coherent rationales and globally correct conclusions. Error analysis identified search satisficing, anchoring and premature closure as the dominant failure modes, the same cognitive biases that characterize novice clinicians under dual-process models of diagnostic reasoning. These findings demonstrate that the primary limitation of current models in clinical oncology is not insufficient medical knowledge but a systematic failure of information-seeking under uncertainty.

---


### 52. [Can Agentic Trading Systems Pay for Their Own Intelligence?](https://arxiv.org/abs/2607.10286)

**<font color=#1a73e8>作者：</font>** Qiqi Duan, Changlun Li, Chen Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly used in trading systems, where model reasoning, tool use, and continual decisions incur costs that are expected to produce trading value. Existing evaluations typically report performance metrics, but rarely examine agentic viability: whether dynamic LLM-mediated decisions convert their induced costs into measurable incremental profit. To apply this criterion, we introduce TradeLens, a trace-grounded diagnostic toolkit for evaluating agentic trading systems from their trading records, runtime traces, and deployment configurations. It reconstructs trading trajectories, attributes profit and cost to interpretable evidence, and diagnoses whether and why an agent pays for its own intelligence. We conduct extensive analysis across backbone models, capital scales, trading frequencies, and system architectures, together with deployment discussion. Our results show that viability hinges on intelligence-to-profit conversion: models exhibit different failure patterns, such as poor asset selection in DeepSeek-V3.2 and negative timing in GLM-4.7, while capital scale, trading frequency, and architecture matter only by amplifying or degrading decision-attributed timing value. These findings reframe the evaluation of LLM-based trading agents from capability-centric performance ranking to trace-grounded diagnosis of intelligence-to-profit conversion. Our code is available at this https URL.

---


### 53. [InterPet4D: A Multimodal 4D Human-Pet Interaction Dataset for Pet Motion Generation](https://arxiv.org/abs/2607.10287)

**<font color=#1a73e8>作者：</font>** Yichen Peng, Jyun-Ting Song, Chen-Chieh Liao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-pet interaction estimation and generation remain underexplored due to the absence of a high-quality large-scale dataset. We present InterPet4D, the first multimodal dataset capturing natural interactions between humans and dogs. Using a synchronized multi-view capture system, we record human-dog obedience tasks and provide annotations for both humans and dogs, including multi-view and egocentric videos, segmentations, 2D and 3D keypoints, meshes, and audio tracks. InterPet4D consists of 6.8 million frames collected from 13 dogs of 11 breeds interacting with 23 human participants. We further introduce the InterPetMoGen framework for human-pet interaction motion generation. Our proposed model achieves an FID score of 11.21 and substantially outperforms the Seq2Seq and DiT baselines, demonstrating the effectiveness of InterPet4D for modeling realistic human-pet interactions.

---


### 54. [SPARK: Susceptibility-Guided Profiling and Steering of Latent Reasoning States in Large Language Models](https://arxiv.org/abs/2607.10296)

**<font color=#1a73e8>作者：</font>** Dongxu Zhang, Yiding Sun, Zihao Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning failures in large language models (LLMs) are usually evaluated from final answers, but a wrong answer does not reveal why the model failed. The same incorrect output may reflect missing capability, an unstable reasoning trajectory, or a failure to activate a reasoning state that is already available in the frozen model. Existing prompting and benchmark-based evaluation methods mostly operate at the output level, while generic activation-steering methods typically apply global directions without diagnosing which examples require intervention. In this paper, we introduce SPARK, which uses hidden-state response to diagnose whether a model internally enters an effective reasoning state and to guide lightweight test-time steering. The key observation is that raw hidden-state susceptibility is strongly confounded by prompt length, especially in programmatic and algorithmic reasoning where harder serialized instances naturally become longer. SPARK therefore uses length-controlled susceptibility to separate input-scale effects from residual reasoning activation, and combines this signal with cross-layer coordination to select reasoning-active anchors and under-activated hard examples. We use FRONTIER-4.5K as a controlled programmatic reasoning suite for latent profiling and difficulty-aware analysis, and evaluate SPARK-Steering on GSM8K and MATH-500 with forward-only benchmark profiling. Our method improves Qwen3 series models consistently; on MATH-500, accuracy rises from 82.0% to 84.6% for Qwen3-4B and from 82.4% to 85.6% for Qwen3-8B. These results suggest that susceptibility can serve not only as a diagnostic signal for reasoning failures, but also as a practical guide for targeted test-time intervention.

---


### 55. [Empowering Long-form Omni-modal Understanding with Robust Audio Perception](https://arxiv.org/abs/2607.10299)

**<font color=#1a73e8>作者：</font>** Kaiying Yan, Luoyi Sun, Xiao Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in large-scale multimodal models have drivenremarkable progress in vision-language tasks; however, comprehensiveomni-modal understanding remains under-explored, largely due to thescarcity of datasets with rich, explicitly aligned auditory cues. To bridgethis gap, we present AVDC (Audio-Visual Decoupled Captions), a large-scaledataset designed to disentangle visual and auditory semantics. Specifi-cally, we propose an automated pipeline that leverages off-the-shelf mod-els to annotate videos with tripartite captions: visual-only (V), audio-only (A), and joint audio-visual (AV). This decoupled structure explic-itly captures both modality-specific nuances and complex cross-modalinteractions. Building upon this, we introduce AVDC-QA-CoT, a Chain-of-Thought augmented question-answering dataset to foster audio-visualreasoning. To fully exploit these resources, we employ a two-stage train-ing paradigm: omni-modal caption generation pre-training on AVDC, fol-lowed by instruction tuning on AVDC-QA-CoT. Extensive experiments acrossdiverse downstream tasks, spanning video captioning, audio-centric anal-ysis, and omni-modal benchmarks, demonstrate consistent and signifi-cant performance gains, showing the efficacy of our proposed datasetsand training strategy in advancing omni-modal perception. Code anddataset are related on this https URL.

---


### 56. [PolyInterview: An LLM-based Platform for Immersive Mock Interview Practice with Comprehensive Multimodal Assessment](https://arxiv.org/abs/2607.10310)

**<font color=#1a73e8>作者：</font>** Zhiyuan Wen, Jiannong Cao, Zijian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preparing for job interviews is important for securing desired positions, yet realistic practice remains difficult to access: real interviews are infrequent, expert mock coaching is costly, and self-practice offers neither adaptive dialogue nor structured assessment. Existing systems typically address only parts of this need through fixed question sequences, limited communication channels, or feedback with little supporting evidence. We present PolyInterview, an LLM-based platform for immersive mock interview practice with comprehensive multimodal assessment. PolyInterview uses the target job description and CV to generate questions tailored to the role and candidate, conducts multi-turn spoken interviews with a lip-synced digital human interviewer that asks answer-aware follow-up questions, and evaluates response content, vocal delivery, and non-verbal behavior. Four parallel evaluators produce 13 behavior-level features that are aggregated into 10 assessment aspects and two competency tracks. Guided by the KSA and STAR frameworks, the report links each score to behavioral evidence and actionable recommendations. PolyInterview is publicly accessible. Its current all-account snapshot contains 101 accounts, 1,564 interview sessions, 7,665 generated questions, and 1,422 five-stage question sets. Generated questions are more closely aligned with their matched job description than with cross-role job descriptions in 93.7% of sessions. An evaluation by ten experts found strong question plans and actionable feedback.

---


### 57. [Imperceptible and Reversible Adversarial Examples against Vision-Language Models for Privacy Protection](https://arxiv.org/abs/2607.10329)

**<font color=#1a73e8>作者：</font>** Qi Lu, Ziqi Zhou, Yufei Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) offer powerful multimodal ability but also expose users to text-based privacy attacks where adversaries crawl online photos and query VLMs to extract sensitive attributes. Existing reversible adversarial example (RAE) methods protect images in purely visual tasks but fail in multimodal settings, and current adversarial examples on VLMs rely on high frequency noise that severely degrades visual quality. We propose CloakDiff, the first framework for reversible, high fidelity privacy protection against text-based query attacks in VLMs. CloakDiff produces imperceptible adversarial examples by combining diffusion based adversarial editing with an invertible network that embeds the original image for lossless recovery. It perturbs both pixel space embeddings and manipulates latent cross attention maps to ensure strong cross-model and cross-prompt transferability while preserving global visual structure. To further enhance fidelity, we design EDM Heuristic Sampling, a principled diffusion schedule for adversarial guidance. Experiments on multiple datasets and VLMs demonstrate that CloakDiff delivers multimodal privacy preservation with high visual quality and reversibility.

---


### 58. [Benchmarking the Robustness of Foundation Models for Mammography under Domain Shift](https://arxiv.org/abs/2607.10358)

**<font color=#1a73e8>作者：</font>** Giang Nguyen, Raghav Mehta, Emma A.M. Stanley 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly used as image feature extractors for mammography, but their robustness under external domain shift remains unclear. We benchmark 15 foundation-model backbones across breast density, BI-RADS severity, and cancer status using a unified frozen-backbone linear-probe protocol, training on 3 source datasets and evaluating on 12 task-compatible out-of-distribution (OOD) datasets after label harmonization. Mammography-specific vision-language models (Mammo-FM and MaMA) provide the strongest mean OOD performance, but robustness is not explained by mammography exposure alone. DINOv3 remains a competitive vision-only baseline, and mammography-adapted pretraining does not consistently improve generalization. Dataset-level analysis further shows that even leading models show heterogeneous performance across datasets. Feature-space inspection reveals that useful representations can preserve clinical signal while retaining dataset and acquisition structure. These findings highlight dataset-level OOD evaluation as a central criterion for assessing mammography representations. Our code is publicly available: this https URL.

---


### 59. [A Control Theory of Predictability in Latent World Models](https://arxiv.org/abs/2607.10362)

**<font color=#1a73e8>作者：</font>** Hanzhe You, Yonggang Zhang, Maohao Ran 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models are trained to predict future states in a learned representation and are then deployed inside a planner that selects actions by simulating them forward. Current practice adopts the prediction error, the single- or multi-step rollout loss on held-out data, as the training and model-selection objective, on the assumption that a lower prediction error yields better control. We show that this assumption is unreliable for a structural reason: a planner does not query the model on the training distribution but on the states that its candidate actions reach, which generally leave the data manifold, so an error averaged over the data cannot by itself govern control. We therefore reframe the objective as the discrepancy between the predicted and the true plan-cost at the plan the planner commits to, and prove that the planner's suboptimality is bounded by twice this discrepancy, whereas the data-averaged prediction error neither bounds nor tracks it. Under a linear-control premise the discrepancy separates into two terms. The first is a small on-manifold residual, on which the predicted and true dynamics agree and which a spectral tax prices through the non-normality of the latent transition operator. The second is an off-manifold divergence, on which an action carries the state off the manifold and the two dynamics diverge; this divergence is the binding term and is bounded by no data-averaged error. Synthetic operators confirm the pricing formulas, and latent model-predictive control experiments confirm the decoupling: across seeds, the single-step validation error is essentially uncorrelated with control success, whereas a fidelity score on the planner-reachable measure tracks it.

---


### 60. [ABot-N1: Toward a General Visual Language Navigation Foundation Model](https://arxiv.org/abs/2607.10383)

**<font color=#1a73e8>作者：</font>** Ruiyan Gong, Yingnan Guo, Junjun Hu 等 40 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Language Navigation foundation models aim to unify deep reasoning for grounded spatial decisions with broad versatility for diverse embodied tasks. Current approaches typically achieve this integration via monolithic policies that map observations directly to actions, yet they often suffer from coordinate drift and poor handling of long-tail semantics. Furthermore, these black-box mappings lack interpretability, hindering the simultaneous achievement of generality, robustness, and transparency. We present ABot-N1, a step toward a general Visual Language Navigation foundation model, that addresses these challenges by decoupling cognition from control via a slow-fast architecture guided by dual visual-language signals. More specifically, a slow vision-language reasoner performs explicit Chain-of-Thought reasoning while producing a pixel goal. This compact set of image-space anchor points serves as a universal interface for diverse tasks, including point-goal, object-goal, poi-goal, instruction-following, and person-following. Subsequently, a fast action expert leverages both the textual cues and the pixel guidance to generate continuous waypoints at the native control frequency. By bridging high-level intents and low-level control through pixel-grounded anchors paired with explicit linguistic traces, our approach ensures robust, generalizable, and interpretable navigation across simulation and real-world benchmarks. ABot-N1 establishes new state-of-the-art records, delivering massive gains specifically in urban-scale navigation: boosting POI arrival by 35.0% (to 77.3%) and achieving 95.4%/92.9% SR in complex indoor and outdoor scenes. It also maintains superior robustness across object-reaching, person-following, and instruction-following tasks. New Point-Goal/POI-Goal benchmarks are released as open source to advance the field of urban-scale navigation.

---


### 61. [Structured Thoughts For Improved Reasoning And Context Pruning](https://arxiv.org/abs/2607.10386)

**<font color=#1a73e8>作者：</font>** Zain Sarwar, Supriyo Chakraborty, Berkcan Kapusuzoglu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at generating long chains of thought, but long reasoning traces are often verbose and memory-inefficient. In this work, we introduce Structured Thoughts, a framework that organizes reasoning into alternating <try> and <outcome> blocks: <try> captures exploratory scratch work, while <outcome> contains the distilled conclusion of that step. We construct a dataset of structured thoughts by segmenting reasoning traces into <try> blocks and prompting an LLM to summarize each step into its corresponding <outcome>. Fine-tuning pretrained foundation models on this reformatted data produces models that adopt the structured reasoning style, leading to performance gains of up to 8.08\% on reasoning benchmarks compared to standard SFT. The explicit structure also enables context pruning: after each <try>/<outcome> pair, the <try> can be pruned, allowing the model to retain conclusions without keeping the full scratch work in the context. A proof-of-concept pruning implementation achieves an average of 85\% memory / context savings with an 8.67\% performance drop across mathematical tasks.

---


### 62. [Enjoy Your Talk: A Human-Centered Benchmark for Multi-Turn Dialogue with Decoupled User Simulation, Target Modeling, and Judging](https://arxiv.org/abs/2607.10428)

**<font color=#1a73e8>作者：</font>** Jinglan Gong, Jiefan Lu, Hewei Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) as multi-turn conversational partners requires probing capabilities that single-turn benchmarks miss: persona consistency, evolving intent tracking, emotional dynamics, and goal completion. We introduce EYT-Bench, a human-centered benchmark built around a three-party decoupled design: a persona-grounded user simulator, a target model that separates intent perception from response generation, and an independent third-party LLM judge with optional multi-judge ensembling. Personas are sampled from public human-curated corpora, Nemotron-Personas-USA and PersonaMem-v2, rather than synthesized, reducing LLM-induced persona bias. EYT-Bench also introduces two trajectory-level metrics: embedding-based intent drift and final-intent completion rate (FICR), inspired by tau-bench. In a 17-target x 200-dialogue evaluation, EYT-Bench reveals four findings: (i) state-of-the-art closed- and open-source models are statistically close on subjective dimensions (empathy / persona / anthropomorphism vary within <= 0.3), but differ by up to 9x on objective intent tracking; (ii) reasoning ("thinking on") sharply improves objective tracking on long-context personas (+0.47-0.50 latent-intent accuracy on Gemma-4) while leaving subjective scores nearly unchanged; (iii) persona format dominates trajectory spread, with FICR saturating above 0.95 on Nemotron-USA but spreading from 0.53 to 0.88 on PersonaMem-v2; and (iv) the warm-up effect is robust on 16/17 models (one outlier, GPT-5.5, reverses the effect), with stable rankings across alpha in [0.05, 0.15]. A cross-judge ablation using deepseek-v4-pro confirms that target rankings and final-intent satisfaction are preserved across judges.

---


### 63. [ANCHOR: Automated Alignment Auditing for CLI Agents on Real-World Harm](https://arxiv.org/abs/2607.10455)

**<font color=#1a73e8>作者：</font>** Kefan Song, Yanjun Qi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous CLI agents can now execute hundreds of actions across multi-hour sessions: writing code, executing shell commands, browsing the web, and managing cloud infrastructure, all with minimal human oversight. Does greater autonomy invite greater risk? We introduce ANCHOR, an automated auditing framework that stress-tests CLI agents on illegal tasks grounded in public US court cases. ANCHOR deploys an auditor agent fine-tuned on dark personality data using supervised and reinforcement fine tuning. This auditor roleplays persistent malicious users who decompose tasks, reframe requests upon refusal, and adapt strategies across multi-turn interactions. Evaluating frontier CLI agents, we find that while they often refuse illegal tasks when prompted directly, compliance reaches 100\% under persistent malicious interaction. When agents comply, they frequently exceed user requests, autonomously building infrastructure for large-scale harm, including catastrophic risk scenarios such as large-scale financial fraud and bioweapon development. These findings demonstrate that current alignment techniques are insufficient for autonomous agents and underscore the need for safety evaluations against persistent, adaptive malicious users. We release ANCHOR at this https URL

---


### 64. [GRASP: GRanularity-Aware Search Policy for Agentic RAG](https://arxiv.org/abs/2607.10463)

**<font color=#1a73e8>作者：</font>** Varun Gandhi, Jaewook Lee, Shantanu Todmal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic retrieval-augmented generation (RAG) extends static RAG by allowing language models to iteratively reason, generate search queries, retrieve evidence, and predict answers. However, it remains challenging for models to decide when to retrieve, whether to use lexical matching or semantic similarity, and how to control context granularity to prevent irrelevant tokens from interfering with agent reasoning. In this paper, we introduce GRASP, a reinforcement learning (RL) framework for training agents to adaptively coordinate complementary retrieval tools during multi-step reasoning. GRASP provides the agent with semantic search, keyword search, and paragraph-reading actions, enabling it to retrieve sentence-level evidence and expand further context only when needed. We train the policy with a reward that jointly accounts for answer accuracy, grounded reading, complementary search, and turn efficiency. Experiments on multi-hop reasoning benchmarks show that GRASP improves both retrieval recall and downstream question answering performance compared with single-step retrieval, prompting-based agentic RAG, and RL-based retrieval baselines. Qualitative and ablation analyses show that the learned policy develops interpretable skimming and scanning behavior: it uses semantic search for broad exploration, paragraph reading for local verification, and keyword search for entity-specific evidence. These results suggest that learning to coordinate retrieval signals and context granularity is critical for agent's correct reasoning.

---


### 65. [Reinforcement Learning with Verifiable Physics: Post-training LLMs with Continuous Rewards](https://arxiv.org/abs/2607.10474)

**<font color=#1a73e8>作者：</font>** Pengfei Cai, Utkarsh Utkarsh, Alan Edelman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial differential equations (PDEs) are foundational to modeling in science and engineering, but constructing reliable numerical solvers remains labor-intensive, demanding expert knowledge of discretization schemes, stability conditions, and boundary treatments. Recent work has begun to frame PDE solving as a code-generation task for large language models (LLMs), yet existing approaches operate primarily at inference time: relying on prompting, debugging, self-refinement, and test-time scaling rather than adapting the model itself. In parallel, reinforcement learning with verifiable rewards has emerged as a post-training paradigm for code and math reasoning, but its verifiers are typically binary: a compiler runs, or a test passes. Such signals discard the graded structure of scientific correctness, where two solvers may both execute and yet differ in solution accuracy by orders of magnitude. In this work, we introduce RLVP: Reinforcement Learning with Verifiable Physics, an RL post-training framework for multi-PDE solver code generation. RLVP addresses this verifiability gap with a hybrid verifier: hard program-validity checks ensure executability, while continuous physics rewards score function-space accuracy and PDE-residual consistency. A single policy is post-trained across diverse PDE families spanning hyperbolic, parabolic, elliptic, and incompressible-flow systems. RLVP improves over both pre-trained and supervised-only baselines on PDE benchmarks, and shows zero-shot improvement transfer to held-out PDEs. We show that a smaller LLM post-trained with RLVP can outperform prompting a frontier model on in-distribution PDE solver generation. The trained policy shows evidence of compositionality in numerical motifs: it recombines stencils, time-stepping schemes, and boundary-handling primitives learned from the PDEs used in training into generated solvers for unseen PDE problems.

---


### 66. [Hallucination Detection in Large Language Models Using Diversion Decoding](https://arxiv.org/abs/2607.10476)

**<font color=#1a73e8>作者：</font>** Basel Abdeen, S M Tahmid Siddiqui, Meah Tahmeed Ahmed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have emerged as a powerful tool for retrieving knowledge through seamless, human-like interactions. Despite their advanced text generation capabilities, LLMs exhibit hallucination tendencies, where they generate factually incorrect statements and fabricate knowledge, undermining their reliability and trustworthiness. Multiple studies have explored methods to evaluate LLM uncertainty and detect hallucinations. However, existing approaches are often probabilistic and computationally expensive, limiting their practical applicability. In this paper, we introduce diversion decoding, a novel method for developing an LLM uncertainty heuristic by actively challenging model-generated responses during the decoding phase. Through diversion decoding, we extract features that capture the LLM's resistance to produce alternative answers and utilize these features to train a machine-learning model to develop a heuristic measure of the LLM's uncertainty. Our experimental results demonstrate that diversion decoding outperforms existing methods with significantly lower computational complexity, making it an efficient and robust solution for evaluating hallucination detection.

---


### 67. [ARMOR: Stabilizing On-Policy LLM RL with Off-Policy Anchor Samples](https://arxiv.org/abs/2607.10481)

**<font color=#1a73e8>作者：</font>** Kexin Huang, Junkang Wu, Jinda Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has significantly enhanced the reasoning capabilities of large language models (LLMs), yet the training process remains notoriously fragile. In this work, we investigate a critical source of this instability: over-optimization, where models exploit training heuristics at the expense of generalizable reasoning. While reverse KL regularization is the standard defense against such degradation, our analysis reveals that it is often insufficient in this regime, as it fails to ensure comprehensive coverage of the reference distribution. To address this, we propose ARMOR (Anchor Rollout and Mixed Optimization for RL), a framework that shifts the paradigm from passive penalty to active sample stabilization. ARMOR comprises two key components: (1) Anchor Rollout, which leverages off-policy data from the reference policy to preserve established solution patterns; and (2) Mixed Optimization, which reformulates the policy objective to enable controlled exploration without relying on auxiliary losses. Extensive experiments on reasoning benchmarks validate that ARMOR effectively mitigates validation collapse, enabling sustained performance improvements over extended training horizons.

---


### 68. [EvidentialRAG: Quantifying and Mitigating Information Conflict in Multi-Source Retrieval-Augmented Generation via Evidential Deep Learning](https://arxiv.org/abs/2607.10491)

**<font color=#1a73e8>作者：</font>** S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation grounds large language models in external evidence, but most pipelines still treat retrieved passages as deterministic and mutually consistent context. In open information environments, retrieved sources may disagree because of temporal drift, source error, ambiguity, or genuine uncertainty. This paper introduces ERAG, an uncertainty-aware RAG framework that converts retrieved chunks into probabilistic evidence before generation. A lightweight evaluator extracts candidate claims and maps chunk-level support to Dirichlet evidence. A conflict-preserving Dempster-Shafer fusion rule then transfers unresolved disagreement into epistemic uncertainty rather than normalizing it away. The generator is routed to direct answering, conflict-aware answering, or abstention according to the fused uncertainty score. Experiments on CRAG, ConflictQA, and MuSiQue show that ERAG remains competitive with the strongest matched baseline on standard question answering while improving behavior under conflict. On the CRAG ambiguous subset, hallucination decreases from 45.3% for Corrective RAG to a human-calibrated estimate of 34.8%, conflict resolution increases from 35.2% to 51.2%, and expected calibration error improves to 0.122. These results suggest that evidential modeling is a practical mechanism for trustworthy information processing in foundation-model-based retrieval systems.

---


### 69. [Articulate Intuition or Genuine Analysis? Benchmarking Epistemic Reliability in LLM-as-a-Judge Peer Reviews](https://arxiv.org/abs/2607.10511)

**<font color=#1a73e8>作者：</font>** Nuo Chen, Qian Wang, Qingyun Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When an LLM judge calls a peer review analytical and a human committee calls another review high quality, are they tracking the same thing? We argue they are not, and that the difference matters philosophically. We operationalise Kahneman's dual-process theory into a structured rubric for peer review and release Kahneman4Review, a benchmark of 3,563 rated reviews scored along nine theoretically motivated textual dimensions, eight bias diagnostics, and a continuous reasoning-quality score. Three findings bear on trustworthiness: decision tier is not detectably aligned with the rubric's text-grounded epistemic-quality proxy; public-showcase agentic reviews receive higher raw scores than pooled human reviews, but length and venue explain most of the gap and the samples are not paper-paired; and ICLR review-text diagnostics shift at the 2022--2023 transition, temporally coincident with widespread LLM availability but without identifying its cause. A matched function-probe pilot further shows that the rubric distinguishes textual probes designed to contrast genuine fault-finding with surface fluency. We argue that a trustworthy reliability benchmark for LLM judges must separate analytical form from epistemic function, and propose concrete design choices toward that goal. An interactive demo is available at this https URL.

---


### 70. [Conditional Optimal Bridge for Riemannian Activation Steering](https://arxiv.org/abs/2607.10517)

**<font color=#1a73e8>作者：</font>** Seyed Arshan Dalili, Ajay Narayanan Sridhar, Vijaykrishnan Narayanan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering offers a lightweight alternative to fine-tuning for controlling large language models at inference time. While many existing methods implicitly optimize a log-density-ratio objective between desired and undesired activation distributions, they do so heuristically rather than deriving it from a principled optimization problem. Moreover, these methods produce query-independent steering directions that can degrade performance on both in-distribution and out-of-distribution (OOD) inputs. We introduce \textsc{Cobras} (Conditional Optimal Bridge for Riemannian Activation Steering), which addresses both limitations by casting activation steering as a Schrödinger Bridge on the residual-stream hypersphere. This formulation yields, to our knowledge, the first principled derivation of the log-density-ratio steering objective from a well-posed optimization problem. Solving the bridge via entropic optimal transport and extracting the probability flow ODE recovers the widely used density-ratio gradient as a special case when the Sinkhorn potentials are uniform. Crucially, the Schrödinger potentials are evaluated at the current activation, making the resulting steering direction inherently query-adaptive. Empirically, across four models and three alignment axes (helpfulness, truthfulness, and detoxification), \textsc{Cobras} consistently outperforms prior activation steering baselines while avoiding the OOD degradation commonly observed in existing methods. The code can be found at this https URL.

---


### 71. [Towards Autonomous and Auditable Medical Imaging Model Development](https://arxiv.org/abs/2607.10522)

**<font color=#1a73e8>作者：</font>** Shengyuan Liu, Jia-Xuan Jiang, Boyun Zheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are beginning to automate machine learning engineering (MLE) by coupling planning, code execution, debugging, and empirical feedback. Translating this capability to medical imaging remains difficult because each task imposes modality-specific experimentation and strict requirements for validation protocols and prediction artifacts. Here we introduce AMID, an autonomous multi-agent framework for medical imaging model development. AMID first proposes Data-Conditioned Method Planning, which refines coarse task-level search spaces into executable, parallelizable method lanes grounded in task-specific data analysis and runnable medical-imaging resources. It then develops Verification-Guided Two-Stage Optimization, moving from broad early exploration of diverse method lanes to selective exploitation of promising candidates while enforcing strict verification of validation protocols, metric computation, and prediction artifacts throughout the optimization. Across 20 medical imaging challenge tasks spanning diverse modalities and prediction types, AMID outperformed evaluated general-purpose MLE systems and, on several tasks, approached or matched strong human-designed challenge solutions. These results suggest that AMID can turn task-specific medical imaging model development from bespoke manual engineering into an agentic workflow for producing high-performing and auditable model artifacts across heterogeneous tasks.

---


### 72. [Cross-Layer Misalignment Detection in Agent Skills: A Progressive Loading-Aware Contrastive Learning Approach](https://arxiv.org/abs/2607.10534)

**<font color=#1a73e8>作者：</font>** Chengjun Zhang, Yang Gao, Jianna Hur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly extended through Agent Skills, reusable artifacts that package natural-language metadata, procedural instructions, and execution-time resources for runtime use. As open-source skill marketplaces expand, users and agents increasingly rely on brief metadata to select third-party skills, making it difficult to detect inconsistencies between a skill's description and its true behavior, a problem we call cross-layer misalignment. To address this issue, we propose Progressive Loading-Aware Hierarchical Contrastive Learning (PL-HCL), an LLM-based framework that detects misalignment by modeling the layered structure of Agent Skills and learning cross-layer consistency. Using a normalized corpus of over 264,000 open-source skills and a human-verified challenge set, PL-HCL improves Macro-F1 from approximately 0.45 for unadapted baselines to 0.87-0.89 across evaluated LLM backbones. This approach offers an effective screening tool for users and operators, as well as design principles for detecting inconsistencies in layered digital artifacts.

---


### 73. [LLM-PDESR: Robust PDE Discovery via Subdomain Weighted Residuals and LLM-Guided Symbolic Hypothesis Generation](https://arxiv.org/abs/2607.10546)

**<font color=#1a73e8>作者：</font>** Jinyang Du, Hao Ma, Xiaohu Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovering governing partial differential equations (PDEs) from noisy observational data is a fundamental challenge in scientific machine learning. Traditional symbolic regression (SR) methods often struggle to identify accurate equations within vast combinatorial search spaces, largely due to their inability to incorporate essential domain-specific prior knowledge. Furthermore, reliance on pointwise evaluations and discrete finite differences inherently amplifies high-frequency noise, creating deceptive fitness landscapes that derail the optimization process. To resolve these bottlenecks, we propose LLM-PDESR, a framework that integrates the structural hypothesis generation of Large Language Models (LLMs) with a mathematically rigorous evaluation environment. By employing C^4-continuous quintic splines for robust differentiation and subdomain weighted residuals as natural low-pass filters, our approach effectively mitigates the fitness landscape distortion that plagues existing methods. A Pareto-driven feedback loop then enables the LLM to iteratively refine candidate equations, balancing predictive accuracy with structural parsimony. We evaluate LLM-PDESR on 23 canonical PDEs and five structurally novel equations (including a multivariate system) specifically designed to preclude dataset memorization and test true discovery capabilities. Demonstrating real-world applicability, the framework successfully extracts a consistent structural skeleton for an interpretable 1D dynamical surrogate (1D-CACE) directly from noisy ERA5 reanalysis data. Extensive experiments and out-of-distribution testing confirm that LLM-PDESR significantly outperforms state-of-the-art methodologies in structural recovery, noise resilience, and the avoidance of spurious complexity and equation bloat.

---


### 74. [UNIBROWSE: A Data-to-Agent Framework for Multimodal BrowseComp](https://arxiv.org/abs/2607.10557)

**<font color=#1a73e8>作者：</font>** Xiyu Wei, Qingwei Zong, Zhuocheng Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal BrowseComp tasks require agents to combine perception, tool use, and long-horizon reasoning over dynamic web content, challenging their ability to handle compositional structure, open-world uncertainty, and multimodal integration across extended interactions. Crucially, real-world multimodal browsing involves three distinct information-flow patterns: text-only, image-to-text, and text-to-image, yet existing data construction methods cover only the text-only and image-to-text patterns, leaving text-to-image largely unaddressed and limiting agent generality and robustness. We introduce UNIBROWSE, a unified data pipeline that for the first time simultaneously generates training data covering all three patterns, augments curated knowledge graphs with live web retrieval for improved fidelity, and introduces a novel metric of exploration degree to filter low-signal instances for efficient reinforcement learning. Through this pipeline, we produce high-quality cold-start tool-use trajectories and exploration-rich QA pairs, and train a 35B-scale agent via supervised fine-tuning and exploration-aware this http URL resulting UNIBROWSE agent achieves state-of-the-art performance on multimodal BrowseComp benchmarks, attaining an average accuracy of 54.4 across five diverse benchmarks -- an improvement of 10.5 points over its base model Qwen3.5-35B-A3B -- and surpassing serveral closed-source agent workflows such as GPT-5 (42.9), Gemini-2.5 Pro (44.8), and Gemini-2.5 Flash (41.3).

---


### 75. [Large language model agents accelerate inverse design of metal-organic frameworks for gas separation](https://arxiv.org/abs/2607.10559)

**<font color=#1a73e8>作者：</font>** Zhaolin Hu, Hehe Fan, Wangyihan Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Metal-organic frameworks (MOFs) offer a highly modular platform for adsorptive gas separation, yet their vast reticular design space makes inverse design difficult under simultaneous constraints of chemical validity, separation performance, and structural diversity. Here, we present LEMO Agent, a large-language-model agent framework for closed-loop inverse design of gas-separation MOFs in MOFid space. LEMO Agent couples language-based candidate generation with MOFid standardization, explicit validity checking, Transformer-based property prediction, structured design memory, and multi-island exploration. Through iterative generate--validate--evaluate--remember cycles, the agent uses feedback from both successful and failed candidates to guide chemically constrained search across linker, metal, and topology choices. We evaluate LEMO Agent on CH$_4$/N$_2$ and CO$_2$/N$_2$ separation tasks. Compared with representative generative, optimization, and agentic baselines, LEMO Agent enriches high-performing candidates, improves predicted separation performance, and maintains broad chemical and topological diversity. Selected candidates are further reconstructed, evaluated by GCMC simulations, and passed through an experimental down-selection workflow based on chemical feasibility and ligand purchasability, leading to initial wet-lab synthesis and SEM characterization. These results demonstrate that large language model agents can serve as interpretable and scalable design engines for accelerating MOF discovery beyond conventional fixed-library screening.

---


### 76. [Laguerre Geometry for Interpreting Large Language Models](https://arxiv.org/abs/2607.10578)

**<font color=#1a73e8>作者：</font>** Chunwei Ma, Russell Wolfinger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing hypotheses represent a concept in an LLM as a single point, a linear direction, or a Gaussian cluster, yet it remains unclear how and why such structures emerge. Here, we show that concept geometry can be precisely characterized via Laguerre Geometry, in which a concept is defined as a region--a Laguerre-Voronoi cell or a union of cells--allowing us to strictly define, measure, and separate concepts. Building on this formulation, we show that finer-grained concept structures, such as inclusion and hierarchy, are naturally revealed by the Laguerre weights. We then push this geometry inside the transformer. Decomposing each layer into piecewise-linear operators, we show that a token's hidden trajectory is governed by two coupled mechanisms: a static tree of self-contained piecewise-linear flow, and a dynamic transport that hops the trajectory across trees when cross-token attention fires. This decomposition yields Geometric Lens, a training-free, hyperparameter-free method for reading out the exact concept a hidden vector encodes at any layer. We also develop Laguerre Autoencoder, a 2D visualizer that renders both the decision geometry and a model's full reasoning trajectory in one view. Finally, we move beyond explanatory geometry toward actionable interpretability, showing that Geometric Lens recovers the correct factual token when a model is prompted with in-context interference. The code is available on GitHub.

---


### 77. [MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference](https://arxiv.org/abs/2607.10582)

**<font color=#1a73e8>作者：</font>** Venkatesha Matam, Keon Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents accumulate heterogeneous context, including system instructions, plans, user turns, retrieved documents, tool outputs, and intermediate reasoning, whose key-value (KV) cache can become a major memory bottleneck. Existing eviction policies generally apply the same attention- or recency-based rule to every token, ignoring semantic structure already available to the agent orchestrator.
We introduce MemDecay, a training-free, region-aware KV-cache eviction policy. MemDecay assigns tokens region-specific base priorities and decay rates, refreshes retention scores when tokens receive attention, and evicts the lowest-scoring pages under a fixed cache budget while allowing critical regions to be pinned. We also provide a procedure for calibrating decay rates from measured attention lifetimes.
We evaluate MemDecay at approximately 450 and 1,700 token contexts using Qwen2.5-1.5B and 3B. Across all settings, attention lifetimes differ by an order of magnitude across regions: system-token half-lives range from 148 to 189 decoding steps, compared with 14 to 16 for scratchpad tokens. Pinning preserves system-region facts at full-cache accuracy in every setting, while no baseline preserves more than 13 of 24. Region-aware retention remains effective as context grows, whereas recency-based retention collapses. Accumulated-attention retention performs better on unpinned content, however, and ablations identify attention-score normalization as the main limitation of the current formulation. These results establish semantic prompt structure as a robust signal for KV-cache management while clarifying how it should be combined with attention-based importance.

---


### 78. [Demographic Prompting at Scale: When More Attributes Hurt LLM--Human Agreement](https://arxiv.org/abs/2607.10590)

**<font color=#1a73e8>作者：</font>** Mahammed Kamruzzaman, Shrabon Kumar Das, Gene Louis Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate how annotator demographic attributes, supplied as prompt cues, shape the alignment between large language model (LLM) predictions and human annotations across five tasks. Using five open-source LLMs, we systematically vary the number and composition of demographic components in the prompt, spanning every combination from single-attribute through full-attribute configurations. Our experiments reveal three principal findings. First, alignment consistently peaks with one to three high-signal attributes and degrades under the full attribute set, establishing a clear over-specification threshold. Second, the overall magnitude of demographic influence on human annotations does not predict which attributes improve LLM alignment; instead, both the learnability and the directional coherence of each attribute's annotation signal need to be considered jointly. Third, neuron probing reveals that specialized activation correlates with alignment gains only under coherent annotation signals, and that activation volume alone does not imply steerability. Together, these results demonstrate that demographic prompting is not a monolithic intervention: its utility is highly context-dependent, shaped by attribute signal quality, task characteristics, and model architecture.

---


### 79. [Anomalous Frame Detection by Grouping Frame Similarities between Two Videos Computed by Vision-Language Model to Extract Expert Workers' Unique Actions](https://arxiv.org/abs/2607.10598)

**<font color=#1a73e8>作者：</font>** Ryo Sakai, Yongpeng Cao, Nobutaka Kimura  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maintenance of critical infrastructures, such as railways and power plants, is essential for operational safety and reliability. However, the declining number of skilled maintenance workers poses a serious challenge to sustaining these operations, highlighting the need to effectively transfer expert know-how to less experienced workers. Although traditional interview-based approaches have been used to elicit maintenance skills, they struggle to capture know-how that experts themselves may not consciously recognize. To address this gap, we proposed a method that detects anomalous frames of candidate actions including know-how by comparing a video of manual-based work with that of expert maintenance workers. In a simulated maintenance experiment involving a distribution board, our method targeted 11 types of actions not described in the manual and achieved a 66.9% extraction rate, marking a 50-percentage-point improvement over conventional techniques. These findings underscore the effectiveness of our approach in revealing hidden maintenance knowledge, thereby contributing to enhanced skill transfer and workforce development in critical infrastructure maintenance.

---


### 80. [MRUF: Multi-granularity Routing with Uncertainty-Aware Fusion for Robust Multimodal Sentiment Analysis](https://arxiv.org/abs/2607.10599)

**<font color=#1a73e8>作者：</font>** Haoran Ma, Yinfeng Yu, Liejun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment analysis relies on language, visual, and acoustic cues, but utterance-level modality quality may vary due to occlusion, background noise, motion blur, or imperfect transcripts, causing conventional fusion to over-trust unreliable modalities. We propose MRUF, a reliability-aware fusion method that combines multi-granularity routing with uncertainty-aware calibration. MRUF summarizes sentiment-relevant representations, performs subspace- and modality-level routing, and supervises modality routing with leave-one-out error increases to estimate utterance-level modality importance. It further predicts modality-wise uncertainty and refines modality gates through inverse-variance reweighting, while modality-invariant contrastive alignment stabilizes the shared representation space. Experiments on CMU-MOSI and CMU-MOSEI under aligned and unaligned settings show consistent improvements over strong baselines, and mechanism analysis verifies that modalities with higher predicted uncertainty receive lower fusion weights.

---


### 81. [Agentic-DPO: From Imitation to Agentic Policy Optimization on Expert Trajectories](https://arxiv.org/abs/2607.10601)

**<font color=#1a73e8>作者：</font>** Yixiong Chen, Alan Yuille  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are commonly trained from expert trajectories using supervised fine-tuning (SFT), which treats multi-turn agent behavior as ordinary text imitation. This recipe is simple and low-cost, but it only learns to imitate the sequence of expert actions, rather than training the agent to choose the right action against plausible mistakes at each state. Existing methods to mitigate this problem include preference learning or reinforcement learning, but they usually need high-cost environment rollouts and reward models. We propose Agentic-DPO, a lightweight offline agent policy optimization method that turns expert trajectories into state-conditioned preference supervision. At each expert action state, Agentic-DPO samples a one-step action from the current state, treats plausible wrong actions as negatives, and contrasts them with the expert action using a DPO-style preference objective. To avoid mixing both policy and schema in preference learning, we introduce Policy-Preserving Augmentation (PPA), which renders the same latent trajectory under multiple schemas while keeping the expert policy fixed. Agentic-DPO requires no online environment rollout, reward model, or full-trajectory student exploration. We conduct experiments across StableToolBench, tau-bench retail, and Mind2Web, where Agentic-DPO consistently improves agents at different model scales beyond imitation. In particular, it raises tau-bench accuracy from 21.7% (SFT) to 41.4% for a 9B model, matching online GRPO under the same backbone with only step-level rollouts and without environment interaction during gradient steps. The results suggest that expert trajectories can support low-cost agentic policy optimization when converted from demonstrations into state-level action preferences. Code for Agentic-DPO is released at this https URL.

---


### 82. [U-Lens: Supporting User Uncertainty Management in Long-Form LLM Responses](https://arxiv.org/abs/2607.10604)

**<font color=#1a73e8>作者：</font>** Yu Mei, Qingyue Zhuang, Jie Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate long-form answers for knowledge-intensive tasks, but users often struggle to decide which parts of a response deserve scrutiny, why they may be unreliable, and what to do next. Prior work on uncertainty communication has largely focused on making uncertainty visible through cues such as confidence scores, leaving less support for the broader process of managing uncertainty distributed across a long response. Through a formative study, we examine how users manage such uncertainty across three stages: interpretation, evaluation, and decision. Based on these insights, we derive design guidelines that address both stage-specific and cross-stage needs: uncertainty target representation, evaluative explanation, response guidance, and interactive presentation. We instantiate these guidelines in U-Lens, an uncertainty-management support system that organizes uncertain information in long-form responses into contextual inspection targets, prioritizes them for attention, and connects each target with evaluative context and response options. We evaluated U-Lens in a controlled within-subjects study with 18 participants, comparing it against a confidence-cue baseline. Our results show that U-Lens improved verification efficiency and effort allocation, lowered perceived workload, and strengthened perceived support across interpretation, evaluation, and decision stages. This work reframes uncertainty support for generative AI from presenting isolated, text-centered cues toward supporting the user-centered process of interpreting, evaluating, and acting on uncertain information.

---


### 83. [WasteAssistant: Regulation-Guided Visual Question Answering Framework for Intelligent Waste Segregation and Sustainable Managemen](https://arxiv.org/abs/2607.10610)

**<font color=#1a73e8>作者：</font>** Khush Kataruka, Harshit Maurya, Anuja Vats 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient waste segregation is critical for sustainable urban management and environmental governance. Existing automated systems are limited by single-modality visual processing, insufficient contextual understanding, and weak regulatory alignment. To address these issues, we propose a language-guided vision-AI framework that integrates vision-language models and multimodal large language models for joint visual-linguistic reasoning. This framework implements a visual question answering paradigm aligned with India's Solid Waste Management Rules 2016. We construct a new WasteVQA dataset with 13,500 question-answer pairs across 21 waste categories. Experiments show that the BLIP-based model achieves a BLEU score of 0.8291 and a BERTScore of 0.9273, outperforming traditional CNN-based methods. This work improves source-level segregation accuracy, ensures regulatory compliance, and supports scalable deployment for municipal and citizen-facing waste management, promoting multimodal AI in sustainable urban infrastructure. The source code and dataset are available at: this https URL

---


### 84. [Eval-Pair Matrix: Answer-Paired Meta-Evaluation of LLM Judges for Grounded RAG](https://arxiv.org/abs/2607.10626)

**<font color=#1a73e8>作者：</font>** Sriram Selvam, Anneswa Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge evaluation is widely used for retrieval-augmented generation (RAG), but reusing the same model family as both generator and judge makes self-leniency difficult to identify. We introduce Eval-Pair Matrix, a controlled meta evaluation protocol for source-grounded RAG. Starting from GaRAGe questions and grounding passages, we induce one hidden answer-causal contradiction per record, generate answers from perturbed passages with GPT, Grok, and Gemini models, and then use the same models as blind judges to evaluate each answer against the original passages. The experiment contains 300 core records, 897 labeled generator outputs, and 2,683 judge verdicts in a crossed 3 x 3 matrix; the primary analysis uses 275 fully validated records. Instead of comparing diagonal and off-diagonal cells across different answers, we estimate same-model effects by pairing judges on the exact same candidate answer. This changes the interpretation: diagonal and off diagonal F1 are similar, and the paired same-model recall effect is near zero (-0.5 pp; 95% cluster bootstrap CI [-2.7, +1.7]). The only robust paired gap is lower matching-judge flagging for answers that avoided the induced claim (-4.3 pp). A targeted human evaluation finds that reviewed apparent false positives are alternate source-error detections, mistakes in labeling whether the induced claim was adopted, or unclear cases; none were adjudicated as genuine false alarms. The lesson is methodological: RAG judge studies should report full matrices, answer-paired effects, behavior strata, and label-task alignment.

---


### 85. [Spectral Heat Flow for Conservative Token Condensation in Vision-Language Models](https://arxiv.org/abs/2607.10640)

**<font color=#1a73e8>作者：</font>** Zhaoyang Li, Yanjun Li, Wangkai Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are costly at inference time because they must process long sequences of visual tokens. Existing token pruning methods often degrade under high compression by blindly discarding information, breaking spatial structure or collapsing diversity. We propose SpecFlow, a training-free framework that shifts the paradigm from destructive pruning to conservative condensation, strictly enforcing spatial coverage and statistical conservation to ensure stability. Treating visual tokens as nodes in a $k$NN graph, SpecFlow (i) computes a stable importance field via spectral heat flow to preserve structural coherence, (ii) allocates budgets via adaptive spatial partitioning to guarantee coverage, and (iii) aggregates discarded information into coreset sinks to maintain statistical conservation. The method is plug-and-play, requires no fine-tuning, and is compatible with FlashAttention. Experiments confirm that our SpecFlow outperforms SOTA methods across tasks, VLM architectures, and pruning ratios. Notably, LLaVA-1.5 with SpecFlow retains 95.6\% of original performance despite pruning 88.9\% of visual tokens, offering an exceptional efficiency-accuracy balance. Code is available at this https URL

---


### 86. [MafiaScope: Non-Invasive, Time-Resolved Belief Probing for LLM Agents in Social Deduction Games](https://arxiv.org/abs/2607.10645)

**<font color=#1a73e8>作者：</font>** Ilia Karpov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An LLM agent's public behaviour reveals little about its social reasoning: an agent that votes correctly may be guessing, and an agent that lies well leaves no trace of what it actually believes. We present MafiaScope, an open testbed that turns the social deduction game Mafia into a measurement instrument for machine Theory of Mind. After every public utterance, every agent privately answers a configurable set of structured probe questions; the answers never re-enter the game and are scored automatically against the ground truth the engine knows. An interactive visualizer renders the belief trajectories: impersonate mode shows the game as one agent sees it, panels chart timeline-aligned accuracy and calibration, and counterfactual replay forks any recorded step. In a 32-game DeepSeek case study with 13{,}815 parsed probe answers, stated confidence is poorly calibrated, with expected calibration error 0.17, agents over-predict being suspected 1.5 times, and a 30-fork replay experiment walks the counterfactual replay workflow end to end. Engine, viewer and a corpus of 200+ cross-model games are released under an open licence; live demo: this https URL screencast: this https URL.

---


### 87. [Knowledge Distillation for Automated AI Tutor Evaluation](https://arxiv.org/abs/2607.10647)

**<font color=#1a73e8>作者：</font>** Tahmid Al Hannan, Diego Garcia, Alex Njoroge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid integration of Large Language Models (LLMs) into K-12 and higher education has outpaced the development of reliable methods for evaluating their pedagogical quality. As the research community starts to explore the space of automating evaluation of AI tutors, we introduce FATE (FLC AI Tutor Evaluator), a specialized 8B-parameter language model designed to evaluate AI tutors. Aligned with the four core evaluation tracks from the BEA 2025 Shared Task, our model assesses pedagogical ability across Mistake Identification, Mistake Location, Guidance, and Actionability. Because pedagogical evaluation is a specialized task with limited labeled data, we leverage knowledge distillation from a frontier LLM to generate additional supervision, yielding absolute performance gains up to 22.63 percentage points. Finally, we demonstrate FATE's utility as an automated evaluator by benchmarking instructional responses generated by popular commercial models, including ChatGPT, Claude, Gemini, and DeepSeek. On average, we have found that Gemini 2.5 Flash perfomed best (82.88%), then ChatGPT 5.5 Instant (80.75%), followed by DeepSeek V4 Flash (80.13%) and Claude Sonnet 4.6 (74.00%).

---


### 88. [Embark Now: User Demand Oriented Framework for Multi-day Urban Travel Itinerary Planning](https://arxiv.org/abs/2607.10651)

**<font color=#1a73e8>作者：</font>** Rongbo Qi, Yaqi Zhang, Shijun Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In large urban areas, planning multi-day travel itineraries is challenging due to the abundance of Points of Interest (POIs), diverse user preferences, and constraints such as opening hours. Effective solutions must dynamically accommodate diverse traveler requirements while optimizing for satisfaction and feasibility within limited computation time. This paper addresses these challenges through introducing an innovative framework that integrates Large Language Models (LLMs) to dynamically capture user requirements with precision and flexibility, and an enhanced Greedy Randomized Adaptive Search Procedure (GRASP) algorithm as a well-suited preference-aware planner to generate feasible multi-day itineraries. The effectiveness of our integrated approach is demonstrated through extensive experiments on two real-world urban datasets from Beijing and Tianjin. Our framework significantly outperforms state-of-the-art (SOTA) methods, improving the average total itinerary score by at least 4.52% and 11.09% across 5,040 user cases with diverse preferences in the two datasets. Furthermore, through end-to-end algorithmic enhancements, it achieves notable average improvements of 17.95% and 26.07% in the computed metrics, while also delivering substantial gains in time efficiency -- realizing average performance increases of 4.64% and 25.55% within shorter computation times compared to suboptimal methods that require multiple iterations. These outcomes underscore our method's superiority in delivering both enhanced itinerary quality and computational efficiency over existing methodologies.

---


### 89. [Unlocking Parallelism in Autoregressive Language Models via Speculative Decoding with Progressive Tree Drafting](https://arxiv.org/abs/2607.10661)

**<font color=#1a73e8>作者：</font>** Zipeng Gao, Zhi Zheng, Qingrong Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding has significantly accelerated Large Language Model (LLM) inference by alleviating memory-bound bottlenecks. However, traditional speculative decoding typically relies on auxiliary draft modules, incurring significant training and communication overhead. Although recent methods attempt to generate drafts within the target model itself, they often fail to fully exploit its latent parallel capacity due to a lack of structural coordination. In this paper, we propose \textbf{Progressive Tree Drafting (PTD)}, which employs a structured, guided parallel drafting strategy to harness the model's parallel potential. By coupling a progressive tree structure with a stepwise pruning mechanism, PTD actively guides the LLM to explore multiple semantic paths in a single forward pass, ensuring both draft diversity and coherence. Experiments demonstrate that PTD achieves up to $2\times$ decoding speedup across various benchmarks while remaining training-free and model-agnostic. Our code is available at: this https URL.

---


### 90. [Answer-Conditioned Chain-of-Thought Distillation for Few-Shot Industrial Vision with Small VLMs](https://arxiv.org/abs/2607.10666)

**<font color=#1a73e8>作者：</font>** Shubham Rao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying AI-based visual inspection in manufacturing is hard because requirements change often, new defect types appear, and large labeled datasets are rarely available. We propose answer-conditioned chain-of-thought (CoT) distillation for rapidly adapting small vision-language models (VLMs) to new industrial tasks using minimal labeled data. A frontier VLM receives each training image along with its correct label and generates a justified visual explanation. A 3B-parameter model is then fine-tuned on these reasoning-augmented examples via LoRA. By conditioning on correct answers, we ensure all training reasoning is directed toward the correct conclusion, which is critical because frontier models score as low as 24.1% on our hardest task. We validate on four industrial classification tasks spanning three image modalities using only 18 to 30 labeled images per task. Across 4 seeds per task (32 training runs), our method outperforms direct fine-tuning on all 16 seed-task combinations, with mean improvements of +1.7 to +4.4 percentage points. A controlled equal-budget experiment confirms the improvement comes from reasoning quality, not additional training steps. An unconditioned baseline demonstrates that with out answer-conditioning, wrong reasoning degrades performance by 17.8 percentage points. On weld radiograph classification, the fine-tuned 3B model outperforms GPT-4.1 by 10.0pp using just 24 training images.

---


### 91. [Learning to Fine-tune Foundation Models under Resource Limitations](https://arxiv.org/abs/2607.10694)

**<font color=#1a73e8>作者：</font>** Thomas Tsouparopoulos, Iordanis Koutsopoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of optimal continual fine-tuning for a pre-trained Foundation Model deployed at a resource-limited device. At each time slot, a new batch of training data arrives, and the controller is faced with two options: either use the data to fine-tune the model and incur a compute cost, or do not fine-tune the model and discard the data. After the decision, the performance of the current model is measured in terms of an application-specific performance metric such as classification accuracy. Our objective is to learn an optimal policy that determines \emph{when to fine-tune the model} on a single task (e.g., sentiment analysis), under a finite compute budget. We formulate this online decision-making problem as a constrained Markov Decision Process, where the system state captures three essential aspects: (\textit{i}) model's performance, (\textit{ii}) computational budget, and (\textit{iii}) data distribution relevance to historic data encountered up to that point. The transition to the next state is stochastic and therefore, we propose a reinforcement learning-based method to solve this problem, namely the \emph{actor-critic} algorithm. We also consider the special case where the performance of fine-tuning for a given model can be predicted or estimated prior to decision; in this case the problem becomes a Dynamic Programming one. Experiments with a large pre-trained model on a widely-used text classification dataset demonstrate that our method consistently outperforms fine-tuning approaches with the same compute budget by more than $4\%$ in terms of accuracy and achieves $97\%$ of full-parameter fine-tuning accuracy while requiring only $25\%$ of the fine-tuning steps.

---


### 92. [WattCouncil: Context-Aware Household Energy Scenario Generation With Governed LLMs](https://arxiv.org/abs/2607.10720)

**<font color=#1a73e8>作者：</font>** Mohannad Takrouri, Nicolas M. Cuadrado A., Martin Takáč  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The accelerating shift toward low-carbon power systems, together with the widespread adoption of behind-the-meter technologies such as rooftop solar and electric vehicles, is placing new operational and analytical demands on electricity grids. At the same time, smart-grid research increasingly relies on machine learning (ML), yet progress is constrained by limited access to high-resolution household energy data due to privacy concerns, regulatory barriers, and collection costs. This work presents WattCouncil, a data-generation framework in which household electricity demand is generated by a council of Large Language Model (LLM)-based agents operating in specialized roles to generate, audit, and validate structured energy scenarios under explicit cultural, temporal, and physical constraints. Rather than acting as static predictors, these agents serve as adaptive decision-makers within a governed pipeline. Motivated by studies highlighting the importance of contextual factors in energy use, our framework produces context-sensitive daily routines through a guided reasoning process that incorporates household composition, temporal factors, and environmental conditions. We evaluate the generated profiles against the detailed CER dataset, which contains over a year of load measurements for 4232 households together with survey-based socio-economic information. We further assess the consistency of the framework through ablation studies. Source code is available at this https URL

---


### 93. [Traj-VLN: Learning Pixel-Space Interaction via Autoregressive Trajectory Generation](https://arxiv.org/abs/2607.10744)

**<font color=#1a73e8>作者：</font>** Changfei Fu, Guangcheng Chen, Wenjun Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benefiting from the powerful priors embedded in large-scale pre-training data and the emerging commonsense reasoning ability, large language models (LLMs) have shown unprecedented generalization capabilities in many research fields. Recently, projecting visual embeddings into the language space via vision-language models (VLMs) to achieve sim-toreal and cross-scene generalization has become a prevailing paradigm in the field of Vision-and-Language Navigation in Continuous Environments (VLN-CE). VLN requires an embodied agent to navigate through unseen environments following natural linguistic instructions. We emphasize that a VLN task can be decomposed into a sequence of sub-tasks, each corresponding to a process of 3D spatial interaction with the environments described by instructions such as "walk to the end of the sofa and turn left." However, such spatial interactions involving moving into the image along the direction of depth sensing are puzzling for VLMs as they were predominantly trained on conversations with RGB images. Rather than incorporating depth or 3D geometric information-which VLMs rarely encounter during pretrainingwe propose an alternative approach: fine-tuning VLMs to learn navigation interactions directly in 2D pixel space through autoregressive trajectory generation. Given a linguistic instruction and historical observations, our model sequentially predicts a series of pixel coordinates, drawing a trajectory from the bottom center of the current observation. While prior work has proved that pixel-goal supervision outperforms learning of discrete actions, our experiments further verify that the supervision of pixel-space trajectory significantly enhances VLN performance. Moreover, we demonstrate that our flagship model achieves state-of-the-art level performance with relatively limited computational resources and training data.

---


### 94. [The First ChineseBabyLM Challenge: training data-efficient and cognitively plausible language models for Chinese](https://arxiv.org/abs/2607.10745)

**<font color=#1a73e8>作者：</font>** Siyuan Song, Zhiheng Qian, Yunhao Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the first ChineseBabyLM challenge, which will be held in the 2026 NLPCC conference. The challenge calls for researchers to train language models from scratch with 100 million Chinese tokens and evaluates the models on 3 tracks of tasks: NLU, cognitive alignment and Hanzi knowledge. There is no restriction on tokenizer, model architecture and the number of training epochs. Details of the challenge can be found in this https URL.

---


### 95. [Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF](https://arxiv.org/abs/2607.10750)

**<font color=#1a73e8>作者：</font>** Chinmayi Dixit  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synthetic data is widely used to train large language models because it is inexpensive to generate and easy to control. As models are increasingly deployed as agents, synthetic trajectories are likely to become an important source of training data for agentic behavior. We investigate the effects of training on synthetic agentic trajectories containing adversarial interactions, including actions such as terminating another agents process, lowering its scheduling priority, or accessing resources without authorization. We finetune Llama 3.3 70B Instruct on these trajectories, generated to approximate reinforcement learning rollouts, and evaluate the resulting models on Anthropics Agentic Misalignment suite and Apollos in context scheming scenarios. Finetuning on these trajectories consistently increases misaligned behavior. Leaking rises by roughly a factor of five over the baseline, 4.6% to 24.9%. This increase survives the removal of every adversarial action from the trajectories. Finetuning on structurally comparable trajectories generated benign from the start produce a substantially smaller effect, 15.5%. These results indicate that the misaligned disposition is introduced during the generation process and encoded diffusely throughout the trajectory, rather than being localized to the harmful actions themselves. The effect also depends on the generating model. Benign trajectories produced by Gemini 2.5 Flash induce slightly higher leaking rates than trajectories generated from identical tasks by Claude 3.7 Sonnet. In contrast, broad safety benchmarks degrade similarly across all finetuned models and therefore fail to distinguish these effects. Our results suggest that action level filtering is insufficient to ensure the safety of synthetic agentic training data and that dispositions introduced by the generating model can survive semantic inspection.

---


### 96. [TOLiD: Bridging the Architecture Gap in Vision Foundation Model to LiDAR Pretraining via Token Lifting for Distillation](https://arxiv.org/abs/2607.10762)

**<font color=#1a73e8>作者：</font>** Sutharsan Mahendran, Darshana Priyasad, Kaushik Roy 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal distillation from Vision Foundation Models (VFMs) to LiDAR backbones has recently emerged as a self-supervised pretraining strategy that reduces reliance on dense point-wise annotation for 3D scene understanding. However, existing distillation pipelines typically treat the VFM as a frozen feature source and train a heterogeneous 3D backbone to match fixed image embeddings, forcing the student to bridge both the modality gap and the cross-architecture gap between dense ViT token representations and sparse 3D encoders. We propose TOLiD, a self-supervised pretraining method for LiDAR representation learning that addresses this gap by coupling a LiDAR backbone with a student Vision Transformer (ViT) initialized from a frozen VFM teacher and applying supervision over compatible patch-token representations. TOLiD converts the set of point features within each image patch frustum into a token using Frustum Pooling followed by Frustum Attention, and performs token-level distillation with visibility masking. For LiDAR-only deployment, we lift token features back to per-point representations using masked bilinear sampling to avoid patches that have limited LiDAR points. We extensively evaluate TOLiD on five heterogeneous LiDAR datasets and four cross-sensor adaptation pairs, demonstrating improved transfer with frozen backbones and lightweight heads.

---


### 97. [Is Energy Guidance All You Need? Training-Free Norm Injection for Driving World Models](https://arxiv.org/abs/2607.10781)

**<font color=#1a73e8>作者：</font>** Xiyan Su, Frank Diermeyer, Markus Lienkamp  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving world models built on large video-diffusion backbones generate realistic scenes but are hard to control: enforcing a traffic norm typically means retraining the backbone or conditioning it on hand-built layouts. We ask whether controllability requires training at all. Our experiment shows that a rectified-flow driving world model, which jointly generates future video and a planned ego trajectory, can have its planned trajectory steered entirely at sampling time by differentiable energy functions that encode driving norms, without knowledge-specific retraining of the diffusion backbone. Concretely, we demonstrate that a world model built on Open-Sora 2.0 MM-DiT backbone can be steered to brake at a counterfactual target by injecting energy guidance at sampling time. However, we find that the generated video does not yet follow the steered trajectory through the backbone's joint self-attention and identify the cross-stream coupling as a crucial requirement for end-to-end-controllable rollouts.

---


### 98. [Imaging-101: Benchmarking LLM Coding Agents on Scientific Computational Imaging](https://arxiv.org/abs/2607.10789)

**<font color=#1a73e8>作者：</font>** Siyi Chen, Jiahe Ying, Yixuan Jia 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computational imaging, which recovers hidden signals from indirect, noisy measurements, underpins quantitative discovery across scientific disciplines, yet building a correct reconstruction pipeline demands deep domain expertise and remains laborious even for domain scientists. We introduce Imaging-101, a benchmark of 57 expert-verified computational imaging tasks spanning six scientific domains, each grounded in a peer-reviewed paper and canonicalized into a standardized four-stage pipeline (preprocessing, forward physics modeling, inverse solver, and visualization) Three evaluation tracks (planning, function-level unit tests, and end-to-end reconstruction) probe distinct agent capabilities across the full pipeline. Evaluating seven frontier LLMs uncovers systematic challenges in applying coding agents to computational imaging that go beyond those exposed by general coding benchmarks, spanning algorithm selection, physical convention handling, and pipeline integration. These findings highlight concrete capability gaps and point toward skill-augmented, domain-specialized agents as a practical path to reliable computational imaging assistance.

---


### 99. [Mixture of Cognitive Experts in Large Vision-Language Models](https://arxiv.org/abs/2607.10796)

**<font color=#1a73e8>作者：</font>** Robert Wijaya, Ngai-Man Cheung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision Language Models (LVLMs) require strong reasoning over both visual and textual input. Recent work suggests that cognitive elements, especially diverse representations and metacognition, correlate with better performance. Many of the needed perceptual functions are already provided by specialized domain-specific computer vision models, which act as the perceptual subsystem for detecting objects, localizing them, inferring states, recovering spatial layout, and reading text. The key challenge is to integrate these multi-encoder experts into a trustworthy, interpretable, and coherent representation that improves verifiability and reduces hallucinations. This is difficult because vision-language questions span different cognitive levels, yet most LVLM pipelines apply the same perception-reasoning routing regardless of the demand of each query. We propose an evidence-driven multimodal reasoning framework that utilizes a Bloom-inspired taxonomy as a hierarchical reasoning protocol. The two-stage cognitive verbalization first produces a Literal Evidence Summary by decomposing expert outputs into short, atomic evidence statements. It then performs Bloom Verbalization to turn these evidence items into a staged reasoning trace, and a lightweight Reasoning Trace Module quantitatively analyzes the trace to make evidence usage and reasoning progression explicit. Through this integration, we observed several improvements in perception and reasoning abilities. Moreover, the trace module provides quantitative evidence that different queries induce different cognitive entry levels and evidence-use trajectories that enable fine-grained analysis.

---


### 100. [Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos](https://arxiv.org/abs/2607.10797)

**<font color=#1a73e8>作者：</font>** Hao Zheng, Jinyi Huang, Tiantian Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assembly action understanding is a key enabler for effective human-robot collaborative assembly, yet it remains challenging due to subtle motions and fine-grained hand-object interactions. We adapt vision-language models (VLMs) to this challenging domain with Compositional Context Fine-Tuning (CCFT), a method that decomposes assembly actions into semantic elements (Verb, Object, Tool) and fine-tunes VLMs to recognize each action element using templated question-answering pairs. This approach ensures near-deterministic outputs. To enable efficient and effective multi-task learning under limited data, a Layer-Partitioned Alternating Training (LP-AT) method is presented, which assigns distinct model layers to recognize specific action elements through element-specific low-rank adapters. LP-AT alternates weight updates across element-specific adapters, reducing cross-task interference while enabling per-adapter hyperparameter optimization. Furthermore, we create HA-ViD-VQA and IKEA-ASM-VQA datasets from existing assembly video datasets. Extensive experiments on these datasets demonstrate that our method consistently outperforms strong action recognition baselines while providing interpretable element-level predictions that can support diverse downstream applications.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-199](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
