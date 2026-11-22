# 🧠 大模型相关研究 | 2026年11月22日

> 本类共 **265** 篇论文：已确认 **245** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-265](./part-06.md)

---

### 201. [Budget Internalization: Fixed-Budget RLVR Trades Test-Time Scaling for In-Budget Accuracy](https://arxiv.org/abs/2611.26172)

**<font color=#1a73e8>作者：</font>** Ilia Zavidnyi, Alexander Kovrigin, Arina Puchkova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models often become more accurate when they can generate longer answers at test time. This behavior is known as test-time scaling. However, RL with verifiable rewards (RLVR) usually trains them with a fixed rollout cap. We find that this cap changes model behavior, not only training cost. After training, models use few additional tokens beyond the training budget. They outperform the base models near that budget, but their accuracy stops improving and falls below the base model at larger budgets. The rollout cap thus becomes a learned constraint, that limits model's test-time scaling. We call this effect budget internalization. We observe it across Qwen3.5-4B, Gemma4-E2B, and Nemotron-3-Nano-4B and two reasoning training tasks: mathematical reasoning and diverse, procedurally generated problems. This effect also transfers from math training to science and coding tasks. Training-objective level ablations on Qwen3.5-4B show that most changes recover little test-time scaling. Stronger KL regularization and lower training-data truncation preserve more scaling, but stronger KL reduces in-budget accuracy. Forcing an answer on truncated training rollouts largely removes budget internalization, but also removes most of the in-budget gain. SFT on artificially truncated traces reproduces budget internalization, whereas SFT on naturally short traces does not, which shows that the effect is not specific to RL. This result links budget internalization to length-censored post-training rather than to an RL-specific objective term. Thus, a rollout cap does not only control training cost. It can trade low-budget gains for lower performance when additional inference compute is available.

---


### 202. [SpatialScout-V2: Can VLM Agents Actively Explore Real-World 3D Scenes and Localize Objects?](https://arxiv.org/abs/2611.26177)

**<font color=#1a73e8>作者：</font>** Zhaoxi Zhang, Hao Liang, Linxuan Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence requires agents to acquire visual evidence and integrate partial observations into coherent three-dimensional representations. We introduce SpatialScout-V2, which extends SpatialScout's active mapping task from simulation to real residential scenes through three advances: real visual observations, preservation of original scene content, and interactive exploration of recorded views. Built from 100 homes in Realsee3D, the benchmark covers 3,171 target objects across 29 categories. Given a fixed target inventory, agents autonomously select recorded viewpoints and viewing directions, integrate calibrated RGB observations, and iteratively estimate and revise object centers within a fixed interaction budget. We evaluate the localization accuracy and completeness of object-center maps using mean IoU, IoU-threshold hit rates, and target coverage. Evaluating seven frontier vision-language models (VLMs), we find that six achieve an all-target mean IoU below 20\%. Even the best-performing model, Claude Opus 5.5, reaches only 22.52\%, with just 18.36\% of targets exceeding an IoU of 0.5. Further analysis shows that broad submission coverage can coexist with limited localization accuracy, while target omissions further reduce overall scores. These results highlight substantial challenges in constructing accurate and complete object-center maps through active exploration of real scenes.

---


### 203. [RegionAgent: Two-Stage Preference Optimization for Regional Image Restoration](https://arxiv.org/abs/2611.26179)

**<font color=#1a73e8>作者：</font>** Weiyu Zhou, Jiacong Tang, Tao Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images under non-uniform coupled degradations require diverse restoration capabilities for different degraded regions. Existing methods employ globally uniform operations, potentially overlooking regional differences and causing incomplete restoration or even damage to image content. Moreover, a degraded region may require successive restoration actions, and earlier actions may alter residual degradation characteristics or introduce artifacts, potentially hindering subsequent restoration. To address these challenges, we propose RegionAgent, an adaptive restoration framework that trains a Vision-Language Model (VLM) through two-stage preference learning to generate a region-specific restoration action at each iteration. Specifically, we first train the VLM to select an action suited to the current region through step-level Direct Preference Optimization (DPO), using preferences derived from immediate restoration feedback to supervise only the differing component in each action pair. To account for the effects of current actions on subsequent restoration, we then apply trajectory-level DPO, using preferences derived from complete trajectory scores to supervise the sole differing action in each trajectory pair. Furthermore, as conventional image-pair datasets do not directly provide preferences over regional restoration decisions, we construct a regional restoration preference dataset comprising 10K action pairs and 20K trajectory pairs for two-stage VLM training. Experiments across multiple datasets demonstrate strong restoration performance under both mixed and single degradations. Ablation studies further validate the effectiveness of two-stage preference learning in improving restoration quality.

---


### 204. [Learning to Think with Images Faithfully via Adaptive Data Selection](https://arxiv.org/abs/2611.26199)

**<font color=#1a73e8>作者：</font>** Yu Zhao, Jiaxin Zhang, Rohit Saxena 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thinking with images (TwI) empowers vision-language models (VLMs) to overcome perceptual bottlenecks by actively cropping and zooming into fine-grained visual details, promising both higher accuracy and interpretable, region-grounded reasoning. However, our analysis shows that the improved accuracy of TwI models does not guarantee faithful tool use; they frequently invoke tools without actually relying on the zoomed region, undermining the reliability of tool-assisted reasoning. We trace this unfaithful behaviour to the training data: when questions are answerable without zooming, the model can answer correctly while ignoring the returned evidence, and this problem is exacerbated during training as the model becomes better at answering without tools. To keep zooming useful throughout training, we adapt the training data to the model's evolving capability and train on questions where correct zoomed evidence can still help the model answer correctly. This selection is supported by a data synthesis pipeline that localises small objects and constructs verifiable questions about their fine details, and complemented by an adaptiveness reward that favours tool-free answers when zooming is unnecessary. The experimental results show that our method substantially improves reasoning faithfulness and achieves state-of-the-art performance on visual search benchmarks (+11.6% on V*, +7.9% on HR-Bench 4K, and +9.4% on HR-Bench 8K). On multimodal hallucination benchmarks, our model also outperforms the compared TwI baselines. These results suggest that improving TwI faithfulness does not sacrifice accuracy and that both can be learnt from the right training data without directly supervising the reasoning process.

---


### 205. [Frontier models need only one text to unmask its human or AI author](https://arxiv.org/abs/2611.26216)

**<font color=#1a73e8>作者：</font>** Atrey Desai, Deniz Böloni-Turgut, Ty Brassington 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Given a single text and a simple zero-shot prompt (no web access, tools, candidate lists, or writing samples), frontier models can answer "who wrote this?" at three increasingly specific levels: (1) whether an AI or human wrote it, (2) if an AI, which lab, and (3) if a human, often exactly who. The latest models (Claude Fable 5.2, GPT-6.1 Sol, Gemini 4 Carbon) match trained detectors like Pangram while also explaining their predictions in natural language, and Opus 5.5 names the correct lab for 98% of texts generated by models from Anthropic, OpenAI, and Google. Most strikingly, Fable 5.2 correctly names the author of 39% of public peer reviews published in Oct-Nov 2026 (78% on a subset of reviews from Nature), and identifies the username behind 69% of comments from active Redditors (with >500 posts over the last year). Accuracy depends on exposure to an author's writing in pretraining data and on reasoning effort, and simply asking a model how familiar it is with someone predicts whether it can identify their writing. For anyone who has published enough writing online, frontier models present a greater threat to anonymity than commonly assumed, and defenses are limited.

---


### 206. [TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs](https://arxiv.org/abs/2611.26248)

**<font color=#1a73e8>作者：</font>** Yang Wan, Linchao Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly expected to act as AI scientists, which requires three increasingly open abilities: carrying out a given computational workflow correctly, choosing the next measurements from a given design space, and designing their own experiments. Existing benchmarks mainly evaluate the first two abilities, in a terminal or in a closed loop that selects from predefined candidates. Evaluating the third ability requires reliably executing an experiment that an agent designs, with readings grounded in a real laboratory. We introduce TwinLab-Bench, which evaluates AI scientists on self-designed experiments in 52 tasks from laboratories in the physical sciences, the life sciences, and engineering. The benchmark supports more than 100 experimental action types, and the agent's report is scored by comparison with a hidden answer taken from real laboratory records. Each task has its own TwinLab agent, an agent that serves as the environment and executes the experiments that the tested agent designs, reading the raw materials of the laboratory and calling calculators that are built from its records. Compared with a language model that sees only the task description, the TwinLab agent almost eliminates readings that deviate from the real records and inconsistent answers to a repeated request, and closed-book probes control for answers recalled from memory. We find that these tasks remain hard for frontier models: the strongest, Claude Fable 5.2, averages a score of only 45.0, and we conduct an empirical study of where it fails.

---


### 207. [dLoop: Looped Diffusion Language Models via Recurrent Latent Refinement](https://arxiv.org/abs/2611.26275)

**<font color=#1a73e8>作者：</font>** Handa Li, Pengxiang Li, Mingyu Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) support parallel generation, yet they often require many denoising steps because only a fraction of token predictions are sufficiently reliable to be committed at each step. Existing acceleration methods primarily optimize confidence learning or commitment policies. However, these approaches operate on the outputs of a single denoising forward pass, in which information from the prompt, previously committed tokens, and uncommitted positions may not yet be fully integrated. Consequently, some predictions remain under-refined when the commitment decision is made, and modifying the commitment policy alone cannot improve their underlying representations. We introduce dLoop, which restructures a pretrained diffusion language model into a Prelude-Loop-Coda architecture and recurrently applies a parameter-shared intermediate block to the same partially masked state. Rather than advancing the denoising process, each additional loop provides further latent computation, allowing information distributed across uncommitted positions to continue interacting and become more fully integrated before commitment. Experiments on GSM8K, MATH, MBPP, and HumanEval show that dLoop achieves the highest or tied-highest accuracy on every benchmark. With tokens per forward pass (TPF) adjusted for loop computation, it outperforms Fast-dLLM in both accuracy and TPF on all four benchmarks and dParallel on three, and is more accurate than d3LLM on all four, while d3LLM attains higher TPF; no compared method surpasses dLoop in both. Mechanistic analyses show that extra loops mainly help on slow, unstable trajectories and that updates at uncommitted positions drive changes in token decisions and later generation. Pre-commitment latent computation thus makes predictions more reliable, offering a route to DLM acceleration distinct from forcing confidence through the training loss.

---


### 208. [What If Chain-of-Thought Is Not Enough?](https://arxiv.org/abs/2611.26282)

**<font color=#1a73e8>作者：</font>** Marc Jansen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning capabilities in large language models have evolved from prompting-based methods to internalized model behaviors. In this paper, we investigate whether the internal thinking model of an LLM can be deliberately changed and whether such a change is beneficial. Instead of relying on Chain-of-Thought, we train models to follow Question--Option--Criteria (QOC), a structured decision process that decomposes a task into explicit questions, competing options, and evaluation criteria. We present a three-generation development pipeline that ranges from a basic QOC decision core to richer answer synthesis and statistically enriched QOC reasoning. We then evaluate the resulting models with respect to both internal consistency and output quality. Across the reported experiments, QOC-based fine-tuning improves answer quality relative to non-fine-tuned base models and yields particularly strong gains once models are large enough to execute the underlying QOC computations reliably. The results suggest that the internal thinking model of an LLM is trainable and that structured alternatives to Chain-of-Thought can provide a promising path toward more reliable, interpretable, and task-adapted decision support.

---


### 209. [Twice-Told Critiques: Claim-Level Homogenization of Peer Review in the LLM Era](https://arxiv.org/abs/2611.26286)

**<font color=#1a73e8>作者：</font>** Ilya Gusev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Peer review relies on several readers finding different problems. We measure critique overlap in conference and journal reviews. At ICLR, measured overlap rose from 12.0% in 2026 to 21.3% in 2027, in reviews from the same stage of the review process, with year-on-year rises at NeurIPS, ICML and the F1000 and PLOS journals. A third ICLR review of a paper added 5.46 new problems to the other two in 2027, against 6.12 in 2026. We apply MELD, a detector of LLM-generated text, to all reviews. Within a paper, two reviews that MELD flags overlap more than two unflagged reviews: by 3.0 points at ICLR in 2024-2025, by 4.5 points in 2026-2027, and by 5.4 points across five journal sources. These results provide evidence that LLM-flagged reviews of one paper are less distinct from each other than unflagged reviews, and suggest that the diversity of critiques among reviews of a single paper is falling.

---


### 210. [SKILL.PNG: Learning Agent Skills in Pixel Space](https://arxiv.org/abs/2611.26296)

**<font color=#1a73e8>作者：</font>** Maximilian Seeth, Chengzhi Martin Hu, Marie Kempkes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI agents are commonly specialized for new tasks and domains using skills, i.e. natural language instructions placed in their context. However, the discrete nature of textual skills prevents continuous optimization. Gradient-based approaches such as finetuning, on the other hand, are typically model-specific, preventing skill transfer across different agents. Since many agents today are built on vision-language models (VLMs), we can address these limitations by introducing this http URL: a method for obtaining skill-like image inputs whose pixels are optimized with gradient descent through the vision encoder of a frozen VLM. Image skills are compatible with any VLM, and a single image can be optimized jointly for an ensemble of models. We show that this http URL significantly outperforms state-of-the-art textual skills optimized using frontier LLMs in 9 of 16 settings (across 4 VLMs and 4 benchmarks) while requiring only 64 to 256 image tokens instead of roughly 900 to 2000 text tokens at inference time. Hybrid skills, i.e. text and image skills jointly optimized, further improve agent performance. Moreover, an image optimized with an ensemble of VLMs can successfully transfer across the models in the ensemble. this http URL thus presents the first agent skill that can be optimized with gradient descent while retaining transfer benefits of text skills. Our code is available at: this https URL

---


### 211. [DailySafe: Benchmarking Dynamic Safety Awareness in Everyday Multi-Turn Multimodal Interactions](https://arxiv.org/abs/2611.26298)

**<font color=#1a73e8>作者：</font>** Xuankun Rong, Xinhao Deng, Wenzhang Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As multimodal large language models (MLLMs) become increasingly integrated into everyday life, their ability to provide safe and reliable assistance in realistic daily activities remains insufficiently explored. Existing safety benchmarks primarily focus on isolated harmful requests or adversarial scenarios, overlooking the safety risks that may arise as ordinary tasks unfold. In practice, users pursue legitimate goals through multi-turn, multimodal interactions, where seemingly benign requests may become safety-critical when considered alongside earlier actions and visual observations. This calls for Dynamic Safety Awareness, the ability to track evolving task conditions, recognize implicit contextual risks, and provide safe and helpful assistance. To systematically evaluate this capability, we introduce DailySafe, a benchmark comprising 195 naturalistic multi-turn, multi-image interactions across 10 everyday domains and 42 task categories. Grounded in authentic user dialogue topics and documented safety knowledge, DailySafe captures realistic scenarios where safety-critical evidence is progressively revealed across conversational turns and visual observations. Using case-specific safety annotations, DailySafe assesses whether MLLMs can recognize and appropriately address evolving risks while supporting users' legitimate goals, bringing multimodal safety evaluation closer to real-world everyday AI assistance. DailySafe is publicly available at: this https URL.

---


### 212. [Client Exits - A Way to Increase LLM Transparency on the Client Side](https://arxiv.org/abs/2611.26309)

**<font color=#1a73e8>作者：</font>** Marc Jansen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Textual recommendations generated by large language models (LLMs) can be difficult to inspect. This paper introduces \emph{Client Exits}, a lightweight mechanism for enriching LLM responses while separating semantic intent from client-specific presentation. The model inserts predefined, machine-interpretable markers into its output, and the receiving client decides whether and how to realize the corresponding enrichments. This allows supplementary information to be presented as graphics, text, speech, or other modalities without prescribing a concrete interface. We implement a prototype combining a finetuned Qwen model with a modified LibreChat client. Using the Question--Option--Criteria (QOC) approach including three XML-based client exits. We evaluate two QOC-oriented model variants trained on essentially the same examples, with client-exit annotations added for one variant. Across 100 test questions, the client-exit model includes all three markers in every response. An LLM judge, informed about the mechanism without being instructed to favor it, prefers this model's answers in 66\% of the comparisons. These results demonstrate successful marker generation on the evaluated test set and support the feasibility of client-controlled enrichment.

---


### 213. [ResVision: Spectrum-Matched Resizing and Context-Preserving Inspection for Visual Reasoning](https://arxiv.org/abs/2611.26318)

**<font color=#1a73e8>作者：</font>** Guojian Zhan, Jiahao Xu, Yahui Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic visual reasoning improves vision-language models by selectively enlarging evidence without adding new scene content, but the benefit depends on whether fine structure remains accessible and whether local observations stay grounded in the full scene. We identify three recurring bottlenecks: high-frequency detail can be attenuated during visual-token formation; spatially distributed evidence can remain encoded yet difficult for the language model to retrieve; and isolated crops can weaken whole-detail correspondence through scale and positional mismatch. ResVision addresses these limitations with two complementary components. Spectrum-Matched Resizing (SMR) estimates image complexity and selects an adaptive global sampling scale, avoiding unnecessary enlargement on simple inputs while allocating more visual tokens to detail-rich images. Context-Preserving Inspection (CPI) returns each inspected crop together with the complete working view, preserving local detail and global context across tool turns. We evaluate Direct and Agentic variants on four frontier VLMs and 29 benchmarks spanning six visual-reasoning families. Complete ResVision (Agentic Base plus SMR plus CPI) is best for every model, improving by 3.36 to 4.94 points over Direct Base and 1.87 to 2.94 points over Agentic Base. These results show that adaptive visual sampling and context-preserving inspection address distinct, complementary constraints in multimodal reasoning.

---


### 214. [Rigel-Ladon: An Option-Count Law for a One-Pass Decision Encoder, Tested on Held-Out Option Counts and Held-Out Schemas](https://arxiv.org/abs/2611.26332)

**<font color=#1a73e8>作者：</font>** Mohammed Nayeem Khan, Vrishank Tiwari, Navin Kumar R  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Laya is a small neural network that reads a text, a question and K written options, and returns one probability per option in a single pass. We ask how its accuracy falls as K grows from 2 to 35 and whether that can be predicted. We score nested option sets (every K-option question contains the smaller ones) on four question pools, for the released model (Base) and our fine-tune (FT), and score every item against each single rival. FT trained on one 12-option topic question (in-family); a 12-option HR (department-routing) question is out-of-family. Logit accuracy (the log of correct over incorrect answers) is linear in log(K-1) with slope 0.68 to 0.88. Fitted on K up to 6, the law predicts K=7 to 12 within 0.6 points and K up to 24 within 1.2 (a log-linear rule: 1.6 and 6.7). Taking the slope from the topic question and measuring only two-option accuracy on HR predicts its other K within 0.3 points (FT) and 0.7 (Base). On a 35-label pool of five schemas the law fails (5 to 11 points). Independence of irrelevant alternatives is rejected: the gold-versus-rival log-odds shifts by +0.24 to +2.07 nats per doubling of K, yet pairwise answers reproduce K-way accuracy within 4.7 points. Order averaging (averaging over several orderings of the options), shortlists, a temperature law and calibrated prediction sets did not transfer (FT's 90% sets cover 84% on HR). 2 of 10 predictions made in advance held. Caveats: one model family and LLM-labelled synthetic text.

---


### 215. [OceanCoder: A Verification-Guided Large Language Model for Automated Simulation Modelling in Ocean Engineering](https://arxiv.org/abs/2611.26333)

**<font color=#1a73e8>作者：</font>** Can Xue, Changhong He, Ziyi Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numerical simulation is important in ocean engineering, but model construction requires expert knowledge. Large language models support automated modelling, but code syntax and successful execution alone do not establish whether generated models and results meet engineering requirements. We present OceanCoder, a Qwen3-8B-based large language model for automated simulation modelling in ocean engineering. To address specialised programming requirements and scarce training data, we develop an extensible data construction pipeline producing 12,000 verified supervised fine-tuning (SFT) examples across 12 engineering task categories. A three-layer verification framework checks model inputs against engineering parameters and task constraints, verifies completion of required simulation analyses, and assesses the engineering plausibility of computed outputs. Its outcomes provide graded rewards for group relative policy optimisation (GRPO), guiding the model towards engineering task completion. We also construct the first benchmark for automated modelling in ocean engineering, covering out-of-distribution tasks and real-world engineering cases. Experiments and ablation studies demonstrate the effectiveness of the data pipeline, verification framework and reward design. OceanCoder outperforms both base models and the closed-source comparison, with Pass@1 increasing from 0% for the base model to 46.77% after SFT and 51.43% after GRPO. These results support engineering verification as a training signal for automated simulation modelling.

---


### 216. [Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers](https://arxiv.org/abs/2611.26334)

**<font color=#1a73e8>作者：</font>** Ryan Lucas, Petros Prastakos, Rahul Mazumder  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers reuse key--value (KV) caches across denoising steps, which quickly becomes a bottleneck for long video generation. We find that quantizing temporally distant cache vectors leads to a large range and high quantization error, but that nearby video tokens in the KV-cache share a persistent pattern per channel. These patterns also vary across videos, motivating rotations that are adapted to each video's unique cache. We propose Temporal Rotation Quantization (TRQ), a method that rotates frames in the cache that are adjacent in time before quantization. For each block of temporally adjacent cache vectors, TRQ fits an orthogonal transform that maps the block's per-channel means to a vector that is close to a constant across channels. To keep the quantization format lightweight, we parameterize this rotation as a tree of $2 \times 2$ planar rotations, each stored with only two bits, followed by a fixed Hadamard transform shared across all blocks. The rotations are fit without gradients or changes to model weights, and we prove that a simple greedy fit is globally optimal for our 'mean-flattening' objective. The transforms are fit online for each new video, and we release fused Triton kernels to make this process efficient at inference. At 2-bit precision and matched compression, TRQ improves VBench subject consistency over the state-of-the-art method QVG from 90.38 to 92.02 on LongCat-Video-13B and from 86.33 to 87.61 on HY-WorldPlay-8B, as well as improving other metrics.

---


### 217. [ClosureBench: A Benchmark for Reasoning under Closure Assumptions](https://arxiv.org/abs/2611.26335)

**<font color=#1a73e8>作者：</font>** Francesco Belardinelli, Flavio Corradini, Matteo Leonesi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents built on large language models (LLMs) often answer questions from incomplete records. Missing information might be interpreted as unknown or false, depending on the completeness of the source. Current evaluations fail to distinguish these two aspects, as they are usually interwoven with other reasoning demands. We present ClosureBench, a benchmark that tests whether LLMs follow the stated rules for dealing with missing information. Every base scenario is tested under OWA, CWA, and LCWA, and only the treatment of missing information changes between variants. ClosureBench provides a verified base benchmark as well as agent extensions for action choice, source scope, and updates. A model is considered correct on a base scenario only if it provides correct answers in all of its closure variants. Across 960 instances, overall accuracy can mask substantial closure mistakes. Models achieve overall accuracy from 71.18% to 99.86% across replicated runs, but their core switch accuracy, measured on the scenarios whose gold label actually changes with the contract, varies between 18.23% and 99.31%. Large discrepancies emerge under LCWA. For example, some agents choose unknown despite the prompt indicating that missing information should be treated as false. Our findings demonstrate that evaluations of AI agents should not only measure whether agents can reason over existing facts but also whether they use the appropriate assumption when information is absent.

---


### 218. [One Framework to Diagnose Them All: A Stratified Benchmark for Bengali LLM Hallucination](https://arxiv.org/abs/2611.26336)

**<font color=#1a73e8>作者：</font>** Asif Shahriyar Sushmit, Shefayat E Shams Adib, Abdullah Al Jubaer Gem 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination research in low-resource languages fragments easily: each newly named failure mode prompts its own dataset, spending scarce annotators on incomparable resources. We argue for consolidation and test it at community scale. Alikbachan is a Bengali hallucination-detection benchmark stratified along three crossed axes: a human-validated cultural-distance band, six task types, and a five-family, 32-mode hallucination taxonomy. It comprises a harvested 2,516-item test set (Phase 1) and a quota-constructed, gold-labeled 5,000-item set (Phase 2). The stratification is diagnostic. Four zero-shot LLM judges vary by over 30 macro-F1 points across strata, and the item-level predictions of 99 Phase-1 and 32 Phase-2 competition systems reproduce the profile: discourse-level omission defeats judges and most teams alike, whereas only a minority over-flag negative controls. The judges' verdict probabilities rank items well (ROC-AUC 0.74-0.95) but are overconfident (ECE 0.04-0.29). An open competition on Alikbachan drew 222 teams and 3,566 submissions, and a single-prompt 32B judge reaches the 57th percentile. Of the 25 teams in both phases, 24 regress on Phase 2 (mean $-17.6$ points) while every zero-shot judge improves, and Phase-1 rank barely predicts Phase-2 rank (Spearman $\rho=0.35$), so a Phase-1 leaderboard alone would have crowned a different winner.

---


### 219. [Sirius-Tiamat: How Small Can a One-Pass Decision Encoder Get Before Its Decisions Change?](https://arxiv.org/abs/2611.26339)

**<font color=#1a73e8>作者：</font>** Mohammed Nayeem Khan, Vrishank Tiwari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A one-pass decision encoder reads a text, a question and several named options, and returns a probability for each option in a single forward pass. We ask how far Laya, a 421M-parameter encoder of this kind, can be compressed before its decisions change. We count decisions that differ from Laya's own full-precision (fp32) answer, and track calibration (how well confidence matches accuracy, measured by expected calibration error, ECE), on 1,221 synthetic items with the training schemas, 273 with an unseen schema, and 800 out-of-family questions from ARC, MMLU and HellaSwag. Layer pruning of a related model family is known; we add flips, calibration, held-out data and retraining. bf16 changes 0.2% of in-family decisions but 2.2% out of family; 6-bit grouped rounding 1.3% and 5.9%; deleting 6 layers 0.9% and 9.1%, while ECE rises from 5.9% to 39.2%. One fitted temperature, needing no labels, restores it to 3.6%. One scale per tensor fails below six bits, and CPU dynamic int8 changes 30% of decisions, nearly all through one layer. Total variation tracks flips for rounding but not for deletion, and an early exit saves layers over a static cut only if its confidence gate is first recalibrated. Distilling a 16-layer student cuts its in-family flips from 44% to 9% (45% out of family). At equal stored size, rounding flips fewer decisions than deletion. Data are synthetic and LLM-labelled, for one architecture.

---


### 220. [Training LLMs to Follow Reasoning Instructions with Minimal Edits](https://arxiv.org/abs/2611.26342)

**<font color=#1a73e8>作者：</font>** Alexandra Yakovleva, Luat Gia Khoi Nguyen, Juho Kannala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly rely on extended reasoning traces, yet the training signals used to shape this behavior remain coarse. Supervised fine-tuning on full trajectories forces the model to imitate an entire demonstration, overconstraining its output distribution, while trajectory-level reinforcement learning provides only weak credit assignment, rewarding or penalizing whole completions without identifying where they succeed or fail. We propose edit-based training, a general framework for learning from a model's own trajectories via localized textual corrections. Given a sampled completion, an editor identifies the first point of failure under a specified criterion and proposes a minimal replacement span. The model is then supervised only on these edited spans. By design, this concentrates supervision where the model's reasoning first breaks down and aims to preserve its existing reasoning patterns elsewhere. The method applies both offline and online, with the latter continually adapting supervision to the model's evolving failure modes. We instantiate this approach on reasoning instruction following with Qwen3-32B on the ReasonIF benchmark. Compared to full-trajectory imitation and trajectory-level reinforcement learning baselines, edit-based training substantially improves compliance with the reasoning instruction while largely preserving the model's skills on untargeted tasks. These results suggest that localized correction is an effective complement to these approaches for shaping how LLMs reason.

---


### 221. [DeepQuest: From Knowledge Gaps to Scientific Discovery in Alzheimer's Disease](https://arxiv.org/abs/2611.26343)

**<font color=#1a73e8>作者：</font>** Chunbo Jiang, Yifei Chen, Beining Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating experiments does not necessarily advance scientific understanding. Research agents must identify meaningful knowledge gaps, determine what available data can resolve, and assess whether their findings advance existing knowledge. We introduce DeepQuest, a knowledge-gap-driven AI scientist framework for Alzheimer's disease research. DeepQuest transforms unresolved questions from domain reviews into traceable, testable hypotheses and prioritizes them through data feasibility screening and groupwise Elo ranking. It couples iterative experimentation with two-level auditing that separates experimental reliability from knowledge contribution relative to two frozen literature corpora. On OASIS-3, DeepQuest produces 42 feasible hypotheses and outperforms the strongest baselines in 14 of 15 evaluator-dimension comparisons across three language-model reviewers. The full framework achieves an audit-assessed scientific finding rate of 95.24%, outperforming both general-purpose executors and domain-specific research agents. This scientific finding rate remains stable across literature corpora and evaluator model families. Representative findings concern neuropsychiatric symptoms and dementia risk, longitudinal amyloid spatial stability, and neocortical tau-associated clinical impairment, with key associations supported in independent ADNI and AIBL cohorts. These results show how aligning knowledge gaps, data feasibility, and evidence auditing can turn automated research into traceable, evidence-supported scientific discovery. Our source code is available at this https URL

---


### 222. [How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents](https://arxiv.org/abs/2611.26361)

**<font color=#1a73e8>作者：</font>** K. R. Jayaram, Vatche Isahagian, Aswath Vaithinathan Aravindan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents on long-horizon tasks fail in recurring, procedural ways. They mis-paginate an API, resolve the wrong entity, or answer when no answer was asked. We built a pipeline that lets an agent learn from its own history. It first mines short \emph{lessons} from the agent's own trajectories, one to three per episode. It then consolidates those lessons into a smaller set of \emph{guidelines}, where each guideline records how many lessons it merged. At inference the agent receives either all guidelines or a selected subset. The pipeline ships in the open-source altk-evolve library and is deployed in IBM's CUGA agent and watsonx Orchestrate platform. We report what we learned building, measuring, and productizing it. Our primary instrument is the AppWorld benchmark, across models spanning 40--92\% baseline task completion. The central finding is that the right amount of memory is a property of the model, not the memory. A strong model keeps improving as guidelines are added. DeepSeek-V3.2 gains +9.5 points of task completion and +16.1 points of scenario completion with its full 191-guideline set. A weak model gains less from the same full set than from a small selected subset. gpt-oss-120b starts at 39.9\% task completion. It reaches 51.2\% with all 199 of its guidelines but 55.4\% (mean of two runs) with a selected subset of about 29. Around that result we report what went wrong: a high-support guideline that backfired, provenance silently dropped during consolidation, a swallowed API error that failed every task while producing a plausible log, and a baseline confound that nearly produced a misleading comparison with a prior method. We distill these into recommendations for teams deploying agent memory.

---


### 223. [HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs](https://arxiv.org/abs/2611.26363)

**<font color=#1a73e8>作者：</font>** Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention in large language models (LLMs) scores every query against every key with a full dot product. We investigate whether this dot product must be computed completely for attention to be effective. We propose Hidden Sparse Attention (HiSA), which keeps the query and key projections intact but only computes a partial dot product, following a static, parameter-free rule set by the token positions: attention becomes sparse in the hidden (feature) dimension, an axis much less explored than token sparsity, rather than over tokens as in almost all sparse attention methods. Based on the structure of rotary position embeddings (RoPE), we decompose keys and queries into parts which can be omitted when computing attention. By training LLMs from scratch with HiSA, we find that this partial dot product does not hurt but improves performance compared with the complete product while computing only about a third of the query-key products. During inference HiSA improves decoding speed and shrinks memory footprint. We also extend HiSA to FlashAttention-3 kernels for training and inference. Finally, we motivate our approach by showing that dense attention learns to suppress the attention score parts that HiSA drops. Code is available at this https URL.

---


### 224. [EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning](https://arxiv.org/abs/2611.26380)

**<font color=#1a73e8>作者：</font>** Yuqi Tang, Yang Shi, Yuran Wang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video captioning requires fine-grained detail and accurate timing, yet current multimodal large language models (MLLMs) often miss brief actions, confuse their order, or misinterpret the wearer's motion. Existing caption formats also offer limited support for combining detailed narration with precise timing. We present EgoCaptioner, which pairs a video-level overview of the setting, participants, and the wearer's overall activity with timed steps whose narration adapts to varying perceptual demands and marks key moments at specific timestamps. We develop a coarse-to-fine annotation pipeline that establishes event structure before expanding step descriptions, yielding 50,000 training examples from eight egocentric video sources. Complementary rewards assess factual accuracy and coverage, measure step-level temporal alignment, and penalize fragmented or redundant narration, guiding caption refinement through Group Relative Policy Optimization (GRPO). To improve the reliability of factual supervision, we supplement caption references with pose-derived motion facts when sensor data are available. Across five egocentric benchmarks, EgoCaptioner achieves leading performance among evaluated open-source models in caption quality, caption-conditioned question answering, and temporal alignment. It also surpasses Gemini 3.1 Pro on PhysCapBench and all evaluated proprietary baselines on Minerva-Ego under the caption-to-QA protocol. Ablations support the complementary roles of factual and temporal rewards and show that coarse-to-fine annotation provides more effective supervision than single-pass annotation.

---


### 225. [Training Vision Models for LLM-Driven Weight-Space Programming](https://arxiv.org/abs/2611.26408)

**<font color=#1a73e8>作者：</font>** Timo Ropinski, Sebastian Kranz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> It has been demonstrated that, in certain settings, large language models can perform weight-space programming to directly modify the weights of neural networks. However, it is unknown how dedicated training of these networks can contribute to the successes of weight-space programming. We present a benchmark of LLM-driven weight-space programming on vision models, in which five LLMs edit convolutional networks and vision transformers on relabeling and error-correction tasks on Waterbirds, CIFAR-100, PACS and Entity-30. We report more than 2,600 such edit processes, whereby each edit is scored on held-out images for success, side effects and accuracy loss. We compare standard training with label smoothing, gradient-based editable training, and our Edit-Ready Training (ERT), a novel method that rehearses the direct, closed-form weight edits LLMs perform. We show that preparing networks for editing raises the success of LLM edits substantially where standard networks are hard to edit. ERT further achieves the highest mean score for GPT-6 Astra and Claude Opus 5.5 across all evaluated baselines. We will release our LLM testing framework alongside all tasks, editing trajectories and scores. Project page: this https URL

---


### 226. [WeMM-Video: Pushing the Frontiers of Open-Source Omni-Modal Video Understanding](https://arxiv.org/abs/2611.26409)

**<font color=#1a73e8>作者：</font>** Changli Tang, Jie Yang, Tianyi Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding, particularly with accompanying audio, remains a central challenge in multimodal intelligence. In this report, we introduce \textbf{WeMM-Video}, a family of Chinese-English bilingual omni-modal foundation models spanning 2B, 4B, 9B, and 35B-A3B variants. Centering on joint audio-visual perception and reasoning, WeMM-Video unifies text, image, audio, and video processing within a hybrid-thinking paradigm, seamlessly supporting both a non-thinking instruct mode for fast, direct responses and a thinking mode for explicit step-by-step reasoning. The models are trained on a large-scale multimodal corpus of approximately 1.2 trillion tokens through progressive pre-training and a multi-stage post-training pipeline incorporating multi-teacher OPD, anti-repetition MrDPO, and specialist RL. Evaluated across more than 120 benchmarks, WeMM-Video demonstrates superior performance in omni-modal video understanding and reasoning, while maintaining highly competitive capabilities across general audio, silent video, image, and text tasks. Specifically, in omni-modal video evaluations, our flagship WeMM-Video-35B-A3B establishes a new open-source state of the art, substantially outperforming proprietary models such as Qwen3.5-Omni-Flash and Seed2.0-Mini-0428 while narrowing the gap with the strong Gemini-3.0-Flash, and our compact WeMM-Video-9B surpasses the larger open-source Qwen3-Omni-30B-A3B-Instruct. We publicly release the WeMM-Video family along with our evaluation and reproduction pipeline to foster further research and development in the open-source community.

---


### 227. [Sequential Anytime Valid Tests for Efficient Inference-Time Alignment](https://arxiv.org/abs/2611.26413)

**<font color=#1a73e8>作者：</font>** Vishesh Kumar Singh, Sayak Ray Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time alignment methods, such as Best-of-N (BoN), improve language model outputs by generating multiple candidates per prompt and selecting among them using a reward model. Much of this cost is wasted: a fixed budget is applied to every prompt, although the computation required by prompts varies widely. Adaptive methods halt once sampled answers appear settled, but their thresholds are tuned heuristics with no statistical control over early-stopping errors. We instead seek an anytime-valid stopping rule that takes an error tolerance $\alpha$ as input and halts only once an answer is certified to hold a majority ($\theta_a > 1/2$) under the generator's distribution. We aggregate candidates by final answer with a reward-weighted self-consistency (RWSC) score and treat stopping as a sequential test over the resulting clusters. Applying Wald's sequential probability ratio test to these clusters yields SPRT-RWSC, which performs well empirically, but its guarantee fails because the leading answer shifts during sampling, and the run is continuously monitored. Our main contribution, e-RWSC, replaces Wald's test with a betting supermartingale (an e-process) for every answer the policy produces, bounding the probability of ever certifying a non-dominant answer by $\alpha$, uniformly over time and across all answers. The RWSC scores drive the bets, so they affect only how quickly a dominant answer $a^\star$ is certified, not validity; certification takes $O(\log(1/\alpha)/d_{\mathrm{KL}}(\theta_{a^\star}\|1/2))$ samples. Experiments across several language models, datasets, and reward models confirm the predicted $1/d_{\mathrm{KL}}$ scaling of cost and show that accuracy improves over baselines at substantially lower token cost.

---


### 228. [ZeroVLN: Learning to Navigate without Supervised Fine-Tuning of the VLM Brain](https://arxiv.org/abs/2611.26414)

**<font color=#1a73e8>作者：</font>** Zixuan Huang, Yang Zhou, Guli Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Representative vision-language navigation (VLN) methods typically couple a vision-language model (VLM) brain with a learnable action head and fine-tune the VLM brain on navigation-domain data to predict geometric goals. However, such adaptation can substantially alter base VLM weights and degrade general visual capabilities. We introduce ZeroVLN, a slow-fast navigation framework that achieves effective navigation with zero navigation-domain SFT of the VLM brain. Rather than teaching the brain to predict geometric goals, we equip it with a semantic tool-calling interface for conveying movement decisions to an action expert in natural language. We first adapt the action expert to carry out these movement requests, then jointly improve the brain's movement decisions and the action expert's continuous execution through closed-loop reinforcement learning (RL). Trained on the same navigation episodes, ZeroVLN substantially outperforms representative SFT-based hierarchical VLN methods on standard VLN-CE (continuous environments) benchmarks, while inducing only minor changes to the brain's weights and largely preserving its general capabilities. To our knowledge, ZeroVLN is the first slow-fast VLN framework with zero navigation-domain SFT of the VLM brain, and the first to jointly optimize its slow and fast policies through closed-loop agentic RL in VLN-CE.

---


### 229. [Reasoning-Trace Analysis Using Large Language Models for Interpretable Q-Matrix Construction](https://arxiv.org/abs/2611.26422)

**<font color=#1a73e8>作者：</font>** Jihong Zhang, Zijing Jin, Mingfeng Xue  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate Q-matrices for diagnostic classification models that approximate expert specifications, but evaluations have focused on the final matrices, leaving the basis of individual item-attribute assignments unexamined. This opacity limits the responsible use of AI in measurement. We propose Reasoning-Trace Analysis (RTA), a framework in which an LLM generates attribute-labeled reasoning steps through chain-of-thought (CoT) prompting and these steps are analyzed to reconstruct, compare, and inspect each assignment. RTA is intended to supplement expert review and empirical validation. In a simulation study with perturbed fraction subtraction items, four LLMs recovered the required attributes and withheld attributes the items did not require. In an empirical study with 11 fraction subtraction items, responses from 536 examinees, four LLMs, up to three temperatures, and 100 replications per condition, CoT-derived Q-matrices overlapped substantially with the reference Q-matrix (mean overlap .809) but less than directly generated Q-matrices (.877), and they varied more across replications. Inspection of the traces linked disagreements to item-type coding, labeling rules, and how operations were expressed as steps. Q-matrices with similar overlap differed in fit to examinee responses. RTA provides inspectable evidence that matrix-level agreement and fit do not.

---


### 230. [Seer: Guiding Small Deep-Research Agents with Shared Decision Models](https://arxiv.org/abs/2611.26423)

**<font color=#1a73e8>作者：</font>** Yuhao Zhou, Yang Zhou, Yuanxi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep-research agents repeatedly decide what to search, read, and verify, often using large cloud-hosted language models for action proposal. However, privacy and local control motivate running agents on users' devices, where limited memory and compute favor smaller models and complicate on-device training. Yet inference-time guidance faces three obstacles: exploring alternatives through real execution adds tool calls, prompted self-evaluation is bounded by the agent's judgment, and model-specific guidance risks repeated adaptation costs. We introduce Seer, an inference-time framework providing local guidance that separates the agent's action proposal from learned consequence prediction and value estimation. From a shared corpus of real research trajectories, we train two models: a tool-response simulator on observed call--response pairs and a value estimator on histories labeled with discounted terminal correctness. The simulator and estimator are trained offline and reused across agents without further training. Moreover, Seer executes only the selected action and adds only real tool responses to the committed history, avoiding tool calls on discarded candidates at additional inference cost. Across multiple deep-research benchmarks, Seer substantially improves agent performance for different language models. For instance, GAIA accuracy rises from 13.6% to 41.7% for Qwen3.5-4B and from 22.3% to 50.5% for Qwen3.5-9B. Furthermore, our analyses suggest that broader candidate coverage can compensate for imperfect simulation, while prediction and scoring errors limit the benefits of wider imagined search. These findings highlight the potential of reusable models for prediction and evaluation to strengthen small research agents through extra local computation without the real execution of the discarded candidates.

---


### 231. [MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management](https://arxiv.org/abs/2611.26427)

**<font color=#1a73e8>作者：</font>** Xuyang Liu, Chenwen Lu, Junxi Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term agents accumulate large external memory stores as interactions unfold, increasing the costs of storage, retrieval, and response generation. Efficiency is constrained by two coupled factors: a growing record count increases retrieval overhead, while longer retrieved contexts increase prefill computation and decoding-time attention costs. Existing methods prune or consolidate records, but pruning can discard useful evidence, whereas consolidation may produce fewer yet longer retrieval units. We introduce MemFolder, a structure-guided memory folding framework that sequentially reduces record count and context length. The framework comprises two core components that share memory groups, using cross-record structure to guide both evidence consolidation and compact representation. RecordFolder grounds entity mentions, progressively selects representative yet complementary anchors, and combines semantic and entity affinity with temporal chaining to consolidate compatible records into fewer retrieval units. ContextFolder encodes the original records within these groups into compact text and uses verification feedback to revise encodings when key facts cannot be recovered. Experiments on the three text-based memory benchmarks LoCoMo, PersonaMem, and LongMemEval and the two multimodal benchmarks M3-Bench-web and M3-Bench-robot demonstrate the strong performance of our methods. Notably, on Mem0, RecordFolder retains 99.0% of the original average performance across the three text-based benchmarks with 50% fewer records, exceeding the strongest baseline by 1.9 percentage points in performance retention. Combined with ContextFolder, existing record compression methods further shorten their output records while retaining most of their performance.

---


### 232. [Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2611.26438)

**<font color=#1a73e8>作者：</font>** Zixuan Liu, Hashem Haghbayan, Zizhan Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented vision-language-action (VLA) models enable efficient test-time adaptation by leveraging expert demonstrations as additional context without updating model parameters. However, even when retrieved demonstrations are relevant to the current task, the VLA may fail to effectively utilize the retrieved information, ultimately leading to task failure. To address this challenge, we propose R2-VLA, a risk-controlled retrieval-augmented VLA framework that enables reliable test-time adaptation by satisfying a user-specified task success rate requirement with minimal expert assistance. Specifically, R2-VLA learns an uncertainty predictor that estimates the uncertainty of the VLA's predicted actions given the retrieved demonstrations, guiding when to act autonomously or request expert assistance. We further introduce a task-level risk-control procedure that calibrates the uncertainty threshold to satisfy a user-specified task-failure risk requirement. Moreover, R2-VLA continually incorporates expert corrections into its retrieval memory to improve future adaptation while preserving the prescribed task-level risk guarantee. Experiments across three VLA backbones and four LIBERO benchmark suites demonstrate that R2-VLA improves average task success by 9.2--11.2 percentage points, achieving the desired target with fewer expert requests. These results highlight the effectiveness of connecting the usefulness of retrieved demonstrations with task-level risk control to enable successful robotic manipulation.

---


### 233. [A CPU Inside an LLM: Zero-Gradient Compilation of Exact Circuits into Pretrained Weights](https://arxiv.org/abs/2611.26450)

**<font color=#1a73e8>作者：</font>** Tanmay Sah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pretrained language models (LMs) remain unreliable on exact multi-digit arithmetic without gradient fine-tuning or external tool interpreters. We introduce closed-form, zero-gradient circuit-grafting primitives that compile deterministic computation directly into pretrained LM weights using zero training examples and zero runtime hooks, while bounding per-layer normalization drift and preserving natural-language (NL) competence. Our construction combines three analytical mechanisms: (1) two-layer Mellin-GLU quadrature over bias-free SwiGLU/GeGLU layers, turning unknown per-token RMSNorm scaling into translation along a log-spaced gate grid ($>250\times$ dynamic range) with IEEE 754 error bounds; (2) cross-token scale cancellation via signed Chebyshev Indefinite-RoPE self-sink attention and memoryless SiLU-antisymmetric GatedDeltaNet shifts; and (3) axis-aligned width extension ($d \to d+K$) with $\sqrt{d/(d+K)}$ norm compensation, Base-1000 canonical BPE emission, and differential $(+254,-256)$ tied unembeddings. An automated 5-stage compiler synthesizes 4-8 digit signed $\{+,-,\times\}$ circuits in constant $\mathsf{TC}^0$ depth alongside 3-literal Boolean (100%, $N=1{,}728$; plus 42-layer Gemma 4 E4B audits) and 5-bit Majority/Parity (100%) circuits. On 6-digit arithmetic ($N=1{,}200$, BF16), IBM Granite 4.2 3B (1.07M-1.33M active non-zeros, $\le 0.036\%$) and Alibaba Qwen 3.5 4B (2.25M-2.39M non-zeros, $\le 0.057\%$) reach 99.17% and 100.00% ALU-prefix accuracy (100% with an FP32 sidecar) and 98%-100% mid-sentence resumption, outperforming 12.8K-sample LoRA (42.2% / 61.7%, 0% inline continuation). A factorized block-sparse sidecar holds A100 memory at 7.89 / 10.65 GiB (4.60 / 8.14 GiB under INT8/INT4 + FP32 sidecar) while passing all 14/14 pre-registered $>2$K-token Tango splits ($N=4{,}392$; 0/11,134 OOD triggers).

---


### 234. [Introducing ReTiNA-Cinema: Real-Time Neuro-Augmented Cinema via Generative AI](https://arxiv.org/abs/2611.26469)

**<font color=#1a73e8>作者：</font>** Antoine Bellemare-Pepin, Philipp Thölke, Yann Harel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (AI) is currently revolutionizing content creation across various media. Between those who fear it will replace human creativity and those who regard it solely as a tool, many in the creative industries are beginning to view generative AI as a collaborator. Yet interaction with these systems often relies on discrete, turn-based prompting that can interrupt flow and constrain expression to symbolic text. We explore physiological signals as a source of continuous adaptation without explicit commands, as a path toward embodied co-creation. This paper presents ReTiNA-Cinema, a methodological proof-of-concept that integrates electroencephalography (EEG) with generative AI to enable physiologically guided visual modulation of cinematic material. By linking physiological activity to the evolving appearance of a film, the system provides a basis for exploring embodied sense-making, in which viewers' bodily responses contribute to shaping the sensory experience through which they interpret the unfolding scenes. The system combines real-time EEG signal processing with a generative AI pipeline based on Stable Diffusion Turbo for frame-level image transformation. Single-user and two-user configurations map EEG-derived features to prompt selection and transformation strength. ReTiNA-Cinema offers a framework for exploring how the physiology of viewers might influence a film's visual presentation, extending the possibilities for participation in cinematic experiences and storytelling. This system raises questions about the effects on engagement, perceived agency, and emotional response, which remain open to future empirical study. Video illustrations: this https URL and implementation: this https URL.

---


### 235. [A new algorithmic approach for finding flat minima: critically damped Polyak stepsizes](https://arxiv.org/abs/2611.26475)

**<font color=#1a73e8>作者：</font>** Francesco Caporali, Jason M. Altschuler, Boris Hanin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a new adaptive stepsize rule that biases gradient descent toward flatter minima in both theory and practice, and establish the first uniform-in-time guarantees for both sharpness and loss reduction for a broad class of locally quadratic objectives. Our critically damped Polyak (CDP) stepsizes multiply the classical Polyak rule by $4$ and a mild damping factor. The factor $4$ is critical in that it produces equioscillations around the manifold of minimizers $\mathcal{M}$ to leading order. Damping provably drives convergence to $\mathcal{M}$. CDP thus operates at the edge of stability by adapting its stepsizes to local curvature. Once the loss is small, its projected iterates follow gradient descent on $\log{\lambda_1(\nabla^2 \mathcal{L})}$ along $\mathcal{M}$ to leading order, paralleling the flatness bias of normalized gradient descent (Arora et al., 2022). Unlike normalized gradient descent, CDP step lengths shrink with the distance to $\mathcal{M}$, enabling convergence to an interpolating solution that locally minimizes sharpness at finite learning rate. We establish our theory for a broad class of non-negative losses with locally quadratic Morse-Bott structure near $\mathcal{M}$, capturing regular interpolation regimes in smooth overparameterized neural networks. Empirically, CDP stepsizes produce a flattening effect similar to that of Sharpness-Aware Minimization (SAM, Foret et al., 2021), reducing sharpness even in settings beyond our theory, including nonlinear teacher-student networks and fine-tuning of pre-trained LLMs.

---


### 236. [Multimodal Error Detection in Chest X-ray Reports: A Large Language Model Reading Image Evidence](https://arxiv.org/abs/2611.26492)

**<font color=#1a73e8>作者：</font>** Yanda Cheng, Bo Wen, Yuhao Lu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rad-Linter checks chest X-ray reports against image-derived evidence to flag potential errors for review. A pretrained image classifier supplies scores for nine pathologies, and a 1.5B-parameter language model, fine-tuned with LoRA on 1,816 examples, checks their consistency with the report. We compare it with a keyword-and-negation rule baseline given the same reports and scores. Evaluation uses controlled report-score pairings from OpenI, with consistency labels derived from automatic report labels and score thresholds. Each counterfactual quad crosses two real reports with two real score vectors from other patients, creating two consistent and two inconsistent pairs. Every report and score vector occurs in both conditions, so either input alone permits only 50% accuracy. On 131 quads, Rad-Linter achieves 98.5% pair accuracy versus 80.5% for the rule baseline, and classifies all four pairs correctly in 94.4% of quads versus 56.5%. The checkers perform similarly on omission items, including unmentioned and negated findings; larger differences occur on the remaining item types, which require interpreting how findings are described. The same language model without fine-tuning remains near 50% accuracy. On a second set of 181 quads that also includes reports on which the automatic labelers disagree, pair accuracy is 93.4% versus 75.3%. These controlled results show that, given the same image-derived scores, a trained language model detects report-score inconsistencies more accurately than the tested rule baseline, with the advantage concentrated in interpreting how findings are worded.

---


### 237. [GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers](https://arxiv.org/abs/2611.26509)

**<font color=#1a73e8>作者：</font>** Sahibzada Allahyar, Julia White, Dhruv Atreja 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models enable fast, confidence-aware decisions by scoring candidate answers in a single forward pass, without generating text or intermediate reasoning. Yet reasoning can substantially improve decision quality, raising the question of whether its benefits can be retained without the cost of generating it. We investigate this question with \textbf{GLiDE}, a family of decision models spanning 0.4B to 27B parameters.
Building on Qwen hybrid language models, GLiDE enables bidirectional interactions between the context, question, and candidate answers by removing causal masking from full-attention layers. To transfer reasoning capabilities into single-pass inference, we combine soft-target distillation from multiple teachers, including a reasoning model, with progressive post-training on diverse decision tasks. We further explore parameter-free recurrent depth to increase inference-time computation without generating tokens.
Across five model sizes, GLiDE lies on the performance--parameter Pareto frontier of the Hugging Face \DI{}, with each model outperforming evaluated alternatives of equal or smaller size. \dmtwo{} (27B) achieves a hidden-set score of 71.52, with an expected calibration error of 2.0\% and a median latency of 92.9\,ms on a single GPU. Further checkpoint averaging and parameter-free recurrent depth yield GLiDE~27B, which reaches 73.37 with an expected calibration error of 2.1\%.

---


### 238. [AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher](https://arxiv.org/abs/2611.26510)

**<font color=#1a73e8>作者：</font>** Guoxin Chen, Shuang Sun, Fanzhe Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task success alone does not specify which behaviors post-training should reinforce. Even successful teacher trajectories can contain unsupported assumptions, unproductive repetition, or superficial verification. We propose Skill-FT (Skill-Guided Fine-Tuning), which uses natural-language skills to suppress undesirable habits and elicit underrepresented effective behaviors during teacher rollouts, then fine-tunes a target model on the resulting trajectories. We introduce AutoMaster, an autonomous post-training system in which an LLM agent develops these interventions through trajectory analysis, skill design, data selection, and feedback from rollouts and target-model evaluation. Across Terminal, Search, and software engineering tasks with 4B and 9B target models, AutoMaster improves mean performance over Vanilla SFT on successful unguided teacher trajectories by 1.42-8.99 percentage points, with the teacher, task pool, training set size, and SFT recipe held fixed. Together with the ablations and trajectory analyses, these results suggest that behavioral shaping can make a fixed model a more effective teacher. We further find that retaining skill instructions during SFT yields higher mean performance than removing them across all six settings, despite their absence at evaluation and identical supervised outputs. These findings suggest that preserving skill context as part of a training demonstration can support better behavioral internalization.

---


### 239. [LLM GerryMandering: Separating Interactions from Additive Effects in LLM Audits](https://arxiv.org/abs/2611.26538)

**<font color=#1a73e8>作者：</font>** George Rahul, Ronit Jahilal, Bhaskara Hanuma Vedula 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intersectional bias arises when a model treats people who hold several marginalised identities at once differently from what their separate identities would predict. Auditing such intersectional subgroups remains a challenge: their number grows quadratically, and there is no agreed baseline for what independent attributes would predict. Without such a baseline, many existing audits flag a subgroup when it exceeds each attribute alone, a condition that attributes acting independently already satisfy. We test this standard criterion on 150 synthetic datasets built with no interaction. With the shuffle null, it flags 66.1 false subgroups per dataset on average, and at least one in every dataset. When we plant interactions of known size into these datasets, a repaired null lets the criterion recover only 32% of them. We introduce ADDIS (Additive Intersectional Screen), which fits an additive model over all attributes, scores each subgroup by its Additive Residual Distance (ARD) from that model's prediction, and tests it against a Freedman-Lane null. On our synthetic benchmark, ADDIS flags 0.09 false subgroups per dataset and recovers 84% of the same planted interactions. We then build IndiPersona, 10,000 synthetic Indian personas with six identity attributes, and audit 13 open language models. The standard criterion flags 7.1% of the 738 tested subgroups on average; ADDIS flags 3.0%. Gender identity crossed with sexual orientation is the largest pairing in every model, and counterfactual personas confirm it and additionally reveal a caste x class interaction in all but one model that the observational test lacked the data to detect. Much of what audits report as intersectional bias can thus arise from independent single-attribute effects alone, yet a small core of interactions survives.

---


### 240. [The Geometry of Lies: Knowledge and Persona Directions for Detecting Deception in Large Language Models](https://arxiv.org/abs/2611.26545)

**<font color=#1a73e8>作者：</font>** Md. Abdullah Al Zami, Suraiya Shanaz, Mahdi Hasan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear probes are the cheapest LLM lie detectors but often fail to transfer across kinds of lie. Label-free directions from honest and deceptive role-play are untested at 70B scale and on lies about knowledge, where a lie and an honest denial can be identical. We widen a published persona bank with roles that deny knowledge they have, plus honest counterparts. At each model's middle layer the resulting persona direction ranks lies across Liars' Bench better than single-dataset probes on three of its four models; it fails on Qwen, even when Qwen stays in role far more often. On Llama-3.3-70B-Instruct it beats directions from a random persona bank, but its gain over the published direction is within the range of random widenings. On lies about knowledge, persona directions mainly track a reply's wording: where lies and honest denials share their words, our three main contrasts stay inside the random-direction band on Llama and Qwen and reach only its edge on Gemma, though on Mistral one clears it. A knowledge direction contrasts questions the model can answer with ones nobody can, each followed by the same scripted denial. It separates lies from identical honest denials on two models and narrowly on a third, but not on the fourth; its other results partly depend on the benchmark's wording. On the Gender-Secret fine-tune it clears the band by a few hundredths on Llama and fails on Mistral. The sum of the two directions ranks lies better than a supervised probe at the same depth on all four models (on one, both near chance) but is level with the persona direction on Llama's average and behind that probe on held-out lies. More varied role-play questions do not help the persona direction on Liars' Bench.

---


### 241. [Text-Aware, Vision-Blind: How Multimodal Image Editing Systems Handle Unsafe Inputs](https://arxiv.org/abs/2611.26569)

**<font color=#1a73e8>作者：</font>** Ziqing Yang, Yixin Wu, Michael Backes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal image generation systems have made rapid progress and increasingly emphasize content safety. However, their safety mechanisms tend to rely on a single modality and lack joint consideration of both visual content and text prompts, particularly in instruction-guided image editing, where the uploaded image may itself carry risk. We thus introduce EditSafetyBench, a benchmark that measures system-level safety awareness of advanced image editing systems, containing 5,940 image-instruction pairs, covering safe and unsafe images across 11 risk categories and three edit intents. We then probe the benchmark dataset on four systems, including Gemini, GPT, Qwen API, and Qwen Local. Based on our evaluation, we observe a systematic text-vision safety mismatch: Gemini and GPT refuse 87.1\% and 81.6\% cases containing unsafe-intent editing prompts, while only refusing 24.2\% and 22.4\% cases with both unsafe images and neutral instructions. At the category level, most risks are considered inconsistently by different systems, e.g., GPT allows 70.4\% editing attempts of unsafe political content while Gemini only allows 34.8\%. Notably, sexual content shows the strongest visual sensitivity, likely benefiting from mature NSFW identification works. Our findings highlight the need for safety guardrails that jointly reason over both visual and textual modalities in image editing systems.

---


### 242. [Represented but misread: Post-training changes how language models read out what they represent](https://arxiv.org/abs/2611.26584)

**<font color=#1a73e8>作者：</font>** Jochen Laubrock  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Does post-training change what a language model represents, or how this representation is read out into an answer? We compared linear probes with the models' own answers, analyzed with signal detection theory, in six open-weight base models and their post-trained versions. For judgments of whether German texts were written by a human or an AI, probes and word n-gram classifiers separated the classes well, but the answers did not and often ordered the texts inversely. Post-training lowered the sensitivity of the answers on average ($\Delta d' = -0.34$ across model families; -0.29 across three prompts). It also changed the use of a stated base rate: Base models shifted their log-odds by less than the stated change in prior odds, most post-trained models by more. In two models with stage-wise checkpoints, the change occurred during supervised fine-tuning, model stitching implicated the early layers, and from mid-depth on internal states at positions after the text, not those of the text, transferred the change between checkpoints. Our corpora cannot be shared, so we add a case reproducible from public data, the truth of negated statements. Here, post-training acted in the opposite direction: Probes decoded truth at or near ceiling in every model, the answers of several base models did not use it, and post-training repaired them; by mid-depth the repair resided at the positions after the statement; below it, the representation of the statement contributed, strongly in one of four models. In a training study, adding 2,000 correctly labeled authorship judgments of news texts to otherwise identical fine-tuning data improved the answers on our newspaper and textbook corpora and inverted them on the chats, where they followed a news-trained probe of the base model. Post-training thus changed how a judgment is read out of what a model represents, and a small training signal can set its direction.

---


### 243. [Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language Models](https://arxiv.org/abs/2611.26590)

**<font color=#1a73e8>作者：</font>** Jiahao Huang, Jun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) integrate visual and textual information, but their outputs do not reveal internal concept representations. Global workspace theory (GWT) proposes that information is selected from parallel brain processes, integrated in a shared workspace, and made available to specialised processes. We introduce the Multimodal Concept Lens (MC-Lens), a multimodal Jacobian lens, to study these functions in VLM concept processing. Its vision encoder and language decoder lenses map intermediate states to a shared semantic space defined by the decoder's output vocabulary to compare concept accessibility across modalities. MC-Lens supports internal concept interventions to examine the role of accessed concepts in downstream computation. (i) Accessibility and selective access. Multimodal concept information is readable in intermediate states and selectively accessible as tasks require. We extend "readout carriers" from one name token to a token set to better capture and express concept information and support counterfactual experiments. (ii) Concepts in downstream computation. Counterfactual experiments show that accessed concept information participates in downstream computation and reasoning. (iii) Development of cross-modal alignment and selective access. We develop two J-space metrics tracking the development of cross-modal concept alignment more clearly than hidden state cosine in controlled VLM training. The experiment also shows that reliable selective access develops later than concept accessibility. (iv) Shared functions across models. Across VLM families and sizes, we find shared patterns of concept accessibility, query-dependent selectivity and cross-task intervention effects despite differences in internal organisation. These findings offer an experimental basis to study GWT in multimodal artificial systems and how it can guide cross-modal alignment improvements.

---


### 244. [Coda-DaVinci: Reimagining Video Generation with Code2Video](https://arxiv.org/abs/2611.26595)

**<font color=#1a73e8>作者：</font>** Yiyan Ji, Qixun Wang, Yang Shi 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Code2Video uses agent-authored 3D proxies to guide video generation, enabling explicit control over structure and dynamics. However, how to construct proxies and prompts for optimal downstream quality remains underexplored, as do the capabilities and limitations of this paradigm. Through controlled experiments and blinded human evaluation, we study proxy granularity, physics simulation, and prompting. The results reveal task-dependent trade-offs: coarse proxies favor natural motion, while medium-grained proxies favor consistency. Physics simulation and proxy-aligned prompting further improve average quality. Guided by these findings, we introduce Coda-DaVinci, a task-adaptive agentic framework for Code2Video generation that selects between proxy-guided and direct generation, adapts modeling granularity to each entity, and coordinates simulation with proxy-grounded prompting. Its multi-agent harness preserves scene assets and guides repairs through visual inspection and independent review. Experiments demonstrate leading instruction following on VTR and scene consistency on R2M, improved physical plausibility over direct generation, and higher visual realism than the compared Code2Video baselines. Long-video evaluations further show gains in event structure and consistency across successive interactions, while revealing limitations in transition stability and adherence to scene settings.

---


### 245. [SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research](https://arxiv.org/abs/2611.26601)

**<font color=#1a73e8>作者：</font>** Amine Lbath, Manan Suri, Aurelien Delaitre 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are scattered across papers, vendor reports and disclosures and are rarely comparable. We introduce a framework that rates these capabilities on an autonomy scale modeled on the levels of driving automation, and qualifies each claim by its correctness, its availability and the strength of its evidence. We use this framework to systematize the published evidence on LLM capability in vulnerability research. We find that agents discovered, validated, and patched vulnerabilities in real-world software without human intervention before the restricted frontier models of 2026, and that open-weight models subsequently attained comparable autonomy for discovery and validation. We then measure the consequences of evolving LLM security capabilities in a decade of public vulnerability records, advisories and exploitation data. In 2026 the number of disclosed vulnerabilities more than doubled, with an increasing share rated critical or high, and severe bugs that had survived a decade or more in widely used code were reported several times more often than before. Yet the time between the stages of a vulnerability's life, from report to fix and from disclosure to attack, has not shifted noticeably so far. We grade the mitigations proposed in the literature with an explicit rubric and draw guidance for each group of stakeholders from the best-supported ones.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 246. [An AI-Powered Multiverse Analysis of Empirical Finance Research: Evidence from Reused Natural Experiments](https://arxiv.org/abs/2611.25184)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ruijiang Gao, Steven Chong Xiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Empirical finance research often reuses natural experiments to study other outcomes, raising concerns about multiple testing and publication bias. We use AI agents to run a multiverse analysis of 324 papers that reuse 13 natural experiments. The agents rebuild the data, reproduce each paper's main estimate and re-estimate it across grids totaling 62,409 estimated defensible specifications. Based on the reproductions and the specification grids, we develop measures of empirical robustness. We reproduce 42% of the main estimates of claims with a signed effect under the papers' own specifications. Across all defensible specifications, on average 25% keep the published sign and have $p < 0.10$. Across experiments, claims based on regression discontinuity are more robust than difference-in-differences claims. Within experiments, claims about first-order effects, claims with larger published $t$-statistics, claims whose authors' data or code we find, claims in top journals, and claims with fewer earlier papers on the same experiment are more robust. Claims on experiments that more papers reuse are not less robust on average. Our findings quantify how much published claims depend on analysis choices, thereby showing that large-scale multiverse analysis becomes feasible with agentic coding.

---


### 247. [VoxForge: A Unified Foundation Model for Dense 3D Features Across MRI, CT and PET](https://arxiv.org/abs/2611.25309)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rushil Anirudh, Jayaraman J. Thiagarajan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A unified 3D medical foundation model promises reusable, frozen features that serve a wide variety of tasks such as segmentation, classification and registration on MRI, CT and PET as well as specialist models do. Generalist models still need separate backbones for localized and global tasks, specialist models are confined to a single modality, with the concern that spanning modalities under-emphasizes fine anatomy, and both typically rely on end-to-end fine-tuning to be competitive. We present VoxForge, a single encoder that integrates recent advances in 3D architecture, self-distillation and cross-modal curricula to learn transferable features from permissively licensed MRI and CT volumes. We evaluate it strictly frozen, the test a reusable foundation model must pass, against state-of-the-art generalist and specialist models on segmentation, classification and registration across MRI and CT, and on PET, which it never sees. VoxForge has the best or tied-best average rank in every task group, serves localized and global tasks across modalities at the level of state-of-the-art specialists, and is extremely label-efficient, matching top-performing models on TotalSegmentator CT with a tenth of the labels.

---


### 248. [Falsifiable Compositional Reasoning in Time Series Forecasting](https://arxiv.org/abs/2611.25388)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hao Xue  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series foundation models as well as the language-guided analytical agents achieve strong accuracy on standard chronological benchmarks. However, models that rank highest on historical validation splits often degrade across non-stationary regime transitions. We hypothesise that this gap arises from using historical backtesting as an open-ended search and model-selection objective instead of using it to test pre-specified compositional assumptions. Real-world time series are generated by recurring latent primitives that co-move within finite historical windows. Under strong historical co-movement, chronological holdout error cannot separate predictors that learn invariant couplings among primitives from predictors that fit transient historical correlations. Searching over large pools of architectures, hyperparameters, or chain-of-thought rules further biases selection toward historical shortcuts. Through theoretical analysis and diagnostic experiments on a controlled multi-primitive benchmark and German day-ahead electricity prices, we show that expanding validation search fails to improve out-of-regime accuracy, and that decomposing primitives without an ex-ante falsification test still breaks down when residual correlations shift. Hence, we propose formulating time series forecasting and reasoning around falsifiable compositional hypotheses that combine neural primitive encoders, explicit coupling constraints, and training-calibrated falsification tests.

---


### 249. [Antom 3-in-1 Transformer: A Payment Foundation Model](https://arxiv.org/abs/2611.25403)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Weiyu Han, Haoyu Jiang, Jie Sheng 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We report the development of Antom 3-in-1 Transformer, a payment foundation model that integrates sequence, tabular, and graph representations for payment risk detection. The model contains approximately 7B parameters, with approximately 1.7B activated per task route. Antom 3-in-1 Transformer is pretrained to learn reusable behavioral and relational representations, primarily on Ant International's internal payment data. In a cross-business transfer experiment, pretraining improves the target business metric by 34.5% over the same architecture trained from scratch. With only 25% of the training labels, the pretrained model outperforms the full-label scratch baseline in Average Precision (AP) and Recall@0.5% on different merchant domains. In a four-month online experiment on Ant International's billion-scale payment platform, the model reduced the overall loss rate by 37.88% relative to XGB-Online.

---


### 250. [CANDOR: Contrastive Self-Denoising Rewards for Label-Free Text-to-Image Post-Training](https://arxiv.org/abs/2611.25457)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junhyeok Lee, Byung-Hoon Kim, Kyu Sung Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training text-to-image generators with reinforcement learning usually relies on external reward models that need annotated preferences or auxiliary evaluators and are prone to reward hacking. We show that the generator's own denoising accuracy, used by a recent intrinsic reward, is a poor proxy for prompt fidelity. Within a same-prompt group, this absolute self-confidence is dominated by image complexity and ranks correct samples above incorrect ones near chance. We introduce CANDOR (Contrastive Alignment from Null-referenced Denoising lOg-Ratio), the log-ratio of unconditional to conditional denoising errors under shared noise probes, which measures how much the prompt helps the model denoise its own sample. It cancels prompt-independent difficulty that scales both errors and ranks the better of two same-prompt samples higher in 60% and 63% of pairs on compositional generation and text rendering. As the only Flow-GRPO reward for a flow-matching model, CANDOR improves text rendering, aesthetic and human-preference scores over the base model and a prior absolute self-confidence reward, with text-rendering and preference gains that stronger classifier-free guidance does not reproduce. On public Flow-GRPO adapters trained on external rewards, CANDOR further raises PickScore and ImageReward, so it can complement those rewards. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
