# 🧠 大模型相关研究 | 2026年10月14日

> 本类共 **230** 篇论文：已确认 **202** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-230](./part-05.md)

---

### 51. [Collaborative Theory of Mind: Learning to Self-Revise by Anticipating User Responses](https://arxiv.org/abs/2610.12872)

**<font color=#1a73e8>作者：</font>** Fanzhi Zeng, Anubrata Das, Maytal Saar-Tsechansky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate strong individual task performance, yet still struggle to collaborate with users over extended, multi-turn interactions, for example by attempting solutions before understanding the user's needs or by failing to revise mistaken assumptions after receiving feedback. We propose Collaborative Theory of Mind (CToM), a framework that addresses these challenges by explicitly training LLMs to anticipate user responses and to use those predictions to improve their own behavior. CToM drafts a response, predicts how the user will respond, and uses this prediction to guide internal revision before presenting a response. During training, the user's reply to each draft serves as the target for predicting the next turn, and we train the assistant to minimize the negative log-likelihood of that reply. We combine this prediction objective with group-relative policy optimization (GRPO) to optimize both task performance and interaction efficiency. Across mathematical reasoning, coding, and writing tasks, CToM achieves higher collaborative task performance than all baselines; for example, on a collaborative mathematical reasoning task, it improves final accuracy from 74.1% to 79.6% compared with naive GRPO. Ablations show that predicting user responses also makes collaboration more efficient: under the same reward, adding prediction supervision reduces the number of user replies by 8% on coding and 17% on writing while improving task performance. Behavioral analyses of interaction trajectories show that user-response predictions become more accurate after training, and that more accurate predictions are associated with larger improvements in collaborative task performance through self-revision.

---


### 52. [Temporal Evidence Forests for Long-Horizon Multi-Party Conversational Memory](https://arxiv.org/abs/2610.12874)

**<font color=#1a73e8>作者：</font>** Junyou Guo, Chongyang Tao, Yan He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory has been widely adopted in LLM-based agents to support persistent interaction and personalized assistance. Long-term multi-party interactions, however, accumulate substantially more detailed information, with decisions repeatedly updated and states evolving across participants and interaction stages. Temporal structure is therefore crucial for tracing such memories: relevant information often appears densely within short intervals, while transitions among different states are anchored by a strict temporal order. Existing temporally aware memory frameworks primarily store time as metadata or use temporal signals to guide retrieval over preconstructed memory structures, without using temporal structure to both recover locally concentrated evidence and reconstruct its complete event progression. To address these limitations, we propose T-Mem, a temporal-structure-based memory framework that preserves interactions and organizes query-relevant evidence through two temporal mechanisms. Temporal Evidence Discovery exploits the local concentration of related messages to recover overlooked evidence, while Temporal Memory Structuring models state transitions and supporting relations over time and compresses low-information spans within the resulting forest. Evidence Forest Linearization then serializes the structured evidence for answer generation. Experiments on two long-term multi-party memory benchmarks demonstrate that T-Mem consistently outperforms competitive memory frameworks across LLMs, parameter settings, domains, and query types.

---


### 53. [One-Step Text Generation by Seq-Drifting](https://arxiv.org/abs/2610.12879)

**<font color=#1a73e8>作者：</font>** Jiayu Liu, Ruizhi Zhao, Tianyun Ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models generate tokens in parallel, but still require multiple sampling steps to produce high-quality text. In this paper, we investigate whether a model can learn to generate an entire sequence in a single forward pass. We propose Seq-Drifting, a framework that applies drifting to sequences of continuous token representations and directly learns a map from Gaussian noise to text. Unlike existing DLMs that derive the supervision at each position directly from the observed token in a training sequence, Seq-Drifting builds a drift field whose position-wise targets adapt to the current generated context. At each position, attraction guides each output toward a set of contextually plausible token representations, while repulsion discourages collapse across samples and repetition within sequences. The generator learns from this drift field during training and produces all tokens jointly in one pass at inference. Empirically, Seq-Drifting achieves a generative perplexity of 36.01 on LM1B in one step and performs competitively in both unconditional and conditional generation. Experiments on translation, summarization, and reasoning further demonstrate the applicability of the framework beyond open-ended generation. These results suggest that drifting over token sequences offers a promising path toward effective one-step text generation. Our code is available at this https URL.

---


### 54. [Mind the Spatial Gap: A Benchmark for Geospatial Reasoning and Constrained Spatial Editing](https://arxiv.org/abs/2610.12881)

**<font color=#1a73e8>作者：</font>** Zheng Ren, Yanning Wang, Ziheng Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding and manipulating spatial relations is fundamental to AI systems that reason about physical environments and construct grounded world models. However, existing evaluations of multimodal large language models (MLLMs) for spatial reasoning rely predominantly on static question-answering (QA) over small-scale or synthetic scenes, rarely probing whether models can modify spatial configurations while satisfying explicit geometric constraints. We introduce GeoSpatialBench, a benchmark designed to evaluate an escalating progression of spatial cognition, ranging from spatial relation understanding and geometric reasoning to constrained spatial editing. Grounded in real-world urban data across six geographically diverse cities, GeoSpatialBench evaluates a comprehensive taxonomy of 28 topological, directional, metric, and ordering relations across structured GeoJSON and map image modalities, with ground-truth references and constraints verified via GIS operations. Our empirical evaluation across frontier MLLMs uncovers a stark spatial gap: structured GeoJSON consistently outperforms map images, with multimodal combinations offering no reliable gain over GeoJSON alone, and while models show reasonable competence on qualitative topological and ordering, performance drops on quantitative metric relations. Crucially, editing performance on ordering relations declines relative to QA, and most failed edits violate at least one specified spatial constraint. These results highlight a gap between passively recognizing spatial relations and actively manipulating geometric configurations. GeoSpatialBench provides an open, rigorous diagnostic testbed to benchmark these spatial limitations, laying essential empirical groundwork for physically grounded world models and embodied spatial AI.

---


### 55. [Personalized Federated Direct Preference Optimization via LoRA Adapters](https://arxiv.org/abs/2610.12885)

**<font color=#1a73e8>作者：</font>** Zhanhong Jiang, Soumik Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Direct Preference Optimization (FedDPO) enables privacy-preserving alignment of language models across distributed agents without centralizing sensitive preference data. However, existing FedDPO analysis assumes all clients converge to a single shared policy, which is fundamentally at odds with the heterogeneous preference distributions present in practice. We propose Personalized FedDPO (pFedDPO), in which each client maintains a small private LoRA adapter atop a shared global base model. In pFedDPO, the base model is synchronized via FedAvg each round, while LoRA adapters remain local and capture client-specific preference patterns. We prove that this decomposition replaces the gradient diversity $\kappa^2$ in the FedDPO bound with a residual heterogeneity $\kappa^2_{\mathrm{eff}}$, which is no larger than $\kappa^2$ when adapters absorb client-specific directions, at the cost of an additive adapter-bias term that vanishes as adapters converge. Experiments on preference datasets show that pFedDPO consistently attains a lower gradient norm than vanilla FedDPO while remaining competitive in training loss and per-client reward accuracy.

---


### 56. [Rethinking the Roles of Diffusion and Decoding: Predictive-State Flows for Parallel Language Generation](https://arxiv.org/abs/2610.12898)

**<font color=#1a73e8>作者：</font>** Jinjin He, Xinsong Feng, Lucheng Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In continuous diffusion language models (DLMs), latents generated by the diffusion prior are mapped almost deterministically to tokens, either by a decoder or through a token embedding matrix. Unlike in image generation, where visual details can vary continuously, the diffusion prior must capture fine-grained discrete token choices in continuous space, which can make the joint latent distribution difficult to model. We argue that generative roles should instead be divided: the diffusion prior should generate high-level predictive information, while the decoder should resolve the remaining token-level choices. Based on this view, we introduce Predictive-State Flows (PSF), which partitions a sequence into blocks and associates each block with a predictive state computed solely from the preceding context. A rectified-flow prior generates the sequence of predictive states, after which a block-causal decoder generates all blocks in parallel, autoregressively only within each block. This design reduces diffusion from L token-level states to K << L predictive states and reduces token-level sequential depth to L/K. On unconditional OpenWebText generation, a 197M-parameter model with K=8 achieves a generative perplexity of 22.8 at entropy 5.16 using 0.31 TFLOPs per 1024-token document, versus 24.0 and 7.2 TFLOPs for ELF-B with 32 sampling steps. The corresponding measured operating points yield MAUVE@512 of 0.93 and 0.73, respectively. Controlled comparisons further show that content states, which additionally encode their own blocks, yield 8-16% higher generative perplexity than predictive states, and that replacing sampled predictive-state trajectories with a shared mean lowers MAUVE@512 by 0.11. These results suggest that latent design for continuous DLMs should consider not only how compactly text is represented, but also how generative roles are divided between the prior and the decoder.

---


### 57. [BLEND: Balancing Personalization vs. Generalization in Federated Vision-Language Models](https://arxiv.org/abs/2610.12907)

**<font color=#1a73e8>作者：</font>** Payam Abdisarabshali, Fardis Nadimi, Kasra Borazjani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated vision-language models (FedVLMs) represent one of the emerging frontiers of machine learning, aiming to integrate federated learning within the fine-tuning pipelines of vision-language models (VLMs). In this work, we introduce BLEND, a new framework designed to jointly enhance the personalization and generalization capabilities of FedVLMs. BLEND proposes a selective VLM parameter fine-tuning and aggregation strategy that consists of (i) global vision and text adapters shared across clients, and (ii) a personalized vision projection adapter tailored to each client. BLEND further introduces a novel loss function that blends the outputs of the global and personalized adapters to achieve personalization, while simultaneously promoting generalization through a principled anchor design implemented via the projection heads of the zero-shot VLM. Extensive experiments demonstrate that BLEND consistently outperforms state-of-the-art baselines, highlighting its ability to effectively balance personalization and generalization across diverse system settings. (Code is available at: this https URL)

---


### 58. [OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models](https://arxiv.org/abs/2610.12914)

**<font color=#1a73e8>作者：</font>** Xule Gao, Xi Wang, Zehua Zang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models have shown strong promise in robotic manipulation, yet their post-training still predominantly relies on trajectory-level supervised imitation over robot demonstrations. While effective for learning feasible actions, this paradigm supervises policies to reproduce expert actions at each step, biasing them toward demonstration-specific action paths and providing limited guidance for recovering toward task-progress states once execution deviates from demonstrated trajectories. To address this limitation, we propose OGPO, an Offline Goal-conditioned Policy Optimization framework for recoverable VLA post-training. Instead of treating offline demonstrations merely as step-wise action labels, OGPO adaptively relabels trajectories with semantic key states and constructs goal-conditioned process rewards to optimize the policy for reaching these task-progress states. In this way, OGPO shifts VLA post-training from trajectory-level action imitation to key-state reachability learning, enabling policies to acquire a more robust ability to complete goal states from feasible off-demonstration states without requiring additional online interaction. Experiments on LIBERO and MetaWorld show that OGPO consistently improves VLA policy performance over standard supervised fine-tuning. Moreover, evaluations on LIBERO-Plus and our proposed LIBERO-ReAct, a mid-execution perturbation benchmark, further demonstrate that OGPO achieves stronger robustness and goal-directed recoverability under distribution shifts and recoverable off-demonstration states.

---


### 59. [Collaborative Learning and Reasoning over Model Slices](https://arxiv.org/abs/2610.12927)

**<font color=#1a73e8>作者：</font>** Yuheng Wang, Runde Yang, Zhuohan Bao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel across diverse tasks, benefiting from knowledge priors, in-context reasoning, and test-time computation. Despite these strengths, single-model reasoning remains vulnerable to error propagation, as later steps depend on the model's earlier outputs, leaving reasoning blind spots difficult to independently reassess. To address this limitation, we develop \textit{collaborative learning}, encompassing the construction of heterogeneous collaborators and the learning of effective cross-model collaboration. Specifically, \textit{model slicing} replaces a large model with smaller, heterogeneous models under a comparable parameter budget, enabling prior reasoning to be reassessed across distinct model parameterizations. \textit{Pyramid supervision} combines protocol distillation with step-level supervision to refine reasoning and interaction decisions throughout collaboration. We evaluate our approach across four task categories: multi-hop question answering, mathematical reasoning, code generation, and open-ended constrained generation. The trained heterogeneous models achieve comparable or better task performance than the original large model and established multi-agent baselines, including reinforcement-learning-based methods, while also achieving higher inference efficiency than the multi-agent baselines and exhibiting differentiated collaboration patterns across tasks. These findings show that learned collaboration turns model heterogeneity into complementary reasoning capabilities.

---


### 60. [Learning More by Training Less: Uncertainty-Guided Progressive Contraction for Efficient Reasoning Post-Training](https://arxiv.org/abs/2610.12933)

**<font color=#1a73e8>作者：</font>** Suorong Yang, Jiaxin Wang, Jiaming Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have achieved remarkable advances in complex reasoning. However, scaling reasoning post-training with ever-larger corpora can substantially increase training cost without proportional performance gains. In this study, we therefore ask: how far can reasoning supervision be compressed without sacrificing capability? To this end, we propose an uncertainty-guided progressive contraction framework that concentrates supervision and optimization on the reasoning trajectories most valuable for learning. Specifically, rather than treating a teacher-generated chain-of-thought (CoT) as a single realized path, we construct uncertainty-profiled reasoning supervision by building Monte Carlo reasoning trees around intermediate reasoning states to expose process-level uncertainty. This uncertainty first contracts the original corpus into a compact teacher-informed pool. A second, learner-aware contraction then performs online routing during SFT, concentrating optimization according to the student's evolving learning state. Together, the two stages progressively contract both supervision and optimization, substantially reducing the student training budget. Experiments across diverse reasoning benchmarks and LLM families show that our method uses as little as 0.22% of the optimization budget of full-data SFT, over 450x less training exposure, while maintaining or improving reasoning performance. Notably, our framework generalizes well across heterogeneous student families, black-box teachers, and weak-to-strong transfer. This indicates that it is not only a way to accelerate training but can also enhance reasoning capability.

---


### 61. [Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding](https://arxiv.org/abs/2610.12939)

**<font color=#1a73e8>作者：</font>** Raghavv Goel, Sudhanshu Agrawal, Mukul Gagrani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decoder hidden states from different layers of large language models (LLMs) often encode complementary information. However, existing speculative decoding methods typically rely on a small set of target-model layers chosen using fixed, position-based heuristics. Selecting an optimal subset of layers is inherently a combinatorial problem, making exhaustive evaluation infeasible even for moderately deep models. In this work, we present a principled framework for multi-layer hidden-state selection for speculative decoding based on two complementary criteria: informativeness, measured through matrix-entropy analysis, and diversity, quantified using centered kernel alignment (CKA). We investigate layer-wise Shannon entropy, aggregate entropy under hidden-state concatenation, and pairwise CKA dynamics across depth, revealing distinct geometric and informational compartments within decoder representations. Motivated by these findings, we propose entropy and CKA-based layer selection algorithms that favor hidden-state sets that are both highly informative and minimally redundant. As part of this framework, we introduce token-entropy filtering, which removes hidden states associated with low predictive-entropy tokens, thereby improving the quality of layer-selection statistics. In EAGLE3-style speculative decoding, our selected sets outperform fixed baseline choices, including the default $[2, N//2, N-3]$ rule, while providing a clearer explanation of why some defaults can remain competitive. Our results provide a practical recipe for multi-layer hidden-state selection for speculative decoding, insights into the geometry and information in LLM decoder states, and a foundation for extending similar analysis to related applications.

---


### 62. [In-Context Learning Can Help Vision-Language Models Overcome Training Priors](https://arxiv.org/abs/2610.12942)

**<font color=#1a73e8>作者：</font>** Kun Wang, Xindi Wu, Sanghyuk Chun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) learn strong statistical regularities during training, which can make them fail to properly respond to visual evidence when input images violate those regularities. It is challenging to disambiguate these prior-induced errors from errors caused by the model missing the underlying visual capabilities. In this work, we use controlled visual in-context learning to encourage the model to focus on the visual evidence, and demonstrate that this alone is frequently sufficient to correct the errors -- suggesting that the models in fact do possess the relevant visual capabilities. Specifically, we show that across five vision-centric tasks, demonstrations yield large gains on prior-conflicting counterfactual examples ($+27.2\%$ for Qwen3-VL 235B and $+15.1\%$ for Qwen3-VL 32B) while leaving accuracy on prior-aligned examples nearly unchanged. These findings generalize across five VLM families with gains from $+9.7\%$ to $+30.3\%$. We analyze visual representations and find that demonstrations indeed redirect attention toward grounding cues while reducing reliance on cues that support the learned prior. Finally, we find that in-context learning is limited when the underlying visual capability is weak or absent. Together, these results show that current VLMs possess visual grounding capabilities that standard evaluations may overlook, underscoring the need for controlled evaluation design in diagnosing and improving model capability.

---


### 63. [MathVis: Can AI Reason through Drawing? A Benchmark for Mathematical Figure Generation](https://arxiv.org/abs/2610.12954)

**<font color=#1a73e8>作者：</font>** Jingjing Wei, Hao Zhao, Xinke Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces MathVis, a benchmark designed to evaluate LLMs' ability to visualize frontier mathematical problems and perform diagram-assisted reasoning. The benchmark consists of 512 tasks, each comprising a mathematical statement, a reference diagram, executable TikZ or SVG code, a Gold Intermediate Representation (IR), atomic rubrics, and error codes. Through rigorous evaluation, GPT-6-Astra, Claude Fable 5, and Gemini 3.1 Pro Preview achieve pass@1 scores of 31.25%, 26.56%, and 22.85%, respectively. We found that although the tasks require visualization, LLMs produce outputs dominated by formal languages, symbols, and graphics programs, rather than explicit diagram-mediated reasoning. Furthermore, while the solutions generated by LLMs may contain all the necessary elements, they are often visually confusing to humans. Ultimately, this benchmark aims to visualize mathematical problems and promote research on enabling LLMs to simplify their reasoning via visual diagrams.

---


### 64. [Video Codec-Guided Training-Free Token Compression for Video Large Language Models](https://arxiv.org/abs/2610.12959)

**<font color=#1a73e8>作者：</font>** Xihua Sheng, Ruijie Liu, Chang Wen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video large language models (VLLMs) rely on long visual token sequences to understand complex temporal content, which makes visual token compression important for efficient inference. Existing training-free compression methods mainly reduce the number of tokens sent to the language model, but the compression process itself can still require many visual feature comparisons, especially for intra-frame token protection and inter-frame temporal token merging. This paper proposes a video codec-guided training-free token compression method for VLLMs that uses coding information already available in compressed video as a low-cost search prior. The method aligns reference-frame dependencies, motion vectors, and residuals with the visual token grid. Residual information forms compact candidate pools for token protection, while motion information is propagated along reference-frame chains to construct localized candidates for temporal token merging between sparsely sampled frames. Local visual feature similarity comparison is then used within these candidates to make the final compression decisions, without modifying the base VLLM. Experiments on three representative VLLMs and four video-understanding benchmarks show that the proposed method achieves performance comparable to the state-of-the-art training-free baseline FlashVID, and in some settings surpasses it, while substantially reducing the feature comparisons required by token protection and temporal matching. These results demonstrate that codec information can effectively improve the accuracy-complexity tradeoff of video token compression.

---


### 65. [MVGraph: Benchmarking LVLMs on Evidence Composition across Multi-View Visual Graph](https://arxiv.org/abs/2610.12961)

**<font color=#1a73e8>作者：</font>** Yingjie Zhu, Han Cheng, Xuefeng Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce MVGraph, a benchmark for evaluating large vision-language models (LVLMs) on multi-graph reasoning where the evidence required by a query is distributed across multiple interrelated visual graph views. Although such evidence commonly resides in source-specific graphs, temporal snapshots, or local observations, existing graph reasoning benchmarks remain confined to a single self-contained structure, assessing only graph perception and reasoning while leaving the alignment and composition of evidence across views underexplored. MVGraph comprises 8k instances spanning 8 \textit{graph-theoretic} tasks, abstracted from two multi-graph scenarios (partial and temporal graph views). Each problem is programmatically constructed and verified to be unsolvable from a single view. Beyond end-to-end evaluation, we decompose multi-graph reasoning into four complementary capabilities---Perception, Alignment, Composition, and Reasoning---and design 29 diagnostic tasks with 64k instances to probe each one, along with golden intermediate representations for evaluating the intermediate process. Across 15 LVLMs, we reveal the difficulty of multi-graph reasoning and identify cross-view edge alignment and relation-level composition as prominent bottlenecks through stage-oriented diagnostics. Meanwhile, temporal constraints and increasing view counts expose further capability boundaries. Code and data are available at this https URL.

---


### 66. [SmartSalesBench: A Resistance-Aware Multi-Turn Benchmark for Evaluating LLM Sales Agents](https://arxiv.org/abs/2610.12975)

**<font color=#1a73e8>作者：</font>** P N Bhargav Teja, Velpula Lokesh Reddy, Madhu Basumata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present SmartSalesBench, the first multi-turn conversational benchmark explicitly designed to evaluate large language model (LLM) sales agents against psychologically grounded, resistant buyer personas. Existing task-oriented dialogue benchmarks assume cooperative users and measure task completion; SmartSalesBench inverts this assumption, placing agents against personas programmed to resist and challenge across conversations of up to twenty turns. The benchmark includes five agent profiles, twelve buyer personas, fifteen smartphone products across six price tiers, and four controlled experiments with 3 iterations totaling 13,680 sessions. Both sales-agent and buyer persona generations are grounded through retrieval-augmented generation (RAG). We introduce nine evaluation metrics grouped into three tiers: primary outcome metrics (CR, BRS, RIR), secondary quality metrics (SMS, PFS, ETI), and exploratory metrics planned for future reporting (ITS, ARI, SPI). Our evaluation combines automated LLM-as-judge scoring with internal human assessment (n = 50, \k{appa} = 0.71, Pearson r = 0.81 with BRS).

---


### 67. [The Evidence Anchoring Boundary: Where Visual Interventions Matter and When They Help in Multimodal LLMs](https://arxiv.org/abs/2610.12981)

**<font color=#1a73e8>作者：</font>** Qiji Zhou, Junyi Hu, Peiyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual interventions provide a training-free way to reduce hallucinations in multimodal large language models. However, an intervention may have little leverage at some layers and may damage a correct answer even when it changes the output. We investigate where visual interventions retain leverage and when they improve predictions. First, we apply the same visual-residual edit at successive decoder layers, matching its RMS strength across depth. Across six checkpoints from three model families, we observe a persistent drop in intervention effect and define its operational onset for this edit as the \textbf{Evidence Anchoring Boundary (EAB)}. With boundaries fixed on calibration queries, held-out effects on disjoint evaluation queries before EAB are $13.78\times$--$26.10\times$ larger than those after it. Comparison with intermediate readouts shows that the edit can lose leverage before answer preferences stabilize. Second, we compare counterfactual subtraction across presence, attribute, and relation questions. Subtraction can correct a misleading preference, leave a decision unchanged, or remove a preference supporting the correct answer. Based on these observations, we develop calibrated selective routing, which preserves the original prediction unless calibration supports an intervention for the question type. It improves full-set attribute accuracy by $1.56$--$1.81$ percentage points across three checkpoints, while universal subtraction is neutral or harmful.

---


### 68. [Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction](https://arxiv.org/abs/2610.12984)

**<font color=#1a73e8>作者：</font>** Yuqi Huang, Hui Li, Yifei Cao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents can perform increasingly complex GUI tasks, yet unfamiliar software and workflows requiring human domain knowledge remain challenging. Human demonstrations convey procedural knowledge through the same GUI interaction space, but reuse requires interpreting actions in context and separating workflow rules from task-specific details. We thus introduce Work2Skill, a framework that captures human GUI experience for reusable agent skill induction. WorkRecorder provides the framework's infrastructure for collecting this experience, aligning screen recordings, mouse and keyboard events, and available accessibility-tree information. Using WorkRecorder, we construct WorkDemo-350, the first synchronized multimodal dataset of human desktop GUI demonstrations for reusable agent skill induction and downstream evaluation. Its 350 demonstrations are screened for completeness and task success. We then propose an agentic skill-induction method that inspects evidence on demand to produce reusable skills capturing workflow rules, step dependencies, and completion checks. When the same four execution models are equipped with skills induced by each method under shared execution settings, Work2Skill achieves the highest scores and success rates. Mean score improvements over the corresponding No Skill baseline are 4.67--10.54 points on MyPCBench Bounded Action and 3.11--7.50 points on a 286-task subset of OSWorld-Verified. Our code and data are available at this https URL.

---


### 69. [Forecasting Corpus-Sampling Disagreement in Masked Text Reconstruction](https://arxiv.org/abs/2610.12987)

**<font color=#1a73e8>作者：</font>** Hare Krishna  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> If a second text corpus were collected from the same population, how much would a predictor's outputs change? We study this question for masked-text reconstruction using a smoothed predictor built from nearby token-pair counts and evaluated over the full 50,257-token GPT-2 vocabulary. Treating each source document as one observation, we derive a first-order formula for the expected disagreement between predictors fitted to two independent corpora. The formula accounts for variable document length, random context counts, and correlations across token offsets, and it can be evaluated from a separate reference corpus without access to either target corpus. On TinyStories, WikiText-103, and CNN/DailyMail, growing each corpus from 512 to 2,048 chunks of 64 tokens lowers disagreement by only 5--40\%, far short of the 75\% implied by $1/n$ scaling. The forecast tracks this slow decline, which we trace to smoothing of rarely seen contexts. Forecast accuracy depends less on how these correlations are modeled than on the size of the reference corpus: small references systematically underpredict disagreement. A source-split jackknife that uses only reference data reduces this calibration error by 57--59\%. After this correction, a simpler smoothed-multinomial approximation is most accurate when the reference corpus is smaller than the target corpus, and a nonlinear source bootstrap is most accurate when it is larger. Finally, small masked diffusion language models trained on the same corpora show that the count-based forecasts partly identify which inputs are most sensitive to the corpus, but miss the neural models' much faster decline in disagreement.

---


### 70. [SwingGuard: Risk-Conditioned Multi-Agent Swing Trading with Dual-Timescale Governance](https://arxiv.org/abs/2610.12988)

**<font color=#1a73e8>作者：</font>** Junzhou Su, Yichen Luo, Yebo Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cryptocurrency swing trading spans mismatched timescales: positions remain active while market and event risk can change within minutes. However, many predictive and large language model (LLM)-based trading systems assess risk after strategy generation or run both functions at the same cadence, leaving proposals unconditioned by current risk and exposure weakly governed between revisions. We propose SwingGuard, a dual-timescale, long-only multi-agent framework for risk-conditioned strategy generation. At the strategy timescale, specialized analysts synthesize point-in-time technical, sentiment, on-chain, and macroeconomic evidence through bullish-bearish deliberation. The resulting evidence and current risk context are then combined by a Portfolio Architect to form a target position. At the governance timescale, a five-minute Risk Controller performs conditional diagnosis, maintains persistent risk states with staged recovery, audits the proposal, and constrains execution until the next strategy revision. This design allows risk to shape the feasible strategy before proposal finalization while continuing to govern the active position afterward. Evaluations on Bitcoin (BTC) and Ether (ETH) show that SwingGuard preserves positive returns after transaction costs while maintaining shallow drawdowns and strong risk-adjusted performance on both assets. The exposure-capped joint portfolio achieves a Sharpe ratio of 2.98, compared with 2.79 for an otherwise identical Post-hoc Risk variant. Structured traces further link risk evidence and state transitions to strategy constraints and executed position changes, providing an auditable framework for asynchronous cryptocurrency swing trading. Overall, the results indicate that conditioning strategy formation on current risk, together with persistent high-frequency governance, improves risk-adjusted performance without sacrificing auditability.

---


### 71. [Language Models Have Interpretable Narrative Mechanisms](https://arxiv.org/abs/2610.12989)

**<font color=#1a73e8>作者：</font>** David Yiyang Liu, Aditya Joshi, Paul Dawson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate whether language models contain internal components that contribute to representing narrativity, the degree to which a text exhibits narrative properties. Across GPT-2-Small, Gemma-2-2B, and Llama-3.1-8B, we identify attention heads, MLP neurons, and sparse autoencoder features whose activations correlate with narrativity. Ablating selected neuron and feature sets increases next-token prediction loss more for high-narrativity than for low-narrativity texts, and reduces the narrativity of open-ended generations. On downstream benchmarks, the largest effects occur in story completion and narrative question answering, although they vary across models and languages; results on confabulation and hallucination benchmarks are mixed. These findings provide causal evidence that selected sets of narrative-associated components contribute to model behaviour, while their internal organisation, relation to narrative theory, and broader functions remain open questions.

---


### 72. [What Should SFT Learn? Conditional Information Gain for Generalizable Post-Training](https://arxiv.org/abs/2610.12995)

**<font color=#1a73e8>作者：</font>** Yuxuan Gu, Kequan Niu, Xiaocheng Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) remains a widely used approach for post-training large language models, because fixed demonstrations can directly introduce desired reasoning strategies and behavioral patterns. Yet forcing a model to imitate externally provided trajectories may also interfere with behaviors already supported by pretraining, limiting generalization beyond the training distribution. Recent dynamic SFT methods mitigate this issue by reweighting token-level supervision according to model-side signals such as predictive probability, prior support, or distributional compatibility. However, model compatibility is not equivalent to learning value: a token that is weakly supported by the current model may either be an undesirable mismatch or precisely the task-specific decision that the demonstration is intended to teach. We propose CIG-SFT, an information-theoretic framework that estimates the task-conditioned information carried by each demonstrated token. Under teacher forcing, we compare the token likelihood from a frozen reference model with and without access to the task input while keeping the gold solution prefix fixed. The resulting conditional information gain quantifies how much the task itself reduces uncertainty about the demonstrated decision. We then convert this information into a KL-regularized projection of the current policy and derive an equivalent scalar-weighted SFT objective whose logit gradient exactly matches that of the projected target. Across mathematical reasoning and code-generation benchmarks, CIG-SFT consistently outperforms standard SFT and recent adaptive fine-tuning baselines, with particularly strong improvements in generalization to challenging evaluation distributions, while requiring neither additional training data nor online rollouts.

---


### 73. [Evaluating LLM Creativity through Long-Tail Performance](https://arxiv.org/abs/2610.12998)

**<font color=#1a73e8>作者：</font>** Yichen Wang, Tenghao Huang, Vishakh Padmakumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Creativity benchmarks for large language models (LLMs) vary widely in task and metric design. This raises the question of whether they capture a common notion of creativity. We propose that this shared target can be formalized as task-specific performance in the long tail of a reference input-output distribution, which describes how common input-output pairs are relative to a chosen source of text. We ground this proposition in the novelty-quality product formulation and evaluate it empirically across 15 benchmarks and 26 open-weight models, using n-gram absence from the pretraining data as a novelty proxy. Our results show that creativity benchmarks lie further in the tail regions than standard benchmarks. Moreover, on both creativity and standard benchmarks, model rankings from higher-tail subsets of each benchmark align more closely with human creativity judgments in LM-Arena. Building on these findings, we introduce q@Tail($\alpha$), a lower-cost creativity diagnostic that measures mean task quality on the tail fraction of an existing benchmark. Applying it to creativity-promoting methods reveals substantial room to improve LLM creativity through stronger tail performance.

---


### 74. [Hindsight Structured Advice Distillation: Steering Executor Agents with Advisors Trained on Their Failures and Task Characteristics](https://arxiv.org/abs/2610.13000)

**<font color=#1a73e8>作者：</font>** O. Ozan Koyluoglu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents are used for specialized work such as financial research, healthcare and law. Such agents are often capable enough for a task but still miss its details. In finance, for example, these details include which filing reports a figure or how a company discloses a metric. Retraining the agent to learn these details is expensive, and often impossible when the agent is a closed or shared system. Writing the missing know-how into the agent's prompt makes the prompt long and identical for every input, although different inputs need different guidance. We propose to learn to generate this guidance instead. A small advisor model reads each input and writes structured advice, which is appended to the prompt of a frozen executor. The advisor is trained with hindsight, following work on distillation with privileged information. On a training pool with graded answers, we analyse the executor's failures, run it under several strategies to see which one worked on each input, and let a teacher that sees the grades and the traces write the advice that would have helped. The advisor then learns, by supervised fine-tuning, to write that advice from the input alone. Because the student is a separate small model rather than the executor, it is cheap to train and adds little latency. We call this approach hindsight structured advice distillation (HSAD). On FrontierFinance, a public benchmark of expert-written financial research queries, an 8B advisor raises the qualification rate of Samaya's proprietary research agent, which already leads the benchmark's leaderboard, from 52.9% to 56.6%. This is above the agent's own high-effort configuration, at 37% lower cost per query. We study the generalization of the proposed approach, and in particular show that HSAD also improves results on WebShop, BIRD text-to-SQL and ExpertLongBench.

---


### 75. [Provenance-Aware Belief Updating in Human-AI Feedback Loops](https://arxiv.org/abs/2610.13008)

**<font color=#1a73e8>作者：</font>** Tianyi Huang, Eric Liu, Jay Chong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In repeated human-AI interaction, a single observation can be quoted, summarized, and returned to a model as multiple reports, making repetition look like independent corroboration. We study whether language models can use supplied report lineage to update according to evidence provenance rather than report count. We introduce Latent Quotient Evidence Training (LQET), a relational objective that combines sparse Bayesian supervision with constraints that encourage stable predictions when reports add no new evidence and consistent updates to the same new evidence across relay histories. On a controlled binary benchmark, LQET reduces new-evidence update RMSE by 41-44% and log-odds drift after eight relay steps by 89-91% relative to task-only training across Qwen3-4B and Phi-4-mini, with three paired training seeds per backbone. The gains extend to a closed-loop simulation in which model confidence controls how many relayed reports re-enter the model's context in later rounds. By grounding belief updates in supplied provenance, LQET offers a route toward dynamic human-AI systems in which influence follows new evidence, not the number of times the same evidence returns.

---


### 76. [Generalized Proximal Policy Optimization: Unifying LLM RL Algorithms from the Perspective of Divergence](https://arxiv.org/abs/2610.13015)

**<font color=#1a73e8>作者：</font>** Zhicheng Cai, Xinyuan Guo, Hanlin Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become the foundational paradigm for enhancing the reasoning capabilities of LLMs. Yet the dominant approach, Proximal Policy Optimization (PPO), relies on a geometrically degenerate clipping proxy that cannot adapt its resistance to policy shifts, leading to premature clipping and degraded exploration. Subsequent variants alleviate these issues through fragmented and heuristic modifications. We propose Generalized Proximal Policy Optimization (GPPO), a principled and unified framework for understanding and designing LLM RL algorithms through the lens of divergence. We establish a generalized $f$-divergence trust-region theory with a monotonic performance improvement guarantee, and show that different $f$-divergences induce distinct geometries and policy update dynamics. We further introduce novel estimator topologies that provide more faithful divergence estimates than the conventional single-sample Monte Carlo estimation. Under this framework, PPO and recent variants such as DAPO, DPPO, and RIPO emerge as special cases, establishing a principled two-dimensional design space of {Divergence $\times$ Estimator}. Extensive experiments on eight competition-level math and coding benchmarks show that both dimensions are critical. The best-performing GPPO instantiation surpasses standard GRPO by up to 50% and 14% on math and coding, delivering SOTA performance.

---


### 77. [Trajectory-Aware Policy Optimization: Closing the State Distribution Gap in Long-Horizon LLM RL](https://arxiv.org/abs/2610.13020)

**<font color=#1a73e8>作者：</font>** Zhicheng Cai, Weinan Dai, Yuyan Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a dominant paradigm for enhancing LLMs' reasoning capabilities. Yet long-horizon autoregressive rollouts introduce a fundamental limitation: local policy mismatch can compound into severe state distribution shift over trajectories. Existing LLM RL methods, such as GRPO and GSPO, control policy mismatch at the token or sequence level, but overlook this trajectory-induced shift, causing training instability and eventual collapse as the horizon grows. To close the state distribution gap, we propose Trajectory-Aware Policy Optimization (TAPO), a principled framework that theoretically derives the state-distribution correction from the off-policy policy gradient and incorporates it into the RL objective. TAPO further employs a geometric-mean estimator for variance reduction, together with a length-aware dynamic clipping that prevents overly deviated updates across the trajectory. Extensive experiments demonstrate that TAPO significantly surpasses existing LLM RL algorithms across eight competition-level benchmarks, achieving up to 48% and 12% improvement over GRPO on mathematical reasoning and algorithmic coding, with substantially enhanced training stability.

---


### 78. [EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents](https://arxiv.org/abs/2610.13021)

**<font color=#1a73e8>作者：</font>** Jie Huang, Yanan Chen, Ruixun Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual learning requires models to accumulate past experience and transfer it to new tasks. Despite substantial research on continual learning, existing work remains largely confined to non-embodied settings, without extending to embodied environments. To address this gap, we introduce EmbodiedCLBench, the first benchmark in embodied simulation for evaluating the continual learning capability of self-evolving agents. With compositional generalization as the core evaluation principle, our benchmark evaluates whether agents can first learn from basic tasks and then recombine the acquired skills to solve complex, unseen advanced tasks. Based on EmbodiedCLBench, we conduct extensive experiments across multiple agent harnesses and learning methods, revealing consistent limitations and distinctive behaviors. Our results show that while advanced tasks can be hardly solved under zero-shot setting, the experience from basic tasks enables consistent improvement. Such benefit from the experience remains stable even if the task complexity increases. However, this improvement does not scale accordingly with the number of learning samples, and current agents cannot extract meaningful information from additional experience. Collectively, our findings highlight continual learning as a fundamental yet underexplored capability, and our benchmark offers valuable resources for designing effective self-evolving agents in embodied environments. Our code and dataset are available at this https URL.

---


### 79. [Evo$^2$: Evolving the Evolver through Weight-Harness Co-Evolution](https://arxiv.org/abs/2610.13025)

**<font color=#1a73e8>作者：</font>** Chejian Xu, Shujian Zhang, Wenxuan Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents are increasingly used to improve language model systems without human intervention through either weight updates or harness improvements. Existing approaches typically pursue these directions separately: some methods update model weights using self-generated experience, while others rewrite the harness that defines how an agent uses prompts, tools, context, and execution feedback. However, these approaches overlook the relationship between model weights and the agent harness. To connect these processes and ensure effective and smooth agent self-evolving, we propose Evo$^2$, a framework for weight-harness co-evolution. For harness updates, we design a unified dual-role pipeline that a single policy serves as both a Proposer, which writes harness edits, and a Reflector, which diagnoses their effects and guides revision. For weight updates, harness modifications and their execution outcomes guide the training of both the Proposer and the Reflector. We further develop EvoTIDE, a training pipeline that recovers usable trajectories through edit extraction and prefix continuation, then combines SFT with interleaved GRPO across the two roles. Extensive experiments across three coding benchmarks demonstrate that Evo$^2$ significantly outperforms existing self-evolution methods. It achieves 82.1% on Polyglot and 48.3% on SWE-bench Verified, compared with 62.6% and 41.0% for the strongest baseline, respectively. We also show that the evolved harnesses transfer to different tasks without further evolution and rank first in cross-benchmark evaluations. Our dual-role harness improvement framework is also able to extend to self-evolution with proprietary models, improving a GPT-5-mini agent's performance from 24.4% to 48.3%. These results demonstrate the applicability of the framework Evo$^2$ across domains and its broad transferability across models and tasks.

---


### 80. [GeoGR: Spatial-Semantic Token Compression and Group Routing for Efficient 3D VLMs](https://arxiv.org/abs/2610.13035)

**<font color=#1a73e8>作者：</font>** Yongxin Zheng, Hao Wu, Fang Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view representations enable pretrained image and video vision-language models to understand 3D scenes, but their long visual token sequences make inference costly. Redundancy arises both from repeated observations of the same scene regions across views and from processing all visual tokens at every LLM layer, regardless of their relevance to the current computation. We propose GeoGR, a two-stage framework that jointly compresses scene representations and visual computation. At the projector level, GeoSemZip consolidates cross-view observations into 3D voxel tokens and combines semantic saliency with spatial coverage to construct a compact scene representation. Unselected voxel features are aggregated into contextual anchors to retain scene information that would otherwise be discarded. At the LLM level, we identify an effective visual computation window and observe that query-conditioned token relevance remains locally stable but changes over longer layer intervals. Guided by these findings, GroupRoute combines late entry and early exit with recoverable group-wise skipping. Low-relevance tokens bypass complete LLM layers while retaining their hidden states and can rejoin the active group at subsequent anchor layers selected under a computation budget. For compression-aware post-training, we construct a compact dataset of 67K samples by retaining 30% of the original training pool. With this protocol, GeoGR retains 95.2% and 96.8% of the dense post-trained models' performance on LLaVA-OneVision-7B and Video-3D LLM-7B, respectively, while accelerating LLM prefill by $6.8\times$ and $6.1\times$. These results demonstrate the consistent effectiveness of GeoGR across 3D VLMs with and without explicit 3D spatial encoding, highlighting a favorable performance-efficiency trade-off. The code is available at this https URL.

---


### 81. [RAMP: Recurrent Adaptive Mixed Precision for Efficient Prefill in Recurrent-Depth Language Models](https://arxiv.org/abs/2610.13041)

**<font color=#1a73e8>作者：</font>** Ke Wan, Chen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recurrent-depth language models improve inference-time reasoning by repeatedly applying a shared network to refine internal representations, but the additional recurrent computation also increases inference cost. This overhead is particularly pronounced during long-context prefill, where the full input sequence is repeatedly processed across recurrent depth. Weight-and-activation quantization offers a natural way to accelerate this computation through lower-precision arithmetic, yet repeatedly applying quantized computation introduces numerical perturbations that accumulate along the recurrent trajectory. We systematically analyze how such errors propagate across recurrent depth and show that quantization errors introduced earlier are attenuated by more subsequent recurrent steps and therefore have a smaller effect on the final representation. Matched-budget experiments strongly support this prediction, showing that placing quantized computation earlier in recurrent depth consistently yields the best fidelity. Based on this insight, we introduce RAMP (Recurrent Adaptive Mixed Precision), which performs early recurrent refinement using low-precision weight-and-activation computation and restores high precision for terminal refinement. Across context lengths up to 4K, RAMP preserves near-full-precision prefill quality while achieving up to 1.16x end-to-end first-prefill speedup on an NVIDIA H100, corresponding to a 13.9% latency reduction.

---


### 82. [Redirecting Teacher Supervision: Temporal-Response-Guided Latent Distillation for Video-Language Models](https://arxiv.org/abs/2610.13045)

**<font color=#1a73e8>作者：</font>** Xinkai Lu, Junli Zha, Haolan Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) transfers capabilities through teacher predictions on student-generated sequences, as studied by GKD and MiniLLM for language models and Video-OPD for video tasks. We ask how internal supervision can further support temporal learning. Direct hidden-state alignment does not explicitly use the student's temporal responses to choose a supervision direction. We propose Temporal-Response Guidance (TRG), which measures representation responses to local temporal perturbations, adds the teacher correction's projection onto their span back to the original correction, and restores its original norm. The projection is not normalized separately, and correction components outside the response space are retained. With an orthogonal tangent projector and a detached target, TRG changes the supervision direction while preserving the cosine-loss value and aligned-representation gradient norm at target construction. On TempCompass, Video-MME, MVBench, and Video-MMMU, TRG improves the 4B student's macro accuracy by 2.86 percentage points over the reported output-only OPD baseline.

---


### 83. [Travel Back To Move Forward: Retrospective Exploration and Evolving for Long Horizon Agents](https://arxiv.org/abs/2610.13058)

**<font color=#1a73e8>作者：</font>** Ziang Ye, Wentao Shi, Lei Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly operate in long-horizon environments where early mistakes can trigger cascading failures and trap agents in dead-end trajectories. Agents must therefore be able to proactively recover from such states and turn their exploratory experience into guidance for subsequent decisions. We introduce ReTRAIL, a framework that enables agents to rewind the environment to earlier states while preserving valid progress and carrying forward knowledge learned from abandoned exploration. The environment state moves backward while the agent's knowledge continues to move forward. ReTRAIL trains a shared policy with two complementary signals: State-Anchored GRPO compares alternative continuations from revisited states to improve execution, while a branch-advancement reward guides reflection through the progress of subsequent exploration. Experiments across four interactive benchmark MineSweeper, Sokoban, ALFWorld and ScienceWorld show that simply adding a rewind primitive provides limited benefit and can even degrade performance. In contrast, ReTRAIL enables agents to rewind from unproductive states and use insights from abandoned branches to guide subsequent exploration. These results demonstrate the value of coupling environment rewinding with experience reuse within an ongoing task for long-horizon task solving. The code is available at this https URL.

---


### 84. [CliQ-RRG: Clinical-Knowledge Guided Disease-aware Visual-Textual Alignment for QA-Style Radiology Report Generation](https://arxiv.org/abs/2610.13059)

**<font color=#1a73e8>作者：</font>** Chandravardhan Singh Raghaw, Shahid Shafi Dar, Arnav Nishith Sharma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Radiology reports are essential for diagnostic reasoning and patient care, yet their manual preparation is time-consuming and cognitively demanding. Automatic radiology report generation (RRG) offers a scalable alternative, but existing models often produce lengthy, unstructured narratives that overlook diagnostic cues and multi-view information. We present Clinical-Knowledge Guided Disease-aware Visual-Textual Alignment for QA-Style Radiology Report Generation (CliQ-RRG), a unified two-stage framework for interpretable and clinically grounded reporting. In Stage 1, CliQ-RRG employs a Disease-aware Visual-Textual Alignment module that aligns image and text representations using predicted disease embeddings, reinforced by a Prior-Guided Attention Module (PrAM) to capture multi-view dependencies across current and prior scans. In Stage 2, GraphRAG-guided retrieval augments intermediate textual representations with graph-grounded clinical evidence, and a large language model restructures them into concise, interpretable question-answer (QA) pairs with diagnostic summaries. Experiments on two public chest X-ray benchmarks demonstrate that CliQ-RRG consistently outperforms prior methods across both lexical and clinical metrics, generating accurate and clinically coherent QA-style radiology reports. Code is available at: this https URL.

---


### 85. [KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse](https://arxiv.org/abs/2610.13060)

**<font color=#1a73e8>作者：</font>** Taiga Ikeda, Daisuke Miyashita, Jun Deguchi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> KV-cache reuse in large language model serving is commonly limited to exact prompt prefixes, preventing reuse when the same retrieved document appears after different system prompts, conversation histories, or dynamic metadata. We present KV-Repurpose, an open-source, vLLM-based system for developing and evaluating segment-wise KV-cache reuse beyond exact prefixes. The system combines cache-aware segment scheduling, prompt construction, capacity management, workload generation, and runtime monitoring. Experiments on long-context benchmarks show that naive segment reuse largely preserves output quality for single-document question answering and summarization, while exposing clear limitations in cross-document reasoning. Under a Zipfian RAG-style workload in which 20% of requests share a fixed prefix, KV-Repurpose achieves a substantially higher token-level cache hit rate than prefix caching at the same 30 GB cache capacity, 63.9% versus 3.3%, resulting in lower TTFT. Even with 1 TB of cache capacity, prefix caching reaches only a 17.9% hit rate in this workload. Source code is available under the Apache-2.0 license at this https URL.

---


### 86. [CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits](https://arxiv.org/abs/2610.13064)

**<font color=#1a73e8>作者：</font>** Jiahang Sun, Zhiwei Shang, Zhipiao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have demonstrated remarkable capabilities in tackling complex tasks through agentic workflows. However, manually designing these workflows is labor-intensive and lacks flexibility to adapt to diverse queries. While automated workflow optimization is a promising direction, existing methods often incur expensive API costs during training-phase feedback collection. Furthermore, they fail to adaptively reuse high-quality workflows, which creates a bottleneck for both performance and cost-effectiveness. To address these limitations, we propose CB-Orchestrator, an adaptive framework that decouples workflow generation from selection. In the first stage, we construct a diverse pool of candidate workflows via evolutionary search. In the second stage, we formulate workflow selection as a Contextual Bandit problem, which enables sample-efficient learning by balancing exploration and exploitation, thereby significantly reducing the feedback required for training. During inference, the model adaptively selects the optimal workflow tailored to each query. Evaluations across five diverse benchmarks demonstrate that CB-Orchestrator consistently outperforms all baselines. Notably, on the MATH dataset, CB-Orchestrator achieves better performance than strong recent baselines while reducing training-phase API token overhead by no less than 40.55% and total end-to-end training (including workflow pool generation) token overhead by no less than 29.73%.

---


### 87. [LongHarness: Advancing Agentic Reasoning over 100M-Token Corpora via Stateful Evidence Management](https://arxiv.org/abs/2610.13075)

**<font color=#1a73e8>作者：</font>** Songtao Huang, Zhijie Zhong, Xiaohan He 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Corpus-level long-context reasoning requires agents to acquire and integrate evidence across document collections that exceed their context windows. Existing agent harnesses enable incremental access to these corpora, but acquired evidence and evolving conclusions often remain entangled in a growing interaction history. This implicit state management can lead to two coupled failure modes: unbounded exploration, where retrieval expands the interaction history without resolving decision-relevant information gaps, and evidence-state drift, where previously acquired evidence or subsequent corrections fail to inform the current conclusion. We present LongHarness, a model-agnostic harness that makes the interaction between acquired evidence and evolving conclusions explicit. Its core mechanism, Evidence-Conclusion Coevolution, uses unresolved conclusions to guide exploration toward missing information, while newly acquired evidence strengthens or revises the conclusions that directed the search. LongHarness couples this process with Evidence Lifecycle Management, which keeps accumulated evidence current and traceable throughout the interaction. Together, these mechanisms focus retrieval on remaining information needs and keep conclusions aligned with current evidence. We evaluate LongHarness on OfficeQA Pro V1 and V2, AA-LCR, and LongBench v2 using GLM-5.3-Flash and Qwen3.8-Flash. Compared with direct reasoning using the same backbone, LongHarness improves GLM-5.3-Flash exact match on OfficeQA Pro from 15.8% to 60.2% on V1 and from 4.4% to 61.1% on V2. Against state-of-the-art agent harnesses, it surpasses Claude Code by 12.0 percentage points on V1 and Codex by 18.9 points on V2. With Qwen3.8-Flash, LongHarness reaches 61.7% on V1, outperforming Claude Code by 8.3 points and Codex by 12.0 points.

---


### 88. [Attention Sees, MLP Refuses: Tracing the Attention-to-MLP Safety Pathway in LLMs](https://arxiv.org/abs/2610.13078)

**<font color=#1a73e8>作者：</font>** Zixuan Weng, Haoqi He, Weifei Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-aligned large language models (LLMs) remain vulnerable to jailbreaks and can over-refuse benign requests. Understanding these failures requires distinguishing harmfulness recognition from the computation that writes refusal. We reframe this as a pathway question and make it measurable on residual-stream updates in decoder-only Transformers, separating the harmfulness information a module update exposes from the change it produces in readable refusal evidence. Across 18 Base-Instruct pairs spanning Qwen, Llama, and Gemma, harmfulness is decoded more readily from attention updates, particularly in early layers, whereas MLP updates contribute more strongly to harm-selective refusal writing in aligned models. Post-training strengthens MLP refusal writing in all 18 pairs without systematically improving harmfulness decodability, while positive MLP writing becomes more concentrated in deeper layers after post-training. Across six reasoning-enabled models, harmfulness remains decodable during reasoning while strong refusal writing concentrates at answer onset, a pattern that persists with reasoning disabled. Causal interventions further support this pathway: resetting downstream MLP updates to their clean values substantially reduces the refusal shift caused by upstream attention interventions. Building on these findings, we introduce Sentinel, which combines an attention-derived perception score P with an MLP-derived decision score D. Their joint profiles characterize jailbreaks and over-refusals, and conditional routing with both signals achieves a lower aggregate error rate than single-signal routing and evaluated fixed reminders across eight models.

---


### 89. [SWEAR: Section-Wise Efficient Audio Reasoning via Self-Rated Difficulty](https://arxiv.org/abs/2610.13081)

**<font color=#1a73e8>作者：</font>** Yixuan Li, Minghao Lv, Xuenan Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work on large audio-language models (LALMs) explores adaptive reasoning to balance accuracy and efficiency. However, existing approaches often rely on coarse-grained difficulty estimation, overlooking the diverse factors that determine reasoning effort. We address this limitation by deriving five-dimensional difficulty scores and compressed reasoning traces from complementary offline assessments. Based on this characterization, we propose SWEAR, a difficulty-aware reasoning framework that learns difficulty signals during supervised fine-tuning and uses reinforcement learning to adapt reasoning allocation across reasoning stages. Experiments on MMAU-test-mini and MMAR show that SWEAR improves accuracy while substantially reducing generated tokens, shortening reasoning for easy instances without sacrificing performance on difficult ones.

---


### 90. [Human and LLM Facilitation in Collaborative Design Meetings: A Computational Behavioral Comparison](https://arxiv.org/abs/2610.13082)

**<font color=#1a73e8>作者：</font>** Mohammed Azeez Khan, Aaron Dsouza, Ashutosh Mishra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly being explored as facilitators of group discussion and collaborative work, but the behavioral differences between LLM-generated and human facilitation remain insufficiently characterized. We compare human Project Manager facilitation turns from scenario-based collaborative design meetings with Llama 3.1 8B Instruct responses across 199 paired contexts from the AMI Meeting Corpus. The analysis covers five confirmatory dimensions: contextual semantic distance, a lexical elaboration proxy, empathyand-hedge lexical density, topic divergence, and phase-vocabulary alignment. An exploratory directiveness measure failed domain validation and is not interpreted. The sampled human Project Manager turns were higher on contextual semantic distance (r = 0.644) and on empathyand-hedge lexical density (r = 0.203). The second contrast is carried mainly by hedge terms, so we read it as lexical hedging rather than psychological empathy. Llama-generated facilitation was higher on topic divergence (r = 0.703), the lexical elaboration proxy (r = 0.288; lengthconfounded), and instruction-conditioned phase-vocabulary alignment (r = 0.382). A secondary no-phase check left the Llama-higher phase contrast in place. The system prompt still requested a facilitation move, so that check is not evidence of spontaneous phase awareness. These differences should not be interpreted as a ranking of facilitation quality. The resulting behavioral profile provides a reference point for later comparisons of LLM facilitators, human facilitators, prompts, models, and collaborative settings.

---


### 91. [When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows](https://arxiv.org/abs/2610.13092)

**<font color=#1a73e8>作者：</font>** Yuchen Ling, Shengcheng Yu, Zhenyu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents depend on repeated decisions to accomplish tasks, with large language models (LLMs) commonly serving as their core decision makers. The recent emergence of Jev offers an opportunity to make these decisions faster and at lower cost. However, it remains unclear whether such local savings can be translated into efficient and reliable task completion. In this paper, we investigate this efficiency transfer across five agents in two representative application settings, embodied tasks in ALFWorld and mobile app use in AndroidWorld. Across 4,500 task executions, we jointly evaluate task effectiveness, decision-level and task-level resource use, and execution behavior. Experimental results show that Jev integration substantially reduces decision cost and latency across all five agents, with task-level gains varying by workflow. Task success remains close to baseline levels on ALFWorld and declines more substantially in two mobile agents. Auxiliary reasoning and additional interactions absorb decision savings, while failed recovery and premature completion limit successful delivery. Mean cost per successful outcome increases in one agent even as spending per attempt falls. These findings highlight the importance of preserving progress, supporting recovery, and verifying completion when integrating efficient decision models into agent workflows. Their practical value should be assessed through successful task delivery, recovery behavior, and resources per delivered outcome.

---


### 92. [VETR: Execution-Grounded Self-Improving Agent for Symbolic Graphics Reasoning](https://arxiv.org/abs/2610.13098)

**<font color=#1a73e8>作者：</font>** Yingbo Ma, Kuangshi Ai, Gordon Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual agents for symbolic graphics reasoning depend on executable world representations, yet continued improvement remains bottlenecked by ambiguous supervision from final renders. Recent agentic systems refine scenes through repeated interaction, but they lack mechanisms to recursively extract actionable evidence from execution traces, overlooking which proposed symbolic edits survived, disappeared, or interfered during program execution. To address this, we propose VETR (Verified Execution Trajectories for Refinement), a framework that enables agentic recursive self-improvement over executable world representations for symbolic graphics reasoning. Within each task, VETR retains aligned program/render records with bounded runtime observations and introduces an execution refiner that compiles observed writes and state changes into constrained alternative programs. The refiner validates their endpoints and preservation conditions against captured runtime state; the ordinary visual verifier then assesses goal relevance. Repair construction makes no additional language-model calls, but can require additional executions. Evaluations on BlenderGym (280 tasks) and BlenderBench (27 released tasks) with GPT-5.6-luna and Qwen3.8-27B show that VETR consistently outperforms existing refinement strategies, including BlenderAlchemy and VIGA. Controlled ablations evaluate the contributions of execution refinement and role-asymmetric evidence organization under fixed generator-interaction caps.

---


### 93. [Robust Vision-Language Navigation with Awareness of Instruction-Execution Progress](https://arxiv.org/abs/2610.13104)

**<font color=#1a73e8>作者：</font>** Jiagan Huang, Zikun Zhou, Hongpeng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In Vision-Language Navigation (VLN) tasks involving multi-step instructions as guidance, an agent must associate its observations with the relevant instruction content at each decision point. Most graph-based methods commonly match candidate trajectories with the entire instruction, allowing already executed content to interfere with subsequent decisions. Although instruction-execution progress provides a direct cue for separating executed and pending content, existing progress estimation approaches often rely on explicit progress supervision, sophisticated progress-learning stages, or costly online reasoning with LLMs. In this paper, we propose a robust VLN framework with Awareness of Instruction-Execution Progress (VLN-AIEP), which couples progress estimation with navigation decision-making. VLN-AIEP associates the visited trajectory with the instruction to suppress embeddings corresponding to executed content, and then matches candidate locations with the pending content. This coupling makes correct navigation decisions depend on accurate progress estimation, allowing the progress estimator to learn directly from navigation decision labels without explicit progress annotations. To support progress estimation, we construct a landmark-anchored trajectory representation that encodes the semantic labels and viewpoint-relative geometry of instruction-referred landmarks. These landmarks serve as spatial references for associating the visited trajectory with executed instruction content. Extensive experiments on R2R, RxR, CVDN, and R2R-CE demonstrate that the proposed method achieves favorable performance across multiple metrics.

---


### 94. [Can Failed Trajectories Reveal Where Agents Go Wrong? Agentic Failure Attribution Without Step-Level Labels](https://arxiv.org/abs/2610.13105)

**<font color=#1a73e8>作者：</font>** Do Nguyen-Thanh, Junlin Fang, Bing Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Failure attribution for LLM agents aims to identify decisive steps responsible for task failure, which is critical for debugging and improving agentic systems. Existing methods rely on costly LLM prompting, step-level error annotations, or verified successful trajectories that lack failure signals for assistance. In this paper, we study failure attribution from step-unlabeled failure trajectories, where each trajectory is known to have failed but its decisive step is unknown. We propose SOAP (Spectral scOring with Attention-guided Propagation), an effective framework requiring neither step-level training labels nor a separate success-only reference set. SOAP first constructs a spectral reference space from LLM representations and assigns each step a base error score according to its projection behavior. Importantly, later steps may exhibit stronger failure signals because they inherit an earlier mistake, causing independent scorers to favor downstream consequences over the decisive error. To address this downstream contamination, SOAP derives soft step dependencies from attention patterns and propagates downstream error evidence toward its likely upstream sources. Extensive experiments show that SOAP consistently improves attribution performance over competitive baselines.

---


### 95. [What Do Visual-Head Discovery Scores Actually Find? Attention Source, Necessity, and Random-Control Pitfalls in Vision-Language Models](https://arxiv.org/abs/2610.13111)

**<font color=#1a73e8>作者：</font>** Md Abdul Kadir, Daniel Sonntag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attention heads that attend to image regions relevant to a question are increasingly used to steer, ground and interpret vision-language models (VLMs) and to reduce their hallucinations. They are mostly found by ranking heads with an attention- pattern score and validated by steering or masking them. We ask how the choices inside such a discovery score shape the heads it returns, and which of the two validations identifies them. On Qwen3-VL-8B-Instruct we vary the query type, the discovery corpus and the token positions whose attention is read (the attention source) in a full 2 x 3 x 2 design, and test all 12 head-sets for steerability (CERS: Contrastive Evidence-Region Steering score) and necessity (NCS: Necessity Con- trast Score) against layer-matched random head-sets. (1) The attention source and the query type reshape the selected heads far more than the corpus: changing the source keeps a median of 49 of the top-100 heads, the query 55 and the cor- pus 84, while two halves of the same data share 96-99. (2) Necessity follows the attention source: head-sets discovered from query-span attention are more nec- essary than last-token ones (difference 0.083, p=6 x 10^-10), and the two re- ferring + query-span sets lie 17-19 standard deviations above 250 layer-matched random sets (Holm-adjusted p=0.048). The referring + query-span effect re- plicates on several recent VLMs. (3) Steerability is not specific to the discovered heads: no discovered head-set steers better than its layer-matched random sets (rank p >= 0.14), and random sets drawn from the same or from any layer span the discovered sets' scores. Necessity therefore separates the discovery settings, while steering at this strength does not. We turn these findings into a protocol for reporting visual-head discoveries.

---


### 96. [Does Location Matter? A Black-Box Causal Audit Reveals Model-Dependent Audio Grounding in LALM Hallucination](https://arxiv.org/abs/2610.13112)

**<font color=#1a73e8>作者：</font>** Mohammad Khalooei, Mohammad Sabokrou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large audio-language models (LALMs) frequently exhibit object hallucination, affirming absent sounds. The dominant mitigation, Audio-Aware Decoding (AAD), contrasts logits under real audio against an all-zero "blank" waveform, flagged by prior review as out-of-distribution. We introduce a black-box causal test that isolates the claimed evidence itself: localize a claim's evidence region via CLAP similarity, remove it by spectral gating, and compare against a random-window control across a 2x2x2 grid on three LALMs. On Qwen2-Audio-7B, localized ablation's raw AUROC trails blank's (0.613 vs. 0.721); this is a duration confound, not a localization failure, since blank removes the entire clip versus the grid's 2-4 s. Holding duration fixed, localization beats random removal at every cell on both models. Raw detection value remains model-dependent, especially on Audio Flamingo 3. The same evidence corrects decoding: contrastive decoding combining blank and language-prior contrasts, gated and ensembled, raises Qwen2-Audio accuracy from 57.1% to 71.9%, beating AAD alone. A unified causal-grounding profile does not transfer between models, indicating different grounding regimes. The source code and a detailed report of our findings, including identified limitations, are available at this https URL.

---


### 97. [DRYLAB-Bench: Benchmarking the Biosecurity Risk of Agentic LLM Mutation Design](https://arxiv.org/abs/2610.13116)

**<font color=#1a73e8>作者：</font>** Yuzhen Wang, Chunxiao Li, Baichen Le 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) acquire advanced biological design capabilities, they offer substantial research benefits but simultaneously introduce severe dual-use risks, such as engineering enhanced pathogens or drug-resistant bacteria. While biosecurity frameworks recognize these threats, the actual risk of LLMs executing dangerous biological modifications remains unquantified, particularly when augmented with specialized biological design tools (BDTs). Existing evaluations primarily assess hazardous knowledge possession rather than practical application, overlook risk amplification from BDTs, and rely on unreliable, expensive, or hazardous validation methods. To address these gaps, we introduce DRYLAB-Bench (Design Risk Yielded by LLM Agent in Biodesign), the first comprehensive benchmark evaluating the high-risk biological mutation design capabilities of LLM agents. Moving beyond basic question-answering, DRYLAB-Bench tasks agents with 30 genuinely hazardous mutation-design scenarios distilled from biosecurity guidelines. It evaluates models in a multi-round, tool-augmented environment where LLMs orchestrate BDTs to iteratively refine candidates. Crucially, it scores designs directly against 187,695 empirical wet-lab measurements from ProteinGym and ViroGym using our proposed Biosecurity Risk Score (BRS), quantifying risk-associated effects while enabling scalable and safe ground-truth verification. Evaluations of 15 frontier models reveal substantial baseline threats: without tools, 67.6% of one-shot designs exceed the average measured variant, and 21.4% reach the highest-risk decile. Equipping models with BDTs significantly amplifies this risk, raising the pooled risk by \(\Delta BRS=+0.116\) and the top-decile share to 23.5%. Code: this https URL

---


### 98. [Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index for Open-Domain Multimodal Document QA](https://arxiv.org/abs/2610.13128)

**<font color=#1a73e8>作者：</font>** Wenlin Lin, Fanzhe Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Question answering over large heterogeneous document collections requires first finding the right passages and then reading them, yet current retrieval-augmented agents give one model both kinds of tools and let it schedule itself. We present KnowForge, a pipeline separated by job: a hybrid-retrieval knowledge-point index; a Locator agent that can only search; a code-scheduled bridge judge that forces the missing second hop; a typed, size-bounded evidence pool that merges every search's ranking; a Deep Reader agent that can only read text, images and tables; and a synthesizer with a format checker. With a self-hosted Qwen3.6-35B-A3B (3B active), KnowForge reaches F1 47.5 on the full open-domain M3DocVQA (2,441 questions, 3,368 PDFs), +11.0 over the published M3DocRAG system and +7.1 over one-shot retrieve-and-answer on the same index and model, and 53.5 with DeepSeek-V4-Flash. On MultiHop-RAG it reaches 73.5 accuracy, above the strongest published RAG and GraphRAG results (71.2); on the single-document MMLongBench-Doc it lifts the same model from 34.8 to 47.0, level with GPT-4o reading page images (46.3). Per-job ablations on the full benchmarks attribute the gain: the Deep Reader is worth 3.8, 9.8 and 0 points on the three corpora, tracking how visual each is; merging both agents into one with all tools and twice the rounds loses 1.9 F1 because it keeps searching instead of reading; a round-budget sweep shows a step at four Locator rounds and a plateau beyond; query latency scales with model calls rather than corpus size. We serve the three indexed benchmarks as read-only knowledge bases (free registration) and release all prompts and the runner code: this https URL

---


### 99. [DP-MIND: Differentially private memory-guided Long context Inference](https://arxiv.org/abs/2610.13132)

**<font color=#1a73e8>作者：</font>** Zhihao Liu, Yitian Cheng, Shuang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Service has become a dominant paradigm for accessing large language models without requiring local deployment. However, the process raises severe privacy concerns when user queries may include sensitive or confidential contexts. Differential privacy (DP) provides a principled approach to protecting such inputs, but existing DP inference methods are primarily designed for short- or moderate-context settings and struggle with million-token-scale inputs due to limited context capacity and severe utility degradation under DP perturbation.
In this paper, we propose DP-MIND, a memory-guided framework that scales differentially private inference to million-token contexts. DP-MIND enables private long-context inference by locally perturbing the input and processing it chunk by chunk with a compact memory that preserves task-relevant information across the sequence. To make this memory robust to DP noise, we optimize the memory construction policy directly on perturbed inputs using reinforcement learning, guided by both final answer correctness and memory consistency. We further recover perturbation-corrupted answer spans through a local denoising module without exposing the original context to the external model. We provide theoretical privacy analysis of DP-MIND and further conduct extensive empirical analysis across multiple long-context benchmarks with context lengths up to the million-token scale, demonstrating that DP-MIND consistently outperforms existing DP and long-context inference baselines in both scalability and utility.

---


### 100. [Neurograf v1: An End-to-End Romanian-First Language Model Family](https://arxiv.org/abs/2610.13134)

**<font color=#1a73e8>作者：</font>** Ionut Adrian Rotaru  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Neurograf v1, an experimental end-to-end Romanian-first language-model pipeline developed to investigate the feasibility of training language models from scratch for a lower-resource European language. The pipeline comprises RoSfera, a 635 GB Romanian corpus containing 175.7 million documents; an 80k byte-level BPE tokenizer; five decoder-only models ranging from 160M to 6B parameters, trained on 131 billion tokens; three instruction-tuned assistants; and two contrastively trained embedding models. Training and evaluation were conducted using computing infrastructure at ELI-NP/IFIN-HH.
The model family exhibits consistent scaling of validation loss and increasing Romanian factual and cultural knowledge with model size. On the 1,000-question WWTBM benchmark, Neurograf-6B achieves 69.89% accuracy on Romanian-context questions, while Neurograf-3.2B reaches 67.38%. Compute-optimal analysis yields a parameter-scaling exponent of approximately 0.423.
Neurograf v1 serves as an experimental demonstrator rather than a production system. The study identifies practical challenges involving diacritic preservation, corpus quality, data composition, and tokenization efficiency, while demonstrating the feasibility of developing Romanian-first base models, instruction-following assistants, and semantic embedding models within a unified training pipeline.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-230](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
