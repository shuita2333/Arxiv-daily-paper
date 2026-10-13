# 🧠 大模型相关研究 | 2026年10月14日

> 本类共 **230** 篇论文：已确认 **202** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-230](./part-05.md)

---

### 101. [Measurable Semantic 3D Gaussian Splatting with Joint Region and Depth Supervision for Interactive Building Inspection](https://arxiv.org/abs/2610.13143)

**<font color=#1a73e8>作者：</font>** Yi Zhang, Tian Tan, Ray Kai Leung Su  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-based 3D reconstruction provides a scalable representation for building inspection and maintenance. However, photorealistic reconstruction alone does not fully provide the geometric measurability, semantic structure, and interactive information access required for engineering applications. This study proposes a measurable semantic 3D Gaussian Splatting (3DGS) framework with region and depth supervision for interactive building inspection from multi-view imagery. Mask-based region supervision suppresses irrelevant backgrounds and focuses optimization on target regions. Point-wise depth supervision guides Gaussian centers toward physical surfaces using reference geometry derived from multi-view stereo (MVS) point clouds, providing geometric anchors for measuring physical dimensions and areas. A semantic Gaussian field associates learnable class features with individual Gaussian primitives, enabling semantic rendering and component-level inspection. These capabilities are operationalized through AEC-SplatTwin, an interactive building inspection platform supporting real-time visualization, semantic analysis, quantitative measurement, and multimodal large language model (MLLM)-assisted interaction. On the synthetic UAV-inspection QuakeCity and smartphone-captured HKUPB datasets, the framework reduces Gaussian-center depth MAE by 58.1% and 86.8%, while its semantic field achieves mIoU values of 0.8529 and 0.8642. On HKUPB, the mean relative errors for height, width, and area measurements are 0.33%, 1.07%, and 0.60%. These results show that the proposed framework extends 3DGS beyond visual reconstruction into a measurable, semantically structured, and interactive engineering representation for building inspection.

---


### 102. [Competence-Aware Orchestration for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2610.13144)

**<font color=#1a73e8>作者：</font>** Songmiao Wang, Yuchen Wang, Chenglin Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MAS) have emerged as a promising paradigm for enhancing complex reasoning through role specialization and collaboration, yet a key challenge remains: how can collaboration be adapted to a backbone's competence on the current query? This problem matters because more collaboration is not always better--richer coordination may help on difficult cases, but it also incurs additional token cost and redundant interactions. We propose a two-stage competence-aware framework for automatic MAS orchestration. It first models the LLM backbone's task-conditioned competence for the current query, and then uses this signal to adapt role activation and the communication graph. Across six benchmarks, our method achieves an average score of 93.81%. Experiments with six LLM backbones of varying competence levels further show that our method adjusts collaboration according to the inferred competence: for higher-competence backbones, it improves average accuracy from 87.22 to 89.97 while reducing token cost by 36.26%; for lower-competence backbones, it yields a further average gain of 4.58 points over existing methods. The same trend also holds on unseen backbones.

---


### 103. [VIGOR: Verifiable Industrial Geometry Optimization and Repair in Scene Programs](https://arxiv.org/abs/2610.13145)

**<font color=#1a73e8>作者：</font>** Fuqiang Wang, Zheng Guo, Xiaoming Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly generate structured layouts and executable scene programs from natural-language instructions. However, executability does not imply engineering feasibility: an industrial scene program may execute successfully while its final state still violates coupled boundary, collision, clearance, aisle, or structural constraints. We identify this mismatch as the executability-engineering-feasibility gap, where locally plausible placements can remain globally infeasible because corrections to one device may introduce violations elsewhere. To make this gap measurable in a controlled setting, we construct an execution-grounded industrial scene-program dataset with 1,749 constructible scenarios, complete executable programs, and 94 final-state geometric checks per scenario. We further propose VIGOR, which combines supervised scene-program generation with execution-grounded verification and staged geometric refinement. Supervised fine-tuning establishes complete program generation, local projection resolves independently correctable violations, and joint conflict-graph repair coordinates residual multi-object conflicts while preserving structural relations. Experiments show that VIGOR achieves 96.86% Complete Feasibility and an Overall score of 91.20, outperforming the strongest evaluated baseline by 10.42 points in Overall. These results show that, under controlled industrial layout conditions, reliable scene-program generation requires not only executable programs, but also explicit verification and coordinated resolution of coupled engineering constraints.

---


### 104. [Quality, Not Just Outcome: A Structural Scoring Framework for Selecting Coding-Agent Trajectories for Supervised Fine-Tuning](https://arxiv.org/abs/2610.13152)

**<font color=#1a73e8>作者：</font>** Sida Li, Yuanxin Liu, Shicheng Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open coding agents are commonly trained through supervised fine-tuning on interaction trajectories whose final patches pass the benchmark test suite. However, this outcome-level filtering criterion ignores process quality: trajectories that eventually succeed may still contain inefficient interaction patterns such as repetitive file inspection, unstable tool usage, or delayed modification behavior, all of which become part of the imitation target. We propose TQS (Trajectory Quality Score), a structural scoring framework for coding-agent trajectories that operates directly on trajectory structure, requires no LLM judge, and runs in linear time. TQS characterizes trajectory quality through structural signals organized around structured convergence: information focus, intent--action alignment, and policy dynamics. Using 155,144 successful trajectories from a public open-license corpus, we rank trajectories by TQS and fine-tune coding agents on filtered subsets. Models trained on top-ranked trajectories consistently outperform those trained on random or bottom-ranked subsets on SWE-Bench-Verified. Our results suggest that process-level trajectory quality is an important factor in coding-agent supervision and that structural trajectory filtering provides an effective and scalable alternative to LLM-based data selection.

---


### 105. [From Glance to Focus: Mitigating Recognition Laziness in MLLMs for Fine-Grained Recognition](https://arxiv.org/abs/2610.13154)

**<font color=#1a73e8>作者：</font>** Yutong Yang, Zhuqi Liu, Mouxing Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) generally fall short of expectations in Fine-Grained Visual Recognition (FGVR), although they exhibit promising FGVR foundations, i.e., visual perception and broad category knowledge. Most existing studies seek to remedy this deficiency by adopting domain-specific post-training, at the risk of compromising generalization to unseen domains. Different from these efforts, in this paper, we revisit the FGVR mechanism underlying MLLMs from both the empirical and theoretical perspectives and uncover an inference-time phenomenon termed FGVR Laziness. In brief, FGVR Laziness refers to the insufficient association between visual cues and category concepts under certain candidate category lists and recognition guidance, leaving the FGVR foundations of MLLMs largely under-utilized. To mitigate FGVR Laziness, we propose Laziness-resIstant Visual rEcognition (LIVE), a training-free framework which jointly refines candidate lists and recognition guidance to elicit the latent FGVR capability of MLLMs. Specifically, LIVE first performs query-adaptive candidate inference to derive a compact yet reliable candidate list. Meanwhile, LIVE constructs category-specific FGVR skills by mining the intra-category characteristics and inter-category differences. Finally, LIVE selectively invokes detailed skill guidance according to recognition uncertainty and category confusion, shifting MLLM-based FGVR from a cursory glance to a focus on associating discriminative visual cues with category concepts. Extensive experiments on 13 benchmarks against 24 state-of-the-art methods spanning fine-grained category recognition, action recognition, and general category recognition, verify the effectiveness and generalizability of LIVE across different MLLM backbones. The code will be released upon acceptance.

---


### 106. [Scaling Agentic Data for Long-Horizon Terminal Intelligence](https://arxiv.org/abs/2610.13166)

**<font color=#1a73e8>作者：</font>** Shun Zou, Ziyu Ma, Yi Zou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Terminal agents are moving beyond local operations toward completing real-world professional tasks. Short trajectories can demonstrate commands and tool calls, but they do not fully show how agents accumulate evidence through exploration, use it to inform judgments, continually adjust strategies based on feedback, and turn intermediate results into final deliverables. High-quality long-horizon trajectories capture these agentic behavioral patterns and their connections within a single problem-solving process, providing richer experience for sustained autonomous work. However, environment synthesis may complete or simplify the key work underlying these patterns in advance and thus remove the need for exploration, implementation, and verification that the agent was meant to perform. To address this, we introduce TerminalHorizon, a fully automated data synthesis engine for long-horizon terminal agents. Starting from real-world professional work, it uses independent execution to identify key work omitted during construction and uses the resulting evidence to guide environment reconstruction. To extend these patterns across stages, it progressively expands tasks under the same goal, introducing new requirements that build on prior results and call for further exploration and improvement. Using this engine, we construct 1.5K task environments and perform supervised fine-tuning of Qwen3.5-27B on the resulting dataset to obtain TerminalHorizon-27B. We achieve substantial performance gains on all 12 benchmarks spanning coding-agent tasks, agentic tasks in real-world production settings, and general reasoning. Multiple RSI case studies, each with a 12-hour research budget, further demonstrate the model's ability to continue experimenting beyond an initial solution, improve its methods based on feedback, and retain effective improvements in its final deliverables.

---


### 107. [Understanding Verification Vulnerabilities in Cross-chain Bridges: An Empirical Study](https://arxiv.org/abs/2610.13170)

**<font color=#1a73e8>作者：</font>** Yuying Wang, Yi Guo, Jiachi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid development of blockchain technology, numerous heterogeneous blockchains have emerged, each featuring distinct architectures, consensus mechanisms, and application ecosystems. Cross-chain bridges have consequently become a critical infrastructure component, typically relying on smart contracts to facilitate message passing and asset transfers across heterogeneous blockchains. Unlike single-chain contracts, bridge contracts introduce additional verification logic to validate external-chain data, such as state proofs, message sender identities, and signatures. However, correctly implementing such logic is challenging. We refer to vulnerabilities that violate the security guarantees of cross-chain verification as Cross-chain Verification Vulnerabilities (CVVs). To characterize CVVs, we conduct the first systematic empirical study of this vulnerability class. By analyzing 588 security audit reports from 36 real-world cross-chain bridge projects, we derive 11 CVV patterns and organize them into 5 high-level categories according to the affected verification properties. Following this taxonomy, we construct a CVV dataset containing 830 vulnerability instances across 786 contract files. The dataset establishes mappings among audit reports, audited source-code versions, affected source files, and CVV-pattern labels. We then assess existing detection approaches. Current tools provide limited documented coverage of CVV patterns, while only two of four evaluated LLMs outperform an all-pattern constant baseline of 29.3% Macro-F1; the best reaches 51.2%. Together, the limited tool coverage and inconsistent LLM gains motivate detection methods tailored to cross-chain verification semantics.

---


### 108. [PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling](https://arxiv.org/abs/2610.13171)

**<font color=#1a73e8>作者：</font>** Nan Jiang, Panagiotis Theodoropoulos, Wei Deng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Power sampling improves large language model (LLM) reasoning at test time by sampling from a sharpened version of the base model's distribution. Its sampler, PowerMH, is slow because its Metropolis--Hastings (MH) updates are sequential: each accept/reject decision sets the state from which the next proposal is generated. Prior work reduces this cost by changing the sampler or the model (e.g., sequential Monte Carlo, approximate lookahead, distillation). We propose Predictive SubTree Prefetching (PreSTO), which accelerates PowerMH by prefetching future proposals and provably leaves its MH transition kernel unchanged. PreSTO views future MH outcomes as a tree of accept/reject decisions: in each model call, it generates the proposals of a \textit{prefetched subtree} of this tree in one batch, then follows the realized path with the original MH acceptance rule. We also observe that MH reaches only a sparse, nearly unary part of each prefetched subtree, we further design a \textit{predictive traversal rule} that chooses the subtree to maximize the predicted number of completed transitions. Across seven datasets and five base LLMs, PreSTO achieves median speedups of $1.71\times$, $1.91\times$, and $2.33\times$ on PowerMH and its follow-ups EntropyCut and MultiTryMH, respectively; on the first two, it makes a median of $3.9\times$ fewer model calls, each only $2.1\times$ longer. On LCB V6 with Qwen3.5-9B, the predictive traversal rule is a further $1.25\times$--$1.37\times$ faster than the default breadth-first traversal.

---


### 109. [RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions](https://arxiv.org/abs/2610.13172)

**<font color=#1a73e8>作者：</font>** Boyuan Xiao, Pu Wang, Ji Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models enable large language model (LLM) agents to anticipate action effects and make informed decisions. For generalization, it is desirable for such world models to transfer efficiently to new environments with similar interaction structure and underlying dynamics. Recent approaches encode world dynamics as symbolic rules or executable programs, whose compositional structure in principle affords transfer, but still organize such knowledge around environment-specific objects. To address this limitation, we introduce RoleWorld, a symbolic world modeling approach which uses reusable prototypes and environment-specific parameter values as functional role abstractions to represent how objects behave in interactions. From interaction trajectories, a teacher LLM extracts role prototypes and executable transition rules defined over role instances, together with a skill that guides the actor LLM to use role information in decision making. In a target world, without the teacher, the actor uses this skill together with its current role assignments and parameter estimates, and actively tests a role instance hypothesis through interaction when its uncertainty affects the current decision. Feedback from each action refines role assignments and estimates parameter values online, with no LLM parameter updates and the transition rules held fixed. Experiments on MARS benchmark show that RoleWorld enables robust generalization across environments with significantly altered object behavior, suggesting that functional role abstractions can serve as an effective component for knowledge transfer in world modeling. Project Page: this https URL.

---


### 110. [AdaC-GRPO: Towards Mastering Long-Horizon Visual Sudoku Puzzles via Adaptive Curriculum Learning](https://arxiv.org/abs/2610.13184)

**<font color=#1a73e8>作者：</font>** Sida Li, Yuanxin Liu, Linli Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While reinforcement learning with verifiable reward (RLVR) enhances reasoning in large language models, its efficacy in long-horizon multimodal tasks remains underexplored. Visual Sudoku puzzles pose a representative challenge, requiring multi-step deductive reasoning over both local constraints and global dependency chains. To this end, we introduce FG-Sudoku, a fine-grained benchmark categorized by grid size and required deductive steps. Evaluations reveal that frontier MLLMs fail on complex long-range dependencies (e.g., 9*9 puzzles). During post-training, this near-zero success rate causes severe reward sparsity, halting standard RLVR. We propose Adaptive Curriculum Group Relative Policy Optimization (AdaC-GRPO) to overcome this. Unlike rigid or prior-based schedules, AdaC-GRPO dynamically constructs training batches by tracking the model's "Zone of Proximal Development" via online rollout accuracy. Experiments demonstrate that AdaC-GRPO enables Qwen2.5-VL-7B to approach the performance of Gemini-2.5-Flash while bridging 62.2% of the overall accuracy gap to Gemini-2.5-Pro, with its generalizability further validated across InternVL-3.5 and Qwen3-VL.

---


### 111. [olBlend: Language-Guided Molecular Blend Retrieval with Mixture Odor Prediction](https://arxiv.org/abs/2610.13188)

**<font color=#1a73e8>作者：</font>** Dian Jin, Zhechang Chen, Qilin Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Converting open-ended natural-language odor descriptions into molecular mixtures that can be physically prepared from an available inventory remains an important challenge in computational olfaction. We propose olBlend, a language-guided framework for molecular mixture retrieval. olBlend first uses MixPOM to predict odor probabilities for candidate molecular pairs and stores these predictions for retrieval. It then uses a language model to translate each odor description into three types of semantic requirements: lead attributes that define the main odor, ambient attributes that describe its background, and absent attributes that should be avoided. A structured scoring algorithm uses the precomputed odor probabilities to score how well each candidate mixture meets these requirements, then retrieves and ranks mixtures from the available inventory. Evaluation on established odor datasets shows that MixPOM improves mixture odor prediction over averaged single-molecule predictions. Retrieval comparisons across natural-language queries demonstrate how background and exclusion requirements guide mixture selection. We further prepare retrieved formulations as physical odor samples, demonstrating the workflow from natural-language descriptions to realizable molecular formulations.

---


### 112. [S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding](https://arxiv.org/abs/2610.13202)

**<font color=#1a73e8>作者：</font>** Yuhang He, Hongyu Ge, Zihan Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast rollout generation for long-context reinforcement learning with verifiable rewards (RLVR) requires reducing KV-cache traffic without changing the response groups used for policy optimization. In our profiled RLVR workloads, attention accounts for 72--76\% of autoregressive decoding kernel time. Sparse attention reduces these reads, but sampling directly from a sparse policy changes the response groups used for learning. For group-relative optimization, we show that even exact response-wise reweighting does not generally recover the expected dense-policy update because the advantage of each response depends on the rewards of other group members. We propose Self-Sparse Speculative Rollouts (S$^3$R). It uses sparse attention to propose tokens, then generates responses through full-attention verification and exact speculative sampling. Drafting and verification share the same policy parameter, eliminating the need to train or update a separate drafter. The resulting response groups follow the dense-policy distribution. Under S$^3$R, we characterize speedup conditions and the costs of drafting and verification. We found that dense verification still requires the complete historical KV cache. A KV-aware scheduler therefore limits KV-cache repeated offloading and restoration while maintaining rollout parallelism. % OR thrashing In a matched ablation with an aggressive sparse drafting budget, S$^3$R maintains stable training while direct sparse sampling with training-side correction becomes unstable. On long-context mathematical reasoning, S$^3$R achieves $1.39\times~1.35\times$ the end-to-end training throughput of autoregressive rollouts on Qwen3 model, with comparable task performance.

---


### 113. [Rethinking Relative Policy Differences Transfer of On-Policy Distillation](https://arxiv.org/abs/2610.13205)

**<font color=#1a73e8>作者：</font>** Rong Wu, Daocheng Fu, Yu Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a target policy on its own rollouts using token-level supervision from a stronger teacher, but typically relies on the teacher being substantially more capable than the target. Recent work relaxes this requirement by transferring the relative policy difference between an expert and a reference policy rather than the expert's absolute distribution. Yet it remains unclear which differences provide useful supervision and which targets can benefit from them. We develop a unified view in which the log-probability ratio between a proxy expert and a proxy reference defines an implicit reward for KL-regularized policy optimization. This formulation induces an on-policy update for the target, recovers conventional OPD as a special case, and enables any-to-any transfer across models that differ in scale, training stage or generation. Our systematic experiments yield three findings. First, a stronger expert is not necessarily a better source of supervision: differences induced by task-specific training, including reinforcement learning and supervised fine-tuning, transfer consistently, whereas those arising from model scale alone transfer weakly or not at all. Second, the expert and reference serve complementary roles: the expert provides the capability to be transferred, while the reference filters out shared behavior and isolates the relevant residual. Third, even a useful difference does not transfer to every target: success requires the induced update to move the target toward the expert and generalize beyond sampled rollouts. Raw policy distance does not predict transferability, whereas an appropriate reference can rescue otherwise unsuccessful transfer. These results characterize when relative policy differences provide effective supervision for OPD.

---


### 114. [SharP: Soft and Hard Prompt-Guided Augmentation with LLM for Low Resource Fake News Detection](https://arxiv.org/abs/2610.13207)

**<font color=#1a73e8>作者：</font>** Ziyu Luo, Wei Li, Haoping Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fake news detection under low resource conditions is challenged by the scarcity of labeled data and the difficulty of capturing subtle deceptive patterns. In this work, we focus on low resource fake news detection, where only a small labeled set is available for training, while evaluation is performed under a fixed and unchanged test protocol. This setting is motivated by costly, ambiguous fact-checking and emerging topics and domains that are poorly covered by existing benchmarks. Existing data augmentation methods, such as synonym substitution, generative adversarial networks, and large language model (LLM)-based generation, often produce fluent but overly generic content, lacking the task-specific relevance needed for accurate detection. To address this, we propose SharP, a boundary-aware text generation framework guided by soft and hard prompts, which leverages LLMs as tools adapted to produce task-specific synthetic samples. SharP employs a dual prompt mechanism: hard prompts provide structured guidance and factual constraints, while soft prompts introduce learned semantic patterns from the data. These two types of prompts are combined to guide the generation process, enabling the model to produce samples that closely align with the characteristics of news. To further enhance detection performance, we incorporate a boundary-aware strategy that steers generation toward areas where the classifier is less confident, helping to clarify subtle distinctions between real and fake content. In addition, we adopt a dual objective optimization that balances semantic alignment with the source data and classifier feedback. This encourages the generation of samples that are both domain-consistent and helpful for refining decision boundaries, ultimately improving model robustness and generalization in low resource fake news detection.

---


### 115. [Monarch-MoE: Structured Experts for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2610.13215)

**<font color=#1a73e8>作者：</font>** Xi Zhang, Boyu Diao, Zesen Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning new tasks in multimodal continual instruction tuning can cause catastrophic forgetting of previously acquired knowledge. Although multi-expert LoRA distributes learning across experts, updates to a dense low-rank expert can still affect many output features. We introduce Monarch-MoE, which replaces the dense factors in LoRA experts with block-diagonal factors connected by a fixed permutation. This structure provides blockwise gradient isolation: individual block-pair updates affect only one output block, while connections between all input and output blocks are maintained. To make these compact experts practical on memory-limited hardware, we combine batched computation, fused forward operators, and an optimized backward pass. Across three continual-learning methods evaluated on MLLM-DCL and UCIT with LLaVA-1.5-7B, Monarch-MoE improves first-task retention while reducing adapter parameters by approximately 75% and 50%, respectively. In the main comparison, first-task forgetting is as low as 0.52 percentage points on MLLM-DCL and 0.10 on UCIT, with method-dependent trade-offs in final performance. Our implementation supports fine-tuning and inference on a single 24 GB RTX 4090, with lower measured memory use and competitive runtime in the evaluated settings. Together, these algorithmic and systems improvements make structured experts a practical option for continual adaptation on memory-limited hardware.

---


### 116. [State-OPD: State-Grounded On-Policy Distillation for Multi-Turn Agents](https://arxiv.org/abs/2610.13238)

**<font color=#1a73e8>作者：</font>** Zhentao Zhang, Yanzhao Zheng, Yanlin Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-Policy Distillation (OPD) has emerged as a powerful paradigm for transferring reasoning capabilities from frontier models to smaller models, while extending its success to multi-turn agentic environments remains challenging. We study agentic OPD through interaction states, distinguishing the objective task and executed action-observation record from the internal semantic trajectory of student reasoning. Through this lens, we identify two roles of student reasoning in multi-turn OPD: prior reasoning distorts teacher supervision, while current reasoning shapes the action alternatives sampled at the same state. Specifically, at matched interaction states, removing prior student reasoning improves teacher continuation success and changes the teacher's token-level targets, with larger continuation gains at later turns. Meanwhile, resampling complete reasoning-action responses yields greater action diversity at the same state than resampling actions under a fixed reasoning trace. We introduce State-Grounded On-Policy Distillation, a framework that grounds teacher supervision in interaction states and reallocates the sampling budget to generate multiple complete reasoning-action responses at states with high response entropy, while retaining full-history student generation. Comprehensive evaluations across ALFWorld, ScienceWorld and WebShop demonstrate that State-OPD achieves the highest macro-average success rate among the evaluated methods for both Qwen3-1.7B and Qwen3-4B students. Notably, for Qwen3-4B, State-OPD raises macro-average success from 26.07\% with the strongest baseline to 31.74\% and surpasses its Qwen3-32B teacher on ALFWorld Seen. Further analyses reveal that State-OPD achieves higher task success with fewer supervised turn responses and substantially reduces persistent failed-action repetition; qualitative traces illustrate decision revision based on interaction feedback.

---


### 117. [CAST: Credit Alignment for Cross-Tokenizer On-Policy Distillation](https://arxiv.org/abs/2610.13257)

**<font color=#1a73e8>作者：</font>** Jingru Yang, Jinhang Wu, Minjing Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-tokenizer on-policy distillation (OPD) requires aligning teacher and student sequences before their scores can be compared. Decoded-text alignment provides such correspondence at the chunk level, but leaves a distinct problem unresolved: credit alignment. A chunk-level signal specifies how much a span should change, but not how that signal should be distributed across student tokens, while tokens without teacher correspondence remain unconstrained. We propose CAST (Chunk-aware credit Assignment with Selective Token Anchoring), a shift-or-stay framework that addresses both issues. For aligned chunks, CAST redistributes each chunk's advantage across student tokens using predictive uncertainty and local teacher-signal smoothness, emphasizing learning opportunities supported by locally consistent teacher feedback while preserving the chunk's total advantage. The resulting weights exactly solve a KL-regularized credit-allocation problem. For unaligned positions, CAST selectively anchors the student to its initial policy through a KL penalty, limiting drift where teacher supervision is unavailable. Because credit assignment is separated from chunk construction, CAST also applies to punctuation-defined or fixed-length chunks under shared tokenization. Across six mathematics, science, and code benchmarks, CAST improves the average over the strongest evaluated baseline by $2.45$ and $1.32$ points for cross-tokenizer transfer from Qwen3-8B to Mistral-7B and Llama-3.1-8B, respectively, and by $2.10$ points for shared-tokenizer transfer to Qwen3-1.7B.

---


### 118. [Beyond a Single Crop: Contextualized Embeddings for Player Re-Identification](https://arxiv.org/abs/2610.13259)

**<font color=#1a73e8>作者：</font>** Ge Luo, Changhuo Yang, Weisi Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Person re-identification is typically addressed by learning identity-discriminative embeddings from individual person crops. However, player re-identification in broadcast sports videos presents a unique challenge: players from the same team often share similar appearances, while video sequences provide repeated observations of the same players under different viewpoints and surrounding contexts. Existing crop-based approaches largely ignore this contextual information, which can be critical for resolving visually similar identities.
Here, we propose ContextReID, a contextualized embedding framework that represents a player by jointly considering other players in the same frame and observations from different frames of the broadcast sequence. By incorporating both co-occurring players and cross-frame observations, the model learns identity features relative to the surrounding visual context rather than relying only on isolated appearance cues. We implement this framework with a vision-language model that takes sets of player crops as input and generates context-aware embeddings for individual players. A combined contextual learning and retrieval objective encourages the model to capture cross-frame identity relationships while maintaining discriminative embeddings for player matching.
Experiments across three multi-object tracking benchmarks show that ContextReID improves player retrieval over conventional single-crop embedding approaches in both Rank-1 and mAP. These results highlight the utility of spatial and temporal context for reliable player identification in broadcast sports videos.

---


### 119. [SheafPrune: Sheaf-Guided Graph Propagation for Visual Token Pruning](https://arxiv.org/abs/2610.13263)

**<font color=#1a73e8>作者：</font>** Xiaoyang Ma, Chi Wang, Hong Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models process the complete visual token sequence, increasing prefill cost even when many tokens are irrelevant to the instruction. Token-wise saliency captures limited inter-token dependence; graph-based selection instead depends on how relations govern importance propagation and ranking. We study support-constrained propagation with node-degree correction. Inspired by sheaf geometry, SheafPrune uses modality-specific maps and a sparse text--visual graph to transfer relevance, then propagates scores on a separate visual graph and corrects them for degree. It retains a hard top-$k$ subset once before the frozen language model. The selector has about $4.5$M parameters and is trained end-to-end through the frozen LLaVA-NeXT-8B backbone using only the language-modeling objective. Explicit retention-ratio conditioning lets one checkpoint serve every budget. Across four backbones, ten benchmarks and seven pruning ratios, with all baselines re-implemented under one protocol, SheafPrune achieves the best retention at $22$ of $28$ backbone--budget settings, with monotonically growing margins in the moderate-to-aggressive regime. On LLaVA-NeXT, retaining $10\%$ of visual tokens yields a $5.15\times$ net prefill speedup and an $84.0\%$ end-to-end FLOPs reduction. Together with component ablations, these results support graph-constrained importance propagation and degree correction as a design for visual token selection across the evaluated backbones and tokenization schemes, improving the trade-off between accuracy retention and inference cost. code:this https URL

---


### 120. [CV-OPD: Contrastive Vision On-policy Distillation](https://arxiv.org/abs/2610.13264)

**<font color=#1a73e8>作者：</font>** Haowei Wang, Hao Lin, Qi Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) reveals versatility and convenience during VLM post-training, providing dense supervision for student from teacher. However, we observed an anomaly that the distilled VLM could still answer the questions accurately even when the related visual regions were masked or replaced with noise. Building on this observation, our quantitative and qualitative experiments demonstrate that OPD, which uses the answer as a hint, has failed to teach students to genuinely seek out and rely on visual evidence. Our theoretical analysis suggests that this failure arises from a shortcut enabled by the lack of visual constraints during distillation. To address the issue, we introduce Contrastive Vision On-policy Distillation (CV-OPD), which compares teacher distributions induced by positive and negative crops while conditioning on the same student prefix and augments optimization with a margin-based contrastive constraint, which is modulated with discrepancy gating across token and sample level. Specifically, CV-OPD first introduces a negative teacher unrelated to the answer and designs a Contrastive Divergence Loss (CDL) that constrains the feature distribution of student by contrasting the positive and negative teachers, correcting how the student exploits visual regions. The CV-OPD introduces a Discrepancy Aware Gate (DAG) that uses token-level and sample-level discrepancies to select visually relevant tokens for optimization, directing the student's attention toward visual content. Extensive experiments across a broad range of fine-grained visual benchmarks demonstrate that CV-OPD substantially alleviates shortcut and consistently improves the visual reasoning capabilities of existing VLMs.

---


### 121. [ConClick: Element-Wise Contrastive Learning Improves GUI Grounding](https://arxiv.org/abs/2610.13268)

**<font color=#1a73e8>作者：</font>** Ruotian Zhang, Yuhui Zhang, Junzhe Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI grounding, the task of locating the interface element specified by a user instruction, is a fundamental capability of GUI agents. However, existing grounding models remain error-prone, often causing downstream task failures. We systematically evaluate 10 grounding models across five datasets and identify a major error pattern: most incorrect clicks hit non-target interface elements rather than the background, with different models repeatedly selecting the same distractors. Motivated by these findings, we propose ConClick, a contrastive learning framework that teaches models to distinguish the target element from plausible distractors. We construct ConClick-Data, a dataset containing 4,292 challenging target-distractor pairs, and train the model using complementary listwise ranking and pairwise margin objectives. ConClick improves the grounding accuracy of Qwen3-VL-8B from 54.71% to 66.03% on ScreenSpot-Pro, from 83.72% to 86.28% on MMBench-GUI L2, and from 63.33% to 70.20% on OSWorld-G, outperforming prior methods built on the same or similarly sized backbones. We further introduce ReClick, an inference-time strategy that revisits promising regions and compares predictions across competing candidates, yielding an additional 2.96 percentage-point improvement in average accuracy across the three benchmarks. Together, our analysis, dataset, and methods provide both empirical insights and practical tools for building more reliable GUI agents. Data and code are available at this https URL.

---


### 122. [OWLET: On-Policy Weighted Learning via Evidence Transfer for Video Large Language Model Post-Training](https://arxiv.org/abs/2610.13272)

**<font color=#1a73e8>作者：</font>** Qitan Lv, Ke Fan, Hong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training has become a key stage for eliciting reasoning capabilities in Video Large Language Models (Video-LLMs). Existing post-training methods mainly follow two paradigms: reinforcement learning (RL) and on-policy distillation (OPD). However, they do not fully exploit visual evidence for effective training. RL supervises the policy with a single trajectory-level reward, which is too coarse-grained for video reasoning: the same response-level advantage is applied to every generated token, disregarding that the tokens of a video response are grounded in the visual stream to very different degrees. OPD provides token-level supervision through output-distribution matching, but lacks direct supervision of the spatiotemporal representations that produce those outputs. We observe across extensive experiments that the same model reasons more accurately when its video view combines global temporal context with question-relevant details. Comparing the same student-generated response under this view and uniform sampling reveals changes in token likelihoods and internal representations, providing a training signal for evidence use. Building on this observation, we propose OWLET, an evidence-privileged RL method that derives training signals from a richer teacher view. This view couples uniform global context with question-conditioned local windows, providing visual evidence without requiring a larger model. To better exploit this privileged visual evidence, OWLET introduces (i) \textbf{evidence-aware credit redistribution}, which compares token likelihoods across the two views and redistributes positive response-level advantages according to their relative evidence support; and (ii) \textbf{spatiotemporal state alignment}, which aligns the two views' hidden states on verifier-accepted responses.

---


### 123. [CopRoute: Dependence-Aware Conformal Routing for Language Models](https://arxiv.org/abs/2610.13276)

**<font color=#1a73e8>作者：</font>** Siva Rajesh Kasa, Santhosh Kumar Kasa, Karan Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Set-based language model routing aims to increase the coverage of the event where at least one model answers a query correctly while controlling the number of inference calls made. Existing risk-controlled routing policies bound the all-miss risk (the probability that every model in the selected set fails) by calibrating a single conformal threshold and applying it to a nested family of model sets. Because each model is scored in isolation, these policies ignore the dependence structure of model failures. Models that share training data or architecture tend to fail on the same queries, so two individually strong models can be jointly redundant while a weaker but complementary model covers the queries that the others miss. To account for this dependence, which existing risk-controlled policies ignore, we propose CopRoute, which orders models by how many new queries each one answers correctly beyond those already selected, decides per query how far down that order to go, and then picks the smallest cutoff that still meets the target risk. We show that CopRoute's ordering attains, on the design data, the best guarantee any efficient fixed-ordering algorithm can give for the average number of calls to the first correct model, and that a separate calibration step certifies the all-miss risk of the deployed sets. On RouterBench and RouterEval, CopRoute attains the fewest certified calls on nine of ten datasets at a target risk of 0.05 and on eight of ten at 0.10, making up to 79 percent fewer calls (median 24 percent) than the state-of-the-art risk-controlled policy at the same certified all-miss risk.

---


### 124. [MHR-Router: Multimodal Heterogeneous Retrieval-Enhanced Adaptive Routing for VLM Inference](https://arxiv.org/abs/2610.13278)

**<font color=#1a73e8>作者：</font>** Wenjuan Zhu, Zheming Yang, Yunqing Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) exhibit complementary capabilities, yet selecting the most suitable expert for a given image-question query remains challenging due to heterogeneous multimodal inputs and varying expert strengths. Existing routing approaches rely on text-based cues or static model profiles, failing to capture fine-grained visual evidence and expert-specific failure patterns. To address this, we propose MHR-Router, a multimodal heterogeneous retrieval-enhanced adaptive routing framework for VLM inference. It accurately dispatches each multimodal query to the most suitable VLM expert via local retrieval evidence. MHR-Router consists of two stages: (1) Multimodal Routing Representation, which fuses frozen multimodal features into a comprehensive query representation; and (2) Heterogeneous Retrieval-Enhanced Adaptive Routing, which retrieves expert-specific success and failure memories as local evidence and employs a shared scorer to adaptively select the optimal expert. Experiments show that MHR-Router effectively achieves heterogeneous modality routing and consistently improves accuracy over traditional baselines.

---


### 125. [BoundaryEvo: Data-Model Co-Evolution at the Capability Boundary for Long-Chain Reasoning Distillation](https://arxiv.org/abs/2610.13285)

**<font color=#1a73e8>作者：</font>** Jiaming Su, Suorong Yang, Xudong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distilling long-chain reasoning trajectories from large teacher models provides an effective way to improve the reasoning ability of small language models. However, existing methods typically select a fixed training set before distillation, overlooking that the usefulness of a reasoning example changes as the student evolves. This mismatch becomes especially costly when only a small number of teacher trajectories can be used for training. Besides, examples already mastered provide little new supervision, while examples far beyond the capability of student may be difficult to learn from. Training data should therefore adapt as model capability evolves, yet reliable data selection is difficult when the student is initially weak. To address these challenges, our key idea is to first establish the basic reasoning capability and then adapt the training data to the evolving capability boundary of the student. We propose BoundaryEvo, a two-stage data--model co-evolution framework. In Capability Priming, we directly distill a small set of teacher-generated long reasoning trajectories without using a separate model to judge and filter them, allowing the student to acquire an initial reasoning capability before capability-aware data selection. In Capability-Boundary Co-Evolution, we repeatedly select questions that the current student has not mastered but the expert can reliably solve, and update the training data as the student evolves. With only 1,000 training examples, BoundaryEvo consistently outperforms static and dynamic data selection baselines across 11 reasoning benchmarks, raising the original Qwen3.5-4B accuracy from 62.9 to 75.3 on IMO-AnswerBench and from 26.8 to 46.0 on AMO-Bench. The code and data will be made publicly available.

---


### 126. [Agreement Without Alignment: Label-Free Rubric Clarification Increases LLM-Judge Consensus but Not Agreement with Humans](https://arxiv.org/abs/2610.13303)

**<font color=#1a73e8>作者：</font>** Sangdo Han, Moonsoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM judges are increasingly deployed as panels, and disagreement among panel members is often read as a symptom of an unclear rubric. We test a label-free procedure that turns this disagreement into rubric repairs. The procedure decomposes each rubric into sub-criteria, ranks them by cross-judge disagreement on a development split, and has an editor model rewrite only the most contested ones. An additional stage that moves text-checkable sub-criteria to deterministic checkers transferred none in our evaluation. Human labels are never used to select or edit clauses; they are used only to evaluate the outcome. We pre-specified four hypotheses in a version-controlled protocol and evaluated six rubric conditions with a panel of five judges from three providers on SummEval, the HealthBench meta-evaluation, and USR Topical-Chat, for a total of 129,770 judge requests, excluding retries. On SummEval, the procedure raised inter-judge Krippendorff's $\alpha$ by 0.069 (95% CI 0.046 to 0.092) over the original rubric and by 0.074 over a control that applied the same edits to an equal number of randomly chosen clauses that were not selected. Agreement with expert ratings showed no detectable change (Kendall $\tau$ difference -0.007, 95% CI -0.037 to 0.021). On HealthBench and USR, neither inter-judge agreement nor human agreement met the preregistered effect criteria. In a preregistered secondary comparison, human agreement after editing the contested clauses was lower than after editing the control clauses on all three datasets in point estimate, although no interval excluded zero. Selecting clauses by disagreement makes judges agree with each other more than editing arbitrary clauses does, but in our setting the added consensus did not bring the judges closer to human annotators. We will release code, frozen rubrics, item identifiers, and judge scores.

---


### 127. [Host-Aware Web Crawling for LLM Pretraining Data](https://arxiv.org/abs/2610.13321)

**<font color=#1a73e8>作者：</font>** Malte Ostendorff  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web crawling is a major source of large language model (LLM) pretraining data, yet data-selection pipelines discard a large share of crawled pages. We investigate how a crawler should allocate its budget across and within hosts to collect more high-quality pretraining data. Combining document-level quality classifier scores, web-graph centrality metrics, and Common Crawl's per-host crawl coverage, we find that roughly half of the variation in classifier scores occurs between hosts. In the crawls we analyze, a few pages from a host also provide a useful estimate of the quality of its remaining pages. Common Crawl uses harmonic centrality, a graph centrality metric, to guide its crawl allocation. In our simulations, using centrality to choose which hosts to crawl yields limited gains over random ordering and performs worse for some classifiers. For deciding how deeply to crawl each host, sampling a few pages and then fetching more from hosts with higher-scoring samples collects several times more high-quality pages per fetch than uniform depth or centrality-based allocation. Finally, Common Crawl's observed per-host coverage has little correlation with the evaluated quality signals. We estimate that tens of millions of high-quality pages remain among known but uncrawled URLs in each crawl examined, with most concentrated on a small share of hosts.

---


### 128. [DuoRate: Two-Rate Per-Expert Precision Allocation for Mixture-of-Experts Serving](https://arxiv.org/abs/2610.13328)

**<font color=#1a73e8>作者：</font>** Mengqi Guo, Zhe Wei, Yuan Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serving a Mixture-of-Experts (MoE) model pays for expert precision twice: the resident footprint pays for every expert the router can reach, while each batch-one decode step pays only for the experts it selects. These are two different rate functionals over the same per-expert widths, yet published per-expert MoE allocators constrain only the first. We call the difference the store-read gap; in the released BitsMoE checkpoint, 2.54 bits per weight (bpw) of storage become 7.50 bpw of decode traffic. We propose DuoRate, which stores once and reads per workload. Offline, it stores one uniform tier of a prefix-readable weight stream and bakes a distortion tensor. Online, it profiles a workload's own prefill without labels and solves a Lagrangian rate-distortion allocation under the decode functional; routing frequency provably cancels from every per-expert decision, and the solve costs one dot product per expert and a bisection. A deployment therefore keeps a single artifact that prefill reads at the stored rate and decode reads at the workload's own rate. On Qwen3-30B-A3B, DuoRate reading 2.3 bpw exceeds every 2-bit-class baseline by 6.3 to 47.0 points of average accuracy, and at 2.9 bpw it matches 4-bit formats that read 1.4-1.6 bpw more. The advantage is largest under long decoding: on GSM8K, DuoRate at 2.9 bpw matches or exceeds every 4-bit format and trails BF16 by only 0.25 points, and at 2.6 bpw it still matches or exceeds the 4.5-bit NF4 and FP4. Against controls in its own format, the allocation alone is worth 0.07-0.11 bpw of read rate. Code will be released upon publication.

---


### 129. [Masked Diffusion Language Agents for Tool-Integrated Chemical Reasoning](https://arxiv.org/abs/2610.13330)

**<font color=#1a73e8>作者：</font>** Mengdi Liu, Chenghao Jia, Hong Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing tool-integrated reasoning agent systems for complex chemical tasks remains a fundamental challenge. Although recent chemical agents have demonstrated promising performance through the integration of external tools, they are still built on the autoregressive paradigm, which is inherently constrained by causal attention and left-to-right generation. As a result, they often struggle with bidirectional molecular understanding, global coordinated tool planning and multi-source evidence integration. To address this challenge, we introduce ChemDiffAgent, the first masked diffusion language agent for tool-integrated chemical reasoning. It reformulates chemical reasoning as iterative denoising over interleaved reasoning and tool-use trajectories, enabling tool-use decisions to be jointly determined under full-trajectory context and thereby better aligning the agent's decision boundary with its knowledge boundary. We further analyze how this paradigm benefits agentic reasoning through harder infilling subproblems during training and flexible arbitrary-order decoding during inference. Then we develop a two-stage post-training framework, comprising agentic supervised fine-tuning and variance-reduced preference optimization, to enhance tool-use and reasoning capabilities. We also construct a comprehensive benchmark covering six chemistry tasks across both single-turn and multi-turn tool-use scenarios. Under matched budgets and evaluation, ChemDiffAgent consistently outperforms autoregressive agents, achieving an overall improvement of approximately 20%. Notably, our 8B model achieves performance comparable to, in some cases surpassing, significantly larger frontier models, such as GPT 5.5 and Claude Opus 4.7. Code is available at this https URL.

---


### 130. [PDE-PFN: Prior-Data Fitted Neural PDE Solver](https://arxiv.org/abs/2610.13334)

**<font color=#1a73e8>作者：</font>** Jaehyeon Park, Mingu Kang, Dongseok Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by the success of large language models (LLMs) with broad generalizability and robustness to noisy or unreliable pre-training data, we explore in-context prediction of PDE solution fields using approximate pre-training data. In addition, inspired by the posterior predictive mean-based inference mechanism of the in-context learning in prior-data fitted networks (PFNs), we propose PDE-PFN, a prior-data fitted neural solver that approximates the posterior predictive mean of PDE solutions via in-context learning. PDE-PFN builds on a PFN architecture with self- and cross-attention mechanisms of Transformer and is pre-trained on noisy approximate solutions generated by physics-informed neural networks, serving as diverse but not necessarily exact priors. Through experiments on a range of two-dimensional PDEs, we demonstrate that PDE-PFN achieves empirical generalization across heterogeneous equations, robustness under noisy priors, and zero-gradient-update in-context inference capability. PDE-PFN achieves competitive or improved predictive accuracy relative to the evaluated baselines while supporting flexible context and query representations.

---


### 131. [AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents](https://arxiv.org/abs/2610.13335)

**<font color=#1a73e8>作者：</font>** R E Zera Marveen Lyngkhoi, Abhivansh Gupta, Vidushee Vats 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-using agents increasingly require a common substrate for building, training, evaluating, distilling, and maintaining agentic systems, yet existing tooling typically addresses these stages in isolation. We present AgentTune, a source-available Python library that provides a unified framework for developing and optimizing tool-using agents. At its core, AgentTune introduces a two-tier EventLog representation that preserves agent trajectories while supporting consistent projections for training, evaluation, and auditing. Building on this substrate, the library provides a shared agent runtime, tool-calling reinforcement learning, agentic distillation, retrieval-augmented generation, decision workflows, evaluation utilities, and a designed path toward self-healing agents. These components are exposed through composable interfaces so that agent strategies, training methods, evaluation procedures, and recovery mechanisms can be combined without requiring separate representations or pipelines. We demonstrate the framework across agentic tasks including legal contract search and domain-specific applications, illustrating its use for trajectory-based optimization, tool-use evaluation, and cross-task agent development. AgentTune is released as a source-available library at this https URL

---


### 132. [Exploring Attention Sinks in Text-to-Image Transformers from Diffusion and Autoregressive Models](https://arxiv.org/abs/2610.13337)

**<font color=#1a73e8>作者：</font>** Binglei Li, Mengping Yang, Zhiyu Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attention sinks are tokens or positions that consistently receive disproportionate attention mass, often beyond what their semantic content would suggest. Despite extensive study in large language models, their behavior and functional relevance in text-to-image (T2I) Transformers remain largely unexplored. To fill this gap and better understand how text-to-image Transformers allocate and route attention, we explore this phenomenon of text-to-image transformers across bidirectional diffusion models and causal autoregressive models. Specifically, we explore whether attention sinks exist, where they emerge, and how they functionally influence generation. Through systematic attention analysis and targeted interventions, we identify that attention sinks emerge in both bidirectional diffusion and autoregressive models but exhibit distinct patterns. The autoregressive model concentrates attention on the first and global-scale tokens, whereas the bidirectional models develop sinks near modality boundaries, within text regions, and at spatial corners. Moreover, these patterns vary across generation stages and are localized to a sparse subset of layers and heads. To assess their functional relevance, we perturb sink-related heads and token positions. It turns out that perturbing sink-ranked heads produces larger average changes than non-sink comparisons, while some sink-position perturbations have limited effects on bidirectional model scores. We further introduce register tokens to redistribute attention sinks and find that several configurations preserve or modestly improve generation performance. Overall, attention sinks are architecture-, inference-stage-, and component-dependent phenomena, providing a basis for mechanistic analysis and principled attention design in text-to-image transformers.

---


### 133. [Understanding Mamba-3 Through Oscillatory Dynamics](https://arxiv.org/abs/2610.13341)

**<font color=#1a73e8>作者：</font>** Shutian Liang, Yue Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mamba-3 introduces input-dependent rotations into recurrent state updates, but their contribution beyond state retention remains unclear. We interpret these ro- tations as underdamped second-order dynamics, providing a framework for in- vestigating the role of oscillation in sequence modeling. Controlled comparisons show that underdamped dynamics outperform non-oscillatory damping regimes on state-tracking tasks, while language-model pretraining demonstrates benefits for long-context prediction and length generalization. Interventions in pretrained models further establish the importance of learned phase, and state analysis sug- gests that rotation regulates how retained information combines with incoming up- dates. Taken together, these findings identify underdamped dynamics as a useful mechanism for recurrent computation and suggest that oscillation supports long- context processing by regulating how information accumulates.

---


### 134. [Test-Time Memory Construction](https://arxiv.org/abs/2610.13348)

**<font color=#1a73e8>作者：</font>** Zijun Wang, Yifan Ji, Haidong Xin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) struggle to answer questions over long interaction histories, where relevant evidence may be scattered across distant sessions. Existing memory systems typically construct and maintain sophisticated memory representations offline, before user queries are observed, incurring substantial overhead and limiting their ability to adapt memory construction to query-specific information needs. In this paper, we propose T$^2$Mem, a Test-Time Memory construction framework that defers memory construction to inference and progressively builds memory along the reasoning process. Specifically, T$^2$Mem extracts lightweight episode-level metadata offline to capture key events and temporal associations as retrieval cues, while retaining links to the original interactions to facilitate the reconstruction of dependencies across episodes. At test time, the LLM adaptively retrieves and organizes metadata and raw interactions, progressively constructing query-specific memory as reasoning unfolds. Experiments on LoCoMo and LongMemEval show the effectiveness of T$^2$Mem by consistently outperforming strong baselines across different backbone LLMs while substantially reducing the overhead of memory construction. Further analysis demonstrates that deferring memory construction to inference enables the memory construction process to dynamically adapt to the information needs of individual queries. All code is available at this https URL.

---


### 135. [SWE-Critix: Post-Training Generalist Verifiers for Assessing Coding-Agent Trajectories](https://arxiv.org/abs/2610.13356)

**<font color=#1a73e8>作者：</font>** Jiajun Hu, Chun Yong Chong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are increasingly deployed for end-to-end software engineering tasks, where a readily available oracle evaluator that defines the success criteria is often absent. This motivates verifications for coding agents that can reliably judge and explain their behavior. However, verification is non-trivial as coding agents are increasingly capable of solving long-horizon software engineering tasks. Their execution trajectories can be extremely long, containing hundreds of iterative interactions with code repositories and external tools. Existing verifiers either rely on general-purpose LLMs without specialized training or train dedicated critics that predominantly focus on producing scalar rewards, highlighting the relatively limited exploration of training-based generalist verification. We introduce SWE-Critix, a post-training pipeline for training generalist verifiers of coding-agent trajectories. Given a task and its execution trajectory, the learned verifier predicts the completion label and generates a natural-language analysis that explains its judgment. Our pipeline combines supervised fine-tuning (SFT) with reinforcement learning (RL) and trains a series of 30B models on trajectories from CodeForge-Preview. On a held-out test set, SWE-Critix improves classification accuracy from 57% for the base Qwen3-30B-A3B reasoning model to 66% after SFT and 78% after RL. We release our models, datasets, and training code to facilitate further research.

---


### 136. [Overcoming Data Imbalances with Expert Selection Biases](https://arxiv.org/abs/2610.13370)

**<font color=#1a73e8>作者：</font>** Ayush K. Tarun, Clara Meister, Antoine Bosselut  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models have become the standard architecture for frontier LLMs. The multiple parallel experts in each transformer block theoretically enable expert specialization according to categories such as domains, languages, or modalities during pretraining. However, when data is imbalanced across categories, minority categories can become concentrated in a small fraction of the expert pool or spread inefficiently across them, effectively limiting their available capacity. In this work, we demonstrate that category-conditioned expert-selection biases can preferentially route tokens from different categories toward specialized expert pools. By applying biases based on input category, we provide a simple way to induce soft category-aligned specialization. This intervention encourages categories toward distinct expert subsets while retaining cross-category sharing when useful. More importantly, it enables the over-allocation of expert capacity to categories that would otherwise be disadvantaged by data scarcity. We observe performance improvements across modalities, low-resource languages, and code in models up to 10.6B parameters. At our smallest and largest model scales, these gains are equivalent to allocating 18.5% and 2.7% additional baseline training tokens, respectively. Overall, our results show that expert biases can serve as a lightweight control for category-level expert allocation, making room for low-resource categories while retaining standard MoE inference.

---


### 137. [From Structure to Validity: Mechanism-Guided Generation and Refinement of LLM Rubrics](https://arxiv.org/abs/2610.13375)

**<font color=#1a73e8>作者：</font>** Feifei Qian, Xuan Chen, Lixin Cui 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubrics have been widely used to evaluate and optimize language models on open-ended tasks. However, existing work primarily focuses on generating better rubrics, with limited understanding of what makes rubric design effective. In this work, we conduct a systematic mechanistic analysis of rubric design across criterion organization, criterion operationalization, and score aggregation. Our analysis shows that structural organization enables more comprehensive criterion construction, semantic specification alone does not ensure effective criterion-level judgments, and sophisticated score aggregation provides limited additional gains. Guided by these findings, we introduce Adaptive Rubric Tree Search with Hybrid refinement (ARTS-Hybrid), which combines adaptive tree construction with semantic-first, response-calibrated refinement. Experiments across benchmarks show that ARTS-Hybrid improves both end-to-end evaluation performance and intrinsic rubric quality. Further experiments suggest that, beyond evaluation, rubrics generated by ARTS-Hybrid provide effective signals for model optimization.

---


### 138. [MoPrO-SD: Modular Prompt Optimization for Stance Detection](https://arxiv.org/abs/2610.13386)

**<font color=#1a73e8>作者：</font>** Meysam Sabbaghan, Nikesh Gyawali, Arman Zareian Jahromi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stance detection remains challenging for large language models (LLMs) due to implicit opinions, sarcasm, and context-dependent expressions of stance. Although automatic prompt optimization offers an alternative to fine-tuning without updating model parameters, existing structured approaches are not specifically designed around stance-label semantics and class-specific ambiguities. We introduce MoPrO-SD, a stance-specific prompt optimization framework that decomposes prompts into functional semantic modules and refines them sequentially using LLM-based feedback. We study three refinement strategies: instruction-only optimization (I), instruction with reasoning (I+R), and instruction with per-example reasoning (I+R+E), using class-conditioned errors for stance-label refinement. We also introduce VaccineStance, a new human-annotated benchmark for vaccine stance detection. Experiments across four datasets and five open-weight LLMs show that MoPrO-SD improves upon the human-written Base prompt in many settings. On SemEval-2016, class-conditioned feedback achieves higher mean Macro-F1 than pooled feedback for four of five backbones. Both reasoning-based strategies, I+R and I+R+E, achieve strong performance, with their relative effectiveness varying across models and datasets, while remaining competitive with recent prompt optimization methods. The MoPrO-SD code and VaccineStance dataset are available on GitHub.

---


### 139. [Towards the Roof of the World: NLP Progress in Tibetan Languages](https://arxiv.org/abs/2610.13398)

**<font color=#1a73e8>作者：</font>** Xi Cao, Yijie Li, Yuan Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tibetan, spoken by some seven million people on and around the Qinghai-Xizang Plateau, remains underrepresented in natural language processing (NLP). We present, to our knowledge, the first peer-reviewed systematic bibliometric survey of Tibetan NLP: 140 publications from 2004 to 2026 in the ACL Anthology and DBLP, annotated for venue type, research area, first-affiliation country, and resource release. Output has grown rapidly, with 84% of the publications appearing since 2018, and has expanded bottom-up along the NLP pipeline, from corpora and word segmentation through script, speech, and applications to large language models (LLMs). Researchers based in China first-authored 87% of the publications, which span all 25 represented research areas, whereas work from other countries concentrates on Classical Tibetan. We argue that this full-pipeline paradigm, realized under the compounded constraints of a complex script, dialectal diversity, and geographic remoteness, offers a reference model for other low-resource languages of the Global South. We also identify gaps in dialect coverage, responsible NLP, native and comparable evaluation, cross-community visibility, and resource release (only 29% of the publications release data, code, or models), and recommend open science, shared standards, and community participation for the LLM era.

---


### 140. [RegulaTutor: A Theory-Informed Framework for Long-Term Personalized Learning](https://arxiv.org/abs/2610.13399)

**<font color=#1a73e8>作者：</font>** Yonggang Li, Boqian Han, Rui Sheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term personalized tutoring requires language models to translate a learner's evolving history into appropriate instructional support. Existing LLM-based tutoring systems use memory and retrieval to personalize responses, but the pedagogical rationale linking historical evidence to teaching strategies is not always explicit. We introduce RegulaTutor, a theory-informed framework for long-term personalized tutoring that connects historical evidence, learner interpretation, and learner-facing instruction. Guided by self-regulated learning (SRL) research, its tutoring harness operationalizes a cognitive, affective, metacognitive, and motivational (CAMM) framework for deriving evidence-supported learner interpretations and teaching policies. The resulting policies retain links to their supporting evidence and are updated as new observations arrive. This staged workflow also supports systematic refinement through PairRoute, an offline procedure that uses intermediate execution records to distinguish harness, model, and mixed failures. PairRoute proposes and evaluates targeted harness revisions, then constructs reviewed stage-level supervision for confirmed model failures remaining under the selected harness. We focus this refinement on historical evidence acquisition, which underpins personalized instruction and allows outputs to be checked against learning records and reference answers. RegulaTutor improves historical-evidence accuracy, learner diagnosis, and judged teaching quality on average across evaluated model configurations. PairRoute results show an endpoint improvement in standalone-model historical-evidence accuracy over the refinement trajectory. Together, these results highlight RegulaTutor's potential to support lifelong personalized education through instructional policies that evolve with learner histories and targeted improvements to the tutoring system.

---


### 141. [In-Context Learning for System Identification: Probabilistic Formulation, Long-Sequence Handling, and Benchmark Validation](https://arxiv.org/abs/2610.13411)

**<font color=#1a73e8>作者：</font>** Matteo Rufolo, Dario Piga, Filippo Pura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional system identification typically involves two steps: initially, training data is processed to estimate a model of the system of interest; then, the model is used to predict outputs for new input queries. In contrast, recent in-context learning approaches learn a meta model that maps directly from training data and query inputs to outputs in a zero-shot fashion, bypassing explicit model estimation. This approach leverages a meta model trained offline, on large sets of synthetically generated data, to emulate the behavior of a system identification algorithm. In this work, we advance this meta-learning framework for system identification in three directions. First, we develop a unified probabilistic meta-identification architecture that combines a Transformer-based encoder-decoder with tailored mechanisms for handling long training sequences, enabling calibrated predictions over long horizons. Second, we show how a pre-trained meta model can act as an uncertainty-aware synthetic data generator for classical system identification, providing task-specific data that regularize parametric models when real data are scarce. Third, we systematically evaluate the framework on standard nonlinear system identification benchmarks and on a challenging out-of-distribution scenario, demonstrating competitive accuracy with state-of-the-art methods and strong generalization, including cases where input-only adaptation is sufficient to handle significant distribution shifts.

---


### 142. [TextVBench: Evaluating Text Rendering and Preservation in Video Generation](https://arxiv.org/abs/2610.13412)

**<font color=#1a73e8>作者：</font>** Ruiqiang Zhang, Hengyi Wang, Chang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video generators can synthesize convincing scenes while rendering a few characters incorrectly, omitting requested text, or changing it across frames. Measuring these failures is harder than applying OCR independently to each frame: when a scene contains multiple text targets and multiple noisy OCR regions, the evaluator must first determine which observation belongs to which intended text. We introduce TextVBench, a benchmark and evaluation framework that formulates visual-text evaluation as a multi-target, multi-instance spatiotemporal correspondence problem. TextVBench contains two complementary tracks: TextVBench-T2V measures the creation and maintenance of prompt-specified text, while TextVBench-Ref2V measures preservation of text from reference images. Both tracks use target-conditioned candidate selection rather than unconstrained VLM transcription, support one target mapping to multiple OCR regions, and separate frame-level spatial fidelity from cross-frame temporal fidelity. A length-weighted harmonic score summarizes these factors, while extra-text diagnostics expose failure modes hidden by a single OCR score. The benchmark is organized around controlled text, layout, carrier, and motion attributes so that aggregate scores can be traced back to specific capability limits. Across the evaluated model runs, MiniMax-H3 reaches a T2V TextVScore of 68.32, while the strongest Ref2V score is 56.51; attribute slices reveal a pronounced drop as the number of simultaneous reference text regions increases.

---


### 143. [Web$hell: A Unified Interface for Agentic Web Access](https://arxiv.org/abs/2610.13416)

**<font color=#1a73e8>作者：</font>** Sunghwan Kim, Deogyong Kim, Sangam Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are becoming direct users of the open web. As they take on increasingly complex and information-intensive tasks, effective web access is becoming a core capability for agentic problem solving. Existing approaches have advanced agentic web access through different access models, including search-augmented agents, browser-based agents, and, more recently, filesystem-based agents. Nevertheless, as users expect agents to complete long-horizon, end-to-end tasks, they increasingly need to conduct broad information gathering, perform browser actions, and revisit acquired evidence within a single trajectory. Yet our preliminary analyses reveal that existing access models struggle to meet these demands. They primarily support either information gathering or browser interaction, while combining their capabilities can involve substantial costs or performance trade-offs. To this end, we present Web\$hell, an interface that unifies web access under a single access model. Using a common schema defined by WebContract, WebCompiler compiles live webpages into addressable information and action objects. These objects are maintained in WebCache and handled through a shared set of operations, providing agents with consistent, operable, and persistent web access. Through extensive experiments across web search, web navigation, and deep research benchmarks, we show that Web\$hell achieves strong task performance at lower cost. Our results further indicate the importance of interface design for effective web access, with Web\$hell opening new possibilities for more capable and efficient LLM agents on the web.

---


### 144. [When AI Advisors Agree: Distinguishing Forecast Risk from Forecast Reliability](https://arxiv.org/abs/2610.13431)

**<font color=#1a73e8>作者：</font>** Russlan Ramdowar  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> If seven AI advisors give similar forecasts, should we trust them more? Agreement can indicate useful shared evidence, but it can also reflect an asset that was easier to forecast in the first place. We examine this distinction using 928 completed first-quarter forecasts for 232 assets across four production batches of iPulse AI. Ten historical Gemini configurations are grouped into seven investment frameworks; their archived forecasts are compared with later market outcomes, without generating new reports. Mean absolute return error rises from 10.31 percentage points in the lowest-disagreement quartile to 21.05 in the highest. Yet a forecast of no price change shows almost the same increase, from 9.89 to 21.15. The relationship between disagreement and additional forecast error is not resolved after accounting for visible asset risk. Retaining the quarter of forecasts with lowest historical volatility produces lower error than retaining those with least disagreement: 7.97 versus 10.31 percentage points. Agreement about direction behaves differently. When at least six of seven frameworks share a direction, directional accuracy is higher, but return-magnitude error is also larger. These results distinguish three questions often collapsed into one confidence score: how risky the asset is, whether advisors agree on its direction, and how precisely they forecast its return. For this historical council, agreement is informative in specific ways; it is not a general certificate of forecast reliability.

---


### 145. [Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Policy Limits](https://arxiv.org/abs/2610.13438)

**<font color=#1a73e8>作者：</font>** Chen Xi, Ding Ruixue, Wang Zhigaoyuan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as a key paradigm for improving large language model (LLM) agents, enabling stronger reasoning, planning, and tool-use in interactive environments. However, existing agent RL methods remain fundamentally constrained by an on-policy reasoning bottleneck: when tasks exceed the model's current capability boundary, effective trajectories become extremely sparse and training often collapses. We introduce Rollout-Time Intervention (RTI), a technique designed to elicit successful trajectories beyond the policy's intrinsic exploration capacity. RTI operates by leveraging reward-side evidence (i.e., evaluation rubrics) during rollout to convert erroneous trajectories into successful ones, providing effective learning signals for tasks that the policy rarely solves on its own. Although intervention trajectories are inherently off-policy, we find that they can effectively guide policy optimization when trajectories with excessive distributional shifts are filtered out. Extensive experiments across five benchmarks demonstrate that RTI consistently outperforms RL baselines, enabling the post-trained policy to approach the performance of substantially stronger contemporary LLMs and, more importantly, transcend its original capability boundary. The code is available at this https URL.

---


### 146. [Agentic Large Language Models](https://arxiv.org/abs/2610.13455)

**<font color=#1a73e8>作者：</font>** Max van Duijn, Michiel van der Meer, Aske Plaat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have taken the world by storm. Their ability to communicate with us in our own language, and to reason about our world, has made them a favorite tool for writing, answering questions, and much more. Their answers already influence our decisions and our actions. What would happen if LLMs themselves could act in the world directly? What would happen if LLMs could interact with each other? Agentic LLMs combine the power of large language models with the ability to act in the real world. In this book we will discuss how agentic LLMs work, how they act, how they interact, and what this means for us, as users.

---


### 147. [SqueezeBench: Saturation-Resilient Evaluation of Mathematical Capability](https://arxiv.org/abs/2610.13461)

**<font color=#1a73e8>作者：</font>** Pablo Manrique, Hai Xia, Stefan Szeider  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are making rapid progress in mathematics, but this progress is hard to measure. Benchmarks of solved problems saturate, and in benchmarks of open problems each problem can be resolved for the first time only once. We present SqueezeBench, a benchmark that is resilient to saturation: a success raises the bar instead of removing the problem. Each problem fixes an integer function $f(n)$ whose values are known only for small $n$, and the benchmark keeps a lower and an upper record on it. A record is a computable Lean function with a machine-checked proof that it bounds $f$. A submission proposes a new function and proves that it bounds $f$, that it is no worse than the current record at any $n$, and that it is strictly better at some $n$. Once accepted, it becomes the record that the next submission has to beat. The system thus chooses the bound as well as its proof, and it may improve the record at a single $n$ or its growth rate. At every $n$, the gap between the two records shows how far the certified bounds are from determining $f(n)$. Every proof is checked by two independent Lean kernels, so no referee needs to check the mathematics. The checks also reject a function that computes $f$ by exhaustive search at small $n$, and a maintainer only reads the submitter's report and looks for such a search at larger $n$. We release ten problems from extremal combinatorics with twenty proved initial records and the admission tools. As a baseline, agents based on a frontier language model, with at most one hour per record, had 82 submissions accepted and improved every record, without going beyond the published literature. Agents based on two newer models then started from these records, had 60 more submissions accepted and improved 19 of the 20 records again. For eight of the ten problems, at least one record is still asymptotically behind the best published bound.

---


### 148. [When MLLMs miss what humans read: diagnosing and learning to read squint text](https://arxiv.org/abs/2610.13465)

**<font color=#1a73e8>作者：</font>** Chen Peng, Shan Huang, Jianbo Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal LLMs can fail to read text embedded in an image's coarse structure (text a human recovers by squinting) and report that no text is present. We name this class Squint Text and study it as a recognition deficiency, motivated by cases from a production moderation pipeline. We introduce SquintBench, comprising 1076 production-derived moderation images, and SquintCtrl, a controlled synthetic suite for mechanism diagnosis. Frozen-weight analysis shows that hidden text leaves a coarse signal while glyph identity is weakly represented; identity becomes substantially more accessible when the correct spatial regions are supplied, implicating spatial selection as a major bottleneck. Suppressing high-frequency content also improves reading at a fixed visual-token budget, while visual token count may also contribute. These findings motivate Squint OPSD: a frozen teacher receives a downscaled view and the ground-truth transcription as privileged context, and its token-level distributions supervise a student along on-policy trajectories. At inference, the student reads the original image alone. Squint OPSD reaches 88.61 ANLS on SquintBench, versus 26.50 for the unadapted backbone, 24.44 for the best general-purpose model on the original view, and 68.60 at best for an off-the-shelf model under a downscaled view. These results substantially narrow the gap between available visual evidence and its generated read-out without auxiliary views at inference.

---


### 149. [A Local Agentic AI Framework to Generate Edge Case Scenarios for Safety Assurance](https://arxiv.org/abs/2610.13479)

**<font color=#1a73e8>作者：</font>** Victoria J. Hodge, Colin Paterson, Rob Alexander  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating edge case scenarios is crucial for training, testing and safety assuring autonomous systems. This identifies hazardous failures to increase system reliability and robustness, ensures the system can still function safely on the boundaries of its operational design domain and learns the expected system behaviour for these edge cases. The rapid advancement in the generation and analysis capabilities of language models (LMs) has expanded their applicability and recent work has investigated LM scenario generation. However, many recent approaches rely on human-in-the-loop or rule-based strategies. This restricts the LM's ability to generate diverse and edge case scenarios; the long tail of the distribution. Our work uses local LMs in a laptop-based agentic AI framework for adaptive scenario generation. This is cheap, fully-controlled, ensures data privacy and security. It uses think, act, observe, update, and continue loops with lightweight JSON encoding to generate scenarios. We use the system requirements, system description and environment description as knowledge bases in contextual prompts for an LM to ensure scenario realism. A second, independent LM critiques each scenario using domain specific criteria so it can be refined. The refined scenarios are run in simulation and evaluation metrics collected. These metric scores are analysed and similar scenarios are created for edge cases (exploitation) or novel scenarios are generated to explore the scenario space. Post-hoc clustering using metric scores and thematic-type analysis of the rich-text scenario descriptions produced by the LM pinpoints functional gaps and their triggering conditions. This creates traceable evidence for the safety assurance case. Our work highlights the potential of a flexible and adaptive local agentic AI framework for automating edge case generation and producing traceable safety assurance evidence.

---


### 150. [Branching On-Policy Distillation](https://arxiv.org/abs/2610.13481)

**<font color=#1a73e8>作者：</font>** Dongyang Chen, Shudong Liu, Shubo Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) provides teacher supervision on student-generated trajectories, but a single trajectory realizes only one continuation at each decision, limiting supervision coverage under a finite sampling budget. We propose BranchOPD (Branching On-Policy Distillation), which selects informative decision points using student uncertainty and teacher-student disagreement, resamples student-policy continuations from shared prefixes, and applies token-level teacher supervision to both main trajectories and branches. BranchOPD operates at token-level decisions in mathematics and within-turn decisions in agent tasks. Shared-prefix reuse reduces student-generated token costs by approximately 19% on ALFWorld and 31% on WebShop relative to seven independent trajectories. We also introduce protocol-boundary repair (PBR), which uses targeted supervision under protocol constraints to mitigate repetition and wasted generation. BranchOPD outperforms Vanilla OPD and Multi-Rollout OPD (n=7) across all evaluated benchmarks, with gains over Vanilla OPD of 18.55 percentage points in mean mathematics accuracy over 16 sampled answers (avg@16) and 13.8 points in mean ALFWorld ID/OOD success. Mechanistic analyses and selection ablations show that branching at uncertain decisions expands subsequent behavior coverage and outperforms random selection and turn-initial branching.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-230](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
