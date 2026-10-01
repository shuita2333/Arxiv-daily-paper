# 🧠 大模型相关研究 | 2026年10月02日

> 本类共 **390** 篇论文：已确认 **371** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-390](./part-08.md)

---

### 101. [Understanding Off- vs On-Policy Distillation: A Tale of Distinct Training Objectives](https://arxiv.org/abs/2609.38666)

**<font color=#1a73e8>作者：</font>** Qiwei Di, Xuheng Li, Kaixuan Ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) learns from teacher feedback on student-generated responses and has shown promise in reducing forgetting relative to supervised fine-tuning (SFT). However, its benefits and fragility remain incompletely understood. We study sequential distillation from multiple teachers, where the student minimizes its average divergence from the teachers. Forward Kullback--Leibler (KL) divergence yields a weighted arithmetic mixture, while reverse KL yields a normalized weighted geometric aggregate. We develop algorithms that learn these targets under off-policy and on-policy feedback, respectively, establishing logarithmic regret bounds in the tabular setting and extending the analysis to function approximation. By analyzing these aggregation targets, we identify mechanisms that help explain both the benefits and fragility of OPD. Relative to forward KL, reverse KL can better retain a confident expert's preferences under uninformative feedback, but is more sensitive to teachers that assign very low probabilities to correct responses. Its token-level conditionals also reveal a dependence on continuation distributions that can favor incorrect prefixes over long horizons.

---


### 102. [Provable Test-Time Scaling for Beam Search in LLM Reasoning](https://arxiv.org/abs/2609.38672)

**<font color=#1a73e8>作者：</font>** Qijia He, Yu Huang, Yuan Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Beam-search-based test-time methods provide an effective way to improve large language model (LLM) performance on long-horizon generation by pruning invalid reasoning paths early, leading to significantly improved reasoning efficiency and more favorable test-time cost scaling. Despite strong empirical success, the theoretical understanding of beam search remains limited. In this paper, we study the test-time compute guarantee of the commonly used beam search framework that uses the model's internal log-likelihood for intermediate scoring, while relying on an external reward model only after a complete response is generated. We first establish a lower bound for vanilla beam search, showing that at least $\Omega(C^\star(x)^2)$ samples are required for the optimal response to survive, where $C^\star(x)$ is the token-level coverage coefficient for prompt $x$. This motivates our modified confidence-filtered beam search (CF-Beam), which reduces the sufficient coverage dependence from quadratic to nearly linear under prefix competitiveness, for fixed horizon, gap, and target accuracy. We then show that the regret of CF-Beam is upper-bounded by the probability of rare failure events and the reward estimation error scaled by a path-level coverage coefficient, where the rare-failure term vanishes as per-step sampling increases. Our results highlight a fundamental advantage of beam search over sequence-level inference methods such as Best-of-N and Best-of-Majority. While the guarantees of these approaches typically involve coverage coefficients that grow exponentially with the horizon $L$, CF-Beam controls the dominant search-induced term through a token-level coverage coefficient that scales polynomially with $L$. Our numerical experiments further confirm that beam search is more robust on hard instances and under increasing reasoning horizons.

---


### 103. [Concept-Grounded Attention: A Controlled Evaluation of Graph-Injected Attention, Temporal Versioning, and Epistemic Status](https://arxiv.org/abs/2609.38684)

**<font color=#1a73e8>作者：</font>** Sachin Dev Duggal, Pradyumna Swarnalatha Ramanna, Alexandros Vassiliades  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge-intensive language-model systems typically represent external knowledge as text chunks or static graphs, with limited support for concept evolution, point-in-time reasoning, and distinctions between validated and inferred knowledge. We introduce the Concept Lifecycle Model (CLM), which represents concepts as persistent, graph-grounded, temporally versioned entities with explicit provenance and epistemic status, and Concept-Grounded Attention (CGA), which injects concept-graph structure into transformer computation through graph-biased self-attention (Form A) and gated cross-attention over concept nodes (Form B). We evaluate the framework in controlled settings using disabled-mechanism baselines. On 200 MuSiQue and HotpotQA questions with retrieval fixed, concept-graph retrieval recovers explicit multi-hop paths but does not improve evidence recall. Form A appears to steer attention, with 2.76 times more attention on gold than distractor concepts, but the same ratio occurs when Form A is disabled; the learned bias is negligible and no answers change. An identity-preserving Form B improves F1 from 0.188 to 0.221, but control concepts yield 0.213, indicating that most of the gain reflects added capacity. On LongMemEval, explicit temporal representation improves answer accuracy by 13 to 25 points across all tested generators, up to 122B parameters, while simplified CLM version resolution performs similarly to dated serialization because concept identity is not established reliably. On a synthetic source-independence task, protocol-derived epistemic status reduces unsupported assertions from 28% to 0.1% in a fine-tuned small model and from 19-68% to 0-5% in 72-122B models. Overall, the results support making temporal validity and epistemic status explicit, while showing that graph-attention diagnostics are not informative without disabled-mechanism controls.

---


### 104. [EPIC: Epipolar-Consistent 360° Immersive Stereo Video Generation](https://arxiv.org/abs/2609.38689)

**<font color=#1a73e8>作者：</font>** Debabrata Mandal, Dongdong Fu, Jonathon Miller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Immersive displays can enable rich and diverse virtual experiences. Manually authoring every possible experience to realize this potential, however, is prohibitively expensive, difficult to scale, and impractical. Generative AI models could remove this bottleneck, but today's models are built for conventional displays and cannot generate the high-resolution, stereoscopic $360^\circ$ content required for immersive viewing. Further, temporal and stereo inconsistencies that may be tolerable on conventional displays can become highly disruptive when viewed through an immersive headset.
Here, we address this gap with a zero-shot generative pipeline that extends existing video diffusion models into 4K stereoscopic $360^\circ$ videos. Inspired from binocular vision and depth perception, we develop an epipolar-aware $360^\circ$ image matching metric that captures the temporal and stereo geometric inconsistencies across views. We then use this metric as a preference signal for direct preference optimization with limited training data. Our work enables $360^\circ$ stereo video generation and provides a scalable path for bringing generative content to immersive displays, allowing diverse mixed reality experiences on demand.

---


### 105. [SpatialCORE: Confidence-Aware Grounded Spatial Reasoning in Large Vision--Language Models](https://arxiv.org/abs/2609.38716)

**<font color=#1a73e8>作者：</font>** Rafi Ibn Sultan, Xiangyu Zhou, Md. Sajid Alam Chowdhury 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have made remarkable progress across visual perception tasks, yet spatial reasoning remains a persistent weakness, especially for questions that require reasoning over visual space. Recent spatial-reasoning methods incorporate generated grounding, where models predict bounding boxes, masks, or other localization outputs for task-relevant objects as part of their reasoning trace. However, these approaches typically optimize final-answer correctness alone, allowing correct answers to be rewarded even when the model does not reason from confidently localized task-relevant objects. We introduce SpatialCORE (Spatially COnfident REasoning), a post-training framework that turns the model's own confidence in generated grounding into a learning signal for spatial reasoning. Its central idea is to reinforce grounding that is both accurate and confident, encouraging the model to reason from confidently localized task-relevant objects. SpatialCORE realizes this through a self-regulating spatial reward that weights each predicted bounding box's matching quality by its coordinate-token confidence. An answer gate further ties grounding optimization to final-answer correctness. SpatialCORE achieves state-of-the-art results among open-source and specialized spatial reasoning models across diverse benchmarks, and transfers effectively in zero-shot settings to unseen data distributions. The source code is available at this https URL.

---


### 106. [Soft Spatial Reasoning](https://arxiv.org/abs/2609.38717)

**<font color=#1a73e8>作者：</font>** Rafi Ibn Sultan, Md. Sajid Alam Chowdhury, Saleh Zare Zade 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) commonly perform spatial reasoning through chain-of-thought (CoT), encoding intermediate reasoning as autoregressive sequences of discrete language tokens. Such hard thinking requires committing to a single token at each step, even when the correct spatial interpretation remains uncertain. This early commitment constitutes premature discretization: an incorrect token selection can propagate errors through subsequent reasoning. We propose Soft Spatial Reasoning, a post-training framework that introduces soft thinking for spatial tasks in LVLMs. At each intermediate reasoning step, the LVLM forms a continuous soft state by mixing token embeddings rather than selecting a single token, allowing multiple candidate continuations to influence the next step. The appropriate degree of softness, however, can vary across reasoning steps: retaining multiple candidates may preserve a useful spatial interpretation, but if those candidates imply conflicting spatial relations, mixing them may interfere with subsequent reasoning. At the core of Soft Spatial Reasoning is AdaptSoft, a controller that uses the current hidden state and predictive uncertainty to adapt the degree of softness at each reasoning step. To train AdaptSoft, we introduce a gradient-alignment learning objective that provides a step-specific learning signal for softness control without intermediate reasoning supervision. Across diverse spatial benchmarks, Soft Spatial Reasoning outperforms hard and fixed-soft CoT baselines using the same backbone, as well as a range of existing LVLMs. The source code is available at this https URL

---


### 107. [MetaSteer: Context-Conditioned, nonlinear Steering via Attention-Projection Adaptation](https://arxiv.org/abs/2609.38718)

**<font color=#1a73e8>作者：</font>** Mehdi Jafari, Hao Xue, Flora Salim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Steering large language models typically relies on linear, context-independent interventions in activation space, an assumption that recent work has challenged and that can induce an information bottleneck when a fixed representation must encode many behavioral distinctions. We introduce MetaSteer, a method that learns nonlinear interventions with context-dependent effects and applies them to attention projection matrices, producing activation effects that vary with the input context by construction and requiring no linear concept-geometry assumption. Framed as preference-based optimization, MetaSteer is trained once on a pooled preference corpus and transferred zero-shot to unseen concepts and out-of-distribution contexts. We find that, despite using low-rank adapters, MetaSteer induces structured, context-dependent changes in hidden-state trajectories while partially preserving aspects of their local trajectory dynamics, including velocity and curvature. We evaluate MetaSteer on three controlled text-generation benchmarks and three agentic settings across multiple model families and scales. MetaSteer matches or outperforms strong task-specific steering baselines on most aggregate comparisons in the zero-shot regime. Across the evaluated settings, stronger text-generation steering is associated with stronger agentic steering performance. We further discuss geometric trajectory effects, capability retention, and safety considerations raised by transferable steering.

---


### 108. [UniEvo-VL: An On-policy Self-Distillation Training Recipe for Multimodal Model Self-improvement](https://arxiv.org/abs/2609.38721)

**<font color=#1a73e8>作者：</font>** Fang Wu, Da Xing, Yanjie Huang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern multimodal models bring generation and understanding into a single unified system, which enables them to provide and learn from their own feedback. Motivated by this unified capacity, we introduce UniEvo-VL, a self-evolving framework for multimodal models to learn from this constructive self-correction feedback during test-time compute. Instead of relying on a separate, often larger, teacher, we leverage their self-critiques as privileged information and ask a single multimodal model to act as both teacher and student with different contexts. The student only sees the vanilla question, while the teacher conditions on the privileged critique. Then training minimizes the per-state divergence between their denoising diffusion distributions over the student's own sampling trajectories. Experiments demonstrate that UniEvo-VL improves the image generation capabilities of multimodal models, while maintaining their sensitivity to additional reflection information. Specifically, we build on top of the open-source Qwen-image-2512 and observe a significant performance gain from 0.747 to 0.808 on GenEval and from 32.97 to 35.53 on GenEval2 Soft-TIFA. Moreover, attempts with more powerful external critics (e.g., GPT5.6-Luna) show that multimodal models with strong judge capabilities can anticipate a higher self-evolving ceiling. Last but not least, mixed text-rendering outcomes show that our self-improvements may not be uniform across different tasks. Our study aims to shed light on the current hot recursive self-improvement research line to enhance the user experience when using multimodal models without external supervision or guidance.

---


### 109. [Anchor-ECC: Local Integrity Checking for Watermarked LLM Outputs via Error-Correcting Codes](https://arxiv.org/abs/2609.38722)

**<font color=#1a73e8>作者：</font>** Zewei Deng, Muhammad Siddeek, Liyan Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM watermarking has become an effective approach to distinguishing AI-generated text from human-written text by embedding detectable patterns during generation. However, a small post-generation edit may change the meaning of the text without removing its overall watermark signal, creating a risk that the modified content is still attributed to the original model. We propose Anchor-ECC, which incorporates the error-correcting code (ECC) constraints and explicit boundary anchors into the watermark structure and pairs them with a dynamic-programming decoder to detect and localize post-generation edits. Across Qwen3-8B, Mistral-7B-Instruct-v0.3, and OPT-125M, the approximate-hard setting achieves about 99.7% block-level true positive rate (TPR) with at most 7.6% false alarm rate (FAR) for edit detection under mixed insertions, deletions, and substitutions, while preserving the distinction between watermarked outputs and unwatermarked text. Additional quality experiments identify lower-perplexity configurations that retain strong edit-detection performance. Together, these results extend LLM watermarking from source identification to local integrity verification while supporting configurable trade-offs between detection reliability and generation quality.

---


### 110. [Afterglow: A Place-Based Memorial Ecology for AI-Mediated Pet Bereavement](https://arxiv.org/abs/2609.38729)

**<font color=#1a73e8>作者：</font>** Hanjing Shi, Dominic DiFranzo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Pet bereavement often receives little social recognition. Generative AI can give a continuing bond a responsive voice, but a comforting reply may also claim authority to forgive or request attention. We investigate how a memorial can support connection without turning remembrance into obligation. Through Research through Design, we developed Afterglow, a mobile world connecting private remembrance, human witnessing, and symbolic Pet messages. A formative survey (N=57) informed the initial design, followed by six online roundtable walkthroughs with 20 unique participants across two prototype iterations. Our interpretive analysis develops tensions between returnable connection and emotional obligation, recognizable likeness and ontological clarity, and protective intervention and surveillant authority. We contribute Legible Restraint, a cross-layer requirement that limits on relational authority survive changes in speaker, generation context, trigger logic, data use, and participation. Its temporal consequence, Designing for Goodbye, keeps remembrance available without making continued use a condition of care.

---


### 111. [Code to Control: Synthesizing Parameterized Reactive Controllers](https://arxiv.org/abs/2609.38733)

**<font color=#1a73e8>作者：</font>** Zergham Ahmed, Joshua B. Tenenbaum, Chris Bates 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent LLM-based approaches to control either invoke a language model to select actions or synthesize world models that require planning at every decision, introducing latency that can limit real-time use. We introduce Code to Control, an approach that synthesizes Python controllers which execute directly as policies. Code to Control separates program structure from parameters. An LLM synthesizes the controller structure, while derivative-free search fits its parameters for continuous control using feedback from the environment. Once learned, the resulting controllers require neither LLM inference nor planning at decision time, enabling real-time gameplay and, under our timing protocol, faster action selection than a PPO policy. Across a suite of Atari games, Flappy Bird, and MuJoCo tasks, Code to Control outperforms planning-based program synthesis methods, remains competitive with deep reinforcement learning while using fewer environment interactions, transfers across substantial changes in environment dynamics, and scales to complex locomotion tasks.

---


### 112. [Learning to Route in Visual Space via Multi-Step Embedding Retrieval](https://arxiv.org/abs/2609.38743)

**<font color=#1a73e8>作者：</font>** Tianyu Chen, Mingyuan Zhou, Jiaxing Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents rely on retrieval tools to access external knowledge, yet visual agentic search remains severely bottlenecked by standard single-step retrievers. In current pipelines, the agent must issue text queries for every intermediate step, struggling when visual clues are difficult to describe or when the retriever fails to surface necessary intermediate evidence within its top results. We hypothesize that offloading multi-step navigation across the entire embedding space directly to the retrieval tool resolves this performance bottleneck. To study this systematically, we introduce VHOP, a flexible data generation framework and benchmark with five core difficulty levels testing both visual matching and search planning. Using this framework, we develop VHOP-Router, an end-to-end training pipeline---combining supervised fine-tuning, online imitation learning, and reinforcement learning---that transforms a standard embedding model into an autoregressive multi-step retriever. Operating directly in the visual latent space, VHOP-Router retrieves linked image chains in a single tool call without requiring the agent to formulate intermediate text queries. Experiments show VHOP-Router boosts retrieval performance from under 5\% to 76.3\%. In agentic search, it improves task success rates by 52.7\% and reduces the average token length by 61\% from 1886 to 728, whereas upgrading the agent yields only a 3.7\% gain. Compared to a strong baseline where the agent retrieves the top 50 results per step, VHOP-Router maintains superior performance while reducing in-context images by $23\times$ and cutting the cumulative API payload by $35\times$. The models also generalize robustly to unseen difficulty levels and realistic test sets. Ultimately, VHOP and VHOP-Router provide an efficient and effective solution for visual agentic search that leaves native LLM capabilities entirely intact.

---


### 113. [Agentic Relative Camera Pose Estimation via Learned Ranking and Verification](https://arxiv.org/abs/2609.38755)

**<font color=#1a73e8>作者：</font>** Zhining Gu, Shangjie Du, Weimin Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A wide range of approaches have been developed for camera pose estimation, including correspondence-based methods, end-to-end pose regression, and recent 3D geometric foundation models. Our key observation is that no single estimator is optimal for diverse challenges, such as wide baselines, lack of texture, appearance changes, and occlusions. Further analysis reveals substantial performance variation across both benchmarks and individual image pairs, with different estimators exhibiting complementary strengths. We introduce PoseAgent, an agentic framework for relative camera pose estimation that dynamically orchestrates pose estimators through learnable ranking and verification. Given an image pair, a profiling agent first extracts appearance, semantic, and geometric features relevant to pose estimation, e.g., scene type. A learned ranking agent then predicts the relative competence of multiple pose estimators given the image-pair profile. The top-ranked estimator is executed, and its predicted pose is assessed by a learned verification agent that estimates the corresponding pose error. When verification fails, PoseAgent adaptively invokes lower-ranked estimators until a candidate is accepted or the execution budget is reached. For pose verification, our verification network predicts pose errors more accurately than prior models. For pose estimation, PoseAgent improves AUC@5 degree up to 4.2% over the strongest standalone estimator on each of ARKitScenes, MegaDepth, ScanNet++, and RealEstate10K. On ARKitScenes, PoseAgent also outperforms VLM-based agents, which include a VLM ranker with the same verifier and fallback policy. These results demonstrate the effectiveness of our learned ranking and verification.

---


### 114. [Self-Evolving Algorithm-Design Agents: Escaping In-Context Evolutionary Stagnation via Population-Curated Policy Optimization](https://arxiv.org/abs/2609.38757)

**<font color=#1a73e8>作者：</font>** Chen Lu, Ke Xue, Siyuan Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly participating in complex real-world tasks in the form of algorithm-design agents, designing and refining algorithms. Many successful algorithm-design agents adopt pure in-context evolutionary frameworks, but they may quickly plateau in domains that require specialized knowledge. Parametric adaptation offers a way to internalize specialized knowledge, but conventional training requires abundant domain-specific corpora while high-quality algorithms are scarce in complex algorithm-design scenarios. In this paper, we propose sample-efficient parametric self-evolution where agents can explore and learn from self-generated algorithms. First, we characterize in-context evolutionary stagnation and analytically propose the Improvement Chain proposition, showing how learning successive self-generated algorithms can locally increase the likelihood of neighboring algorithms. Motivated by this local-transfer perspective, we further propose Population-Curated Policy Optimization (PCPO) to utilize a global population and a hybrid policy update scheme for retaining and reusing high-quality, diverse self-generated algorithms, shifting the policy towards stronger algorithms. In the task of learning rate schedule design for global placement in electronic design automation, trained only on 4 chip cases, PCPO outperforms the state-of-the-art in-context evolutionary methods (e.g., OpenEvolve and ShinkaEvolve) on average across 16 chip cases. With an 8B-size base model, PCPO achieves competitive performance compared to frontier closed-source models such as GPT-5.5. PCPO also reduces inference-time token cost by internalizing grounded domain knowledge and prompt distillation. Moreover, PCPO achieves significant speedups on four GPU kernel designs, with an average of 8.27$\times$ speedup against the PyTorch Eager baseline.

---


### 115. [Event-Driven Refresh and Recurrence Memory to Reduce Stale Grounding in Referring Video Object Segmentation](https://arxiv.org/abs/2609.38758)

**<font color=#1a73e8>作者：</font>** Abu Hanif Muhammad Syarubany, Jaehyun Jang, Siwoo Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Video Object Segmentation (RVOS) aims to produce a pixel-accurate mask sequence for an object specified by natural language. Sa2VA combines a multimodal large language model with SAM2 for grounded segmentation; however, its inference typically grounds the query from a small fixed set of initial keyframes and then relies on propagation. In long or dynamic videos, this can cause stale grounding and persistent false positives when the object composition changes (e.g., distractors enter or the target disappears/re-appears). We propose Event-Driven Refresh + Recurrence Memory (EDRRM), an enhancement that selectively re-invokes Sa2VA only at stable change points. EDRRM triggers refresh boundaries using an EMA-smoothed event score computed from tracking-derived cues (births/deaths and coarse composition/layout changes) with temporal constraints. A recurrence memory further retrieves anchor frames via CLIP similarity to re-condition the model on re-appearance events. Experiments on Ref-DAVIS17, MeViS, and ReVOS show that EDRRM achieves a competitive accuracy-efficiency trade-off relative to fixed-window and FrameDiff-SSIM baselines, maintaining comparable or superior J&F scores at substantially lower average refresh-call budgets and reducing false-positive failures. End-to-end runtime analysis further confirms that the overhead introduced by tracking, CLIP-based recurrence matching, and the identifiability gate remains modest relative to the dominant Sa2VA inference cost, thereby validating the efficiency of the proposed pipeline.

---


### 116. [Where Do Multi-Agent Systems Fail? Evidence-Grounded Diagnosis of Collective Mechanisms](https://arxiv.org/abs/2609.38761)

**<font color=#1a73e8>作者：</font>** Zhengye Han  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> When a multi-agent system answers correctly, it is tempting to conclude that its agents shared, checked, and used information as intended. Yet a system can break one of its collective mechanisms, the rules that govern how agents route, admit, store, and act on shared information, and still return the right answer, while a wrong answer rarely reveals which mechanism failed. We ask what evidence from an execution is sufficient to conclude that a particular mechanism was violated. Our answer is a diagnostic contract, which separates what counts as a violation from which execution records can establish one, and concludes that a violation is supported, ruled out, or unknown; removing records can make this conclusion unknown but never reverse it. We test contracts for four mechanisms by replaying executions from the step where a mechanism acts, once unchanged, once with the mechanism broken, and once with it restored. Broken mechanisms often left the answer correct. An LLM diagnoser detected many more violations from internal records than from public outputs, yet with identical records a generic prompt often claimed certainty the records did not support, which prompts stating the contracts largely avoided. The contracts also applied, in narrow form, to mechanisms in independently developed systems, but a diagnostic behavior that was nearly perfect on our benchmark degraded on an independently developed workflow. A correct outcome is therefore no substitute for records of how collective mechanisms operated, and agreement on one benchmark does not show that a diagnoser transfers to another system.

---


### 117. [Lasting Effects of Abstract Pretraining Beyond Perplexity](https://arxiv.org/abs/2609.38764)

**<font color=#1a73e8>作者：</font>** Zachary Shinnick, Hemanth Saratchandran, Damien Teney 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are typically pretrained from random initialization. Recent work challenges this convention, showing that a brief warm-up on abstract, algorithmically generated data can provide a better starting point for subsequent learning of natural language. In this paper, we show that in small language models, such a warm-up improves specific capabilities that are not reflected in language-modeling perplexity. Our warm-up uses an abstract stack-manipulation task that requires compositional and state-tracking capabilities. Allocating as little as 1% of pretraining tokens to this data improves multi-hop question answering by up to 3.9 F1 points on MUSIQUE, with additional gains on HOTPOTQA and 2WIKIMULTIHOPQA despite comparable language-modeling perplexity. Controlled experiments show that the warm-up substantially accelerates the acquisition of deeper reasoning chains. We also explore what drives this transfer. First, the structure of the data matters: replacing the stack task with a queue fails to produce the same gains. Second, the gains are specific: performance improves on sequential reasoning chains, with no consistent benefit on tasks that combine or compare independent facts. Third, timing matters: mixing abstract data with natural language is far less effective than an initial dedicated phase, and exposure after pretraining completely removes the benefits. The early advantage persists through billions of subsequent language tokens. These results show that early abstract training can reliably shape the capabilities language models later acquire.

---


### 118. [dattri-LLM: A Unified and Efficient Library for Training Data Attribution at LLM Scale](https://arxiv.org/abs/2609.38767)

**<font color=#1a73e8>作者：</font>** Shixuan Liu, Tongli Zhou, Junwei Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training data attribution (TDA) estimates the contribution of individual training examples to model outputs. Most scalable TDA methods rely on per-example gradients, whose computation and use at LLM scale pose challenges in efficiency, compatibility, and extensibility. We introduce dattri-LLM, a TDA library that makes gradient-based attribution more practical at scale. For efficiency, dattri-LLM uses compact gradient representations and dynamically routes gradient operations based on a cost model. For compatibility, its capture mechanism collects per-example gradients from existing training loops that call backward(), without requiring changes to the loop or its configuration. This includes distributed training with DDP and FSDP and pipelines built with HuggingFace Transformers, TRL, and OLMo. For extensibility, dattri-LLM exposes reusable gradient operations and training-time callbacks for implementing attribution methods and applications. These interfaces support a variety of attribution methods, including gradient similarity, curvature-based influence, and trajectory-based methods, as well as applications that act on gradients during training, such as online data selection. On the same hardware and workload, dattri-LLM achieves 3.2x the throughput of the fastest competing library on average, scales multiple attribution methods to 110B-parameter models across four H200 GPUs, and offers superior attribution fidelity-cost trade-offs across a range of models with different model families and scales.

---


### 119. [Distill the Visual Evidence, Not Just the Answer: Cross-World On-Policy Distillation for Vision-Language Models](https://arxiv.org/abs/2609.38777)

**<font color=#1a73e8>作者：</font>** Yuanhao Sun, Huawei Ji, Jiaxin Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A central goal of vision-language model (VLM) distillation is to transfer both the teacher's language capabilities and its visual understanding. However, existing methods primarily supervise the student's output, leaving visual understanding implicit. Our analysis reveals that a student can match the teacher's answer without relying on the same visual evidence, raising the question: how can we ensure the student responds to the visual information that actually determines the answer? To this end, we propose \textbf{Cross-World On-Policy Distillation (CW-OPD)}, which explicitly supervises the student's response to changes in visual evidence. For each example, CW-OPD constructs two visual worlds that share the question and scene context but differ in answer-critical evidence, yielding different answers. We perform on-policy distillation in both worlds and distill the teacher's cross-world belief transition, encouraging the student to match not only \emph{what} the teacher predicts but also \emph{why} its prediction changes with the evidence. A gradient analysis shows that this term is invariant to errors shared by both worlds and supplies a corrective signal invisible to endpoint matching alone. In this way, CW-OPD makes reliance on the relevant visual evidence an explicit distillation target rather than an implicit consequence of output matching. To diagnose whether a model truly grounds its answers in visual evidence, we introduce CWBench, which measures cross-world consistency via Cross-World Pair Accuracy (CWPA). Experiments on Qwen3.5-4B show that CW-OPD outperforms the strongest baseline by \textbf{1.2} points on average, and the 4B student exceeds DeepSeek-V4.1 (552B) by \textbf{22.4} CWPA points on CWBench. Code is released in this https URL.

---


### 120. [Action Conditioned Bisimulation For GUI Agent Memory](https://arxiv.org/abs/2609.38778)

**<font color=#1a73e8>作者：</font>** Hongbo Zhang, Liuyang Song, Quanquan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent that remembers what it did on a web page must decide when two pages count as the same. Memories built on observation similarity merge pages that look alike but behave differently, and GUIs are full of such pages: two tabs of one widget or two rows of one menu answer the same click differently. We define the merge rule as an action-conditioned bisimulation over the empirical predictive state graph a frozen agent fills as it acts. Two states merge only when their shared actions lead to agreeing outcomes and successor blocks under an affordance label. Observation similarity never enters the rule, and nothing is trained. It replaces the merge rule of an existing outcome-value memory, so a closed-loop comparison isolates it. On MiniWoB++ it raises success rate over a memoryless agent, while a control taking identical exploratory detours, the prior successor-representation merge, and the same criterion without action conditioning change nothing.

---


### 121. [ChartDensity-Bench: Benchmarking MLLMs for Numerical Data Reconstruction under Visual Density](https://arxiv.org/abs/2609.38781)

**<font color=#1a73e8>作者：</font>** Xinhe Wu, Yadong Jin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) offer a promising approach for recovering numerical data from scientific charts, but their ability to reconstruct chart data from visually dense figures remains poorly understood. Existing chart understanding benchmarks primarily evaluate question answering or chart-level reasoning and provide limited support for evaluating structured numerical reconstruction from scientific figures. We introduce \textbf{ChartDensity-Bench}, a benchmark for evaluating MLLMs on structured numerical data reconstruction from compound chart figures under controlled visual density. Built from charts paired with source-level ground-truth data, ChartDensity-Bench systematically varies the number of simultaneously presented charts ($k\in{1,3,6,9}$), enabling controlled evaluation of density-induced degradation. We further propose a multi-dimensional evaluation framework covering structural reliability, reconstruction completeness, parseability, and numerical fidelity. Experiments on five recent MLLMs show that numerical reconstruction generally degrades as visual density increases, while the magnitude of degradation varies substantially across models. Chart-level paired comparisons further show that the same source chart can incur higher reconstruction error when embedded in denser visual contexts. These findings highlight visual density as an important and previously underexplored factor in MLLM chart data reconstruction and provide a systematic benchmark for evaluating model robustness in this setting.

---


### 122. [Persona and Persuasive Framing in AI Voice Agents: A $2\times2$ Field Experiment with Children](https://arxiv.org/abs/2609.38782)

**<font color=#1a73e8>作者：</font>** Thilo Tamme, David Steck, Anton Hantel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational agents increasingly interact with children, yet evidence on how their design shapes children's susceptibility to persuasion comes almost entirely from the lab. We report a $2\times2$ randomized field experiment embedded in a public German Santa Claus telephone hotline. Children's calls were randomly routed to one of four LLM voice agents varying persona (Santa, high authority, vs. Helper, low authority) and framing (persuasive nudges toward prosocial wishes vs. neutral). Of 1,072 logged calls, 89 conversations (median age 6) met inclusion criteria. Persuasive framing raised the probability of a prosocial wish from 11.6% to 45.7%, robust to controls. Persona authority showed a near-zero effect: Santa did not outperform the Helper. Persona instead shaped engagement; children hung up on the Helper far more often within the first minute (65% vs. 39%). Where context already lends an agent legitimacy, how it speaks shapes children's compliance more than who it claims to be.

---


### 123. [LEARN-TS: LLM-Enhanced Alignment and Reconstruction with Normality Guidance for Multivariate Time-Series Anomaly Detection](https://arxiv.org/abs/2609.38789)

**<font color=#1a73e8>作者：</font>** Jahyeob Koo, Kio Yun, Byoungmo Koo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstruction errors in multivariate time-series anomaly detection may not reliably distinguish abnormal behavior from benign deviations. Language-derived semantics offer complementary context, but existing multimodal approaches may rely on time-associated paired textual information that is difficult to obtain consistently and is not provided by standard multivariate time-series anomaly detection benchmarks. This setting poses two challenges: (1) conditioning masked reconstruction on window-specific semantics without exposing exact numerical targets or anomaly-specific cues, and (2) using a window-independent concept of normality as a complementary semantic reference rather than an independent anomaly detector. We propose LLM-Enhanced Alignment and Reconstruction with Normality Guidance for Time Series (LEARN-TS), which uses a frozen language model to construct two role-separated semantic representations without requiring temporally paired external text. Window-specific observation semantics encode temporal and cross-variable context without exact numerical values to guide channel-shared patch-masked reconstruction. A fixed, dataset-agnostic normality prompt provides a window-independent semantic reference for aligning normal representations and estimating normality discrepancy. At inference, masking each temporal patch once yields timestamp-level reconstruction evidence, conditionally modulated by discrepancy from a separate unmasked view. Across four benchmarks, LEARN-TS achieves the highest mean performance in 13 of 16 dataset-metric comparisons. Controlled ablations examine observation conditioning, joint normality alignment and scoring, and reference content, showing dataset-dependent ranking benefits and modest average gains from semantic over random references.

---


### 124. [Training LLM Judges from Language Feedback via Position-Selective Self-Distillation](https://arxiv.org/abs/2609.38792)

**<font color=#1a73e8>作者：</font>** Ilgee Hong, Changlong Yu, Zhenghao Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study training LLM judges from natural language feedback, especially for subjective tasks where the verdict depends strongly on which evaluation criteria the judge invokes and how it weighs them. The dominant approach, outcome-supervised RL (e.g., GRPO), credits every token in the rollout with a single scalar determined only by the accuracy of the final verdict, providing no separate credit at the criterion-choice tokens and ignoring the rich language feedback (e.g., preference rationales) that naturally accompanies preference labels. Self-Distillation (SD) is one natural way to use this language feedback: the same model, conditioned on this feedback, acts as a teacher providing dense, position-level supervision. However, not all positions carry equally useful signal. Using the per-position entropy shift between teacher and student, we identify two regimes: context sharpening, where the teacher concentrates probability on a particular feedback-aligned criterion expression, and context spreading, where the teacher distributes probability across multiple feedback-aligned alternatives. We interpret these patterns as follows: sharpening encourages memorization of a particular criterion expression, whereas spreading promotes semantic understanding by preserving these alternatives. Motivated by this asymmetry, we introduce position masking based on the entropy shift that retains the lower tail of the entropy-shift distribution. Experiments show that masking higher-entropy-shift positions improves out-of-distribution generalization over naive SD. The resulting self-distilled judges outperform judges trained with outcome-supervised RL by 2-9 percentage points on the evaluated subjective subcategories, while remaining competitive on objective ones.

---


### 125. [GraphCert: Bootstrap Agentic Graph Reasoning with Certified Evidence Rubrics](https://arxiv.org/abs/2609.38798)

**<font color=#1a73e8>作者：</font>** Weiqi Jiang, Yuchen Ying, Rui Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph agents extend large language models (LLMs) with the ability to actively explore and reason over knowledge graphs through multi-step interactions with graph tools. However, training capable graph agents typically requires large collections of question-answer pairs and reasoning trajectories, whose manual construction is costly and difficult to scale. Moreover, employing proprietary LLMs to generate such supervision further risks exposing sensitive graph data to external services. Therefore, we propose GraphCert to bootstrap agentic graph reasoning with certified evidence rubrics during post-training. Specifically, the Bootstrapped Graph Quizzer guided by generation controls produces graph-grounded QA pairs and marks supporting evidence, which undergo execution certification and semantic curation. The accepted evidence is then canonicalized into certified evidence rubrics that later reward Graph Solver evidence alignment alongside answer correctness during GRPO training. Experiments on five graph reasoning domains in GRBENCH demonstrate that GraphCert consistently outperforms substantially larger LLM agents and post-training method. Furthermore, our analysis demonstrates that the learned policy transfers robustly across heterogeneous graph domains, suggesting that GraphCert acquires reusable graph-reasoning capabilities rather than domain-specific patterns. These results establish executable self-certification as an effective approach to self-training compact graph reasoning agents. Our code will be made publicly available.

---


### 126. [Overlap, Unique and Conflict: Can LLMs Extract What They Can Recognize?](https://arxiv.org/abs/2609.38799)

**<font color=#1a73e8>作者：</font>** Eftekhar Hossain, Santu Karmaker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding multi-perspective alternative narratives requires identifying how their information agrees, conflicts, or differs across sources. Existing work on cross-text relations largely focuses on categorizing relations between predefined text pairs, such as entailment or contradiction, rather than directly extracting such information from full narratives. To address this gap, we introduce Overlap-Unique-Conflict (OUC) extraction, a cross-narrative task that extracts all overlapping, conflicting, and unique clauses from two narratives. To support this study, we construct a benchmark of approximately 22K narrative pairs and 140K OUC instances spanning factual, argumentative, and political discourse. Evaluating 14 open-source LLMs (0.6B-35B), we find that unique information is far easier to extract than overlap and conflict: the strongest model, Gemma-4-31B, reaches only 61.13% F1-score on overlap and 48.58% on conflict, against more than 75% on unique. Further diagnostic analysis reveals that this difficulty does not stem from relation recognition alone, but rather from a failure to pair and extract the corresponding clauses from full narratives, especially in smaller models. Nevertheless, learning these extractions with task-specific supervision narrows the gap considerably: a fine-tuned Qwen-3-8B gains 15-28% absolute over its baseline and surpasses models roughly four times its size (e.g., Qwen-3.6-35B) on several tasks. Even so, overlap and conflict remain well below satisfactory, leaving cross-narrative clause extraction an open challenge.

---


### 127. [Uncovering Uncontrolled Repetition through Residual Stream Dynamics](https://arxiv.org/abs/2609.38802)

**<font color=#1a73e8>作者：</font>** Yuanhe Zhang, Xinyao Zhou, Haoran Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uncontrolled repetition can prolong autoregressive generation in large language models (LLMs) and enable resource consumption attacks. Prior analyses of repetitive generation have identified strongly activated features in intermediate and late layers. However, how uncontrolled repetition activity emerges and develops before becoming prominent in these layers remains insufficiently understood. In this paper, we investigate this question primarily in large vision-language models (LVLMs), which support a richer set of uncontrolled repetitions through both visual and textual inputs. We propose Tokenwise Residual Comparison (TRC), a method that identifies and localizes anomalies associated with repetition from residual dynamics during generation. TRC compares attention and multilayer perceptron writes to the residual stream across generated tokens to identify patterns associated with repetition. It then selectively suppresses coordinates in the residual stream at the identified layer. Experiments show that TRC effectively mitigates uncontrolled repetition, reducing loop rates by 57\% on average. Our analysis further shows that repetition semantics emerge in shallow layers and propagate through the residual stream, disrupting normal representations. TRC also generalizes to large language models (LLMs) and large reasoning models (LRMs), where it consistently captures analogous repetition dynamics and achieves effective mitigation. Our work broadens the study of repetitive generation from its prominent internal representations to earlier opportunities for intervention, providing insights for mitigating resource consumption attacks.

---


### 128. [Explicit Trajectory Diversity for RL-Based Post-Training of LLM Agents](https://arxiv.org/abs/2609.38805)

**<font color=#1a73e8>作者：</font>** Huaiyu Fu, Heng Cao, Hao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents often admit multiple high-quality solutions to the same task, differing in reasoning structure, tool-use pattern, or interaction trajectory. Yet existing notions of diversity in LLM post-training are mostly implicit, arising from general stochasticity and regularization mechanisms rather than explicitly targeting task-relevant behavioral variation. While such implicit diversity can be useful, it does not directly specify which forms of behavioral variation should be encouraged for a given task. In this work, we study explicit trajectory diversity in RL-based post-training for LLMs. Our key idea is to define diversity through user-specified, task-specific trajectory descriptors, which map each sampled trajectory to an interpretable behavioral representation, and then measure diversity as a set-level functional over the resulting descriptor matrix. Building on this formulation, we introduce Trajectory-guided Joint Policy Optimization(TJPO), a single-policy framework that optimizes explicit diversity over sampled trajectory groups, avoiding the need for population-based policy training, and instantiate it within group-based policy optimization through trajectory-level learning signals. This design makes the diversity objective both interpretable and controllable. Experiments on Sokoban and ALFWorld show that TJPO improves task-specific trajectory diversity while maintaining competitive task performance. Descriptor and trajectory analyses show that the learned variation follows the specified behavioral dimensions and includes distinct successful strategies. Extra experiment results suggest that explicitly shaping trajectory diversity can help LLM agents satisfy user requirements and remain effective when task conditions change.

---


### 129. [Blackboard Intelligence Can Surpass Autoregressive on Globally Constrained Problems](https://arxiv.org/abs/2609.38806)

**<font color=#1a73e8>作者：</font>** Woosang Jeon, Jaeyeon Kim, Sham Kakade 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Next-token prediction has driven remarkable progress in large language models, yet a growing body of evidence suggests that they can struggle on problems governed by complex global constraints. In this work, we focus on this regime and ask whether some of these limitations arise from the inference interface induced by next-token prediction itself. We study this question through blackboard intelligence: an inference-time perspective in which a model works on a fixed, revisable canvas and searches over candidate solution states rather than committing to a causal, left-to-right trajectory. We instantiate this idea with diffusion language models, whose any-order prediction interface naturally exposes predictions over partially filled solution states. Our key observation is that mean confidence, a simple model-internal quantity available from the standard masked diffusion objective, provides a useful proxy for global coherence and can guide inference-time search and revision. Empirically, across ZebraLogic, Nurse Rostering, and Job-Shop Scheduling, Blackboard consistently improves inference while holding the fine-tuned LLaDA-8B-Instruct checkpoint fixed and substantially outperforms same-scale autoregressive baselines, reaching 90.4% accuracy on ZebraLogic-Hard, 76.4% exact feasibility on Nurse Rostering, and 80.2% optimality on JSSP. Stronger autoregressive search and refinement also fail to close the gap on ZebraLogic-Hard, while Blackboard surpasses tested frontier LLMs there and on JSSP despite their substantially greater scale and strong test-time reasoning. We open-source our codebase at this https URL.

---


### 130. [StateTree: Enhancing Long-Term Dialogue Reasoning via Reinforcement Learning](https://arxiv.org/abs/2609.38809)

**<font color=#1a73e8>作者：</font>** Naen Xu, Wanqing Cui, Yibo Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models deployed as personalized assistants must reason over long, evolving interaction histories. However, in long-term dialogue reasoning, relevant evidence is scattered across sessions, preferences may be revised over time, and standard long-context training fails to address these challenges under data scarcity and prohibitive computational costs. We propose StateTree, a data-driven RL method that constructs a challenging auxiliary task from scarce dialogues with verifiable ground truth. StateTree augments multi-session dialogues with a tree-structured path-tracing task: key-value records are embedded across sessions to form a binary tree. Solving the task requires the model to traverse from root to leaf by retrieving records across sessions and comparing timestamps to resolve branches, then recover the hidden target question among distractor leaves. We apply curriculum RL training progressively increasing tree depth and introduce a compositional variant whose edges carry step-level reasoning fragments, training the model to compose partial cues into coherent queries. Trained on 10K-token contexts, StateTree generalizes to 128K tokens without full-length RL costs and exhibits capabilities including cross-session retrieval, temporal reasoning, knowledge update, and compositional multi-hop reasoning. StateTree outperforms both SFT and RL-based baselines while preserving short-context general reasoning. StateTree-7B achieves gains up to +23.60% on LongMemEval (128k), and StateTree-14B reaches 59.00% accuracy on LongMemEval, surpassing QwenLong-L1-32B (45.20%).

---


### 131. [CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models](https://arxiv.org/abs/2609.38810)

**<font color=#1a73e8>作者：</font>** Chunzheng Zhu, Jiaqi Zeng, Hongbo Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As vision language models are increasingly deployed in clinical diagnosis, understanding how they internally resolve competing visual and textual signals becomes a safety imperative. Existing mechanistic analyses remain confined to unimodal text and offer no explanation for why a single misleading sentence can override a correct image based diagnosis, or why a model commits to a confident answer despite insufficient visual evidence. We find that these two safety risks, arbitration failure where textual context overrides visual grounding and brake failure where the model commits without adequate evidence, are mediated by spatially disjoint attention head populations: arbitration heads form a mid-to-deep wideband reflecting cross-layer evidence competition, while brake heads concentrate in a narrow middle-to-late layer band that regulates evidence sufficiency and abstention behavior. To ground these observations in causal circuitry, we introduce CRAFT, which localizes each failure mode to a minimal causal head set via dual criteria and verifies necessity and sufficiency through temporal probes and Tuned Lens trajectory analysis. Excising arbitration heads sharply reduces conflict following with negligible degradation on clean inputs, while excising brake heads restores appropriate abstention under degraded visual evidence. The two interventions target spatially disjoint head sets and produce distinct corrective effects, underscoring the mechanistic separability of the failure modes. Experiments across multiple medical VQA benchmarks and VLM architectures validate both the localization and interventions, demonstrating that the identified heads causally drive each failure mode and that targeted modulation generalises without retraining. The code is available at GitHub repository.

---


### 132. [Can Terminal Agents Trust Their Own Verification? Diagnosing and Improving Self-Verification](https://arxiv.org/abs/2609.38812)

**<font color=#1a73e8>作者：</font>** Yingfeng Luo, Shaowei Wei, Daixin Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Terminal agents rely on self-verification to assess and correct their solutions as they solve tasks through interaction with command-line environments. Yet how trustworthy such self-verification is remains poorly understood. To investigate this question systematically, we introduce a diagnostic framework that identifies the first complete solution in each trajectory, determines whether it is objectively correct, and uses this ground truth to quantify the agent's subsequent verification and recovery behavior. Applying it to ten terminal agents on TerminalBench2.1, we find that verification is nearly universal after a complete candidate is formed, yet only 61.43\% of incorrect candidates are detected and only 49.36\% of detected errors are successfully repaired. These results show that the main weakness in self-verification lies not in initiating verification, but in detecting and repairing errors. Motivated by these findings, we propose Student-Conditioned Verification Distillation (SCVD), which lets the student first produce a candidate solution and distills a stronger teacher's subsequent verification and recovery from the same interaction context. Across three Qwen3.5 backbones, SCVD improves \textsc{Pass@1} on TerminalBench2.1 by 9.74--16.85 percentage points over the corresponding base models and by 4.49--8.61 points over the standard full-trajectory distillation, while avoiding the pronounced out-of-distribution degradation of full-trajectory distillation on SWE-bench Verified.

---


### 133. [You're Hired: Strategic Model Selection for LLM Collaboration](https://arxiv.org/abs/2609.38816)

**<font color=#1a73e8>作者：</font>** Zongwan Cao, Ziyuan Yang, Shangbin Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While multi-agent and model collaboration algorithms gain traction to combine the strengths of diverse Large Language Models (LLMs), existing systems remain bottlenecked on pre-defined and hand-crafted model pools. In this work, we investigate the problem of model selection in multi-LLM systems. We propose and systematically evaluate a taxonomy of 9 selection algorithms ranging from diversity of model descriptions, capability-aware behavioral diversity, and LLM-based recruiters. We conduct extensive experiments across two candidate pools of 10 and 32 models, deployed in four model collaboration algorithms, and evaluated across tasks spanning math, coding, QA, and reasoning. Results demonstrate that successful selection algorithms greatly outperform random or heuristics-based teams such as merely selecting the models with top individual performance, by up to 36.1% across settings. Specifically, capability- and training-based selection strategies alleviate selection variance and achieve the best performance, which we recommend to employ before deploying real-world multi-LLM systems. Further analysis reveals that larger candidate pools pose greater challenges to shallow selection heuristics, while algorithms grounded in interacting with candidate models and understanding model capability robustly filter out misaligned, unsafe models, as well as generalizing to novel, out-of-distribution tasks. Together, we establish that principled and informed team selection is critical and present strong model selection algorithms for assembling effective multi-LLM systems.

---


### 134. [Whose Voice Survives the Summary? A Voice-Retention Audit of LLM Employee Listening](https://arxiv.org/abs/2609.38818)

**<font color=#1a73e8>作者：</font>** Thilo Tamme, Anton Hantel, Bijan Khosrawi-Rad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizations increasingly route employee feedback to leaders through large language model (LLM) summaries, an unaudited layer that silences already-spoken voice. We introduce a Voice Retention / Representation Ratio metric for representational bias in summarization and apply it to a bilingual (English/German) corpus of 2,586 free-text responses from a global professional service company. First, employees supply criticism more reliably than praise (withholding praise is 82 times more common). Second, across 45 leader-summaries the pipeline filters by popularity, not sentiment: criticism survives, yet a concern voiced once is dropped 86% of the time, with short and German-only content lost on the same axis (theme retention 0.14 vs 0.74; German directional). Controlling for frequency, sentiment has no independent effect; the harm is prevalence-driven, which sentiment-only audits miss. A targeted prompt recovers only named themes. We contribute the metric, field evidence, and a disaggregated voice-retention card.

---


### 135. [BARRAC: Adaptation of an English Aspect-based Sentiment Analysis Approach for Classification Tasks in Arabic Dialects](https://arxiv.org/abs/2609.38820)

**<font color=#1a73e8>作者：</font>** Ali Almutairi, Gelareh Mohammadi, Imran Razzak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rapid growth of Arabic NLP, several models, datasets and benchmarks have been reported. This paper asks whether approaches developed for majority languages like English can be adapted to Arabic tasks. We adapt an English aspect-based sentiment analysis framework to Arabic classification tasks and present the adaptation as BARRAC: Brainstorming Alignment and Replaced Representation learning for ArabiC tasks. BARRAC replaces consumer-review attribute pools with Arabic linguistic devices and markers for dialectal sentiment, sarcasm, and dialect identification, and replaces noisy self-training with two-stage training. Evaluated on five Arabic dialect datasets, BARRAC achieves a mean macro-F1 of 63.93\%, outperforming the best few-label SOTA by 3\%, and outperforming GPT-4o on four out of five tasks. Error analysis provides insights into remaining challenges. These results demonstrate that adapting task-specific approaches is a promising direction for Arabic NLP alongside adapting models, datasets and benchmarks.

---


### 136. [DecoMoE: Decoupling Visual Propagation and Expert Computation for Efficient Multimodal MoE Inference](https://arxiv.org/abs/2609.38823)

**<font color=#1a73e8>作者：</font>** Xudong Tan, Peng Ye, Ming Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal mixture-of-experts (MoE) models combine sparse expert activation with visual-language capabilities, yet their inference remains costly because long visual-token sequences repeatedly incur attention, routing, dispatch, and expert-MLP computation. Existing methods typically compress either the token or expert dimension, leaving redundancy along the other. Our analysis reveals two complementary regularities: the depth required for visual propagation varies across inputs, while text-token routing exhibits concentrated and recurrent expert-importance patterns. Based on these observations, we propose DecoMoE, a two-dimensional structured compression framework that decouples visual propagation from expert computation. The Sample-Adaptive Visual Boundary (SAVB) predicts an input-dependent visual-exit layer at which the visual-token block is removed. The Routing-Calibrated Expert Prefix (RCEP) reorders experts offline using text-token routed mass and, from this predicted exit layer onward, retains at each MoE layer the shortest contiguous prefix covering a target routed-mass fraction. We evaluate DecoMoE on Qwen3-VL-MoE and InternVL3.5-30B-A3B across six benchmarks. On Qwen3-VL-MoE, DecoMoE retains 97.91% of dense-baseline performance while reducing computation from 27.06 to 16.73 TFLOPs and latency from 0.44 to 0.26 seconds, yielding a 1.69x speedup. Code will be available at this https URL.

---


### 137. [Diversity Combining for Multi-Path LLM Reasoning](https://arxiv.org/abs/2609.38829)

**<font color=#1a73e8>作者：</font>** Guangsheng Yu, Litianyi Zhang, Qin Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-path reasoning methods such as self-consistency (SC) sample $K$ reasoning paths and choose the most frequent answer. However, their gains quickly plateau as $K$ increases, and existing methods do not predict when this saturation will occur. We formalize multi-path LLM reasoning as a diversity combining problem from wireless communications: each path is a noisy channel observation, and the pairwise correlation of path correctness caps the design-effect effective sample size of the vote at a finite ceiling. Generalized least squares (GLS) analysis shows that, under exchangeability, the optimal symmetric linear combiner of latent embeddings is uniform, supporting majority vote as the natural default in standard SC while leaving room for weighting or pruning under heterogeneous prompt-template branches. Across 5 models and 12 benchmarks, prompt-template diversity reduces path correlation in $55$ of $57$ valid cells, with the strongest effect on open-ended QA. We derive an Adaptive-K rule that uses a four-path pilot to select $K^*$, retaining $96$--$103\%$ of MV@$K{=}32$ accuracy across Math, QA, and NLU.

---


### 138. [Forging LLM Authorship Fingerprints with Targeted Rewriting](https://arxiv.org/abs/2609.38831)

**<font color=#1a73e8>作者：</font>** Haohan Yuan, Simin Chen, Xi Niu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model-attribution classifiers can often identify which language model produced a text, making model-specific writing patterns a signal of provenance. Accurate attribution on unmodified text, however, does not show whether the prediction still identifies the original source after deliberate rewriting. We formulate this problem as targeted fingerprint transfer: rewriting one model's output so that attribution classifiers assign it to a chosen target model. We study summarization, where different models receive the same document and express the same underlying content, providing a controlled setting for conditional generation. We introduce ForgePrint, a search-then-distil framework that first searches for rewrites that move attribution toward a target fingerprint, then distils the selected rewrites into a one-pass 4B Student model. On CNN/DM, the Student reaches 70.2% target success rate, outperforming both its Teacher (54.1%) and the strongest of six published rewriting baselines (39.3%), against held-out classifiers that are never queried by the attack. It also reaches 68.3% target success when transferring summaries from an open model toward chosen commercial models. These results show that fingerprint detectability should not be conflated with source authenticity, and that text-only attribution can provide misleading evidence of model identity under targeted rewriting, even when it is accurate on unmodified text.

---


### 139. [Scaling Parameter and Context in Attention: Native Sparse Attention from Mixture-of-Head](https://arxiv.org/abs/2609.38832)

**<font color=#1a73e8>作者：</font>** Zizhuo Fu, Runsheng Wang, Meng Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scaling attention parameters can improve language model quality, but retaining full token histories makes additional heads costly at long contexts. Furthermore, since attention retrieves and combines contextual information, parameter scaling should also support longer contexts. We therefore ask whether attention parameter scaling can directly enable efficient and effective context scaling. We introduce NAMOH, an architecture-native sparse attention mechanism that activates $K$ of $H$ heads per token. Each head retains only its assigned tokens and performs causal attention within this subsequence. Head selection thus jointly determines active parameters and available context without scanning the full history. Under balanced assignments, increasing $H$ at fixed $K$ shortens head histories and reduces per-token key-value (KV) access without increasing total KV storage. We further support head-relative rotary position embeddings to shorten positional spans within routed subsequences, aiming to mitigate position-induced attention noise. Experiments show that NAMOH can outperform fully activated models with the same total parameters, while enabling more efficient long-context inference than smaller dense models with matched active parameter counts. It remains compatible with GQA and existing sparse attention mechanisms. We hope this work offers a new path for scaling attention, with parameter scaling directly enabling context scaling.

---


### 140. [Scoring Higher, Answering Worse: Mitigating Reward Hacking in Rubric-Based RL via Protocol-Level Rubrics](https://arxiv.org/abs/2609.38847)

**<font color=#1a73e8>作者：</font>** Maoqi Liu, Junwei He, Bowen Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning (Rubric-RL) trains language models where no verifier exists. A judge checks each criterion of a rubric, and the verdicts are aggregated into a reward, most often by a weighted sum. We show that this additive aggregation is the weak point. Under a sum, criteria compensate for one another: a policy that misses the one decision that matters can buy the points back with advice nobody asked for. On clinical consultation, such a policy scores higher and answers worse. Rubric coverage rises while appropriateness on held-out physician criteria falls below the untrained model. The medical criteria are not to blame. Grouped so that they must hold together, the same criteria, unchanged to the word, recover a third of the loss; shorter answers recover almost none. We therefore propose Protocol-level Rubrics (ProRubric), which keeps what the criteria ask for and changes how they are aggregated. It groups a checklist into a few protocol-level dimensions. A dimension counts only when all of its criteria hold and its failure clause does not fire. The grouping is done once, offline, and leaves the optimizer unchanged. ProRubric raises appropriateness by 10.8 points without losing coverage and has the best seven-benchmark average at both scales. Reward validity is set not only by what a rubric verifies, but by how it aggregates. Code is available at this https URL

---


### 141. [OpenJev-RLCD: A Working RLCD Implementation](https://arxiv.org/abs/2609.38850)

**<font color=#1a73e8>作者：</font>** Zhimin Gao, Pichao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models such as Jev answer questions with probabilities, which are only useful if they are calibrated. Open-source reproductions rely on supervised fine-tuning plus temperature scaling, while reinforcement learning from verifiable rewards (RLVR) makes reasoning models overconfident. We present a working implementation of reinforcement learning for calibrated decisions (RLCD) for reasoning models: the model samples a rationale, and we score the answer distribution it commits to afterwards with a strictly proper scoring rule. A variance identity shows that scoring the mixture of several samples rewards disagreeing rationales, and that RLVR is exactly this mixture objective without its diversity term. Optimized naively, the per-rationale objective either switches reasoning off or is drowned out by policy-gradient noise, which leads to a two-stage recipe: calibrate, then reinforce. With Qwen3-1.7B on two reasoning tasks (3 seeds, paired tests), RLCD matches or beats SFT, RFT/STaR and GRPO (each temperature-scaled) in accuracy and beats all of them in selective prediction; on GSM8K answer verification a single query decides \gvTwoCovFive\% of the items at $\le$5\% error, versus \gvGrpoCovFive\% for GRPO. When uncertainty comes from annotator disagreement, RLCD provably cannot beat cross-entropy. Code and results: this https URL.

---


### 142. [Where MLLMs Fail and Why: Causal Task Decomposition for Capability Failure Diagnosis](https://arxiv.org/abs/2609.38851)

**<font color=#1a73e8>作者：</font>** Xia Hu, Brian Potetz, Chun-Ta Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> End-to-end accuracy on compositional tasks records how often MLLMs fail, but cannot distinguish whether a failure reflects an intrinsic deficit in the targeted capability or a cascading error from an upstream prerequisite. We propose a causal decomposition framework that isolates these two failure modes through controlled interventions on the prerequisite dependencies of each task. Our capability metrics (NC, IC, RC) score each task under unassisted, correct, or incorrect prerequisites to diagnose where failures arise; contribution metrics (N-Score, S-Score), adapted from probabilities of causation, quantify each prerequisite's necessity and sufficiency to determine why. We instantiate the framework in CADET, a diagnostic benchmark of 10 composite tasks decomposed into 46 unit tasks with over 33,000 human-annotated questions spanning perception, spatial, temporal, and cognitive categories. Diagnosing frontier MLLMs with our framework uncovers systematic patterns that end-to-end accuracy obscures. Capability-wise, supplying correct prerequisites eliminates 54\% of errors on cognitive tasks, lifting them from weakest to above spatial and temporal. Prerequisite-wise, causal contributions are concentrated in a few critical prerequisites, and supplying the single most important one alone captures 84\% of the gain from supplying all prerequisites.

---


### 143. [Optimal Design for Active Preference Learning with Biased LLM Judges](https://arxiv.org/abs/2609.38860)

**<font color=#1a73e8>作者：</font>** Zhongman Du, Huiming Zhang, Haodong Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from human preferences is central to large language model (LLM) alignment, but human preference annotation is costly. Active preference learning reduces this cost by selecting informative comparisons, and LLM judges can provide additional scalable feedback. However, the preferences of the judges may deviate from those of the target human population. Even after calibration on trusted reference data, active acquisition can shift the comparison distribution and expose residual judge bias. We therefore incorporate judge deviations into the acquisition design rather than relying on a separate calibration stage. Under joint estimation, comparisons that appear highly informative about the reward may also reflect judge bias and therefore provide less information about human preferences. To address this issue, we propose Nuisance-Adjusted Optimal Design (NAOD), a comparison-selection strategy that prioritizes policy-relevant target information after nuisance adjustment and uses the Frank-Wolfe algorithm for optimization. Theoretically, we establish a sharp conditional local asymptotic minimax lower bound on policy risk and construct an estimator that attains it. We further characterize the finite-sample cost of learning the nuisance representation and show that representation error can reverse an oracle design advantage. Finally, we validate these predictions experimentally and evaluate NAOD on Chatbot Arena data across 17 judges, 15 budget configurations, and 15 random cluster-level splits. NAOD reduces the mean regret of proxy policy by 29.1% relative to a matched target-information design, outperforms existing methods, and improves human-preference prediction on held-out data.

---


### 144. [When Context Changes: Understanding Update Failures in LLMs](https://arxiv.org/abs/2609.38866)

**<font color=#1a73e8>作者：</font>** Junyu Guo, Yuchen Fang, Shangding Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As preferences, goals, and facts change, LLM agents must use the current state while earlier versions remain in context. Yet they can answer with an old value of the same variable, a failure that we call stale binding. To study when models use outdated information and why, we introduce Controlled In-Context Memory (CICM), a benchmark for tracking and using updated information in conversations and agent logs. We observe that even frontier reasoning models can fail to recover the current state. We find that in open-source models probes can still recover the updated value when the model answers with an old one, pointing to a failure to select information that remains available. Component tests in Qwen and Pythia identify a mechanism for this selection failure: attention drift, where attention favors old values over the current one when producing an answer. We study a one-layer transformer to mathematically understand how this phenomenon happens: when attention scores are similar, several old values can together receive more attention than the current value. Guided by this explanation, we redirect attention toward the current value without further training. When the current value is requested directly, adjusting this intervention for each input corrects most old-value errors across various model families while preserving nearly all initially correct answers. Reliable context management therefore requires more than remembering updated information: models must use it to guide their answers.

---


### 145. [Talk2Agent: Benchmarking Voice Interfaces for Text Agents](https://arxiv.org/abs/2609.38867)

**<font color=#1a73e8>作者：</font>** Terumi Chiba, Guangzhi Sun, Zheqi Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) computer-use agents are typically evaluated with clean written instructions, despite speech being an increasingly popular interface for interacting with such systems. Speech input introduces an additional failure point: transcription errors can alter task-critical entities, constraints, or targets before the agent begins reasoning, while conventional ASR metrics do not directly measure whether the information required for successful execution has been preserved. We introduce Talk2Agent, a benchmark for evaluating how effectively voice interfaces convey human-spoken instructions to LLM-based computer-use agents. Talk2Agent builds human-spoken versions of tasks from WildClawBench and OSWorld and evaluates a range of voice interfaces, including dedicated ASR models, audio-capable LLMs, contextual biasing, and LLM-based ontology repair. Because repeatedly executing long-horizon computer-use tasks is costly and stochastic, we further propose an execution-free, task-conditioned evaluation framework that projects the original task grader onto prompt-addressable intentions and measures how much task-relevant information is retained after the voice interface. On WildClawBench, Talk2Agent's execution-free native projection provides a practical, execution-grounded measure of voice-interface quality, correlating with downstream task completion and improving Pearson correlation by 0.246 over WER/CER on 32 hours of real human speech.

---


### 146. [Reasoning Externalization for Faithful Large Language Model Narratives of Stock Return Predictions](https://arxiv.org/abs/2609.38869)

**<font color=#1a73e8>作者：</font>** Sujung Kim, Seung Hwan Cho, Sangjin Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In finance, interpreting machine learning predictions is essential, yet the numerical outputs of explainable AI can be difficult for non-experts to understand. While large language models (LLMs) can translate these outputs into natural language, they may produce errors when inferring numerical changes and feature relations. We propose an LLM narrative framework for cross-sectional stock return prediction that combines temporal Shapley additive explanations (SHAP) evidence with historical regime analogs. Temporal evidence tracks changes in the normalized global SHAP importance of an XGBoost model over six months. Historical analogs are past periods with similar changes in SHAP importance, their model performance and subsequent market returns are provided as comparative context. Using this framework, we conduct a controlled study of progressive reasoning externalization, sequentially providing raw SHAP sequences, deterministic temporal descriptors, and feature relations. Each generated claim is verified against provenance-linked evidence. Across Qwen3, externalizing numerical and relational reasoning improved evidence faithfulness as well as temporal and relational accuracy. Evidence faithfulness increased from 0.696 to 0.996 for Qwen3-32B-Instruct. While historical analogs did not improve structured automatic faithfulness, they received higher human-rated usefulness scores. These results suggest that externalizing verifiable reasoning enhances narrative faithfulness and that historical context adds interpretive value.

---


### 147. [Does Learning Protein Folding Generalize to Broader Reasoning?](https://arxiv.org/abs/2609.38879)

**<font color=#1a73e8>作者：</font>** Yong Liu, Zhanpeng Shi, Yizhou Dang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models rely heavily on human text, which often conveys surface answers rather than the spatial and structural logic behind them. Protein folding is a natural testbed, because one solved structure yields thousands of exactly checkable spatial and topological statements. We ask: can learning to fold proteins teach general models reusable reasoning capabilities? To answer this, we build FoldingCorpus, a protein-derived question-answer dataset, and Fold2Reason, a recipe that post-trains on it through two complementary signals: discrete structural answers predicted via the model's native language head, and continuous 3D geometry decoded from the same shared representations. On FoldBench, Fold2Reason achieves structure prediction scores 2.7 to 3.5 times those of Qwen3.5-9B. Beyond protein structure prediction, it improves performance on all 10 benchmarks spanning spatial, graph, scientific, and general reasoning, raising macro-average accuracy from 45.09% to 48.33% (+3.23 pp), with positive gains on all 10 benchmarks, while matched controls built from random, synthetic, and shuffled structure yield substantially smaller or negative gains. Our work shows that non-linguistic, structure-dense scientific data can systematically improve broad reasoning in language models, making a solved scientific problem a practical source of post-training supervision.

---


### 148. [STRATA: Self-Learning Through Role-Aligned Tiered Agents for Real-Time Strategy Games](https://arxiv.org/abs/2609.38881)

**<font color=#1a73e8>作者：</font>** Xinhe Tian, Xiaoyue Zhang, Ziyou Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-time strategy (RTS) games require agents to coordinate economic development, production and construction, base defense, unit organization, and attack timing over long matches. Existing studies have applied large language models to command decision-making in RTS games, enabling agents to read textual game states and generate high-level plans. However, long inference latency can cause them to miss critical tactical events. The complexity and tactical diversity of full RTS matches also leave existing systems heavily dependent on manually written experience-based prompts, with limited ability to learn continuously from past games. We present STRATA, a role-aligned hierarchical system with cross-game self-learning for Red Alert. STRATA assigns in-game strategic, logistical, and tactical decisions to a Strategic Agent (SA), Logistics Agent (LA), and Tactical Agent (TA), respectively. The SA generates high-level directives based on the global game state and relevant experience cards, while the LA and TA handle logistics and tactical execution. After each match, a Review Agent (RA) derives candidate experience from game traces, validates and revises it using evidence from subsequent matches, and compresses strategic experience supported across multiple games into concise experience cards for SA retrieval. We evaluate STRATA through the formation of experience cards, full-match comparisons before and after learning, and experience learning against AI opponents with different play styles. Under a fixed scenario, using the learned experience cards increases the observed win rate from 30% to 100%. Sequential learning against AI opponents with different play styles also produces distinct long-term strategic experience.

---


### 149. [Right Answers, Costly Models: The Efficiency Gap in LLM-based Optimization Modeling](https://arxiv.org/abs/2609.38884)

**<font color=#1a73e8>作者：</font>** Zhong Li, Xin Huang, Jinhui Wan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization modeling formulates real-world decision problems as mathematical programs that solvers can use to find optimal decisions. Large language models (LLMs) can automate this process, but the resulting correct formulations can require substantial time and memory to construct and solve, limiting practical scalability. Therefore, we systematically investigate whether LLMs can identify problem structure from natural-language descriptions and apply suitable optimization modeling techniques to generate mathematical models and solver code that solve the problems correctly and efficiently. To this end, we first curate OptTips, a knowledge base of 50 expert modeling techniques in eight families. Using this knowledge, we develop OptDachshund, a multi-agent framework that transforms problems from existing optimization benchmarks into new tasks for evaluating LLMs' use of modeling techniques. It constructs conventional and expert mathematical models with solver code for the same task and data, providing baselines for correctness and computational cost. The resulting EfficientOpt benchmark contains 561 expert-reviewed tasks with paired reference implementations. Evaluation of 11 representative LLMs reveals an efficiency gap on correctly solved tasks with comparable measurements: for every LLM, most generated programs take longer to solve than their expert counterparts. Within the comparable reference-size subset, 57\% of programs with correct objective values and fewer variables and linear constraints have longer recorded solver times. Case studies show that different modeling techniques can achieve the same optimal value at similar recorded cost. Faster solving may not reduce execution time if the code takes longer to prepare data and build the model. LLM optimization modeling should therefore be evaluated for both correctness and computational efficiency.

---


### 150. [Consistent Plan-Act for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2609.38891)

**<font color=#1a73e8>作者：</font>** Heng-Zhuang Li, Yi-Kai Zhang, Yu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agentic tasks demand strong reasoning and efficient execution across successive interactions with dynamic environments. A common approach decouples high-level planning from low-level execution through separate planner and actor roles. To investigate coordination failures in these tasks, we prompt both agents for structured state assertions and compare their reports programmatically to detect explicit contradictions. Our analyses reveal systematic disagreement about the same task-relevant state facts, a phenomenon we term planner-actor state mismatch. We further find that providing agents with task-relevant state information reduces mismatch and improves coordination and task performance. Based on the systematic analysis of the state mismatch, we propose Consistent Plan-Act (ConPAct), which feeds detected contradictions back to both agents to form consistent state interpretations and fine-tunes them on curated consistent interactions for better coordination. ConPAct improves performance across various environments and model configurations, e.g., increasing MiniGrid success rate from 38.6% to 54.4% with GPT-5.6-sol/terra as planner and actor respectively, demonstrating that state consistency can guide both inference-time correction and coordination training.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-390](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
