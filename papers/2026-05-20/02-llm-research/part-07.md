# 🧠 大模型相关研究 | 2026年05月20日

> 本类共 **346** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**301-346**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-346**

---

### 301. [Code-as-Room: Generating 3D Rooms from Top-Down View Images via Agentic Code Synthesis](https://arxiv.org/abs/2605.18451)

**<font color=#1a73e8>作者：</font>** Yixuan Yang, Zhen Luo, Wanshui Gan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Designing realistic and functional 3D indoor rooms is essential for a wide range of applications, including interior design, virtual reality, gaming, and embodied AI. While recent MLLM-based approaches have shown great potential for 3D room synthesis from textual descriptions or reference images, text-based methods struggle to capture precise spatial information, and existing image-conditioned agents suffer from instability and infinite looping when tasked with holistic room generation from top-down views. To address these limitations, we propose Code-as-Room, an MLLM-based agentic framework equipped with a structured execution harness, which represents 3D rooms with Blender codes. Given a top-down room image, the framework parses the reference image to extract scene elements and their spatial relationships, and synthesizes executable Blender code for geometry, materials, and lighting in a principled, multi-stage pipeline. A cross-stage memory module is maintained throughout to mitigate context forgetting inherent to existing agent-based frameworks. We further introduce a dedicated benchmark for code-based 3D room synthesis, encompassing various evaluation protocols. Based on our benchmark, comprehensive comparisons against existing agent-based methods are conducted to validate the effectiveness of our proposed execution harness.

---


### 302. [Speech-Guided Multimodal Learning for Vocal Tract Segmentation in Real-Time MRI](https://arxiv.org/abs/2605.18466)

**<font color=#1a73e8>作者：</font>** Daiqi Liu, Lukas Mulzer, Md Hasan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmenting vocal tract articulators in real-time MRI (rtMRI) is a challenging dynamic image segmentation problem characterized by low contrast, rapid motion, and limited spatial resolution. However, while rtMRI acquisitions may provide synchronized acoustic signals, existing methods discard this information, and the few multimodal approaches that incorporate audio cannot be deployed when audio is unavailable. We propose a three-stage framework that leverages acoustic and phonological supervision during training while requiring only the rtMRI image at inference: phonological representations are converted into spatial bounding-box priors for articulator localization, visual and acoustic encoders are aligned via dual-level cross-modal contrastive pretraining, and the learned representations are fused through a cross-attention decoder, effectively transferring multimodal knowledge into a single-modality inference pipeline. Evaluated on 75-Speaker~Annot-16 and USC-TIMIT datasets, our method outperforms existing unimodal and multimodal methods, demonstrating that multimodal supervision provides transferable benefits for precise and clinically deployable vocal tract segmentation.

---


### 303. [GAMMA: Global Bit Allocation for Mixed-Precision Models under Arbitrary Budgets](https://arxiv.org/abs/2605.18475)

**<font color=#1a73e8>作者：</font>** Zhangyang Yao, Haiyan Zhao, Haoyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-precision quantization improves the budget--accuracy trade-off for large language models (LLMs) by allocating more bits to sensitive modules. However, automating this allocation at LLM scale faces a unique combination of constraints: learnable approaches require quantization-aware training, which is infeasible for billion-parameter models; training-free alternatives rely on static proxy metrics that miss cross-module interactions and must be recomputed per target budget; and search-based methods are expensive without guaranteeing exact budget compliance. We propose GAMMA, a quantizer-agnostic framework that learns module-wise precision preferences entirely within a post-training pipeline. GAMMA optimizes a teacher-forced hidden-state reconstruction objective under an augmented Lagrangian constraint, and projects the learned preferences into exact budget-feasible discrete assignments via integer programming. A key property is score reuse: because the learned preferences encode a stable sensitivity ranking rather than budget-specific weights, a single training run serves arbitrary deployment targets by re-solving only the integer program, reducing per-budget adaptation from hours to a few minutes. Across Llama and Qwen models (8B--32B), GAMMA outperforms both fixed-precision baselines (up to +12.99 Avg.) and search-based mixed-precision methods (up to +7.00 Avg.), and can match fixed 3-bit quality at 2.5-bit average precision, enabling deployment at substantially smaller memory footprints.

---


### 304. [Vector RAG vs LLM-Compiled Wiki: A Preregistered Comparison on a Small Multi-Domain Research](https://arxiv.org/abs/2605.18490)

**<font color=#1a73e8>作者：</font>** Theodore O. Cochran  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We preregistered a comparison of two ways to help an LLM answer questions over a small research corpus: a single-round Vector RAG system and an LLM-compiled markdown wiki. Both systems answered the same 13 questions over 24 papers using the same answer-generating model, and their answers were scored by blinded LLM judges.
The wiki scored much better at connecting findings across papers, but its advantage in answer organization was not strong after judge adjustment. RAG met the preregistered test for single-fact lookup questions. The clean query-side cost result went against the expected wiki advantage: under the tested setup, the wiki used far more query tokens than RAG, so it could not recover any upfront build cost through cheaper queries.
Two exploratory analyses changed how we interpret the result. First, claim-level citation checking favored the wiki: its cited pages more often supported the exact claims being made, even though RAG scored better on the overall groundedness rubric. Second, a decomposition-based RAG variant recovered most of the wiki's advantage on cross-paper synthesis at lower LLM-token cost, but it did not recover the wiki advantage in claim-by-claim citation support.
The main conclusion is that grounded research synthesis is not a single capability. Systems can differ in how well they organize evidence, how well their citations support each claim, and how much they cost to run. In this study, no architecture was best on all three.

---


### 305. [DBES: A Systematic Benchmark and Metric Suite for Evaluating Expert Specialization in Large-Scale MoEs](https://arxiv.org/abs/2605.18498)

**<font color=#1a73e8>作者：</font>** Jing Wang, Hongxuan Lu, Jazze Young 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expert specialization in Mixture-of-Experts (MoE) models remains poorly understood, with traditional evaluations conflating architectural load-balancing with functional specialization. We introduce DBES, a comprehensive diagnostic framework combining a multi-domain benchmark with five theoretically grounded metrics: Routing Specialization, Normalized Effective Rank, Domain Isolation, Routing Stiffness Score, and N-gram Expertise measures.
Critical findings demonstrate distinct specialization paradigms across models: Qwen-series exhibit modular specialization with high domain isolation, while DeepSeek and GLM employ distributed collaboration. However, we emphasize that specialization is a diagnostic dimension, necessary but not sufficient for downstream performance. Most crucially, interventional evidence validates the actionability of these metrics: by using DBES to identify high-specialization expert paths during domain-specific post-training, we achieved 66% to 94.48% improvement in specialized domains with only 15% of original training resources, demonstrating that these diagnostic tools can be converted into concrete optimization operators. This work provides the first systematic methodology for evaluating expert specialization independently of accuracy metrics, offering crucial insights for the design and post-training optimization of next-generation MoE systems.

---


### 306. [Implicit Hierarchical GRPO: Decoupling Tool Invocation from Execution for Tool-Integrated Mathematical Reasoning](https://arxiv.org/abs/2605.18500)

**<font color=#1a73e8>作者：</font>** Li Wang, Xiaohan Wang, Xiaodong Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have increasingly leveraged tool invocation to enhance their reasoning capabilities. However, existing approaches typically tightly couple tool invocation with immediate execution. Such immediate tool interaction may disrupt the reasoning coherence of LLMs and constrain their expressivity, ultimately degrading reasoning performance. To this end, for the first time, we propose and formalize the problem of decoupling tool invocation from execution during reasoning, and introduce delayed execution with explicit control to enhance tool-integrated reasoning (TIR). Furthermore, we propose a hierarchical control framework and theoretically derive a surrogate loss that enables an implicitly hierarchical policy to learn behavior equivalent to that of an explicit hierarchical policy, leading to the proposed IH-GRPO algorithm. Extensive experiments on IH-GRPO achieve absolute improvements of 1.87\%, 2.16\%, and 2.53\% on Qwen3-1.7B, Qwen3-4B, and Qwen3-8B across six out-of-domain mathematical reasoning benchmarks over the strongest baseline method, while also yielding consistent performance gains in other domains. Our code is available at this https URL.

---


### 307. [Ancient Greek to Modern Greek Machine Translation: A Novel Benchmark and Fine-Tuning Experiments on LLMs and NMT Models](https://arxiv.org/abs/2605.18504)

**<font color=#1a73e8>作者：</font>** Spyridon Mavromatis, Sokratis Sofianopoulos, Prokopis Prokopidis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine Translation (MT) for Ancient Greek (AG) to Modern Greek (MG) is a low-resource task, constrained by the lack of large-scale, high-quality parallel data. We address this gap by introducing the AG-MG Parallel Corpus, a new resource containing 132,481 sentence-aligned pairs derived from literary, historical, and biblical texts. We present a novel corpus creation pipeline that combines web-scraped, excerpt-level data with a multi-stage sentence-level alignment, and refinement process. Our method uses VecAlign with LaBSE embeddings, which we first fine-tune on a manually-aligned AG-MG subset, followed by an LLM-based error/misalignment correction phase using Gemini 2.5 Flash to ensure high alignment quality. Furthermore, we provide the first comprehensive benchmark of modern MT models on this task, evaluating three fine-tuning strategies across NMT models (NLLB, M2M100) and a Greek LLM (Llama-Krikri-8B). Our experiments show that fine-tuning yields significant improvements over base models, increasing performance by up to +10.3 BLEU points. Specifically, full-parameter fine-tuning of Llama-Krikri-8B achieves the highest overall performance with a BLEU score of 13.16, while the QLoRA-adapted M2M100-1.2B model demonstrates the largest relative gains and highly competitive results. Our dataset and models represent a significant contribution to Greek NLP.

---


### 308. [Easier to Judge than to Find: Predicting In-Context Learning Success for Demonstration Selection](https://arxiv.org/abs/2605.18512)

**<font color=#1a73e8>作者：</font>** Haochun Wang, Chaofen Yang, Jiatong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) is highly sensitive to which demonstrations appear in the prompt, but selecting them is expensive because the space of possible demonstration contexts and combinations is enormous. We argue that demonstration selection is \emph{easier to judge than to find}: predicting whether a specific query--context pair $(q,D)$ will succeed is cheaper and more general than searching for an optimal $D^\star$. Based on this insight, we propose DiSP, a sample-and-judge framework that stratifies queries by difficulty. DiSP runs random demonstration trials to estimate success rate of each training query, trains a lightweight router to predict difficulty from the query, and trains level-specific judges for sampled demonstrations. At inference, DiSP performs stop-on-acceptance judging under an explicit budget, emitting diagnostic risk tags when no suitable context is found. Across five classification datasets with Llama~3--8B and Qwen~2.5--7B, DiSP achieves the best average accuracy, improving over strong learned selection baselines by up to 3.4\%, while achieving up to $23\times$ end-to-end wall-clock speedup.

---


### 309. [AMR-SD: Asymmetric Meta-Reflective Self-Distillation for Token-Level Credit Assignment](https://arxiv.org/abs/2605.18529)

**<font color=#1a73e8>作者：</font>** Zhenlin Wei, Pu Jian, Yingzhuo Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The alignment of Large Language Models (LLMs) for complex reasoning heavily relies on Reinforcement Learning with Verifiable Rewards (RLVR). However, standard algorithms like GRPO apply sequence-level rewards uniformly to all tokens, creating a severe credit-assignment bottleneck. While on-policy self-distillation attempts to resolve this by conditioning a self-teacher on privileged contexts, direct exposure to raw oracle solutions often induces over-conditioned teacher distributions, implicit answer leakage, and late-stage training collapse. To overcome these limitations, we propose Asymmetric Meta-Reflective Self-Distillation (AMR-SD). Instead of conditioning directly on raw reference traces, AMR-SD inserts a reflection bottleneck: it compresses diagnostic signals -- from verifier outcomes, peer rollouts, or reference feedback -- into concise, self-generated Socratic hints and critiques. Furthermore, we introduce Causal Information Gain (CIG) with an asymmetric, ReLU-gated threshold to translate these reflections into sparse, highly precise token-level advantage modulations. Combined with temporal annealing, this mechanism preserves the base environmental reward while filtering out distributional noise. Experiments across scientific, mathematical, and tool-use benchmarks demonstrate that AMR-SD significantly outperforms existing baselines, achieving robust long-horizon stability and successfully preventing late-stage collapse.

---


### 310. [XCTFormer: Leveraging Cross-Channel and Cross-Time Dependencies for Enhanced Time-Series Analysis](https://arxiv.org/abs/2605.18534)

**<font color=#1a73e8>作者：</font>** Israel Zexer, Omri Azencot  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time-series analysis involves extracting informative representations from sequences of multiple interdependent variables, supporting tasks such as forecasting, imputation, and anomaly detection. In real-world scenarios, these variables are typically collected from a shared context or underlying phenomenon, suggesting the presence of latent dependencies across time and channels that can be leveraged to improve performance. However, recent findings show that channel-independent (CI) models, which assume no inter-variable dependencies, often outperform channel-dependent (CD) models that explicitly model such relationships. This surprising result indicates that current CD models may not fully exploit their potential due to limitations in how dependencies are captured. Recent studies have revisited channel dependence modeling with various approaches; however, these methods often employ indirect modeling strategies, which can lead to meaningful dependencies being overlooked. To address this issue, we introduce XCTFormer, a transformer-based channel-dependent (CD) model that explicitly captures cross-temporal and cross-channel dependencies via an enhanced attention mechanism. The model operates in a token-to-token fashion, modeling pairwise dependencies between every pair of tokens across time and channels. The architecture comprises (i) a data processing module, (ii) a novel Cross-Relational Attention Block (CRAB) that increases capacity and expressiveness, and (iii) an optional Dependency Compression Plugin (DeCoP) that improves scalability. Through extensive experiments on three time-series benchmarks, we show that XCTFormer achieves strong results compared to widely recognized baselines; in particular, it attains state-of-the-art performance on the imputation task, outperforming the second-best method by an average of 20.8% in MSE and 15.3% in MAE.

---


### 311. [VISAFF: Speaker-Centered Visual Affective Feature Learning for Emotion Recognition in Conversation](https://arxiv.org/abs/2605.18547)

**<font color=#1a73e8>作者：</font>** Linan ZHU, Zihao Zhai, Xiao Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotion Recognition in Conversation (ERC) is essential for effective human-machine interaction, aiming to identify speakers' emotional states in multi-turn dialogues. Early text-based methods struggle with complex scenarios like sarcasm because they inherently neglect vital non-verbal information. While recent Vision-Language Models (VLMs) address this by analyzing video directly, they are not inherently tailored for ERC and often focus on emotionally irrelevant background regions or passive listeners rather than the active speaker. Furthermore, fine-tuning these large models incurs prohibitive computational costs. Additionally, isolated visual signals are frequently ambiguous or technically compromised without the context of linguistic content and vocal prosody. To address these challenges, we propose VISAFF, a speaker-centered VISual AFFective feature learning framework for ERC. VISAFF consists of two stages: Speaker-Centered Affective Grounding and Reliability-Guided Affective Complementation. VISAFF utilizes a tuning-free approach to unlock the reasoning capabilities of frozen VLMs, efficiently steering them to focus on the active speaker's emotional visual cues without heavy training overheads. In the second stage, we introduce a reliability-guided affective complementation mechanism that dynamically leverages textual and acoustic modalities to compensate for visual uncertainty. Experiments on two real-world datasets demonstrate that VISAFF achieves highly competitive performance compared to state-of-the-art methods in a tuning-free setting, significantly enhancing computational efficiency by eliminating the need for expensive fine-tuning of large VLMs. The source code is available at this https URL.

---


### 312. [STT-Arena: A More Realistic Environment for Tool-Using with Spatio-Temporal Dynamics](https://arxiv.org/abs/2605.18548)

**<font color=#1a73e8>作者：</font>** Tingfeng Hui, Hao Xu, Pengyu Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) deployed in real-world agentic applications must be capable of replanning and adapting when mid-task disruptions invalidate their prior decisions. Existing dynamic benchmarks primarily measure whether LLMs can detect temporal changes in a timely manner, leaving the complementary challenge of adaptive replanning under spatio-temporal dynamics largely unexplored. We introduce STT-Arena (Spatio-Temporal Tool-Use Arena), a benchmark of 227 high-quality interactive tasks spanning nine spatio-temporal conflict types and four solvability levels. Each task is grounded in a realistic, executable environment equipped with injected spatio-temporal triggers that can abruptly invalidate an ongoing plan, forcing the model to detect the state shift and construct a revised execution strategy. Extensive evaluation of frontier LLMs reveals that even the SOTA proprietary models, including Claude-4.6-Opus, achieves less than 40\% overall accuracies, highlighting the fundamental difficulty of spatio-temporal dynamic reasoning. Systematic analysis of failure trajectories uncovers three recurring error modes of existing models: Stale-State Execution, Misdiagnosis of Dynamic Triggers, and Missing Post-Adaptation Verification. Guided by these findings, we propose an iterative trajectory refinement technique that eliminates these failure patterns from training data, and combine it with online RL to produce STT-Agent-4B which outperforms frontier LLMs on STT-Arena.

---


### 313. [Query-Conditioned Knowledge Alignment for Reliable Cross-System Medical Reasoning](https://arxiv.org/abs/2605.18570)

**<font color=#1a73e8>作者：</font>** Yan Jiao, Jingran Xu, Pin-Han Ho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cross-domain knowledge alignment is essential for integrating heterogeneous medical systems, yet existing approaches typically treat entity alignment as a static matching problem, ignoring query context and cross-system asymmetry. This limitation is particularly critical in integrative medical settings, where correspondence between concepts is inherently context-dependent, non-bijective, and direction-sensitive.
In this paper, we propose Query-Conditioned Entity Alignment (QCEA), which reformulates entity alignment as a query-conditioned correspondence problem. Instead of learning a fixed mapping between entity representations, QCEA treats the textual description of a source entity as a query and ranks candidate entities in the target graph, enabling context-dependent alignment. The framework integrates semantic encoding, graph-based representation learning, and a direction-aware transformation module to capture asymmetric and many-to-many correspondence across heterogeneous knowledge systems.
We evaluate QCEA on TCM--WM knowledge graphs derived from SymMap, covering both symptom alignment and herb--molecule alignment tasks. Experimental results show consistent improvements over representative baselines, particularly on rank-sensitive metrics such as Hit@K and MRR. Furthermore, downstream retrieval-augmented generation (RAG) experiments demonstrate that improved alignment leads to better evidence retrieval, stronger grounding, and higher answer accuracy. These findings highlight that alignment is not merely a data integration step, but a key factor that shapes knowledge accessibility and reliability in cross-system medical reasoning.

---


### 314. [MA$^{2}$P: A Meta-Cognitive Autonomous Intelligent Agents Framework for Complex Persuasion](https://arxiv.org/abs/2605.18572)

**<font color=#1a73e8>作者：</font>** Dingyi Zhang, Ziqing Zhuang, Linhai Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persuasive dialogue generation plays a vital role in decision-making, negotiation, counseling, and behavior change, yet it remains a challenging problem. In complex persuasion where the persuadee's internal states are not expressed clearly, the persuader must interpret responses, infer the persuadee's latent mental states (e.g., beliefs and desires), and translate them into targeted, strategy-consistent actions; however, current approaches often produce generic or weakly grounded responses even when such cues are identified. Moreover, although large language models (LLMs) can generate persuasive content, their performance varies substantially across domains due to uneven knowledge coverage and limited reasoning generalization. To address these challenges, we propose MA$^{2}$P, a meta-cognitive autonomous intelligent agent framework for complex persuasion. Specifically, we develop an autonomous multi-agent architecture that coordinates perception management, mental-state inference, strategy execution, memory maintenance, and performance evaluation. To mitigate cross-domain performance variation, we further design a meta-cognitive configurator that selects an appropriate meta-strategy from a structured knowledge base at the outset, thereby guiding subsequent reasoning and planning. Experimental results show that our approach achieves a higher persuasion success rate than baselines.

---


### 315. [S2Aligner: Pair-Efficient and Transferable Pre-Training for Sparse Text-Attributed Graphs](https://arxiv.org/abs/2605.18579)

**<font color=#1a73e8>作者：</font>** Yuhan Wang, Haopeng Zhang, Yibo Ding 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-training on text-attributed graphs (TAGs) is central to building transferable graph foundation models, where LLM-as-Aligner methods align graph and text representations through the semantic knowledge of large language models. However, these methods usually assume that node texts provide sufficient and reliable supervision, an assumption often violated in real-world sparse TAGs. When textual anchors are missing, noisy, or uneven across domains, graph structures must be aligned with weak semantic evidence, leading to unreliable structure-semantics correspondence and sparsity-induced transfer bias. This paper presents S2Aligner, a sparsity-aware and structure-enhanced LLM-as-Aligner framework for graph-text pre-training on sparse TAGs. The key idea is to decouple semantic alignment from structural modeling, allowing topology-aware signals to enhance alignment without contaminating the shared semantic space. Specifically, S2Aligner decomposes graph-text representations into semantic and structural components, uses structure-oriented reconstruction with consistency control to inject reliable topology cues into text representations, and suppresses inconsistent structural signals under textual sparsity. Moreover, S2Aligner introduces sparsity-aware cross-domain risk balancing, which calibrates domain risks through a global-domain density ratio and downweights unreliable sparse samples via graph reliability estimation. Theoretical analysis shows that this objective reduces cross-domain generalization gaps by controlling domain risk discrepancy. Extensive experiments across diverse graph domains, sparsity levels, and downstream tasks demonstrate that S2Aligner consistently outperforms existing baselines.

---


### 316. [Latent Action Reparameterization for Efficient Agent Inference](https://arxiv.org/abs/2605.18597)

**<font color=#1a73e8>作者：</font>** Wenhao Huang, Qingwen Zeng, Qiyue Chen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents often rely on long sequences of low-level textual actions, resulting in large effective decision horizons and high inference cost. While prior work has focused on improving inference efficiency through system-level optimizations or prompt engineering, we argue that a key bottleneck lies in the representation of the action space itself. We propose Latent Action Reparameterization (LAR), a framework that learns a compact latent action space in which each latent action corresponds to a multi-step semantic behavior. By reparameterizing agent actions into latent units, LAR enables decision making over a shorter effective horizon while preserving the expressiveness of the original action space. Unlike hand-crafted macros or hierarchical controllers, latent actions are learned from agent trajectories and integrated directly into the model, allowing both planning and execution to operate over abstract action representations. Across a range of LLM-based agent benchmarks, LAR significantly reduces the effective action horizon and improves inference efficiency under fixed compute budgets. As a consequence, our approach achieves substantial reductions in action tokens and corresponding wall-clock inference time, while maintaining or improving task success rates. These results suggest that action representation learning is a critical and underexplored factor in scaling efficient LLM agent inference, complementary to advances in model architecture and hardware.

---


### 317. [Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models](https://arxiv.org/abs/2605.18601)

**<font color=#1a73e8>作者：</font>** Shangwen Zhu, Qianyu Peng, Zhao Pu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern interactive video world models have achieved impressive visual fidelity, yet lack fine-grained multi-entity control and cross-entity, cross-world generalization. We trace this gap to the action interface: standard control protocols (e.g. animation IDs, device inputs, scene-level captions) bind action semantics to specific entities or engines at design time. We propose natural language as the interface to unlock expressiveness that no prior interface can achieve, and we present Incantation, the first interactive video world model with per-latent-frame (0.25 s) natural-language conditioning that supports simultaneous multi-entity control and concept-level cross-entity transfer beyond any fixed rendering pipeline. We pair a pretrained bidirectional video backbone with frame-local text cross-attention, and enable real-time long-horizon streaming through ODE-initialized Self-Forcing distillation with a RoPE-decoupled sliding KV-cache. We surpass the Action-Index baseline on cross-entity transfer (89% vs. 43%) and out-of-vocabulary prompts (90% vs. 0%), and our 2-step student sustains 19.7 FPS at 480p with stable FVD over 2-hour rollouts. We further apply the same architecture and training recipe to The King of Fighters, changing only the per-entity action vocabulary slots. We have released a preview subset of the Incantation dataset at this https URL, containing manually collected Elden Ring player-boss combat clips with structured action-oriented metadata. Larger-scale Elden Ring and KOF data will be released with the full project.

---


### 318. [Starve to Perceive: Taming Lazy Perception in VLMs with Constrained Visual Bandwidth](https://arxiv.org/abs/2605.18603)

**<font color=#1a73e8>作者：</font>** Yuhuan Wu, Cong Wei, Fangzhen Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) deployed as situated agents in high-resolution visual environments require active perception -- the ability to dynamically decide where to look through operations like zooming, cropping, and panning. However, current training paradigms produce models that mimic the surface form of such operations without functionally depending on their outputs, a phenomenon we term lazy perception. We trace this to a fundamental learning asymmetry: when coarse global views combined with language priors suffice for moderate accuracy, the model has no incentive to learn harder multi-step visual search. If a model can succeed without actively looking, it will never learn to look. This motivates Starve to Perceive, a training paradigm that constrains visual bandwidth -- restricting each observation to a tight token budget so that no single view suffices for task completion, making active perception the only viable strategy. Despite requiring no auxiliary losses, reward shaping, or architectural changes -- serving as a minimal, plug-in modification to standard post-training pipelines -- models trained under perceptual starvation achieve substantial gains of 5% average relative improvement across diverse benchmarks.

---


### 319. [Forecasting Downstream Performance of LLMs With Proxy Metrics](https://arxiv.org/abs/2605.18607)

**<font color=#1a73e8>作者：</font>** Arkil Patel, Siva Reddy, Marius Mosbach 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Progress in language model development is often driven by comparative decisions: which architecture to adopt, which pretraining corpus to use, or which training recipe to apply. Making these decisions well requires reliable performance forecasts, yet the two commonly used signals are fundamentally limited. Cross-entropy loss is poorly aligned with downstream capabilities, and direct downstream evaluation is expensive, sparse, and often uninformative at early training stages. Instead, we propose to construct proxy metrics by aggregating token-level statistics, such as entropy, top-k accuracy, and expert token rank, from a candidate model's next token distribution over expert-written solutions. Across three settings, our proxies consistently outperform loss- and compute-based baselines: 1) For cross-family model selection, they rank a heterogeneous population of reasoning models with mean Spearman Rho = 0.81 (vs. Rho = 0.36 for cross-entropy loss); 2) For pretraining data selection, they reliably rank 25 candidate corpora for a target model at roughly $10{,}000\times$ less compute than direct evaluation, pushing the Pareto frontier beyond existing methods; and 3) for training-time forecasting, they extrapolate downstream accuracy across an $18\times$ compute horizon with roughly half the error of existing alternatives. Together, these results suggest that expert trajectories are a broadly useful source of signal for assessing model capabilities, enabling reliable performance forecasting throughout the model development life cycle.

---


### 320. [CrossView Suite: Harnessing Cross-view Spatial Intelligence of MLLMs with Dataset, Model and Benchmark](https://arxiv.org/abs/2605.18621)

**<font color=#1a73e8>作者：</font>** Wei Wang, Yuqian Yuan, Tianwei Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence requires multimodal large language models (MLLMs) to move beyond single-view perception and reason consistently about objects, visibility, geometry, and interactions across multiple viewpoints. However, progress in cross-view reasoning remains limited by three major gaps: the scarcity of large-scale well-annotated training data, the lack of comprehensive benchmarks for systematic evaluation, and the absence of explicit alignment mechanisms that establish object-level consistency across views. To address these gaps, we thoroughly develop CrossView Suite across three coordinated components: CrossViewSet, CrossViewBench, and CrossViewer. Firstly, we introduce a multi-agent data engine to meticulously curate a large-scale, high-quality cross-view instruction dataset, termed CrossViewSet, covering 17 fine-grained task types with 1.6M samples. Second, we meticulously create a scene-disjoint CrossViewBench to comprehensively assess the cross-view spatial understanding capability of an MLLM, evaluating it across various aspects. Finally, we propose CrossViewer, a progressive three-stage framework for cross-view spatial reasoning in MLLMs, following a Perception -> Alignment -> Reasoning paradigm. Our method equips an adaptive spatial region tokenizer to capture fine-grained object representations, and then aligns the multi-view objects explicitly, and thus fuses aligned features for boosting the cross-view inference capacity for MLLMs. Extensive experiments and analyses show that large-scale training data, systematic evaluation, and explicit cross-view alignment are all critical for advancing MLLMs from single-view perception toward real-world spatial intelligence. The project page is available at this https URL.

---


### 321. [SCICONVBENCH: Benchmarking LLMs on Multi-Turn Clarification for Task Formulation in Computational Science](https://arxiv.org/abs/2605.18630)

**<font color=#1a73e8>作者：</font>** Nithin Somasekharan, Youssef Hassan, Shiyao Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed as scientific AI as- sistants, and a growing body of benchmarks evaluates their capabilities across knowledge retrieval, reasoning, code generation, and tool use. These evaluations, however, typically assume the scientific problem is already well-posed, whereas practical scientific assistance often begins with an ill-posed user request that must be refined through dialogue before any computation, analysis, or experiment can be carried out reliably. We introduce SCICONVBENCH, a benchmark for multi- turn clarification in scientific task formulation across four computational science problem domains: fluid mechanics, solid mechanics, materials science, and par- tial differential equations (PDEs). SCICONVBENCH targets two complementary capabilities: eliciting missing information (disambiguation) and detecting and correcting erroneous requests containing internally contradictory information (in- consistency resolution). Our benchmark pairs a structured task ontology with a rubric-based evaluation framework, enabling systematic measurement of LLM per- formance across three dimensions: clarification behavior, conversational grounding, and final-specification fidelity. Current frontier models perform relatively well on inconsistency resolution, but even the best model resolves only 52.7% of the disambiguation cases in fluid mechanics. We further find that frontier LLMs fre- quently make silent assumptions and perform implicit specification repairs that are not grounded in the conversation with users. SCICONVBENCH establishes a foundation for evaluating the upstream conversational reasoning that a reliable computational science assistant requires. The code and data can be found at this https URL.

---


### 322. [Data Presentation Over Architecture: Resampling Strategies for Credit Risk Prediction with Tabular Foundation Models](https://arxiv.org/abs/2605.18635)

**<font color=#1a73e8>作者：</font>** Aditya Tanna, Mitul Solanki, Mohamed Bouadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit default prediction is a tabular learning problem with severe class imbalance, heterogeneous features, and tight latency budgets. Tabular Foundation Models (TFMs) approach this problem through in-context learning, which makes their predictions sensitive to how the context window is built. We benchmark four classical models and five TFMs on the Home Credit and Lending Club datasets, varying the context-construction strategy (seven options) and the context size (1K to 50K). On both datasets, the choice of context strategy explains more variance in AUC-ROC than the choice of TFM family: balanced and hybrid sampling add 3 to 4 AUC points over uniform sampling, and the gap exceeds the spread between TFMs. With a balanced context of 5K to 10K examples, the strongest TFMs reach the AUC of classical baselines trained on the full data, while also recovering meaningful default-class recall that default-threshold GBDTs do not. We frame this as evidence that context construction, rather than architecture choice, is the primary deployment lever for TFMs in imbalanced credit-risk settings.

---


### 323. [Leveraging Latent Visual Reasoning in Silence](https://arxiv.org/abs/2605.18641)

**<font color=#1a73e8>作者：</font>** Dongyao Zhu, Zhen Wang, Xi Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent visual reasoning involves visual evidence more directly in multimodal reasoning by inserting continuous latent tokens before textual generation. However, the necessity of these latent tokens at inference remains ambiguous. We show that replacing latent tokens with random noise or removing them completely causes little performance degradation across spatial reasoning benchmarks. Reinforcement learning further diminishes the latent generation behavior after post-training. These observations raise a central question: Is latent visual reasoning still meaningful? We argue that its value should be measured by how effectively latent tokens guide learning, rather than whether they persist as an inference-time format. Our analysis shows that latent reasoning is unevenly favorable across question types, yet hard task-level routing for applying latent generation is brittle. Motivated by these findings, we propose an attention-based reward that encourages generated latent tokens to interact with later text tokens during RL. This reward promotes latent utilization when the latent mode is activated while preserving the flexibility to use pure-text reasoning. Experiments show that our method improves performance across perception and visual reasoning benchmarks, even when latent tokens are rarely generated after post-training. Our results highlight that, without explicit expression at inference, latent visual reasoning can shape better visual grounding and more accurate textual reasoning in silence. Our code and trained models are publicly available at \href{this https URL}{GitHub} and \href{this https URL}{Hugging Face}.

---


### 324. [Post-Trained MoE Can Skip Half Experts via Self-Distillation](https://arxiv.org/abs/2605.18643)

**<font color=#1a73e8>作者：</font>** Xingtai Lv, Li Sheng, Kaiyan Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) scales language models efficiently through sparse expert activation, and its dynamic variant further reduces computation by adjusting the activated experts in an input-dependent manner. Existing dynamic MoE methods usually rely on pre-training from scratch or task-specific adaptation, leaving the practical conversion of fully trained MoE underexplored. Enabling such adaptation would directly alleviate the inference costs by allowing easy tokens to bypass unnecessary expert during serving. This paper introduces Zero-Expert Self-Distillation Adaptation (ZEDA), a low-cost framework that transforms post-trained static MoE models into efficient dynamic ones. To stabilize this architectural conversion, ZEDA injects parameter-free zero-output experts into each MoE layer and adapts the augmented model through two-stage self-distillation, utilizing the original MoE as a frozen teacher and applying a group-level balancing loss. On Qwen3-30B-A3B and GLM-4.7-Flash across 11 benchmarks spanning math, code, and instruction following, ZEDA eliminates over 50% of expert FLOPs at marginal accuracy loss. It outperforms the strongest dynamic MoE baseline by 6.1 and 4.0 points on the two models, and delivers ~1.20$\times$ end-to-end inference speedup.

---


### 325. [Language-Switching Triggers Take a Latent Detour Through Language Models](https://arxiv.org/abs/2605.18646)

**<font color=#1a73e8>作者：</font>** Francis Kulumba, Wissam Antoun, Théo Lasnier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks on language models pose a growing security concern, yet the internal mechanisms by which a trigger sequence hijacks model computations remain poorly understood. We identify a circuit underlying a language-switching backdoor in an 8B-parameter autoregressive language model, where a three-word Latin trigger (nine tokens) redirects English output to French. We decompose the circuit into three phases: (1) distributed attention heads at early layers compose the trigger tokens into the last sequence position; (2) the resulting signal propagates through mid-layers in a subspace orthogonal to the model's natural language-identity direction; (3) the MLP at the final layer converts this latent signal into French logits. The entire circuit flows through a serial bottleneck at a single position: corrupting that position at any layer entirely mitigate the trigger but also hinder the model's capabilities. The orthogonal latent encoding suggests that defenses that search for language-like signals in intermediate representations would miss this trigger entirely.

---


### 326. [MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652)

**<font color=#1a73e8>作者：</font>** Ziyun Zeng, Hang Hua, Bocheng Zou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent GUI agents have made substantial progress in visual grounding and action prediction, yet they remain brittle in long-horizon tasks that require maintaining task state across many interface transitions. Existing agents typically rely on raw history replay or text-only memory, which either overwhelms the model with redundant screenshots or discards localized visual evidence needed for future decisions. To address these limitations, we introduce \textbf{MementoGUI}, a plug-in agentic memory framework that equips MLLM-based GUI agents with \textbf{MementoCore}, a learned controller for online memory selection, compression, and retrieval. Rather than treating interaction history as a fixed context, MementoGUI formulates long-horizon GUI control as an online memory-control problem: working memory selectively preserves task-relevant interface events with textual summaries and ROI-level visual evidence, while episodic memory retrieves reusable past trajectories through learned relevance selection. MementoCore modularizes memory control into specialized operators for step processing, memory compression, episodic writing, and episodic selection, enabling plug-in memory augmentation without finetuning the GUI agent backbone. We further develop a scalable data curation pipeline that converts computer-use trajectories into memory-controller training data, introduce \textbf{MementoGUI-Bench} for evaluating long-horizon decision-making in GUI agents, and design MLLM-based metrics for semantic action matching, task progress, and memory consistency. Experiments on GUI-Odyssey, MM-Mind2Web, and MementoGUI-Bench show that MementoGUI consistently improves GUI agents over no-history, history-replay, and text-only memory baselines, with larger MementoCore backbones further strengthening memory-augmented GUI control.

---


### 327. [Pocket Foundation Models: Distilling TFMs into CPU-Ready Gradient-Boosted Trees](https://arxiv.org/abs/2605.18654)

**<font color=#1a73e8>作者：</font>** Aditya Tanna, Nassim Bouarour, Mohamed Bouadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fraud scorer needs to answer in under 2 ms. The best tabular foundation models (TFMs) take 151-1,275 ms on GPU. We close this gap by distilling the TFM offline into an XGBoost or CatBoost student that runs natively on CPU. The central obstacle is specific to in-context learning (ICL) teachers: they leak labels when scoring their own training set, so the soft targets collapse to near-one-hot vectors with no inter-class structure left to distill. Stratified out-of-fold (OOF) teacher labeling prevents this. Across 153 classification datasets drawn from TALENT, OpenML-CC18, TabZilla, and TabArena, distilling TabICLv2 into XGBoost gives 0.882 macro-mean AUC (96.5% of teacher AUC) at 1.9 ms on CPU, a 38x to 860x speedup across teacher-student pairs with a statistically significant edge over a tuned CatBoost baseline (Wilcoxon p = 0.0008; 51% win rate). Four further findings: teacher rank transfers exactly to student rank; gains concentrate on low-dimensional data (< 21 features: +0.011 over CatBoost vs. >21 features: +0.001); multi-teacher averaging helps MLP students (+0.006, p = 0.003) but adds less than 0.001 for tree students; and on high-dimensional tasks where the teacher itself trails CatBoost, distillation makes things worse rather than better. The full pipeline is open-sourced as part of the TabTune library.

---


### 328. [KairosHope: A Next-Generation Time-Series Foundation Model for Specialized Classification via Dual-Memory Architecture](https://arxiv.org/abs/2605.18657)

**<font color=#1a73e8>作者：</font>** Luis Balderas, José Alberto Rodríguez, Miguel Lastra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Foundation Models (TSFMs) have demonstrated notable success in general-purpose forecasting tasks; however, their adaptation to specialized classification problems remains constrained by the computational bottleneck of standard attention and the systematic omission of classical statistical knowledge. This technical report introduces KairosHope, a next-generation TSFM designed to reconcile massive generalization with analytical precision in classification tasks. The core of the proposal is the HOPE block, an architecture that replaces quadratic attention with a dual-memory system: Titans modules for dynamic short-term retention and a Continuum Memory System (CMS) for the abstraction of long-term historical context. To enrich the inductive bias, a Hybrid Decision Head is introduced, which fuses deep latent representations with deterministic statistical features extracted via tsfeatures package. KairosHope undergoes self-supervised pre-training on the massive Monash archive, combining Masked Time Series Modeling (MTSM) and contrastive learning (InfoNCE). Its subsequent adaptation to the UCR benchmark datasets is conducted through a rigorous Linear Probing and Full Fine-Tuning (LP-FT) protocol to prevent catastrophic forgetting. Empirical results demonstrate superior performance in domains characterized by strict temporal causality such as HAR or Sensor data. Consequently, KairosHope establishes a robust and efficient framework for the adaptation of foundation models to time series analysis.

---


### 329. [Position: A Three-Layer Probabilistic Assume-Guarantee Architecture Is Structurally Required for Safe LLM Agent Deployment](https://arxiv.org/abs/2605.18672)

**<font color=#1a73e8>作者：</font>** S.Bensalem, Y. Dong, M. Franzle 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper argues that enforcing LLM agent safety within a single abstraction layer is not merely suboptimal but categorically insufficient for deployed LLM agents -- a structural consequence of how agent execution works, not a contingent limitation of current systems. The three dimensions that jointly constitute safe operation -- semantic intent and policy compliance, environmental validity, and dynamical feasibility -- each depend on a strictly distinct set of information that becomes available at different stages of execution. No single guardrail can certify all three. We argue that the community must respond with a contract-based architecture in which each safety dimension is enforced by an independently certified layer whose probabilistic guarantee satisfies the next layer's assumption. We sketch such an architecture and derive the compositional system-level safety bounds it admits via the chain rule of probability. Three open problems stand between this and a deployable standard: bound estimation from non-i.i.d.\ traces, graceful degradation of contracts under deployment drift, and extension to multi-agent settings -- the most important unfinished business in LLM agent runtime assurance.

---


### 330. [Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://arxiv.org/abs/2605.18678)

**<font color=#1a73e8>作者：</font>** Fengyi Fu, Mengqi Huang, Shaojin Wu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Lance, a lightweight native unified model supporting multimodal understanding, generation, and editing for both images and videos. Rather than relying on model capacity scaling or text-image-dominant designs, Lance explores a practical paradigm for unified multimodal modeling via collaborative multi-task training. It is grounded in two core principles: unified context modeling and decoupled capability pathways. Specifically, Lance is trained from scratch and employs a dual-stream mixture-of-experts architecture on shared interleaved multimodal sequences, enabling joint context learning while decoupling the pathways for understanding and generation. We further introduce modality-aware rotary positional encoding to mitigate interference among heterogeneous visual tokens and boost cross-task alignment. During training, Lance adopts a staged multi-task training paradigm with capability-oriented objectives and adaptive data scheduling to strengthen both semantic comprehension and visual generation performance. Experimental results demonstrate that Lance substantially outperforms existing open-source unified models in image and video generation, while retaining strong multimodal understanding capabilities. The homepage is available at this https URL.

---


### 331. [Democratizing Large-Scale Re-Optimization with LLM-Guided Model Patches](https://arxiv.org/abs/2605.18692)

**<font color=#1a73e8>作者：</font>** Tinghan Ye, Arnaud Deza, Ved Mohan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Optimization models developed by operations research (OR) experts are often deployed as decision-support systems in industrial settings. However, real-world environments are dynamic, with evolving business rules, previously overlooked constraints, and unforeseen perturbations. In such contexts, end users must rapidly re-optimize models to recover feasible and implementable solutions. This paper introduces an agentic re-optimization framework in which a large language model (LLM) acts as an OR expert, dynamically supporting end users through natural-language interaction. The LLM translates user prompts into structured updates of the underlying optimization model, selects suitable re-optimization techniques from an optimization toolbox, and solves the resulting instance to return implementable solutions. The toolbox leverages primal information, including historical solutions, valid inequalities, solver configurations, and metaheuristics, to accelerate re-optimization while preserving solution quality. The proposed framework enables interactive and continuous adaptation of deployed optimization models, reducing dependence on OR experts and improving the sustainability of decision-support systems. Extensive experiments on two complementary large-scale real-world case studies demonstrate the effectiveness and scalability of the proposed framework. The first considers online supply chain re-optimization, where solutions must be generated rapidly while remaining close to the deployed plan, whereas the second focuses on offline university exam scheduling, where solution quality is prioritized over runtime. Results show that the toolbox-driven architecture significantly improves computational efficiency through primal-based and solver-aware re-optimization techniques, while the structured patch-based updates improve interpretability and traceability of model modifications.

---


### 332. [SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents](https://arxiv.org/abs/2605.18693)

**<font color=#1a73e8>作者：</font>** Yifan Zhou, Zhentao Zhang, Ziming Cheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents are increasingly built around reusable skills, a central challenge is no longer only whether agents can use provided skills, but whether they can generate correct, reusable, and executable skills from repositories and documents. Existing benchmarks primarily evaluate the efficacy of given skills or the ability of agents to solve downstream tasks from raw context, but they do not isolate skill generation itself as the object of study. We introduce SkillGenBench, a benchmark for evaluating skill generation pipelines under a unified and controlled protocol. In SkillGenBench, a generator receives raw corpora and produces standardized skill artifacts, which are then executed under fixed harnesses and assessed with unified evaluation procedures. The benchmark covers two generation regimes: task-conditioned generation, where a task-specific skill is synthesized after the task is revealed, and task-agnostic generation, where a reusable skill library must be distilled before downstream tasks are known. It also spans two complementary procedural sources: repository-grounded instances, where procedures are distributed across code, configuration, and scripts, and document-grounded instances, where procedures and constraints must be distilled from long-form text. We provide standardized task specifications, pinned environments, and evaluation protocols centered on deterministic execution-based checks, supplemented by auxiliary signals for diagnosis. Experiments across a range of skill-generation methods and backbones show substantial performance variation, highlight the difficulty of reusable skill distillation, and reveal distinct failure modes in skill generation from software repositories versus long-form documents. SkillGenBench establishes a reproducible testbed for studying skill generation as an independent research problem in agent systems.

---


### 333. [Ensembling Tabular Foundation Models - A Diversity Ceiling And A Calibration Trap](https://arxiv.org/abs/2605.18696)

**<font color=#1a73e8>作者：</font>** Aditya Tanna, Yash Desai, Pratinav Seth 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) now match or beat tuned gradient-boosted trees on a growing fraction of tabular tasks, but no single TFM wins on every dataset. Ensembling is the go to fix here, and it works less well than expected. Six modern TFMs form a near-redundant pool: their mean pairwise Q-statistic is $0.961$, close enough to $1$ that any convex combination is bounded above. We benchmark six ensemble strategies over six TFMs on 153 OpenML classification tasks. The best ensemble, two-level cascade stacking, buys $+0.18\%$ accuracy over the strongest single TFM at $253\times$ the compute. A Friedman and Nemenyi analysis places three ensembles and the best base TFM in a single equivalence group; three other ensembles are significantly \emph{worse} than the best base. Stacking with a logistic-regression meta-learner is the most striking case: competitive accuracy and ROC-AUC, the worst log-loss rank among the ensembles. The meta-learner improves accuracy by sharpening class boundaries, which destroys calibration. We recommend greedy selection as the practical default.

---


### 334. [Distilling Tabular Foundation Models for Structured Health Data](https://arxiv.org/abs/2605.18702)

**<font color=#1a73e8>作者：</font>** Aditya Tanna, Nassim Bouarour, Mohamed Bouadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) achieve strong performance on health datasets, but their inference cost and infrastructure requirements limit practical use. We study whether their predictive behavior can be transferred to lightweight tabular models through knowledge distillation. Since in-context TFMs condition on the training set at inference time, naive distillation can introduce context leakage; we address this with stratified out-of-fold teacher labeling. Across $19$ healthcare datasets, $6$ TFM teachers, $4$ student families, and several multi-teacher ensembles, we find that distilled students retain at least $90\%$ of teacher AUC, outperforming teachers in some cases, while running at least $26\times$ faster on CPU and preserving calibration and fairness critical for health applications. Moreover, multi-teacher averaging does not consistently improve over the best single teacher. Leakage-aware distillation is thus a viable route for bringing TFM-quality predictions into inference-constrained health settings.

---


### 335. [EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL](https://arxiv.org/abs/2605.18703)

**<font color=#1a73e8>作者：</font>** Minrui Xu, Zilin Wang, Mengyi DENG 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Equipping LLMs with tool-use capabilities via Agentic Reinforcement Learning (Agentic RL) is bottlenecked by two challenges: the lack of scalable, robust execution environments and the scarcity of realistic training data that captures implicit human reasoning. Existing approaches depend on costly real-world APIs, hallucination-prone LLM simulators, or synthetic environments that are often single-turn or depend on pre-collected documents. Moreover, synthetic trajectories are frequently over-specified, resembling instruction sequences rather than natural human intents, reducing their effectiveness for RL training. We introduce EnvFactory, a fully automated framework that addresses both challenges. EnvFactory autonomously explores and verifies stateful, executable tool environments from authentic resources, and synthesizes natural multi-turn trajectories through topology-aware sampling and calibrated refinement, producing grounded queries with implicit intents. Using only 85 verified environments across 7 domains, EnvFactory generates 2,575 SFT and RL trajectories. Despite using significantly fewer environments than prior work, which are often 5 times more, EnvFactory achieves superior training efficiency and downstream performance, improving Qwen3-series models by up to +15% on BFCLv3, +8.6% on MCP-Atlas, and +6% on conversational benchmarks including $\tau^2$-Bench and VitaBench. By fully automating both environment construction and trajectory synthesis, EnvFactory provides a scalable, extensible, and robust foundation for Agentic RL.

---


### 336. [Semantic Generative Tuning for Unified Multimodal Models](https://arxiv.org/abs/2605.18714)

**<font color=#1a73e8>作者：</font>** Songsong Yu, Yuxin Chen, Ying Shan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) strive to consolidate visual understanding and visual generation within a single architecture. However, prevailing training paradigms independently optimize understanding via sparse text signals and generation through dense pixel objectives. Such a decoupled strategy yields misaligned representation spaces, isolating visual understanding from generation and hindering their mutual reinforcement. This work presents the first systematic investigation into generative post-training, where we formulate hierarchical visual tasks as generative proxies to bridge the isolation in UMMs. Our empirical investigation reveals that high-level semantic tasks, particularly image segmentation, serve as optimal proxies. Unlike low-level tasks that distract models with texture details, segmentation provides structural semantics that significantly enhance both vision-centric perception and generative layout fidelity. Building upon these insights, we introduce Semantic Generative Tuning (SGT), a novel paradigm that leverages segmentation as a generative proxy to align and synergize multimodal capabilities. Mechanistic analyses further demonstrate that SGT fundamentally improves feature linear separability and optimizes visual-textual attention allocation pattern. Extensive evaluations show that SGT consistently improves both multimodal comprehension and generative fidelity across mainstream benchmarks. Our code is available on the this https URL.

---


### 337. [SafeDiffusion-R1: Online Reward Steering for Safe Diffusion Post-Training](https://arxiv.org/abs/2605.18719)

**<font color=#1a73e8>作者：</font>** Komal Kumar, Ankan Deria, Abhishek Basu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have been widely studied for removing unsafe content learned during pre-training. Existing methods require expensive supervised data, either unsafe-text paired with safe-image groundtruth or negative/positive image pairs, making them impractical to scale. Furthermore, offline reinforcement learning and supervised fine-tuning approaches that generate synthetic data offline suffer from catastrophic forgetting, degrading generation quality. We propose a novel online reinforcement learning framework that addresses both data scarcity and model degradation through post-training with Group Relative Policy Optimization (GRPO) on both negative and positive text prompts. To eliminate the need for fine-tuning specialized safe/unsafe reward models, we introduce a \textit{steering reward mechanism} that exploits an inherent property of CLIP embeddings: steering text representations toward positive safety directions and away from negative ones in the embedding space. Our online-policy approach enables the model to learn from diverse prompts, including explicit unsafe content, without catastrophic forgetting. Extensive experiments demonstrate that our method reduces inappropriate content to 18.07\% (vs. 48.9\% for SD v1.4) and nudity detections to 15 (vs. 646 baseline) while improving compositional generation quality from 42.08\% to 47.83\% on GenEval. Remarkably, these safety gains generalize to out-of-domain unsafe prompts across seven harm categories, achieving state-of-the-art performance without supervised paired data or reward tuning. Github: this https URL.

---


### 338. [General Preference Reinforcement Learning](https://arxiv.org/abs/2605.18721)

**<font color=#1a73e8>作者：</font>** Muhammad Umer, Muhammad Ahmed Mohsin, Ahsan Bilal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training has split large language model (LLM) alignment into two largely disconnected tracks. Online reinforcement learning (RL) with verifiable rewards drives emergent reasoning on math and code but depends on a programmatic verifier that cannot reach open-ended tasks, while preference optimization handles open-ended generation yet forgoes the continuous exploration that powers online RL. Closing this gap requires a verifier for open-ended quality, but a scalar reward model is the wrong shape for the job. Quality is multi-dimensional, and any scalar score is an incomplete proxy that lets online RL collapse onto whichever axis the score is most sensitive to. We turn instead to the General Preference Model (GPM), which embeds responses into $k$ skew-symmetric subspaces and represents preference as a structured, intransitivity-aware comparison. Building on this, we propose General Preference Reinforcement Learning (GPRL), which carries the $k$-way structure through to the policy update. GPRL computes per-dimension group-relative advantages, normalizes each on its own scale so no axis can dominate, and aggregates them with context-dependent eigenvalues. The same structure powers a closed-loop drift monitor that detects single-axis exploitation and corrects it on the fly by reweighting dimensions and tightening the trust region. Starting from $\texttt{Llama-3-8B-Instruct}$, GPRL reaches a length-controlled win rate of $56.51\%$ on AlpacaEval~2.0 while also outperforming SimPO and SPPO on Arena-Hard, MT-Bench, and WildBench by resisting reward hacking across extended training runs.

---


### 339. [Predictable Confabulations: Factual Recall by LLMs Scales with Model Size and Topic Frequency](https://arxiv.org/abs/2605.18732)

**<font color=#1a73e8>作者：</font>** Matthew L. Smith, Jonathan P. Shock, Samuel T. Segun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While scaling laws govern aggregate large language model performance, no scaling law has linked factual recall to both model size and training-data composition. We evaluated 38 models on over 8,900 scholarly references evaluated by an automated reference verification system. Recall quality follows a sigmoid in the log-linear combination of model parameter count and topic representation in training data. These two variables alone explain 60% of the variance across 16 dense models from four families, rising to 74-94% within individual families. The form matches a superposition-inspired account in which recall is gated by a signal-to-noise ratio: signal strength scales with concept frequency and the noise floor with model capacity.

---


### 340. [Advancing Narrative Long Video Generation via Training-Free Identity-Aware Memory](https://arxiv.org/abs/2605.18733)

**<font color=#1a73e8>作者：</font>** Jinzhuo Liu, Jiangning Zhang, Wencan Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generation has improved rapidly in visual fidelity and interactivity, but it still suffers from long-term inconsistency and memory degradation. Most existing solutions either compress historical frames using predefined strategies or retrieve keyframes based on coarse implicit attention signals, both of which fail to handle evolving prompts with shifting entity references, leading to identity drift, character duplication, and attribute loss. To address this, we propose IAMFlow, a training-free identity-aware memory framework that explicitly models and tracks persistent entity identities, enabling consistent generation across prompt transitions. Specifically, an LLM extracts entities with visual attributes from each prompt and assigns unique global IDs for identity-aware memory, while a VLM asynchronously verifies and refines attributes from rendered frames, enabling explicit entity tracking in place of implicit similarity-based matching. To keep the proposed framework computationally practical, we design a systematic inference acceleration pipeline, including asynchronous visual verification, adaptive prompt transition, and model quantization, which achieves faster generation than existing baselines. Furthermore, we introduce NarraStream-Bench, a benchmark for narrative streaming video generation that features 324 multi-prompt scripts spanning six dimensions and a three-dimensional evaluation protocol that integrates both traditional metrics and multimodal large language model-based assessments. Extensive experiments show that IAMFlow, despite being training-free, achieves the best overall performance on NarraStream-Bench, outperforming the strongest baseline by 2.56 points, while achieving a 1.39$\times$ speedup over the most efficient baseline in the 60-second multi-prompt setting.

---


### 341. [What Does the AI Doctor Value? Auditing Pluralism in the Clinical Ethics of Language Models](https://arxiv.org/abs/2605.18738)

**<font color=#1a73e8>作者：</font>** Payal Chandak, Victoria Alkin, David Wu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medicine is inherently pluralistic. Principles such as autonomy, beneficence, nonmaleficence, and justice routinely conflict, and such ethical dilemmas often sharply divide reasonable physicians. Good clinical practice navigates these tensions in concert with each patient's values rather than imposing a single ethical stance. The ethical values that large language models bring to medical advice, however, have not been systematically examined. We present a framework for auditing value pluralism in medical AI, comprising a benchmark of clinician-verified dilemmas and an attribution method that recovers value priorities directly from decisions. The ecosystem of frontier models spans physician-level value heterogeneity, and models discuss competing values in their reasoning (Overton pluralism) before committing to a decision. However, individual model decisions are near-deterministic across repeated sampling and semantic variations, failing to reproduce the distributional pluralism of the physician panel. Across benchmark cases, these consistent decisions reflect committed, systematic value preferences. While most model priorities fall within the natural range of inter-physician variation, some significantly underweight patient autonomy. A single LLM deployed without regard for its value priorities could amplify those priorities at scale to every patient it serves. Without explicit efforts to balance ethical perspectives with one or multiple models, these tools risk replacing clinical pluralism with a deployment monoculture.

---


### 342. [Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation](https://arxiv.org/abs/2605.18740)

**<font color=#1a73e8>作者：</font>** Qianhao Yuan, Jie Lou, Xing Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) still struggle with fine-grained visual understanding, where answers often depend on small but decisive evidence in the full image. We observe a regional-to-global perception gap: the same MLLM answers fine-grained questions more accurately when conditioned on evidence-centered crops than on the corresponding full images, suggesting that many failures stem from difficulty to focus on relevant evidence rather than insufficient local recognition ability. Motivated by this observation, we propose Vision-OPD (Vision On-Policy Distillation), a regional-to-global self-distillation framework that transfers the model's own privileged regional perception to its full-image policy. Vision-OPD instantiates two conditional policies from the same MLLM: a crop-conditioned teacher and a full-image-conditioned student. The student generates on-policy rollouts, and Vision-OPD minimizes token-level divergence between the teacher and student next-token distributions along these rollouts. This enables the model to internalize the benefit of visual zooming without external teacher models, ground-truth labels, reward verifiers, or inference-time tool use. Experiments on multiple fine-grained visual understanding benchmarks show that Vision-OPD models achieve competitive or superior performance against much larger open-source, closed-source, and "Thinking-with-Images" agentic models.

---


### 343. [Code as Agent Harness](https://arxiv.org/abs/2605.18747)

**<font color=#1a73e8>作者：</font>** Xuying Ning, Katherine Tieu, Dongqi Fu 等 42 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent large language models (LLMs) have demonstrated strong capabilities in understanding and generating code, from competitive programming to repository-level software engineering. In emerging agentic systems, code is no longer only a target output. It increasingly serves as an operational substrate for agent reasoning, acting, environment modeling, and execution-based verification. We frame this shift through the lens of agent harnesses and introduce code as agent harness: a unified view that centers code as the basis for agent infrastructure. To systematically study this perspective, we organize the survey around three connected layers. First, we study the harness interface, where code connects agents to reasoning, action, and environment modeling. Second, we examine harness mechanisms: planning, memory, and tool use for long-horizon execution, together with feedback-driven control and optimization that make harness reliable and adaptive. Third, we discuss scaling the harness from single-agent systems to multi-agent settings, where shared code artifacts support multi-agent coordination, review, and verification. Across these layers, we summarize representative methods and practical applications of code as agent harness, spanning coding assistants, GUI/OS automation, embodied agents, scientific discovery, personalization and recommendation, DevOps, and enterprise workflows. We further outline open challenges for harness engineering, including evaluation beyond final task success, verification under incomplete feedback, regression-free harness improvement, consistent shared state across multiple agents, human oversight for safety-critical actions, and extensions to multimodal environments. By centering code as the harness of agentic AI, this survey provides a unified roadmap toward executable, verifiable, and stateful AI agent systems.

---


### 344. [Aurora: Unified Video Editing with a Tool-Using Agent](https://arxiv.org/abs/2605.18748)

**<font color=#1a73e8>作者：</font>** Yongsheng Yu, Ziyun Zeng, Zhiyuan Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video editing models have converged on a unified conditioning design: a single diffusion transformer jointly consumes text, source video, and reference images, and one set of weights covers replacement, removal, style transfer, and reference-driven insertion. The design is flexible, but it assumes that the user already provides model-ready text, reference images, and spatial grounding for local edits, which real requests often omit. We present Aurora, an agentic video editing framework that pairs a tool-augmented vision-language model (VLM) agent with a unified video diffusion transformer. The VLM agent maps a raw user request to a structured edit plan aligned with the transformer's conditioning channels, thereby resolving textual and visual underspecification before generation. We train the VLM agent with supervised data for complete edit planning and reference-image selection, together with preference pairs for robust tool use and instruction refinement. We introduce AgentEdit-Bench to evaluate agent-enhanced video editing under textual and visual underspecification. Experiments on AgentEdit-Bench and two existing video editing benchmarks show that Aurora improves over instruction-only baselines and that the VLM agent transfers to compatible frozen video editing models. Project page: this https URL

---


### 345. [DashAttention: Differentiable and Adaptive Sparse Hierarchical Attention](https://arxiv.org/abs/2605.18753)

**<font color=#1a73e8>作者：</font>** Yuxiang Huang, Nuno M. T. Gonçalves, Federico Alvetreti 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current hierarchical attention methods, such as NSA and InfLLMv2, select the top-k relevant key-value (KV) blocks based on coarse attention scores and subsequently apply fine-grained softmax attention on the selected tokens. However, the top-k operation assumes the number of relevant tokens for any query is fixed and it precludes the gradient flow between the sparse and dense stages. In this work, we propose DashAttention (Differentiable and Adaptive Sparse Hierarchical Attention), which leverages the adaptively sparse $\alpha$-entmax transformation to select a variable number of blocks according to the current query in the first stage. This in turn provides a prior for the second-stage softmax attention, keeping the entire hierarchy fully differentiable. Contrary to other hierarchical attention methods, we show that DashAttention is non-dispersive, translating to better long-context modeling ability. Experiments with large language models (LLMs) show that DashAttention achieves comparable accuracy as full attention with 75% sparsity and a better Pareto frontier than NSA and InfLLMv2, especially in high-sparsity regimes. We also provide an efficient, GPU-aware implementation of DashAttention in Triton, which achieves a speedup of up to over FlashAttention-3 at inference time. Overall, DashAttention offers a cost-effective strategy to model long contexts.

---


### 346. [Can These Views Be One Scene? Evaluating Multiview 3D Consistency when 3D Foundation Models Hallucinate](https://arxiv.org/abs/2605.18754)

**<font color=#1a73e8>作者：</font>** Soumava Paul, Prakhar Kaushik, Alan Yuille  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiview 3D evaluation assumes that the images being scored are observations of one static 3D scene. This assumption can fail in NVS and sparse-view reconstruction: inputs or generated outputs may contain artifacts, outlier frames, repeated views, or noise, yet still receive high 3D consistency scores. Existing reference-based metrics require ground truth, while ground-truth-free metrics such as MEt3R depend on learned reconstruction backbones whose failure modes are poorly characterized. We study this reliability problem by comparing neural reconstruction priors with classical geometric verification. We introduce \benchmark, a controlled robustness benchmark for multiview 3D consistency, and a parametric family that decomposes neural metrics into backbone, residual, and aggregation components. This family recovers MEt3R and yields variants up to $3\times$ more robust. Our analysis shows that VGGT, MASt3R, DUSt3R, and Fast3R can hallucinate dense geometry and cross-view support for unrelated scenes, repeated images, and random noise. We introduce COLMAP-based metrics that use matches, registration, dense support, and reconstruction failure as failure-aware consistency signals. On real NVS outputs and a structured human study, these metrics achieve up to $4\times$ higher correlation with human judgments than MEt3R.

---


> [!TIP]
> 当前位于：**301-346**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-346**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
