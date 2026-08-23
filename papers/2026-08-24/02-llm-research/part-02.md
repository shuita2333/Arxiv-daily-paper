# 🧠 大模型相关研究 | 2026年08月24日

> 本类共 **121** 篇论文：已确认 **114** 篇，待复核 **7** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-121](./part-03.md)

---

### 51. [Question-Guided Evidence Acquisition for Multimodal Visual Question Answering](https://arxiv.org/abs/2608.19739)

**<font color=#1a73e8>作者：</font>** Alin-Ionut Popa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal LLMs can see a document, but they often can't read it reliably. Small text, tables, visual cues, and topological elements still trip them up under direct visual inference, even when the page is already sitting in the model's context. Most document-VQA systems treat perception as fixed: they encode the page once, ask the question, and answer from whatever the model happened to extract in that single fast pass. We think document VQA needs slower, more deliberate perception: rather than answering from one fixed encoding, the model should spend a bit of extra compute at inference time working out what to look at next, and only then answer. We build this into \textbf{Q-Guide}, a small agent that reads a question, works out what evidence it is still missing, and calls targeted tool(s) to recover it---reading text where text is needed, zooming in where detail is needed, or grounding a region where position matters. On DocVQA2026 and Manga109, Q-Guide outperforms both direct prompting and recent multi-agent document systems ($65.0\%$ vs.\ $40.0\%$ on DocVQA2026, $32.4\%$ vs.\ $24.4\%$ on Manga109), and the improvement holds across three Claude backbones (Opus 4.6, Sonnet 4.6, and Opus 4.5). We find that accuracy scales with the perception budget---most of the gain appears within two to three deliberate rounds---and that the gain comes from directing perception to the right place, not from complex control logic: adding planners, routers, or multiple collaborating agents does not help.

---


### 52. [PersonalBench: Measuring the Authorship Gap in LLM Personalization](https://arxiv.org/abs/2608.19746)

**<font color=#1a73e8>作者：</font>** Yash Ganpat Sawant  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized text generation aims to make LLMs write in a specific individual's style, yet existing benchmarks measure task accuracy or preference alignment rather than whether the model's output actually resembles the target author's writing. We introduce PersonalBench, a benchmark that evaluates inference-time personalization methods through three independent lenses: LUAR (a trained authorship verification model), an LLM-as-judge, and automated stylometrics. Across 50 authors, 1,000 generations, and two model families (Qwen 3, GLM-4), we find that personalization methods do produce author-differentiated output (LUAR discriminates target authors within generated text at AUC=0.918) but this differentiation never crosses the human-LLM boundary. All methods achieve LUAR similarity to real authors in the range 0.484-0.508, below the cross-author human floor of 0.626 (ceiling 0.756). The LLM's own authorship fingerprint dominates: generated text is more distant from any human author than random humans are from each other. Methods are statistically indistinguishable from each other on LUAR (spread 0.024) despite appearing differentiated on the LLM judge, a discrepancy we trace to circularity between trait extraction and profile extraction. We validate that LUAR reliably measures authorship in our corpus (AUC=0.76 single-post, 0.96 multi-post). We release PersonalBench as a calibrated measuring stick: inference-time personalization modulates the LLM's style but does not bridge the gap to human authorship.

---


### 53. [FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving](https://arxiv.org/abs/2608.19758)

**<font color=#1a73e8>作者：</font>** Qihang Fan, Huaibo Huang, Zhiying Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context modeling is a pivotal capability for Large Language Models, yet the quadratic complexity of attention remains a critical bottleneck, particularly during the compute-intensive prefilling phase. Our previous work, FlashPrefill, mitigates this cost through instantaneous pattern discovery and max-based dynamic thresholding; however, it remains an algorithmic prototype that is still distant from production deployment. In this paper, we present FlashPrefill V2, which evolves FlashPrefill from a prototype toward practical long-context serving along three dimensions. First, we introduce a mean correction term that effectively suppresses the approximation error, keeping performance degradation manageable even at extreme sparsity levels. Second, we redesign the sparse attention operator with PackGQA memory access, warp specialization, and pingpong pipelining, fully aligning with the latest FlashAttention-3/4 implementations and supporting FP8 inference to meet practical quantization requirements. Third, FlashPrefill V2 natively supports paged KV cache and continuous batching, allowing integration as an attention backend in modern inference frameworks such as SGLang. Extensive evaluations on NVIDIA H20 GPUs---among the most widely deployed inference accelerators---demonstrate that FlashPrefill V2 delivers up to 47.26x and 27.19x speedups over FlashAttention-2 at 128K context length under FP8 and BF16 precision, respectively, and, in FP8, still achieves a 30.49x speedup against an FA3/4-aligned dense baseline.

---


### 54. [Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against Executed Replay](https://arxiv.org/abs/2608.19760)

**<font color=#1a73e8>作者：</font>** Haiyue Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Audited against causal ground truth from executed replay in a single-agent tool environment (ALFWorld), none of the step-level credit signals used to train LLM agents -- LLM-judge scores, outcome-conditioned logprob ratios, or the policy's own confidence -- identifies which steps causally matter better than chance. Existing evaluations grade these signals against annotated step *correctness*; we audit them against step *contribution* -- what re-sampling the policy's own alternatives at each decision point and rolling forward actually changes about the outcome -- and the two come apart. The ground truth itself is structured: causal contribution is sparse (30.5% of decision points where ground truth is defined carry measurable effect), and measurability is model-dependent -- the fraction of points with no policy-supported counterfactual differs by a factor of two (13.1% vs. 26.8%) between two similar-scale policies. The failure mode is identifiable: implicit credit echoes the policy's fluency (median rank correlation +0.75, replicating at +0.70 in a second family under a corrected instrument), while conditioning on the outcome adds no causal information (partial correlation -0.004, Qwen). A confidence-only router recovers pivotal steps at chance level, but cuts judge cost by 13.1% per turn (14.0% per trajectory). In a seven-arm pre-registered training experiment, no arm reliably outperforms the untrained policy, and the checkpoints' apparent instrument signature is fully explained by training dose -- sparser credit retains fewer examples, an order-of-magnitude spread in optimizer steps -- not credit content. Comparisons of credit rules must therefore match effective sample size, or they measure dose, not credit.

---


### 55. [Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation](https://arxiv.org/abs/2608.19778)

**<font color=#1a73e8>作者：</font>** Tatsuya Amano, Hirozumi Yamaguchi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Pedestrian simulators need a behaviour rule for every agent, but privacy usually limits the data for setting one to aggregate statistics, namely zone-level device counts and origin-to-destination (OD) flows, with no individual trajectories. Such aggregates under-determine individual behaviour, because many different sets of decisions reproduce the same counts. We fine-tune a language model crowd agent so that the simulated population matches the observed destination composition, the fraction of the departing crowd heading to each point of interest. We read this target from the OD flow and reweight the model's own destination distribution onto it by iterative proportional fitting. Because fine-tuning inflates the dominant destination class, we fit the low-rank adapter to trajectories resampled to a corrected training composition that reaches the target after this inflation. On mobile network counts from two baseball games the fine-tuned agent runs without inference-time correction, cutting the destination-share error by 25%, while the grid correlation remains similar across policies.

---


### 56. [LLMs as Acquisition Policies for Finite-Pool Materials Optimization: A Controlled Study](https://arxiv.org/abs/2608.19790)

**<font color=#1a73e8>作者：</font>** Dino-Rober Demir, Florian Le Bronnec, Rio Yokota  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discovering materials with desirable properties often requires searching large candidate spaces while experimental or computational evaluations remain costly. Active learning addresses this challenge by using previous observations to select which candidate to evaluate next, typically through probabilistic surrogate models. We investigate whether open-weight large language models (LLMs) can serve as standalone acquisition policies in this setting. We evaluate five LLMs across four retrospective finite-pool materials optimization tasks under different candidate-presentation strategies and compare them with random selection and conventional Gaussian-process methods. LLM policies generally reach the global optimum in fewer iterations than random selection, indicating that they provide a useful acquisition signal without task-specific training. Their performance relative to Gaussian-process methods is mixed: conventional acquisition performs better on most tasks, while LLMs match or outperform it in some settings. Performance varies substantially across tasks, models, initializations, and candidate presentations, with no LLM approach performing best across all tasks. Overall, open-weight LLMs show potential as acquisition policies for finite-pool materials search, although their reliability remains sensitive to the task and to how candidates and scientific context are presented.

---


### 57. [Towards general embodied intelligence: integrating large language models, knowledge bases, and reasoning capabilities to build the next generation of AI agents](https://arxiv.org/abs/2608.19794)

**<font color=#1a73e8>作者：</font>** Fujiang Yuan, Xia Huang, Lusheng Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The convergence of large language models (LLMs), structured knowledge bases (KBs), and reasoning ability (RA) presents a promising trajectory toward general embodied intelligence (GEI). This paper reviews the evolution of LLM-centered intelligent systems, emphasising their integration with knowledge representation, logical reasoning, and physical embodiment. We analyse LLM architectures, pre-training methods, and inference mechanisms, along with their interaction with external knowledge sources and structured reasoning frameworks. Furthermore, we examine embodied intelligence (EI) paradigms wherein agents learn and act in physical environments. To synthesise these dimensions, we present a conceptual framework that illustrates the synergy among LLMs, KBs, RA, and embodiment, serving as a guiding model for perception, reasoning, and action rather than an implemented engineering architecture. To advance toward GEI, we identify five key challenges: efficient LLM deployment, closed-loop knowledge integration, hybrid symbolic-neural reasoning, perception-action grounding, and continual learning. This survey provides a comprehensive roadmap for developing adaptive, multimodal agents capable of operating in complex, dynamic settings.

---


### 58. [SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?](https://arxiv.org/abs/2608.19799)

**<font color=#1a73e8>作者：</font>** Zhipeng Xu, Jiahao Lu, Yining Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Software increasingly functions as part of the scientific instrument itself, making failures in scientific code capable of compromising not only program behavior but also the evidence underlying scientific conclusions. Yet existing evaluations of coding agents largely emphasize aggregate task success, providing limited insight into why agents fail when repairing scientific software. We introduce \textbf{SWE-bench Science}, a repository-level benchmark for scientific software engineering comprising 119 tasks from 98 GitHub repositories across 20 scientific domains. Each task is organized into one of three paradigms: Issue-driven, Expert-exploratory, and Engineering-integration. Even the best-performing agent, \textbf{Claude Code with Opus-5 (max), achieves a pass@1 below 50\%}, highlighting the substantial challenges posed by scientific software engineering. We identify four recurring failure mechanisms: deficits in scientific knowledge or abstraction, misguided exploration or surface-level repair, incomplete repair coverage or system integration, and failures to generalize scientific knowledge beyond observed cases in our analysis. We further conduct a paired ablation that removes explicit scientific guidance while preserving the repository and executable engineering context. The results show that scientific knowledge is not uniformly beneficial: well-grounded information can constrain repair and improve average performance and token efficiency, whereas poorly aligned guidance can induce anchoring and does not necessarily improve exact repair success. Together, SWE-bench Science provides a broad testbed for studying both the capabilities and failure mechanisms of coding agents in scientific software engineering.

---


### 59. [Stopping and Routing LLM Judge Panels](https://arxiv.org/abs/2608.19802)

**<font color=#1a73e8>作者：</font>** Bin Zhu, Yi Xie, Yanghui Rao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM evaluation pipelines often have many candidate judges: general LLM-as-a-judge prompts, reward models, safety classifiers, confidence variants, and task-specific verifiers. The deployment question is not only which judge is best, but which judges should be called, on which examples, and when panel construction should stop. We formulate judge-panel design as a role-conditioned allocation problem. From a small labeled audit set, declared slices, and judge costs, the method estimates target-relative roles: copies add no conditional information, complements improve the global panel, and specialists help only on slices. These roles induce a policy: drop copies, add complements globally, route specialists conditionally, and stop when validation gain falls below a threshold. Across reasoning, code, safety, preference, reward-model, summarization, and math audits, the method is compared with single judges, flat panels, matched diversity heuristics, full-call stacking, reliability juries, and frugal cascades. The result is a regime map for judge calls: route specialists on deployable slices, stop in saturated verifier regimes, keep broad ensembles when their risk benefit is worth the cost, and ignore conditional copies. The output is a reusable, auditable call plan for the next evaluation batch.

---


### 60. [MileGPO: Milestone Inference with Local Evidence for Graph-Based Policy Optimization of Long-Horizon LLM Agents](https://arxiv.org/abs/2608.19803)

**<font color=#1a73e8>作者：</font>** Bo Qian, Yuting Wu, Shuang Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit assignment is challenging in long-horizon agentic reinforcement learning, where supervision often comes only from final rewards. Existing methods refine trajectory-level signals into step-level credits through step grouping or graph-based advantage estimation, but can overlook meaningful intermediate milestones. We propose MileGPO (Milestone Inference with Local Evidence for Graph-Based Policy Optimization), which derives process-level credit from grouped on-policy rollouts through three designs. Milestone Discovery identifies candidate milestones on successful rollouts and recurring traps on failed ones. Reliability-Calibrated Shaping (RCS) weights these candidates by outcome-based confidence, strengthening reliable milestones and traps while down-weighting uncertain ones. Progress-Contrastive Calibration (PCC) further tests whether a candidate reflects local progress and whether its incoming ansition outperforms observed alternatives from the same this http URL requires neither auxiliary models nor additional environment interaction. Experiments on ALFWorld and WebShop show state-of-the-art performance and a small in-distribution to out-of-distribution gap on ALFWorld. Ablations and credit diagnostics indicate that reliability weighting, local progress, and same-state branch evidence complement milestone discovery and resolve ambiguous intermediate credit.

---


### 61. [Answer-Level Trust Selection for Physical Vision-Language Reasoning](https://arxiv.org/abs/2608.19807)

**<font color=#1a73e8>作者：</font>** Rongyu Yu, Ke Niu, Fengxiang He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can estimate physical quantities such as duration, speed, and acceleration from visual observations, but existing benchmarks primarily assess overall model performance against annotated ground truth. In deployment, a key question is whether an individual prediction can be trusted when its ground truth is unavailable. Self-consistency alone may fail to capture important failure modes: a VLM may produce stable-but-wrong estimates or rely on textual priors rather than visual evidence. We formulate answer-level selective prediction for quantitative physical reasoning and propose Answer-Level Trust Selection (ATS), a post-hoc, model-agnostic framework for accepting or rejecting individual VLM predictions. ATS requires no fine-tuning, auxiliary verifier, or access to the model's internal logits. Instead, it aggregates eight interpretable behavioral diagnostic scores derived from repeated queries and controlled interventions into a unified trust score. We evaluate ATS in depth on Qwen2.5-VL-7B and across 20 VLM backbones, examining selective performance, diagnostic behavior, and targeted failure modes. Our results show that intervention-based diagnostics help identify stable-but-wrong and prior-tracking predictions that repeated agreement alone may miss. However, improved failure-case rejection can come at the cost of lower retention of correct predictions. ATS therefore complements model-level capability evaluation with answer-level reliability assessment for quantitative VLM predictions. Code will be released upon publication.

---


### 62. [When Saying No Makes Better Videos: Designing Dual Gatekeeping for Pedagogically Grounded AI Content Creation](https://arxiv.org/abs/2608.19812)

**<font color=#1a73e8>作者：</font>** Yearim Kim, Njun Baek, Nojun Kwak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To prevent the adoption of aesthetically polished but pedagogically flawed AI content, we study a video authoring pipeline featuring two layers of structured refusal. The first layer empowers educators to iteratively reshape AI scripts based on multimedia learning theory, while the second employs automated metrics to flag violations in instructional coherence and narrative-visual synchronization. While neither layer is exhaustive, their synergy ensures that principled resistance--the act of deferring AI output until it meets rigorous standards--becomes a catalyst for higher quality. Evaluation combining a study with 23 educators across 3 topics and automated metrics across 7 topics drawn from established science and philosophy curricula shows that both layers independently improve the same instructional dimensions, suggesting that thoughtful resistance and generative AI are not opposites but partners.

---


### 63. [Towards Clinically Faithful Medical Image Captioning via Enhanced Vision-Language Alignment](https://arxiv.org/abs/2608.19825)

**<font color=#1a73e8>作者：</font>** Yunseo Lee, Hyun Jun Kim, Heeseung Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image captioning is a technique that accelerates early-stage diagnostic workflows and enhances the interpretability of medical diagnostic AI systems. However, unlike general image captioning, clinically reliable captioning remains challenging due to grayscale-based modalities, subtle anatomical cues, specialized medical phrasing, and variations in data quality. Despite recent advances in large vision-language models, fluent outputs do not necessarily guarantee sufficient alignment with clinical concept spaces or evaluation criteria. To address this issue, we propose a framework that strengthens clinical alignment by separating and enhancing training-time alignment and inference-time alignment. We build a medical image captioning pipeline that integrates single/dual vision encoders based on BioMedCLIP and SigLIP2, a Q-Former, and a LLaMA-based decoder, and examine the contribution of auxiliary learning for UMLS concept/type prediction. At inference, we apply single-embedding-based reranking to select the best caption among candidates, while at training we introduce MedPAIR-SCST, which combines clinically relevant rewards to shift the generative distribution toward improved clinical alignment. Our experiments show that complementary visual representations with a multi-encoder design and concept-level auxiliary learning help preserve clinically meaningful information. Furthermore, inference-time reranking provides a practical way to improve semantic and clinical alignment without additional training, whereas MedPAIR-SCST goes beyond selection by directly improving the model's distribution to generate more consistent and clinically grounded captions. These findings suggest that jointly leveraging selection-based alignment and reinforcement-learning-based alignment can promote more trustworthy medical image captioning even in data-constrained settings.

---


### 64. [SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.19842)

**<font color=#1a73e8>作者：</font>** Dayang Liang, Lang Feng, Bo An 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) has become a critical stage in the post-training of large language models. Existing critic-free, group-relative methods estimate policy advantages from multiple rollouts, avoiding the substantial memory overhead of conventional proximal policy optimization (PPO) and achieving strong performance on long-horizon interactive tasks. Despite their success, recent studies revealed three limitations: (1) Lack explicit value generalization and effective temporal credit assignment; (2) Suffer from potential advantage collapse in long-horizon complex tasks; (3) Require a costly trade-off between sampling budget and policy performance. In this work, we propose Single-rollout Autoregressive Policy Optimization (SAPO), a low-memory and compute-efficient framework in which the policy and value functions share a single autoregressive backbone. SAPO exploits the autoregressive structure of LLMs to produce policy and value predictions at distinct causal boundaries with shared parameters, while independently optimizing the PPO objectives and auxiliary on-policy SARSA objectives. To robustly estimate the contribution of each turn, we further introduce a trajectory-level generalized advantage estimator that combines lambda-returns with batch normalization. Experiments across ALFWorld and WebShop with Qwen2.5-1.5B/7B show that SAPO trains stably and outperforms PPO and GRPO by mean +15.1 and +12.1 percentage points, respectively, while eliminating the memory cost of a separate critic model and reducing per-iteration runtime by 33.2% over PPO.

---


### 65. [Inadvertent Context Leakage in Language Models](https://arxiv.org/abs/2608.19857)

**<font color=#1a73e8>作者：</font>** Jaiden Fairoze, Neal Mangaokar, Kamalika Chaudhuri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For AI agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert carrier to transmit secrets through seemingly innocuous text. In both cases, this limited leakage is exploited using a novel adaptive attack that assumes black-box access to the underlying model.
In controlled experiments across eight proprietary models, we find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82\% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. We observe that more capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, suggesting leakage is a byproduct of capability as opposed to a patchable bug. We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent.

---


### 66. [PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents](https://arxiv.org/abs/2608.19861)

**<font color=#1a73e8>作者：</font>** Seongjae Kang, Taehyung Yu, Sung Ju Hwang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Customer-service LLM agents must follow organizational policy when acting on a user's behalf. Compliance failures arise from either forbidden actions, such as granting an ineligible change, or omitted procedural requirements, such as identification or confirmation. Runtime safeguards can intervene on risky actions, but action-local checks do not guide an agent through a multi-step procedure. Workflow-following systems support prescribed process execution, but primarily target workflow completion rather than safeguarding agent behavior. PolicyGuide instead compiles each domain policy into a workflow graph and invokes a proactive verifier at user-turn boundaries. From persisted graph state, the verifier reconciles open requests and returns step-specific remediation along a policy-compliant path. Across the $\tau^2$-bench airline, retail, and telecom domains with a GPT-5.4 agent and verifier, PolicyGuide raises mean $\mathrm{Pass}^4$ from $0.42$ to $0.62$, with the largest gain on telecom ($0.19$ to $0.61$), the most workflow-structured domain. The same workflows transfer to Claude Sonnet 4.6 and Gemini 2.5 Pro agents. Complementary evaluations find the lowest observed attack-success rate under adversarial users and the strongest procedural compliance in an author-designed workflow-level validation.

---


### 67. [DIFFCZSL: Compositional Zero-Shot Learning Regularized by Diffusion Representations](https://arxiv.org/abs/2608.19871)

**<font color=#1a73e8>作者：</font>** Hangyu Tian, Zhenqi He, Yanghao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional Zero-Shot Learning (CZSL) aims to recognize unseen attribute-object compositions by leveraging knowledge of primitive concepts learned from seen compositions. Although recent works achieve impressive performance in CZSL by leveraging large vision-language models, they primarily rely on discriminative representations that may not explicitly preserve the structured relationships between primitive concepts and their compositions. Motivated by the recent success of diffusion-based classifiers and their competitive performance relative to discriminative models, we investigate whether intermediate diffusion representations can provide complementary cues for CZSL. To this end, we propose DIFFCZSL, a diffusion-augmented framework that injects generative priors from pre-trained diffusion models into CLIP-based CZSL pipelines. We extract intermediate diffusion representations and project them into the CLIP embedding space to provide auxiliary supervision on both image and text modalities. Through contrastive alignment between CLIP embeddings and diffusion features during training, our method encourages the embedding geometry toward richer composition-aware semantics, while introducing no additional cost at inference time. Extensive experiments on three public CZSL benchmarks demonstrate consistent improvements over strong CLIP-based baselines under both closed-world and open-world settings. Our results highlight the complementary strengths of generative diffusion representations and discriminative vision-language models for compositional generalization.

---


### 68. [A knowledge-guided agentic framework for mitigating patient-context ambiguity in health queries](https://arxiv.org/abs/2608.19875)

**<font color=#1a73e8>作者：</font>** Mahyar Abbasian, Saba A. Farahani, Arshia Ilaty 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patients often submit short, underspecified queries to healthcare chatbots that lack the patient-specific information needed to determine an appropriate response. Although these queries may be linguistically clear, they can support multiple plausible answers depending on undisclosed factors such as symptoms, diagnoses, medications, allergies, or dietary restrictions. A language model answering such a query directly may therefore rely on unsupported assumptions about the patient. We introduce a knowledge-guided agentic framework for mitigating patient-context ambiguity before final response generation. The framework operates between the patient and an otherwise unchanged downstream language model. It interprets the initial query, uses a task-specific knowledge graph to construct a set of plausible hypotheses, identifies the missing patient-context variables needed to distinguish among them, and asks targeted follow-up questions. The original query and the acquired context are then combined into a clarified prompt for the downstream model. We evaluated the framework across five language models using two controlled ambiguity-mitigation benchmarks: diagnosis retrieval from 1,034 symptom queries with clinically relevant evidence systematically masked, and dietary-safety classification from 487 queries with decisive health context omitted. The framework was compared with direct answering of the underspecified query and with rephrasing the same query without acquiring new patient information. In diagnosis retrieval, it increased overall exact Top-1 accuracy by at least 57.1 percentage points and selective exact Recall@5 by at least 77.7 percentage points across the five evaluated models compared with direct prompting. In dietary-safety classification, it improved accuracy across all five models and achieved the highest Matthews correlation coefficient for four...

---


### 69. [EnvHarness: Awakening Static Worlds for Agent Learning](https://arxiv.org/abs/2608.19880)

**<font color=#1a73e8>作者：</font>** Chengsong Huang, Zifeng Wang, Rujun Han 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents learn by interacting with environments, yet these environments are hand-built and static: blind to an agent's weaknesses, and quickly left behind as it improves. While recent environment generation methods attempt to address this, they require domain-specific pipelines, rely on expensive or unreliable verifiers, and still produce static environments. To alleviate the engineering burden of rebuilding environments from scratch, we propose Environment Harness (EnvHarness), a programmable layer of plug-in components that wraps a static environment to reshape its behavior without modifying the underlying logic. Operating through standard interfaces, EnvHarness applies across diverse domains while ensuring every reshaped environment retains its original verifier. To automate this process, we introduce EnvRigger, which treats the target policy as a black box, observing its execution trajectories to synthesize EnvHarness components targeting diagnosed flaws, and validating them via fresh rollouts. Across five benchmarks in four domains, EnvHarness outperforms both original environments and domain-specific environment generation pipelines, achieving up to a 9.0-point improvement on held-out instances with 9.8% fewer execution steps. Furthermore, EnvHarness provides a superior optimization signal for reinforcement learning, enabling continuous, targeted co-evolution of the policy and its environment.

---


### 70. [Write Once, Run Everywhere: The Axon DSL for Shape-Safe and Framework-Agnostic LLM Architectures](https://arxiv.org/abs/2608.19889)

**<font color=#1a73e8>作者：</font>** Jacob Nielsen, Danial Namazifard, Lukas Galke Poech 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The entire ecosystem of open-source language models effectively relies on a single platform. What if this platform was forced to shut down tomorrow? Implementing and maintaining efficient model definitions and translating them between different training and inference regimes is a resource-heavy task that severely limits model efficiency and portability, hindering both scaling and deployment. Here, we present Axon, a strongly typed domain-specific language with Haskell-like syntax, that enables a write-once, run everywhere paradigm for LLM architectures. By basing collaboration on a language specification rather than a specific framework's vision, Axon fosters open cooperation and empowers researchers to implement highly specialized architectures without giving up optimization infrastructure or accepting deployment lock-in. Axon allows for concise, auditable specifications that can be automatically compiled to standalone implementations for leading frameworks: PyTorch, PyTorch with Triton, JAX, MLX and vLLM. In 467 inference benchmarking experiments on models ranging from 135M to 32B parameters, we demonstrate median speedups of 7% on PyTorch, 12% on PyTorch with Triton, 91% on JAX, and 107% on MLX, compared to the reference implementations from Transformers. When deployed as native vLLM architectures with PagedAttention and KV-cache, Axon models achieve a 58% median speedup over Transformers implementations.

---


### 71. [EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891)

**<font color=#1a73e8>作者：</font>** Bhavya Sukhija, Oliver Groth, Mohit Shridhar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How to efficiently finetune robot policies to learn new tasks on the fly? State of the art robotic manipulation policies are based on behaviour cloning of large vision-language-action (VLA) models with billions of parameters on huge teleoperation datasets. While this simple approach has enabled significant advances for robotic manipulation, finetuning of VLA policies for learning new tasks still remains an open problem. In particular, collecting teleoperation datasets requires hundreds of hours of expensive human labour and the alternative, reinforcement learning (RL), can be notoriously sample-inefficient especially for long-horizon tasks. In addition, RL with VLAs imposes several challenges due to the model's size and architectural design. In this work, we propose EXIMO, an efficient algorithm for finetuning of VLA policies. EXIMO operates in three stages: explore, imitate, and optimize. During the explore phase, EXIMO equips the VLA with a vision language model (VLM) that acts as a planner. The VLM thinks and breaks down challenging long-horizon problems into shorter ones for the VLA. The VLM, together with the VLA, is used to collect an orchestrated dataset on new tasks. During the imitate phase, the VLA is finetuned with the orchestrated data. Finally, during the optimize stage, we use residual off-policy RL to further finetune the policy. In our experiments, we ablate all three stages of EXIMO and show that it outperforms existing approaches significantly in terms of sample-efficiency and final performance.

---


### 72. [Interrupting the Loop: Periodic Subject Changes Raise Judged Surprise and Connection in Base Language Models](https://arxiv.org/abs/2608.19893)

**<font color=#1a73e8>作者：</font>** Roberto I. Ono Filho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Where does the novelty a base language model produces with no task come from, and what can an LLM judge of a long stream actually see? We dismantle a cognitively inspired generation loop over 24 conditions on three base models. Most of its effect lives in one operation: a new subject injected every few hundred tokens (an interruption) into a stream whose literal repetition is damped (habituation). We judge windows of generated text only, with the premise as the unit (n=10) and a judge measured for repeatability, against a second judge family and against human readers. Under that protocol the interruption raises judged surprise by 1.2 to 1.4 points and connection by 0.8 over habituation alone. A connective that asks for continuity hurts; a bare paragraph break adds nothing detectable on fresh text; a reset context does at least as well as a kept one; and a pre-registered replication on new premises confirms the primary contrast. Three things the window judge could not see changed the first version of this study, and we think they are of general use. The judge scores the experimenter's injected sentence as the model's own. A fixed rotation of injected sentences makes the model replay its earlier segments from beyond the judge's horizon, and the judge scores the replay as surprise and connection (65-80% of post-interruption windows at periods 150-300). And the local gains do not compose: no arm produces an integrated document. The salience monitor, the in-loop judge, memory across interruptions and a judge-gated Review run with a gate that opens add nothing. On a problem with a verifier (online bin packing), the interruption multiplies valid, distinct candidate heuristics three- to fourfold without raising the quality of the best. We report an evaluation protocol for long generation and a controlled characterization of a simple intervention, not a mechanism of creativity.

---


### 73. [MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection](https://arxiv.org/abs/2608.19901)

**<font color=#1a73e8>作者：</font>** Yue Wang, Yi Liu, Gelei Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent Skills extend LLM agents with reusable instruction packages that may also include scripts, resources, and service configuration. This creates a direct distribution channel for malicious behavior, yet existing malicious-Skill datasets are fragmented across sources, artifact formats, evidence regimes, and benign coverage; duplicated and structurally related content further complicates direct aggregation and evaluation. We present MaliciousSkillBench, a comprehensive benchmark for malicious Agent Skill detection. We consolidate 13 public sources, 11 of which contribute Core malicious artifacts, and reduce 8,414 raw malicious records to 7,539 normalized-unique identities in 4,588 operational structural families. After conservative cross-label conflict exclusion, the primary benchmark contains 9,740 Skills: 7,505 malicious and 2,235 benign. To characterize its coverage, we harmonize 11 attack categories for 4,983 malicious identities with supported source-native mappings and find substantial differences in threat composition across sources. We then evaluate three learned text detectors and three off-the-shelf Skill scanners. Learned detectors achieve 0.882-0.932 Random Macro-F1 but only 0.653-0.665 under Source-Disjoint evaluation; the strongest word TF-IDF SVM scores 0.932/0.916/0.665 on Random/structural-disjoint/Source-Disjoint while retaining 95.6% malicious recall but producing 62.4% benign FPR on held-out sources. Off-the-shelf scanners occupy different but also unsatisfactory operating regimes, reducing false positives only at the cost of sharply lower malicious recall. Together, these results show that reliable malicious-Skill detection requires both broader cross-source benchmark coverage and evaluation that jointly measures attack detection and benign over-flagging.

---


### 74. [Learning how to Forget: Fine-tuning for Long-Context Sparse Attention](https://arxiv.org/abs/2608.19920)

**<font color=#1a73e8>作者：</font>** Matthias Seeger, Zeyu Zhang, Vihang Patil 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A lot of prior work addressed key-value (KV) cache selection and compression by sparse attention to enable long-context inference for transformer language models without excessive hardware budgets. We provide a new method for fine-tuning models with sparse attention. It works for any KV cache policy, runs on a moderate hardware budget (e.g., a single Nvidia A100 GPU with 40 GB RAM), and allows the model to co-adapt with the policy, often outperforming models trained with exact attention (sequence parallelism). We also provide an efficient implementation of H2O sparse attention (the leading policy in our experiments) with dedicated scaled dot product attention kernel support. KeysAndValues (this https URL), a new open source library for long-context inference and fine-tuning, provides easy-to-use and performant code for all methods discussed here.

---


### 75. [From Noise to Signal: Improving Security Log Anomaly Detection Using LLMs with Endpoint-Specific Logs](https://arxiv.org/abs/2608.19938)

**<font color=#1a73e8>作者：</font>** Christopher Henshaw, Gour Karmakar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing approaches to anomalous behaviour log detection, such as Wazuh rely primarily on predefined detection rules, while statistical anomaly detection approaches such as OpenSearch identify deviations from previously observed behavioural patterns. Recent research has investigated LLMs for log anomaly detection because of their ability to interpret semantic and contextual information. However, LLM-based approaches can be affected by prompt construction, noisy log data, and reliance on generic datasets that may lack endpoint-specific authentication behaviours. To address these limitations, this study develops a standardised instruction-based LLM classification framework for detecting anomalous authentication behaviours, including borderline cases. A controlled cybersecurity testbed was developed to generate endpoint-specific authentication data, producing a curated dataset comprising normal, borderline, and anomalous behavioural scenarios. Three instruction-tuned LLMs, Meta Llama 3.1 8B Instruct, Qwen 2.5 7B Instruct, and GPT-OSS 20B, were evaluated against Wazuh rule-based detection and OpenSearch Anomaly Detection using a common ground-truth severity framework. Meta Llama 3.1 8B Instruct achieved the strongest overall end-to-end detection performance, with an accuracy of 89.3%, recall of 88.2%, F1-score of 91.8%, and false negative rate of 11.8%. In comparison, Wazuh achieved an accuracy of 52.0% and false negative rate of 68.6%, while OpenSearch achieved an accuracy of 49.3% and false negative rate of 74.5%. Meta Llama also detected 80% of the borderline anomalous scenarios, compared with 20% for Wazuh and 15% for OpenSearch. Qwen achieved lower overall detection performance than Meta Llama but recorded the lowest average inference latency and 100% structured-response validity. GPT-OSS demonstrated strong classification performance when valid responses were produced.

---


### 76. [Natural Language Code Retrieval for 1C:Enterprise: An Open Benchmark and Efficient Bi-Encoder](https://arxiv.org/abs/2608.19957)

**<font color=#1a73e8>作者：</font>** Konstantin Chesnokov, Chingiz Mingazov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language code retrieval is a rapidly evolving task in computer science. However, the 1C:Enterprise ecosystem combines Russian syntax with highly domain-specific terminology, for which open datasets and specialized models have been virtually non-existent. We present a comprehensive pipeline for 1C code retrieval: an open benchmark of 3,413 real-world, PII-scrubbed query-code pairs, a reproducible evaluation harness, and a specialized bi-encoder. To overcome scarce labeled data, we fine-tune on 784,057 synthetic triplets generated by google/gemma-4-26B-A4B-it from public code repositories, using Matryoshka Representation Learning (MRL) and a privacy-aware tokenizer. Because the benchmark subsets differ in size, we report balanced-subset macro, query-weighted micro, and forum-only results. Our model reaches 0.5992 balanced macro nDCG@10, 0.5044 micro, and 0.4617 on forum, versus 0.4932 macro for the baseline architecture and 0.5404 for google/embeddinggemma-300m. Removing every benchmark example flagged by the conservative exact/13-gram overlap audit leaves 0.6011 balanced macro (0.5010 micro), indicating that detected train-benchmark overlap does not explain the headline result. MRL truncation to 256 dimensions preserves 99.9% of retrieval quality while reducing dense-index storage and exact similarity arithmetic by a factor of three.

---


### 77. [Open-Vocabulary 3D Object Detection with Co-Distillation Discovery and Dual Guidance Robust Training](https://arxiv.org/abs/2608.19973)

**<font color=#1a73e8>作者：</font>** Shangbo Yuan, Jie Xu, Xiaofeng Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, open-vocabulary 3D object detection (3D-OVD) has gained increasing attention for its ability to detect unseen objects in 3D scenes. Existing approaches typically adopt a two-stage pipeline that first discovers novel objects using foundation models and then trains a 3D-OVD model based on these discovered objects. Although effective, this pipeline often suffers from inaccurate localization and mismatched classification during the discovery stage, which subsequently limits the performance of the model training stage. To address these limitations, we advocate for improving both the reliability of novel object discovery and the robustness of model training, and propose an innovative framework. Specifically, for reliable discovery, our co-distillation strategy distills high-quality novel objects by applying Hungarian matching over a comprehensive score that incorporates geometric consistency, structural objectness, and semantic certainty. To enhance robust model training, we further propose a dual-guidance learning scheme, incorporating a scene-awareness-guided uncertainty regularization for the regression head and an LLM-guided hierarchical alignment for the classification head, effectively mitigating the negative effects of imprecise 3D bounding boxes and semantic ambiguity. Extensive experiments on SUN RGB-D and ScanNetV2 demonstrate that our method achieves significant performance gains over state-of-the-art approaches. Code is available at this https URL

---


### 78. [ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance](https://arxiv.org/abs/2608.19974)

**<font color=#1a73e8>作者：</font>** Yiyang Luo, Yihang Jiang, Qijun Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents in financial markets may cite rules yet still submit orders that violate executable constraints or misread surveillance evidence. We introduce ReguSim, a controlled financial-compliance environment, and ReguBench, a target-marked monitoring benchmark, to separate four artifacts: stated reasoning, attempted action, execution enforcement, and monitor evidence. In trader runs with DeepSeek V4 Pro and Gemini 3.5 Flash, visible rules reduce but do not eliminate rejected actions, and incentive or persona framing shifts behavior. A bridge study shows that trader rationales can mislead an independent monitor unless enforcement evidence is shown. In monitoring, simple structured baselines either match or exceed prompt-only LLMs. The results frame financial compliance evaluation as an audit of rule-grounded actions and evidence use, rather than a single compliance score.

---


### 79. [HealMed: Multilingual Evaluation of Large Language Models in Medicine](https://arxiv.org/abs/2608.19981)

**<font color=#1a73e8>作者：</font>** Yingjian Chen, Fan Gao, Sherry T. Tong 等 45 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present HealMed, an expert-reviewed benchmark for multilingual evaluation of large language models in medicine. HealMed contains 1,000 examples in each of nine languages, drawn from nine datasets and covering three task formats: MCQA, NLI and open-ended QA. The benchmark was developed over two years by 23 physicians and medical experts based across nine countries and regions. Each translation was evaluated and revised by two experts fluent in English and the corresponding target language. On HealMed, performance declined most in low-resource languages, although the size of the gap varied markedly across languages and models. The strongest proprietary models were the most stable across languages, whereas many open-source and medically specialized models showed larger and less consistent gaps. Medical specialization alone did not ensure multilingual robustness. Furthermore, expert revision could either raise or lower measured performance, indicating that translation quality materially affects cross-language evaluation results.

---


### 80. [Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees](https://arxiv.org/abs/2608.19993)

**<font color=#1a73e8>作者：</font>** Yu Chen, Ruishuo Chen, Xun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Loading reusable skill documents into a bounded context window is now the primary way large language model (LLM) agents acquire task-specific capabilities, which makes skill selection a first-order determinant of task performance and token cost. Yet current agents score skills independently by semantic relevance and assemble the set by top-$k$ or greedy packing, with no quality guarantee or cost awareness on the selected set. As a result, redundant or poorly chosen skills waste scarce context tokens and can even degrade performance. We give the first model of how the selected skill set shapes execution outcomes and cast skill selection as an optimization problem: choose a skill set under a hard token budget to maximize a monotone submodular benefit minus context penalty. For this problem, we develop Best Prefix Selection (BPS), a polynomial-time algorithm, and prove, to our knowledge, the first performance guarantee for skill selection: a bicriteria $(1-1/e,1)$ approximation whose benefit coefficient is optimal in polynomial time. On a contamination-controlled BigCodeBench variant, BPS outperforms all the baselines, reaching $0.73$ measured task success versus $0.20$--$0.52$ for released skill routers, text retrievers, and the executor's own selection, on $28\%$ fewer tokens than the strongest released router.

---


### 81. [From Street View Imagery to Street Quality Indicators: Vision Language Inference for the Suburban 15-minute City](https://arxiv.org/abs/2608.20026)

**<font color=#1a73e8>作者：</font>** Joan Perez, Giovanni Fusco  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streetscape quality has become a central concern in contemporary urban planning, particularly within the framework of the pedestrian-friendly 15-minute city, where walkability and public-space quality are increasingly recognized as key determinants of urban performance. However, assessing streetscape qualities across large suburban and peri-urban territories remains challenging due to the time and resource demands of conventional field surveys. This paper presents a planning-oriented assessment of streetscape qualities in the north-eastern periphery of Nice (France) using the latest release of SAGAI (Streetscape Analysis with Generative AI), an open-source workflow that leverages vision-language models (VLMs) for large-scale streetscape analysis from Google Street View imagery. The new release addresses limitations of the original framework through improved image acquisition, geographically consistent view generation, support for multiple VLM architectures, consensus-based inference, and an integrated analytical environment. The workflow is applied to several thousand street-level observations to evaluate qualities relevant to pedestrian-friendly urban environments: sidewalk presence, pedestrian entrance density, and vegetation. The resulting maps reveal that the desired streetscape qualities characterize only a fraction of today's suburban streetscapes, mainly in compact developments and traditional suburban faubourgs, while they are particularly lacking on residential hills. The analysis demonstrates the potential of contemporary VLMs to support urban diagnostics in extensive suburban territories where fieldwork would be prohibitively time-consuming. Beyond the case study, the paper illustrates how recent advances in vision-language models can contribute to evidence-based planning by enabling scalable, flexible, and interpretable assessments of urban public-space quality.

---


### 82. [What You Can't See Is What You Learn: Restricted Evidence Visibility Favors Compositional Generalization in Shared-Genome Language-Model Societies](https://arxiv.org/abs/2608.20054)

**<font color=#1a73e8>作者：</font>** Narcis Marincat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-module systems often expose every module to the full input. We test whether restricting evidence visibility changes which solutions gradient-based training discovers. Four-cell societies share one frozen pretrained language model and one low-rank adapter, communicating only through two model-width continuous vectors in a fixed relay. On a prospectively sealed natural-language function-composition task, we train ten matched restricted/global pairs sharing initialization bytes, training order, token layout, parameters, and computation; only the attention mask differs. Restricted societies outperform their globally visible twins by at least 20 points at both depths in 9 of 10 pairs, with median paired advantages of 0.7648 and 0.6050. Cutting communication reduces every restricted society to chance, and the depth-three advantage remains 0.558 on programs whose composite function never appeared in training. Across six audited restricted societies, same-value packet transplants preserve behavior at 0.94-1.00 across all tested interfaces; destructive interventions collapse performance; and counterfactual packets redirect outputs toward the mathematically predicted answer. The sole high-performing global model also requires communication, but its same-value packets are not interchangeable across episodes. Restricted visibility is thus not necessary for composition; under this protocol it substantially increases the probability of a generalizing relay and favors a reusable, value-indexed interface. The complete preregistered battery nevertheless formally fails because restricted-arm median depth-three accuracy is 0.6988, below the 0.70 floor. An earlier qualification cohort likewise yielded 0/10 complete passes: one model met every task-performance gate, but all ten failed ordinary-language preservation, confining the system to explicitly task-gated use.

---


### 83. [EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models](https://arxiv.org/abs/2608.20055)

**<font color=#1a73e8>作者：</font>** Yiting Qu, Ziqing Yang, Chi Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hidden chain-of-thought (CoT) traces, especially those from frontier proprietary large reasoning models (LRMs), are valuable model assets. Yet whether these hidden CoTs can be directly extracted from black-box models remains largely unexplored. In this work, we systematically study whether hidden CoTs can be extracted near-verbatim from black-box LRMs through API interactions. We identify a previously overlooked reasoning replay surface between tool calls and develop EchoCoT, a multi-step attack that iteratively extracts hidden CoTs using API-returned fidelity signals. We further develop an LLM-based optimization framework that automatically searches for an effective universal injection trajectory across various datasets. We evaluate EchoCoT on three open-source and five frontier proprietary LRMs. On open-source LRMs, EchoCoT achieves up to 66.4\% near-verbatim extraction success, with the extracted trace length within 10\% of the target and at least 90\% of tokens exactly matching the target CoT. The same injection trajectory also generalizes to unseen datasets, achieving up to 80\% extraction success under the same criterion. For tested frontier proprietary LRMs, a substantial fraction of extracted CoTs closely align with provider-reported reasoning lengths and available CoT summaries. EchoCoT can also extract very long CoTs: on Gemini-2.5, it extracts 33,463 tokens from a 32,948-token target. These results establish hidden-CoT extraction as a practical security risk and highlight the need to better protect hidden CoT assets.

---


### 84. [Let's Scale Step by Step: Compute-Efficient Hyperparameter Transfer for Large-Scale Mixture-of-Experts](https://arxiv.org/abs/2608.20061)

**<font color=#1a73e8>作者：</font>** Nayeon Kim, Hojin Lee, Yunju Bak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures significantly expand model capacity without a proportional increase in computational cost. However, optimizing their hyperparameters---particularly the learning rate---at extreme scales of both model size and token budget via sweeping remains computationally prohibitive. In this paper, we propose a compute-efficient, two-step hyperparameter transfer framework that estimates optimal learning rates for training large MoE models by transferring them across scaling model widths, and subsequently extrapolating to trillion-token horizons. First, we formulate a Maximal Update Parameterization ($\mu$P) adaptation for MoE architectures utilizing Multi-head Latent Attention (MLA) and the Muon optimizer, demonstrating that optimal learning rates transfer consistently across width-scaled models. Second, we extend this transferability along the token dimension by establishing a predictive scaling law. By applying linear regression to the optimal values derived from small proxy models on limited budgets, we successfully extrapolate the ideal learning rate to massive training horizons (e.g., 10 trillion tokens) with high fidelity ($R^2=0.95$). Consequently, this indicates that proxy training on small models is sufficient to determine the optimal learning rate for the extensive training of large-scale MoEs. We apply the proposed methodology to pretrain our foundation model (155B total, 17B active parameters) from scratch, and the stable training and evaluation results validate that optimal configurations for full-scale target models can be accurately predicted with minimal ablation costs.

---


### 85. [V-REX: Efficient Specialist VLM Training for Veterinary X-Rays](https://arxiv.org/abs/2608.20069)

**<font color=#1a73e8>作者：</font>** Tim Elsner, Nicole McNally, Andre Dourson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While generalist VLMs are expensive to train, creating domain experts is widely assumed to require fine-tuning increasingly large foundation models. We show that, in veterinary radiology, this assumption is misguided. By rethinking the entire VLM pipeline - from text tokenisation and pre-training to grounding and inference - we demonstrate that careful engineering can yield models that outperform much larger foundation models from scratch, without relying on any other data. Our approach introduces new strategies for generative pre-training and grounding that improve training efficiency, increasing data utilisation and downstream performance. Using only a fraction of the parameters, data, and compute of contemporary generalist models, we develop the first VLM capable of generating diagnostic reports for veterinary radiographs, surpassing open foundation models on this task by significant margin.

---


### 86. [TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring](https://arxiv.org/abs/2608.20097)

**<font color=#1a73e8>作者：</font>** Baixiang Liu, Haotian Che, Yuan Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) lets Large Language Models (LLMs) pull in up-to-date, domain-specific information instead of relying only on what they were trained on. Yet most RAG systems still draw from centralized databases with limited oversight, making it difficult to verify where a document came from, whether it has been tampered with, or whether it should be trusted at all. This is a serious problem in domains where both the timeliness and accuracy of retrieved content are critical, such as healthcare, finance, logistics, and legal case law, where a wrong or manipulated document can directly lead to bad decisions.
We present TrustRAG, a committee-based, blockchain-backed RAG system: before a document is used, it is certified by a committee of domain experts through a zero-knowledge protocol, and the committee's hidden scores are combined via secure multi-party computation into a trust score that any client can verify. These scores, along with the underlying document data, are maintained jointly across chains through hash commitments, so no document or score can be silently altered or dropped, and every ranking can be independently replayed and checked.

---


### 87. [Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design](https://arxiv.org/abs/2608.20099)

**<font color=#1a73e8>作者：</font>** Poomphob Suwannapichat, Boonyarit Changaival, Caesar Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based Multi-Agent Systems (MAS) achieve strong performance on complex reasoning tasks by coordinating multiple agents, but at the cost of substantial token consumption. Recent work on automatic topology design, ARG-Designer, has reframed this problem as autoregressive graph generation. However, its training objective provides no explicit incentive for the model to generate sparse and efficient topologies. We address this limitation by introducing a Reward-Guided Autoregressive Graph Generation (RGA-Designer) inspired by Reinforcement Learning from Human Feedback (RLHF). We train a reward model that jointly captures task correctness and structural compactness, and then fine-tune the pretrained graph generator using the reward model as feedback. Our method preserves task accuracy at the level of ARG-Designer while reducing token consumption by an average of 20.5%.

---


### 88. [OenoBench: A Wine-Domain Benchmark for Knowledge-Grounded Evaluation of Large Language Models](https://arxiv.org/abs/2608.20106)

**<font color=#1a73e8>作者：</font>** Nikita Khudov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce OenoBench, a wine-domain knowledge benchmark of 3,266 multiple-choice questions across six pillars (regions, grape varieties, viticulture, winemaking, producers, business) and four difficulty tiers. The corpus is built from 38,104 atomic, source-anchored facts extracted by 35 provenance-verified scrapers from government registries (INAO, TTB, OIV), peer-reviewed journals, and Wikipedia/Wikidata. Our methodological contribution is an LLM-driven pipeline in which language models reformat verified facts and audit the result, but never serve as the source of truth: every claim traces to a URL, every question is generated by one of five strategies across five generator families, and every question is scored by a nine-agent audit calibrated against a human gold sheet via Cohen's $\kappa$. Evaluating sixteen frontier configurations, we find: (i) overall accuracy spans 53%-84%, led by o3 at 83.6%; (ii) reasoning-mode lift concentrates in DeepSeek R1 (+6.8pp) and is absent in Claude Opus and Gemini Pro; (iii) Anthropic shows +9pp self preference on its own questions while Google shows -8pp inverse preference; (iv) frontier open-weight models share the cost-vs-accuracy Pareto frontier with proprietary reasoning models; and (v) every config gains around 33pp on closed-book solvable items, revealing a parametric-recall ceiling that only the contextual slice avoids. We release corpus, audit findings, human-review app, and construction code under CC-BY-SA-4.0.

---


### 89. [BeyondMasks: Evaluating Causal and Physical Consistency in Video Object Removal](https://arxiv.org/abs/2608.20107)

**<font color=#1a73e8>作者：</font>** Yigit Ekin, Enes Sanli, Aykut Erdem 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative video models have significantly improved visual realism in video object removal, yet evaluation protocols still focus on masked region fidelity, treating removal as local inpainting. In real scenes, object removal is a causal intervention: eliminating an object also requires removing its induced physical effects, such as shadows, reflections, illumination changes, translucency, and dynamic traces. Existing benchmarks lack aligned clean references or remain limited to simplified synthetic settings, preventing systematic evaluation of causal consistency. We introduce BeyondMasks, a paired benchmark for causally consistent video object removal, consisting of temporally aligned synthetic and real world video pairs with clean background references. The dataset spans diverse photometric, geometric, volumetric, and dynamic interactions, and supports both mask based and instruction driven editing. We further propose CORE, a structured vision language model based evaluation protocol that jointly measures object disappearance and after effect consistency, aligning more closely with human judgments than existing metrics. Benchmarking state of the art methods reveals systematic failures in removing secondary physical effects despite high masked region fidelity, exposing a gap between visual plausibility and causal correctness. BeyondMasks reframes video object removal as causal scene consistency rather than local reconstruction and provides a unified framework for its evaluation.

---


### 90. [When Text and Numbers Disagree: Evidence Arbitration in Large Language Models](https://arxiv.org/abs/2608.20116)

**<font color=#1a73e8>作者：</font>** Mattia Carletti, Edward Phillips, Fredrik K. Gustafsson 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in settings where textual summaries, numerical observations, and external tool outputs may provide conflicting evidence. We study how LLMs arbitrate between such sources when they support opposing decisions. To do so, we introduce a controlled synthetic benchmark in which latent risk trajectories generate both numerical time series and natural language summaries, allowing us to construct conflicts where exactly one evidence source is aligned with the ground-truth label. This design lets us independently manipulate modality, temporal recency, source reliability, and evidence provenance. Across open-weight instruction-tuned models, we find that arbitration behaviour is systematic rather than random: models exhibit distinct text-versus-number preferences, follow temporal recency more consistently than explicit reliability cues, and can over-rely on external forecasts even when they conflict with direct contextual evidence. These results suggest that current LLMs often rely on heuristic arbitration strategies when integrating heterogeneous evidence, highlighting a failure mode for tool-augmented decision systems.

---


### 91. [ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation](https://arxiv.org/abs/2608.20122)

**<font color=#1a73e8>作者：</font>** Linhan Cao, Siyuan Li, Jun Lan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large multimodal models (LMMs) have demonstrated strong OCR recognition capabilities, yet remain vulnerable to adversarial visual text that is readable to humans but challenging for models to localize and recognize. Existing OCR benchmarks mainly focus on natural or document-style text, while adversarial OCR evaluations remain limited in scale, task coverage, or region-aware evaluation. In this paper, we formulate adversarial OCR as a \textbf{grounded OCR perception} task and introduce \textbf{AdvSpot}, the first benchmark for grounded adversarial OCR evaluation. AdvSpot comprises 390 images with region-level annotations, spanning 5 primary categories and 13 fine-grained adversarial OCR types. To address this challenge, we propose \textbf{ArmorOCR}, a two-stage training framework for robust adversarial OCR perception. ArmorOCR first acquires missing adversarial OCR perception from privileged transformed observations through On-Policy Self-Distillation (OPSD), and then refines grounded OCR perception through Group Relative Policy Optimization (GRPO) with task-conditioned rewards for localization, recognition, full spotting, and visual question answering (VQA). Experiments on our AdvSpot, other adversarial OCR benchmarks, and general OCR benchmarks demonstrate that ArmorOCR consistently improves adversarial OCR perception while preserving competitive general OCR capability.

---


### 92. [Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving](https://arxiv.org/abs/2608.20129)

**<font color=#1a73e8>作者：</font>** Mehdi Azarafza, Faezeh Pasandideh, Ali Ehteshami Bejnordi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles require robust perception and decision-making capabilities to operate in diverse and unseen scenarios. While reinforcement learning and rule-based methods can provide effective control and safety mechanisms, their performance may degrade in situations requiring contextual reasoning. Large Language Models (LLMs) have demonstrated strong capabilities in understanding multimodal information and generating contextual reasoning, however, their use for direct vehicle control can introduce latency and hallucination risks. To address these limitations, a hybrid framework is proposed. This system uses an orchestrator to coordinate PPO-trained reinforcement learning and PID control, with LLM common-sense reasoning applied throughout the framework. LLM reasoning is further employed iteratively to refine the RL reward function for dynamic driving environments. The proposed framework is evaluated in highly randomized CARLA scenarios under diverse environmental and traffic conditions. The results demonstrate the potential of integrating LLM-based reasoning with conventional autonomous driving methods while retaining structured control and safety mechanism.

---


### 93. [DPC-Net: Dual-Prior Collaborative Network for All-in-One Image Restoration](https://arxiv.org/abs/2608.20141)

**<font color=#1a73e8>作者：</font>** Zhaokun He, Kangbiao Shi, Axi Niu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> All-in-One Image Restoration (AiOIR) aims to handle diverse degradations within a unified model. However, existing methods often overlook image semantics in degradation modeling and lack low-level visual priors during reconstruction, leading to structural distortions and semantic inconsistencies. To address these issues, we propose a novel Dual-Prior Collaborative Network (DPC-Net), which achieves high-quality restoration by jointly exploiting degradation-semantic coupled priors and low-level visual priors. Specifically, degraded images are fed into a Degradation-Aware Network (DAN) to extract degradation-semantic coupled features. To this end, a Vision-Language Model (VLM) supervises DAN by constraining its features distribution, introducing image semantics into the encoding of degradation patterns. A Degradation-Semantic Modulation Module (DSMM) further translates this guidance into degradation-semantic coupling and propagates coupled representations to the decoder. During decoding, knowledge bases provide low-level visual priors, and the Dual-Prior Collaborative Reconstruction Module (DPCR) integrates dual-prior information to guide degradation removal while preserving structure and semantics, producing high-fidelity restored images. Extensive experiments on multiple restoration benchmarks demonstrate that DPC-Net achieves superior performance against state-of-the-art AiOIR methods.

---


### 94. [FormalTCS: Benchmarking End-to-End Frontier Formal Theoretical Computer Science Research of Large Language Models](https://arxiv.org/abs/2608.20153)

**<font color=#1a73e8>作者：</font>** Dingzirui Wang, Xuanliang Zhang, Keyan Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown growing potential for automated theoretical computer science (TCS) research, yet existing benchmarks remain far from realistic research settings. We introduce \ourbenchmark, an expert-validated benchmark for evaluating LLMs on frontier, end-to-end TCS research. \ourbenchmark contains $175$ instances drawn from papers accepted to STOC, FOCS, SODA, and COLT in 2025-2026, preserving paper-specific definitions, assumptions, and proof dependencies, with expert-verified Lean formalizations and proofs. Evaluations of leading LLMs reveal that current models remain far from reliably completing the full research pipeline. In particular, autoformalization is the sharpest bottleneck: the best model achieves only $11.5$ on translating natural-language claims into formal theorem statements, compared with $28.6$ Pass@8 when proving human-provided formal statements. Building on \ourbenchmark, we further develop an automated TCS research framework that generates, formalizes, filters, and proves new claims. Of $64$ generated claims, only $6$ ultimately pass expert evaluation and proof verification, indicating that beyond formalization, limited research taste remains another major barrier to autonomous TCS research.

---


### 95. [DARS: Dual-Level Credit Assignment RL with Structured Reasoning for Instruction-Based Image Editing](https://arxiv.org/abs/2608.20161)

**<font color=#1a73e8>作者：</font>** Haoxiang Cao, Jiajiong Cao, Xuanpu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editing uses a planner-renderer pipeline: a vision-language model (VLM) first converts the instruction into an edit plan, and a diffusion model then executes that plan. Training such systems with only final-image rewards is inefficient because a poor edit does not reveal whether additional optimization should place more emphasis on the planner or the renderer, and even planner-dominant cases remain difficult to localize within a free-form reasoning trace. We present DARS, a reinforcement learning framework for dual-level credit assignment in this two-stage setting. Across modules, multi-plan multi-render rollouts estimate between-plan and within-plan reward variability for soft module routing, while rollout mean rewards provide hardness estimates for an adaptive curriculum. Within the planner, a four-field structured reasoning output enables a prefix-gated reward and token-level advantage reweighting, turning outcome-level feedback into localized supervision. Experiments on five benchmarks show that DARS outperforms a Joint~RL baseline with the same backbone, data, reward model, and rollout budget, with the largest gains on reasoning-intensive edits.

---


### 96. [Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection](https://arxiv.org/abs/2608.20169)

**<font color=#1a73e8>作者：</font>** Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a novel approach to efficient LLM agent harness optimization through adaptive validation task selection. Harness optimization iteratively rewrites the harness code based on validation performance, enabling substantial performance gains without updating the underlying model weights. Existing approaches, however, evaluate a fixed validation set in full at every iteration, incurring substantial evaluation costs even on tasks that become less discriminative as the harness evolves. We propose $\textbf{Task-CoEvolve}$, which co-evolves the validation tasks with the harness by addressing two challenges: selecting informative tasks and estimating full-set performance from partial evaluations. Task-CoEvolve builds on the observation that tasks on which candidate harnesses disagree are more informative for distinguishing among them than tasks that are consistently solved or failed. It uses variance-weighted sampling based on past outcomes to focus evaluation on tasks near the agent's capability frontier, with the sampling distribution adapting as the harness evolves. It then estimates full-set scores from the sampled tasks by accounting for their sampling probabilities, enabling consistent comparisons across iterations despite evaluating different subsets. Experiments on online text classification and Terminal-Bench 2.1 show that Task-CoEvolve consistently outperforms fixed-subset baselines and matches the final performance of full-set search while reducing the number of evaluations during optimization by 80%. Code will be released at this https URL.

---


### 97. [Decoding silent reading from non-invasive EEG](https://arxiv.org/abs/2608.20186)

**<font color=#1a73e8>作者：</font>** Ingo Marquardt, Anthilia Alchanat, Priyanka Jain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-invasive decoding of inner speech faces a fundamental data problem: a corpus pairing brain activity with a person's spontaneous inner monologue cannot be collected, and the available proxy paradigms (cued repetitive and retrospectively reported generative inner speech) are slow to acquire, poorly time-locked, and subject compliance is unverifiable. We therefore treat silent reading as a scalable proxy task and ask how much lexical and semantic information a contrastive decoder can extract from it. We report an open-vocabulary analysis of approximately 240,000 word presentations recorded from a single densely-sampled participant across 393 runs (ca. 49 h) of 19-channel dry-electrode EEG. Words from continuous narrative text were presented in rapid serial visual presentation, with typography randomised on every trial to partially decorrelate word identity from low-level visual form. A convolutional EEG encoder, optionally followed by a causal transformer, was trained with a CLIP-style contrastive objective to align short EEG windows with hidden-state embeddings of the presented word taken from a large language model. Decoding, evaluated as word-grouped top-10 retrieval against permutation baselines, was reliably above chance, extended to mid-frequency and rare words, and scaled log-linearly with training-data volume with no sign of saturation. Removing occipital and posterior-temporal electrodes reduced the word-level gain by roughly one third but left context tracking unchanged. Control analyses separate word-level decoding from narrative context tracking and from a non-neural positional prior introduced by the transformer's positional embedding. These results establish that open-vocabulary word-level information is recoverable from EEG during silent reading, and that decoding is data-limited rather than saturated.

---


### 98. [MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use](https://arxiv.org/abs/2608.20202)

**<font color=#1a73e8>作者：</font>** Mengru Wang, Haozhe Luo, Zhenqian Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory has become a key component of large language models, enabling them to retain information and learn from long-term interactions. However, existing memory benchmarks mainly evaluate whether information is correctly extracted, stored, and retrieved, while largely overlooking how retrieved memories reshape model reasoning and affect performance on the current task. We identify memory-induced cognitive traps: even faithfully recorded and semantically relevant memories can distort model reasoning or beliefs and degrade current task performance. To systematically evaluate these failure modes, we introduce MemTrapBench, which covers two forms of cognitive traps: Reasoning Fixation and Belief Distortion. Experiments across two model families and five representative memory frameworks show that MemTrapBench is challenging: all evaluated memory strategies underperform the no-memory setting, with even the strongest methods suffering drops of more than 10%. To mitigate these cognitive traps, we propose AdaptiveMem, a simple yet effective inference-time method that instructs LLMs to avoid memory traps. AdaptiveMem mitigates cognitive traps on MemTrapBench while preserving or improving performance on standard memory benchmarks across diverse memory frameworks.

---


### 99. [ContractScrub: A benchmark for final review of legal contracts](https://arxiv.org/abs/2608.20204)

**<font color=#1a73e8>作者：</font>** Yejin Bang, Kirsty Fielding, Brandan Oliver 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Legal work, with its heavy reliance on processing large amounts of text, is often considered one of the domains most exposed to the use of LLMs. Contract ``scrubbing,'' the final review of transactional agreements for errors and inconsistencies, is a particularly suitable task for automation, because it is routine, painstaking work requiring detailed attention to long documents. Scrubbing also seems to align naturally with the general capabilities expected of frontier LLMs around long-context reasoning, consistency checking, and named entity recognition (NER). Despite the economic value and potential for automation, no formal evaluations of LLMs performing contract scrubbing have been conducted. We introduce ContractScrub, the first benchmark designed to evaluate contract scrubbing capabilities, comprising contracts hand-crafted by experienced lawyers over diverse error categories such as misuse of defined terms, incorrect references, and inconsistent language. Frontier models perform surprisingly poorly with only one model reaching 0.75 macro average recall despite strong performance on seemingly related general benchmarks, demonstrating the practical limits of current models and the importance of narrowly targeted, domain-specific benchmarks for measuring real-world impact.

---


### 100. [Unwarping the Lens: A Physics-Grounded Approach to Video Glasses Removal](https://arxiv.org/abs/2608.20212)

**<font color=#1a73e8>作者：</font>** Radim Spetlik, David Futschik, Radek Danecek 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity removal of eyeglasses from video is a major challenge in facial attribute editing, as the underlying facial geometry is often obscured by complex refractive distortions and view-dependent specular reflections. While large-scale generative priors have shown promise in eye-glasses removal via static image inpainting, they often lack the structural constraints necessary to maintain identity, expression, and pose, leading to visible "identity drift" in both static images and dynamic sequences. In this paper, we propose a novel transfer framework that addresses the stochastic nature of generative priors. Our pipeline first extracts high-fidelity synthetic face images from a commercial-grade generative model (Nano Banana, Gemini 3 Pro Image), regularizes them via a three-stage structural filtering process to preserve identity, expression, and pose, and finally applies physically-based simulation of lens optics during training to provide diverse, paired data. This process transfers Nano Banana's photo-realistic, multi-view knowledge into a specialized restoration architecture, JFSnet (Joint Feature-Spatial network). JFSnet integrates DINOv2-based semantic features with a convolutional decoder for spatial reconstruction, leveraging translation equivariance constraints to improve temporal consistency and high-frequency detail preservation. Evaluations on the curated Flickr-Faces-HQ (FFHQ) subset (12,163 images) show that our approach achieves high fidelity and structural accuracy, while maintaining inference speed of 27.68 FPS. In perceptual studies on CelebV-Text video sequences, our results are consistently preferred over diffusion and GAN-based baselines for ocular consistency, temporal stability, and overall restoration quality.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-121](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
