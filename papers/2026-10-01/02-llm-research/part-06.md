# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 251. [SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging](https://arxiv.org/abs/2609.36982)

**<font color=#1a73e8>作者：</font>** Zhiwei Yang, Jiahua Yang, Huiru Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge concept tagging aims to assign specific concept or topic labels to educational content, which is essential for both educators and learners in traditional and online teaching practices. Recent work has explored large language models (LLMs) for this task, achieving promising performance. However, LLMs still struggle to select the correct concept from a large-scale candidate set due to the high dimensionality of the decision space. In this paper, we propose a novel three-stage Select-Reason-Judge (SRJudge) framework, which empowers LLMs with selective reasoning capability for fine-grained knowledge concept tagging. Specifically, the Selector in Stage 1 first narrows the candidate concepts to a top-K shortlist by fine-tuning a small language model (SLM), e.g., BERT, since the top-$K$ predictions hit the correct concept in most cases, thereby reducing the decision space of correct candidates. Next, the Stage 2 Reasoner employs a lightweight LLM for refined reasoning over the shortlisted candidates. It further integrates an improved reinforcement learning strategy with a dynamic task-specific reward function and a pruning mechanism to better align with human reasoning preferences. Finally, a larger LLM acts as a judger that evaluates the overall rationality of the reasoning process and its explanations to determine the final output. In addition, we construct two high-quality datasets for further validation, i.e., the biology dataset S_Bio and the physics dataset S_Phy. Experimental results demonstrate that our method consistently outperforms state-of-the-art baselines across benchmark datasets, verifying its effectiveness and superiority. Resources are available at: this https URL.

---


### 252. [OPFL: Optimistic Verification of Federated Learning via Empirical Boundary](https://arxiv.org/abs/2609.37011)

**<font color=#1a73e8>作者：</font>** Hongxu Su, Jianzhu Yao, Xuechao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning enables multiple clients to collaboratively train models without sharing their private data. However, the lack of visibility into local training makes it difficult to verify whether clients follow the prescribed training procedure or submit malicious updates, such as model poisoning. A natural approach is to replay client training for verification. However, privacy-preserving replay produces numerical results that cannot be directly matched with local client execution because the two run in different environments. We present OPFL, an optimistic verification framework for privacy-preserving federated learning. To protect data privacy, OPFL performs replay inside secure multi-party computation (MPC). Although gradients computed on MPC and local GPUs are not bitwise identical, we observe that their absolute differences are stable and bounded. OPFL therefore calibrates an empirical boundary offline and uses it to distinguish benign numerical deviations from malicious manipulation. To reduce the cost of expensive MPC replay, OPFL adopts optimistic verification by post auditing only sampled training steps. Experiments on LeNet, BERT, and Qwen show that the boundary generalizes across datasets, input lengths, and GPUs, while achieving $0$\% ASR against model poisoning and PGD-based attacks. On a LeNet workload, at $p=0.01$, OPFL is approximately $98.6\times$ faster than full MPC-based FL and $625.5\times$ faster than ZK-based approach.

---


### 253. [LatCom: Cross-Agent Latent Compression for Efficient Multi-Agent Collaboration](https://arxiv.org/abs/2609.37017)

**<font color=#1a73e8>作者：</font>** Shinan Zhang, Tao Zhang, Qihui Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MAS) increasingly use latent collaboration to avoid the information loss and repeated encoding-decoding overhead of natural-language communication. However, directly forwarding all sender latents makes the receiver-side context scale with both the number of agents and the reasoning length, increasing computation, memory usage, and collaboration latency. A natural solution is latent compression. But we find that cross-agent redundancy remains unresolved in existing latent compression approaches, which typically compress each sender independently and then concatenate the results. We propose LatCom, a cross-agent latent compression framework for efficient multi-agent latent collaboration. LatCom maps multiple sender latents into a fixed number of receiver-readable and task-relevant slots. Rather than reconstructing all sender hidden states, it optimizes the compressed latents for receiver-side task utility. LatCom trains the compressor in two stages: single-sender readability learning first establishes a latent interface interpretable by the frozen receiver, and multi-sender fusion learning then trains the compressor to fuse complementary evidence and remove redundancy across agents. Experiments on multiple benchmarks with Qwen3-4B show that LatCom achieves an average 2.46x inference speed-up over LatentMAS and reduces output token usage by 70.3% while maintaining comparable average accuracy.

---


### 254. [AnyAct: Universal Action for Self-Evolving Agents](https://arxiv.org/abs/2609.37025)

**<font color=#1a73e8>作者：</font>** Lingrui Xu, Yangqin Jiang, Jiachang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) advance, AI agents are increasingly deployed in open-world environments to tackle complex sequential tasks (e.g., document processing, cross-application collaboration), relying heavily on actions ranging from GUI operations to semantic APIs. However, three core challenges persist: the "scale dilemma" of massive tool ecosystems exceeding LLM context windows, the "non-stationarity" of tool quality due to updates or outages, and the "heterogeneity" of feedback formats (pixels, text, structured data) creating information silos. To address these, we propose AnyAct, a universal action layer that unifies available capabilities into a self-evolving action space, enabling agents to operate efficiently and reliably in large-scale, dynamic tool ecosystems. AnyAct's core design focuses on two objectives: constructing this action space via hierarchical progressive retrieval (filtering task-relevant actions) and test-time reliability evolution (pruning unreliable actions), and enabling reliability-aware action orchestration through a heterogeneous observation grounding module that unifies multi-modal feedback. Additionally, it defines a hybrid action space (primitive + semantic actions) and optimizes for a balance between task success rate and execution cost. Evaluations on LiveMCPBench and OSMCP (a new benchmark we developed for multi-granularity action collaboration) demonstrate state-of-the-art performance. AnyAct delivers substantial performance gains over baseline methods across various LLM base models on LiveMCPBench and improvements are particularly notable for models with constrained native capabilities. On OSMCP, it achieves 77.27% overall success with only 50 steps, which is half the steps required by most competitors.

---


### 255. [LongSpark: Efficient speculative decoding with a fixed-cost parallel drafter](https://arxiv.org/abs/2609.37029)

**<font color=#1a73e8>作者：</font>** Hao-Yuan He, Peng-Fei Liu, Si Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive inference by verifying multiple draft tokens in a single target forward pass. However, as the context grows, existing state-of-the-art drafters become increasingly expensive, eroding the very efficiency advantage they are designed to provide. We argue that this scaling is unnecessary. A standalone language model must grow with its prefix because it is solely responsible for every token it produces. A drafter, by contrast, only proposes candidates; the target catches and corrects every error before any token is committed. The drafter's decoding cost can therefore be made entirely independent of the prefix length. We introduce LongSpark, a block-diffusion drafter that achieves this by extracting fixed-size, multiscale views from the target's verification pass, thereby eliminating the need for a growing persistent state. Extensive evaluations demonstrate that LongSpark achieves state-of-the-art end-to-end efficiency across multiple model scales and realistic serving conditions. Notably, it delivers the lowest time-per-output-token on long-context tasks while reducing the drafter's context state by several orders of magnitude.

---


### 256. [Selecting The Most Informative Tokens in Natural Language Autoencoders](https://arxiv.org/abs/2609.37040)

**<font color=#1a73e8>作者：</font>** Federico Torrielli, Gianluca Barmina, Andrea Blasi Núñez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language autoencoders translate a language model's internal activations into readable explanations. Explaining every token position is costly. Which positions should an auditor inspect to understand a potential threat? We study this question across $4.7$ million explanations on prompt injection and concealment. We compare signals from model computation with a ranker trained only on chat structure. Chat structure usually selects more relevant explanations than the computational signals, without requiring a model forward pass for position selection. On three of four datasets, explaining just $5\%$ of positions retains nearly all of the success rate from explaining every position, where success means obtaining an explanation about the threat. The benefit varies with the audit task. We also show that pretrained verbalizers recover words that models have learned to conceal through fine-tuning, without additional verbalizer training. These results identify where auditors can concentrate explanation generation and show that useful explanations can extend beyond the model a verbalizer was trained to describe.

---


### 257. [Beam Search as Test-Time Self-Distillation via Counterfactual Contexts](https://arxiv.org/abs/2609.37041)

**<font color=#1a73e8>作者：</font>** Su Ee Tan, Xiaotong Ji, Rasul Tutunov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-Distillation Fine-Tuning (SDFT) enables a language model to act as its own teacher: by conditioning on a demonstration, the model produces an implicit reward via pointwise mutual information, which guides on-policy learning without external supervision. However, SDFT operates at training time: it requires gradient updates and access to expert demonstrations, making it inapplicable at inference. We propose test-time self-distillation, a decoding-time method that extracts a steering signal from the self-distillation framework without any parameter updates, reward models, or training data. Our key insight is that counterfactual contexts, i.e. fixed textual templates that hypothetically prime the model for excellent versus poor reasoning, can substitute for the demonstration. The log-odds ratio of a candidate answer under these two counterfactual conditions defines a new reward signal. We derive the optimal KL-regularized policy under this reward, which takes the form of a Gibbs reweighting of the base distribution. Crucially, this reweighting is global: it cannot be decomposed into independent per-token operations without ignoring future trajectory quality. We therefore approximate the target distribution via beam search. Experiments on mathematical reasoning (MATH500), code generation (HumanEval), and graduate-level science QA (GPQA) across multiple model scales show that test-time self-distillation improves over standard sampling, low temperature, beam search and power sampling baselines on average, demonstrating that the self-distillation principle can be operationalized at inference time.

---


### 258. [GleanVID: Complementary Token Selection for Efficient Video Large Language Models](https://arxiv.org/abs/2609.37042)

**<font color=#1a73e8>作者：</font>** Shuo Yang, Changbai Li, Rui Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (VideoLLMs) have achieved strong video understanding capabilities but incur substantial inference overhead due to the large number of visual tokens. Existing VideoLLM token compression methods largely rely on selection-independent scoring, overlooking cross-frame complementarity and consequently retaining redundant evidence across frames. Instead, we view video token selection as a progressive evidence accumulation process. It aims to retain visual evidence that is individually informative and collectively complementary under a limited token budget. Building on this insight, we introduce GleanVID, a training-free inference acceleration framework for VideoLLMs. Specifically, GleanVID first allocates the global token budget across frames according to temporal novelty and then selects tokens by jointly considering local representativeness and subspace complementarity, thereby preserving richer and less redundant visual evidence. Extensive experiments across diverse VideoLLMs and benchmarks demonstrate that GleanVID consistently achieves state-of-the-art performance. Notably, with only 25% of visual tokens, GleanVID preserves 98.6% of Qwen3-VL's original performance while reducing its prefill latency by 44.7%. On LLaVA-OV-7B, GleanVID at a 25% retention ratio even slightly surpasses the original model.

---


### 259. [Learning from Think-Mode Advantage via On-Policy Distillation](https://arxiv.org/abs/2609.37044)

**<font color=#1a73e8>作者：</font>** Wanqi Ren, Jianxiang Wang, Danxuan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Explicit intermediate reasoning gives large language models (LLMs) a stronger problem-solving mode. We study learning from this think-mode advantage via on-policy distillation (OPD). OPD preserves student-generated trajectories and provides dense token-level teacher targets at student-visited prefixes. Privileged reasoning is used during distillation rather than student inference. Uniform ThinkOPD, a natural think-enabled OPD baseline, conditions a fixed teacher on one shared think trace and uniformly distills every sibling student response. Although its prefixes are on-policy, the trace need not follow a route compatible with every complete response: the same privileged trace can induce different teacher-student discrepancies even when responses reach the same outcome. We summarize this interaction with trace-response divergence (TRD) and introduce ThinkOPD, which routes supervision at the response level by combining group-relative reward gain with a TRD-based compatibility proxy. Final response weights are normalized within each rollout group. Across mathematical reasoning and code generation, ThinkOPD outperforms Uniform ThinkOPD in both same-model settings and both cross-model teacher-student pairs, and it exceeds representative rationale and self-distillation baselines in a controlled comparison. Controlled interventions show that outcome benefit and the TRD-based proxy provide complementary routing signals in this setting. Think-enabled OPD provides a controlled setting for studying how teacher advantage becomes transferable along student responses.

---


### 260. [Speed in the Blind Spot: An Interpretability Analysis of Dynamic Perception in VLMs for Autonomous Driving](https://arxiv.org/abs/2609.37046)

**<font color=#1a73e8>作者：</font>** Katharina Winter, Stefan Englmeier, Fabian B. Flohr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models are increasingly used in autonomous-driving systems, yet their ability to recover dynamic physical state from visual input remains insufficiently characterized. We study velocity understanding as a controlled diagnostic across three tasks: surrounding-agent speed, current ego speed, and short-horizon future ego-speed proposal. On nuScenes, we evaluate open-weight general-purpose and PhysicalAI VLMs, together with the driving-oriented Alpamayo-1.5 Vision-Language-Action model, using multiple input and output formulations. We combine verbal evaluation with temporal perturbations, counterfactual ego-speed hints and linear probes of hidden representations. The tasks exhibit distinct failure modes. Surrounding-agent speed is weakly encoded in an agent-specific form, whereas current ego speed is often internally accessible but poorly verbalized: continuous probes achieve 4.7-5.8 km/h MAE compared with 10.2-16.8 km/h MAE for verbal outputs. Multiple frames provide inconsistent verbal gains to single frame inputs, and frame order is rarely exploited. Under non-optimized QLoRA, task-specific adaptation improves both task-relevant latent speed representations and verbal readout, but continuous surrounding-agent speed estimation remains weak, while most future-speed gains survive frame shuffling, indicating limited temporal grounding. Driving specialized Alpamayo-1.5 shows stronger latent representations for surrounding-agent and future ego speed, while current ego-speed decodability is comparable and substantial probe-verbal gaps remain. Thus, driving specialization can strengthen motion representations but does not guarantee stronger encoding across both scene and ego states or reliable readout. The results show that plausible planning outputs do not necessarily imply reliable recovery or temporal grounding of the underlying dynamic state.

---


### 261. [OmniRoute: Mapping Temporal Semantic Evidence to Audio-Visual Token Budgets for Efficient Omnimodal Large Language Models](https://arxiv.org/abs/2609.37052)

**<font color=#1a73e8>作者：</font>** Yuchen Deng, Zidang Cai, Feidiao Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnimodal large language models (Omni-LLMs) encode audio and visual streams into temporally interleaved token sequences for multimodal reasoning. However, processing long audio-visual token sequences incurs substantial prefill costs. Existing compression methods have made progress, but often overlook temporal changes in audio-visual semantic relevance. Motivated by temporal variation and local continuity, we propose OmniRoute, a training-free, two-stage compression framework. First, Temporal Evidence-Guided Budgeting (TEGB) derives chunk-wise modality preferences and initial leading-modality budgets from semantic relevance and local content variation. Second, Budget-Constrained Semantic Compression (BCSC) compresses the leading modality and then calibrates the follower's retention target using the actual retained fraction. For video, it combines spatiotemporal grouping with query-guided selection; for audio, it selects tokens based on encoder attention and query relevance, then merges residual tokens into context anchors under visual guidance. Experiments on four representative benchmarks demonstrate a better trade-off between inference efficiency and performance than competitive baselines. The code and interface will be released to facilitate further research.

---


### 262. [MatToolBench: Benchmarking Multimodal Agents in Real-World Materials Science Workflows](https://arxiv.org/abs/2609.37053)

**<font color=#1a73e8>作者：</font>** Mei Wu, Rui Xie, Runyu Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal GUI agents have achieved impressive results on general software benchmarks, yet their ability to operate professional scientific software remains largely unexplored. In materials science, sparse domain-specific web data, specialized interfaces, and tacit workflow conventions create blind spots that general-purpose pretraining cannot readily bridge. We present MatToolBench, the first real-environment benchmark for evaluating multimodal GUI agents on professional materials science software, comprising 204 tasks across 10 tools in three modalities: GUI operation, OriginPro scripting, and code-based database queries, all executed inside a Windows 11 VM. Each task is decomposed into fine-grained sub-criteria by domain experts, enabling interpretable partial-credit scoring; the GUI component of our multi-level evaluation pipeline achieves an average F1 of 0.98. For OriginPro figure-generation tasks, we further conduct a human-LLM agreement study to validate the use of a multimodal judge for secondary aesthetic assessment. Our experiments show that strong performance on general benchmarks does not transfer to professional scientific workflows, and that this gap is not a visual-grounding problem alone: failures arise from domain-specific operational knowledge, sparse pretraining coverage of scientific software, weak cross-tool artifact handoff, and critical states exposed only visually. Even the best model reaches only 25% success rate on GUI tasks and 45% on code tasks. MatToolBench therefore serves as a challenging diagnostic benchmark and real-environment testbed for data-scarce, knowledge-intensive scientific workflows.

---


### 263. [Spatial-OPSD: Self-Improving Spatial Reasoning via Label-Free Self-Distillation](https://arxiv.org/abs/2609.37055)

**<font color=#1a73e8>作者：</font>** Zhenyu Liu, Zhangquan Chen, Keyi Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) increasingly operate in embodied and spatially grounded settings, where accurate understanding of depth, viewpoint, and three-dimensional relations is essential. However, improving spatial reasoning typically relies on ground-truth answers, answer-derived rewards, or other forms of task-specific supervision. We introduce Spatial-OPSD, a label-free self-improvement framework that instead exploits spatial structure naturally available from perception and reconstruction tools. During training, a privileged teacher receives automatically obtainable spatial priors, such as depth, reconstructed 3D relations, and camera geometry, while the student observes only the original visual-language input. On trajectories sampled by the student itself, the teacher provides dense token-level supervision, allowing the student to internalize spatial knowledge without ground-truth answer labels or privileged information at inference time.
To extend this supervision beyond a single round, we adopt a round-wise recursive training scheme: the teacher remains frozen within each round to provide a stable learning target, and the improved student initializes both teacher and student in the next round, where privileged spatial priors re-establish an informative teacher--student asymmetry. This enables repeated self-improvement while avoiding a rapidly moving teacher during optimization. Across four VLM families, a single round of Spatial-OPSD consistently improves the five-benchmark average, while three rounds further push a strong spatially specialized model to the open-source frontier, achieving the highest average among the open models and the best results on three of five spatial reasoning benchmarks. Our code is available at this https URL.

---


### 264. [Message Passing Does More with Less for In-Context Learning on Graphs](https://arxiv.org/abs/2609.37057)

**<font color=#1a73e8>作者：</font>** Dooho Lee, Jinmo Lee, Minho Jeong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Achieving strong performance with graph neural networks (GNNs) typically requires training and hyperparameter tuning for each dataset, incurring repeated costs and effort. Graph in-context learning (ICL) avoids this by using a single pretrained model to predict unknown node labels directly from labeled context nodes. Existing approaches, however, rely on dense attention across nodes, making inference increasingly expensive as graphs grow. In this work, we present Ephris, a new graph in-context learner built on sparse message passing, scaling linearly with the number of node-feature entries and graph edges. Ephris is pretrained entirely on synthetic graphs generated from structural causal models with diverse graph structures and relational dynamics, exposing the model to varied dependencies among topology, features, and labels. We evaluate Ephris on 51 node-classification datasets against 15 extensively tuned GNNs and existing graph ICL methods under both high- and low-label train/validation/test splits. Across both settings, Ephris ranks first on all four aggregate measures: Elo, improvability, average rank, and accuracy. Its inference cost remains comparable to training a single GNN once, while being over 10 times faster than previous graph ICL models. Together, these results advance the performance-runtime Pareto frontier, demonstrating that strong graph ICL does not require dense attention. Code and model weights are available at this https URL.

---


### 265. [Beyond Compression: Diagnosing How Post-Training Changes Mathematical Reasoning](https://arxiv.org/abs/2609.37066)

**<font color=#1a73e8>作者：</font>** Hongyang Li, Yiming Zhu, Xiao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training is central to mathematical reasoning in modern large language models (LLMs), but endpoint pass@1 alone underidentifies what has changed. Gains may reflect newly reachable solutions, cheaper sampling of latent solutions, surface robustness, or memorisation. We compare three post-training paths under a common diagnostic readout: our sufficiently trained off-policy distillation trajectories, released Qwen3 off-policy-plus-on-policy distillation endpoints, and a released DeepSeek-Math endpoint trained with Group Relative Policy Optimisation (GRPO). Our probe uses cross-surface pass@K over verbatim prompts, paraphrases, numerical isomorphisms, and translations, plus consistency, distribution-shape, and verified supervised-fine-tuning (SFT) membership analyses. We find two regimes. On easier AMC problems, large-K ceilings are near saturation, so post-training mainly compresses sample cost. On harder AIME problems, post-training expands the large-K ceiling over the base model: sufficient off-policy distillation already raises this ceiling, Qwen3 released endpoints raise it further, and DeepSeek-Math GRPO does not dominate sufficient off-policy distillation at large K. English-dominant distillation improves non-English reasoning but preserves language-tier gaps. A controlled-overfit audit finds limited sensitivity in current SFT-membership probes. Compression is one regime of post-training, not a universal explanation.

---


### 266. [UnlearningSoup: Is Repeated Tuning Necessary for Large Language Model Unlearning?](https://arxiv.org/abs/2609.37076)

**<font color=#1a73e8>作者：</font>** Puning Yang, Qizhou Wang, Junchi Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models trained on vast corpora inherently risk memorizing harmful content that may later re-emerge in their outputs. To mitigate this issue, existing unlearning methods typically rely on training-based parameter updates, such as gradient ascent and its variants, to delete targeted content while preserving other knowledge. However, balancing the competing goals of forgetting and retention makes hyperparameter choices for these methods particularly difficult, often requiring repeated tuning to obtain a strong model that still leaves substantial room for improvement and transfers poorly across models and datasets. To address this challenge, we investigate whether unlearning runs exhibit exploitable structure in weight space, and observe that models from different runs still lie in a shared evaluation-performance basin. This suggests that stronger models may be recovered through an unlearning-tailored soup strategy, reducing the need for repeated tuning for further improvement or new settings. Motivated by this, we propose UnlearningSoup, a unified framework that provides two strategies: EfficientSoup uses binary-search-based interpolation to quickly discover a well-performing model in the early stage, where repeated tuning would otherwise make strong model selection costly. PerformanceSoup uses reweighted souping to efficiently unlock the remaining performance potential in the later stage, where repeated tuning becomes increasingly inefficient. Extensive experiments across diverse datasets and models show that UnlearningSoup delivers 2.4x to 3.3x efficiency gains in hyperparameter selection, while consistently improving performance across settings.

---


### 267. [Real2Gym: Building Gyms from Videos, Bringing Skills to Robots](https://arxiv.org/abs/2609.37089)

**<font color=#1a73e8>作者：</font>** Kerui Ren, Yingxiang Xu, Kaiwen Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world videos provide rich demonstrations of manipulation, but turning them into reusable robot skills requires visually aligned environments, executable physical interactions, and mechanisms for learning from experience. We introduce Real2Gym, an agentic Real2Sim2Real framework that turns human and robot demonstrations into interactive simulation gyms and brings skills acquired in simulation to physical robots. The Real2Sim module reconstructs editable scenes, aligns objects and cameras with the input, validates demonstrated or retargeted actions through native physics execution, and generates task-conditioned variations with action-feasibility checks. Within these environments, the agent generates executable code for manipulation stages, observes their outcomes, and distills successful attempts and failures into reusable task procedures, object-relative motions, and recovery strategies. Through a shared perception-and-control interface, these skills guide subsequent execution in simulation and on real robots, with motions adapted to current observations and no updates to the underlying model weights. Extensive evaluations demonstrate that Real2Gym enables high-fidelity simulation environment reconstruction, outperforming GPT-6 Astra Direct Mode by 16.7% in success rate with approximately 74.9% fewer policy-execution tokens across these environments, while exceeding it by 33.3% in physical robot execution success rate across four tasks on a real Franka robot.

---


### 268. [Task-Oriented Visual Feature Compression via Residual Vector Quantization for Device-Edge Multimodal Inference](https://arxiv.org/abs/2609.37090)

**<font color=#1a73e8>作者：</font>** Luning Pang, Cheng Yuan, Jiawei Shao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large multimodal models (LMMs) support diverse visual understanding and reasoning tasks but are often impractical to run entirely on resource-constrained devices. Device-edge co-inference reduces device computation, yet transmitting visual data over bandwidth-limited uplinks can introduce substantial delay. Task-oriented feature compression (TOFC) reduces the payload through feature aggregation and entropy coding. However, continuous-feature coding remains costly, and query-agnostic aggregation may discard task-relevant local evidence. We propose query-guided task-oriented feature compression (Q-TOFC) for device-edge multimodal inference. Q-TOFC employs residual vector quantization (RVQ) to encode each merged feature as a compact sequence of codebook indices, reducing its representation cost and allowing more features to be transmitted. It further incorporates query relevance into feature aggregation and uses a quantization error compensation adapter to mitigate the distortion introduced by discrete quantization. Experiments on seven multimodal benchmarks show that Q-TOFC reduces the visual payload by 53.6% relative to TOFC while maintaining comparable average normalized task performance. End-to-end latency evaluations further demonstrate lower latency under bandwidth-constrained uplinks.

---


### 269. [LLM-Based Multi-Agent Systems over Wireless Networks: A Joint Agent--Network Design Perspective](https://arxiv.org/abs/2609.37094)

**<font color=#1a73e8>作者：</font>** Chao Hu, Yuan Guo, Guanlin Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) evolve from standalone models into collaborative agents embedded in physical systems, their reasoning and execution are increasingly distributed across wireless edge nodes. In this setting, wireless networks are experiencing a paradigm shift from only providing data connectivity to supporting the multi-agent reasoning workflow itself. The task performance of such network-constrained LLM-based multi-agent systems (MASs) is jointly affected by the multi-agent reasoning dependencies as well as the underlying network connectivity and edge resources. This coupling gives rise to various technical challenges, including the metric misalignment and message redundancy, state inconsistency and topology mismatch, as well as resource limitation and trust discontinuity. To address these challenges, this article develops a novel joint agent--network design perspective that coordinates decisions on both sides of the system. Specifically, we present the joint design of agent--interaction scheduling and resource allocation, the message selection-transmission co-design, as well as the joint agent--network topology design and workload--resource allocation. Furthermore, we consider the network-verified provenance that is linked with agent-side information-flow control to constrain how received information affects subsequent operations. An illustrative vehicle-to-everything (V2X) case study shows that jointly adapting agent-side interaction decisions and network operations improves task completion under communication and edge-resource constraints, outperforming the conventional agent-only and wireless-only separate designs.

---


### 270. [Why MLLMs Struggle to Count: Overcoming Individuation and Aggregation Bottlenecks with ConvStack](https://arxiv.org/abs/2609.37096)

**<font color=#1a73e8>作者：</font>** Liwei Che, Yihao Quan, Sen Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) consistently struggle with fine-grained visual counting, yet the underlying causes remain poorly understood. In this work, we present a mechanistic analysis of this failure mode, identifying two critical bottlenecks inherent to the global attention pipeline of MLLMs. First, we reveal an individuation bottleneck stemming from image patchification: because Vision Transformers process patches independently, they struggle to group fragmented geometric features across boundaries into distinct object representations. Second, we identify a collapse in the subsequent counting aggregation process, where representation separation rapidly diminishes as numerosity increases due to attention compression. Identifying and formalizing these twin bottlenecks constitutes our first major contribution. To overcome them, we propose ConvStack, a lightweight architecture that operates directly in the visual token space to explicitly aggregate and inject local spatial structures via zero-initialized residual connections. By explicitly addressing the individuation bottleneck, ConvStack provides unambiguous geometric evidence for downstream aggregation. Remarkably, by fine-tuning exclusively on counting tasks, the model achieves substantial improvements in dense object counting and broader spatial understanding benchmarks, without compromising on general visual capabilities.

---


### 271. [Breaking the Illusion of Review Reliability under Static Evaluation: SCOPE Fuzzing for LLM-based Scientific Reviewers](https://arxiv.org/abs/2609.37097)

**<font color=#1a73e8>作者：</font>** Zhuo Chen, Hao Zeng, Jiawei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid growth of submissions and reviewing workload has accelerated the use of large language models (LLMs) in peer review. Prior studies suggest that LLM-based reviewers can penalize content perturbations, such as overclaiming, indicating a certain degree of reliability. Yet these conclusions are largely based on a narrow set of perturbation strategies instantiated with static templates, providing limited evidence of actual reliability. In this paper, we construct a three-level evaluation framework covering perturbations to surface presentation, argumentative logic, and value judgment. Experiments on representative LLM-based reviewers reveal two limitations of static evaluation: stratified vulnerability, where perturbation effects depend on whether the paper's original review score is high or low, and perturbation undercoverage, where a single template misses vulnerabilities exposed by diverse realizations. To address these limitations, we propose SCOPE-Fuzzer, a strategy-aware fuzzer that combines feedback-driven strategy selection with adaptive mutation of paper content. By iteratively probing reviewers with dynamic perturbations, SCOPE-Fuzzer consistently uncovers vulnerabilities overlooked by static evaluation and other baselines.

---


### 272. [What Does Post-Training Change in Multilingual Reasoning?](https://arxiv.org/abs/2609.37104)

**<font color=#1a73e8>作者：</font>** Hongyang Li, Xiao Li, Caesar Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-source reasoning models provide unequal access to reasoning capability across languages. When a model can solve a problem but cannot deliver a complete solution in the user's language, language becomes an access barrier rather than merely a source of performance variation. We audit Qwen3 checkpoints on competition-mathematics tasks in eleven languages. Across the ten non-English languages, only 15.4-17.9% of problems receive a correct, terminating solution with visible reasoning in the requested language in any of 16 samples, compared with 92.9% in English. To identify the source of this disparity, we evaluate thirteen endpoints from one model family, spanning released checkpoints, multilingual supervised fine-tuning (SFT) at two scales, controlled SFT ablations, and three reinforcement-learning (RL) reward formulations. We jointly track correctness, language adherence, termination, and delivery efficiency. The dominant bottleneck shifts across post-training stages. Released models often reason in English. Multilingual SFT restores target-language reasoning, but accuracy declines across multilingual, English-only, and single-language SFT runs, showing that this cost is not specific to multilingual mixing; non-English reasoning traces additionally become prone to non-terminating loops. RL restores termination in both arms at no cost in accuracy, but only the arm whose reward includes a language term delivers: rewarding correctness alone returns the model to English. Together, these stages establish a constructive post-training path from English-pivoted capability to multilingual reasoning that is reliably delivered.

---


### 273. [VACE: Validation-Gated Alternating Co-Evolution of Agent Models and Harnesses](https://arxiv.org/abs/2609.37105)

**<font color=#1a73e8>作者：</font>** Jiexing Qi, Yu He, Jun Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language model agents can be improved by updating their model weights or refining the harness that guides task execution. These components are coupled: weight updates change how the model uses the harness, while harness updates change the trajectories used for training. We propose VACE, Validation-Gated Alternating CoEvolution, which alternates agentic reinforcement learning with trajectory-driven harness refinement. After each RL stage, VACE reuses the collected trajectories to propose a harness revision and evaluates the incumbent and candidate with the updated model held fixed. The candidate guides subsequent training only if it improves validation performance. With Qwen3.5-9B, VACE achieves 45.26% test accuracy on OfficeQA and a mean partial-credit score of 75.19% on AutomationBench, exceeding weight-only RL by 6.43 and 9.09 percentage points and ungated alternation by 4.59 and 6.95 points, respectively. Across 44 harness proposals, 17 reduce validation performance at the updated checkpoint and are rejected before subsequent RL training, highlighting the importance of validation gating.

---


### 274. [Learning from Viable Failure Prefixes: Milestone Viability Potential Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.37111)

**<font color=#1a73e8>作者：</font>** Qi Zhou, Yuanfan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents require reinforcement learning methods that can assign credit to intermediate decisions under sparse and delayed rewards. Existing group-based methods such as GRPO and GiGPO alleviate this issue by comparing rollout returns or repeated anchor states, but they still fail when the compared returns have no variation. We identify this failure mode as zero-credit failure: during early training, many failed rollouts contain useful prefixes, yet existing methods assign them no task-discriminative advantage. To address this issue, we propose Milestone Viability Potential Policy Optimization (MVPO), a potential-routed policy optimization algorithm that learns from viable failure prefixes. MVPO estimates prefix potential over Union-Find viability regions, repairs zero-credit groups with potential-difference advantages, and attenuates the potential branch according to relative performance progress. Experiments with Qwen2.5-1.5B-Instruct show that MVPO outperforms eight strong baselines, including GRPO and GiGPO. Under the same training length, MVPO improves over the GiGPO baseline by +4.4 success points on ALFWorld and +5.3 on WebShop, while adding only 0.16%-0.20% advantage-construction overhead.

---


### 275. [Unlocking the Critic: Reward-Free Policy Optimization for LLM Post-Training](https://arxiv.org/abs/2609.37119)

**<font color=#1a73e8>作者：</font>** Hongyang Li, Xiao Li, Caesar Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent approaches to reinforcement learning (RL) post-training for large language models increasingly remove the critic to reduce training instability and memory overhead. Even where a critic is trained, it is discarded once training ends, although it has learned to predict outcomes. We revisit this trend and show that a pretrained critic's ability to predict future outcomes can make it a valuable asset for efficient long-horizon reasoning. First, we find that instability in critic-based RL for long chain-of-thought reasoning is largely an optimization artifact: keeping policy updates small and low in variance restores stable convergence. Second, a well-pretrained critic estimates the posterior probability of eventual success from later trajectory states and unfinished prefixes. Its predictions provide outcome-derived, dense, per-prefix learning signals that, during policy optimization, require neither completed rollouts, step-level annotations, nor external reward labels. Building on this insight, we introduce Reward-Free Policy Optimization (RFPO), which repurposes a single calibrated, frozen critic as a rollout-level reward, a value baseline for generalized advantage estimation, and a success forecaster for unfinished prefixes. We further show that binarizing the debiased score stops the policy from exploiting the critic's length bias. Binarized, RFPO matches supervised PPO without a single label in the training loop, while cutting compute and memory overhead. This makes RFPO well suited to long-horizon reasoning tasks, where outcomes arrive late and generation dominates cost: because rollouts can be rewarded before they finish, training no longer has to pay for waiting on every trajectory to complete. Our findings challenge the prevailing critic-free paradigm and establish critic-based, reward-free optimization as a scalable and computationally efficient path for LLM post-training.

---


### 276. [Cross-Linguistic Effects in Bilingual Phoneme BabyLMs](https://arxiv.org/abs/2609.37121)

**<font color=#1a73e8>作者：</font>** Nikitas Theodoropoulos, Maria Lymperaiou, Giorgos Filandrianos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-linguistic effects are a central topic in bilingual first-language acquisition. Artificial learners can help investigate L1-L2 interactions by enabling controlled comparisons across language combinations and learning conditions. Recent work explores this direction by training bilingual language models under developmentally plausible constraints. However, human and model learners still diverge in fundamental ways, with one major difference being input modality: children learn primarily from spoken input, whereas language models are typically trained on orthographic text. To reduce this gap, researchers have trained models on phonemic representations of speech. In this work, we combine these research directions to train bilingual BabyLMs with phonemic input. We keep English fixed as the L2 and vary the L1 across German, Swedish, Persian, and Basque, selected to represent contrasting combinations of syntactic and phoneme-inventory distance from English. Our results show stronger L1-related variation in grammatical learning trajectories under phonemic than orthographic input, while early lexical differences align with phoneme-inventory similarity.

---


### 277. [EviViT: Evidence-Adaptive Vision Transformers for Fine-Grained Perception](https://arxiv.org/abs/2609.37123)

**<font color=#1a73e8>作者：</font>** Yaoxin Niu, Zhangquan Chen, Yang Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained visual perception enables vision-language models to distinguish subtle attributes and ground their answers in visual evidence. In high-resolution scenes, processing the whole image at greater resolution spends visual tokens on irrelevant content, while isolated crops can lose the context needed to interpret the selected evidence. We introduce EviViT, a lightweight attachment that learns where a pretrained vision transformer should acquire detail. Human visual-search traces supervise a question-conditioned evidence density, which guides regional re-reading from the original pixels and the allocation of visual tokens. A sparse, coordinate-aware bridge then connects the regional features to the global scene, allowing the host to interpret precise evidence in context. Learned with the host backbone frozen, the attachment serves both the base model and compatible post-trained descendants without refitting. Experiments across nine hosts show consistent gains in average fine-grained accuracy. Matched-budget comparisons further show that EviViT outperforms global-only processing at every tested token ceiling while using fewer visual tokens.

---


### 278. [LLM unbranding: Erasing Commercial Identity while Preserving Generic Utility](https://arxiv.org/abs/2609.37127)

**<font color=#1a73e8>作者：</font>** Kajetan Ożóg, Alicja Wojciechowska, Dawid Malarz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Establishing unbranding as a critical practice to prevent visual logos from acquiring negative connotations is standard in image generation. Large Language Models (LLMs) now face a parallel and emerging challenge. These models frequently generate brand descriptions within diverse contexts. This frequency introduces significant risks, such as trademark dilution, false attribution, and brand defamation. In response, we formally define the novel task of LLM Unbranding. We specifically address the complex challenge of managing trade dress within textual outputs. This involves neutralizing characteristic language, slogans, and stylistic markers that define brand identity. Crucially, these elements are less evident than explicit visual logos. To benchmark this task, we introduce a comprehensive evaluation dataset incorporating prominent brands from multiple commercial domains. We rigorously evaluate existing state-of-the-art machine unlearning models using this benchmark. This evaluation identifies their limitations in selective textual unbranding. Finally, we propose MUTE, a novel inference-time method that effectively neutralizes textual trade dress while preserving the LLM's general capabilities and utility. By leveraging an iterative refinement loop, MUTE systematically optimizes system instructions to safely eliminate brand leakage without requiring fragile parameter updates.
Code and dataset: The evaluation dataset and code for LLM Unbranding are available at this https URL. The implementation of MUTE is available at this https URL.

---


### 279. [SkillCome: Group Contrast Skill Optimization with Dual Memory](https://arxiv.org/abs/2609.37128)

**<font color=#1a73e8>作者：</font>** Haolin Li, Feng Hong, Ang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill evolution improves the capabilities of large language models by analyzing trajectories generated under a given skill and modifying the skill accordingly. Existing approaches typically generate a single trajectory per question. However, this provides insufficient optimization signals since it requires inferring effective skill edits from a solitary path. It is difficult to pinpoint which actions caused the failure in a failed trajectory, or to determine which actions in a successful one should be incorporated into the skill. Furthermore, they rely on a local batch of trajectories for analysis, making the optimization direction susceptible to noisy evidence. To address these, we propose SkillCome, a Skill-evolution method based on group Contrast optimization with dual memory. For each question, SkillCome generates trajectories and performs group contrast analysis to precisely identify key behavioral divergences between successful and failed trajectories, offering reliable optimization signals. The dual memory system further accumulates evidence from historical steps to track patterns shared across different groups, leading to more generalized optimization directions. Together, SkillCome builds a systematic optimization process that transforms experience from observed successful trajectories into reusable skills. Extensive experiments on six benchmarks spanning question answering, reasoning, and agentic tasks demonstrate the effectiveness of our method. SkillCome consistently outperforms baselines across five models of varying families and scales, with gains up to +5.69 points.

---


### 280. [Train Ahead, Distill Back: Bootstrapping On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2609.37132)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Xinyue Tan, Lufei Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) improves large language models by letting a self-teacher with privileged information provide dense token-level supervision on the model's own trajectories. Yet existing methods typically construct the self-teacher from the current, initial, or slowly averaged policy state, leaving the quality of supervision constrained by the teacher's ability to exploit privileged information. We ask whether the model's own optimization progress can instead be recycled into a stronger self-teacher. In this paper, we introduce Bootstrapped On-Policy Self-Distillation (B-OPSD), which temporarily trains the policy ahead to obtain a future teacher, restores the student to the original policy state, and then uses the future teacher to supervise the restarted student. The future teacher improves supervision in two complementary ways, it can generate more reliable privileged trajectories and, conditioned on them, provide more informative token-level targets along the restarted student's on-policy trajectories. Experiments on mathematical reasoning with Qwen3-4B and Qwen3-8B show consistent improvements over standard OPSD in both settings, including gains from 27.50 to 41.30 and from 48.80 to 64.44 in the rollout-privileged setting. Our findings point to a broader principle for self-improving models that future learning progress can be distilled backward, preserving acquired knowledge while bootstrapping beyond the optimization state that produced it.

---


### 281. [From Judgment Quality to Downstream Utility: Rethinking LLM-as-a-Judge for Open-Ended Tasks](https://arxiv.org/abs/2609.37145)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Lufei Li, Xinyue Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge is increasingly used to evaluate policy responses on open-ended tasks that lack ground-truth answers. Existing work often directly converts the resulting judgments into reward signals for policy training, paying limited attention to intrinsic judgment quality and largely restricting the use of Judges to training-time supervision. We systematically investigate judgment quality and downstream utility by examining both how judgments are elicited and how they are used. For judgment elicitation, we vary the Judge protocol along three dimensions: verdict granularity, critique usage, and evaluation batching. For judgment usage, beyond policy training, we extend Judge to test-time inference through Best-of-N selection, Judge-guided revision, and beam search. We find that, (i) Surprisingly, judgment quality and downstream utility do not always align. (ii) Judge protocol design substantially affects both intrinsic judgment quality and downstream utility. (iii) Judge guidance effectively converts test-time compute into performance gains, with benefits varying across inference strategies. Our results call for a multifaceted evaluation of LLM Judges on open-ended tasks, encompassing intrinsic judgment quality, and downstream utility.

---


### 282. [FlowMAS: Learning Multi-Agent Workflow Topology via Information-guided Generative Flow Network](https://arxiv.org/abs/2609.37151)

**<font color=#1a73e8>作者：</font>** Haitao Wang, Chenjing Liang, Haipeng Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Automated multi-agent systems offer clear advantages over manually designed ones in scalability and adaptability, but existing workflow topology methods still face important limitations. Search-based methods are often computationally expensive, textual-gradient-based methods rely on coarse-grained feedback, and existing generation-based methods are not well suited to discrete workflow topologies with complex dependencies. To address these limitations, we propose FlowMAS, a multi-agent workflow topology method based on Generative Flow Networks (GFlowNets). FlowMAS models workflow generation as reward-guided flow over the topology space and introduces three components: a GFlowNet-based topology generation backbone, a curiosity-driven module for structure-aware exploration, and an information-guided optimization module for evaluating intermediate topologies. Concretely, the curiosity-driven module encourages exploration of structurally novel workflows, while the information-guided module measures both the information contribution and the communication efficiency of different operators to favor more informative and effective collaboration patterns. Experiments on six benchmark datasets with three LLM backbones show that FlowMAS consistently outperforms multiple baselines.

---


### 283. [When Tools Silently Lie: Evaluating and Mitigating Blind Compliance in Tool-Augmented Data Agents](https://arxiv.org/abs/2609.37153)

**<font color=#1a73e8>作者：</font>** Zifu Tao, Changqing Yin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented data agents rely on tool outputs for analytical decisions. Yet successful execution can return plausible but incorrect evidence, requiring agents to decide whether to trust or verify it. Understanding this failure requires examining both the evidence obtained through checking and the answer ultimately adopted. We introduce ToxicBench to measure checking and adoption under numerical, label, schema, and retrieval errors, pairing clean and poisoned observations over fixed source data. In the 118-task GPT evaluation across three adapters, poisoning lowers task success by 26 to 39 percentage points. Ordinary retries help under one-shot poisoning, whereas repeated poisoning reveals wrong-answer adoption after checking. Controls on three public tables isolate how supplied evidence affects recovery. After freezing the scorer, we compare its judgments with human annotations on 200 trajectories, finding 96% task-success agreement. Human judgments support retry gains over Base and confirm adoption after checking on audited tasks. We release trajectories, versioned scoring, and reference and delivery audits. These findings highlight evidence availability and answer selection as complementary dimensions of agent reliability.

---


### 284. [From Learner Behavior to Reusable Skills for Effective and Efficient Learner Simulation](https://arxiv.org/abs/2609.37157)

**<font color=#1a73e8>作者：</font>** Zijian Chen, Zheng Zhang, Miao Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learner simulation aims to reproduce how a particular learner behaves on new tasks. Although Large Language Models (LLMs) can generate increasingly fine-grained learning behaviors, existing approaches often need to repeatedly process a growing interaction history to reconstruct the learner. This introduces additional context and inference costs and makes the acquired learner-specific simulation capability difficult to reuse across different LLMs. We therefore propose Learner2Skill, which externalizes the simulation capability acquired from historical interactions into a persistent and reusable Simulation Skill. The Skill captures the learner's current learning state and recurring response patterns, evolves as new real interactions arrive, and can be adapted to a new LLM through lightweight executor calibration without reconstructing the learner from scratch. Experiments show that Learner2Skill more faithfully reproduces fine-grained learner behavior while reducing overall token cost, and that the same constructed Skills can be effectively reused across different LLM executors.

---


### 285. [Trajectory Soup: Pushing the Compute-Scaling Frontier of LLM Mid-training via Diverse Trajectories](https://arxiv.org/abs/2609.37169)

**<font color=#1a73e8>作者：</font>** Zhehao Huang, Changxin Tian, Qingyuan Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mid-training equips pretrained large language models with specialized and reasoning capabilities, but the returns of this stage are bounded since additional serial compute yields little further downstream improvement and can even degrade some capabilities, which places a practical ceiling on how much compute mid-training absorbs. We revisit how this compute should be allocated to a single run or multiple similar optimizations. We find that branches forked from a shared checkpoint under various controlled recipe reaches measurably different regions of parameter space, and establish a form of compatible diversity that extending one run cannot supply. Therefore, we introduce Trajectory Soup, which distributes a mid-training budget over several independent branches, and consolidates strongest checkpoints selected on validation through intra- and inter-trajectory averaging into a single model. A local bias and variance analysis separates the two averaging levels, showing that inter-trajectory averaging removes residual error beyond the reach of averaging within a trajectory, while checkpoint selection carries a bias that bounds how many checkpoints are worth merging. Across model scales, learning-rate schedules, token budgets, and trajectory counts, Trajectory Soup improves aggregate downstream performance over the strongest single-trajectory average under matched budgets and keeps improving as budgets expand, with the advantage preserved after an identical post-training pipeline. These results position trajectory allocation and merging as a practical way to extend the compute-scaling frontier of mid-training beyond serial saturation.

---


### 286. [Interpolated Policy Distillation: A Controllable Continuum Between Off-Policy and On-Policy Distillation](https://arxiv.org/abs/2609.37170)

**<font color=#1a73e8>作者：</font>** Youxu Shi, Yifan Sun, Dacheng Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy and on-policy distillation have traditionally been formulated as separate paradigms, each favoring a different property of distillation trajectories. Teacher-generated (off-policy) traces are typically high-quality but lie far from the student's distribution, whereas student-generated (on-policy) rollouts are more learnable but often contain erroneous reasoning. We view these paradigms as the endpoints of a policy continuum and posit that a more effective rollout policy may lie in between. We introduce \textbf{Interpolated Policy Distillation (IPD)}, which defines the next-token distribution at every decoding step as an explicit linear interpolation between the student and teacher distributions. The interpolation operates at the distribution level, token by token, and its coefficient provides direct control over the balance between trajectory quality and student learnability. Naively sampling from this policy would require sequentially querying the teacher at every token and is thus expensive. To make IPD practical, we accelerate it with a new speculative-decoding rule while exactly preserving the interpolated next-token this http URL the trajectory level, the resulting rollouts naturally interleave student- and teacher-generated segments. Unlike recent heuristic segment-interleaving methods, however, this interleaving is induced by an exactly realized token-level interpolated policy rather than by hand-designed switching rules. Across text-only and multimodal reasoning benchmarks, IPD consistently outperforms both endpoint policies (SFT and OPD), their conventional two-stage combination (SFT-then-OPD), and recent heuristic segment-interleaving methods, demonstrating that token-level policy interpolation better balances trajectory quality and student learnability.

---


### 287. [Bridging Semantic Gaps in RAG through Generated Context Knowledge Fusion](https://arxiv.org/abs/2609.37171)

**<font color=#1a73e8>作者：</font>** Xinkai Du, Chao Lv, Yalin Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation has established itself as a fundamental framework in natural language processing, seamlessly integrating information retrieval with the generative capabilities of large language models. However, this process is fundamentally constrained by a critical challenge: semantic space mismatch between queries and retrieved contexts. We propose Knowledge-Aware Semantic Bridging (KASB), a novel framework that improves passage selection quality through semantic space alignment between queries and retrieved documents through intelligent knowledge fusion. Our approach leverages the complementary strengths of generative and retrieval-based knowledge through a multistage process that enhances both relevance and accuracy. We evaluate KASB on three popular open-domain Question Answering datasets to demonstrate the effectiveness of our approach.

---


### 288. [SimpleEvol: An Agent-Loop Framework for LLM-Driven Automated Heuristic Design with Minimal Human Priors](https://arxiv.org/abs/2609.37172)

**<font color=#1a73e8>作者：</font>** Jianghan Zhu, Cong Zhang, Rongjie Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have emerged as powerful tools for automated heuristic design (AHD), enabling iterative generation and refinement of heuristics. However, the dominant paradigm embeds LLMs as narrow, fixed components, such as crossover or mutation, within heavily hand-engineered evolutionary frameworks. We argue this misapprehends LLMs. It treats them as specialized tools rather than general reasoners, constrains them to low-level operations, and underutilizes their autonomy. Moreover, the extensive human priors in these frameworks violate the bitter lesson principle that general methods scaling with computation surpass hand-crafted solutions. This raises a key question: which AHD framework designs best convert stronger LLM capabilities into better heuristics? To address this, we propose metrics for LLM-driven AHD framework handcraftedness (AHI) and intelligence conversion efficiency (ICE). Evaluating ten LLMs across three challenging combinatorial optimization problems, we obtain a notable finding that frameworks with fewer human priors consistently yield higher ICE. Based on this finding, we propose SimpleEvol, an agent-loop framework for AHD which removes nearly all human priors and allows the LLM to operate autonomously. SimpleEvol consistently achieves the highest ICE, often by a large margin. Our results challenge the trend toward complex AHD pipelines and point to a lighter and more model-centric alternative, suggesting that reducing human priors is a more effective strategy to scale up with model intelligence. The source code is available at this https URL.

---


### 289. [VLM Fine-Tuning for End-to-End Combinatorial Optimization](https://arxiv.org/abs/2609.37175)

**<font color=#1a73e8>作者：</font>** Qingsong Yan, Xia Jiang, Yaoxin Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have provided a unified interface for end-to-end combinatorial optimization (CO), but textual serialization alone may obscure spatial and relational structures that are important for generating effective CO solutions. This paper presents a general-purpose vision-language solver that augments textual instance descriptions with input-derived visual representations. A single vision-language model (VLM) is applied across different CO tasks and trained using supervised fine-tuning followed by verifier-guided reinforcement learning. While the visual inputs contain no gold solutions or solution-derived information, our experiments show that the VLM generally improves solution quality over its text-only counterpart, with particularly clear gains on more complex CO problems such as CVRP and JSSP. The advantage of visual information is more pronounced at large problem scales.

---


### 290. [Absorbed in Inertia: Activation Analysis for Computer-Use Agents](https://arxiv.org/abs/2609.37176)

**<font color=#1a73e8>作者：</font>** Giulio Segalini, Zhi Wen Soi, Jérémie Decouchant 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents have become increasingly capable of executing tasks on live desktops through natural-language instructions, based on trajectories of screenshots, actions, and reasoning. We discover that they can stealthily exhibit inertia, in which they repeat fruitless actions despite recognizing that these actions are ineffective. We hypothesize that inertia is reflected in the agent's internal state, i.e., the activation values of the agent's underlying model, and propose a protocol to measure the relationship between the two. Extensive analysis of high-dimensional activation states shows that inertia corresponds to an absorbing region of activation space, where activation values become stale across actions and even after attempts to steer them. We conjecture that drastically changing the agents' activations by re-initializing them is necessary to escape inertia. Specifically, we propose R$^3$ (Reset, Reroute, Restore), which temporarily resets the agent's context trajectory to escape the absorbing region and then restores the historical context to effectively complete the task. Our approach yields 17-55% lower measured inertia across models relative to unmodified agents. These results suggest that changing the context can interrupt recurrence more effectively than directly steering the resulting activations. Our code is available at this https URL

---


### 291. [Exploring In-Context Learning for Handwritten Text Recognition](https://arxiv.org/abs/2609.37195)

**<font color=#1a73e8>作者：</font>** Eric Ayllon, Abel Gandia, Jorge Calvo-Zaragoza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwritten Text Recognition (HTR) systems have become an indispensable tool for the digitization of historical documents. Not only do they cut down time and cost, but they also allow democratizing access and processing of their contents by generating their transcripts. However, literature in HTR currently focuses mostly on specialized models that require large amounts of annotated samples to achieve satisfactory performance.
We explore the use of In-Context Learning with pre-trained Vision-Language Models (VLMs) to create a transcription pipeline without updating the model's parameters. We then evaluate this pipeline across multiple collections and models, and demonstrate that general-purpose VLMs can be effectively taught how to transcribe handwritten text from images. To assess how our observations may translate to practical applications, we evaluate the performance in a Cross-Domain (CD) scenario, where context examples are drawn from a different collection than the query image.
Results in both the controlled In-Domain (ID) scenario and the realistic CD scenario follow the same patterns. First, as context size grows, the error range is expected to narrow towards the average performance. Thus, larger context sizes sacrifice the performance of the oracle-best sampling for lower expected error rates.
The results obtained show that, without any parameter updates, this methodology has strong potential to compete with traditional HTR in the presence of domain shift. Moreover, we show and argue that some context samplings work better than others and suggest more effort should be put into finding an ideal sampling method in future work.

---


### 292. [ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents](https://arxiv.org/abs/2609.37196)

**<font color=#1a73e8>作者：</font>** Yanjie Li, Xiangyu He, Xuelong Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents remain vulnerable to indirect prompt injection because trusted instructions and untrusted observations share one context, allowing malicious content to steer consequential input-filtering defenses. Multi-path consensus defenses still leave a high attack success rate because they examine content or aggregated outputs rather than authorizing effects, especially for the within-tool attack, which preserves the intended tool but manipulates its arguments. Data-Flow Control such as CaMeL provides stronger guarantees, but incurs substantial time latency that limits practical deployment. We introduce ToolFence, which compiles a typed authorization blueprint before execution, enforces it through a deterministic monitor, and when the blueprint is incomplete asks a judge to grant new capabilities rather than adjudicate each concrete call. ToolFence provides two key advantages. First, its fine-grained provenance-aware authorization enables the system to distinguish user-authorized values from untrusted observations, effectively addressing the within-tool attack. Second, its deterministic fast path and capability-level runtime grants substantially reduce the frequency of expensive judge calls, improving runtime efficiency. On AgentDojo with Qwen3-max, ToolFence reduces overall ASR to near zero with only a 3.80 percentage-point clean-utility drop and practical runtime overhead.

---


### 293. [Learning to Prove, Not Just to Answer: Reinforcement Learning from Formal Verification for Natural-Language Logical Reasoning](https://arxiv.org/abs/2609.37203)

**<font color=#1a73e8>作者：</font>** Qili Zhang, Qianren Mao, Hanze Cai 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed for natural-language logical reasoning, where the final answer is easy to check but the proof behind it is not. In natural-language logical reasoning, an intermediate conclusion should follow from its premises, and the resulting derivation should support the final answer. Existing methods lack machine-checkable verification of intermediate conclusions and answer-supporting proof dependencies, so they may assign credit to invalid or answer-irrelevant steps. We propose Proof-R1, an RL framework from formal verification that trains LLMs to construct verifiable proofs for natural-language logical reasoning. Proof-R1 admits a generated conclusion into the verified proof state only when the corresponding reasoning action satisfies the proof obligations through UNSAT-based machine-checkable formal verification. Proof-R1 also recovers the answer-supporting dependency closure to trace the proof structure of the final answer and align outcome credit with the proof dependencies. Experiments demonstrate that Proof-R1 improves answer accuracy across three logical reasoning benchmarks and four backbone models and outperforms training-free agents and training-based methods in terms of reasoning-process verifiability.

---


### 294. [OptiCom : A Unified Framework for State-Conditioned Composition in LLM-Driven Optimization](https://arxiv.org/abs/2609.37221)

**<font color=#1a73e8>作者：</font>** Chenxing Wei, Sichen Liu, Lizhao Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed to solve complex scientific and practical problems via iterative optimization. However, dynamically coordinating diverse search mechanisms as candidate quality, failure modes, and resource budgets evolve remains a critical open challenge. Targeted empirical diagnostics reveal that mechanism effectiveness is highly state-dependent. Motivated by this, we analyze how individual decisions drive final outcomes, decomposing the expected terminal improvement under a shared budget into cumulative decision opportunities minus cumulative selection losses. Guided by this opportunity-loss theoretical foundation, we propose OptiCom, a unified framework that represents LLM-driven optimizers within a shared configuration space: C=(A,Q,O,E,M,S), corresponding to artifact, query, operator, evaluation, memory, and strategy. Operating within this space, a fast LLM-based Optimization Controller dynamically composes immediate mechanisms through structured Action Packages, while a slower Strategy Adapter refines long-term selection preferences, operator weights, and templates based on accumulated trajectory feedback. Comprehensive evaluations across 32 benchmark groups demonstrate the superiority of framework: OptiCom achieves an average Max-score rank of 1.72 among 14 evaluated configurations, securing the top score in 23 groups. Ultimately, these results highlight the broad applicability and high extensibility of OptiCom as a general-purpose paradigm for robust LLM test-time scaling.

---


### 295. [ResComEmb: Effective and Efficient Multimodal Embedding via Residual Homogeneity Compression](https://arxiv.org/abs/2609.37225)

**<font color=#1a73e8>作者：</font>** Zijing Cai, Yuzhe Wang, Jingxian Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown strong potential for universal multimodal representation learning. However, existing methods either compress each input into a single vector, limiting fine-grained expressiveness, or retain long sequences of visual-token vectors, incurring substantial storage and interaction costs. To resolve this trade-off, we propose ResComEmb, a trainable framework for effective and efficient universal multi-vector multimodal embedding. ResComEmb first encodes each input at native dynamic resolution into ordered global, intermediate, and fine-grained views. After MLLM contextualization and embedding projection, a trainable Residual Homogeneity Compression (RHC) module reduces within-granularity redundancy and cross-granularity repetition under explicit visual token budgets. Then, ResComEmb introduces a length-adaptive Bidirectional Late-Interaction Matching mechanism for robust query-document scoring, which averages the strongest token-level matches in each direction and combines the two scores using a weight based on how many valid tokens each side has. Extensive experiments on MMEB, ViDoRe V1, and ViDoRe V2 show that ResComEmb produces higher-quality universal multimodal embeddings than VLM2Vec-V2, and outperforms ColQwen2.5 in visual document retrieval using only 37.5% of its full visual token budget, demonstrating a favorable effectiveness-efficiency trade-off.

---


### 296. [Follow the Entities: A Corpus Map for Agentic Search](https://arxiv.org/abs/2609.37226)

**<font color=#1a73e8>作者：</font>** Soyeong Jeong, Sujay Kumar Jauhar, Sung Ju Hwang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answering questions and completing tasks over large document collections often requires connecting evidence spread across multiple documents, such as a project's approval recorded in one, its requirements in another, and its latest status in a third. Recent LLM agents approach this by iteratively searching the full corpus rather than reading only a fixed set of top-ranked documents. However, when the corpus is exposed only as a flat collection of files, a relevant document gives no indication of how it relates to others, so the agent must rediscover these relationships for every query, often missing complementary evidence while simultaneously consuming substantial additional tokens. To address this, we introduce CorpusMap, a navigation layer that organizes the corpus around its recurring entities, which are identifiable from the documents themselves and can link a single document to many others across sources. Specifically, CorpusMap represents each recurring entity as an Entity Page that aggregates information about it and links to every document that refers to it, forming a graph between entities and documents that the agent can traverse to gather otherwise disconnected evidence. Moreover, since CorpusMap is constructed offline by resolving mentions of the same entity across documents, its links are shared across queries rather than rediscovered repeatedly at inference time. Using 7 different models with 3 benchmark datasets, we show that CorpusMap improves both evidence discovery and answer quality over raw-corpus agentic search while using fewer tokens on average, and further outperforms 4 alternative navigation layers, suggesting that entities serve as effective anchors for navigating large document collections.

---


### 297. [Seeing Is Not Addressing: Auditing Linguistic Access to Frozen Visual Geometry](https://arxiv.org/abs/2609.37230)

**<font color=#1a73e8>作者：</font>** Woosang Jeon, Jiwon Yang, Soo Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual distinctions are often finer than those reflected in linguistic conceptualization. Vision-language models exhibit a similar asymmetry: a distinction can remain discriminable in frozen image geometry while being weakly addressable through the native text interface. We study this gap by separating visual discriminability from linguistic addressability in text-to-image retrieval. Using FactorAtlas, a fully crossed testbed of 23,040 images spanning shape, hue, pattern, and nuisance variation, we compare both readouts on held-out images of the same distinctions. We then derive image-side contrasts that separate each value from its alternatives for matched visual grounding, and test whether this reduces the native-text access gap across factors and models. Direction-specific and visual-absence controls tie these gains to the relevant visual contrast; the gains persist after global alignment and extend to compositional retrieval and natural images. Together, these results show that visual discriminability and linguistic addressability need not coincide, and that matched visual grounding can probe and reduce the resulting access gap.

---


### 298. [Trident: Unifying Guarded Dispatch and Host Execution for PyTorch Triton Workloads](https://arxiv.org/abs/2609.37241)

**<font color=#1a73e8>作者：</font>** Jinjie Liu, Xiaoyan Liu, Shuhan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> User-written Triton kernels enable high-performance GPU computation within PyTorch, but their end-to-end latency can remain dominated by host-side orchestration, especially when device execution is short. Although this http URL can generate native host wrappers for captured graphs, each invocation still passes through runtime-managed specialization lookup, guard evaluation, and preparation before reaching the wrapper. We present Trident, a compiler backend that removes this recurring overhead from the specialization cache-hit path. Trident introduces the Specialization Cache Module (SCM), which compiles guarded specialization selection, argument and execution-environment preparation, and host execution for multiple specializations into a single executable module. An invocation enters the SCM once, remains in compiled code when a specialization matches, and returns to Python only when a new specialization must be compiled. Built on Torch-MLIR, Trident lowers guards and host-side orchestration to native code while retaining calls to optimized runtime implementations of supported ATen operators. Our evalu- ation on two LLMs shows that Trident achieves up to a 1.47x speedup in model-level end-to-end latency over eager execution and up to 1.68x over this http URL.

---


### 299. [Beyond Attention Imbalance: Mitigating Hallucinations via Spectral Surgery](https://arxiv.org/abs/2609.37263)

**<font color=#1a73e8>作者：</font>** Siqi Lu, Suo Wei, Yongbin Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Large Vision-Language Models (LVLMs) achieve remarkable success, hallucinations remain a significant barrier to their reliable deployment. Recent studies primarily attribute these issues to cross-modal attention imbalances; most solutions therefore focus on reweighting visual tokens or suppressing language priors. However, such approaches often overlook the spectral characteristics of the visual information flow and frequently rely on Contrastive Decoding (CD), which doubles inference time. Instead of following conventional approaches, we identify two distinct hallucination patterns-Perceptual-Semantic Dissociation and Localized Fixation-and propose FLASH (Frequency-Localized Attention SHaping), a training-free and CD-free framework. FLASH utilizes a Spectral Vortex Score to detect vision heads within multi-head attention layers and applies adaptive spectral modulation to rectify the visual information flow during decoding. Empirical results demonstrate that FLASH achieves a superior balance between performance and efficiency compared to SOTA methods.

---


### 300. [UniAfford: Token-Routed Multitask Learning for Generalizable 2D-3D Affordance Perception](https://arxiv.org/abs/2609.37264)

**<font color=#1a73e8>作者：</font>** Yuhao Liu, Yiming Zhong, Hanqing Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Affordance perception aims to localize actionable regions supporting embodied interaction, yet 2D and 3D affordance grounding have evolved as separate problems, with different task definitions, supervision formats, datasets, and evaluation protocols. This fragmentation limits the learning of transferable object-affordance semantics across visual and geometric spaces. We propose Token Router for Tasks, a multitask training paradigm for MLLM-based systems that routes contextual hidden states to task-specific branches without requiring the language head to generate predefined markers. Routed states are supervised directly by branch-specific objectives, enabling dense prediction losses to shape shared MLLM representations. We instantiate this paradigm as UniAfford, a unified framework for generalizable 2D-3D affordance perception, together with UniAfford-Data, a dataset integrating pixel-level 2D annotations, point-level 3D annotations, and language instructions under a shared object-affordance taxonomy, supporting heterogeneous supervision through semantic-level 2D-3D pairing. UniAfford adopts an MLLM as a shared semantic hub and a modality-aware token router to produce image- and point-cloud-affordance queries. These queries respectively condition a SAM-style pixel decoder and a SONATA-based point decoder, enabling flexible 2D, 3D, and joint affordance inference from image-only, point-cloud-only, or paired multimodal inputs. Experiments demonstrate strong zero-shot generalization across 2D and 3D affordance benchmarks without target-specific fine-tuning, alongside state-of-the-art branch-wise performance under modality-isolated protocols. Ablations validate token routing, joint 2D-3D supervision, and decoder coupling, while language-head diagnostics show that routed latent states carry meaningful object-affordance semantics. Project page: this https URL

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
