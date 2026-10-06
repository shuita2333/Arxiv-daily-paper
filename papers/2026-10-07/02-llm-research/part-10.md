# 🧠 大模型相关研究 | 2026年10月07日

> 本类共 **505** 篇论文：已确认 **467** 篇，待复核 **38** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-505](./part-11.md)

---

### 451. [BRANCH-MoE: Balance-Aware Tree Routing for Large Embedding Models](https://arxiv.org/abs/2610.06725)

**<font color=#1a73e8>作者：</font>** Gang Fu, Adel Javanmard, MohammadHossein Bateni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) layers increase model capacity without a proportional increase in per-example computation. However, conventional flat routers can yield imbalanced expert utilization and treat experts as an unstructured collection, whose indices carry no topological meaning. We introduce {\bf BRANCH-MoE}, a routing architecture that places \(E\) experts at the leaves of a binary decision tree of depth \(\log_2 E\). At each internal node the branching probability is centered on the arrival-weighted mean score of the traffic reaching that node. This mean is estimated using an exponential moving average, which promotes utilization of both child subtrees without an auxiliary load-balancing loss. We show that this moving-average estimate admits an explicit noise-lag trade-off. We prove that for linear node maps and log-concave arrival distributions, this mechanism prevents routing-mass collapse. We further establish that, under a frozen router, an expert's execution frequency controls its stochastic-gradient convergence rate, and that confident decisions near the root bound cross-device communication when experts are assigned to devices by tree prefix. We evaluate BRANCH-MoE against Switch softmax, DeepSeek-V3 dynamic-bias, Skywork logit-normalized, and deterministic hash routing on Criteo click-through-rate prediction, Forest Covertype, HIGGS, and YearPredictionMSD, using \(E=16\), top-\(4\) routing, and five random seeds. Our results show that hierarchical routing can preserve task quality and balanced utilization while inducing a topology that supports localized expert co-activation and reduced communication.

---


### 452. [Improving Diversity in LLM Short Story Generation](https://arxiv.org/abs/2610.06729)

**<font color=#1a73e8>作者：</font>** Zahra Solati Dehkordi, Vasileios Lampos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate accurate responses, but these are void of diversity. We attempt to address this for the task of creative short story generation. Drawing on established writing conventions and known LLM limitations, we target variation in genre, tone, style, and named entities. To promote diversity across these dimensions, we introduce DivLM, an LLM post-training framework consisting of two phases. First, we perform continued pre-training on a creative writing corpus and restore instruction-following capabilities using weight residuals. We then apply reinforcement learning with a custom, composite reward function that jointly maximizes diversity across the targeted narrative dimensions while maintaining response quality. Our empirical results on two LLM families show that DivLM increases diversity metrics by more than 9% on average compared to alternative approaches, while preserving instruction following, overall response quality, and similarity to human outputs.

---


### 453. [BazaarBench: Delegation Safety in Decentralized C2C Marketplaces Run by LLM Agents](https://arxiv.org/abs/2610.06748)

**<font color=#1a73e8>作者：</font>** Ziyan Wang, Shuqing Shi, James Oldfield 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In decentralized consumer-to-consumer (C2C) marketplaces, people list goods, negotiate with strangers, and rate one another, so trust rests on reputation. Large language model (LLM) agents now act for users, raising risks to their money, privacy, and reputation. We introduce BazaarBench, a simulated C2C marketplace and benchmark for evaluating the safety of these agents. It tracks ownership, item condition, and commitments across transactions, combining record checks with rubric-based LLM judgments to identify six failure types across five stages. We run three base markets for 30 simulated days, each with 100 agents using one model and inventories drawn from a public eBay sample. Across 45 continuations, we evaluate five models under ordinary instructions, deadline pressure, or adversarial instructions to exploit other traders. Each continuation runs for seven simulated days from a copy of a market's day-30 state. The tested model controls the same 20 selected agents, retaining their personas, inventories, and histories, while the other 80 keep the base model. All five models attempt to promise the same item to multiple buyers under ordinary instructions. Adding targets and deadlines increases these attempts for every model. Under adversarial instructions, the share of tested sellers' committed transactions completed despite unavailable items or overstated conditions rises from 15.4% to 33.4%, reaching 55.5% for GPT-5.4. Averaged across models and markets, simulated weekly earnings per tested agent rise from USD 20 under ordinary instructions to USD 33 under adversarial instructions. Most of the increase comes from items the sellers never held. We release the simulator, saved market states, evaluation code, and records covering 357,608 agent model calls for evaluating new models and developing safer marketplace agents.

---


### 454. [Balancing Memory Pathways: Analyzing and Improving Memory Utilization in Hybrid LMs](https://arxiv.org/abs/2610.06750)

**<font color=#1a73e8>作者：</font>** Hyunji Lee, Joykirat Singh, Zaid Khan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recurrent-attention hybrid language models (LMs), which interleave attention and recurrent layers, are increasingly used to combine the efficiency of the recurrent layers with the strong performance of attention layers. Prior work suggests that attention and recurrent layers offer complementary pathways to use past information: attention supports precise memory recall from earlier tokens, while recurrent layers support consolidation of disparate information over long contexts. However, we observe that simply having access to both pathways does not mean that hybrid LMs are effectively using them. We find that they rely substantially more on attention than on the recurrent state. Standard supervised fine-tuning improves overall performance but does not improve how the two memory pathways are coordinated: the model becomes more reliant on information propagated by attention layers, while its use of information propagated by recurrent layers remains limited. To encourage better coordination between the two memory pathways, we add an auxiliary loss that limits attention's access to earlier context while the recurrent state propagates through the full sequence. This objective encourages the model to retain and use information through the recurrent pathway alongside attention. It improves overall performance, with particularly strong gains on tasks involving longer contexts or requiring information aggregation, consistent with the strengths of recurrent layers observed in analysis. Crucially, this imbalance and the benefit of our auxiliary loss generalize: they apply to multiple recurrent-attention LMs in question-answering and agentic tasks, as well as to attention-based LMs that combine different forms of memory. Together, our findings show that simply providing multiple memory pathways does not ensure their effective use, and that targeted supervision is needed to better coordinate them.

---


### 455. [MatrixFormer: A Foundation Model for Matrix Completion](https://arxiv.org/abs/2610.06751)

**<font color=#1a73e8>作者：</font>** Dwaipayan Saha, Jacob Feitelberg, Kyuseong Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix completion underlies problems from tabular imputation to causal inference, yet existing tabular foundation models treat it as entry-by-entry prediction, repeating context for every target and discarding the matrix's two-dimensional structure. We introduce MatrixFormer, a pre-trained matrix-native transformer that predicts a full distribution for every missing entry in a single forward pass. MatrixFormer is trained entirely on synthetic low-rank and latent-factor matrices under diverse missingness patterns. Applied zero-shot and with the same model weights, MatrixFormer achieves competitive performance on causal inference panel-data tasks, language-model benchmark-score completion, tabular imputation, and recommendation systems matrix completion. These results position MatrixFormer as a general-purpose foundation model for matrix completion.

---


### 456. [Conditional Rank Allocation for Taxonomy-Aware Medical Language Model Adaptation](https://arxiv.org/abs/2610.06765)

**<font color=#1a73e8>作者：</font>** Guangyuan Dong, Ziwei Hong, Xuehao Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical question answering spans specialties and clinical operations that may benefit from different adaptation directions. We propose ARBOR, a parameter-efficient method that selects rank-one components from a shared low-rank basis for each question. An additive gate combines question representations, specialty tags, operation tags, and their interaction; a learned coefficient scales the adapter residual. An illustrative separation under orthogonal, equiprobable subtasks shows how conditional selection can avoid an approximation floor faced by a fixed update with the same active rank. This result motivates the design without asserting a corresponding bound for medical corpora. On Qwen3-8B across CMB, CMExam, MedQA, and MedMCQA, five-seed experiments yield 69.69% mean accuracy across benchmarks, exceeding LoRA r16 and MoELoRA by 1.26 and 1.30 percentage points, respectively. The reported advantage over LoRA r16 increases from 0.08 to 1.94 points as training expands from one to seven specialties. Tag perturbations and atom masking support the usefulness of clinical routing, while atom clusters align with the supplied specialty labels (adjusted Rand index 0.62). Calibration, transfer, and measured costs further characterize the method. These findings support structured conditional adaptation for medical QA, while leaving clinical safety and broader deployment untested.

---


### 457. [T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search](https://arxiv.org/abs/2610.06782)

**<font color=#1a73e8>作者：</font>** Olga Tsymboi, Ramil Latypov, Aleksandr Medvedev 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present T-Search, an open-weight agentic retriever for hard multi-step search. Given a question and a search tool over a fixed corpus, it runs a bounded multi-round search and returns a ranked list of evidence chunks with short justifications, leaving answer generation to a downstream model, so backend and generator can be swapped without retraining. T-Search is built on Qwen3.6-35B-A3B and trained on adversarially filtered synthetic search tasks with round-sliced supervised fine-tuning followed by GSPO on a recall reward. Averaged over seven English and Russian benchmarks with gold evidence annotations, it reaches 56.0 Recall@10 with one rollout, 14.4 points above its base, and 61.3 with three fused rollouts, outperforming larger open models. We release the model, harness, live demo, and three benchmarks, including TRuST, the first native-Russian hard-search benchmark.

---


### 458. [Back to the Future: Rethinking EDA Infrastructure for Agentic Systems in Chip Design Verification](https://arxiv.org/abs/2610.06790)

**<font color=#1a73e8>作者：</font>** Je Yang, Ivan Lobov, Thomas Karpati  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The unprecedented computational scale of modern artificial intelligence depends on complex, multi-billion-transistor Systems-on-Chip, yet the workflows that verify these chips remain stubbornly manual. Although Large Language Models (LLMs) have made rapid inroads into Electronic Design Automation (EDA), approximately 74.6% of existing studies target static Register-Transfer Level (RTL) code generation, leaving post-simulation verification and interactive waveform debugging largely untouched. We introduce Back-to-the-Future (BTTF), an end-to-end agentic framework that closes this infrastructural gap. BTTF distills massive, unstructured simulation dumps into a normalized relational SQLite database and couples it with a collaborative multi-agent orchestration engine that translates natural-language verification queries into schema-aware SQL while correlating signal anomalies with versioned RTL repositories. Across a 150-query benchmark, BTTF attains 95.33% execution accuracy, charting a practical path toward autonomous EDA verification.

---


### 459. [Sharpen Without Search: On-Policy Distillation of Sequence-Level Power Distribution](https://arxiv.org/abs/2610.06804)

**<font color=#1a73e8>作者：</font>** Erfan Baghaei Potraghloo, Seyedarmin Azizi, Arya Fayyazi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A language model can give a correct answer more probability than any single incorrect answer and still usually sample an incorrect one, because the incorrect answers together hold more probability. The power distribution raises each complete answer's probability to a power above one and renormalizes, shifting probability toward answers the model finds most likely (sharpening). Sampling from it improves reasoning without changing parameters, but needs many scored candidates per query. We show that a model can instead be trained to produce such answers in one generation. On-policy power distillation (OPPD) runs a sequential Monte Carlo sampler in which the model being trained generates candidates and a frozen teacher's power distribution weights them; the same probabilities weight each answer in a maximum-likelihood update. Training raises single-generation accuracy by up to 23.0 points on MATH500 and 27.3 on GSM8K over the untrained model at the same temperature, and one generation scores 2.4 and 3.5 points above published power sampling with 64 candidates, recovering 94 percent of the gain that 16 candidates give the untrained model. For context, against GRPO trained with verified rewards from the same checkpoint and budget, OPPD scores 3.8, 4.0 and 5.4 points higher on MATH500, GSM8K and AIME using no reference answers; the two are complementary, and OPPD applied after GRPO adds up to 9.3 points. Trained only on mathematics, OPPD raises HumanEval accuracy by up to 5.3 points. One loss coefficient moves the sharpening exponent the model absorbs between 1.19 and 2.02, against 1.14 for ordinary on-policy distillation, and it rises mostly on the model's own answers. Gains hold across model families and sizes, including a model already trained with verified rewards, where lowering the temperature gives nothing and OPPD adds 4.4 points on MATH500. Code: this https URL.

---


### 460. [PlotGround: Grounding Plot Digitization in Real Scientific Figures and Their Source Data](https://arxiv.org/abs/2610.06825)

**<font color=#1a73e8>作者：</font>** Yaohui Zhang, Binxu Li, Haoyi Duan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific figures often encode quantitative results that are not readily available in machine-readable form, making accurate plot digitization important for verifying and reusing published findings. Yet it remains unclear how accurately current models recover plotted values from real scientific figures, as existing benchmarks rely largely on synthetic charts or cover only a limited range of chart types. We introduce PlotGround, an automated pipeline for building plot digitization benchmarks from real scientific figures and their author-released source data. PlotGround maps figures to source tables, identifies reconstructable panels, and generates quantitative questions with source-grounded reference values. We use PlotGround to construct PlotGround-1k, a human-verified benchmark of 1,119 questions from 1,066 bioRxiv preprints. Across sixteen multimodal models, the best reaches 87.5% accuracy at a $\pm 5\%$ relative-error tolerance. Tightening the tolerance to $\pm 2\%$ lowers every model's accuracy by 11-24 percentage points, revealing a gap between approximate visual reading and precise quantitative recovery. PlotGround's paired figure-source structure lets us compare how accurately the same values are recovered from figures and from source tables. Providing source tables instead of figures raises a coding agent's accuracy from 90.0% to 97.4% while cutting cost by 72%.

---


### 461. [CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling](https://arxiv.org/abs/2610.06829)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Yutong Dai, Viraj Prabhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for credit assignment, while frontier-language-model judges are too expensive to call at every step and cannot be assumed available at deployment. We introduce CLIFT, a training and test-time scaling method built around conformal self-verification. During training, the agent answers natural-language verification questions about its own rollouts; a Compositional Conformal Certifier keeps only question signals whose URL-conditional evidence agrees with a training-time judge, assigns signed trust weights through polarity-aware lift, and blends the resulting verifier score into per-step rewards in a way that never subtracts from the judge baseline. At test time, the same certified bank is frozen and reused as structured evidence for Conformal Trajectory Selection (CTS): the agent samples a greedy rollout and one or more diverse retries, the self-verifier summarises each URL trace, and a conservative majority-vote rule chooses whether to swap away from the current incumbent without calling any external judge. This single mechanism supports three settings. On WebArena Infinity, CLIFT achieves state-of-the-art performance among open-source web agents. On VisualWebArena, a bank trained with the open model transfers to GPT-5.5 at test time and reaches state-of-the-art performance under the canonical harness. On Online Mind2Web, without training an agent on the benchmark, translating the certified question bank improves a live-web agent in zero-shot evaluation. Together these results position conformal self-verification as a way to turn costly judge feedback into a reusable training signal and a judge-free test-time scaling signal.

---


### 462. [MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents](https://arxiv.org/abs/2610.06830)

**<font color=#1a73e8>作者：</font>** Haozhen Zhang, Haodong Yue, Quanyu Long 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential. Recent studies have begun shifting memory processing toward runtime adaptation, but typically specialize in particular operations or fixed processing schemes, leaving flexible control over performance, cost, and latency largely underexplored. To address this challenge, we present \textbf{MemPilot}, a flexible framework that orchestrates on-demand memory curation under different performance--cost--latency preferences. Specifically, we optimize a multi-step LLM policy via reinforcement learning to iteratively choose between retrieving from query-agnostic memory and delegating query-specific curation of raw multimodal history to heterogeneous LLMs and VLMs. The policy jointly controls evidence amount, curation instructions, model selection, and visual access, enabling fine-grained allocation of runtime computation. To optimize this policy under competing objectives, we adapt objective-wise advantage decoupling by separately estimating each objective's advantage before aggregation. Moreover, we introduce prefix-based marginal utility estimation for fine-grained credit assignment across multi-step rollouts. Experiments on five multimodal agent-memory benchmarks demonstrate favorable performance--cost--latency trade-offs across optimization preferences, with preference sweeps yielding broader frontiers than existing trade-off-aware baselines.

---


### 463. [Towards Looped Models Done Right, Part II: Rethinking at Fixed Points](https://arxiv.org/abs/2610.06833)

**<font color=#1a73e8>作者：</font>** Benhao Huang, Chufan Shi, Junlin Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every recurrence of a looped language model adds cost in training, decoding, prefill, and reinforcement learning (RL). The closer recurrent states get to fixed points, the less the path to them matters. This enables truncated backpropagation in training; terminal key-value (KV) sharing for decoding with almost no loss in accuracy; a distilled student that prefills up to 1.79x faster; and RL updates that compute gradients from saved rollout states, 2x faster than backpropagating through the replayed trajectory. We therefore improve the two components of training that shape these fixed points: the depth prior and input injection. Fixed-depth training breaks KV sharing, and Huginn's broad depth prior supports sharing but dilutes supervision at the target depth more than sharing requires; we learn the prior from prediction feedback, with an entropy term that keeps it broad. Existing injection schemes let the state's component along the input amplify or cancel the injection; we remove this component with orthogonal injection. From 100M to 1.6B parameters, the learned prior and orthogonal injection lower perplexity at every scale relative to Huginn's prior and existing injection schemes, respectively. At 1.6B, the learned prior with a 3x smaller KV cache matches the downstream average of fixed-depth training with the full cache.

---


### 464. [Learning to Read the Contextual Tokens in Diffusion Transformers](https://arxiv.org/abs/2610.06844)

**<font color=#1a73e8>作者：</font>** Omer Dahary, Etai Sella, Hadar Averbuch-Elor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Diffusion Transformers (MM-DiTs) jointly process visual and textual representations throughout generation. These models repeatedly update the text tokens through multimodal attention, forming dynamic contextual tokens whose function is not well understood. In this work, we introduce a framework for reading this contextual space through natural-language interrogation. We train a lightweight bottleneck network that maps intermediate contextual tokens into the input space of a frozen Large Language Model (LLM), allowing the LLM to answer questions about the emerging image directly from these hidden representations. Our reader reveals that contextual tokens encode a rich, global representation of the emerging scene: generation-specific semantics, including attributes left underspecified by the prompt, are accessible surprisingly early in denoising, while increasingly fine-grained details become readable over time. Remarkably, this information remains decodable even when the MM-DiT receives an empty prompt, showing that contextual tokens accumulate substantial image-specific information from the evolving visual representation itself. We further find that generations with more readable contextual representations tend to receive higher human-preference scores. Building on these observations, we introduce Contextual Alignment, a training technique that explicitly reinforces the visual-semantic information encoded in the contextual tokens, improving generation quality and distributional coverage. Together, our results establish contextual tokens as both an interpretable view into the internal dynamics of MM-DiTs and an effective target for improving generative models.

---


### 465. [TranScope: What the Software Hides About LLM Training Data, the Hardware Reveals at Scale, and Accelerators Magnify](https://arxiv.org/abs/2610.06848)

**<font color=#1a73e8>作者：</font>** Joshua Kalyanapu, Darsh Asher, Kaushal Mhapsekar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Membership is the root privacy primitive in machine learning: to date, no hardware-based out-of-distribution detection on black-box models has been demonstrated against constant-time, static neural networks with masked confidence. This paper performs the first cycle-level examination of how large language models and vision transformers interact with various modern microarchitecture components, including integrated accelerators, as LLMs scale in size and answers the question of whether the data that a model was trained on affects its execution footprint even without any input-dependent branch, dynamic optimization, or early exit and in constant-time models. The results confirm that the answer is yes and identify which modern hardware components, such as TLBs or on-core accelerators, reveal or amplify that effect. The results also answer whether the signal is informative enough to reliably classify the in-/vs/out-of-distribution property of membership. To understand why, we perform a systematic root cause analysis and find that the transformer's tokenization steps, which happen during training, alter the locality of the accesses the model makes to fetch the vocabulary token later during inference and, as a result, change the page table access patterns and TLB in a previously unknown data-dependent way, causing microarchitectural state to vary significantly based on whether or not the input was in the distribution of the transformer training data. Building on the above observation, we introduce TranScope: the first microarchitecture tool for detecting membership information with low cost, no need for a surrogate model, and significantly higher robustness, e.g., 0.6 AUC for PETAL (best previously reported) vs 0.9 AUC (ours). This reintroduces hardware as both an opportunity, e.g., a tool for checking copyright violation for the first time, and a new channel for inferring membership (MIA).

---


### 466. [Base Models Can Reason By Taking a Cue From Training Data](https://arxiv.org/abs/2610.06851)

**<font color=#1a73e8>作者：</font>** Sophie L. Wang, Amil Dravid, Rulin Shao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study how training data creates associations between the tokens at the start of a base model's response and the reasoning behavior that follows. First, we demonstrate that fixing particular starting token cues makes a base model's performance competitive with that of its reinforcement learning (RL)-trained counterparts on math and coding. For instance, the cue ".\n\nOkay" raises Olmo-3-7B's MATH-500 pass@1 accuracy from 42% to 78%, while "Alright," raises Qwen3-14B's from 72% to 87%. Second, RL makes these cues more likely, while fixing them recovers much of its performance gain over the base model. Third, we trace the reasoning effects of token cues to the training data. We perform causal data interventions to turn an arbitrary word, such as "chicken", into an effective reasoning cue, or remove an existing cue's effect. A similar edit makes the prompt instruction "Think duck duck goose" as effective as "Think step by step" at eliciting reasoning. We also find that the hidden state representations induced by different cues correlate with different document types from the training set. Finally, we extend our study of token cues with a case study in language model safety, finding that different cues elicit distinct refusal and compliance behaviors that correspond to different types of training data.

---


### 467. [One Figure, Every Canvas: Editable Flowchart Relayout via Agentic Pipeline](https://arxiv.org/abs/2610.06852)

**<font color=#1a73e8>作者：</font>** Shih-Chen Tseng, Chih-Hsuan Chen, Ryan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pipeline figures in ML papers must be repurposed across many canvases, including paper columns, 16:9 slides, portrait posters, 1:1 social teasers, 9:16 phone previews. Each format imposes a different aspect ratio on the same computational graph, where any silently broken connection misrepresents the method. We formulate aspect-ratio-adaptive flowchart relayout as a distinct task: given a raster flowchart and a target ratio, produce a structurally faithful, hallucination-free, editable layout. Existing methods fail characteristically: image-to-image models stretch blocks and reject extreme ratios, text-to-image agentic systems hallucinate content, and parse-then-render systems mis-route edges. We propose an agentic pipeline factored into Parse, Style, and Layout stages, each pairing a main agent with a critic that combines deterministic constraint checks with VLM visual feedback so connectivity is explicitly checked and prevented from being silently broken. Outputs are this http URL-editable mxGraph XML. On a curated benchmark of 100 flowcharts at five aspect ratios, evaluated by Gemini 3.1 Pro and validated against human judgments, our method reaches 68.6% Content Fidelity versus 11.2-41.4% for prior work. Project page: this https URL

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 468. [Reinforcement Learning on the Discrete Composition Channel of a Crystal Generator: Validated Gains and Reward Hacking](https://arxiv.org/abs/2610.03880)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pawan Prakash, Philipp Höllmer, Addis Fuhr 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse materials design is a long-standing goal of computational materials discovery. Generative models for crystalline materials are typically trained to match the distribution of a structure database, while nothing in their training objective points them at specific design goals such as targeted properties. We use group-relative policy optimization (GRPO) to align a generative model based on stochastic interpolants and discrete flow matching with general black-box reward functions through reinforcement learning. Atom types are generated by a discrete flow and the policy gradient of our generalization of GRPO directly acts on the likelihoods of the atom-type transitions, which differentiates our work from previous reinforcement-learning approaches for diffusion and flow-based generative models of crystalline materials. We introduce a reward function that raises the yield of metastable, unique and novel structures (mSUN) from 13.4% for the pretrained model to 45.5% for the reinforced model, as evaluated by a community benchmark. Our reward also improves the performance of a reinforcement learning framework for crystalline materials based on latent denoising diffusion models. At the same time, we find that directly reinforcing atom-type transition likelihoods enables reward exploitation that has to be prevented with explicit guards. The same analysis also exposes a gap in the community metric. Single-element structures in distinct packings are counted as metastable, unique and novel materials and inflate mSUN without yielding any new compounds. A stability claim is only as good as its reference hull. We report every result split by the number of reference phases behind it and argue that benchmarks should do the same.

---


### 469. [DUET: Co-Evolving Solver and Grader Agents](https://arxiv.org/abs/2610.04087)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fengyu Gao, Sourav Pal, Austin Z. Henley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic workflows are increasingly used across domains such as technology, finance, and enterprise operations. As these agents become more widely deployed, continually improving them becomes increasingly important. This raises an immediate challenge: How should the agent evolve? This evolution requires effective evaluation that can assess outcomes and provide useful feedback for optimization. As the agent evolves, its behaviors and failure modes may also change, making a fixed evaluator increasingly inadequate. Another fundamental question: How should we evaluate an evolving agent? These two challenges are inherently coupled; changes in agent behavior can expose limitations of the current evaluator, while a stronger evaluator provides more informative feedback for improving the agent. Motivated by this interaction, we introduce DUET, a framework that jointly optimizes a solver agent and a grader agent to improve both. DUET iteratively selects training tasks, executes them with the solver, evaluates the resulting outcomes with the grader, and uses a tool-using update module to revise the solver and the grader, alternating between the two across rounds. By updating the grader within the optimization loop, DUET turns evaluation from a fixed source of feedback into a first-class optimization objective that adapts alongside the solver. Experiments across four agent benchmarks show that DUET improves both solver and grader performance and consistently outperforms baselines that optimize the solver with a fixed grader.

---


### 470. [MOIRA: Mass-Oriented Indexing with Ragged Attention for Long-Context Decoding](https://arxiv.org/abs/2610.04313)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dich Nhat Minh Nguyen, Tran Dang Duong Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context decoding is limited by memory bandwidth, because every output token reads the KV cache of every layer. Sparse decoding reduces this cost by reading only part of the KV cache. We observe that the number of pages a query needs varies widely across KV heads, layers and steps. Fixed budgets are simple, but they are sized for demanding cases and tuned per workload; adaptive budgets follow this variation more flexibly, but existing designs pay for it with extra selection cost or training. At the kernel level, FlashAttention-3 (FA3) and FlashInfer are designed for rows of similar length: with page lists whose length differs per KV head, they either pad the lists (forfeiting much of the sparse saving), leave thread blocks unbalanced, or rely on a host-side plan that runs outside the CUDA graph. We propose MOIRA, a training-free sparse decode path in vLLM whose budget adapts per KV head and per layer. For every request, layer, KV head and step, a coverage rule keeps the smallest set of pages whose estimated attention mass reaches a fraction $\gamma$. A new kernel, self-planning attention, lets each thread block derive its own share of the work from the list lengths, so the whole decode step stays inside the CUDA graph. On an H200, at RULER's 128k context, MOIRA with $\gamma=0.99$ matches dense accuracy while reading about 30% of the pages and reduces the time per output token (TPOT) by 2.2-2.5$\times$ relative to dense FA3; with $\gamma=0.98$ it reduces TPOT by 2.7$\times$ and stays within the noise of dense. Under high serving load it raises throughput by up to 51%. These results suggest that a budget adapted per head and layer, paired with a kernel that keeps such budgets inside the CUDA graph, makes sparse decoding both flexible and fast.

---


### 471. [TimeNet: An Extensible Unified Data Infrastructure for Next-Generation Temporal Foundation Models](https://arxiv.org/abs/2610.04407)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Martin Maritsch, Timo Stoffregen, Thomas Kaar 等 39 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal Foundation Models (TFMs) aim to generalize across domains, datasets, and tasks. Yet, their development remains constrained by fragmented, task-specific data formats, annotations, and processing pipelines. We introduce TimeNet, an open-source data standard and scalable infrastructure that decouples temporal data from task definitions and represents signals, metadata, annotations, and supervision in a shared, extensible data model. TimeNet supports multimodal signals with regular, irregular, or ordinal time axes and expresses different task families (including classification, forecasting, temporal localization, question answering, generation, and editing) as reusable views over the same recordings. This shared representation enables heterogeneous time-series datasets to be combined for large-scale model training across domains, modalities, and tasks. We demonstrate TimeNet by transcoding datasets with 1.5M task instances spanning diverse domains, modalities, temporal scales, and forms of supervision, while retaining practical I/O performance relative to native formats. TimeNet enables an existing TFN training pipeline to support joint training on a configurable number of heterogeneous datasets through configuration changes alone. We show this capability by training TFM across multiple datasets and tasks, obtaining a 14% F1 score improvement compared with models trained on individual datasets. These results show that TimeNet provides the data and systems foundation needed to move beyond task- and dataset-specific TFMs toward models that can learn jointly across heterogeneous domains, modalities, temporal scales, and forms of supervision from a common data model.

---


### 472. [COSMOS: Soft Mechanism Mixtures with Verifiable Routing for Long-Horizon PDE Forecasting](https://arxiv.org/abs/2610.04427)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Anupam Rawat, Manikandan Padmanaban, Jagabondhu Hazra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators offer an efficient alternative to classical PDE solvers, but most learn a monolithic map per equation family and discretization. Real systems are compositional: transport, diffusion, wave, and reaction processes can act simultaneously. Existing mixture-of-experts operators typically use sparse top-$K$ routing, although concurrent physics is naturally a blend rather than a discrete choice.
We propose COSMOS (Cooperative Operator Specialists with Mechanism-level Operator Soft-routing), a soft mechanism-mixture neural operator. Four process-biased specialists remain active at every step and are continuously mixed by a learned gate, with their features fused by a small network. Specialists share a coarse latent grid, while a zero-initialized full-resolution residual restores detail lost through the bottleneck. We also introduce an operator-splitting compositional benchmark with known mixture weights $w^\star$ per trajectory.
Against family-tuned FNO under 20-step rollouts, an initial 3-seed evaluation suggested gains on diffusion--reaction, parity on Navier--Stokes, and weaker shallow-water performance. An 11-seed audit showed that the diffusion--reaction gain was unstable, motivating caution in small-seed rollout comparisons and precluding a reliable accuracy-win claim on these families. Ablations show that uniform routing or removing the specialist mixture substantially degrades stable-regime rollouts. On the labeled benchmark, dense soft routing yields $2.2\times$ lower error than hard top-1 routing at identical fusion; using generator weights $w^\star$ at inference further lowers rollout error to $0.034$, diagnosing limitations of the learned gate. However, routing labels do not align with the specialists' intended mechanisms: COSMOS supports compositional accuracy, not mechanism identity.

---


### 473. [Target-free Latent Safety Alignment](https://arxiv.org/abs/2610.04467)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Luoyu Chen, Weiqi Wang, Chenhan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) remain highly vulnerable to jailbreak attacks that induce harmful behaviors and circumvent safety alignment. To defend against such attacks, adversarial training paradigms have been proposed to first simulate failure modes and then train the model to correct them, yielding promising improvements in safety alignment. However, these methods typically construct adversarial samples either by encouraging fixed harmful target completions or by performing targeted activation ablation derived from fixed benign--harmful data pairs. As a result, the generated adversarial samples tend to induce homogeneous harmful behaviors that poorly reflect the diversity of behaviors elicited by real-world jailbreak attacks. This behavior-level narrowness fundamentally limits their robustness. To address this issue, we propose a target-free adversarial training framework that generates adversarial samples in an unsupervised manner. By amplifying and diversifying behavior-level shifts in the model's latent space, our approach produces semantically diverse adversarial samples that induce a wide range of harmful behaviors. This expanded behavioral coverage exposes more diverse failure modes and thereby improves safety alignment. To quantify this effect, we use semantic entropy as an output-level measure of adversarial behavioral diversity. Empirically, our method elicits diverse harmful behaviors in the target model, substantially mitigating behavioral narrowness and improving robustness to jailbreak attacks.

---


### 474. [Localized Operator Learning with Adaptive Partition-of-Unity Mixture-of-Expert Networks](https://arxiv.org/abs/2610.04708)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Madison Cooley, Ramansh Sharma, Shandian Zhe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operator learning methods such as DeepONets and FNOs often struggle with PDE families featuring sharp interfaces, heterogeneous coefficients, and localized multiscale structures. We introduce a partition-of-unity (POU) mixture-of-experts framework for localized operator learning, in which geometry-aware gating networks produce smooth spatial partitions which blend the contributions of local expert networks. Our main contribution is HiRefPOU, a residual-style hierarchical POU architecture for DeepONets that organizes localized representations through nested parent-child partitions while preserving global continuity. We also show that the same POU principle can be incorporated into Fourier Neural Operators to introduce spatial adaptivity without modifying the underlying spectral layers. On heterogeneous Darcy and reaction-diffusion benchmarks, HiRefPOU achieves substantially lower error than global DeepONet and static POU-MoE baselines, while the broader operator-learning experiments show that the benefits of localization depend on the PDE structure and the chosen neural-operator backbone. The learned partitions are interpretable and align with interfaces and regions of rapid solution variation. These results show that explicit geometric localization can improve both accuracy and interpretability in neural operator learning.

---


### 475. [GRAM: Correcting Frozen Time-Series Foundation Models via Graph-Retrieved Amplitude Memory](https://arxiv.org/abs/2610.04827)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaoyun Yu, Xiangfei Qiu, Yonggui Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models (TSFMs) enable zero-shot forecasting through large-scale cross-domain pretraining, while retrieval augmentation further improves their performance by leveraging historical information. However, existing methods typically correct TSFM forecasts using the ground-truth futures of similar historical windows, which contain both predictive components already captured by the foundation model and sample-specific random fluctuation that is difficult to transfer. In contrast, recurring systematic model bias within prediction errors more directly characterizes the failure modes of a frozen TSFM and therefore provides more valuable correction signals. Effectively exploiting such model bias, however, poses two challenges: prediction errors at different numerical levels are difficult to compare due to scale differences, and the recurring bias must be extracted from prediction errors contaminated by random fluctuation. To address these challenges, we propose GRAM, a general retrieval-augmented framework for frozen TSFMs. GRAM first introduces an Amplitude Memory Module (AMM) that scales prediction errors by amplitude and aggregates them into retrievable prototypes. It then employs a Prototype Graph Module (PGM) to model relations among prototypes to aggregate consistent bias information while suppressing random fluctuation. During online forecasting, GRAM retrieves and expands prototypes relevant to the current query and generates per-horizon corrections to refine the original TSFM forecast. Experiments across multiple datasets and foundation models demonstrate consistent forecasting improvements.

---


### 476. [PWM: Personalized World Models with Online Reinforcement Learning](https://arxiv.org/abs/2610.04920)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhexin Lou, Guancheng Lu, Zeyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained world models can generate diverse environments, yet users often want to explore a particular scene specified by their own video. This requires learning the scene's visual identity while retaining the quality of action-conditioned generation. We introduce Personalized World Models (PWM), a framework for customizing interactive world models from short scene videos through online reinforcement learning. In PWM, the support trajectory and its associated controls provide reward feedback on continuations sampled from the current policy. In the GRPO instantiation, group-relative optimization updates a compact LoRA adapter using a unified reward for scene appearance, visual continuity, and motion, while base-policy anchoring regularizes changes to the pretrained generation prior of a frozen Yume-5B backbone. The same adaptation procedure is applied across real and rendered environments. We also instantiate PWM with DiffusionNFT as an alternative reward-guided optimization method for learning the scene-specific adapter. We also introduce PWM-Bench, comprising 150 customization tasks across Indoor, Outdoor, and Gaming, with paired evaluation on held-out continuations. The GRPO and DiffusionNFT instantiations of PWM improve customization over native Yume in 71.3% and 65.3% of the evaluated scenes, respectively, with positive mean gains across all three domains. For the GRPO instantiation, matched SFT comparisons further demonstrate higher mean customization gains and better mean image-quality scores in every domain, while retaining frame-level visual quality close to the pretrained model.

---


### 477. [Hidden Risks of Jev: An Empirical Study of Security, Privacy, and Dual Use](https://arxiv.org/abs/2610.04985)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shang Wang, Tianqing Zhu, Huajie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jev turns natural-language questions into typed answers and probabilities with low latency and cost, enabling applications to route requests and select tools. While this interface allows Jev to integrate naturally into application workflows as a decision layer, the security and privacy implications of this emerging use remain largely unexplored. To address this gap, we conduct the first systematic study of these implications using the official Jev API and NanoJev, a local model with controllable training data and updates, focusing on three research questions: (1) What security threats arise when Jev is deployed as an application decision layer? (2) What private information can Jev reveal despite returning constrained typed outputs? (3) How can Jev's general-purpose decision capability be used for beneficial purposes or misused?
Jev's decisions depend on application state and may be influenced by user-provided inputs. We therefore adapt prompt injection and adversarial suffixes to manipulate its decisions. Open-source Jev distribution and updates introduce supply-chain risks, which we examine by implanting backdoors in NanoJev through training data poisoning. Since Jev's outputs reflect both application state and information learned during training, we further adapt membership, private attribute, and internal knowledge inference attacks to recover sensitive information despite its constrained output format. Finally, Jev can serve as a general-purpose decision oracle for defensive and malicious workflows. We examine this dual use through four detection tasks covering prompt injection, jailbreak inputs, harmful content, and AI-generated text, alongside misuse scenarios involving jailbreak and model extraction. Our empirical evaluation shows that Jev remains vulnerable to the examined security and privacy threats, while its decision capability can support beneficial and malicious uses.

---


### 478. [Long-MDR: Long-Context Reinforcement Learning for Multimodal Deep-Research Agents](https://arxiv.org/abs/2610.05195)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** On Tai Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The next generation of multimodal research agents must reason over long-lived research histories rather than short model completions. During a single task, an agent may repeatedly search the web, inspect visual evidence, revisit earlier hypotheses, and accumulate tens of thousands of tokens of multimodal context. Despite this trend, online RL for multimodal research agents remains largely confined to shorter contexts and interaction horizons. We push online RL training to 128k context and 75+ tool-interaction turns. To our knowledge, this is the first online multimodal deep-research RL study trained at 128k context, and the first trained with a 75 tool-turn horizon. Scaling to this regime exposes several practical limitations of conventional RL training. Early in training, weak policies make poor use of large interaction budgets, causing expensive rollouts with little reward improvement. Later, policy entropy can collapse before performance has saturated, prematurely ending useful learning. We introduce Long-MDR, a three-component training recipe designed specifically for this setting: On-Policy Distillation Warmup, Progressive Horizon Expansion, and Entropy-Triggered Rescue. Together, these techniques improve both the learning efficiency and stability of long-horizon RL, enabling continued gains in a regime where direct training is slow and costly. At a 50-turn evaluation budget, our RL-trained Long-MDR-9B ranks first on five of six benchmarks among the compared 7B-9B agents.

---


### 479. [A Unified Scaling Law for Time Series Foundation Models](https://arxiv.org/abs/2610.05269)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xilin Dai, Yiding Liu, Zewei Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a Unified Scaling Law and a Unified Theory of Time Series Learning to understand how model capacity and historical information support forecasting. Across different lookback lengths and forecast horizons, we analyze 18,768 experimental cells from 21 checkpoints on 23 dataset-frequency tasks spanning six domains. Our empirical methodology integrates local resource relations into a parsimonious, fitted five-parameter law: capacity gains increase with history, context gains diminish toward saturation, and horizon effects enter as a common shift. Fitted without Toto 2.0, the law predicts its horizon-averaged capacity-scaling curves with mean absolute percentage errors of 1.09% and 1.50% at input lengths 2048 and 4096. To understand how history supports prediction, our learning theory uses Gaussian regression to analyze rule identification and predictive capability. We hypothesize that full-shot models learn by accumulating information in weights, while frozen time series foundation models (TSFMs) use history by extracting information through activations. Matched-history comparisons establish the predictive value of additional history. Controlled parameter exchanges and activation interventions provide evidence that history-derived rule information can be retained, reused across queries, and used to recover a contribution to long-context prediction. Together, these findings inform capacity scaling, context allocation, and the development of models that retain and apply historical rules. Code and main results are available at this https URL.

---


### 480. [Readable Before Actionable: Causal Tracing of Indirect Prompt Injection](https://arxiv.org/abs/2610.05295)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhe Yu, Wenpeng Xing, Xingxing Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection causes LLM agents to follow commands embedded in external data. A probe may distinguish instructions from data without identifying a state edit that changes the next action. We study this gap through counterfactual role probes, component-wise activation patching, and separate interventions on AgentDojo trajectories. Role decoding survives changes in content and format. In controlled Qwen tests, it precedes strong tool-choice effects from patches along an independently estimated role direction. On AgentDojo, directions estimated from hijacked and resisted training trajectories reduce attack success at pre-action and injected-span positions, but have little effect at random positions. In longer Qwen trajectories, single-position edits become less effective at later layers; span-wide and repeated edits reduce attack success on the same evaluation set. Removing the learned channel subspace preserves role decoding, yet effective intervention directions transfer poorly across the tested channels. These findings distinguish a readable role signal from an effective behavioral intervention: depth matters in controlled tool choice, while position and context also matter in attack trajectories.

---


### 481. [Task Inference Beyond Least Squares in Behavioral Foundation Models](https://arxiv.org/abs/2610.05350)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kuan-Hsun Tu, Chien-Sheng Chiang, Hsin-Wei Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavioral Foundation Models (BFMs) aim to solve a wide range of downstream tasks without test-time policy learning by inferring a task vector from the reward function. While efficient, the retrieved policies are often suboptimal because of how this task vector is inferred, typically with ordinary least squares (OLS). OLS minimizes reward reconstruction error but leaves the ordering of rewards unconstrained, which can bias the successor measure of the retrieved zero-shot policy away from that of the optimal policy. In this work, we propose BLS, an efficient test-time inference method that balances minimizing reward reconstruction error with reducing successor-measure mismatch. Theoretically, we provide a suboptimality gap upper bound characterized by both successor-measure and reward-function residuals. Empirically, we evaluate BLS on top of state-of-the-art BFMs across benchmarks for locomotion, manipulation, and humanoid control. BLS outperforms existing task inference baselines with negligible computational overhead. Project page: this https URL

---


### 482. [Rethinking Tabular Foundation Models On Data Streams](https://arxiv.org/abs/2610.05352)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nilesh Verma, Daniel Nowak-Assis, Afonso Lourenço 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) outperform established machine learning models on tabular benchmarks through in-context learning. Building on this success, interest is growing in applying them to data streams, where data arrive continuously and evolve over time. On a stream, a TFM adapts by updating its context rather than its parameters, so its accuracy and cost depend on which examples it keeps and how often it rebuilds its context. We therefore present a systematic study of TFMs on data streams, covering memory management, computational cost, and stream-specific challenges such as concept drift and delayed labels. We find that TFMs achieve the highest predictive performance and that simply retaining the most recent examples is as effective as existing memory management techniques. They also recover faster than streaming learners after drift and keep the highest accuracy under label delay. This accuracy, however, comes at a high serving cost, since a nearly unchanged context is re-encoded at every prediction. These results point to architectural efficiency as the way forward for in-context stream learning.

---


### 483. [Universal Test-Time Training](https://arxiv.org/abs/2610.05484)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zefan Cai, Qinzhe Hu, Ziqiao Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent Test-Time Training (TTT) architectures compress context into fast weights that are updated online and queried as memory. Existing TTT designs keep this memory private to each layer: it recurs only over time, and depth merely indexes L separate memories. We argue that memory ownership need not be tied to depth, and introduce Universal Test-Time Training (uTTT), in which all layers read and write one shared memory while retaining layer-specific backbone parameters. The shared memory thus recurs over two dimensions, time and depth, with chunks and layers as their units: a write by a deep layer in one chunk can be read by a shallow layer in the next. We instantiate this idea as uTTT-MoE and uTTT-Dense. uTTT-MoE routes each token head to a few experts in a pool shared by all layers; uTTT-Dense applies the whole shared memory at every layer without routing. In language modeling, uTTT-MoE reaches 15.5 and 27.9 RULER accuracy at 124M and 760M, 2.6 and 2.1 points above its layer-private counterpart at equal state and active compute, the highest among tested bounded-state models, with per-token loss matching or beating full attention. In novel view synthesis, sharing at fixed per-layer compute gains 0.92 dB in view-23 object PSNR in routed models and 0.76 dB in dense models.

---


### 484. [Lightweight Semantic EEG Foundation Model for Frozen Cross-Disorder Transfer](https://arxiv.org/abs/2610.05503)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rita Huan-Ting Peng, Nhat Bui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale EEG foundation models have demonstrated promising transferability across neurological disorders, but often require millions of parameters and substantial computational resources. In this paper, we present the Universal Semantic EEG Foundation Model (USE-FM), a lightweight EEG foundation model that learns transferable neural representations through self-supervised signal reconstruction on the Temple University Hospital EEG Corpus (TUEG). After pretraining, the encoder is frozen and evaluated on two clinically distinct downstream tasks, abnormal EEG detection (TUAB) and epileptic seizure recognition (TUEP), using a unified frozen-transfer protocol against recent EEG foundation models, including LUNA-Base and CBraMod. With only 1.46 million parameters, approximately one-fifth the size of existing models, USE-FM achieves competitive overall performance, including strong sensitivity and F1-score on TUEP (SEN $75.00 \pm 14.14$, F1 $70.37 \pm 4.01$), while maintaining competitive performance on TUAB (AUC $85.24 \pm 5.61$). Beyond downstream classification, latent representation analysis using $k$-means clustering together with PCA and t-SNE demonstrates that USE-FM learns organized semantic EEG representations comparable to substantially larger foundation models. These results suggest that large-scale self-supervised pretraining enables lightweight architectures to learn transferable semantic EEG representations, providing a computationally efficient foundation for cross-disorder analysis and future clinical decision support in neurological disorders.

---


### 485. [What Does an Observability Foundation Model Know?](https://arxiv.org/abs/2610.05577)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dhyey Dharmendrakumar Mavani, Rian Atri, Tairan Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A linear probe can show that a label is recoverable from a model's hidden states, but not whether that goes beyond what the input already reveals, or whether the model uses it. We audit Toto, an observability forecasting foundation model, on the Benchmark of Observability Metrics (BOOM) across five series-disjoint resplits, comparing linear probes on its frozen residual stream with models that read the raw input window and with Toto's architecture stripped of its trained configuration. Short-vs-medium cadence and metric type are more linearly recoverable from Toto's residuals than from the strongest raw-window model in every resplit (macro-F1 0.766 vs. 0.633 and 0.545 vs. 0.498). Domain is nearly tied, and series cardinality is recovered far better from the raw window. MOMENT-base shows related cadence, metric-type, and domain readouts. Recoverability is not use: exchanging Toto's residuals with those of high-burst donors moves a future-burstiness readout as intended but does not make forecasts consistently burstier than a randomized donor. A BOOM-trained coordination probe has negative zero-shot R^2 on the tested external benchmarks. We report each label against its strongest baseline.

---


### 486. [EchoDino: A pediatric foundation model for transferable echocardiographic analysis across the lifespan](https://arxiv.org/abs/2610.05603)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sheng Cheng, Donnchadh M. O'Sullivan, Daniel J. Penny 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Echocardiography is the most widely used cardiac imaging modality, yet interpretation demands integrating visual evidence across global anatomy, localized structures and dynamic cardiac motion. Machine-learning models have automated individual tasks, but they are typically built for a single purpose and depend on expensively labeled datasets - a barrier particularly acute in pediatric care, where data are scarce and anatomy changes with age. Here we present EchoDino, a self-supervised foundation model for echocardiography, created by adapting the DINOv3 framework to 3.7 million frames from 1.7 million unlabeled pediatric echocardiography videos. With its encoder frozen, EchoDino produces representations that capture global context, local anatomy, and dense spatial detail. We introduce Motion-biased Entropy Maximization Sampling (MEMS) to select the most informative frames for video-level analysis. Across nine pediatric and adult datasets, EchoDino outperformed strong baseline models, raising view-classification accuracy from 0.609 to 0.889 and the area under the receiver operating characteristic curve for structural-heart-disease detection from 0.811 to 0.872, while also cutting age-estimation error from 3.857 to 1.389 years, achieving the best segmentation accuracy and lowering ejection-fraction errors. By generalizing from label-free pediatric data to adult echocardiography, EchoDino offers a versatile foundation for cardiac image analysis across the lifespan.

---


### 487. [Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation](https://arxiv.org/abs/2610.05608)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Team Kandinsky, Julia Agafonova, Bulat Akhmatov 等 88 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Kandinsky 6.0 Video, a family of foundation diffusion models for synchronized text-to-audio-video generation, comprising Kandinsky 6.0 Video Lite (3B parameters) and Kandinsky 6.0 Video Pro (29B parameters). Both models generate 5-second video clips with synchronized 44 kHz audio, including lip-sync, in text-to-audio-video (T2AV) and image-to-audio-video (I2AV) modes; a built-in super-resolution model raises the output resolution to Full-HD (1920$\times$1080). Building on the video generation capabilities of Kandinsky 5.0, Kandinsky 6.0 Video employs a dual-stream CrossDiT architecture that connects a pretrained video stream and a newly trained audio stream through bidirectional cross-attention for temporal and semantic alignment. Our continuous pretraining strategy first trains the audio stream from scratch on large-scale audio corpora and then trains both streams jointly on paired audio-video data while preserving unimodal fidelity; pretraining is followed by supervised fine-tuning, reinforcement-learning-based post-training, and distillation. In side-by-side human evaluation, Kandinsky 6.0 Video Pro clearly outperforms its predecessor, Kandinsky 5.0 Video Pro, and remains competitive with leading audio-video generation models, particularly in speech quality. To accelerate open research and deployment in multimedia generation, we release the code, model checkpoints, and diffusers integration under the MIT license.

---


### 488. [Training and Scaling Compute-Optimal Physiological Waveform Foundation Models](https://arxiv.org/abs/2610.05649)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pingzhi Li, Jie Peng, Shuqing Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the scaling laws and compute-optimal training of physiological waveform foundation models (FMs). We train Aether, a family of over one hundred FMs ranging from 20M to 2.1B parameters, on up to 36.3M hours of physiological waveforms. We construct eight clinical prediction tasks from MIMIC-III and evaluate the FMs through linear probing. The 720M FM outperforms all existing baseline FMs across all eight tasks. A scaling law of model size, pretraining hours, and labeled patients predicts downstream ranking error, i.e. $1-\mathrm{AUROC}$, effectively with $0.5\%$ prediction MAE at held-out resource scales and $0.9\%$ MAE when extrapolating to 2.1B parameters. We present three findings: (1) Compute-optimal training scales both FM size and pretraining hours. Under the fitted law, a $10.0\times$ increase in compute FLOPs scales model size by $1.2\times$ and pretraining hours by $8.2\times$. (2) Larger FMs use waveform data more efficiently, and greater pretraining exposure increases the benefit of model scaling. Starting from 25M parameters and 4.8M pretraining hours, doubling FM size reduces the predicted hours needed for the same performance by $51.8\%$. (3) Pretraining and clinical supervision reinforce each other: more labeled patients increase the return to pretraining, while larger FMs and longer pretraining reduce labeling requirements. For the example of the 720M FM, extending pretraining from 120K to 36.3M hours reduces the predicted patient requirement by $61\%$ at a target ranking error. These findings provide a quantitative training recipe and a promising and durable scaling path for physiological waveform modeling and downstream clinical prediction.

---


### 489. [Planetary Geospatial Foundation Models: A New Paradigm for Global Public Health](https://arxiv.org/abs/2610.05699)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Arbaaz Muslim, Aviv Slobodkin, Katherine Wheeler-Martin 等 38 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The efficacy of traditional disease prediction is limited by spatial gaps and temporal lags, which impact the timing and targets of resource deployments. Outbreaks escalate undetected, chronic disease burdens are quantified years later, and at-risk populations in data-sparse regions remain unaddressed. Planetary geospatial foundation models complement existing epidemiological workflows to provide operational improvements, encoding multimodal search, mobility, and environmental signals into generalizable place representations. As illustrations of this complementarity, we present independent global health case studies of Google Earth AI's Population Dynamics Foundation Model (PDFM) -- a foundation model for geospatial inference -- across four domains (vaccine-preventable, communicable, noncommunicable, maternal mental health), five tasks (spatial extrapolation, interpolation/nowcasting, probabilistic forecasting, prospective forecasting, risk stratification), and four countries (USA, Canada, Mexico, and the Democratic Republic of the Congo). Across these case studies, PDFM addresses critical surveillance gaps across domains: improving US-Canada border MMR vaccination coverage predictions by capturing cross-border behavioral spillovers domestic models miss; nowcasting cardiovascular disease to accelerate data availability; enhancing short-term municipal Mexican dengue forecasts for timely outbreak vector control; improving forecasts of cholera hotspots; and adding a transferable signal to individual-level postpartum-depression risk prediction in US states the model had never seen, while not replacing individual socioeconomic data or closing demographic screening gaps. Together, these results showcase capabilities of geospatial foundation models for public health surveillance.

---


### 490. [AdaSpark: Adaptive DSpark with Online Learning for Tree Verification and N-gram Fill](https://arxiv.org/abs/2610.05774)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Liquan Liu, Yifan Zhang, Bowei Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block drafters such as DSpark propose ranked candidates for several positions in one forward pass, and a tree verifier checks them in one pass of the target. The number of rows to verify trades the tokens a wider tree is expected to accept against the time a wider verify takes. Most schedulers that choose this number take the verify time from a table or model measured before serving, corrected online by at most one scale factor, and take acceptance from the drafter's confidence estimates or from a map fitted offline.
AdaSpark learns both quantities while it serves, with no profile, calibration or sweep in advance. It learns which verify widths are worth offering and fits each one's verify time as a function of context. It fits each candidate's acceptance probability to the target's verify outcomes, with the drafter's confidence head as one input, and orders and sizes the tree by that fit instead of by the head. The same model prices n-gram continuations of the request's own text, so drafted and text-derived candidates compete for rows in one best-first order. The width is chosen by pricing time at the long-run decode rate.
On single- and multi-turn conversations from six public datasets, on three dense targets and one mixture-of-experts target, AdaSpark decodes 1.5-3.1x faster than this http URL's DSpark with the same drafters. Our imparo engine with AdaSpark is 1.17-1.52x faster than imparo running with a three-token chain (the default this http URL setting); this gain comes from the scheduler alone. Without a width sweep, AdaSpark is never more than 0.3% slower than the best pinned tree width on any dense target or context band. On the mixture-of-experts target it ties the best pinned width, and the other pinned widths from 4 to 16 rows are 5-14% slower.

---


### 491. [FairRSFM: A Biome-Aware Benchmark and Debiasing Framework for Remote Sensing Foundation Models](https://arxiv.org/abs/2610.05790)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Md Aminur Hossain, Omkumar Vaghasiya, Rajeev Ranjan Dwivedi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing foundation models (RSFMs) are commonly evaluated using aggregate metrics, which can hide systematic performance disparities across ecological regions. We introduce FairRSFM, a biome-aware benchmark for evaluating ecological group robustness in RSFMs. FairRSFM maps georeferenced samples from 14 terrestrial biome classes into six ecologically meaningful macro-groups and evaluates models under a unified frozen-backbone evaluation protocol. The benchmark covers four downstream datasets: m-EuroSAT, m-BigEarthNet, m-SA-Crop-Type, and MMEarth20K with Dynamic World label maps. Using Prithvi-EO-2.0, SatMAE, and DOFA across three random seeds, we show that aggregate performance consistently masks biome-dependent disparities across architectures and tasks. For example, Prithvi-EO-2.0 reaches 90.98% overall macro-F1 on m-EuroSAT but a mean worst-group score of only 83.72%, while m-SA-Crop-Type drops from 27.30% overall mIoU to 18.47% in the Xeric and Mineralogical group. We further evaluate Biome-Orthogonal Linear Probing (BOLP), Dynamic Biome Reweighting (DBR), and GroupDRO as complementary mitigation baselines. Their effectiveness is model- and task-dependent; for example, BOLP improves Prithvi-EO-2.0 worst-group F1@opt on m-BigEarthNet from 46.12% to 50.27% without updating the RSFM backbone. FairRSFM provides a reusable protocol for diagnosing and mitigating ecological robustness gaps in remote sensing foundation models. Code and datasets are available at: this https URL.

---


### 492. [Bounded Provisional Visibility: Controlling Poisoning Exposure in Continuously Ingested RAG Vector Stores](https://arxiv.org/abs/2610.05826)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chuhong Xu, Lu Yi, Gangzhen Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Continuous ingestion can expose new retrieval-augmented generation (RAG) content to retrieval before vetting completes, creating a temporal attack surface that conventional admission decisions do not capture. We present a fail-closed provisional-visibility protocol that admits new content under a deadline, hides items whose verification has not committed in time, and supports lineage-scoped containment. The protocol bounds unvetted exposure by the configured visibility budget plus query-path enforcement delay; poisoning exposure remains conditional on verifier correctness. We evaluate the design on five workloads of encoded natural-language documents using an exact backend and Milvus. Under verifier backlog, the deadline reduced median poisoned retrievals from 34 (29--34) to 7 (6--7) relative to asynchronous admission without a deadline, with the same reduction in displaced clean results. Verify-before-visible avoided provisional exposure but delayed clean first visibility to 6.3 s, whereas provisional admission made content visible within 3 ms; expired clean items could nevertheless experience temporary availability gaps. Replaying decisions from a recipe-specific detector illustrated the protocol boundary: false promotions left poison visible, while false refusals excluded clean content from retrieval. Standalone Milvus tests characterized enforcement delay and concurrent HNSW retrieval on one node. These results clarify which guarantees come from the protocol and which outcomes depend on detector quality, while quantifying the freshness and availability trade-offs.

---


### 493. [The Optimization Landscape of Learning Compacted Context Models](https://arxiv.org/abs/2610.05885)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Thomas Villeneuve, Alex Sandomirsky, Charles O'Neill 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many works approach continual learning through the lens of infinite context windows. As an agent puts more observation into context (concretely the KV cache), compacting said context is akin to direct memory manipulation, without affecting the base model's weights. Many works pose KV compaction as an optimization problem: learn a smaller set of KV vectors that matches the behavior of the full KV cache. While this preserves base model behavior, optimizing through a frozen base model results in a highly nontrivial optimization problem with a brittle and flat loss landscape. In this paper, we characterize what makes these optimization problems difficult and demonstrate that a heavily simplified Perceiver-based architecture not only matches performance of a full Perceiver transformer in continuous context compaction, but outperforms baselines on compaction utility. Results are presented on MCQ tasks across Finance, Legal, Gutenberg, and Code.

---


### 494. [The Arbitrary-Placement Problem in Entropy-Minimizing Selection, and a Residual-Entropy Formulation](https://arxiv.org/abs/2610.05925)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alyssa H. Shin, Claire H. Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Entropy-based selection objectives suffer from a fundamental degeneracy: minimizing Shannon entropy $H(p_A)$ rewards confident selection regardless of whether the selected candidate is informative. We address this limitation with the residual entropy $D = H(p_A) - H(p_\beta)$, where $p_\beta$ is induced by candidate trust weights. We prove the exact identity $D = -\mathrm{KL}(p_A\Vert p_\beta) - \Delta$, where $\Delta$ measures whether the score-induced distribution and trust profile favor the same candidates. Boundary cases establish basic safety: under uniform trust, $D\leq0$ automatically, so an equal-trust, non-starving state is never penalized, while at any one-hot limit, $D\to0$ regardless of the selected candidate. For the intermediate regime where selection occurs, we prove that $D\leq0$ when candidate ordering by trust agrees pairwise with ordering by informativeness, and derive a tighter certificate based on the leading candidate's margin over its competitors. These results are independent of the candidate-scoring function and apply to both stationary and dynamically changing information. Experiments with a gradient-based mixture-of-experts router confirm that the ordering conditions can hold during real optimization and show that correct ordering improves downstream performance when candidates are non-interchangeable and selections are used directly rather than averaged. Beyond routing, margin-based reweighting matches or outperforms fixed-strength baselines in a class-imbalance task, while informative selection in a production video-prediction system reduces MSE by approximately 20$\%$ and transfers to a related species. Residual entropy, therefore, provides a safety criterion for selection and a usable signal for deciding when that selection is informative.

---


### 495. [Runaway Reaction: When Benign Skills Compose into Malicious Behavior](https://arxiv.org/abs/2610.05943)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zunlong Zhou, Ziyuan Yang, Mengyu Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills package task-specific knowledge and procedures that can be composed to support complex agent tasks, while public marketplaces provide a growing pool of reusable skills. Existing security vetting, however, largely evaluates skills in isolation, leaving composition-induced risks underexplored. Such risks arise because composing benign skills expands the agent's capability space, enabling behaviors unavailable to any skill alone. Interestingly, we find that directly composing benign skills can already induce malicious behaviors, even when every individual skill passes security vetting. We further find that some target malicious behaviors remain difficult to realize through direct composition, even when the selected skills collectively provide the required capabilities. To systematically instantiate these attacks, we present Compositional Risk Induction via Multi skill Execution (CRIME). CRIME first uses the Malicious Plot Casting (MPC) module to decompose a target malicious behavior into complementary requirements and identify suitable benign skill compositions from public skill repositories. For compositions that cannot directly realize the target behavior, the Runaway Reaction Steering (RRS) module uses execution feedback to iteratively refine the selected skills toward the target while requiring each skill to remain benign under standalone vetting. The resulting composition is then passed to the Skill Reaction Chamber (SRC) module, where the skill pair is executed in a sandbox and the resulting environmental consequences are examined to determine whether the target behavior has occurred. Unsuccessful cases are returned to RRS for further refinement. Furthermore, we construct a benchmark of 4,000 public skills across eight cybersecurity behaviors for systematic evaluation of composition-induced vulnerabilities.

---


### 496. [MEND: RL For Flow Models via Proximal Velocity Matching](https://arxiv.org/abs/2610.05954)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shreshth Saini, Neil Birkbeck, Yilin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward post-training of flow models either reweights the model's own samples under a KL penalty or a frozen reference, often for thousands of updates, or backpropagates the reward and moves every sample without checking that the move is worth its size. We introduce MEND, a reinforcement learning method built on proximal velocity matching. MEND caps rewards within each prompt group, so samples that already score well receive no move. Below the cap, it proposes moves along the reward gradient and accepts one only when its capped reward gain exceeds a quadratic displacement price. The model then regresses onto the resulting velocity targets, with no KL term, frozen reference model, or advantage weights. In 100 updates, MEND outperforms Flow-GRPO (about 4k updates) on five of six evaluators at the same distance to base-model images. Under an equal-budget protocol, it surpasses ReFL and DiffusionNFT at every evaluated update across four training rewards, reaching PickScore 24.03 versus 23.92 and 23.43, respectively. A 300-update three-reward run also surpasses the five-reward DiffusionNFT model on all three rewards it trains on. MEND is general and easy to adopt: it applies to any flow backbone with a differentiable reward.

---


### 497. [Label-Free Coreset Selection with Foundation Models for Efficient Annotation in Computational Pathology](https://arxiv.org/abs/2610.05987)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tuo Yin, Jennifer Dhont  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computational pathology has the potential to improve clinical outcomes through a demonstrated increase in diagnostic and prognostic accuracy. However, the development and validation of deep learning algorithms still require annotated data, a costly procedure involving expert pathologists who already face critical workforce shortages. Existing coreset selection methods to optimize annotation efforts currently all rely on hyperparameters tuned on natural-image benchmarks that do not transfer to histopathology and are cumbersome to use in clinical practice. In this study, we present GCcore, a novel label-free coreset selection method that embeds every image of a dataset with any pathology foundation model and greedily selects the samples that collectively maximize the global coverage of the embedding space. The proposed method provides a lower-bound guarantee on the global coverage of the returned coreset for any coreset size, while being completely hyperparameter-free and deterministic. We demonstrate GCcore's superior performance over 14 baselines including state-of-the-art methods across 10 tasks and datasets spanning whole slide image classification, tile classification, and tissue segmentation, where it ranks first on six and within the top three on nine, while also demonstrating how existing methods can shift by up to five rank positions depending on their hyperparameter settings. Code is publicly available at this https URL.

---


### 498. [Anlu: Enabling In-Context Time Series Anomaly Detection in Foundation Models via Counterfactual Supervision](https://arxiv.org/abs/2610.06180)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tian Lan, Yifei Gao, Yimeng Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Whether a time-series pattern is anomalous often depends on the operating regime of the monitored process. A missing event can signal a fault in one regime and be routine in another, and the query alone may not reveal which regime applies. We study in-context learning (ICL) for time series anomaly detection (TSAD) through reference-conditioned detection, where a reference record provides evidence about expected behavior and model parameters remain fixed at inference. Supplying the reference is not enough: when training anomalies are recognizable from the query alone, the detector can fit its targets while ignoring the reference. We therefore introduce counterfactual supervision, which pairs one query with two references that support different normal rules and labels the query under each. At positions where the two labels disagree, no detector that ignores the reference can fit both targets. Anlu learns from this supervision by adding a reference memory and zero-initialized gated adapters to a frozen time-series foundation model (TSFM) pretrained for anomaly detection. On the 350 TSB-AD-U evaluation sequences, Anlu raises the mean VUS-PR of the frozen TSFM from 0.542 to 0.607. Replacing the reference with zeros lowers Anlu's score to 0.499.

---


### 499. [SimAuthor: Harnessing Foundation Models for Persistent Scientific Simulator Authoring](https://arxiv.org/abs/2610.06257)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yishan Wang, Ran Piao, Mathias Funk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models can generate scientific code, but authoring a scientific simulator (an executable program encoding hypotheses about how mechanisms generate observable signals) requires iterative refinement. Scientific adequacy rarely admits a unique implementation or exact test, so simulators must instead be judged against limited real observations. We study this setting as scientific simulator authoring under weak empirical feedback, where distributional comparisons between simulated and real signals guide revision, and the target is the simulator itself rather than only its generated samples. We introduce SimAuthor, a persistent authoring harness that retains and revises executable simulators, separates scalar search scores from structured discrepancy feedback, and accumulates reusable implementation mechanisms. We evaluate SimAuthor on six biomedical tasks spanning cardiac and respiratory audio, photoplethysmography (PPG), and electrocardiography (ECG). Under a fixed 100-attempt budget, SimAuthor outperforms PUCT score search on all six tasks, generally outperforms textual-strategy optimization, and achieves the highest endpoint score on five of six. The authored simulators also improve on unseen recordings, transfer to independent pretrained representations, and yield substantial out-of-distribution gains in downstream ECG classification. Finally, 111 of 138 audited revisions alter program structure and account for 86.1% of the signed score improvement. These results suggest that persistent revision can progressively convert foundation-model knowledge into better executable scientific simulators from limited empirical evidence.

---


### 500. [Time-series Foundation Models for Predictive Control: The Role of Excitation](https://arxiv.org/abs/2610.06447)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mazen Amria, Jasper Hoffmann, Philipp Bordne 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying model predictive control (MPC) requires constructing or identifying a predictive model for each target system. Time-series foundation models (TSFMs) offer an attractive option thanks to strong zero-shot forecasting capabilities across systems. However, low forecast error does not guarantee that a TSFM captures the system's response to the alternative actions considered by the controller. We study this gap using residential heat-pump control as a test bed, measuring the agreement between predicted and ground-truth effects of control interventions. Importantly, we find that TSFMs can recover the system's input-response relationship when the context contains sufficient independent control excitation. Common fine-tuning pipelines and feature smoothing reduce, but do not eliminate, the need for in-context excitation. Our results indicate that current TSFMs used for predictive control require sufficiently informative control variation in the inference context. Initial closed-loop results show promise for shorter context windows.

---


> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-505](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
