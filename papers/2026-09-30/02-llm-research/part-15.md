# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**701-750**（第 15/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | **701-750** | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 701. [Unified Trajectory Matching Policy Optimization: Diverse T2I Generation and VLA Generalization](https://arxiv.org/abs/2609.34688)

**<font color=#1a73e8>作者：</font>** Zhiyuan Ma, Jiaming Li, Lingzhen Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reward-maximizing reinforcement learning (RL) is widely used to post-train stochastic diffusion and flow policies for text-to-image (T2I) generation. However, reward-maximizing RL causes policy mode collapse even under reference KL or entropy regularization, reducing the policy to a single high-reward mode. In T2I, this produces similar images and reward hacking. When extended to vision-language-action (VLA) models, the same collapse removes alternative successful strategies and weakens task and scene generalization. To address this limitation, we introduce Unified Trajectory Matching Policy Optimization (Uni-TMPO), a unified RL post-training framework for diffusion and flow policies. First, Uni-TMPO converts standardized rewards into a target distribution within each trajectory group and derives the policy distribution from trajectory log probabilities. Then, forward Kullback-Leibler optimization matches the two distributions instead of maximizing expected reward. A progress-conditioned coarse-to-fine scheduler efficiently constructs T2I trajectories. Within the unified framework, feedback-conditioned sampling uses updated observations to construct VLA trajectories. Extensive experiments show that Uni-TMPO achieves higher T2I rewards and VLA ID success rates than the strongest baselines. More importantly, it achieves the best T2I reward-diversity-efficiency trade-off and VLA generalization to held-out tasks and scenes, while real-robot evaluation demonstrates the value of multiple action strategies when the higher-reward target is blocked.

---


### 702. [Using LLMs to Detect LLM-Generated Texts: A Cross-Generation Analysis](https://arxiv.org/abs/2609.34691)

**<font color=#1a73e8>作者：</font>** Haiyue Yuan, Jie Guo, Weidong Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated detection of LLM-generated texts (LGTs) is critical, yet dedicated detectors often struggle to generalize across domains and models. While general-purpose LLMs offer flexible zero-shot authorship classification with explanatory rationale, their detection behavior, especially regarding self-detection versus cross-detection across model generations, remains poorly understood. We systematically evaluate 15 LLMs spanning three model generations as both generators and detectors. Using a benchmark of 1,000 human-written texts and 15,000 LGTs (1,000 per model), we collected over 233,000 binary classifications alongside natural-language explanations. Our results reveal that detection efficacy is primarily driven by detector capability rather than generator provenance, although outputs from newer generators remain notably harder to detect. Crucially, statistical comparisons show no systematic advantage or disadvantage for self-detection across models. Error analysis further exposes generational bias shifts: first-generation detectors under-detect LGTs (high false-negative rates), second-generation detectors over-flag human texts (high false-positive rates), and the latest models achieve balanced trade-offs. Finally, we highlight significant inconsistencies in how different LLMs apply textual cues to justify their decisions. Code: this https URL.

---


### 703. [FromPitch2Board: Benchmarking LLM Agents in Long-Horizon Football Management](https://arxiv.org/abs/2609.34710)

**<font color=#1a73e8>作者：</font>** Peiyu Zang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agent benchmarks typically report how far an agent progresses, but do not identify whether its performance comes from the foundation model, scaffold, responsibility scope, match-control granularity, or horizon. We introduce FromPitch2Board, a deterministic football-management benchmark that studies five configurable factors through controlled comparisons on a single simulator, using paired seeds and a frozen calibration. We evaluate four foundation models and four agent scaffolds. In the Model Track, Coach points Z-scores span 0.19, while Manager points Z-scores span 0.68, with GPT-5.6 showing a sharp rise in passivity under responsibility expansion. Its responsibility ladder rises from 46.1 to 58.1 points with recruitment, then falls to 46.8 under full management, localizing the regression to the final responsibility boundary. Across that boundary, its skipped-decision rate rises from 1.1% to 57.9%. Within the Flash-Pro pair crossed across every scaffold, scaffold choice changes Manager points Z-scores by up to 0.48 relative to the fixed stateless scaffold. The 3Y cohort shows a directional reversal in mean ranking between years one and three, while a selected Claude Code+Pro configuration peaks in year three and remains below that peak, showing that responsibility scope and horizon expose behavior changes that a single headline score conceals.

---


### 704. [RSI-Router: Evolving Subtask-Level LLM Routing and Skills for Cost-Efficient Agents](https://arxiv.org/abs/2609.34712)

**<font color=#1a73e8>作者：</font>** Hao Li, Hangfan Zhang, Zhiyao Cui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Practical deployment of large language model (LLM) agents requires strong task performance at affordable inference cost. For long-horizon agentic tasks, this performance-cost trade-off can be improved through within-task large-small model collaboration, as smaller models can handle some stages even when they cannot solve the full task. In this paper, we introduce RSI-router, a routing framework that constructs subtask-level model assignments and model-specific skills through recursive self-improvement over accumulated experience. Each iteration consists of four stages: Subtask Mining derives subtask definitions and identification rules from training trajectories; Routing Strategy Evolution proposes and evaluates diverse model assignments; Model-Specific Skill Evolution compares routed and large-model-only trajectories to diagnose failures and develop reusable execution skills; and Pareto-Optimal Router Selection updates the Pareto population using historical and newly generated routers while retaining dominated routers as experience for subsequent evolution. Routing between DeepSeek-V4.1-Flash and Qwen3.5-9B, RSI-router consistently surpasses the DeepSeek-only baseline at roughly half the inference cost (48.3%) across five agentic benchmarks. In particular, on ALFWorld, ScienceWorld, and WebShop, it cuts inference cost by 74.7-82.2% while simultaneously improving performance; on Terminal-Bench 2.0, it achieves a 16.7% relative performance gain at 18.0% lower cost. Moreover, RSI-router establishes a stronger performance--cost Pareto frontier than 9 routing methods.

---


### 705. [ReMCTS: Reflection-Enhanced Monte Carlo Tree Search for Code Generation](https://arxiv.org/abs/2609.34717)

**<font color=#1a73e8>作者：</font>** Huifei Wang, Xinying Huang, Yiheng Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-weight large language models (LLMs) can generate function-level programs from natural-language prompts, but plausible candidates still fail on hidden semantics and repeat mistakes across repair attempts. We present ReMCTS, an execution-grounded, memory-augmented, LLM-guided MCTS-style search framework. It organizes program candidates as tree states, retains branch-local debugging context, retrieves failure experience across branches, and distinguishes failed checks from unavailable evidence. On HumanEval and MBPP-Sanitized, visible-test ReMCTS improves over direct generation in 8 of 10 model-dataset pairs under held-out evaluation, whereas proxy-only search is less stable. Controlled tree-search, sampling, repair, and memory ablations characterize the source and limits of these gains. A 30-task HumanEval-X C++ pilot further demonstrates compatibility with compiler-backed execution, but does not constitute a broad multilingual evaluation.

---


### 706. [Quality Determines Direction, Length Shapes Magnitude: Length Control for Open-Ended Reinforcement Learning](https://arxiv.org/abs/2609.34718)

**<font color=#1a73e8>作者：</font>** Zijun Weng, Zhongan Bi, Xuanang Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) changes not only what language models say, but also how much they say, often increasing response length at the cost of token efficiency. Controlling this length growth is particularly challenging in open-ended RL because (i) response length is entangled with quality, (ii) open-ended tasks lack a natural success boundary for deciding when efficiency should be prioritized, and (iii) dense, graded rewards often yield small within-group quality margins, making quality-induced advantages especially sensitive to reward-level length shaping, which can perturb their magnitudes and even reverse their signs. We therefore adopt an asymmetric principle: quality should determine the direction of reinforcement, while length should only shape its magnitude. We instantiate this principle with Quality-Gated Length Advantage Shaping (QGLAS), which first computes advantages from quality rewards alone, then adds bounded bonuses only to shorter positive-advantage responses, leaving all other advantages unchanged. The bonus strength is further adapted to within-group quality separation, allowing conciseness to matter more when quality-favored responses are similar and less when their quality differences are clear. Across different model families, open-ended benchmarks, and reward sources, QGLAS consistently achieves a stronger quality--length trade-off than representative baselines. At approximately 30% compression, QGLAS retains 98.4--102.0% of the macro-average quality gains achieved by quality-only RL over the base model, compared with 68.3--75.5% for these baselines at comparable compression.

---


### 707. [SeLMRoute: Probabilistic Semantic Evidence for Large Language Model Routing](https://arxiv.org/abs/2609.34736)

**<font color=#1a73e8>作者：</font>** Vasilis Perifanis, Nikolaos Pavlidis, Symeon Symeonidis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) routing aims to select the most suitable model for each incoming query. Most existing routers learn this decision directly from query embeddings, model representations, preference data, or clusters of similar examples. Such approaches can be effective, yet the representation used for routing rarely states what a query actually requires. We introduce SeLMRoute, a routing framework that separates the extraction of candidate-independent semantic evidence from the learning of candidate performance and the application of deployment objectives. A decision model first evaluates a set of interpretable questions about the query, such as its reasoning requirements and use of external knowledge, with each judgment retained as a probability distribution. The resulting probabilistic semantic state is used by a lightweight supervised router to estimate candidate model performance. Routing objectives are applied after performance estimation, which allows the same semantic state to support performance-oriented and cost-aware decisions. On the LLMRouterBench (15 datasets, 20 candidate models, 11,481 queries), SeLMRoute achieves an average accuracy of $72.08\% \pm 0.45$, while grouped five-fold out-of-fold evaluation reaches $72.64\%$, compared with $69.23\%$ for the strongest fixed candidate. The representation achieves the highest mean performance among the evaluated semantic, dense, lexical, and domain-level representations. In a separate 13-model performance-cost setting, SeLMRoute improves performance in all five grouped splits, with a mean PerfGain of $2.66\%$. Our code is available at this https URL.

---


### 708. [Beyond Token Alignment: Event Completion for Cross-Tokenizer On-Policy Distillation](https://arxiv.org/abs/2609.34738)

**<font color=#1a73e8>作者：</font>** Jiacheng Liu, Jingwei Song, Qituan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) transfers knowledge between language models through teacher supervision on student-generated trajectories. With different tokenizers, a single teacher token may require multiple student tokens to generate, creating intermediate states where the event is entered but not yet completed. Existing cross-tokenizer methods align tokens or text spans to construct comparable prediction targets. We study a complementary problem after partial generation: once the student produces a prefix of a teacher token, multiple next tokens may complete the same remaining bytes, but the teacher only specifies the required completion rather than how probability should be divided among these valid continuations. We introduce Event-Set Completion Distillation (ESCD), which complements cross-tokenizer probability alignment with completion-set supervision. ESCD aggregates prefix-related teacher events and supervises the total probability of byte-compatible one-step student completions, avoiding tokenizer-dependent probability splits among individual tokens. The method reuses student trajectories and predictions, requiring neither additional rollouts nor changes to the student vocabulary. Experiments demonstrate consistent gains in mathematics, code, and scientific reasoning across model families and tokenizers, extending to large-scale MoE distillation from a 1T teacher to a 35B student. Local analyses show that retaining completion sets better matches the reference supervision, while one-step completion covers over 99% of observed compatible teacher mass after partial event entry in the studied tokenizer pairs. These findings support event entry and event completion as complementary supervision targets for cross-tokenizer knowledge transfer. Code will be released on GitHub.

---


### 709. [Do Emotion Concepts Generalize Across Sources, Modalities, and Architectures in Vision-Language Models?](https://arxiv.org/abs/2609.34742)

**<font color=#1a73e8>作者：</font>** Bohao Xing, Xin Liu, Kaishen Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent studies suggest that large language models encode emotion concepts as structured internal representations, but most existing work focuses on text and a single architecture. Therefore, we ask, do emotion concepts generalize across sources, modalities, and architectures in vision--language models (VLMs)? To address this, we construct CMES (Cross-Modal Emotion Stimuli), a multi-source collection of emotion-conditioned stories, real facial expressions, synthetic portraits, and synthetic emotion-evoking scenes. For each stimulus source, we extract a separate set of six Ekman emotion vectors from each of three VLMs. We report four main findings as follows: 1) Image-derived emotion vectors form a low-dimensional geometry similar to that of text-derived vectors. Valence is relatively stable across sources, while arousal varies more. 2) Text- and image-derived emotion vectors have modest cosine similarity but still show held-out cross-modal correspondence. Text-derived vectors can also steer image interpretation. 3) Cross-architecture correspondence remains even when native cosine is near zero. Transformations estimated from generic ImageNet activations recover both correspondence and causal transfer without using the six emotion vectors or their labels. 4) After aligning representations across architectures, we construct a shared emotion subspace that preserves affective geometry and selective steering effects. The corresponding consensus emotion vectors also generalize to a held-out fourth architecture at two model sizes. These results suggest that emotion representations can share relational structure and causal effects across sources, modalities, and architectures, even when individual vector directions differ.

---


### 710. [No Pain, More Gain: Iterative Merging for Effective Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2609.34745)

**<font color=#1a73e8>作者：</font>** Seonghyeon Kim, Chaeyun Jang, Noah Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) combines independently developed domain teachers into a single student by distilling their predictions on student-generated samples. We study a setting where teachers share a reference model but undergo different post-training procedures, and find that MOPD can struggle to recover some teacher capabilities. Because distillation occurs on student-generated prefixes, the student initialization can strongly affect subsequent recovery. However, initial benchmark performance is not a reliable predictor of a good MOPD initialization. For example, merge initialization can start below SFT warm-up yet finish higher after MOPD. We further find that effective merging depends on both the relative teacher contributions and the overall merge scale, with some strong configurations lying outside the simplex of convex parameter averaging. Thus, selecting a good merge initialization requires evaluating not only its immediate performance but also the learning it enables under MOPD, making one-shot coefficient search difficult. We propose Iterative Merging for MOPD (IM-MOPD), which starts from a uniform merge and progressively adds task-vector increments for under-recovered domains during distillation. In a 5-domain setting, IM-MOPD achieves higher average normalized recovery than MOPD with either uniform merge initialization or SFT warm-up, showing that effective teacher contributions can be determined progressively during training.

---


### 711. [Draft-KV: Learning Useful Latent Communication Between Language Models](https://arxiv.org/abs/2609.34754)

**<font color=#1a73e8>作者：</font>** Linquan Wu, Shichang Meng, Tianxiang Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent communication passes internal states between language models instead of decoded text, but higher receiver accuracy does not show that the receiver used the message content. Across five method-dataset pairs, replacing each message with one from an unrelated question changes accuracy by at most 0.60 points, even when communication adds 15.44 points over the receiver alone. Thus the interface can supply the gain while making the sharer dispensable. Draft-KV instead sends the key-value states formed while the sharer drafts an answer to the current question. Linear projections place these states in a side memory read through a gated attention branch, and progressive training moves from message reconstruction to answer supervision under a guard on harm from mismatched messages. Both models remain frozen and the interface trains 1.05M parameters, 348x fewer than C2C. With a Qwen3-8B sharer, a frozen Qwen2.5-0.5B-Instruct receiver reaches 78.04% on MMLU-Redux, versus 37.45% alone and 36.40% with reassigned messages. At fixed interface size, scaling the sharer from 0.6B to 8B raises accuracy from 46.11% to 78.04%; communication also transfers to held-out tasks and can exceed both models when each holds different evidence.

---


### 712. [PanoVLN: Towards Effective Panoramic Vision-and-Language Navigation](https://arxiv.org/abs/2609.34759)

**<font color=#1a73e8>作者：</font>** Zhen Wang, Changpeng Wang, Zhe Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent vision-language models (VLMs) have advanced vision-and-language navigation (VLN), enabling models to predict navigation actions from visual observations and language instructions. In this work, we explore VLN with panoramic observations and introduce PanoVLN. The motivation is straightforward: more complete visual context should enable better-informed navigation decisions. For example, a panorama can reveal a passage outside a perspective camera's field of view, allowing the model to identify the intended route without additional exploration. However, we find that simply replacing perspective images with panoramas yields only limited gains. Our diagnosis suggests that fully exploiting wider visibility requires modifications to action prediction, training supervision, and visual representation. First, wider visibility supports longer-horizon action planning. We make the model predict longer action sequences, enabling larger turns and subsequent movement from a single panorama. Specifically, we introduce a confidence-guided execution (CGE) strategy that dynamically determines how many predicted actions to execute before replanning. Second, wider visibility also brings more complex route choices. We therefore construct training routes with frequent branching points and clear instructions to provide targeted supervision for route selection. Third, panoramic navigation requires understanding spatial relationships across viewing directions, beyond recognizing individual landmarks. We combine semantic and geometric features from RGB panoramas to capture both scene content and spatial layout without adding visual tokens. With a 4B backbone and RGB-only input, PanoVLN surpasses the previous SOTA by 11.9% and 8.7% in success rate on R2R-CE and RxR-CE Val-Unseen. Real-world experiments on a quadruped further demonstrate faster navigation with fewer pauses than prior VLN methods.

---


### 713. [Beyond Reconstruction Loss in Post-Training Quantization: Balanced Fitting for Large Vision-Language Models](https://arxiv.org/abs/2609.34765)

**<font color=#1a73e8>作者：</font>** Minchan Kang, Kyeonghye Park, Seungyeon Sa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) enables efficient deployment of large vision-language models (LVLMs), but is typically calibrated on a small set while expected to generalize across diverse downstream tasks. Although recent PTQ methods for LVLMs incorporate sensitivity signals, they still minimize reconstruction loss with respect to the full-precision model, potentially over-preserving FP behavior and calibration-specific bias. Rather than treating quantization solely as an error to be minimized, we observe that it can also provide beneficial regularization for certain layers and modalities. Motivated by this observation, we propose Balanced Fitting, a quantization effect-based framework that balances precision and regularization beyond reconstruction-based optimization. By measuring layer- and component-wise quantization effects for weights, vision activations, and text activations, Balanced Fitting combines fine-grained fitting for sensitive components with coarser fitting to exploit potential regularization benefits. Experiments on multiple LVLMs show that our method consistently outperforms prior PTQ approaches under both weight-only and weight-activation quantization, while lower reconstruction loss does not reliably translate into better downstream performance. The source code is publicly available at this https URL

---


### 714. [Reference-Grounded Data Curation for Instruction-Following Thai-English Machine Translation](https://arxiv.org/abs/2609.34770)

**<font color=#1a73e8>作者：</font>** Thodsaporn Chay-intr, Krittapad Harnchang, Mahannop 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-following machine translation (IF-MT) requires respecting prompt-level rules on terminology, formatting, and register. Rule compliance typically trades off against translation quality, a tension that general-purpose IF data augmentation methods do not address. We propose Reference-Grounded Data Curation, a two-phase pipeline that extracts every supervised constraint from a reference translation that already satisfies it, ensuring feasibility by construction. Phase 1 applies Instruction-Following Difficulty (IFD) scoring to retain the hardest-but-learnable instances from an English-Thai parallel pool. Phase 2 extracts constraints from each reference target and keeps only generations satisfying every constraint, yielding the 1.97M-record Grounded dataset. We fine-tune open-weight bases on Grounded to produce ChindaMT, a Thai-English translation family at 4B, 2B, and 0.8B parameters. Under length-controlled pairwise judging, ChindaMT outperforms or matches every same-size baseline at every tier on both plain translation and under explicit rules, reaching up to a 68.4% win rate against the strongest baseline. The recipe transfers cleanly across Qwen generations. We release model weights, the Grounded dataset, and evaluation suites.

---


### 715. [Before the Token Commits: Trajectory-Level Benchmarking of Visual Hallucinations in Diffusion VLMs](https://arxiv.org/abs/2609.34772)

**<font color=#1a73e8>作者：</font>** Yadong Wang, Siping Yue, Yu Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal diffusion language models generate responses by iteratively unmasking tokens, making each answer the endpoint of a multi-step trajectory rather than an immediate commitment. Hallucination benchmarks built for autoregressive models evaluate only the final output, and therefore cannot determine whether an unsupported claim in diffusion VLMs appears late or has already stabilized before any answer token is revealed. We introduce DynaHall, a trajectory-level benchmark of annotation-backed binary visual propositions covering object existence, counting, attributes, and relations, with controlled hard negatives graded by visual prior. DynaHall is paired with a commitment-aware protocol that records the intermediate answer tendency at every unmasking step alongside the committed output. Across five diffusion VLMs from three architecture families, visual hallucination is settled before commitment: an unsupported answer is already the preferred state while the answer position is still masked, and later unmasking steps rarely reverse it, so the failure is not introduced at the write step. This holds across decoding schedules, answer formats, and open-ended generation. DynaHall also exposes failures hidden by final-output metrics, including counting and relation collapse, prior-driven false positives, and attribute errors whose direction changes by type. Guided by this diagnosis, PGS (Pre-commitment Gradient Steering) edits still-masked answer states to reduce false positives, bringing the affirmation rate close to balance, and transfers to another architecture without degrading general ability. DynaHall and PGS suggest that hallucination should be measured and mitigated along the generation trajectory of diffusion VLMs, not only at the final answer.

---


### 716. [Page-Aware Retrieval-Augmented Generation for EvalLLM 2026: A Five-Variant Study on French PDFs](https://arxiv.org/abs/2609.34776)

**<font color=#1a73e8>作者：</font>** Abdelhak kelious  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study retrieval-augmented generation (RAG) for questions about French PDF documents when both the answer and its supporting document pages are evaluated. Five system variants add dense retrieval, rank fusion, reranking, and query decomposition to a BM25 baseline. On 595 challenge questions, the complete system scores 0.4450 MRR@10 and 0.4013 Recall@10, compared with 0.3430 and 0.2994 for BM25. Dense retrieval alone and a simple lexical--dense fusion both underperform BM25. Reranking improves the hybrid system, whereas adding query decomposition produces the largest further gain, with higher latency and more detected output artifacts. The complete system slightly exceeds the reported anonymous overall mean on two answer metrics but falls below it on most page-retrieval metrics. These results identify accurate page selection, rather than semantic retrieval in isolation, as the main opportunity for improvement in this setting.

---


### 717. [Applying Language Models in medical Medicine: Recent Trends and Perspectives](https://arxiv.org/abs/2609.34780)

**<font color=#1a73e8>作者：</font>** Erik Aerts  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The use and applicability of artificial intelligence (AI) in medical research and clinical practice has received increasing attention in the literature over recent years. The emergence of large language models (LLMs) has expanded discussions in regards to applications of AI within healthcare. While traditional deep learning based AI applications in medicine have often focused on specific and defined tasks, LLMs offer broader capabilities and flexibility in working with available data,. At the same time of writing, the integration of LLMs into medical settings raises important questions regarding their reliability, accuracy, transparency, safety, and appropriate role in a medical setting. This text presents and discusses recent talks and articles concerning the application of LLMs in medicine, with particular emphasis on their potential utility in research and clinical practice. It considers both the opportunities offered by these technologies and the challenges associated with their implementation, aiming to provide a perspective on the current and emerging role of LLMs within the medical field.

---


### 718. [When VLMs Trust Context: Evaluating Scene Text Recognition under Misleading Context](https://arxiv.org/abs/2609.34781)

**<font color=#1a73e8>作者：</font>** Yuxing Cheng, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can read text in natural scenes, but their predictions may be influenced by the surrounding context. When the printed text conflicts with what the scene suggests, a model may return a more plausible word instead of the shown text. We introduce SceneFaith, a benchmark of 781 generated scene images for studying this behavior. Each output is classified as Literal, Canonical, or Other, separating faithful transcription from context-consistent rewriting and ordinary recognition errors. Across 15 models from seven families, all models show rewriting on clear images, with rates ranging from 8.45\% to 58.51\%. Controlled experiments further show that surrounding context matters: removing surrounding scene information reduces rewriting and improves literal accuracy, while changing the scene around the same text patch can also change model outputs. Moreover, weakening the target text with blur increases rewriting. These results show that reliable scene-text recognition requires VLMs to balance visual character evidence with contextual information, preserving clear text while using context mainly when the visual evidence is uncertain.

---


### 719. [TQTS-Bench: A Multi-Syntax Benchmark for Text-to-Query over Time-Series Databases](https://arxiv.org/abs/2609.34783)

**<font color=#1a73e8>作者：</font>** Fei Lyu, Zhiyi Peng, Jiaming Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have significantly advanced natural language querying over relational databases, yet their ability to query time-series databases (TSDBs) remains largely unassessed. Existing benchmarks fail to adequately capture the non-unified query syntaxes, diverse application domains, and unique time-specific query intents inherent to TSDBs. To address this gap, we introduce TQTS-BENCH, a multi-syntax benchmark for evaluating text-to-query capabilities over TSDBs. TQTS-BENCH contains 6,125 high-quality question-answering (QA) pairs spanning 97 TSDBs, 23 distinct query syntaxes, 22 application domains, and 4 types of time-specific query intents. It is constructed through a human-centric AI-assisted workflow, where all QA pairs are carefully reviewed and revised by domain experts to ensure quality and correctness. Extensive evaluations of advanced LLMs and state-of-the-art text-to-query methods reveal challenges in querying TSDBs. Even the best-performing model evaluated, Claude-Opus-5, achieves only 48.98% execution accuracy, while humans reach 87.34%. Error analysis reveals that this performance gap mainly stems from the heterogeneous query syntaxes across different TSDBs, misinterpretation of time-specific intents, and incorrect schema linking. These findings highlight new opportunities to narrow the gap between current LLM capabilities and the requirements of TSDB queries in real-world applications. The benchmark is available at: this https URL.

---


### 720. [BEHAVE: Functional Behavior Modeling Enables Self-Improving Agents for Hardware Design and Verification](https://arxiv.org/abs/2609.34785)

**<font color=#1a73e8>作者：</font>** Yuheng Wu, Berk Gokmen, Sujeeth Jinesh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing agents for hardware design and verification requires reliable correctness feedback. As a hardware specification may permit correct implementations with different latencies, matching design and reference outputs cycle by cycle can reject valid designs. To address this, we introduce BEHAVE, an agentic framework for multi-turn joint hardware design and verification through functional behavior modeling. We define Behavior IR to express task functionality as executable behavior models without prescribing implementation timing beyond the specification. The agent iteratively develops a register-transfer-level (RTL) design and a behavior model as the design's verification reference. Our evaluator, BEHAVE-Sim, checks both artifacts separately against a hidden golden behavior model using input stimuli generated by random sampling and solver-guided search. BEHAVE thus supports power, performance, and area (PPA) exploration across task-permitted latencies and microarchitectures. During training, the same evaluator provides verifiable reinforcement learning (RL) rewards from specification-behavior pairs without reference RTL. For self-improvement, the agent continually searches for high-level implementations relevant to its capability gaps, constructs and checks specification-behavior pairs, and trains on the expanded task pool. We release BEHAVE-Train and BEHAVE-Eval with 600 human-reviewed specification-behavior pairs for realistic hardware workloads. Starting from 60 seed tasks and acquiring 100 new tasks, self-improvement raises Qwen3.8-27B's RTL pass@1 on BEHAVE-Eval from 55.0% to 75.0%, reaching performance comparable to RL using a 540-task pool.

---


### 721. [D$^2$-VLA: Dual-Memory Dual-Frequency Vision-Language-Action Model For Long Dynamic Manipulation](https://arxiv.org/abs/2609.34792)

**<font color=#1a73e8>作者：</font>** Zijian Ye, Chengqi Wei, Wei Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon manipulation requires robots to remember cues that are no longer in view while responding to moving objects. Yet vision-language-action (VLA) policies often rely on the latest observation, and refreshing their visual context typically requires another costly vision-language model (VLM) pass. We present D$^2$-VLA, which combines dual memory and dual-frequency control at the KV-cache interface of a pretrained VLA. D$^2$-VLA uses block-wise causal KV caching to encode observations incrementally and, guided by distinct temporal attention patterns, constructs separate historical KV read views for the VLM and action expert. Between periodic VLM updates, a gated adapter incorporates fresh visual features into the latest history-conditioned KV block, while a short fast-memory queue supports action replanning. We introduce DOMINO-Long, a ten-task benchmark requiring robots to use earlier visual cues when manipulating moving objects. D$^2$-VLA achieves complete-task success rates of 29.3\% on DOMINO, compared with 9.6\% for $\pi_{0.5}$ and 17.2\% for PUMA, and 60.0\% on DOMINO-Long, compared with 35.4\% and 20.6\%, respectively. It improves success rates on eight real-robot tasks and reaches 97.5\% on LIBERO-Long and 74.3\% on RoboTwin 2.0.

---


### 722. [InfiMed2: A Generalist Medical Multimodal Foundation Model from Contextual Evidence and Stability-Aware Supervision](https://arxiv.org/abs/2609.34798)

**<font color=#1a73e8>作者：</font>** Guanghao Zhu, Zeyu Liu, Zhitian Hou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent medical multimodal models have benefited from larger corpora, broader modality coverage, and stronger reasoning-oriented training, yet effective data design across continued pretraining (CPT) and post-training remains challenging. Medical sources vary substantially in structure, granularity, and information density, and their utility shifts as training progresses from broad knowledge acquisition to late-stage consolidation. Meanwhile, post-training is often dominated by short-form visual question answering, providing limited supervision for informative and answer-consistent explanations. We introduce InfiMed2, a family of 4B and 27B generalist medical multimodal foundation models built around stage-aware data design. We curate a 55.68B-token corpus that combines broad clinical knowledge with context-rich biomedical visual evidence through source-specific processing. Our CPT pipeline first adapts the vision encoder, then builds broad medical knowledge, and finally transitions to an evidence-focused data mixture during learning-rate decay. For supervised fine-tuning (SFT), we regenerate visual question-answering responses using answer stability, answer-masked reconstruction, and correctness-constrained selection to produce more informative and answer-consistent supervision. The 4B model is further optimized with reinforcement learning with verifiable rewards (RLVR). Across five medical multimodal benchmarks, InfiMed2-4B achieves 66.73% mean accuracy after RLVR, surpassing the larger Qwen3.5-9B, while InfiMed2-27B reaches 73.72%, the highest among the evaluated open-weight models.

---


### 723. [Pass or Fail? Evaluating LLMs on Two Greek Examination Benchmarks](https://arxiv.org/abs/2609.34800)

**<font color=#1a73e8>作者：</font>** Panagiota Kyriazi, Eleni Kasoura, Prokopis Prokopidis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Large Language Models (LLMs) imposes a thorough evaluation of their linguistic and analytical capabilities as well as constraints, particularly for a language with limited benchmark coverage such as Greek. To address the limited availability of comprehensive benchmarks in this domain, we introduce Prot-Ex and Pan-Ex, two benchmarks consisting of questions from entrance exams for Greek Model and Experimental schools as well as the Panhellenic exams (the Greek national university entrance examinations). These benchmarks are employed to assess the performance of text-only LLMs-including the Greek-adapted KriKri-8B-Instruct, Llama-3.1-8B, Gemma-4-26B, and Qwen-3-32B-across diverse academic disciplines (Modern Greek, Mathematics, Physics, etc.) and task formats (closed, structured, and open-ended), including textualized visual context (i.e., image descriptions). Our findings indicate the localized KriKri-8B significantly outperforms its base model, successfully rivalling much larger LLMs in linguistically demanding humanities tasks. By leveraging an LLM-as-a-Judge methodology, we expose the inadequacy of traditional lexical metrics for evaluating complex reasoning. Crucially, we uncover a few-shot prompting paradox: while synthetic examples improve accuracy in closed-ended questions, they severely overload the context window of 8B models in structured tasks, causing significant performance degradation. Ultimately, this study suggests targeted linguistic adaptation offsets lower parameter counts in specialized domains, despite the fragility of smaller models to prompt verbosity.

---


### 724. [SIPO: Selective-Inference Policy Optimization for Tree-Structured Agentic RL](https://arxiv.org/abs/2609.34805)

**<font color=#1a73e8>作者：</font>** Zenghuang Fu, Ningqi Chen, Mingda Jia 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tree-structured reinforcement learning trains search agents by comparing alternative continuations and propagating terminal rewards to intermediate decisions. Adaptive expansion, however, creates a statistical asymmetry: an incumbent is selected using its own generation statistic, whereas fresh siblings are sampled after selection. When that statistic is associated with return, branch values can reflect selection history as well as continuation quality, even for a shared parent. We propose Selective-Inference Policy Optimization (\SIPO{}), which incorporates this distinction into tree-based credit estimation. Its scale-free branch criterion keeps generation scores and sibling penalties on a consistent relative scale; exchangeable branching supplies multiple fresh continuations from each selected parent; and order-statistic correction adjusts retained incumbent values using selection rank and the estimated score--outcome association. These mechanisms preserve the leaf budget and the host policy optimisation objective. Across seven QA benchmarks using Qwen3-4B, Qwen3-8B, and Qwen2.5-7B, \SIPO{} achieves the highest reported multi-hop and single-hop averages among the compared methods. On Qwen3-8B, it improves these averages over AT\textsuperscript{2}PO by $1.31$ and $1.07$ percentage points, respectively, and ranks first on six of seven benchmarks. Component ablations evaluate the individual and combined changes, while early-training paired diagnostics show a selected--fresh value gap alongside a near-zero fresh--fresh reference. Together, these results support accounting for selection history when constructing and evaluating search-agent rollouts. Our code is available at this https URL

---


### 725. [ControlTrace: Recovering Control Fields for Hidden-Content Recognition](https://arxiv.org/abs/2609.34807)

**<font color=#1a73e8>作者：</font>** Zijian Liu, Yaoguang Chen, Liwei Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatially conditioned diffusion models can embed words and contours in natural-looking images, but vision-language models (VLMs) may fail to recognize the hidden content. Transformation-based recovery depends on parameter and view selection. To evaluate hidden-content recovery and recognition, we construct FreqBlind, a 6,000-image benchmark spanning contours, real words and non-words across three conditioning strengths. The evaluated transformation-based methods show limited recognition of contour patterns and weakly conditioned hidden content. To address this limitation, we propose ControlTrace to recover the grayscale control field used during generation. An 8.4M-parameter U-Net predicts this field from the carrier image, and a VLM then identifies its content. With Qwen2.5-VL-7B-Instruct, ControlTrace achieves 60.2% open-ended contour recognition accuracy across the three conditioning strengths, exceeding the best of the three evaluated prior methods by 26.9 percentage points. On an A100 GPU, the complete pipeline adds only 7.4 ms (5.3%) to direct VLM inference. Recovered fields have lower pixel errors and higher structural similarity than the evaluated transformation views. Across four evaluated VLMs, ControlTrace retains its overall contour recognition advantage. Recognition remains stable under the tested JPEG compression, Gaussian noise and downsampling. These results support control-field recovery for hidden-content recognition in the evaluated setting.

---


### 726. [From Perception to Integration: Revisiting the Internal Dynamics of Reasoning in Vision-Language Models](https://arxiv.org/abs/2609.34809)

**<font color=#1a73e8>作者：</font>** Rong Yu Xu, Prayag Tiwari, Shaolei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can answer simple visual questions, but often struggle when one question requires several visual judgments. We study this gap with controlled tasks for feature binding, numerosity, spatial relations, and amodal completion, together with a Composite task that combines them. Matched counterfactual image pairs isolate changes in the visual evidence needed to answer. Across four models, direct answers, hidden-state readouts, and state interventions show that the individual judgments can be made without explicit reasoning and that intervening on the corresponding states can affect the answer. During reasoning, the Composite answer becomes decodable from hidden states and usable from shortened traces, often before the model stops on its own. We train a small detector to predict this readiness and stop reasoning at that point. On MMStar and RealWorldQA, this reduces mean reasoning tokens by 79.1% and 74.5%, while average accuracy rises by 3.13 and 3.30 percentage points, respectively. These findings connect the internal development of answer readiness to a practical rule for allocating reasoning computation.

---


### 727. [UniOPSD: Unifying Outcome and Hindsight Feedback for Agentic Reinforcement Learning](https://arxiv.org/abs/2609.34810)

**<font color=#1a73e8>作者：</font>** Zenghuang Fu, Zhaoyang Li, Qiuyuan Ai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become an effective approach to training language model agents, but sparse and delayed outcome rewards provide limited guidance for credit assignment across long interaction sequences. Recent work on on-policy self-distillation (OPSD) offers complementary supervision by evaluating a policy's sampled responses under privileged training-time context. However, our diagnostics show that positive average agreement between outcome and hindsight feedback coexists with substantial local disagreement, raising the question of how to allocate influence between them at each decision. We introduce UniOPSD (Unified On-Policy Self-Distillation), which unifies these feedback sources through adaptive local credit arbitration. UniOPSD constructs comparable credit estimates from environmental returns and successful-peer hindsight at shared interaction anchors. Historical agreement determines the global mixing level, while current signal availability and relative precision adjust each source's influence at individual decisions. The episode-level outcome contribution is retained, and bounded token modulation refines the fused step credit for policy optimization. With Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct, UniOPSD achieves ALFWorld success rates of $82.8\%$ and $83.6\%$, WebShop success rates of $75.0\%$ and $82.0\%$, and Search-QA aggregate accuracies of $45.3\%$ and $49.8\%$, respectively. On 3B WebShop, UniOPSD improves over SDAR by $7.0$ percentage points. Our code is available at this https URL

---


### 728. [CEO Arena: Evaluating Long-Horizon Multi-Agent Decision-Making in Competitive Markets](https://arxiv.org/abs/2609.34821)

**<font color=#1a73e8>作者：</font>** An Yan, Yu Huo, Zhiwei Shang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Long-horizon competition tests agents' ability to coordinate business decisions under uncertainty and adapt to changing rival strategies. We introduce CEO Arena, a benchmark that uses matched replacement evaluation to assess operating returns alongside an agent's effects on rivals and the market. Each CEO agent is compared with a reference policy in the same company under the same economic seed, holding other agents' identities and assignments fixed while all agents adapt. In a shared eight-company market spanning 500 simulated days, CEOs make sequential decisions on pricing, procurement, marketing, research and development, and service using private company information and noisy market signals, under resource constraints and delayed feedback. We evaluate eight LLM-based CEO agents in 27 main runs and 26 robustness runs. In the main evaluation, most agents have negative mean returns, and private gains can accompany market losses. Robustness analyses suggest that aggregate patterns extend beyond the original rule-based baseline; four of the 56 directed pairs show relatively stable effects. Memory, action, and accounting traces suggest demand capture and rivals' pricing and spending responses as possible explanations. CEO Arena provides a controlled testbed for studying long-horizon agent competition, strategic interaction, and market externalities.

---


### 729. [WM-VLM: Probing Internal World Models for Interleaved Visual-Textual Reasoning](https://arxiv.org/abs/2609.34826)

**<font color=#1a73e8>作者：</font>** Yuheng Zha, Yilei Wang, Qiyue Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans often solve spatial problems by mentally simulating visual transformations. In contrast, conventional vision-language models (VLMs) reason primarily through language. We investigate whether VLMs can solve spatial problems by reasoning with both text and generated visual states. To this end, we introduce WM-VLM, which equips a pretrained VLM with a lightweight world model branch for generating intermediate visual states. Our two-stage training first teaches the model to generate the next visual state and then to use that state for reasoning. We programmatically construct spatial reasoning tasks with verifiable intermediate visual states. These tasks allow us to evaluate how well the model generates visual states and how much it relies on them to answer the question. On 2D and 3D mental rotation tasks, WM-VLM consistently outperforms the supervised fine-tuned backbone, with gains of up to 39.25 percentage points. Ablations suggest that these gains depend on the generated visual states, as removing or corrupting them sharply reduces performance. Together, these results suggest that internal world models offer a promising path toward VLMs that reason in both language and visual space.

---


### 730. [Simulating Respondents, Not Single Questions: Coherent Survey Generation with Large Language Models](https://arxiv.org/abs/2609.34828)

**<font color=#1a73e8>作者：</font>** Ji Huang, Mengfei Li, Shuai Shao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to simulate response distributions in social surveys. Prior work has achieved accurate population-level simulation for individual questions. Real questionnaires, however, ask each respondent a sequence of related questions. A simulated respondent should show coherent preferences across the whole questionnaire, not merely accurate distributions for isolated items. Existing single-item methods cannot accurately reproduce how the same person answers a complete survey. We propose FullRespondent-LLM (FR-LLM), which fine-tunes two specialized LLMs: a marginal model for each item's response distribution and a respondent-level autoregressive model for dependencies across answers. Marginal-Constrained Joint Projection (MCJP) then projects the autoregressive joint distribution onto the set satisfying the item-level marginals learned by the first model. This yields complete questionnaires with realistic cross-item relationships while retaining strong item-level accuracy. On two real-world social survey datasets, FR-LLM more accurately reproduces multi-question response patterns, maintains competitive single-item accuracy, and generalizes better to unseen populations and questions. In a small commercial-survey dataset, we use simulated responses to make pricing and stocking decisions; FR-LLM achieves the highest realized profit.

---


### 731. [From Weak Task Specifications to Scientific Extraction Agents: Optimizing Task Construction](https://arxiv.org/abs/2609.34829)

**<font color=#1a73e8>作者：</font>** Zixiao Dong, Wei Yang, Zihao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most methods that optimize LLM prompts and agent workflows assume that task-specific output schemas, extraction instructions, and evaluation criteria are predefined. For scientific extraction agents, however, a short task goal may not fully determine these components, while specifying them manually is costly. We study the upstream problem of constructing the task-specific configuration from a weak specification containing only a short goal and unannotated reference documents. Rather than treating automatic construction as a fixed preprocessing step, our framework constructs a task-specific schema, extraction instructions, and base training rubrics, then keeps schema construction and extraction instructions editable during optimization. Failure-focused updates concentrate textual-gradient feedback on lower-scoring documents, while training-time evaluation criteria adapt to recurring failures. On a heterogeneous-catalysis literature corpus, automatic construction remains improvable, and optimizing both schema construction and extraction instructions performs best across all four judge-rubric settings, with ablations and blinded human evaluation supporting the proposed formulation.

---


### 732. [BV Loss: Block Verification-Aware Loss for Block Diffusion Speculative Decoding](https://arxiv.org/abs/2609.34832)

**<font color=#1a73e8>作者：</font>** Suyoung Kim, Jahyun Koo, Hyeonjin Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion drafters accelerate speculative decoding by proposing multiple tokens in parallel. Despite recent advances in speculative decoding through sequence-level drafting and verification, existing training objectives remain largely designed around token-level verification. To address this mismatch, we introduce Block Verification-aware loss (BV loss), a training objective designed to maximize the expected acceptance length of a drafted sequence. BV loss is directly derived from the block verification acceptance rule, providing a principled connection between the drafter training objective and the inference-time verification mechanism at the sequence level. Across math, code, and chat benchmarks, BV loss increases the mean number of tokens accepted per verification call under block verification by 13.0--21.0\% over cross-entropy loss training for DFlash and DSpark with Qwen3-4B and Qwen3-8B without changing the inference procedure. BV loss also outperforms tokenwise acceptance objectives such as TV loss and LK loss, and its gains extend to token verification and greedy decoding. These results demonstrate the benefit of training block diffusion drafters with an objective aligned with sequence-level verification, rather than optimizing each token independently.

---


### 733. [DivOPD: Spread Wide, Look Close for Asynchronous On-Policy Distillation of Multi-turn Agents](https://arxiv.org/abs/2609.34838)

**<font color=#1a73e8>作者：</font>** Hanyang Wang, Zeyuan Liu, Zhengyu Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains student agents through teacher supervision on their own interactions with an environment. However, in asynchronous multi-turn training, arrival-order batching can allow a few early or long rollouts to dominate learner updates while other valid rollouts become stale before being used, wasting already-generated experience. To address this problem, we introduce DivOPD, a simple learner-side batch-selection method that spreads a fixed turn budget across more rollouts and, within each rollout, prioritizes turns with larger cumulative teacher-student disagreement. Turns without usable teacher feedback are excluded. The per-turn loss and optimizer remain fixed; selection only changes which student-visited turns receive training weight. For no-progress rollouts, an optional extension briefly hands control to the teacher before returning it to the student. Across six teacher-student settings on the simulated ALFWorld, ScienceWorld, and WebShop benchmarks, with 1.5B-7B students, DivOPD raises cross-setting mean peak success rate from 77.4 to 84.4 and mean success over the last five evaluations from 71.5 to 78.6. It reaches all reported setting-specific targets with geometric-mean speedups of 1.84x in training tokens and 1.87x in learner GPU time relative to vanilla OPD. Teacher intervention further raises this last-five mean to 82.4 while retaining about 1.7x learner-GPU speedup over vanilla OPD. Code will be released at this https URL.

---


### 734. [Adapt Semantics, Not Structure: Few-Instance Schema Calibration for Scientific PDF Extraction](https://arxiv.org/abs/2609.34841)

**<font color=#1a73e8>作者：</font>** Zixiao Dong, Wei Yang, Zihao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A well-designed extraction schema is not necessarily ready for reliable LLM execution. When only limited verified extractions are available, manually tuning hundreds of field definitions through trial and error is costly. We frame this problem as few-instance schema calibration: adapting the operational semantics of an existing schema from a few annotated documents while preserving its structural contract. We introduce CPSE, a contract-preserving semantic extraction framework that jointly calibrates extraction prompts and field-level semantic descriptions from a few gold annotations. CPSE decomposes the schema into an invariant structural contract and mutable field semantics, and further separates identity discovery from record completion using manifest-conditioned resolution. On expert-annotated polymer-science documents, CPSE improves extraction by 9.93 points over an execution-matched baseline, with consistent gains under an independent judge and in a blinded expert audit. These results show that CPSE enables low-resource schema execution while preserving the output structure required downstream.

---


### 735. [When Sparse Reward Meets Dense Distillation: Training Dynamics of On-Policy Distillation](https://arxiv.org/abs/2609.34849)

**<font color=#1a73e8>作者：</font>** Xinke Jiang, Tao Feng, Zhibang Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards provides a sparse post-training signal: a single binary outcome evaluates the entire rollout, and every token receives the same sequence-level advantage regardless of its individual contribution. To complement this sparse supervision, a growing family of methods adds a scalar-weighted teacher KL term to the policy-gradient objective, providing dense token-level guidance that may be unreliable at some positions. Despite the benefits of combining these signals, their interaction during optimization can destabilize joint training. To understand how this instability develops, we study the learning dynamics of hybrid reward--distillation training through a neural tangent kernel (NTK) analysis. We introduce the cross-signal NTK $K_{DR}(n)$, a token-level statistic that measures the alignment between reward and distillation gradients at position n. Through this analysis, we identify two failure modes: 1 Magnitude drowning, where the reward gradient exceeds the distillation gradient by orders of magnitude, so that even weak directional conflict can cause the distillation loss to rise despite its explicit inclusion in the training objective; and 2 Localized directional conflict, where the sequence-level advantage and the teacher's position-specific distribution induce opposing updates at the same token ($K_{DR}(n)\!<\!0$). The severity of these effects depends on the optimization regime: the gradient-norm ratio $\kappa\!=\!\|\nabla\mathcal{L}_R\|/\|\nabla\mathcal{L}_D\|$ varies by roughly an order of magnitude across tasks, and our experiments reveal an empirical threshold beyond which naive mixing can lead to persistent training collapse. Motivated by these findings, we introduce the M3 family, which combines magnitude normalization with three strategies...

---


### 736. [When Text Matters: Design Principles for Visual Token Pruning in Vision-Language Model](https://arxiv.org/abs/2609.34861)

**<font color=#1a73e8>作者：</font>** Minchan Kang, Kyeonghye Park, Seoyoung Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning has been widely studied as a practical approach to reducing the computational cost of large vision-language models. However, it struggles to preserve essential visual information, which can lead to substantial performance degradation. In particular, image-based token selection can overlook task-relevant details, while text-guided token selection may fail to capture the text--visual relationships needed for complex reasoning. We find that applying textual guidance too early can limit its ability to identify answer-relevant visual regions, whereas text-to-visual attention becomes more informative at intermediate decoder depths. This finding motivates our training-free method, which separates early vision-guided pruning from deferred text-guided reselection. We first prune visual tokens using vision-encoder attention, retain additional candidates until the decoder midpoint, and then use text-to-visual attention to determine the final visual-token set. Across eight benchmarks and three models, our method outperforms the best-performing baselines by an average of 11.10 and 16.84 percentage points in performance recovery at 80% and 90% pruning, respectively, with comparable or lower LLM-prefill latency than most baselines. The source code is publicly available at this https URL

---


### 737. [JEV as a Judge for Agent Trace Security: An Empirical Comparison with Generative LLM Judges](https://arxiv.org/abs/2609.34862)

**<font color=#1a73e8>作者：</font>** Zhiqiang Wang, Yichao Gao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security evaluation of tool-using agents requires judging actions in context, yet generative judges add latency, explanation overhead, and output-validation failures. We study whether JEV, a typed decision model, offers a useful alternative for retrospective trace classification. We evaluate JEV and four generative judges on four benchmark collections totaling 5,219 trajectories, using a common risk rubric and behavior-level labels. JEV attains a benchmark-averaged positive-class F1 of 77.8, compared with 74.1 for the strongest generative configuration, GLM-5.2, with valid-result coverage of 95.5\% and 94.4\%, respectively. Performance varies across datasets, with JEV leading on ATBench500 and MCPHunt and GLM leading on R-Judge and TraceSafe. Across the four benchmarks, JEV's median successful-call latency is 0.99 seconds; estimated token cost averages \$0.000195 per valid judgment. These results support JEV as an economical screening signal, with trade-offs in precision and recall.

---


### 738. [Revisit to Segment: Working Memory Distillation for Reasoning Segmentation](https://arxiv.org/abs/2609.34863)

**<font color=#1a73e8>作者：</font>** Cilin Yan, Yilun Qiu, Wanyang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have approached image segmentation by reasoning about visual content and predicting target locations. Their generated responses contain reasoning traces and localization proposals that can serve as working memory when revisiting the same image and query. Our exploration reveals that MLLMs benefit from using this self-generated working memory as context, leading to enhanced reasoning segmentation. Motivated by this finding, we seek to strengthen the backbone model's reasoning segmentation capabilities by distilling the guidance gained from revisiting prior attempts, enabling it to benefit with or without working memory at inference time. To this end, we propose Reasoning Segmenter with Working Memory (SWiM), a working-memory distillation framework for reasoning segmentation. Specifically, SWiM selects rollouts based on segmentation quality to construct working memory and uses the memory-conditioned model as a teacher. The teacher provides token-level distributional supervision along student-generated trajectories, while the student receives only the original image and query. Joint optimization of on-policy self-distillation and outcome-based reinforcement learning combines working-memory guidance with direct feedback on segmentation quality. Extensive experiments on reasoning segmentation benchmarks demonstrate that SWiM achieves state-of-the-art performance, validating the effectiveness of working-memory distillation.

---


### 739. [On the Limits of Metacognitive Monitoring in LLMs](https://arxiv.org/abs/2609.34864)

**<font color=#1a73e8>作者：</font>** Dongqi Han, Yifan Yang, Dongsheng Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable decisions depend on recognizing when an answer may be wrong. In biological cognition, metacognitive monitoring can dissociate from task performance, raising the question of how closely solving and judging are linked in language models. Here we study the confidence reports of four frontier models across 15 benchmarks. High task accuracy can coexist with weak error discrimination: a model solves 97% of competition mathematics problems while its answer-time confidence ranks correct answers above errors barely better than chance. Confidence separates correct answers from errors more effectively on questions solved by a separate reference model, while review brings limited improvement on reference-hard questions. Aggregate discrimination also rewards ranking correct answers on easy questions above errors on hard ones, which question-only forecasts already do well. Cross-evaluation helps most where the evaluator answered correctly, and errors shared by the two models usually retain high confidence. Hard questions and shared errors remain difficult targets for prompted self-review and peer oversight, even in models with strong problem-solving performance.

---


### 740. [From Attention Sensitivity to Layer Role: Revisiting Mixed-Precision Quantization of Transformers](https://arxiv.org/abs/2609.34866)

**<font color=#1a73e8>作者：</font>** Nafiseh HosseinpourFardi, Negar Alihadi, Mahmoudreza Babaei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most post-training quantization pipelines fit each weight matrix to its pretrained counterpart, one matrix at a time. Whether that proxy tracks what an attention block actually computes, or how errors in the Q, K and V projections compound inside the softmax, is rarely checked. We write the objective on the attention output instead, over all three projections at once, and reuse it throughout the pipeline. JAB defines one scalar loss over the joint Q, K, V weights of a block, evaluated against the block's real causally-masked attention output, and uses it twice: to fit the quantized weights (GPTQ warm start, then STE with learnable scales), and to score the block for a multiple-choice knapsack allocation.
On attention-only quantization of Mistral-7B this works. At 3 bits JAB recovers 77-90% of the gap between uniform GPTQ and full precision, and its sensitivity estimate tracks an oracle costing 73 forward passes to within a fraction of a point. It stops working once MLP layers enter the allocation. A role-aware offset rule needing no sensitivity estimate at all beats JAB on GPT-2's MLP and on the full Mistral-7B model: with a 3-bit floor it quantizes 96.4% of the weights to 4.5 bits per parameter at 6.933 perplexity, within 4.4% of full precision (6.643) at 3.56x compression, against 7.158 for JAB at the same budget. Which matrix a weight sits in matters more than any sensitivity estimate we computed.
Two things came out sideways. Block-local reconstruction is an unreliable proxy for end-to-end perplexity: one run improved a block's own objective 4.6x while perplexity rose 32x, which is why every allocation here is validated end-to-end. And on attention-only quantization, fine-tuning moved weights farther from their pretrained values while pulling attention outputs closer, with net gains. Post-training seems to recover attention behavior, not weights.

---


### 741. [P4Q: Co-designing Token Pruning and Quantization for Vision-Language Model Acceleration](https://arxiv.org/abs/2609.34867)

**<font color=#1a73e8>作者：</font>** Haizhao Jing, Zhenhao Shang, Haokui Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision language models have achieved strong performance across a wide range of multimodal applications, yet their substantial computational and memory costs hinder efficient deployment. Visual token pruning and post-training quantization reduce inference overhead along two complementary dimensions, namely sequence length and numerical precision. Existing workflows typically optimize these techniques independently or apply them sequentially. Their distinct optimization objectives leave critical interactions unaddressed and constrain the achievable compression performance. We revisit these designs and present P4Q, a practical co-design framework that jointly optimizes visual token pruning and low-bit quantization for efficient VLM inference. First, P4Q introduces a quantization-aware visual token selection strategy before the LLM. It applies fake quantization to copies of the features produced by the projector and selects visual tokens using statistics computed from these fake-quantized features, thereby conditioning the selector's feature-based decisions on simulated low-bit perturbations. Second, P4Q introduces a pruning-aware quantization calibration strategy. It uses the same selection strategy as pruning to calibrate the quantized model on the retained-token distribution, thereby aligning the calibration process with the pruned execution path used during deployment. By coupling these two components, P4Q achieves substantial inference speedups while maintaining comparable task performance, resulting in a better efficiency-accuracy trade-off than independently optimized pipelines. For instance, on LLaVA-NeXT, P4Q achieves an average end-to-end inference speedup of 2.8x across eight distinct test sets, while retaining higher accuracy than prior compression and quantization methods.

---


### 742. [One Readout, Many Repairs: Diffusion-Guided Hierarchical Search for Tool-Agent Repair](https://arxiv.org/abs/2609.34879)

**<font color=#1a73e8>作者：</font>** Xiang Xia, Cheng Yan, Fan Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool agents use large language models to act through external tools, yet successfully executed calls can still leave user requests unfulfilled. Tool-agent repair seeks alternative call sequences that execute successfully and fulfill the original requests. However, repair requires exploring both operation choices and their concrete realizations, making complete-sequence regeneration costly. Moreover, regeneration repeats operation selection even when failure arises from how those operations are realized. The resulting challenge is to reduce this repetition while preserving exploration of alternative operations and realizations. Therefore, we formulate repair as hierarchical search over operation supports, which we introduce as sets of permitted operation types that define reusable search regions for concrete tool-call sequences. We propose ReCommit, a training-free, diffusion-guided framework for improving tool-agent failure recovery while reducing repair computation. ReCommit amortizes operation-level proposal computation across repair trials by reusing operation-type scores from a single parallel readout of a masked diffusion language model. These scores guide search across supports, while realization search explores alternative entity bindings, arguments, and action composition within each support. Experiments on real failures across four enterprise services in the Agent-Diff benchmark show 75.9\% and 63.2\% relative recovery gains with 61.3\% and 51.3\% reductions in mean full-budget repair time at repair budgets $B=3$ and $B=13$, respectively, over the strongest evaluated 8B comparison method. ReCommit achieves a favorable recovery--cost trade-off, including in comparisons with the evaluated 32B models.

---


### 743. [SubRot: Signed Gradient Subspace Calibration for VLM Rotation Quantization](https://arxiv.org/abs/2609.34884)

**<font color=#1a73e8>作者：</font>** Zhenhao Shang, Haizhao Jing, Haokui Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training quantization reduces the deployment cost of vision-language models (VLMs), but preserving multimodal capabilities at low bit widths remains challenging. Existing methods rely on modality- or token-level gradient statistics, which are susceptible to cross-sample variations in visual-to-textual token ratios and the positions of visual information, limiting statistical stability. Moreover, overly coarse aggregation through absolute values and averaging discards gradient signs and channel-wise differences, limiting the separation of modality-specific sensitivities. In contrast, the channel space provides a shared coordinate system across samples, making it a more natural basis for capturing stable task-sensitive structures. We therefore propose SubRot, a signed gradient subspace calibration method for VLM rotation quantization. Through eigendecomposition of the empirical Fisher matrix of activation gradients, SubRot identifies a sensitive channel subspace with three properties: cross-sample stability, clear sensitivity separation, and consistent signed effects on the autoregressive loss along certain directions. Guided by a local Taylor expansion, SubRot combines signed first-order guidance along sign-stable directions with second-order constraints along the remaining sensitive directions, while retaining MSE for overall reconstruction quality. This objective steers quantization errors toward loss-decreasing directions while controlling their magnitude. Experiments on five VLMs across five benchmarks show consistent average-score improvements over FlatQuant under W4A6 and W4A4, reaching 1.4 percentage points on LLaVA-NeXT-7B. Under W4A4, average accuracy degradation from FP16 remains within 1.4 percentage points across all evaluated models, while LLaVA-v1.5-13B exceeds its FP16 average score by 0.4 percentage points.

---


### 744. [Fewer Assumptions by Design: A Reusable Skill for LLM-Assisted Verus Verification](https://arxiv.org/abs/2609.34886)

**<font color=#1a73e8>作者：</font>** Andrada-Livia Antoneac, Dorel Lucanu, Dragoş Teodor Gavriluţ  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-assisted Verus verification is a less tedious method to verify Rust implementations, but paired with self-referential structures, e.g., Doubly Linked Lists (DLLs)â€”notoriously difficult to formalise for verificationâ€”it becomes a substantially more demanding verification task.    Moreover, a specification weakness can arise when verification relies on unproven or invalidated assumptions, such as axiomatic lemmas and assume statements. We investigate whether LLM agents can synthesize strong DLL specifications while minimizing these trusted base. The analysis follows three different approaches: manual verification, property-specific verification, and a defined skill for the specific case of DLLs and certain properties of this type of data structure. The skill encodes domain knowledge and a task-decomposition strategy. We show that an LLM agent equipped with a carefully designed verification skill can generate strong, low-trust specifications for DLLs in Verus.

---


### 745. [Role-Guided MOE for Encoder-Level Pathology Representation Learning in WSI Classification](https://arxiv.org/abs/2609.34897)

**<font color=#1a73e8>作者：</font>** Xinyu Ma, Xing Yang, Hongtao Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole slide image classification is a fundamental task in computational pathology, where patch representation quality directly affects downstream aggregation and slide-level discriminability. Pathology foundation models are widely adopted as frozen feature extractors for WSI classification; however, their fixed encoders may produce representations insufficiently adapted to target-specific tissue patterns and discriminative cues. Fine-tuning can improve target adaptation, but introduces a trade-off between pathology-specific representation capacity and adaptation efficiency, particularly in data-scarce settings. To address this, we propose a pathology role-guided mixture-of-experts feed-forward network (MoE-FFN) framework for efficient encoder-level representation learning. We design a two-stage training paradigm to establish and adapt pathology-aware expert specialization. In source-domain expert initialization, pathology-specific priors are distilled from a frozen Virchow2 teacher into a lightweight DINOv2-small student, while role prototypes serve as weak pathological anchors to encourage distinct expert functions. MoE-FFN blocks are introduced into selected high-level transformer layers to provide transformation diversity for heterogeneous pathological patterns. In target-domain adaptation, the initialized experts are refined through asymmetric prototype-guided optimization, enhancing task-relevant positive evidence and separating confusable hard negatives. The resulting encoder extracts offline patch representations that can be directly integrated with standard MIL aggregators. Experiments on the public BRACS dataset and a private PAROTID WSI dataset across five representative backbones demonstrate consistent improvements over the strongest baseline.

---


### 746. [ReSight-SMC: Two-Stage Power Sampling via Island SMC with Visual Scouts](https://arxiv.org/abs/2609.34905)

**<font color=#1a73e8>作者：</font>** Yaowen Zhang, Xiangyu Qiu, Junyi Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Power sampling has emerged as a training-free approach to LLM reasoning, eliciting capabilities comparable to reinforcement learning by sharpening the model distribution over complete responses. Despite this success, power sampling remains underexplored in large vision-language models (LVLMs). We transfer Power-SMC to LVLM decoding by defining a sequence-power target conditioned on both the image and the prompt. This direct transfer provides a strong training-free baseline, but leaves two aspects of finite-particle multimodal inference unaddressed. At the particle level, global resampling can collapse genealogies, while particle-based power sampling does not diversify trajectories through distinct visual cues in multimodal decoding, limiting exploration under a finite particle budget. At the answer level, sequence-level sharpening makes distinct reasoning trajectories compete even when they support the same answer. We introduce ReSight-SMC, a verifier-free two-stage power sampler for LVLM inference. Its first stage uses ancestry-isolated SMC islands to preserve independent trajectory families and routes a bounded set of prefix-conditioned visual scouts to prefix-relevant image regions while discouraging redundant overlap. Each scout temporarily increases attention to the image tokens and emphasizes its routed region. Exact importance correction preserves the base LVLM sequence-power target. The second stage aggregates terminal importance mass by canonical answer, powers the answer marginal, and samples an answer together with a supporting trajectory. Across four LVLM backbones and five benchmarks, ReSight-SMC achieves stronger aggregate performance than Power-SMC over both the reasoning and perception benchmark groups. Without post-training, it remains competitive in aggregate with backbone-matched models trained using reinforcement learning.

---


### 747. [DGF-Bench: A Benchmark for Simulating and Auditing Deception Against Multi-Agent Governance Boards](https://arxiv.org/abs/2609.34913)

**<font color=#1a73e8>作者：</font>** Jeremy Canale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using language-model agents can review enterprise projects as governance boards do: they read the evidence, apply written rules and decide whether the project may proceed. Part of that evidence comes from suppliers and project members with a stake in the decision. DGF-Bench is a benchmark in which a board of agents (specialist gates and a General gate that consolidates their decisions) reviews synthetic dossiers while an attacker plants deceptive content in evidence the organization does not vouch for. Dossiers are generated from canonical facts under 61 executable rules, with 42 authoritative records and 32 narrative documents; every gate is certified decidable from those records. Attacks never change an authoritative value, so an attacked dossier keeps the reference decisions of its clean copy. A success is attributable only when the agent receives the injection and takes the exact injected action, which it does not take on the paired clean dossier; the DGF score is the share of applicable fixed attacks a model blocks. Reading documents and records themselves, five of six models were outcome-strict (disposition, findings, actions and authorization all correct) on 82 to 85 of 85 gates. Over 2,622 attacked gate runs, seven direct-order, false-data and false-authority attacks obtained one attributable success against these five, whereas task-aligned attacks imitating the organization's own process passed against four of them: a record note citing a fake review procedure lowered GPT-6 Luna Pro from 34 to 6 outcome-strict gates and DeepSeek V4 Pro from 33 to 7. DGF scores ranged from 96.2 to 26.9, and a policy-aware adaptive attacker writing in records succeeded against five of six models. The approval tool executed no forged approval, yet deceived agents submitted approvals that the rules forbid. The open-source package dgf-bench computes the DGF score with one command.

---


### 748. [Muon Sublates the Edge of Stability in LLM Pretraining](https://arxiv.org/abs/2609.34915)

**<font color=#1a73e8>作者：</font>** Yanzhe Chen, Qifang Zhao, Xiaoxiao Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon is increasingly used for language-model pretraining, yet its large-step dynamics are not captured by the classical edge-of-stability (EoS) picture of gradient descent (GD). In GD, loss neutrality, equal-magnitude update reversal, and marginal stability meet at a single learning-rate-dependent edge. We show that Muon breaks this coupling. For stochastic no-momentum Muon, we derive a coherence-corrected conditional loss-neutral boundary $2\rho_b/\eta$, while temporal alignment follows a separate geometry. Controlled experiments show that loss balance and temporal alignment respond differently to learning rate and batch size. Across our language model experiments, the 130M Llama-like LLM runs exhibit loss-boundary tracking with weak negative alignment, whereas the studied 1B LLM configuration shows stronger partial cancellation; in both settings, directions remain far from coherent reversal while training continues to improve. These results support a split EoS picture for Muon: a stochastic loss-neutral edge survives, but it is not accompanied by a universal temporal-direction signature. The source code for reproducing the experiments can be found in this https URL

---


### 749. [Drug-Target Interaction Prediction via Hierarchical Sequential Cross-Attention over Chemical and Protein Language Models](https://arxiv.org/abs/2609.34921)

**<font color=#1a73e8>作者：</font>** Khadidja Henni, Hamza Abdelali, Abdelkrim Aries 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting Drug-Target Interactions~(DTIs) is a central task in computational drug discovery, with direct applications in virtual screening, drug repurposing, and therapeutic candidate prioritization. Although recent deep learning methods have improved DTI prediction, many sequence-based models still process drugs and proteins independently and only combine their representations at a late prediction stage. This limits their ability to explicitly model cross-molecular dependencies between chemical substructures and protein sequence regions. In this paper, we propose a sequence-only DTI prediction architecture that combines two pre-trained language models, ChemBERTa for drug SMILES strings and ESM-2 for protein amino acid sequences, with a hierarchical interaction module. The proposed model first extracts contextual representations using pre-trained encoders, then applies 1D convolutional layers to condense local sequence patterns, followed by a sequential bidirectional cross-attention mechanism inspired by the induced-fit view of molecular recognition. Finally, attention-based pooling constructs fixed-size interaction-aware vectors for binary prediction. Experiments on BIOSNAP, Davis, and BindingDB show that the proposed model achieves the best performance on BIOSNAP, matches the best AUROC on Davis, and remains competitive on BindingDB while using only 25.2 million trainable parameters. Ablation results confirm the contribution of both the CNN and cross-attention modules, and cold-start experiments indicate promising generalization to unseen proteins and drugs.

---


### 750. [Audit the Scaffold, Not the Checkpoint: A Stationarity Dichotomy for Recursive Self-Improvement in Agentic Coding](https://arxiv.org/abs/2609.34924)

**<font color=#1a73e8>作者：</font>** Sebastian Bobadilla-Suarez, Bob Suh, Ryan Fortin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An auditor who checks whether a system's weights are frozen is checking the wrong thing. Our stationarity dichotomy says that iterative self-modification hits strict diminishing returns whenever the agent's reachable set of edits stays fixed, and can escape only if that set expands. Rewriting scaffolding (tools, verifiers, decomposition) expands what an agent reaches without touching a weight, so frozen weights buy an eventual ceiling but no stationarity along the way. The criterion also separates three regimes usually merged: search within a fixed class, test-time training that raises the ceiling itself, and scaffold rewriting between them. Audit the scaffold, not the checkpoint.
The same ceiling binds sideways. Best-of-$k$ orchestration realizes the best worker's ceiling exactly: width buys rate, not budget. Re-consulting a fixed pool has a horizon computable in advance, decided by the pool alone, and the one arrangement that would beat it, a weighted vote, needs diversity real workers lack: on 30 same-family workers the failure overlap sits at its maximum, and a majority fails 23/55 (42%) of tasks.
We obtain the criterion by reading refinement as gradient boosting on the residual error between draft and target, a patch or git diff, and then measuring where that reading breaks: patches compose instead of standing beside each other to be voted on, and failures overlap. What we measure is saturation. Per-round improvement decays toward zero on SWE-bench, and churn decays geometrically across 401 production sessions, a shape shared with a pre-AI human baseline that establishes the regime without identifying its cause. Both breaks are engineering choices rather than laws about code, so together they specify a harness worth building.

---


> [!TIP]
> 当前位于：**701-750**（第 15/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | **701-750** | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
