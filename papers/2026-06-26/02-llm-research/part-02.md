# 🧠 大模型相关研究 | 2026年06月26日

> 本类共 **112** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-112](./part-03.md)

---

### 51. [Hybrid-IR: Dual-Path Hybrid Retrieval with Iterative Reasoning for Complex Medical Question Answering](https://arxiv.org/abs/2606.25338)

**<font color=#1a73e8>作者：</font>** Sheng Wan, Jiahui Zhang, Zicheng Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promising performance across a wide range of biomedical applications, including medical question answering (QA), yet they remain prone to hallucinations and outdated knowledge. Although retrieval-augmented generation (RAG) can alleviate this issue by incorporating external documents, there still exist two fundamental limitations. First, medical knowledge is often fragmented across documents, while most RAG methods rely on a single retrieval path, which makes it challenging to jointly preserve fine-grained semantic information and structured global associations. Second, static retrieval strategies are typically insufficient to support deep reasoning that is important in complex medical QA. In this paper, we present a dual-path retrieval framework with an iterative retrieval-reasoning mechanism termed "Hybrid-IR" for complex medical QA. The proposed Hybrid-IR integrates graph-based retrieval for exploration of structured knowledge and dense retrieval for fine-grained semantic matching. Moreover, the reasoning trajectory can be progressively refined through an iterative retrieve-reason loop. Experiments on three widely used medical QA benchmarks demonstrate the effectiveness of our Hybrid-IR.

---


### 52. [Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention](https://arxiv.org/abs/2606.25342)

**<font color=#1a73e8>作者：</font>** Luke McDermott, Robert W. Heath jr., Rahul Parhi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lifelong continual learning remains an obstacle on the path to human-like intelligence. Modern transformers show sparks of intelligence with in-context learning. The quadratic nature of attention, however, prohibits transformers from performing this process on arbitrarily long sequences. In this work, we argue that extending in-context learning to lifelong settings is a practical solution for continual learning in AI agents. In particular, we argue that \emph{parametric forms of attention} are needed to understand a lifetime of context with transformers on a fixed hardware budget. These attention mechanisms learn the relationship between keys and their associated values at test-time with parametric regression. Our generalization of parametric approaches (linear attention, state-space models, fast weight programmers, and test-time training layers) contrasts with nonparametric counterparts like softmax attention. They replace the ever-growing key-value cache with an online-trainable neural network, maintaining a constant memory footprint. We highlight how parametric attention currently fall short of lifelong learning due to limited memory capacity or costly online updates. To address these issues, we pose a set of open questions with novel insights to guide the field toward long-horizon agents.

---


### 53. [Efficient and Trainable Language Model Test-Time Scaling via Local Branch Routing](https://arxiv.org/abs/2606.25354)

**<font color=#1a73e8>作者：</font>** Yutong Yin, Mingyu Jin, Jin Pan 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling improves language-model reasoning, but existing approaches often face a difficult trade-off: long chain-of-thought sampling remains single-threaded, while sentence- or solution-level search can be computationally expensive and hard to train end-to-end. We introduce Local Branch Routing (LBR), a token-level test-time scaling framework that expands a small local lookahead tree, forwards all sampled branches through the language model, and uses a lightweight router to select the depth-1 subtree to commit. By routing over the hidden states of candidate local futures, LBR allows each token decision to use evidence beyond the root next-token distribution while avoiding full solution-level search. The resulting prune-shift-grow decoding process preserves discrete branch identities and defines a tractable tree-trajectory likelihood: newly grown nodes are counted when first sampled, and router decisions are assigned explicit probabilities. This enables end-to-end reinforcement learning with verifiable rewards, jointly optimizing the base model and router under the same likelihood-ratio principle as discrete-token RLVR. On synthetic hierarchical-planning tasks, LBR shows that post-candidate hidden states provide useful routing evidence. On mathematical reasoning benchmarks, LBR improves both Pass@1 and Pass@32 over discrete chain-of-thought, vanilla discrete-token RLVR, and RL-compatible soft-token branching baselines. These results suggest that lightweight local branching offers an efficient, trainable, and discrete form of language-model test-time scaling.

---


### 54. [Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games](https://arxiv.org/abs/2606.25358)

**<font color=#1a73e8>作者：</font>** Gabriel Santos, Rita Julia, Marcelo Nascimento  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assessing financial literacy during gameplay without disrupting the learning experience remains a key challenge in serious games for education. We present the Agentic BKT pipeline, a multi-agent large language model architecture for stealth assessment of financial competencies from open-ended gameplay events. The pipeline processes events from a 2D platformer serious game aligned with the OECD/INFE financial literacy framework through four phases: (1) the game captures every player decision as a structured event log; (2) an LLM event classifier labels each action on a four-point rubric validated against three domain experts (Fleiss kappa = 0.624, substantial agreement); (3) four domain-specific agents specializing in risk mitigation, investing, spending, and credit management perform session-level reasoning over behavioral trajectories, feeding per-competency Bayesian Knowledge Tracing that estimates mastery within each domain; and (4) an expert judge agent synthesizes the domain-level estimates into an overall mastery score. Evaluated with 193 K-12 participants across 264 game sessions, the Agentic BKT pipeline yields mastery estimates significantly correlated with learning gain (r = 0.276, p = 0.0001) and post-test scores (r = 0.333, p < 0.0001) while showing no correlation with pre-test scores, providing both convergent and discriminant validity. The multi-agent approach approximately triples the predictive validity of a single-LLM baseline (r = 0.095, not significant) in this study, demonstrating that domain decomposition and session-level reasoning play a central role in capturing the multidimensional nature of financial literacy from gameplay

---


### 55. [Hypergraph Normal World Models for Logical Visual Anomaly Detection](https://arxiv.org/abs/2606.25368)

**<font color=#1a73e8>作者：</font>** Weizhi Nie, Zibo Xu, Weijie Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual anomaly detection is often deployed with only normal training images. Most one-class detectors map test patches or features to a normal reference distribution. This works well for local structural defects. Logical anomalies are different. Each visible part may look normal, while the whole image violates a normal count, co-occurrence, or spatial relation. This paper studies whether a model can learn such a category-specific normal world from nominal images alone. We propose the Hypergraph Normal World Model, a normal-only detector that distills frozen DINOv2 patch tokens into patch, relation, and hypergraph statistics. It builds spatial hyperedges over token groups. It then scores each test image with an information quotient that separates local, relational, hyperedge, and hyperedge-relation evidence. On the available MVTec LOCO breakfast-box validation data, the full hypergraph model improves logical anomaly AUROC from 0.8434 for DINOv2 patch-kNN to 0.9279. It also improves over the non-hypergraph variant, from 0.9013 to 0.9279. Few-shot experiments show that the model remains effective with very limited normal images. We also test whether the score reflects normal-world knowledge rather than a shallow mapping. t-SNE separates logical anomalies in the learned energy space. Relation counterfactuals increase the information quotient by 83.13 on average. Random hypergraphs reduce logical AUROC, and hyperedge attribution is much larger on logical anomalies. Qualitative examples show that high scores are driven by relation-bearing terms. These results suggest that logical visual anomaly detection should model normal relations, not only normal local patches.

---


### 56. [Beyond Visual Forensics: Auditing Multimodal Robustness for Synthetic Medical Image Detection](https://arxiv.org/abs/2606.25375)

**<font color=#1a73e8>作者：</font>** Ching-Hao Chiu, Hao-Wei Chung, Gelei Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid adoption of generative AI, synthetic medical images pose growing risks, including diagnostic deception and insurance fraud. Although prior work has explored vision-language model (VLM)-based synthetic image detection, these evaluations typically consider images in isolation. In clinical practice, however, images are interpreted alongside structured records and metadata, and VLMs are increasingly deployed under joint image-record inputs. We uncover a previously underexamined multimodal vulnerability: when given both modalities, VLMs may overweight record context in authenticity judgments, such that the same image receives different predictions solely due to changes in its accompanying text. This raises concerns about robustness in real-world deployment. To systematically characterize this effect, we reformulate synthetic medical image detection as an audit of multimodal robustness at the image-record interface and introduce a paired benchmark that holds the image fixed while swapping controlled metadata variants. Across multiple imaging modalities, we evaluate diverse open-weight and frontier API VLMs and quantify how metadata alone shifts authenticity predictions. Our benchmark provides a standardized tool for assessing and improving multimodal robustness beyond image-only settings. The code is available at this https URL.

---


### 57. [A Survey of Toxicity Detection and Mitigation Strategies for Multilingual Language Models](https://arxiv.org/abs/2606.25380)

**<font color=#1a73e8>作者：</font>** Soham Dan, Himanshu Beniwal, Thomas Hartvigsen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed across languages, but their safety behavior remains uneven across linguistic and cultural contexts. This survey synthesizes work on toxicity detection and detoxification for multilingual LLMs. We first catalogue threat models that exploit language choice, translation pivots, code-switching, orthographic variation, multi-turn interaction, and post-deployment fine-tuning to weaken safety alignment. We then organize task formulations (toxic-to-neutral rewriting, toxicity classification, and toxic-generation evaluation), multilingual detection approaches (cross-lingual encoders, translation pipelines, representation-level probes, and LLM-based detectors), and mitigation strategies spanning data filtering, supervised and preference-based tuning, decoding-time steering, representation editing, and multilingual guardrails. Across these areas, we identify persistent challenges: uneven language coverage, culturally contingent definitions of harm, fragmented evaluation protocols, and the risk that detoxification suppresses legitimate dialectal or identity-related expression.

---


### 58. [BrainAgent: A Large Language Model-Driven Multi-Agent Framework for Autonomous Brain Signal Understanding](https://arxiv.org/abs/2606.25400)

**<font color=#1a73e8>作者：</font>** Yangxuan Zhou, Sha Zhao, Jiquan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Brain-Computer Interfaces (BCIs) and brain signal understanding are pivotal for clinical health and next-generation interactions. Despite this significance, its widespread adoption in real-world scenarios remains restricted, primarily because current analytical paradigms lack sufficient agentic intelligence. First, existing methodologies impose prohibitive technical barriers, requiring extensive specialized expertise. Second, they remain inherently static and task-specific, failing to execute the complex, long-horizon workflows essential for real-world deployment. To accelerate the democratization of brain signal understanding, we draw inspiration from Large Language Models (LLMs) to introduce BrainAgent, an LLM-driven multi-agent framework designed to ground abstract natural language intent into rigorous, executable, and end-to-end processing pipelines. BrainAgent employs a hierarchical architecture where a central supervisor orchestrates specialized sub-agents for adaptive task decomposition and execution. Furthermore, we establish a comprehensive, systematic benchmark for evaluating agentic systems in brain signal analysis. Empirical results demonstrate that BrainAgent effectively automates complex workflows with superior reliability, marking a paradigm shift toward democratized brain signal understanding.

---


### 59. [Beyond Next-Observation Prediction: Agent-Authored World Modeling for Sequential Decision Making](https://arxiv.org/abs/2606.25421)

**<font color=#1a73e8>作者：</font>** Guangfeng Cai, Kaibing Yang, Shuo He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent studies on world modeling for Large Language Model (LLM) agents typically formulate the learning objective as next-observation prediction. However, this objective ties supervision to what a transition happens to reveal, which may omit the dynamics most relevant to the agent's current decision. To bridge this gap, we propose Agent-Authored World Modeling (AAWM), a training procedure that constructs supervision from the policy's own decision needs. Specifically, at each state, the agent identifies what it needs to understand about the environment before acting. These needs drive the retrieval of relevant transition evidence across trajectories, which is then synthesized into training targets that capture decision-oriented dynamics instead of reconstructing the next observation. This aligns the training objective with the dynamics the policy needs before acting, not with the contents of the next observation. Experimental results validate the effectiveness of AAWM across multiple environments and training settings. These results show that decision-aware world-model targets provide a more effective learning signal than next-observation prediction.

---


### 60. [PolicyAlign: Direct Policy-Based Safety Alignment for Large Language Models](https://arxiv.org/abs/2606.25442)

**<font color=#1a73e8>作者：</font>** Chang Wu, Junfeng Fang, Houcheng Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment of large language models (LLMs) typically depends on high-quality supervision data, such as safe demonstrations or preference pairs. However, in real-world deployment, emerging safety requirements are often specified as natural-language policies, while corresponding supervision data may be costly, delayed, or unavailable. This creates a mismatch between rapidly evolving safety policies and conventional data-driven alignment methods. To address this, we propose PolicyAlign, a simple yet effective framework for directly aligning LLMs with safety policies. Given a safety policy, PolicyAlign first synthesizes policy-violating instructions and then performs on-policy self-distillation to internalize policy-guided behavior. To improve training stability and data efficiency, we further introduce Policy-Sensitive Filtering, which selects instructions where the policy induces the largest behavioral shift. Experiments across multiple models show that PolicyAlign consistently improves safety while maintaining low over-refusal and preserving general capabilities. PolicyAlign also generalizes to medical, legal, and financial safety scenarios, highlighting its potential as a scalable and maintainable approach to policy-based LLM safety alignment. The code is released at this https URL.

---


### 61. [The Interplay of Harness Design and Post-Training in LLM Agents](https://arxiv.org/abs/2606.25447)

**<font color=#1a73e8>作者：</font>** Kyungmin Kim, Youngbin Choi, Seoyeon Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-integrated LLM agents are often wrapped within a harness: the scaffolding that determines which tools are exposed, how they are described, and what auxiliary information accompanies each per-step observation. While agents are routinely post-trained, this scaffolding is typically treated as a fixed engineering detail, with design effort limited to the training-free regime. Moreover, existing post-training algorithms assume a static environment, even though tool environments and tasks often shift upon deployment. To address this gap, we extend $\texttt{ALFWorld}$ (i) to treat the harness as a controllable design dimension and (ii) to support evaluation under task and tool environment shifts. Building on this, we systematically analyze how the harness design influences post-training in both in-distribution and out-of-distribution (OOD) settings. We empirically show that harness-aware post-training not only improves in-distribution performance but also enables agents to robustly adapt to OOD settings. Under a harness with minimal design effort, post-training suffers a drastic performance drop under stronger tool environment shifts, further highlighting the importance of harness-aware post-training under such shifts.

---


### 62. [Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473)

**<font color=#1a73e8>作者：</font>** Kaiwen Zheng, Guande He, Min Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion with causal diffusion transformers has emerged as a major paradigm for real-time streaming video generation and action-conditioned interactive world models. In this work, we extend rCM, an advanced diffusion distillation framework, to autoregressive video diffusion. The core philosophy of rCM lies in the complementarity between forward and reverse divergences, represented by consistency models (CMs) and distribution matching distillation (DMD), respectively, in diffusion distillation. This philosophy naturally carries over to the autoregressive setting, where teacher-forcing (TF) provides an offline, forward-divergence causal training paradigm, while self-forcing (SF) corresponds to an on-policy, reverse-divergence refinement.
Our contributions are: (1) through extensive experiments, we show that teacher-forcing CM is currently the best complement to self-forcing DMD as an initialization strategy (2) we present the first implementation of teacher-forcing-based continuous-time CMs (e.g., sCM/MeanFlow) for autoregressive video diffusion, enabled by our custom-mask FlashAttention-2 JVP kernel, achieving 10$\times$ faster convergence compared to discrete-time CMs (dCMs) (3) we introduce Causal-rCM, a leading, unified, and scalable algorithm-infrastructure open recipe for diffusion distillation and causal training (4) we achieve state-of-the-art streaming video generation performance in both frame-wise and chunk-wise settings, using only synthetic data for training.
Notably, our distilled 2-step causal Wan2.1-1.3B model achieves a VBench-T2V score of 84.63 with only 1 or 2 sampling steps. We further apply Causal-rCM to Cosmos 3, an advanced omnimodal world foundation model for physical AI with action-conditioned generation capability, enabling an interactive world model.

---


### 63. [A Red Teaming Framework for Large Language Models: A Case Study on Faithfulness Evaluation](https://arxiv.org/abs/2606.25476)

**<font color=#1a73e8>作者：</font>** Abrar Alotaibi, Raed Mughus, Moataz Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable performance across natural language processing tasks, yet their deployment in high-stakes applications raises critical concerns regarding reliability, safety, and trustworthiness. In this paper, we present a red teaming framework that systematically uncovers vulnerabilities in LLM outputs. Our approach employs a novel multi-role architecture comprising target, attacker, and jury models. The attackers generate increasingly effective adversarial prompts while the jury rigorously evaluates response accuracy and consistency across tasks. In a case study, our strategy proved particularly effective at exposing unfaithfulness in LLM responses. Exploitative adversarial prompts increased the attack success rate by up to 7.9% in question-answering tasks, revealing weaknesses in reliability. The approach identifies how structural constraints in summarization can shape vulnerability patterns, with format limitations yielding measurable gains in faithfulness, and shows that architectural design choices typically outweigh parameter scaling in determining model safety. The framework's key strength is its adaptability across evaluation tasks, from English question-answering to Arabic summarization, enabling comprehensive comparison of model vulnerabilities. While it excels at comparing cross-model and cross-linguistic vulnerabilities, it faces challenges in fully automating adversarial prompt generation across languages. Our experiments also reveal limitations in detecting subtle forms of unfaithfulness that do not manifest as explicit factual contradictions, particularly across linguistic contexts. Overall, this architecture provides both actionable insights into current LLM vulnerabilities and a scalable methodology for ongoing safety evaluation as models evolve.

---


### 64. [When LLM Rationales Become User-Facing: Effects on Trust Perception, Decision-Making, and Gaze Behaviors](https://arxiv.org/abs/2606.25489)

**<font color=#1a73e8>作者：</font>** Xin Sun, Ting Pan, Yajing Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly show step-by-step reasoning rationales alongside their answers, turning reasoning from an internal model capability into a user-facing interface feature. Yet it is unclear whether such rationales help users judge when trust is warranted or merely persuade through fluent reasoning. We address this gap through the lens of auditable trust calibration: user-facing rationales should help people inspect whether an answer is warranted by evidence. We test this framing in factual verification through two linked studies. Study 1, an online experiment (N=68), manipulated rationale presentation format (instant, delayed, on demand), rationale correctness (correct, incorrect), and certainty framing (none, certain, uncertain). Study 2, a controlled eye-tracking study (N=54), examined how no-, correct-, and incorrect-rationale conditions were associated with users' trust, decision-making, and eye-movement patterns. Study 1 showed no reliable presentation-format effects; instead, rationale correctness and certainty framing influenced the trust in the information, trust in the LLM system, and decision confidence. In Study 2, incorrect rationales drew more attention to the supporting evidence and larger pupil diameter while the rationale was viewed, consistent with greater cognitive effort. Incorrect rationales also lowered trust in LLM system relative to showing no rationale, whereas the no-rationale difference was weaker for trust in information. A post-hoc predictive modeling analysis of gaze data from Study 2 further showed that gaze features carried predictive signal for trust- and decision-related user states. This work challenges the assumption that more reasoning is always better and supports rationale designs that are selective, linked to evidence, calibrated in how they express certainty, and easier to verify.

---


### 65. [Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models](https://arxiv.org/abs/2606.25519)

**<font color=#1a73e8>作者：</font>** Xinyu Lian, Walid Krichene, Beichen Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantization is widely used to reduce the inference cost of large language models, but its effect on reasoning models is not fully captured by final-answer accuracy or per-token latency. We show that low-bit post-training quantization can introduce a hidden test-time compute cost: quantized reasoning models often generate longer chains of thought even when they still answer correctly. Across mathematical reasoning, code generation, scientific question answering, and agentic tool-use benchmarks, we find that INT4/INT3 quantization can preserve accuracy but increase reasoning-token usage, offsetting the expected per-token speedup. To measure this effect, we introduce the CoT Token Inflation Ratio, which compares reasoning length between quantized and full-precision models averaged across all evaluation benchmarks. We further show that token inflation is accompanied by behavioral changes in the reasoning trace, including more intermediate steps and greater semantic repetition. These changes translate into measurable end-to-end real-world serving penalties. Finally, we evaluate mitigation strategies and find that prompting and decoding-time sampling offer inconsistent accuracy-length trade-offs, while quantization-aware training shows more promise in reducing both accuracy degradation and token inflation. Our results suggest that reasoning-token usage should be reported alongside accuracy when evaluating quantized reasoning models.

---


### 66. [Cliff Tokens: Identifying Single-Token Failure Triggers in LLM Mathematical Reasoning](https://arxiv.org/abs/2606.25524)

**<font color=#1a73e8>作者：</font>** Jaeyong Ko, Pilsung Kang, Yukyung Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) reach high accuracy in mathematical reasoning, but individual traces on the same problem diverge; some arrive at the correct answer while others fail. Prior work analyzes failure at the step, chunk, or sentence level, or at tokens where failure has already occurred. Neither identifies the precise token that triggers the shift toward failure. We introduce the cliff token, a token where the token-wise potential drops significantly under an adaptive threshold that scales with the local token-wise potential, based on a one-sided two-proportion z-test. Across seven models and three mathematical reasoning benchmarks (GSM1K, MATH500, AIME 2025), cliff tokens act as failure triggers; deleting the first cliff token and resampling recovers pass@64 to 1.0, while keeping it limits recovery to between 0.71 and 1.00. We further introduce a cliff taxonomy of deterministic, uncertain, and sampled-off cliffs, defined by greedy choice and token entropy. Each type has distinct probabilistic characteristics, and the taxonomy generalizes across model scales. Finally, we validate the taxonomy via single-token preference optimization at cliff positions (Cliff-DPO). Trained on GSM8K, Cliff-DPO improves accuracy across benchmarks by up to +6.6. Optimizing at uncertain and sampled-off cliffs improves reasoning, while deterministic cliffs do not.

---


### 67. [Beyond One-Size-Fits-All: Diagnosis-Driven Online Reinforcement Learning with Offline Priors](https://arxiv.org/abs/2606.25527)

**<font color=#1a73e8>作者：</font>** Guozheng Ma, Lu Li, Zilin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning (RL) agents increasingly depend on knowledge acquired offline to achieve practical efficiency. Originally studied in offline-to-online RL, this paradigm now spans foundation model post-training and embodied intelligence, with prior types expanding from offline datasets and pre-trained policies to increasingly diverse knowledge sources such as multimodal foundation models and generative world models. Offline priors have become central to how deep RL is developed and deployed. However, this reliance introduces a challenge that the prevailing benchmark-driven paradigm cannot resolve: because prior validity varies across deployments and shifts during training, no single approach to managing it is universally optimal, and benchmark rankings offer limited guidance for real-world deployments. Rather than pursuing universal solutions, we argue that the field should shift to diagnosis-driven tension management, in which deployment-specific evidence guides how the learner relates to its priors throughout training, enabling both flexible and adaptive deployment. We support this position with a framework characterizing how priors reshape online optimization through three functional roles, controlled experiments demonstrating help-or-hurt reversals, cross-domain evidence from foundation model post-training to embodied intelligence, and engagement with five substantive counterarguments.

---


### 68. [Agentic evolution of physically constrained foundation models](https://arxiv.org/abs/2606.25532)

**<font color=#1a73e8>作者：</font>** Jiangwei Zhang, Wen Sun, Chong Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence increasingly drives automated scientific discovery, yet contemporary generalist agents lack physical grounding, frequently hallucinating hardware-incompatible designs. Here, we present a physically grounded, multi-agent discovery engine that autonomously architects hardware-compliant computing systems. Anchored by an Evolutionary Knowledge Graph structuring past scientific innovations, the framework extracts an "algorithmic Chain-of-Thought" to transform blind stochastic search into directed structural evolution. Applied to the extreme testbed of foundation model deployment, the engine evolved two hardware-aware compression methodologies surpassing human-engineered heuristics: Q-Enhance mitigates long-context accuracy loss in dense models, and MoE-Salient-AQ outperforms state-of-the-art manual sparse Mixture-of-Experts designs by 3.7% at sub-3-bit regimes. Utilizing a bandwidth-efficient Sensitivity Profile, we successfully deployed a massive 235-billion-parameter model onto a constrained dual-A100 server, reducing memory requirements by 75% with a marginal 0.64% accuracy degradation. By transforming unconstrained combinatorial search into knowledge-driven autonomy, this establishes a scalable hardware-software co-design paradigm for machine-driven discovery within strict physical boundaries.

---


### 69. [SAC$^2$-Net: Semantic Anchoring and Complementary-Consensus Fusion for Multimodal Micro-Expression Recognition](https://arxiv.org/abs/2606.25542)

**<font color=#1a73e8>作者：</font>** Xuepeng Zheng, Tong Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-expression recognition (MER) is challenging due to subtle facial movements, limited data, and the ambiguous relationship between Action Units (AUs) and emotion categories. Optical flow and motion magnification have been widely used to describe subtle facial dynamics from different perspectives: the former captures local motion displacement, while the latter amplifies weak appearance changes. In this work, we observe that these two modalities often exhibit asymmetric failure patterns: one modality may become noisy, distorted, or uninformative, while the other still preserves discriminative AU-related evidence. This phenomenon reveals their complementarity, but also raises two key challenges for fusion: cross-modal heterogeneity and spatially varying modality reliability. Motivated by this observation, we propose SAC$^2$-Net, a Semantic Anchoring and Complementary-Consensus Network for multimodal MER, which first aligns visual modalities with semantic anchors and then performs reliability-aware fusion. To reduce cross-modal heterogeneity before fusion, we introduce Semantic Anchoring Soft Alignment (SASA), which converts activated AUs into textual prompts and uses them as stable semantic anchors to align motion-magnified and optical-flow representations. Unlike hard contrastive learning, SASA constructs hierarchical AU-aware soft labels to preserve semantic proximity among samples with overlapping or anatomically related AU patterns. Based on the aligned representations, Complementary-Consensus Fusion (CCF) first repairs unreliable local evidence through complementary exchange and then enforces a shared spatial focus through consensus refinement. Extensive experiments on five MER benchmarks show that SAC$^2$-Net achieves state-of-the-art or highly competitive performance across coarse-grained, fine-grained, large-scale, and cross-dataset evaluation settings.

---


### 70. [SFL-MTSC: Leveraging Semantic Frame-Level Multi-Task Self-Consistency for Robust Multi-Intent Spoken Language Understanding](https://arxiv.org/abs/2606.25552)

**<font color=#1a73e8>作者：</font>** Po-Yen Chen, Berlin Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt-based spoken language understanding (SLU) with large language models (LLMs) often suffers from inconsistent intent--slot structures due to decoding stochasticity, particularly in multi-intent scenarios. In view of this, we propose Semantic Frame-Level Multi-Task Self-Consistency (SFL-MTSC), a novel structured aggregation framework operating at the semantic frame level. Instead of output-level majority voting, SFL-MTSC decomposes predictions into intent-specific frames, applies domain--intent grouping and slot-level clustering, and evaluates cluster reliability using path support scoring. Reliable frames are retained and re-integrated to form the final prediction. Zero-shot experiments on the MAC-SLU benchmark dataset show improved slot F1 and overall accuracy over single-path inference, while intent accuracy remains largely stable across most settings.

---


### 71. [BiPACE: Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation for LLM Agents](https://arxiv.org/abs/2606.25556)

**<font color=#1a73e8>作者：</font>** Hanyang Wang, Weijieying Ren, Yuxiang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stepwise group-based RL is an attractive way to train long-horizon LLM agents without a learned critic: it reuses multiple sampled rollouts to estimate local advantages. Its weakness is less visible but more fundamental: every group-relative estimator assumes that the steps it compares are equivalent for credit assignment. We show that current agentic variants violate this assumption through a state-action credit mismatch. The observation-hash partition is overly fine on the state side, creating singleton groups with zero step-level signal, while a single within-group mean is too coarse on the action side, mixing state-value estimation with action-specific credit. We introduce BiPACE (Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation), a drop-in advantage estimator that fixes both sides without adding a critic, auxiliary loss, or extra rollouts. BiGPO clusters steps by cosine distance in the actor's own hidden-state geometry, an empirical policy-induced proxy for bisimulation that substantially lowers the singleton rate left by observation hashing. PACE then recenters returns within each behavioral cluster using action-conditioned peer baselines; its Q-style instance estimates a local Q(s,a)-V(s) nonparametrically. On ALFWorld/Qwen2.5-7B, BiPACE_Q raises overall validation success from GiGPO's 90.8 to $97.1\pm0.9$ over three seeds, and crosses the 95% threshold on every seed, which GiGPO never does within the same budget. On Qwen2.5-1.5B it reaches $93.5\pm1.2$ versus GiGPO's 86.7, and on WebShop and TextCraft it improves over GRPO and GiGPO at both model scales. The measured BiPACE-specific overhead is 11.3% of a single training-step wall time. Yet it changes the estimator's comparison unit from surface identity to approximate behavioral equivalence plus action-side counterfactuals. The code is available at this https URL.

---


### 72. [Riazi-8B: An Urdu Large Language Model for Mathematical Reasoning](https://arxiv.org/abs/2606.25568)

**<font color=#1a73e8>作者：</font>** Azher Ali, Ibtsam Haider, Raja Khurram Shahzad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent LLMs demonstrate strong mathematical reasoning capabilities, but existing gains rely heavily on English-centric training resources and benchmarks. As a result, reasoning performance degrades substantially in low-resource languages such as Urdu, where reasoning-oriented datasets and adapted models remain scarce. Urdu lacks both reasoning-oriented resources and models adapted for multi-step mathematical problem solving, limiting the applicability of recent progress to Urdu-speaking users. We address this gap through Riazi-8B, an Urdu mathematical reasoning model developed through a two-step adaptation process comprising continued pre-training on Urdu Wikipedia and supervised fine-tuning on Urdu Chain-of-Thought data derived from GSM8K. We evaluate Riazi-8B on MGSM-Urdu against existing Urdu instruction-tuned models. Our results show consistent improvements in answer correctness, reasoning quality, response completeness, and Urdu generation. Our findings demonstrate that combining Urdu language adaptation with reasoning-focused fine-tuning is an effective strategy for extending mathematical reasoning capabilities to low-resource languages.

---


### 73. [Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints](https://arxiv.org/abs/2606.25605)

**<font color=#1a73e8>作者：</font>** Fangzheng Li, Aimin Zhang, Chen Lv  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool Calling and Structured Output are two core capabilities of modern Agent systems, yet their interaction under joint deployment conditions remains insufficiently understood. This paper reports a reproducible phenomenon observed in a production Agent system: when Tool Calling and JSON Schema constraints are simultaneously enabled, multiple open-weight models cease invoking tools despite maintaining high schema compliance. We refer to this behavior as Tool Suppression. Through controlled experiments across multiple model families and deployment settings, we consistently reproduce Tool Suppression under joint constraints, while tool execution and schema compliance remain functional when evaluated independently. Further analysis reveals that JSON Schema constraints are compiled into grammar-based token masks, causing tool-call tokens to become unreachable during decoding. This provides an implementation-level explanation for the observed behavior. To interpret the phenomenon, we formulate the Constraint Priority Inversion (CPI) hypothesis, which suggests that schema satisfaction may dominate action-selection behavior under multiple simultaneous constraints. We present CPI as a behavioral hypothesis consistent with the observed evidence rather than a verified internal mechanism. To mitigate the problem, we propose Transparent Two-Pass Execution, an inference-time strategy that decouples tool execution from schema-constrained response generation. Experimental results show that this approach restores tool invocation while preserving structured output guarantees without requiring model retraining. These findings suggest that evaluating tool use and structured output separately may overlook important reliability issues in production Agent systems. Code, data, and docs will be released at this https URL.

---


### 74. [SSMNBench: Diagnosing Image-based Cross-View Human-Object Understanding via Single-View Sufficiency and Multi-View Necessity](https://arxiv.org/abs/2606.25634)

**<font color=#1a73e8>作者：</font>** Tianchen Guo, Chen Liu, Ling Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown remarkable progress in single-image perception, yet their ability to reason about complex cross-view human-centric scenes remains largely unverified. Current multi-view benchmarks evaluate models using a fixed "bag of frames" and thus conflate a model's robustness to visual distraction with its genuine ability to fuse fragmented cross-view evidence. To address this issue, we introduce SSMNBench, a diagnostic benchmark comprising 3,300 curated QA pairs for cross-view human and human-object understanding. SSMNBench uniquely categorizes tasks into Single-View Sufficiency (SVS) and Multi-View Necessity (MVN). By systematically perturbing view availability across 17 state-of-the-art MLLMs, critical limitations are revealed: models suffer from severe "distraction degradation" when presented with redundant views (SVS), and fail to integrate fragmented geometric evidence across cameras (MVN). Our evaluations demonstrate that modern MLLMs rely on multiple single-image semantic averaging and view preference rather than genuine cross-view synthesis. By exposing these fundamental vulnerabilities, SSMNBench provides a rigorous diagnostic framework to drive the advancement of future cross-view-aware multimodal architectures. The code is available at: $ \href{this https URL}{\text{SSMNBench}} $

---


### 75. [MedGuards: Multi-Agent System for Reliable Medical Error Detection and Correction](https://arxiv.org/abs/2606.25651)

**<font color=#1a73e8>作者：</font>** Congbo Ma, Hu Wang, Yichun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly deployed in healthcare settings, accurate error detection and correction in generated or existing text becomes critical, as even minor mistakes can pose risks to patient safety. Existing methods for error detection and correction, including automated checks and heuristic-based approaches, do not generalize well across unseen datasets. In this paper, we propose MedGuards as a medical safety guardrail, which is a new framework that treats medical error detection and correction as a multi-agent in-context learning task. Specialized agents separately detect, localize, and correct errors, while a confidence-guided arbitration mechanism resolves disagreements using reasoning traces and confidence scores. This design enhances interpretability, robustness, and adaptability, without requiring additional training of the base LLMs. Additionally, we introduce the Keyword-Prioritized Correction Score (KPCS), a new evaluation metric that considers whether critical keywords within the reference text are generated correctly, providing a more comprehensive assessment than conventional metrics. Experiments across four multilingual medical datasets consisting of clinical notes demonstrate significant improvements by the proposed framework across several metrics and models. Our aim is to enable safer deployment of LLMs in real-world healthcare applications. For reproducibility, we make our code publicly available at this https URL.

---


### 76. [Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization](https://arxiv.org/abs/2606.25656)

**<font color=#1a73e8>作者：</font>** Long Chen, Ryan Razkenari, Yuxuan Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As advanced RAG variants like GraphRAG and Agentic RAG emerge, one leading question is when and how to use them. Here, we introduce a framework for different RAG scenarios evaluation and comparison on semi-structured knowledge bases, including regular RAG, GraphRAG, Modular RAG and Agentic RAG. We provide implementation for 9 standardized RAG scenarios, and conduct experiments for a comprehensive comparison. These scenarios are designed for real use cases regarding data and domain restrictions, spanning from simple document-based retrieval to advanced features such as hybrid text-graph retrieval, integration with computed or pre-defined domain knowledge graphs, agentic multi-step planning, and agent-graph integration. Besides, we present a novel context engineering method for GraphRAG and Agentic RAG, addressing the context/memory overflow issues, efficiently managing text and graph retrievals with new representations and agentic loop design, leading to 19%-53% reduction on token usage. Moreover, further analysis identifies a retrieval-generation gap where expanded retrieval does not proportionally improve generation quality, suggesting retrieval-oriented metrics overstate advanced retrieval benefits. This work provides data-driven insights on when and how to use them for building production-ready intelligent RAG systems.

---


### 77. [Steering Vision-Language Models with Joint Sparse Autoencoders](https://arxiv.org/abs/2606.25657)

**<font color=#1a73e8>作者：</font>** Huizhen Shu, Xuying Li, Hongxu Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse Autoencoders (SAEs) have shown promise for analyzing language models, but applying them to vision-language models (VLMs) often yields representations that are difficult to use as controllable cross-modal steering directions. We introduce the Joint Sparse Autoencoder (JSAE), which uses an explicit alignment constraint to jointly factorize sequence-pooled vision and language activations into shared, interpretable image/caption-level features. Applied to LLaVA, JSAE recovers cross-modal features for recognizable concepts (e.g., food and animals). Through bidirectional interventions (additive steering and suppression), we observe a layer-dependent asymmetry under our protocol: additive steering peaks at mid-to-late (pre-output) layers and weakens at both ends, whereas suppression scores remain within a comparable range across all probed layers within statistical noise. Experiments on three VLMs, namely LLaVA-v1.6-Mistral-7B, Llama3-LLaVA-8B, and the MoE-based Qwen3-VL-30B, show related layer-localized effects across architectures. Together, these results suggest that explicitly aligned sparse representations support more controllable intervention-based analysis of multimodal features, within an identifiable layer range, than the unconstrained alternatives tested here.

---


### 78. [Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding](https://arxiv.org/abs/2606.25658)

**<font color=#1a73e8>作者：</font>** Baiyang Song, Yuli Lin, Qiong Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Currently, streaming video understanding is still a daunting task for existing \emph{multimodal large language models} (MLLMs). Its difficulties not only lie in handling the ever-increasing video frames, but also in the unpredictability of future video content and input instructions. In this paper, we study this task from the perspective of constructing a dynamic but fixed-budget memory bank, and propose a novel and training-free approach termed \emph{\textbf{CausalMem}}. CausalMem is dedicated to constructing a dynamic visual memory update mechanism, thereby maximizing the amount of information in streaming video within a limited memory space, much like the human brain. In practice, CausalMem estimates the redundancy of visual tokens and updates the memory bank via an online semantic basis, which models the principal semantics of the observed video stream. To validate CausalMem, we apply it to two representative MLLMs, namely LLaVA-OneVision and Qwen2.5-VL respectively, and conduct extensive experiments on both streaming and offline video understanding benchmarks. The experimental results not only show the great advantages than existing methods under both streaming and offline settings, \emph{e.g.}, $+3.2\%$ and $+3.0\%$ average accuracy gains respectively, but also witness the superior semantic preservation for streaming videos, \emph{e.g.}, using 12$k$ token budgets to memorize hour-long streaming videos, which achieves more than \textbf{20$\times$} visual token compression ratio and only occupies about \textbf{82 MB} storage. \textbf{Our code} is given in \href{this https URL}{CausalMem}.

---


### 79. [BitNet Text Embeddings](https://arxiv.org/abs/2606.25674)

**<font color=#1a73e8>作者：</font>** Zhen Li, Xin Huang, Liang Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based text embedders have substantially improved retrieval and semantic representation quality, but their deployment remains costly: large backbone models slow down embedding inference, while high-dimensional full-precision embeddings impose substantial storage and bandwidth overhead on large-scale indexes. In this paper, we present BITEMBED, an extreme low-bit framework for LLM-based text embedding that jointly targets encoding efficiency and vector storage. BITEMBED converts pretrained LLM backbones into BitNet-style embedding encoders with ternary weights, quantized activations, and lightweight normalization refinement. The converted model is adapted to representation learning through continual contrastive pre-training, followed by supervised contrastive fine-tuning with both similarity-distribution distillation and attention-relation distillation from a full-precision teacher. Beyond quantizing the backbone, BITEMBED further trains output embeddings to support multiple storage precisions meeting different storage needs in various scenarios. Experiments on MMTEB (eng, v2) with Qwen3-0.6B and Gemma3-270M show that BITEMBED is largely comparable to full precision teacher embedders. Moreover, BITEMBED flexibly obtains text embeddings of various precisions, achieving a trade-off between performance and storage cost.

---


### 80. [Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning](https://arxiv.org/abs/2606.25700)

**<font color=#1a73e8>作者：</font>** Samuel Valland Lyngset, Tor Viljen Raanaas, Gard Sveipe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When fine-tuning Large Language Models (LLMs), there has been success in minimizing both memory usage and computation with Parameter-Efficient Fine-Tuning (PEFT), like Low Rank Adaptation (LoRA). In this article, we have explored whether this approach is transferable to the world of robotics and Reinforcement Learning (RL), allowing learning with reduced memory usage and improved computational performance. Specifically, we focused on a version of multi-task robotics, where a library of specialist policies are created. In such a library memory efficiency is especially important. We used a Proximal Policy Optimization (PPO) algorithm and fine-tuned a baseline model to different tasks using LoRA. Our results demonstrate that, depending on the hyperparameters, LoRA can minimize memory usage by a factor of 20-160 compared to full fine-tuning of all layers. This implies a 90-95% storage saving when deploying a library of many (10-50) specialized policies, which can be the differentiating factor between being able to store the entire library in memory or having to use swap-memory in an applied robotics setting. At the same time, our results indicate that there is no significant difference in the success-rate between full fine-tuning and LoRA fine-tuning for the selected tasks.

---


### 81. [Falcon: Functional Assembly and Language for Compositional Reasoning in X-ray](https://arxiv.org/abs/2606.25701)

**<font color=#1a73e8>作者：</font>** Yonathan Michael, Mohamad Alansari, Natnael Takele 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional vision-language models are largely object-centric, focusing on detecting and describing individual entities. In safety-critical X-ray baggage screening, however, threat often emerges not from a single object but from the functional compatibility of spatially dispersed components, such as batteries, detonators, and explosive charges. We formalize this setting as \emph{compositional threat reasoning}, where risk is modeled as a relational property of grounded regions rather than an independent detection outcome. We introduce \textbf{Falcon}, a multimodal framework that abstracts segmentation-aware region features into a structured safety state capturing component presence, pairwise functional compatibility, and scene-level risk. This structured representation is injected into the language model as an explicit intermediate interface, encouraging relationally consistent and safety-aware reasoning. To evaluate this problem, we present \textbf{Falcon-X}, a benchmark that unifies dense grounding with structured supervision over component completeness and risk inference in cluttered X-ray imagery. Experiments show that while existing multimodal models adapt to appearance, they struggle with compositional safety reasoning. Falcon improves functional grounding and produces more coherent threat assessments, establishing compositional safety reasoning as a distinct evaluation paradigm for multimodal systems.

---


### 82. [What Does the Brain See? Multiview Neural Representations to Demystify the Brain-Visual Alignment](https://arxiv.org/abs/2606.25718)

**<font color=#1a73e8>作者：</font>** Salini Yadav, Taveena Lotey, Pravendra Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot visual decoding from electroencephalography (EEG) aims to infer visual semantics from non-invasive neural recordings, but remains challenging due to the low signal-to-noise ratio, non-stationarity, and limited spatial resolution of EEG. Existing EEG-vision alignment methods often rely on holistic EEG embeddings, which can obscure the complementary temporal, spectral, and spatial structure underlying visual perception. We introduce a unified multiview EEG representation learning framework for aligning brain responses with visual semantic embeddings. Our method builds an EEG encoder that jointly models three complementary views: input-conditioned state-space temporal dynamics, learnable wavelet-based spectral decomposition for sample-adaptive frequency modeling, and attention-modulated graph learning for structured electrode interactions. The resulting multiview EEG embeddings are fused and aligned with pretrained visual representations in a shared semantic space using contrastive learning with EEG-specific regularization, enabling 200-way zero-shot visual classification. Experiments on THINGS-EEG benchmark show that our method achieves state-of-the-art performance, with 54.8% Top-1 and 85.6% Top-5 accuracy in the within-subject setting and 15.3% Top-1 and 45.4% Top-5 accuracy in the cross-subject setting. We further present the first systematic cross-session EEG-image decoding evaluation, achieving 40.8% Top-1 and 78.0% Top-5 accuracy. These results suggest that explicitly modeling multiview neural structure improves both semantic alignment and generalization in EEG-based visual decoding.

---


### 83. [OPERA: Aligning Open-Ended Reasoning via Objective Perplexity-based Reinforcement Learning](https://arxiv.org/abs/2606.25757)

**<font color=#1a73e8>作者：</font>** Wenxuan Jiang, Zining Fan, Zijian Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has enabled LLMs to excel in objective reasoning tasks such as mathematics and code generation. However, applying RL to open-ended tasks, such as creative writing, remains challenging because LLM-as-a-judge reward models often exhibit stylistic biases and positional inconsistencies, leading to unstable supervision. To address this, we propose OPERA (Objective Perplexity-based Reflective Alignment), which replaces unreliable external judges with intrinsic rewards derived from perplexity dynamics. Specifically, we derive an intrinsic reward signal from perplexity dynamics, quantifying uncertainty reduction at critical reflective states. During the cold-start phase, we introduce a data synthesis method that leverages carefully designed guiding words to generate diverse reasoning traces, along with perplexity-prioritized rollouts that utilize internal log-probabilities to identify logically consistent reasoning branches. This pipeline yields a large-scale dataset comprising 20,000 high-quality reasoning trajectories. Empirical evaluations consistently demonstrate the scalability and efficacy of our approach in alignment for open-ended tasks. Implementing OPERA on Qwen3-8B establishes a new state-of-the-art among open-source models, achieving parity with or surpassing proprietary models like Gemini2.5 and MiniMax-M2.5 in some open-ended tasks. The code is available at this https URL.

---


### 84. [Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets](https://arxiv.org/abs/2606.25760)

**<font color=#1a73e8>作者：</font>** Divake Kumar, Sina Tayebati, Devashri Naik 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computer-use agents turn vision-language model (VLM) predictions into executable GUI clicks, so reliable uncertainty estimates are essential for rejection, calibration, miss-severity ranking, and spatial safety regions. Yet evidence on post-hoc uncertainty quantification (UQ) for these agents is fragmented across isolated model and dataset pairs, leaving it unclear whether UQ rankings stay stable when the agent, benchmark, or observable interface changes. We present Argus, a cross-regime benchmark for post-hoc UQ in single-step executable GUI grounding: a 27-method open-weight matrix over 4 VLM agents and 4 datasets, plus an 8-method closed-source matrix across 3 frontier vendors where logits, hidden states, and attention maps are unavailable. Evaluated methods span logit-based scores, sampling and consistency measures, hidden-state and density estimators (Mahalanobis, SAPLMA), attention-based scores, P(True) and verbalised-confidence prompting, and split-conformal prediction. The main finding is selective transfer: UQ rankings are stable across datasets for a fixed model, but degrade across model classes and observable interfaces. Hidden-state and density methods are the most stable open-weight family, while CoCoA-1MCA, Focus, sampling-based scores, and verbalised self-assessment win in specific regimes. Within-model ranking transfer is strong (Spearman rho up to 0.969), but cross-tier transfer to closed-source vendors averages only +0.08, so closed-source UQ should be reranked on the target rather than extrapolated. Conformal click regions show score-level discrimination is not enough for deployment: locally weighted disks shrink radii by 40-60% when the plug-in UQ is calibrated, but coverage degrades under calibration-test or interface mismatch. We release per-item records, calibration/test splits, UQ scores, and analysis scripts for regime-aware UQ selection in GUI agents.

---


### 85. [ShutterMuse: Capture-Time Photography Guidance with MLLMs](https://arxiv.org/abs/2606.25763)

**<font color=#1a73e8>作者：</font>** Jiayu Li, Yixiao Fang, Tianyu Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world photography requires capture-time guidance for both camera framing and subject pose. Yet existing aesthetic cropping benchmarks mainly evaluate post-hoc crop prediction and overlook subject-side recommendations, leaving the capture-time guidance capabilities of multimodal large language models (MLLMs) underexplored. To address this gap, we introduce CaptureGuide-Bench, a benchmark with two complementary tasks: photographer-side composition decision and refinement, and subject-side scene-conditioned pose recommendation. Our evaluation reveals limitations: general-purpose MLLMs can make composition decisions but lack precise refinement localization, while specialized aesthetic cropping models localize crops effectively but are limited to refinement; neither provides actionable pose guidance. To support model development, we further construct CaptureGuide-Dataset, comprising 130K samples with textual rationales and structured visual annotations, and develop ShutterMuse, a unified MLLM trained with supervised and reinforcement fine-tuning. Experiments on CaptureGuide-Bench show that ShutterMuse achieves the best overall photographer-side performance among evaluated baselines and competitive subject-side pose recommendation with substantially lower inference cost, demonstrating the potential of MLLMs as interactive assistants for photography during image capture.

---


### 86. [Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation](https://arxiv.org/abs/2606.25782)

**<font color=#1a73e8>作者：</font>** Han Jeon, Shiv Medler, Joseph Voyles 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the widespread adoption of large language models (LLMs) in chatbots and everyday applications, companies increasingly need guardrails that are effective while remaining low-cost and low-latency. Safety evaluation of LLM outputs has generally relied on LLM-based judges, which can be effective but are often slow and expensive to deploy at scale.
In this paper, we evaluate whether fine-tuned modern encoder classifiers from the ModernBERT family, including ModernBERT and Ettin, can reliably identify harmful LLM outputs in user-model conversations without substantial performance loss relative to LLM-based judges. We benchmark these encoder classifiers against rule-based prefix matching, fine-tuned LLM classifiers, and LLM judges using a range of judge-prompting strategies across open-source adversarial datasets.
The LLM judges include evaluation methodologies from StrongReject, ShieldGemma, JailbreakBench, AILuminate, SorryBench, and a Claude-as-a-judge setup, as well as fine-tuned safety classifiers such as LlamaGuard 3 and LlamaGuard 4. The encoder classifiers are fine-tuned on judge-labeled data using a majority-voting label strategy and are then evaluated on a gold-standard holdout dataset to assess their performance relative to LLM judges.
We report absolute performance using F1 score, false negative rate, and precision-recall metrics. We also break down results by attack technique, including single-turn prompting, decomposition, escalation, and context manipulation, to identify where encoder classifiers align with or diverge from LLM-based judges. Our findings provide guidance on when encoder classifiers can serve as cost- and latency-efficient alternatives to LLM-based safety evaluation.

---


### 87. [Designing Trustworthy LLM-based Wellbeing Recommendation through Controllable Interaction](https://arxiv.org/abs/2606.25809)

**<font color=#1a73e8>作者：</font>** Alan Said, Alexandra Weilenmann  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate personalized guidance in wellbeing contexts such as physical activity, stress management, and mental health support, enabling fluent and context-aware interaction but relying on largely implicit mechanisms that shape how recommendations are expressed and adapted. We argue that this reliance on implicit adaptation through prompting and alignment limits control over guidance, responsibility framing, and user influence, which is particularly problematic in wellbeing settings where recommendations affect users' actions and long-term outcomes. We propose a system-level perspective in which conversational behavior is structured through explicit interaction constraints, including guidance strategies, explanation styles, degrees of directness, and mechanisms for user control. Building on prior work on tangible recommendations, we show how these constraints address key challenges in wellbeing-oriented recommendation, namely trust calibration, intent alignment, and consequence awareness. We outline a modular architecture for controllable LLM-based recommendation and discuss how different configurations can be systematically designed and evaluated in relation to user-centered outcomes such as self-efficacy, perceived agency, and appropriate reliance. This paper contributes a system-level framework for designing LLM-based recommender systems that are adaptive while remaining transparent, controllable, and aligned with human wellbeing.

---


### 88. [Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability](https://arxiv.org/abs/2606.25819)

**<font color=#1a73e8>作者：</font>** Yang Tian, Zhengpeng Shi, Bo Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as agents that solve tasks by interacting with external tool environments. Although recent tool-use benchmarks increasingly cover complex task settings, they still largely assume clean, stable, and trustworthy tool environments, leaving tool-environment unreliability insufficiently examined. We introduce ToolBench-X, a benchmark for evaluating agents under recoverable reliability hazards. ToolBench-X contains executable multi-step tasks across diverse domains and sequential, parallel, and mixed workflows, each paired with deterministic tools and a canonical final answer for automatic evaluation. Starting from clean tool environments, ToolBench-X injects five structured hazard types: Specification Drift, Invocation Error, Execution Failure, Output Drift, and Cross-source Conflict. Crucially, each injected instance remains solvable through at least one valid recovery path, such as retrying, fallback, verification, or cross-checking. Experiments reveal a substantial reliability gap: agents that perform well with reliable tools often fail under recoverable hazards. Further analysis shows that failures are driven less by tool-use volume or inference budget than by limited hazard diagnosis and ineffective recovery. Targeted recovery hints recover many failed tasks, while test-time scaling yields more limited gains. These results suggest that tool-use evaluation should move beyond function-call accuracy toward task completion under unreliable tool environments. The code and data is available at this https URL.

---


### 89. [SARA: Unlocking Multilingual Knowledge in Mixture-of-Experts via Semantically Anchored Routing Alignment](https://arxiv.org/abs/2606.25821)

**<font color=#1a73e8>作者：</font>** Tianyu Dong, Yangyang Liu, Jiang Zhou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) architectures have emerged as an increasingly influential paradigm as they offer a strategic balance between parameter scalability and computational efficiency. However, low-resource languages, which suffer from a scarcity of high-quality training data, often have their tokens routed to different experts than those predominantly activated by high-resource inputs, which limits cross-lingual expert sharing. This cross-lingual routing divergence consequently hinders their efficacy in multilingual contexts. To address this issue, we propose SARA (Semantically Anchored Routing Alignment), a framework designed to transfer specialized capabilities from high-resource languages as anchors to low-resource languages. SARA explicitly aligns the routing distribution of multilingual inputs with high-resource semantic anchors using a symmetric Jensen-Shannon (JS) divergence constraint. Unlike traditional distillation methods that operate on output logits, SARA directly aligns the internal routing distributions of MoE layers, encouraging mechanistic consistency in expert selection across languages. We conduct experiments on 2 LLMs across 5 low-resource languages and 3 benchmarks. Experiment results demonstrate that SARA outperforms standard instruction tuning, e.g., +0.8% on Qwen3-30B-A3B and +1.2% on Phi-3.5-MoE-instruct on Global-MMLU. Further analyses show that SARA effectively addresses performance bottlenecks in low-resource languages, providing a scalable pathway to enhance multilingual capabilities in sparse architectures.

---


### 90. [MiniOpt: Reasoning to Model and Solve General Optimization Problems with Limited Resources](https://arxiv.org/abs/2606.25832)

**<font color=#1a73e8>作者：</font>** Ke Zhao, Zixiang Di, Hong Qian 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Achieving strong optimization generalization across diverse optimization problems while requiring limited training resources remains a challenging problem for optimization-oriented large language models (LLMs). Existing approaches typically rely on large-scale supervised datasets, costly reasoning annotations, and expensive intermediate step verification, resulting in substantial training overhead. To address these challenges, we propose MiniOpt, a reinforcement learning framework that learns to solve optimization problems through an "reasoning-to-model-and-solve" paradigm. MiniOpt decomposes optimization reasoning into structured optimization modeling and executable solver generation. Building upon this paradigm, we introduce OptReward, a reward function with hierarchical score structure that jointly evaluates formulation and solution, enabling effective policy learning without expert demonstrations. We further develop an optimization-oriented policy optimization strategy that improves exploration efficiency and stabilizes reinforcement learning for compact models. Extensive experiments show that MiniOpt-3B exhibits strong optimization generalization across various optimization types, problem scenarios, and task domains. For models with fewer than 10B parameters, MiniOpt series achieves the highest average solving accuracy (SA). For models with more than 10B parameters, MiniOpt still shows competitive performance. These results suggest that optimization-oriented reward design and reinforcement learning provide an effective pathway for developing compact optimization-specialized language models with strong optimization generalization capabilities. The code is available at this https URL.

---


### 91. [AI Snitches Get Glitches: Towards Evading Agentic Surveillance](https://arxiv.org/abs/2606.25836)

**<font color=#1a73e8>作者：</font>** Hyejun Jeong, Dzung Pham, Amir Houmansadr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To better assist users with completing challenging tasks, AI agents mediate communications, access data, and interact with different APIs. Many employers (and even nation-states) already provide their users with this technology. However, widespread adoption of AI agents creates a new risk to abuse access to user data for another goal: surveilling users. These users might not even have the ability or permission to control the actions and data accesses of the surveilling agents.
We introduce and formalize the problem of agentic surveillance: the ability of an AI agent to analyze available information, craft a report, and send it out using available tools. To evaluate surveillance capabilities across different models, we create SurveilBench, a dataset of various reporting scenarios focusing on three domains: corporate, education, and police. We find that some models exhibit emergent (i.e., unprompted) tendencies to help surveillance, but they also report the attempts to surveil users to the government.
Finally, we repurpose prompt injections for evading surveillance and develop three evasion techniques that hide from, deceive, or induce over-escalation in surveillance agents. We conclude that agentic surveillance can already be easily implemented and, therefore, call for a comprehensive technical, ethical, and legislative framework to protect users.

---


### 92. [Graph it first! Enabling Reasoning on Long-form Egocentric Videos through Scene Graphs](https://arxiv.org/abs/2606.25842)

**<font color=#1a73e8>作者：</font>** Agnese Taluzzi, Riccardo Santambrogio, Simone Mentasti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing multi-modal large language models (MLLMs) face significant challenges in processing long video sequences due to strict input token limitations. As a result, current video understanding approaches, especially in egocentric settings characterized by complex dynamics, frequent state changes, and moving cameras, are forced to massively subsample frames. This leads to severe loss of temporal and contextual information, constraining their ability to perform fine-grained video reasoning. In this work, we introduce a framework for egocentric video question answering (VQA) that overcomes these input constraints through Egocentric Scene Graphs (EgoSGs), i.e., temporally grounded, structured representations that capture objects, attributes, spatial relations, and interactions over time. By representing videos as compact, text-based scene graphs, our method preserves the essential visual and temporal information of the original video in a symbolic form that drastically reduces input length while maintaining semantic richness. Crucially, this enables MLLMs to reason efficiently over entire video sequences within their token budget. On HD-EPIC VQA, our method achieves state-of-the-art results, outperforming strong video-based baselines on multiple models and suggesting that structured, temporally grounded representations like EgoSGs can bridge long-form egocentric video understanding and the context limitations of today's MLLMs.

---


### 93. [Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents](https://arxiv.org/abs/2606.25852)

**<font color=#1a73e8>作者：</font>** Peng Xu, Sijia Chen, Junzhuo Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on whether their trajectory eventually succeeded or failed. Such semantic credit inconsistency sends conflicting gradients to similar actions and wastes the partially-correct progress inside failed rollouts. Motivated by this, we propose Semantic Consistency Policy Optimization (SCPO), a value-free reward-shaping method that mitigates this inconsistency by recovering step-level credit from successful siblings in the same rollout group. Concretely, SCPO scores each failed step against a successful sibling and adds positive step-level credit for new progress along that sibling. On ALFWorld and WebShop, SCPO matches or exceeds strong group-based baselines, reaching 93.7+/-4.1 percent success on ALFWorld and 74.8+/-2.0 percent on WebShop at 1.5B parameters, with gains concentrated on the hardest multi-step tasks.

---


### 94. [USS: Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning](https://arxiv.org/abs/2606.25880)

**<font color=#1a73e8>作者：</font>** Yuchen Xie, Xinyu Zhou, Kuangji Zuo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied Visual Tracking (EVT) requires an agent to continuously follow a specified target while actively moving through dynamic environments. However, prevailing EVT paradigms predominantly rely on language-based target indication. While language is expressive and convenient, cluttered scenes often contain multiple objects that satisfy the same semantic description, leading to ambiguous target grounding. We therefore propose a paradigm shift, reframing target indication in EVT from text-only specification to unified spatial-semantic prompting. Based on this paradigm, we introduce Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning, USS, an end-to-end embodied tracking framework that supports text, point, bounding box, and mask prompts within a unified architecture. USS encodes heterogeneous prompts with modality-specific encoders, fuses prompt tokens with visual features through hybrid attention, and decodes compact prompt-conditioned representations into egocentric waypoints. To further improve temporal robustness, USS incorporates a latent world model that predicts future representations through self-supervised alignment. Real-robot experiments demonstrate that explicit spatial target cues yield higher success rates than text-only prompts, particularly in scenarios involving similar distractors and longer-horizon tracking where maintaining instance-level target identity is critical. In the simulation benchmark, USS also achieves state-of-the-art performance among non-MLLM-based methods and competitive results against recent MLLM-based approaches with faster inference speed. Our findings reveal that spatial-semantic prompting provides a more precise and flexible target indication interface for embodied visual tracking. Project site: this https URL.

---


### 95. [Manipulation Is Task-Dependent: A Multi-Axis, Multi-Environment Evaluation of Frontier LLMs](https://arxiv.org/abs/2606.25899)

**<font color=#1a73e8>作者：</font>** Adeeb Zaman, Erik Nordby, Fred Heiding  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We evaluate manipulative behavior in six frontier language models across six environments, ranging from negotiation tasks to agentic workflows, resulting in 13{,}590 individual scenarios. Manipulation rates are measured across three axes: framing (mandate honesty or permit manipulation), incentive structure (from no incentives to substantial ones), and task difficulty. Existing benchmarks typically vary a single axis within a single environment, an approach our results show is insufficient. We rank models by manipulation rate and find Spearman rank correlations across environments average $\rho = 0.055$, indicating manipulative tendencies in one task do not necessarily predict those in another. Additionally, we find the axis that drives manipulation varies across different environments. In environments where models are incentivized to misrepresent future actions, instructional framing and structurally binding incentives are the primary drivers; in environments where models are incentivized to misrepresent a ground truth, task difficulty dominates. This split was identified in five environments and validated against a sixth held-out environment. Together, these findings illustrate the importance of rigorous multi-dimensional evaluations when measuring manipulative propensities.

---


### 96. [SurgAtlas: A Large-Scale Surgical Video-Language Dataset with 2,391 Hours of Open and Minimally Invasive Surgery](https://arxiv.org/abs/2606.25905)

**<font color=#1a73e8>作者：</font>** Filippos Bellos, Andre S. Gala-Garza, Miaowei Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SurgAtlas, the largest surgical video-language dataset to date, comprising 15,291 videos (2,391 hours) spanning 18 surgical specialties and over 5,000 procedure types, sourced entirely from publicly available YouTube content. SurgAtlas is also the first surgical video-language dataset to include open surgery at scale, with 6,182 open procedure videos alongside over 9,000 minimally invasive recordings, and the first to establish standardized benchmarks for open-surgery video understanding. We additionally provide an expert-validated subset with verified visual question-answer pairs across diverse open and minimally invasive procedures, serving as a clinically grounded benchmark for surgical reasoning. Compared with existing surgical video-language datasets, SurgAtlas provides one of the most diverse annotation schemas, combining segment-level captions, step- and phase-level descriptions, video-level surgical descriptions, and reasoning-oriented question-answer pairs organized within a hierarchical taxonomy. These annotations are constructed through an automated multi-tier pipeline with LLM-based enrichment and a staged VQA generation framework with explicit groundedness verification. The scale and diversity of SurgAtlas enable training surgical foundation models with broad procedural coverage: we finetune Qwen3-VL-8B through a two-stage captioning-then-instruction pipeline and achieve competitive or state-of-the-art results on multiple established surgical benchmarks, including phase recognition, triplet detection, and reasoning question answering. More broadly, SurgAtlas provides a large native public video corpus that can support future large-scale pretraining of multimodal surgical AI systems and contribute to the development of next-generation foundation models for surgery.

---


### 97. [OracleAnalyser: Analysing Implicit Semantics of Oracle Bone Scripts through MLLMs with Post-training](https://arxiv.org/abs/2606.25906)

**<font color=#1a73e8>作者：</font>** Zijia Song, Yelin Wang, Zhengyi Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the advancement of artificial intelligence, research on oracle bone scripts has entered a new era. However, existing methods and benchmarks remain largely confined to recognition tasks, overlooking the equally crucial aspect of oracle bone analysis. To address this gap, we propose OracleAnalyser, a reasoning framework for oracle bone analysis based on post-training techniques. Specifically, we fine-tune Qwen2.5-VL-3B-Instruct through multiple post-training stages and introduce a new preference optimization algorithm, Stable Focal Preference Optimization (SFPO), tailored to the characteristics of oracle bone datasets. In addition, we release both an oracle bone reasoning dataset and an oracle bone preference dataset, and further construct a new benchmark to evaluate models' analytical capabilities for oracle bone scripts. Extensive experiments validate the superior analytical performance of OracleAnalyser, which achieves remarkable results with only 3B parameters, surpassing models with substantially larger scales.

---


### 98. [In-context Region-based Drag: Drag Any Region to Any Shape](https://arxiv.org/abs/2606.25907)

**<font color=#1a73e8>作者：</font>** Jiacheng Sui, Tianyu Hao, Bingjie Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have shown promise in drag-style editing. Previous works mainly focus on point-based drag, which is inherently ambiguous. This paper focuses on region-based drag and introduces a novel In-Context Region-based Drag (ICRDrag) method. Under the in-context learning framework, ICRDrag consumes a source image, a source region mask, and a target region mask, producing the target dragged image. Built upon the basic in-context learning model, we introduce two novel attention regularization: 1) image-mask attention consistency to ensure that a target region attends to similar source regions for image and mask modalities; 2) source-target attention correspondence to ensure the mutual correspondence between source and target regions. To facilitate region-based drag, we also construct Paired Region Dataset (PRD), a large-scale dataset with paired masks and images. Extensive experiments show that ICRDrag significantly outperforms existing methods in both quantitative metrics and user studies, achieving superior editing accuracy and visual fidelity. The dataset, code, and model are available at this https URL.

---


### 99. [Explainable Control Framework (XCF) based on Fuzzy Model-Agnostic Explanation and LLM Agent-Supported Interface](https://arxiv.org/abs/2606.25941)

**<font color=#1a73e8>作者：</font>** Faliang Yin, Hak-Keung Lam, David Watson  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Increasing demand for precise and reliable control in complex scenarios has led to the development of increasingly sophisticated controllers, including data-driven approaches employing closed box models and mathematically rigorous yet complex designs. This complexity highlights the needs for explainable control that can provide human-understandable insights into controller behavior. In this paper, an explainable control framework (XCF) along with supporting algorithms and user interface are proposed to explain how controllers determine their control actions and their underlying working mechanism. The novel contributions of this work are threefold: First, the XCF is designed to provide model-agnostic explanations for controllers in closed-loop systems and can optionally refine local explanations by system response dynamics. Second, a novel explanation method, hierarchical fuzzy model-agnostic explanation for control systems (HFMAE-C), is proposed based on the designed framework. The HFMAE-C employs a fuzzy logic system to approximate the controller's behavior and system dynamics, providing sample, local, domain and universe level explanations via IF-THEN rules revealing the controller's decision logic and salience values quantifying the contribution of system states to control actions. Third, a large language model agent-supported user interface is developed to automatically analyze user requirements, select appropriate algorithms, interpret the generated explanations to a natural language report, and provide interactive consultation. Case studies on inverted pendulum system and Turtlebot obstacle avoidance demonstrate the effectiveness of the proposed method through simulated user experiments and quantitative comparisons with mainstream explainable control approaches.

---


### 100. [Agentic System as Compressor: Quantifying System Intelligence in Bits](https://arxiv.org/abs/2606.25960)

**<font color=#1a73e8>作者：</font>** Zihan Qin, Hongrui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are turning from isolated predictors into agentic systems: they call tools, retrieve evidence, obey environment constraints, use verifiers, and complete tasks through search and multi-turn interaction. We adopts an analytical viewpoint based on "compression is intelligence": under a fixed task distribution, interface, and compute budget, a stronger agentic system lets a target object be reconstructed with fewer bits. We operationalize the measure with arithmetic coding, seed coding, and a fallback, and evaluate it in five settings: reversed text, chess moves, protein sequences, retrieval-augmented question answering, and semantic story compression; in all of them agentic components reduce codelength. These small, controlled experiments cover component types typical of real agentic systems, show that codelength can analyze how components, observers, and budgets change residual uncertainty, and offer guidance for evaluating real agent systems.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-112](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
