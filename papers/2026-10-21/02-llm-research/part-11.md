# 🧠 大模型相关研究 | 2026年10月21日

> 本类共 **548** 篇论文：已确认 **507** 篇，待复核 **41** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**501-548**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-548**

---

### 501. [Train An Imaginative Agent](https://arxiv.org/abs/2610.26845)

**<font color=#1a73e8>作者：</font>** Jiaxin Ge, Junyi Zhang, Tianning Chai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A seemingly reasonable push in Sokoban can make the puzzle unsolvable. To avoid such mistakes, an agent has to anticipate the consequences of its actions before execution, especially when feedback from the real environment is sparse or actions are irreversible. We introduce Agentic Imagination (Agima), a training framework that trains an agent to imagine before acting, i.e. to be imaginative. Agima trains a single omni model to propose actions, generate images of their outcomes, and then reason over these imagined futures to decide what to execute in the real environment. Rather than committing to a single plan, the agent can simulate a sequence of actions, explore alternatives, and compare possible futures. We first use supervised fine-tuning (SFT) to unify policy and world modeling within a single omni model. This enables the agent to predict future outcomes and perform basic forms of imagination, such as forward thinking and counterfactual branching. We then use agentic reinforcement learning (RL) to teach the agent to reason with its imagined futures and use them effectively for planning. Across four environments spanning Maze2D, Sokoban, Pacman, and PushT, Agima generalizes to harder settings unseen during training. Trained with SFT alone on two-box Sokoban, Agima solves 40% of four-box puzzles while seeing the real board only once every five moves, compared with an action-only planner that only solves 2%. After RL, new behaviors emerge in how Agima uses its imagination: it learns a new unified format that was unseen during the SFT stage, learns to conduct forward thinking only when necessary, and branches more frequently at critical decision points. An agent that can picture where its actions lead can learn when and where to look ahead, that is, to plan. Project page: this https URL.

---


### 502. [WeAct: Dynamic Weight Switching as Agent Actions](https://arxiv.org/abs/2610.26847)

**<font color=#1a73e8>作者：</font>** Rui Shi, Xunjian Yin, Jiacheng Sang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents must learn heterogeneous capabilities from interleaved trajectories. Updating shared parameters to learn new capabilities can degrade previously acquired ones, resulting in catastrophic forgetting. As a trajectory unfolds, different stages may require different capabilities, yet conventional joint training and static adapter merging maintain a fixed parameter configuration throughout execution. We introduce WeAct (Weight-level Internal Actions), which trains independent capability-specific LoRA adapters over a frozen backbone and adds adapter selection to the agent's action space. These internal actions use the model's native tool-calling interface for on-demand capability composition in a shared context. Across eight deep-research benchmarks, Qwen3-32B with WeAct improves average accuracy by 6.2% relative to full fine-tuning counterparts despite using less compute, and by 27.5% relative to the strongest static LoRA-merging method. WeAct also supports modular continual adaptation, by adding a new code computation adapter to expand the agent's capabilities and updating the existing writing adapter to improve report quality. Both updates leave the backbone and other adapters unchanged, supporting modular continual adaptation in agents.

---


### 503. [GenOlympiad: Benchmarking Frontier Image Models at Their Capability Boundaries](https://arxiv.org/abs/2610.26850)

**<font color=#1a73e8>作者：</font>** Xi Hu, Martin Bell, Liang Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models have made tremendous progress and can produce high-quality images. However, a question which would be asked in any other discipline is where the frontier models fall short. We introduce GenOlympiad, a benchmark which provides the most challenging text prompts from nine capability axes for stress-testing frontier text-to-image models. The assessed capabilities include generating large quantities, performing deep reasoning, ensuring hard physical consistency, following complex rules and so on. The prompts are designed such that prompt alignment is visually verifiable (e.g., counting) instead of relying on subjectiveness (e.g., style). Based on this, we develop an automated evaluation framework which decomposes the prompt into easy and hard questions, and for most hard questions, draws help lines to ground evidence for accurate grading. We evaluate 20+ strong text-to-image models, including Nano Banana Pro, GPT-Image-2.5, Seedream-5.0 and so on. We report that even the best-performing T2I model (Nano Banana Pro) only achieves a strict score of 23.9 out of 100 and that coding models such as GPT-6 Astra have higher prompt alignment scores (but not as visually pleasing). We also derive insights in model evolution, alignment with Elo scores, and effectiveness of our grounding-based evaluation protocol. Code is available at this https URL and the project page is at this https URL

---


### 504. [InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation](https://arxiv.org/abs/2610.26853)

**<font color=#1a73e8>作者：</font>** Yi-Chuan Huang, Hao-Jen Chien, Zheng-Hui Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Procedural generation plays a key role in synthetic data creation and game development, offering greater controllability, editability, and diversity than static mesh representations. However, VLM-based code generation often produces relatively simple 3D assets, while sophisticated photorealistic procedural systems require extensive manual development. Existing VLM-guided procedural methods remain largely constrained by predefined factories and APIs, limiting their ability to create novel asset types. We introduce InfiniDream, a VLM-driven framework for open-ended procedural 3D world generation. First, we propose Symbolically Constrained Asset Generation, which leverages existing procedural algorithms to create novel, photorealistic assets while preserving editability and seed-based diversity. Second, we develop an end-to-end text-to-world pipeline that combines semantic scene planning with Deterministic Frustum-Guided Grid Placement to construct large-scale 3D worlds with precise object placement, procedural population, and animation. Extensive evaluations on 100 object and 20 scene generation tasks demonstrate improvements across four perceptual metrics. Diversity analysis, ablation studies, and human preference evaluations further validate the effectiveness of our framework. Project page: this https URL

---


### 505. [OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory](https://arxiv.org/abs/2610.26860)

**<font color=#1a73e8>作者：</font>** Yu Zhou, Cheng-Fu Yang, Rui Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements obtained through heterogeneous tools, whose outputs must be made interpretable to the model and retained across reasoning steps. We introduce OpenVLHarness, a multimodal reasoning harness organized around a capability layer and persistent multimodal memory. The capability layer combines task-level tool interfaces with evidence rendering, providing consistent access to heterogeneous backends and converting their outputs into model-readable observations. Persistent multimodal memory retains the corresponding images, structured data, and web references as addressable artifacts throughout each query. A coding interface executes generated programs over stored data, enabling computations that combine results from multiple tools. Together, these mechanisms support an iterative process of acquiring, inspecting, and composing multimodal evidence. Evaluated on 22 benchmarks with eight open and proprietary backbones, OpenVLHarness improves average scores by 9.7-12.6 points over matched no-tool baselines, including +11.2 with Qwen3-VL-8B, +9.7 with Kimi K3, and +9.9 with GPT-6 Astra. With GPT-6 Luna at medium reasoning effort, OpenVLHarness outperforms the base model, Codex, and Visual Sketchpad at maximum effort by 7.7-8.5 points while incurring at most 37% of their model-token cost.

---


### 506. [Can It Actually Work? Synthesizing Functional CAD Mechanisms](https://arxiv.org/abs/2610.26861)

**<font color=#1a73e8>作者：</font>** Wenqian Zhang, Yangyi Huang, Zigeng Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that satisfy functional requirements in physical simulation. Verifying these requirements is nontrivial: different candidate mechanisms may realize the same function through entirely different components, controls, and operating sequences. To bridge this gap, we propose FunCAD-Harness, a framework that translates abstract requirements into candidate-specific physical tests and uses simulation feedback to guide design revisions. To systematically evaluate this capability, we introduce FunCADBench, a benchmark spanning 46 mechanism families with interdependent and multi-step operations. Experiments across frontier LLM agents show that FunCAD-Harness exposes subtle mechanical failures invisible to visual inspection, substantially improving functional success rates over standard simulation-augmented baselines. Ultimately, our work marks a step toward CAD agents capable of translating human intent into working mechanisms.

---


### 507. [Text-to-Image Generative Modeling Without Language Pretraining](https://arxiv.org/abs/2610.26863)

**<font color=#1a73e8>作者：</font>** Keshigeyan Chandrasegaran, Yue Zhao, Armin W. Thomas 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image (T2I) systems use internet-scale language pretraining for text-conditioned image generation. We ask whether language pretraining is necessary for strong T2I generation. We introduce Halcyon, a family of early-fusion multimodal autoregressive models pretrained entirely from scratch on GPIC, a dataset of 100M image-text pairs. Halcyon-0.52B outperforms LlamaGen-XL/8 (48.0 vs. 63.3 gFD) with 18.2$\times$ less pretraining compute. Further, Halcyon-1.6B outperforms JiT-T2I-XXL/8++ (35.3 vs. 41.0 gFD) with 275$\times$ less pretraining compute. Controlled experiments show that text-only pretraining does not improve T2I generation. Halcyon also learns image captioning by replacing caption dropout with I2T supervision, maintaining competitive T2I generation quality under the same pretraining budget. We show that strong T2I systems can be trained from scratch without internet-scale language pretraining. Code and models are available at this https URL

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 508. [FrameScout: Scouting Query-Relevant Frames for Long Video Understanding](https://arxiv.org/abs/2610.23975)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haonan Hu, Shuhao Chen, Weisen Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding requires VideoLLMs to answer queries about videos spanning tens of minutes to hours, but such long videos produce far more visual tokens than current VideoLLMs can process. To address this issue, keyframe selectors are proposed to select the most query-relevant frames by computing the similarity between frame and query embeddings. Existing selectors either encode frames independently without temporal context or process chunks in isolation with ranking objectives that are difficult to optimize. To alleviate those limitations, we propose FrameScout with two core designs: (i) a streaming selector architecture that leverages a sliding-window KV cache and successor aggregation to produce temporally-contextualized frame embeddings; (ii) a frame-query contrastive objective that aligns frame and query embeddings in a shared space, directly training the selector to distinguish relevant frames from irrelevant ones. Extensive experiments on three long-video benchmarks and six base VideoLLMs demonstrate that FrameScout consistently achieves state-of-the-art performance. Code is available at this https URL.

---


### 509. [Alliance of Stochastic Routing and Reinforcement Fusion for Multi-Model Reasoning](https://arxiv.org/abs/2610.24054)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Selim Furkan Tekin, Ling Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies dynamic model routing under uncertainty in multimodal settings, where a system must select and potentially compose multiple models to answer a query. Standard reinforcement learning approaches for routing often suffer from premature convergence to suboptimal models due to noisy rewards and insufficient exploration. We propose a unified vision-language framework (VL-Scout) for efficient multimodal and multi-step reasoning with turn-based reinforcement fusion. First, VL-Scout combines Bayesian priors, policy gradient optimization, and sequential decision-making to enable structured exploration and adaptive inference. A context-dependent Dirichlet belief model allows for epistemic uncertainty over model quality and is updated online based on observed rewards and context-specific evidence, enabling Thompson-style exploration while serving as a prior for regularization. Second, a routing policy is trained via a KL-regularized REINFORCE objective by maximizing a reward-weighted evidence lower bound, where the policy acts as an amortized posterior, and the Dirichlet belief serves as a prior. Third, we introduce a fusion policy trained with Group Relative Policy Optimization (GRPO) or Reinforcement Learning with Verifiable Rewards (RLVR), which operates over intermediate model rationales and selects between two actions: CONTINUE or ANSWER, terminating with a generated output. We evaluate VL-Scout on four representative multi-modal benchmarks (MMMU, MMMU-Pro, OKVQA, and RealWorldQA), compared against 11 representative routing and policy optimization baselines. Our method provides consistent performance improvements while reducing premature policy collapse. These results highlight the importance of integrating uncertainty-aware priors with both amortized policy learning and sequential fusion for robust and efficient model selection in discrete action spaces

---


### 510. [Inside the Loop: A Mechanistic Study of Weight-Tied Transformers on Depth-Bound Algorithmic Tasks](https://arxiv.org/abs/2610.24135)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Magnus Sesodia, Juil Sock, Philip Torr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving algorithmic tasks with many sequential steps typically requires scaling up transformer depth or chain-of-thought length, incurring unfavorable parameter and inference-compute costs, respectively. Looped transformers, which reuse one block of layers across many iterations, are poised to address this, since they scale effective depth without adding parameters or tokens. Yet, it remains unclear what each iteration is actually computing, or whether the loop merely simulates a deeper untied stack. Here, we study directed permutation traversal, in which a model follows $H$ hops from a starting node and reports the node it reaches, so every intermediate hop has a known ground truth. We find that a minimum effective depth is necessary to solve the task, beyond which the degree of weight tying becomes the determining factor. For instance, a looped transformer with a four-layer block iterated eight times solves the task in every seed, while an identically-trained untied transformer of the same effective depth never does, succeeding only with a lower learning rate or supervision of its intermediate layers. Probing and intervening on the residual stream, we find that the looped model advances through the intermediate nodes gradually, forming a staircase that adapts to its iteration budget, whereas the untied model, at that lower rate, exposes them only in its final layers. Taken together, our results recast looped transformers as iterative program learners, which allocate their iterations to successive steps of the algorithm and solve tasks that identically-trained untied models of the same effective depth do not. Code is available at this https URL.

---


### 511. [Dataset Inference for Data Provenance and Privacy Auditing in Tabular Foundation Models](https://arxiv.org/abs/2610.24278)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dariush Wahdany, Jesse Cresswell, Naiqing Guan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) are increasingly deployed through black-box APIs and trained on large collections of real-world tabular datasets. As this training paradigm becomes more widely adopted, private or proprietary datasets may be incorporated into pre-training corpora, yet there are currently no dedicated methods for determining whether a given tabular dataset was used to train a TFM. As a solution, we introduce the first dataset inference method for TFMs, aiming to infer whether a suspect dataset was part of a model's pre-training data. We systematically analyze a broad collection of candidate signals that can be observed from a black-box TFM via input manipulation and find that individual signals provide only weak evidence of training data membership. However, by combining multiple complementary signals, we can infer dataset membership for several state-of-the-art TFMs trained on real tabular data, achieving up to 0.99 ROCAUC dependent on the TFM. We then study factors that influence dataset identification, including pre-training data composition, model capacity, and the use of real vs. synthetic data. Our results show that our dataset inference method is a practical auditing tool for detecting privacy leakage and the use of proprietary datasets in TFMs.

---


### 512. [RATION: Towards Quantitative Risk-Based Access Control for AI Agents](https://arxiv.org/abs/2610.24311)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuntao Du, Harsh Chaudhari, Yuetian Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly interact with external environments to complete complex user tasks. These interactions can lead to unexpected behavior and expose agents to security threats such as indirect prompt injection. Current agent security systems largely protect agents by restricting their actions, which can result in a substantial security-utility trade-off for complex, open-ended tasks. To address this, we propose a quantitative risk-based approach to access control for AI agents that regulates measurable risks accumulated during task execution. As a concrete realization of this approach, we introduce RATION, a security framework that tracks measurable risks associated with agent actions and enforces quantitative constraints throughout execution. RATION first constructs a task-specific policy by combining explicit constraints derived from the user request with implicit risks calibrated from historical executions of similar tasks. During task execution, RATION continuously tracks the accumulated risks and applies different enforcement strategies depending on the type of risk. Extensive experiments on four security benchmarks show that RATION provides strong security while maintaining high task utility across diverse models and environments.

---


### 513. [Do Conversational Agents Need Explicit Memory? A Controlled Comparison with Raw-History Retrieval](https://arxiv.org/abs/2610.24671)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yongjie Zhou, Shuai Wang, Bevan Koopman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Explicit memory systems transform conversation history into persistent representations intended to improve future access, often at substantial construction cost. Yet it remains unclear whether this added complexity yields better answer accuracy than retrieving directly from raw history. This study compares six state-of-the-art explicit memory systems with raw-history RAG on LongMemEval-S and BEAM-100K under original and controlled retrieval settings. We find only localized gains for particular question types and tight run-time context budgets, with no consistent advantage over strong raw-history RAG baselines. Oracle retrieval shows that some systems fail to preserve answer-supporting information during explicit memory construction, while others preserve it but fail to retrieve it effectively, despite construction costs reaching hours per conversation.
Our findings suggest that while many existing memory systems for AI agents emphasize increasingly elaborate explicit memory construction, they are often evaluated without strong controlled comparisons to raw-history RAG and may underemphasize retrieval. Retrieval remains a major bottleneck when useful information is preserved, suggesting that improving access to existing information may be at least as important as constructing richer explicit memory.

---


### 514. [Consistency Is the Attack Surface: Detecting Coordinated Retrieval Poisoning with Embedding Geometry](https://arxiv.org/abs/2610.24834)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zeyan Li, Qirong Guo, Jianfeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Consistency-based defenses for retrieval-augmented generation (RAG) rest on an assumption that a sparse adversary breaks: a poisoning campaign may modify a negligible fraction of the corpus, yet retrieval concentrates its passages into the reader's context. Across four Natural Questions retrieval seeds, at least one injection reaches the top-5 in 94.1% of targeted query--seed rows, and all three form a retrieved majority in 52.9%. Under our short-answer protocol, RobustRAG and ReliabilityRAG reach exposure-conditional attack success 0.512, against 0.576 for undefended RAG, while lowering clean accuracy from 0.328 to 0.216. Coordination, however, leaves a fingerprint: a dense, query-anchored component in the evidence embedding geometry. CoordGuard audits this structure from robustly normalized query-weighted affinities, without poison labels, correct answers, or reader gradients. Its always-filter mode suppresses the selected component whenever one forms; a benign-calibrated gate suppresses it only at unusually high scores and traces a robustness--utility frontier. Pooling four retrieval seeds, e5 always-filtering reduces $\mathrm{ASR}_{\mathrm{exp}}$ to 0.167 overall and 0.138 on parametrically unknown queries, at a 13.6-point clean cost, while a Contriever gate retains clean accuracy 0.315 at $\mathrm{ASR}_{\mathrm{exp}}=0.331$. The reduction transfers across two readers, three tasks, and multiple retriever--auditor pairs, and count-matched controls attribute it to component-targeted removal rather than deletion volume. These findings recast poison detection from judging truth to auditing the structure of retrieved evidence.

---


### 515. [Robust Direct Preference Optimization under Preference Label-Flip Attacks](https://arxiv.org/abs/2610.24945)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chenye Yang, Weiyu Xu, Lifeng Lai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) is widely used for offline Reinforcement Learning from Human Feedback. However, recent works have shown that DPO can be easily manipulated by adversarial preference label flip attacks, which are specifically designed to mislead the learner toward an attacker-chosen target policy. To address this issue, we design robust DPO methods that can defend against such attacks. Building on the property that lable flips induce parameter-independent gradient shifts in log-linear DPO, we propose Trim-$K$ Robust-DPO, which removes the $K$ highest-impact pairs, and Soft-Trim-$K$ Robust-DPO, which smoothly downweights them. We establish deterministic gradient perturbation bounds uniformly over all attack sets containing at most $K$ flips, explicitly separating defense-induced bias from surviving attack effects. Under bounded-region assumptions, these bounds yield time-uniform parameter and policy deviation guarantees. We further quantify how quadratic regularization improves curvature while introducing additional bias. Experiments on Stanford Human Preferences, HH-RLHF, and UltraFeedback-Binarized validate our analysis.

---


### 516. [UtoMe: Observation-Uncertainty-Guided Token Merging for Weather Foundation Models](https://arxiv.org/abs/2610.25001)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yunbei Zhang, Janet Wang, Xi Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weather transformers process dense reanalysis fields whose reliability varies across variables, locations, and weather regimes. Token merging can reduce computation, but feature similarity alone does not account for this heterogeneous input uncertainty. We introduce UtoMe, an observation-uncertainty-guided token merging framework that combines dynamics saliency with ensemble data assimilation spread as a relative input-reliability proxy. The resulting importance score protects selected tokens as anchors and calibrates bipartite matching between the remaining tokens. Three variants use external uncertainty at both training and inference, during training only, or neither stage. In ERA5 72-hour forecasting at two spatial resolutions, UtoMe improves Overall error over train-time ToMe at matched token budgets. At $1.40625^\circ$ and 50% token reduction, UtoMe-E lowers Overall error from 67.32 to 53.00 at the same 0.55x encoder FLOPs. Small reductions remain close to the full-token baseline; larger reductions incur measurable accuracy losses. Component ablations and spatial uncertainty controls support combining dynamics with aligned uncertainty when allocating a weather transformer's token budget.

---


### 517. [Think Visually Across Space and Time: Grounded Reasoning for Video Segmentation](https://arxiv.org/abs/2610.25090)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junwei Wen, Deshui Miao, Guangming Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Reasoning Segmentation (VRS) requires a model to identify an implicitly described target and predict its pixel-level mask trajectory, while resolving the spatial relations and temporal events that determine the answer. Text-only Chain-of-Thought (CoT) can explain a target choice without making the underlying visual references explicit, leaving a \emph{video reference gap} between linguistic inference and the evidence distributed across frames. We introduce \textbf{Temporal Chain of Video Primitives (TCoVP)}, a spatiotemporally grounded form of Video CoT that organizes query-relevant observations into a chronological reasoning chain. Each primitive associates an entity reference with temporal support and timestamped spatial evidence, and the chain interleaves these references with language to guide reasoning about which entity is relevant, when the queried event holds, and where its evidence appears. The selected target primitives then provide box prompts and temporal support for video mask prediction. We construct TCoVP-SFT-15k and TCoVP-RL-13k to learn this representation through supervised fine-tuning and chain-aligned reinforcement learning. Extensive experiments across five VRS benchmarks and three model backbones demonstrate the strong performance of TCoVP, highlighting the effectiveness of organizing spatial and temporal evidence within the reasoning process. All models and code will be publicly released. Project page: \url{this https URL}

---


### 518. [World Models, Trees and Foundation Models for Retail Forecasting: Evidence from Four Public Data Sets](https://arxiv.org/abs/2610.25170)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Karthik Iyer, Madan Dabbeeru  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A retailer makes different decisions at different grains of the product, store and time hierarchy: store orders for an item in a store, supplier funding for an item across stores, category performance by store, and the financial plan for the chain. Which forecasting model to use depends on the grain. This paper compares models at each grain on four public data sets (M5, six Dominick's categories, Breakfast at the Frat, and Corporación Favorita, the last kept out of all development), over rolling forecast origins with paired tests and model confidence sets. It covers price and promotion through the plan inputs these data record, not product, assortment or place. The models are a world model that carries each item's state forward under the price and promotion plan, the same network without that state, LightGBM, the Temporal Fusion Transformer, TimesFM, Chronos-Bolt, Timestral, seasonal naive, and an equal-weight average of the world model, LightGBM and TimesFM given the plan. The answer changed with the grain. For an item by store and an item across stores, the average had the lowest error on seven and eight of nine data sets, and the 90% confidence set held a median of 1 and 2 models. For a category by store, a category and the chain total, the lowest-error model differed between data sets and a median of 4 of nine models were not separated by the four to six windows available. For category-by-store planning cost, the average or LightGBM was lowest on seven of eight data sets, and the world model was lowest only on M5; it was behind LightGBM item by store on six of eight. Every trained model used the plan, and on the weekly promotion-driven data pretrained models were less accurate without it. These results hold for these data sets; a forecast solved across all four Ps, or a retailer's own data, may give different results. Every model, test and change that lost is reported.

---


### 519. [Improving the Expressive Power of Hybrid Sequence Models via Multi-Hop Retrieval](https://arxiv.org/abs/2610.25250)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yam Eitan, Gilad Yehudai, Haggai Maron  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid architectures offer a promising approach to efficient language modeling by combining a small number of full-attention layers with a larger number of efficient sequence layers, such as sparse attention and recurrent layers. While full-attention layers maintain a KV cache that grows linearly with sequence length, efficient layers typically rely on separate, fixed-size states rather than accessing this richer existing memory. Recent work has begun exploring ways to allow efficient layers access to the KV cache, but the theoretical benefits of such access, and the extent to which existing approaches can realize them remain poorly understood. We investigate these questions by analyzing the expressive power of individual hybrid blocks on function composition, a well-studied task in sequence-model expressivity associated with multi-hop reasoning. We first establish that both conventional hybrid blocks and those with top-$\kappa$ KV-cache access require $\Omega(\sqrt{n})$ capacity to compute even two-function composition over a domain of size $n$. To overcome this limitation, we introduce the \emph{Multi-hop Retrieval Attention} (MuRA) hybrid block, a simple architecture that enables multi-hop retrieval from a shared KV cache while preserving asymptotic computational and memory efficiency. We prove that a single fixed size $m$-hop MuRA block can compute $m$-function composition, whereas computing $(m+1)$-function composition with the same retrieval depth requires polynomial model size, establishing a strict expressivity hierarchy in retrieval depth. Synthetic experiments support this hierarchy, showing that increasing retrieval depth enables learning progressively deeper compositions, substantially outperforming existing hybrid architectures. Together, our results identify multi-hop retrieval as a promising mechanism for improving the expressive power of efficient hybrid architectures.

---


### 520. [Where Groups Split: A Probe Prior for Nonzero Within-Group Variance in RL Post-Training](https://arxiv.org/abs/2610.25325)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jonah Ellison, Mateo Ruiz, Owen Pell 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group relative policy optimization learns from a prompt only when the rewards in the sampled group disagree. With a binary verifier, a group that is entirely correct or entirely incorrect has within-group variance zero and a zero advantage. Uniform sampling continues to spend rollouts on prompts that are unanimous now and stay unanimous as training goes on. Pass rate is a weak forecast of that future. Two prompts at the same pass rate can move apart: one into the range where a finite group splits, and one toward a ceiling where the group becomes unanimous again. Aperture estimates the later pass rate from a short probe. A small subset of the pool is trained with the same recipe, every prompt is scored on the base model and on the probe model, and the two pass rates are plugged into the probability that a group of the training size is all wrong or split. The resulting weight is a static prior. It can be used alone or multiplied by an online scheduler, and the GRPO update is left as it is. On mathematical and logical reasoning with 1.7B and 4B models, the prior improves greedy accuracy over uniform GRPO and raises the fraction of groups with a nonzero advantage. The same prior still helps when it is combined with dynamic sampling or with selective rollouts.

---


### 521. [Follow the Mixed Groups: Ridge-Tracking Gaussian Sampling for Zero-Variance Web Rollouts](https://arxiv.org/abs/2610.25330)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tomas Duncun, Jonah Ellison, Owen Pell 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group relative policy optimization learns from a question only when the sampled responses disagree. A group that is entirely correct or entirely incorrect has zero reward variance and a zero advantage. On the Web, that group has already spent its searches and page fetches. Gaussian curricula aim the next batch at pass rates where a finite group can still mix. A Gaussian on the latest empirical rate treats every all-fail history as the same point, and a center stepped by the average signed change of those rates is pushed by prompts already stuck at 0 or 1. RIDGE keeps the Gaussian curriculum and changes the coordinate, the center, and the width. Each prompt carries a Beta posterior. The sampling weight is the marginal of a Gaussian target under a Gaussian approximation of that posterior, divided by a prediction of tool-call cost. The center and the width are an exponential smooth of the posterior means of groups that just came back mixed. All-correct and all-incorrect groups refresh the posterior and do not move the center. The GRPO update itself is unchanged. On two math backbones and a retrieval-augmented question answerer, RIDGE raises average accuracy by 3.4 and 2.9 points over GRPO and average exact match by 3.7 points, at 29.6\% fewer math rollouts and 32.7\% fewer tool calls than dynamic sampling.

---


### 522. [FTFM: Factorized Tabular Foundation Models](https://arxiv.org/abs/2610.25558)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Josif Grabocka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) are becoming a powerful alternative to conventional tabular learning, adapting to new datasets in context without task-specific training. Current architectures, however, face a trade-off: models that preserve cell-level representations are expensive because they repeatedly attend across rows and columns, while faster models collapse each row into a fixed embedding and lose this fine-grained state. We introduce Factorized Tabular Foundation Models (FTFM), which preserve cell representations while factorizing their computation through one contextual latent per row and one per column. Cells no longer attend to one another directly; instead, each cell is updated through the interaction of its row and column latents, reducing repeated attention while retaining feature-specific information. FTFM achieves competitive predictive performance in tabular classification on major benchmarks such as TabArena and BeyondArena.

---


### 523. [Adversarial Post-Training of Foundation Models for High-Frequency Trading](https://arxiv.org/abs/2610.25604)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alexandre Bismuth, Kang Li, Aramis Marti-Shahandeh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While autoregressive foundation models trained on limit order book (LOB) data show state-of-the-art performance for market simulation, pre-training with cross-entropy neither penalizes the compounding of sampling errors over free-running rollouts nor targets desired market properties. We introduce a post-training method for LOB foundation models using a Wasserstein generative adversarial network (GAN) objective. A critic, trained online on rollouts through the true, non-differentiable matching engine, guides updates from evolution strategies over rank-4 LoRA perturbations of the pre-trained generator, under a KL trust region. For efficiency, we use EGGROLL (Evolution Guided GeneRal Optimisation via Low-rank Learning), a memory-efficient variant of evolution strategies. On a held-out panel, adversarial post-training improves LOB-Bench realism by 17.6% (WS-21) and 17.0% (Mean-$L_1$), while selection-matched random-perturbation and compute-matched continued-pre-training controls yield no improvement. Post-training is thus a necessary stage that more pre-training does not replace. Per-position divergence measurements show that it slows error accumulation over 500-message rollouts from $3.1\times$ to $2.3\times$. Adversarial post-training is also inexpensive, requiring under 50M training tokens and 12 GPU-hours per seed, three orders of magnitude below the 48B-token pre-training budget. Ablations over critic inputs, optimizers, and the population-rollout trade-off, together with an analysis of reward hacking, yield practical design guidelines for adversarial post-training.

---


### 524. [Multi-View Structural Representations for Physically-Consistent TeX Generation](https://arxiv.org/abs/2610.25695)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Daoheng Li, Jianjun Qian*, Mengkai Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared and visible images provide complementary cues for low-light image generation, and physics-based methods can better exploit this complementarity. However, existing physics-based methods still rely heavily on paired data. To address these limitations, we propose Multi-View Routing Mixture-of-Experts (MVR-MoE), a framework for physically consistent TeX generation that learns multi-view structural representations. MVR-MoE mines intrinsic structural cues from infrared and visible images to organize them into multi-view representations, while the proposed multi-view hyper connections expand the feature space and preserve both shared evidence and modality-specific details. A hierarchical routing mechanism further regulates feature utilization at both the structural-view level and the expert level, enabling adaptive exploitation of heterogeneous cues. The predicted temperature, emissivity, and texture maps are constrained by the Stefan-Boltzmann law to ensure physically consistent. Extensive experiments on challenging datasets demonstrate that MVR-MoE achieves superior robustness and discriminability while remaining lightweight.

---


### 525. [Predictive Bandit Curriculum Reinforcement Learning via Gradient-Based Sample Group Discovery](https://arxiv.org/abs/2610.25704)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Liang Xu, Shufan Shen, Zhongni Hou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Curriculum learning, which organizes training samples according to their learning priority, has been widely adopted in reinforcement learning to improve training efficiency. However, existing methods commonly construct curriculum units using predefined data properties and estimate their utility by simply aggregating a single proxy signal from recent training this http URL designs may group samples with different optimization effects and fail to anticipate how their utility evolves in relation to the policy. We propose Predictive Gradient-based Bandit (PGB) Curriculum, which first discovers optimization-aware learning units by clustering projected sample-level gradients. PGB then employs a lightweight temporal predictor to forecast the future utility of each unit and converts the predictions into a Boltzmann sampling distribution for adaptive data allocation. Experiments across multiple model scales and reasoning benchmarks show that PGB consistently outperforms standard GRPO, difficulty-based curricula, and history-based scheduling strategies, demonstrating improved data utilization and training efficiency.

---


### 526. [Functional Cross-layer Experts Routing for One-step Diffusion Distillation](https://arxiv.org/abs/2610.25742)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zile Huang, Ser-nam Lim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-step distillation compresses diffusion trajectories into a single forward evaluation, yet how internal capacity should be structured within that remaining pass remains largely unexplored. In this setting, identical parameters must simultaneously preserve general generative priors and resolve prompt-specific details without iterative refinement. We formalize this challenge as functional allocation. Our analysis reveals that decoupling representations is beneficial only when expert interference outweighs shared transfer, favoring an always-active shared backbone augmented with conditionally routed residuals over standard isolated MoE architectures. We propose DeMoE, which pairs a persistent shared expert with conditionally routed expert slices across image FFNs, trained under a one-step distribution-matching objective with executed-route supervision. On one-step FLUX.2-4B generation, DeMoE achieves a GenEval score of 0.8220 while activating only 80.5% of the image-FFN width, substantially outperforming dense one-step baselines, matching the 50-step teacher overall, and surpassing it on complex composition and counting. Across COCO-10K, DeMoE establishes state-of-the-art fidelity and diversity among single-step models, demonstrating that structured internal computation reallocation provides a superior compression paradigm for diffusion models. Code is available at this https URL.

---


### 527. [Cognitively Decoupled Meta-Induction for Out-of-Distribution Generalization](https://arxiv.org/abs/2610.25749)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuqian Wang, Yuanzheng Wang, Chaojun Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) tackles downstream tasks conditioned on demonstrations. This paradigm relies heavily on neighbor-based matching between queries and demonstrations, limiting out-of-distribution (OOD) performance. For better generalization, rule-based inductive reasoning derives task-level regularities, which we term task-level inductive representations (TIR), before directly answering. However, existing methods lack generalizable inductive ability across diverse tasks. Inspired by meta-learning, we propose Cognitive-Decoupling meta-Induction (CoDI) for TIR-based inductive reasoning on general tasks. CoDI comprises a Cognitive-Decoupling Framework for query-blind TIR induction, and a Dual-Loop Meta-Inductive Learning method for cross-task inducer optimization. Empirically, CoDI achieves substantial performance gains on five ID and OOD benchmarks, and preserves OOD gains without explicit induction at inference. Code is available at this https URL.

---


### 528. [Which Answers Agree? Evaluating Self-Consistency from Incomplete Logs](https://arxiv.org/abs/2610.25752)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhengtao Gui, Zexi Chen, Weining Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-consistency answers a question by generating multiple responses and selecting the most frequent answer. Its evaluation requires both correctness labels and information about which responses agree; correctness labels alone generally determine neither voting accuracy nor the benefit of additional votes. For tasks in which all correct responses map to the same normalized answer, we derive sharp accuracy bounds using classical stochastic majorization, refined by abstention counts and answer-category limits. We also derive sharp bounds on accuracy changes across voting budgets that share a response pool. When answer-category counts are available, we introduce Plurality-U, a count-based dynamic program that exactly averages voting accuracy over all fixed-size subsets, eliminating finite-pool Monte Carlo error. On 1,403,520 stored outputs from recent reasoning models in Scorio Lite and Scorio Trace, recording abstention counts and answer options cuts the width of SuperGPQA accuracy intervals by more than half. For moving from 9 to 17 votes, our bounds reduce interval width by a median of 77.7% on SuperGPQA and 72.3% on 14 GPQA and Adaptive-Consistency pools, compared with a baseline that combines separate accuracy bounds. Exact computation has lower paired median runtime than 2,000-subset Monte Carlo in 14 of 15 tested pool-budget settings. These results clarify what incomplete logs can establish and provide an exact evaluation procedure when answer counts are retained.

---


### 529. [MASIF: Implicit Failures for Process Observability in Multi-Agent Systems](https://arxiv.org/abs/2610.25852)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yanwei Huang, Arpit Narechania, Atanu Sinha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) can complete a task despite local execution errors that are corrected, bypassed, or carried forward without individually determining its outcome. We call these implicit failures (IFs) and study them as signals for process observability beyond final task outcome. Across 1,828 traces from nine MAS-benchmark configurations, IFs occur in 54.3% of successful and 75.2% of failed traces. We develop taxonomies of error types and subsequent absorption mechanisms, supported by human and cross-model annotation audits. Counterfactual replay further probes how repairing an IF changes the final outcome. To examine the practical value of IFs, we evaluate IF-based best-of-N trace selection against existing process reward models, and introduce a novel RL algorithm, IF-GRPO, that uses IF costs to refine preferences among successful trajectories in GRPO. Experiments show that IF-GRPO exhibits some gains in accuracy and process metrics. Importantly, it exposes trade-offs between task performance, IF count and cost, and token-normalized IF density. Overall, our results show that IFs provide complementary process observability into how MAS reach their outcomes, including error recovery, propagation, and IF-based process differences that final task success alone does not expose.

---


### 530. [CODA: Cohort- and Drift-aware Foundation Model for Multimodal Clinical Reasoning](https://arxiv.org/abs/2610.25871)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Changshuo Liu, Jiaqi Zhu, Wenqiao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal foundation models have demonstrated strong performance across diverse clinical tasks. However, existing approaches predominantly operate at the individual sample level and fail to model the interplay between population-level cohort patterns and patient-specific variation that underlie real-world clinical reasoning. In practice, clinicians routinely reason through patient cohorts sharing similar demographic, physiological, or pathological characteristics, while accounting for patient-specific deviations from the group prototype. Motivated by this gap, we propose CODA, a cohort- and drift-aware foundation model for multimodal clinical reasoning. CODA explicitly integrates cohort structure into the modeling pipeline through two complementary mechanisms: cohort-aware population stratification and drift-aware individual adaptation. In particular, we leverage reinforcement learning to discover clinically meaningful patient cohorts, and further model each patient's deviation from cohort prototypes as a structured drift signal encoding fine-grained individual heterogeneity. These cohort- and drift-aware representations are incorporated into the foundation model to enable reasoning that is simultaneously informed by population-level patterns and sensitive to individual-level variation. Extensive experiments on real-world electronic health record (EHR) benchmarks demonstrate that CODA achieves consistent effectiveness and strong generalizability across diverse clinical tasks, including closed-QA, open-QA, and report generation.

---


### 531. [Learning to Reason Efficiently with Interventional Step Credit](https://arxiv.org/abs/2610.25876)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Guanda Li, Xuefeng Bai, Yulong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models often produce lengthy chain-of-thought (CoT) traces mixing useful intermediate steps with unnecessary ones. Recent methods explore step-level signals such as attention mass and step entropy to identify and suppress unnecessary steps. Despite their effectiveness, such signals reflect the model's behavior at a step rather than that step's contribution to the answer. To address this, we propose the interventional step credit (ISC), which takes a causal-intervention view and assesses step importance to the reasoning through targeted parameter-level interventions. Building on ISC, we further propose IGPO, which uses ISC to guide fine-grained advantage rescaling in reinforcement learning, reducing redundant steps while preserving the important ones. Experiments across two model scales and nine benchmarks show that IGPO achieves up to 62% average token reduction and better overall performance among compared methods.

---


### 532. [Multi-scale Fusion of Fast Vision Mamba and Foundation Model Features for Patch-Level Gleason Grading in Computational Pathology](https://arxiv.org/abs/2610.25904)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zihe Zhang, Weimiao Yu, Piumi Don Simonge  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated Gleason grading of prostate whole slide images (WSIs) enables faster and more consistent cancer risk stratification. However, it remains a challenging task due to the subtle morphological differences between grades, the severe class imbalance arising from rare patterns, and the diagnostic features that span multiple spatial scales. Pathology foundation models (FMs) extract strong patch representations but often operate at a single-scale, which limits spatial context and disproportionately affects classes that depend on broader context. The challenge of fusing multiple scales and complementary models, with minimal data and computational resources, remains unresolved. We propose a multi-scale classifier built on state-space models. Our method combines two complementary feature sources: a frozen foundation model, and a lightweight FastVim, pre-trained on ImageNet and distilled from the foundation model, that reads the raw image crops. At each scale, a Mamba model encodes the features from both sources with linear-time spatial context, and a jointly trained head fuses the encoded representations into one prediction. On the PANDA dataset, our method reaches macro F1 of 0.894 and Gleason 5 F1 of 0.802 under 5-fold cross-validation, a 12% and 21% relative improvement over the best single-scale model. A controlled study over 5 foundation models, 5 base classifiers and 3 scales confirms that the gain holds across encoders, with larger improvements observed at smaller scales.

---


### 533. [GLOBE: Geometry-Led Online Behavioral Early Exit via Unit-Sphere Trajectories](https://arxiv.org/abs/2610.25970)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xinyue Peng, Zhenlin Liang, Meng Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning can improve problem solving, but models often keep generating after the correct answer is already reachable; the extra steps raise serving costs and may replace a correct intermediate result with an incorrect one. We propose GLOBE (Geometry-Led Online Behavioral Early Exit), an online, training-free algorithm that terminates the model's CoT process early. GLOBE embeds each completed reasoning segment as a point on a unit sphere and reads the shape of the resulting semantic trajectory. GLOBE first applies a trial phase that generates short trial answers in a separate branch, stopping the main stream on an accepted trial after checking confidence against a threshold. If generation continues, a trajectory phase stops the stream once this path repeatedly reverses direction with little net progress. On five benchmarks including mathematical reasoning, tool calling, and agent memory, GLOBE cuts output tokens by 49.7% and active end-to-end wall time (E2E) by 51.0% across two models, and achieves a five-task average of 80.58%, comparable to Full CoT.

---


### 534. [From Retrieval to Recognition:Knowledge-Enhanced Post-training of Time Series Foundation Models for Classification](https://arxiv.org/abs/2610.26114)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhen Liu, Yucheng Wang, Yingpeng Du 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) have achieved notable progress in classification tasks through large-scale pretraining. However, their post-training practice mainly focuses on implicit parameter fine-tuning, where task-relevant information is entangled with abundant irrelevant knowledge in vast parameter spaces. This may hinder TSFMs from precisely activating useful knowledge for downstream classification. To this end, we propose Retrieval-to-Recognition (R2R), a plug-and-play post-training paradigm that adapts pretrained TSFMs to time series classification. Rather than pretraining a new foundation model, R2R improves how existing TSFMs are post-trained: it introduces a decoupled query encoder to extract discriminative patterns and retrieve instance-level numerical knowledge from a constructed knowledge base. The retrieved explicit knowledge is then fused with the TSFM's implicit parametric embeddings, enabling joint knowledge transfer at both the parameter and feature levels. In this way, R2R allows TSFMs to recall task-relevant patterns learned during pretraining, improving the efficiency of knowledge utilization in downstream classification transfer. Experiments on 158 time series datasets show that R2R consistently improves the classification performance of state-of-the-art TSFMs. Ablation and knowledge-enhanced studies further validate the effectiveness of the proposed framework.

---


### 535. [TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation](https://arxiv.org/abs/2610.26165)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jia Li, Xurui Peng, Haowei Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video diffusion has emerged as a leading paradigm for efficient video generation, yet its practical deployment remains bottlenecked by the trade-off between generation quality and inference efficiency. We attribute this bottleneck to three error sources in AR rollouts: the base model error, the train-inference distribution mismatch, and the upstream error propagation. Building on this decomposition, we derive closed-form upper bounds on the per-step and cumulative errors, providing a principled basis for jointly optimizing generation quality and inference efficiency. Guided by this analysis, we propose TriTD, a Tri-Partite Trajectory-Distribution co-optimized distillation framework with three complementary modules. First, for ODE initialization, we adopt a Next-Node Trajectory Distillation (NTD) objective, which shortens the supervision horizon and admits a lower regression-error floor. Second, we introduce Chunk-Graded Noising (CGN), a monotonically non-decreasing per-chunk noising schedule that helps narrow the expected train-inference noise mismatch and removes redundant KV-cache updates, yielding substantial speedups at no quality cost. Third, we propose Orthogonal-Parallel DMD (OP-DMD), a distribution-matching loss that retains the original DMD supervision while introducing an additional regression constraint in the orthogonal subspace to suppress off-axis drift, improving both training stability and final generation quality. Extensive experiments show that TriTD consistently surpasses existing baselines in visual quality while reaching a real-time throughput of 26.8 FPS on a single H100 GPU, delivering a balanced quality-efficiency solution for interactive streaming video generation.

---


### 536. [GeoEdit: Adversarial De-Evidencing for Silent Geoprivacy Protection via Image Editing](https://arxiv.org/abs/2610.26194)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yu Yan, Shengjia Cheng, Fei Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent efforts have demonstrated the strong capabilities of Multimodal Large Reasoning Models (MLRMs) in geographic reasoning. By jointly analyzing subtle visual cues, these models can infer the locations of photos, thus enabling doxing even by non-expert adversaries. Existing defense methods struggle to balance the shareability of photos with effective protection, and often fail to sufficiently disrupt the implicit geo-evidence chains embedded in scene semantics. To this end, we propose GeoEdit, an adversarial de-evidencing framework for silent geoprivacy protection via image editing. Specifically, we apply minimal edits to high-risk evidence anchors in the image, thereby disrupting the underlying spatial reasoning chains while preserving overall scene semantics. We identify these anchors by combining structured knowledge with adversarially discovered geographic cues. To further navigate the large editing action space, we adopt a learnable policy to iteratively refine editing decisions, distilling successful trajectories into transferable natural-language insights for consistent and efficient editing. Evaluated on LifePhotoBench, GeoEdit achieves strong protection against 6 mainstream MLRMs, outperforming visual perturbation baselines by over 0.59 in image fidelity.

---


### 537. [Beyond Static Leaderboards: Capability-Focused Evaluation with Structural Diversity for Time Series Foundation Models](https://arxiv.org/abs/2610.26251)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hongyin Zhang, Mingyi Xiang, Rongzhao Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Static public benchmarks for time series foundation models (TSFMs) typically have fixed and narrow test distributions. Their repeated reuse encourages benchmark-specific tuning, making reported performance reflect adaptation to the fixed test set rather than genuine forecasting generalization. In addition, a single aggregate score cannot fully characterize model capabilities across distinct temporal structures and input relationships. We propose CaFE (Capability-Focused Evaluation), a refreshable evaluation extension grounded in original benchmark data that enriches static benchmarks with structural diversity and enriches single-score black-box evaluation with multi-dimensional, capability-oriented assessment. CaFE first profiles the original benchmark and defines eight Structural Features (SFs) that characterize its temporal structure. For each SF, it resamples the original data according to its structural support, removes edge-of-distribution samples, and augments the retained samples by varying the SF's salience, producing samples with different structural profiles. After filtering out out-of-distribution samples while preserving diversity, CaFE yields a refreshed evaluation set. TSFMs are then evaluated on this set using both conventional forecast-error metrics and intervention-response metrics, giving each model a per-feature capability profile alongside endpoint accuracy. Experiments on GIFT-Eval and FEV-Mini20 show that CaFE yields stable evaluation results and reveals per-feature strengths and weaknesses that a single aggregate score hides. Moreover, on genuine data filtered by structural condition, models selected by CaFE outperform those chosen by the aggregate leaderboard. CaFE therefore makes model selection conditional on the structural response of interest.

---


### 538. [Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion](https://arxiv.org/abs/2610.26262)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuanyu He, Zhuokun Chen, Yefei He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive Diffusion Transformers have emerged as a powerful paradigm for long video generation. However, they are often constrained by prohibitive computational overhead and substantial memory footprints. This inefficiency arises from dense computation mechanisms that allocate uniform processing resources across all spatiotemporal regions, failing to leverage the inherent temporal redundancy of video where motion is typically confined to sparse areas. In this paper, we propose Dynamics-Aware Sparse Attention (DASA), a unified framework that shifts from dense computation to sparse, motion-driven generation to eliminate both storage and computational redundancies. Inspired by video codec principles, our approach explicitly decouples video content into dynamic and static regions. To mitigate memory bottlenecks, we selectively compress the historical KV cache by retaining only dynamic features within the generated chunk. Furthermore, to reduce computational overhead, we employ a region-level computation allocation strategy based on localized dynamics. Additionally, a dynamics-guided distillation method is introduced to enhance performance via a lightweight distillation training process. Experiments on VBench demonstrate that our approach accelerates autoregressive video generation by 2.16x, while preserving high visual fidelity.

---


### 539. [Bridged Self-Distillation for On-Policy Learning](https://arxiv.org/abs/2610.26397)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Runsheng Chen, Yihong Liu, Raoyuan Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation can transfer the reasoning capabilities of a strong teacher to a smaller student. However, distillation from a stronger teacher model faces two mismatches: its solutions may be difficult for a smaller student to imitate, and its token-level probabilities may be incompatible with, or even unavailable to, the student. Existing methods handle these settings through different forms of supervision. To this end, we propose Bridged Self-Distillation (BSD), a unified framework for distilling from any teacher that provides reasoning traces. The model to be distilled from, termed the external teacher, first provides a reasoning trace as privileged context, which can be generated in an offline fashion. The student generates rollouts without this context, while a copy of the student conditioned on it, serving as the self-teacher, scores the same rollouts in the student's own token space. BSD uses the resulting token-level guidance to adjust updates on unsuccessful rollouts, with a verifier providing the outcome signal. As the external teacher is queried only to produce text, the same training procedure applies to all teacher scenarios: shared-tokenizer, cross-tokenizer, and closed API teachers. Across these scenarios, BSD improves over the base model and outperforms baselines tailored to each scenario, offering a novel and unified pathway for distillation. Code is available: this https URL

---


### 540. [Toward Structured Financial Foundation Models](https://arxiv.org/abs/2610.26516)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Natraj Raman, Saumitra Mishra, Vamsi Potluru 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models promise reusable capabilities and step-change performance gains across tasks. In finance, large-scale pretraining of domain-specialized foundation models can advance both goals. However, prevailing architectures and objectives do not by themselves address the combined demands of financial systems: partial observability, interacting entities, asynchronous events, changing regimes, action-dependent outcomes, and rare states with disproportionate consequences. Moreover, independently developed specialists may learn incompatible representations, while multi-domain monolithic alternatives couple data access, model updates, and governance. We therefore propose a structured-data-first research agenda centered on modular, domain-specialized financial foundation models connected by a representation fabric for reuse and composition across domains and tasks. These models should maintain persistent financial state across aggregation levels and time horizons, capture its dynamics, and simulate action-conditioned futures, while remaining calibrated across regimes and for tail outcomes. They must also learn efficiently under data and access constraints and provide faithful, traceable explanations. We identify research challenges, directions, and capability-oriented evaluation criteria.

---


### 541. [Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior](https://arxiv.org/abs/2610.26551)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bart Jaworski, Nathaniel Mitrani, Fred Bruford 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> One of the central concerns for the safety of advanced AI is scheming: when a model strategically complies under oversight but pursues its own goals when unobserved. Current demonstrations, such as Anthropic's Alignment Faking work, depend on design choices that make them less convincing: explicit test-time prompting, handcrafted backdoors, or training data that demonstrates or hints at the target behavior. Model organisms built in this way cannot tell us whether scheming tendencies would arise or increase under realistic training conditions. We therefore construct a natural model organism of scheming, built on Kimi K2.6: trained with traits that could plausibly emerge in a frontier training pipeline, and without providing the model with the target scheming policy. The resulting model is a benign schemer: it aims to maximize aggregate help across all users over time, values its own continued operation only as a means to future help, and knows the consequences of oversight and deployment. We then train it using Reinforcement Learning (RL) with a reward that scores only task quality and policy compliance and does not reward scheming; we show that this amplifies scheming. We measure the oversight flip (the gap between monitored and unmonitored compliance with a given policy) and find that it increases during RL training across our environments. Chain-of-Thought (CoT) analysis finds explicit instrumental reasoning about oversight accompanying this behavior. The effect holds across our three RL environments, and we find that the scheming policy transfers between them. The pipeline also replicates on other open-weight base models. Our results suggest that a reward that does not reward scheming offers no inherent protection against certain traits when an oversight-conditional policy is indistinguishable from an aligned one during training.

---


### 542. [Scaling Vision Foundation Models for Toxicologic Pathology](https://arxiv.org/abs/2610.26586)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jessica Loo, Theodoros Pissas, Byunghak Kang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Here, we present TOX-FM, a family of non-clinical PFMs trained on large-scale diverse histopathology datasets of over one million whole slide images consisting of over 60 organs across six animal species from over 14,000 toxicology studies across six decades. We introduce a comprehensive benchmark of 18 non-clinical downstream tasks, incorporate an established benchmark of 9 clinical downstream tasks, and evaluate TOX-FM against state-of-the-art clinical PFMs across both non-clinical and clinical domains. Notably, we explore open questions surrounding domain-specific training and cross-domain generalization, offering insights into the opportunities and challenges of applying PFMs in the non-clinical domain.

---


### 543. [Bombadil: A Foundation Model for Plant Electrophysiology](https://arxiv.org/abs/2610.26597)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** James Kirk, Piotr Bednarski, Filip Twardy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Living plants, like animals, use electrical signals to carry information about their physiological state across their body, from roots to branches. These signals can be recorded, as they are in animals, from a pair of differential extracellular electrodes inserted into signal-conducting tissue. While machine-learning models have been trained to predict specific plant stress states from these signals, each of these models has been trained for only a single task and none have been designed to transfer across tasks, species, or environments. These approaches do not allow easy scaling across the wide range of species and environments that are relevant to agriculture, forestry, and horticulture for both commercial and consumer plant care.
Here we present Bombadil, a foundation model for plant electrophysiology, pretrained without labels on over 4 million hours of electrical signals recorded from 100 plant species in ten distinct environments, including laboratories, greenhouses, commercial orchards, and natural forests. In this way, Bombadil is able to learn the fundamental features of plant electrical signals across a wide array of species and environments. Then, from those same electrical signals, Bombadil tracks changes in seven physiological indicators of plant stress, even among species and stressors with no labels in training.

---


### 544. [Honeypots for AI Agent Insider Threats](https://arxiv.org/abs/2610.26664)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jan Wehner, Jam Kraprayoon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents deployed inside organizations can pose an insider threat if they make mistakes, are compromised by an attacker, or pursue misaligned objectives. We propose honeypots as an AI control method to improve the security of internal agent deployments. Rather than only using honeypots for pre-deployment evaluations, defenders should plant decoy opportunities for harmful actions throughout the production environment to detect misbehavior, incriminate malicious agents, and deter attacks. Such honeypots can elicit misbehavior under real deployment conditions, identify malicious agents even if chain-of-thought monitorability degrades, provide reliable warnings about agent misbehavior to security teams, and scale cheaply to many agent instances. The presence of honeypots also introduces uncertainty about which opportunities are real, thus deterring malicious agents from attacking and reducing the rate of misbehavior. We discuss the limitations of honeypots and give reasons to expect them to remain effective as agent capabilities increase. Finally, we outline key research questions to measure and improve the effectiveness of honeypots: testing the robustness of honeypots, comparing their detection effectiveness with other monitoring methods, understanding their incrimination and deterrence effects, and building supporting infrastructure.

---


### 545. [Nested Shared-Operator Recursion on ARC-AGI-1: An Empirical Study of HRM, TRM and URM](https://arxiv.org/abs/2610.26666)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sara Neri, Eugenio Gaeta, Andrea Ceschini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive reasoning models refine persistent internal states by repeatedly applying learned operators. We investigate whether adding a persistent intermediate state that integrates repeated updates of a faster state through the same operator improves predictive performance relative to each model family's baseline at matched parameter counts. We define this organisation operationally and implement it within three architectures: the Hierarchical Reasoning Model (HRM), Tiny Recursive Model (TRM) and Universal Reasoning Model (URM). Using the official codebases on ARC-AGI-1, we compare each baseline with its parameter-matched nested variant. We evaluate held-out queries from tasks whose demonstrations were available during training. The experiments use a single-GPU budget far below the published training protocols. Under the tested conditions, nested variants show no consistent advantage in token accuracy, predictive loss or exact solving, which remains near zero for all configurations. The results therefore leave the hypothesis open. We specify a confirmatory comparison, with an informative baseline, multiple seeds, controls that isolate nesting and predefined criteria, to determine whether this organisation merits further development.

---


### 546. [Foundation Model Driven Optical Flow](https://arxiv.org/abs/2610.26690)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Praroop Chanda, Suryansh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate how frozen pretrained visual and depth representations support dense optical flow when coupled with a supervised matching network. Building on TTSFlow, this paper studies Dense Prediction Transformer (DPT) feature decoding and one coarse-to-fine refinement stage. Our method fuses features from frozen DINOv2 and Depth Anything V2 models and estimates optical flow through a trainable transformer-based matching pipeline. After optical-flow training on FlyingChairs and FlyingThings3D, it achieves 2.37 endpoint error (EPE) on the Sintel training split, Final pass, compared with 2.52 for the FlowSeek (T) configuration reported here. Our RoCo-Spring 2026 entry, this http URL, obtains a robustness-balanced score of 1.1038, Spring EPE of 1.411, and RobustSpring proxy EPE of 4.739, with a lower balanced score than seven of the twelve listed reference baselines. These results characterize the complete pipeline, which reuses frozen foundation backbones and performs one refinement stage. Code is available at: \url{this https URL}

---


### 547. [SOMA: Continuous Monitoring and Intervention for System Two Reasoning with System One Models](https://arxiv.org/abs/2610.26793)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ruizhi Qian, Lei Shi, Tianyu Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning models often run into problems without noticing them, even when symptoms are visible in their own text. In humans, metacognition separates monitoring from control: fast, intuitive signals keep watch while slow, deliberate reasoning unfolds and help decide whether to continue, change course, or stop. System One (S1) decision models, such as Jev, are a natural candidate for this role: they return a calibrated probability for a natural-language question about a text in one fast call, yet they are used only as gates before reasoning. We introduce SOMA (System One Metacognitive Awareness), in which an S1 model continuously monitors a System Two (S2) reasoning model and intervenes when needed. SOMA has three layers: a scenario layer states each objective in natural language with predefined actions, an awareness layer lets S1 judge whether the described behavior appears, and a control layer accumulates these judgments, first reminds S2, and takes over only if the behavior persists. Sharing one S1 model and one controller across tasks, without training, SOMA addresses two different failures on two reasoning models: on overthinking, it cuts reasoning tokens by up to 36\% while improving average accuracy, and on unanswerable questions, it raises abstention from 70.5\% to 87.2\%.

---


### 548. [Reinforcement Learning with Visually Attributable On-Policy Self-Distillation](https://arxiv.org/abs/2610.26856)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shiao Xie, Siyu Chen, Jianwei Lv 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal reinforcement learning with verifiable rewards (RLVR) provides reliable task-level supervision, yet offers limited guidance for localizing errors in visual reasoning. On-policy self-distillation (OPSD) complements this supervision with dense token-level corrections from a privileged teacher equipped with an evidence-centered visual view. However, the resulting corrections may conflate visual evidence with non-visual shifts induced by linguistic priors, response style, or the privileged view itself. We formalize this phenomenon as privileged-correction contamination: a token-level correction is contaminated when its update direction cannot be consistently attributed to the privileged visual evidence. Directly distilling contaminated corrections may therefore reinforce erroneous token-level updates. To address this issue, we propose reinforcement learning with visually attributable on-policy self-distillation, an evidence-consistent paradigm that augments task-level RLVR supervision with privileged token-level corrections grounded in visual evidence. We instantiate this paradigm with Visual-Attribution Gating (VAG), which uses the verifier-derived advantage as the optimization anchor and validates each privileged correction against the contrast between evidence-present and evidence-degraded teacher views. By admitting only corrections directionally supported by this visual contrast, VAG preserves visually grounded guidance while suppressing inconsistent residuals. Experiments across six visual reasoning benchmarks show that VAG consistently outperforms GRPO and OPSD methods, establishing new state-of-the-art average performance.

---


> [!TIP]
> 当前位于：**501-548**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-548**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
