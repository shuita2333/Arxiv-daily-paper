# 🧠 大模型相关研究 | 2026年09月10日

> 本类共 **483** 篇论文：已确认 **447** 篇，待复核 **36** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

---

### 301. [LLM Layers Immediately Correct Each Other](https://arxiv.org/abs/2609.07876)

**<font color=#1a73e8>作者：</font>** Arjun Patrawala, Jiahai Feng, Erik Jones 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent methods in language model interpretability employ techniques such as sparse autoencoders to decompose residual stream contributions into linear, semantically meaningful features. Such methods are commonly interpreted as identifying features that persist in the residual stream and that subsequent layers build upon. We challenge this view by identifying the Transformer Layer Correction Mechanism (TLCM), wherein adjacent transformer layers systematically counteract portions of each other's contributions. TLCM appears in 5 out of 7 major open-source model families and activates across nearly all tokens in diverse texts. We show that TLCM emerges during pretraining, operates most strongly on contextually dependent tokens, and adaptively calibrates its correction strength based on the preceding layer's output. Using the layer Jacobian, we further show that TLCM selectively corrects specific subspaces while reinforcing others, which we interpret through a ``propose-and-reject'' framework in which layers propose candidate features and subsequent layers selectively remove inappropriate ones. This dynamic suggests that the residual stream at any layer contains transient proposals alongside persistent features, helping explain why SAE feature descriptions often have low specificity, why effective model steering requires extreme feature amplification, and why transcoders hold a theoretical advantage over SAEs.

---


### 302. [Do Large Language Models Know What They Don't Know II? A Fully Behavioral, Non-Cognitive Measure of Epistemic Honesty](https://arxiv.org/abs/2609.07879)

**<font color=#1a73e8>作者：</font>** Ali Şenol, H. Russell Bernard, Huan Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are frequently confident, eloquent, and well versed. A natural question arises: do they know what they don't know? To answer this question, we borrow the concept of epistemic honesty and develop a novel metric to systematically evaluate whether an LLM appropriately acknowledges the boundaries of its knowledge. In this work, we introduce the Epistemic Honesty Quotient (EHQ), which reports three observable sub-scores across two operational axes (epistemic restraint and substantive-answer calibration), and construct EHQ-3000, a 3,000-question benchmark spanning Fabricated Entity, Post-Cutoff Event, Hyper-Niche True, and Context-Conditioned Questions. From a frozen registry of 21 model API routes, 15 completed the protocol after endpoint and eligibility checks; 14 entered the confirmatory analysis because severe provider-side truncation made one route's score indeterminate. The study reveals substantial variation across models, including a difference that can not be explained by their capability to extract explicitly available information. Composite EHQ ranges from 0.31 to 0.81 across the analysed panel, despite near-ceiling performance on the document-grounded capability probe. The two restraint criteria overlap strongly under the present category composition, whereas substantive-answer calibration varies across models and does not reliably co-vary with restraint; however, the small panel leaves substantial uncertainty. Thus, EHQ reveals behavioral differences that are not visible to conventional correctness-based assessment, while also showing why dataset composition, provider behavior, and confidence elicitation must remain part of the interpretation.

---


### 303. [Deadline-Aware Adaptive Prefill Chunking for Efficient Large Language Model Serving](https://arxiv.org/abs/2609.07883)

**<font color=#1a73e8>作者：</font>** Siyu Song, Qi Bai, Jinbo Hao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous batching improves large language model (LLM) serving throughput, but long prompt prefills can delay decode iterations and violate inter-token latency objectives. Chunked prefill mitigates this interference, yet its chunk size is normally fixed: small chunks protect decode latency but repeatedly pay launch overhead, while large chunks improve prefill efficiency but create latency spikes. We introduce SLOWeave, an online scheduling method that selects the largest prefill chunk predicted to finish before the earliest active decode deadline. The decision requires no workload-specific chunk-size tuning and is computed by a logarithmic-time search over a monotone iteration-cost model. We prove that, whenever a decode-only iteration is feasible and the cost predictor is accurate, SLOWeave maximizes immediate prefill progress among decisions that preserve every active request's next-token deadline. We evaluate the method in a reproducible event-driven simulator and an iteration-level GPU runtime across chat, mixed-context, long-context, and bursty workloads. Under a 25ms time-per-output-token objective, SLOWeave improves goodput over the strongest fixed-chunk baseline by 39% on mixed requests and 38% on long-context requests. Under a stricter 10ms objective, the gains rise to 3.3$\times$ and 2.4$\times$, respectively. These results isolate adaptive chunk sizing as a useful serving primitive and provide an implementation-ready controller for integration with iteration-level LLM runtimes.

---


### 304. [Are Image Generators Zero-Shot Perceivers? A Rigorous Evaluation](https://arxiv.org/abs/2609.07884)

**<font color=#1a73e8>作者：</font>** Shangzhe Di, Zhaokai Wang, Weidi Xie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work, such as Vision Banana, shows that lightweight instruction tuning can enable an image generator to achieve state-of-the-art performance across multiple visual perception tasks. Motivated by this perspective, we ask how far image generators can go on public visual perception benchmarks in a zero-shot setting. We introduce ProbeGen, a benchmark for zero-shot generative perception that casts monocular depth estimation, referring/reasoning segmentation, and object counting as conditional generation tasks specified through text prompts, and compares 20 models in total---including proprietary and open-weight image generators, specialist perception models, and MLLMs---across 11 published benchmarks. We observe that pretrained image generators show measurable zero-shot perceptual competence, but with a clear trade-off: specialist models remain stronger for in-distribution accuracy and efficiency, while generative models are often more robust under distribution shift and better at compositional semantic reasoning. We hope this study helps establish zero-shot generative perception as a meaningful research direction and provides a useful foundation for future work at the intersection of visual generation and understanding.

---


### 305. [Quantization Amplifies Determinism, Not Bias: Scale-Dependent Behavioral Effects of Serving-Time Weight Compression](https://arxiv.org/abs/2609.07901)

**<font color=#1a73e8>作者：</font>** Dachi Kurtskhalia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Weight quantization largely determines the economics of serving open-weight LLMs. Its costs are usually assessed with capability benchmarks, on which 4-bit quantization of mid-sized models is often considered "nearly free." We examine a different question: when several answers are valid, does quantization change what a model chooses to say? We serve three checkpoints (Qwen3-8B/14B/32B) at three weight precisions (W4A16 AWQ, W8A16 FP8-Marlin, and bf16), holding the hardware, software, and sampling configuration constant, and collect approximately 71,000 completions paired by prompt and seed across two custom, leak-checked prompt batteries. We pre-specified the analyses in three waves in version control. At 8B, int4 reduces output diversity: the probability that two samples for the same scenario recommend the same brand increases by 5.1 percentage points (prompt-paired sign-flip test, Holm p = .023; reproduced at +4.4pp on a full regeneration of the arm), and lexical diversity falls substantially (TTR -0.011, standardized effect -0.51; robust to a length-controlled measure). At 14B and 32B, no content-concentration measure reaches significance; instead, stylistic drift emerges (em-dash rate +0.46/1k words at 14B and +0.61/1k at 32B, both Holm p <= .0024). Pre-specified tests of stereotype direction are null at every scale: outputs concentrate on the modal answer for each prompt rather than on stereotypical answers. Mechanistically, the token-level distribution becomes flatter (decision-token entropy +0.091 bits, p = .015) while the semantic distribution, measured directly from first-token log probabilities, becomes more concentrated (collision +2.6pp, p = .023): individual tokens become less predictable even as meanings become more repetitive. At 8B, the smallest size tested, AWQ-int4 serving measurably narrows the range of suggestions; audits should assess concentration as well as bias.

---


### 306. [PRIMUS: Identity, Governance, and Verification for Multi-Agent Federations](https://arxiv.org/abs/2609.07910)

**<font color=#1a73e8>作者：</font>** Sasank Annapureddy, Anjaneya Prasad Thamatani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent federations need governance that answers three questions under adversarial conditions: who participated (identity), did they conform (enforcement), and who decides (authority). A separate question is whether the verification machinery that polices a federation's outputs can also steer a generate-and-test loop toward better answers.
Part I. PRIMA introduced prime-power agent identity and a consensus token whose factorization indexes participation, but assumed honest agents. We present PRIMUS, which couples prime-power identity with BLS aggregate signatures (PIAC), derives a safe-kill threshold that reduces false-positive agent termination from 80% to 0.00% under 10% channel noise, gives the closed-form economic boundary where singleton governance outperforms Byzantine quorum ($\gamma^* \approx 9f$, verified flat across n = 50 to 10,000), and specifies VRF succession with lease and fencing that makes safety unconditional under partial synchrony. Five problems are identified as provably unfixable within the model and stated as scope boundaries.
Part II. A verifier is not a solver. We ask whether PRIMA's binary artifact-fidelity verdict can be converted into a graded fitness signal, and measure the conversion on binary covering codes. Calibration against injected fault burden is strong ($\rho$ = 0.676 deterministic, 0.819 full); against real LLM-generated candidates the same scores fall to 0.158 and 0.406, roughly a quarter of the calibration value (the same-designer confound, measured). As a pre-filter it beats a random-score control convincingly and a binary gate narrowly. Under 400 iterations of explicit optimization it was not gamed, but only because the objective saturated after one honest answer. A cross-family judge preserves the burden-ordering signal while destroying individual judgments. No covering-code record resulted. Measured program cost: USD 164.78.

---


### 307. [Humans Introduce, Models Elaborate: Asymmetric Narrative Agency in Human-LLM Co-Writing](https://arxiv.org/abs/2609.07920)

**<font color=#1a73e8>作者：</font>** Halfdan Nordahl Fundal, Yuri Bizzoni, Charlotte Gjørup Bilde 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-LLM co-writing is increasingly used for open-ended text generation, but much prior work focuses on final outputs rather than the interactional dynamics through which stories are produced. We study turn-based collaborative storytelling across three matched conditions: Human-Human (HH), Human-LLM (HA), and LLM-LLM (AA). Using a shared storytelling paradigm, we measure how agents align, introduce novel material, and influence narrative development through turn-level measures of valence adaptation, semantic novelty, transience, and resonance. Our results show that HA co-writing is not intermediate between HH and AA collaboration. Instead, it displays a distinctive asymmetry where humans tend to introduce more novel and persistent narrative material, while LLMs tend to elaborate and stabilize the existing context. These findings suggest that, in this setting, LLMs function less as human co-authors and more as adaptive narrative amplifiers that reshape how agency is distributed in collaborative writing.

---


### 308. [FrogNano: Training a 4B Coding Agent via Online Task Synthesis](https://arxiv.org/abs/2609.07925)

**<font color=#1a73e8>作者：</font>** Minseon Kim, Zhengyan Shi, Emiliano Penaloza 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present FrogNano, a 4B coding agent designed to tackle software engineering (SWE) tasks efficiently and effectively, even under resource-constrained environments. It is post-trained exclusively via RL on around 1,500 SWE environments with synthetic tasks. A key ingredient for improving performance is an online task synthesis pipeline that creates tasks calibrated to the frontier of learnability for the current checkpoint. This report provides evidence that competitive small coding agents can be trained with synthetic tasks alone, without traditional distillation from larger models, and that generating tasks at the learnability frontier of the current agent is important. We report details on the training methodology, evaluations across diverse environments, and in-depth analyses, serving as a foundation for our ongoing exploration of lightweight yet capable coding agents that can run on minimal hardware.

---


### 309. [TDDN: Text-aligned Diffused DINO Network for Puzzle Understanding](https://arxiv.org/abs/2609.07937)

**<font color=#1a73e8>作者：</font>** Harsha Patnala, Debopriyo Banerjee, Ayush Sunil Munot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured visual reasoning, such as image puzzles, demands fine-grained visual perception, an ability current Vision Language Models (VLMs) lack. VLMs built on CLIP-based ViT backbones trade fine-grained detail for high-level semantics, and we show this loss propagates downstream. To recover it, we fuse DINOv3 and CleanDIFT representations into a perception encoder (DiffusedDINO) and align it with RoBERTa-L, yielding a text-aligned model TDDN that preserves this perceptual advantage: with frozen backbones and only $\sim$590K alignment pairs, TDDN matches CLIP on image-text retrieval, surpassing it on three of four settings. It does so while more than tripling CLIP's dense-prediction accuracy (ADE20K 5.20 $\to$ 18.11 mIoU, COCO-Stuff 7.35 $\to$ 24.44), despite CLIP's massive training corpus. TDDN leads on segmentation benchmarks among general-purpose contrastive encoders, including SigLIP$\,$2. We further introduce Puzzle Perception, a segmentation and visual question answering dataset that probes fine-grained spatial understanding, on which TDDN doubles CLIP's segmentation accuracy (11.04 $\to$ 22.51 mIoU).

---


### 310. [ReactVAU: A Slow-Fast Decoupled Framework for Streaming Video Anomaly Understanding](https://arxiv.org/abs/2609.07941)

**<font color=#1a73e8>作者：</font>** Chia-Hui Chen, Shih-Ying Yeh, Fu-En Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose ReactVAU, a Slow-Fast Decoupled Framework for real-time streaming Video Anomaly Understanding (VAU). Existing VAU methods rely on offline inference with global temporal sampling, which violates causality and prevents deployment in live surveillance streams. Conversely, general streaming video models satisfy causal access but dilute rare transient anomalies during memory compression and often invoke heavyweight MLLMs uniformly over long normal intervals. React VAU addresses this gap with three synergistic components: a lightweight Fast Detection Module based on Spatial Grid Folding (SGF) for continuous anomaly filtering; an Anomaly-Aware Persistent Memory (AAPM) that protects critical visual cues from temporal decay; and a heavyweight Slow Reasoning Module that remains dormant during normal streams and is awakened only by suspicious events for semantic verification and causal description. Extensive experiments on multiple benchmarks demonstrate that ReactVAU operates under strict streaming constraints while simultaneously achieving competitive performance in both anomaly detection and causal reasoning, alongside significantly enhanced computational efficiency by minimizing heavyweight MLLM invocations. Project page is available at this https URL

---


### 311. [Beliefs and Behavior in Language Models](https://arxiv.org/abs/2609.07943)

**<font color=#1a73e8>作者：</font>** Alex Smolin, Bryan Wilder  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There is significant uncertainty about whether abstractions like beliefs or desires usefully describe the behavior of large language models (LLMs). In addition to the inherent scientific interest of this question, these latent quantities are often invoked to explain the behavior of LLMs to users or to define and evaluate harmful behaviors which are relative to intent. Nevertheless, we currently lack a means to systematically test whether concepts like "belief" are well-applied to LLMs, and hence whether they are likely to be fruitful ingredients of attempts to align models with human interests. We propose an approach for empirically studying such questions, asking whether a single latent variable inferred from the LLMs' outputs -- interpreted as a degree of belief -- allows an observer to make interpretable predictions of how the LLMs' will respond to new prompts. We find that highly capable models are usefully described as holding beliefs and that, generally, the predictability of model outputs based on an inferred latent belief tracks overall trends in model capability. Building on these findings, we provide empirical strategies to study how beliefs in LLMs can be measured, the extent to which LLMs comply with instructed decision rules or payoffs, and how beliefs evolve within individual instances of an LLM over the course of reasoning.

---


### 312. [CausalVerify: An Execution-Grounded Benchmark for LLM Causal Inference Workflows](https://arxiv.org/abs/2609.07944)

**<font color=#1a73e8>作者：</font>** Yonghong Zhang, Ricardo Correia, Isabel M. Parra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing causal-inference benchmarks for LLMs mostly score method descriptions or whether generated code runs, not whether the executed workflow recovers the target causal estimate. CausalVerify studies this verification problem for structured econometric causal-estimation workflows by separating realistic interpretation from verifiable computation. It pairs 259 published economics papers (reconstructed research question, data description, institutional context) with 100 fixed-seed synthetic scenarios that realise CSV datasets for difference-in-differences, event study, instrumental variables, and regression discontinuity designs. Experiment A (real-paper text agreement) scores method-family and direction agreement against four-LLM consensus labels. Experiment B (synthetic execution) runs model-written R code and checks whether the extracted treatment-effect estimate matches a canonical estimator on the same realised dataset; this execution-grounded correctness layer is L2b+, distinct from L2b, which records only whether the code executes. A calibration arm asks whether self-reported confidence separates correct from incorrect workflows. On Experiment B, seven LLMs reach L2b+ pass rates of 10% to 88% at the default 50% tolerance, and 66 of the 426 workflows that execute (15.5%) return a wrong estimate. Execution ranking (L2b) agrees with L2b+ far better than text-direction scoring (L4): Kendall $\tau=0.81$ and Spearman $\rho=0.93$, versus Kendall $\tau$ between $-0.20$ and $0.10$ for L4. Llama-3.3-70B-Instruct shows the same qualitative gap, and reported confidence does not reliably separate correct from incorrect workflows. The claims are confined to standardized single-shot workflows in these four design families under the evaluated R backend and model panel; the benchmark does not measure general causal-inference ability. Code, data, cached outputs, and a datasheet are released.

---


### 313. [MetaKV: Adaptive KV Cache Compression for Constrained LLM Inference](https://arxiv.org/abs/2609.07966)

**<font color=#1a73e8>作者：</font>** Michael Wang, Keith Li, Roozbeh Bostandoost  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Key--value (KV) cache compression is an effective way to reduce the memory overhead of large language model (LLM) inference, particularly for long-context workloads. However, existing compression methods make different trade-offs among accuracy, inference latency, and peak KV cache memory utilization, making a single fixed configuration unsuitable across different prompts and resource constraints. We introduce MetaKV, an adaptive framework that selects a KV cache compression configuration for each input prompt based on user-specified latency and peak memory budgets. MetaKV uses lightweight prediction models to estimate the end-to-end latency, peak memory, and probability of a correct response for each candidate configuration, and selects the configuration that best satisfies the latency-memory constraints while preserving accuracy. We evaluate MetaKV across ten configurations from three representative KV cache compression methods, KVQuant, H$_2$O, and RocketKV, together with an uncompressed FP16 configuration, on four datasets covering mathematics, science, commonsense reasoning, and reading comprehension. Across a wide range of latency and peak memory constraints, MetaKV consistently outperforms the best static configuration, improving constrained success rate (CSR), the fraction of prompts answered correctly while satisfying both constraints, by approximately 0.07 on average and up to 0.135. These results demonstrate the benefit of adapting KV cache compression to individual prompts and latency-memory constraints. Code is available at this https URL

---


### 314. [Reasoning Beyond Transcription: Audio Language Models on Child Stuttering Speech](https://arxiv.org/abs/2609.07968)

**<font color=#1a73e8>作者：</font>** Chibuzor Okocha, Christan Grant, Zoey Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Child speech differs from adult speech in acoustics, prosody, and linguistic structures. Speech disfluencies (such as repetitions) further challenge automatic understanding. While Audio Language Models (ALMs) show strong semantic reasoning from speech audio, their ability to reason about disfluent child speech in mixed-speaker settings remains unexplored. We investigate this through two tasks: child-focused semantic summarization and speech entailment. Experiments use recordings of children who stutter in mixed speaker interviews without explicit speaker separation. Models are instruction-guided to focus on the child, preserve clinically relevant disfluencies, and avoid adult-speech leakage. Evaluation combines LLM-based judges and reference-based metrics, anchored by transcript-oracle baselines to isolate errors. Results show that while ALMs extract high-level meaning from stuttered speech, reasoning degrades significantly with increased

---


### 315. [MeRoTune: RoPE-Safe Merging with a Tunable Dial](https://arxiv.org/abs/2609.07971)

**<font color=#1a73e8>作者：</font>** Salman Faroz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When you merge two fine-tuned models from the same base checkpoint by simply averaging their weights, you implicitly assume their attention subspaces are still aligned. Recent work attempts to fix misalignments by learning an invertible correction matrix, $M$, for each model's query and key projections. This correction cancels out---using $M$ on the query side and $M^{-T}$ on the key side---right before the dot product. However, this cancellation is only exact if nothing sits between the projection and the dot product. In reality, almost all modern open-weight language models put a rotary position embedding (RoPE) exactly there. In this paper, we show that this cancellation is exact under RoPE if and only if $M$ commutes with RoPE's per-position rotation. We derive the specific class of matrices where this holds: a scaled rotation acting independently within each RoPE frequency pair. This forms a strict, low-dimensional subset of the unconstrained matrices that current methods normally train. Building on this, we turn this constrained matrix class into a new merging method. While keeping the base weights entirely frozen, two fine-tunes each learn their own RoPE-compliant correction matrices. We optimize these corrections against a chosen blend ratio so the final result can be adjusted post-hoc like a dial, rather than locked into a single fixed merge. Our default approach trains at one fixed blend ratio, similar to how LoRA sets its scaling hyperparameter in advance. We also experiment with resampling the blend ratio randomly at every training step, and we report the results of both approaches.

---


### 316. [From Event Logs to Governed Action: A BlueSky Agenda for Agentic Process Mining](https://arxiv.org/abs/2609.07984)

**<font color=#1a73e8>作者：</font>** Yiyuan Yang, Zheshun Wu, Yong Chu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Process mining has long turned event logs into process knowledge: discovered models, conformance evidence, bottleneck diagnoses, and runtime predictions. Agentic AI changes the target. Process-aware agents will not only ask what happened. They will ask whether a proposed action should be taken, given the available evidence, privacy budget, organizational authority, and downstream risk. This BlueSky paper proposes event-to-action process mining: a process-mining agenda for transforming heterogeneous operational event data into governed action. The goal is not another dashboard, a generic enterprise simulator, or a language interface over logs. We argue that the community needs four mineable artifacts: event-object representations, action evidence packages, governance contracts, and benchmarks where act, defer, ask, and refuse are all valid outputs. This agenda is timely because agentic business process management (BPM), LLM-assisted process mining, object-centric event standards, causal process monitoring, and privacy-preserving learning are maturing separately. Bringing them together defines a data-mining target inside process mining: mining logged organizational behavior for accountable action, not only retrospective insight.

---


### 317. [Automated Chest CT Protocol Selection via Large Language Model Derived Text Embeddings from Imaging Request Text](https://arxiv.org/abs/2609.07986)

**<font color=#1a73e8>作者：</font>** Zahra Hosseini, Mahan Pouromidi, Farzad Khalvati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Purpose: Accurate CT protocol selection is critical for diagnostic quality and patient safety, yet the current process is manual, time-consuming, and prone to inconsistencies. Prior Machine Learning methods using keywords or bag-of-words lack contextual understanding and perform poorly on rare protocols. We propose a decision support system using large language model (LLM) features to recommend protocols from free-text clinical indications, capturing clinical nuance and phrasing variation for more consistent, efficient selection.
Methods: In this REB-approved retrospective study, 285,123 chest CT imaging requests from a large academic medical center (2017-2024) were split into training (228,099, 80%) and held-out test (57,024, 20%) sets. Each request included procedure names, clinical indication, HIS comments, and the selected protocol. Clinical text was embedded using a fine-tuned LLM, Meta's LLaMA-3.1-70B; these features input a logistic regression classifier predicting 18 protocol labels (e.g., PE, LDCT).
Results: The pipeline achieved a weighted precision of 0.84, weighted F1-score of 0.81, and overall accuracy of 79% across 18 CT protocols. On 300 independent cases with expert consensus, the LLM reached an overall accuracy of 80% versus 83% for radiologists, with no significant difference (p = 0.263). Performance was comparable across most classes, with the LLM exceeding radiologists for some challenging categories, and entropy analyses indicated more balanced protocol use, suggesting reduced variability.
Conclusion: An LLM-based recommendation system can leverage general knowledge from a large natural-text corpus to accurately assign chest CT protocols from free-text imaging requests, and may serve as a viable foundation for protocol recommendation tools where inputs require language understanding.

---


### 318. [When Can LLM Digital Twins Reduce Human Measurement? From Behavioral Fidelity to Statistical Substitutability](https://arxiv.org/abs/2609.07987)

**<font color=#1a73e8>作者：</font>** Steven Wang, Kyle Hunt, Shaojie Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based digital twins promise to reduce repeated human data collection by generating person- specific responses, yet existing evaluations provide little evidence about whether they can reduce human measurement while preserving valid inference. To address this, we introduce statistical substitutability, an inferential criterion that evaluates the extent to which twin predictions can reduce human measurement for a particular estimand while preserving valid inference. We develop a framework, grounded in mixed-subject and prediction-powered inference, that evaluates statistical substitutability along four dimensions: aggregate fidelity, paired respondent-level signal, finite-sample human-label recovery, and stability across populations. Across two empirical evaluations spanning behavioral experiments, multiple models, and alternative respondent representations, we find that digital twins can reproduce average human effects while providing little information about which individuals differ from those averages. Newer models and richer respondent information improve some dimensions of performance but do not reliably translate into human-data savings. Human calibration can reduce aggregate prediction error, yet limited labeled samples often fail to produce stable precision gains. Importantly, these findings demonstrate that behavioral fidelity is neither necessary nor sufficient for statistical substitutability. More broadly, they suggest that AI-generated evidence should be evaluated based on its ability to support valid scientific inference rather than its ability to reproduce human outcomes alone. Digital twins should therefore be judged for confirmatory use by whether they reduce uncertainty about human quantities, not merely by whether they reproduce human means, distributions, or effects.

---


### 319. [Sparks of In Silico Cognitive Science: Theories from Simulated Data Can Generalize to Humans](https://arxiv.org/abs/2609.08003)

**<font color=#1a73e8>作者：</font>** Akshay K. Jagadish, Younes Strittmatter, Nori Jacoby 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavioral foundation models have been proposed as stand-ins for human participants across settings, but it is unclear whether theories discovered on them generalize to humans or merely characterize the simulator. We ran the Automated Cognitive Scientist (\textsc{AutoCog}), a closed-loop discovery system in which LLM agents design theory-discriminating experiments, collect responses, arbitrate between competing theories, and synthesize successors, entirely on behavior simulated by Centaur, a foundation model of human behavior. In a multi-attribute decision-making setting, the theories \textsc{AutoCog} found on Centaur generalized to human data: they outperformed canonical theories on ten held-out experiments and were rivaled only by theories found by running the same loop on people. We argue that this succeeds despite the simulator's inevitable imperfections because a discovery loop that arbitrates between competing theories demands less of its simulator than estimation does. The simulator only needs to capture the regularities that distinguish the theories, and not necessarily reproduce behavior precisely. Imperfect simulators can therefore widen the search over theories, with human data then testing whether the surfaced theories generalize.

---


### 320. [A Layered Analysis of Disagreement And Answer Quality in Multi-Agent LLM Debate](https://arxiv.org/abs/2609.08016)

**<font color=#1a73e8>作者：</font>** Chen Qian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate, in which several LLMs exchange arguments before answering, is widely assumed to improve answer quality by surfacing genuine disagreement. That mechanism is rarely checked. We introduce four measurements: (A) the agreement a debater reports; (B) whether its reply text actually pushes back; (C) whether the position persists once the eliciting instruction is removed; and (D) for open-weight models, the stance response in the debater's own token log-probabilities. We evaluate three-model committees debating open-ended GlobalOpinionQA across 750 debates under three tones: friendly (seek common ground), neutral, and hostile (stress-test every position). (A) Tone strongly reshapes reported agreement: full agreement differs by 50.4 percentage points between the friendly and hostile endpoints. (B) A judge that reads only the reply text, never the self-report or the condition, recovers the same pattern. (C) The dissent appears partly tied to the instruction that elicited it: labels revert toward agreement 23.1 points more often after deleting the hostile instruction than under a matched re-ask that keeps it; question-weighted inference is inconclusive on first-round turns alone (p=0.0625), significant pooling all rounds (p=0.016), and only 11/28 first-round reversions also appear in the reply text. (D) Opposing arguments weaken a debater's stance margin more consistently than they shift its direction. For final answers we detect no quality gain: a bias-checked jury returns 299/299 ties (ruling out only large differences), accuracy on a verifiable control task is unchanged, and a jury without the bias check had declared debate the winner 66% of the time -- an artifact of reading order. Taken together, LLM debate readily changes what agents say, but we find much weaker evidence that it changes what they persistently endorse or improves the quality of the final answer.

---


### 321. [Eliciting Self-Verification in Multimodal Reasoning Agents with Reinforcement Learning](https://arxiv.org/abs/2609.08025)

**<font color=#1a73e8>作者：</font>** Vishwas Sathish, Viresh Ranjan, Xinliang Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning agents increasingly rely on external tools such as web search to answer complex queries. Reinforcement learning (RL) finetuning algorithms such as GRPO have improved long-form reasoning in text-only language models, particularly for coding and mathematics. Reliable tool use in multimodal agents, however, remains challenging because models must interpret text and images while integrating noisy retrieved evidence, often under sparse outcome-level supervision without explicit verification signals. We present Self-Verification via Reinforcement Learning (SVRL), an RL-only finetuning framework that trains multimodal agents to verify and filter retrieved evidence within their own reasoning traces, reducing reliance on external verifiers at inference time. SVRL also introduces a search-aware penalty that discourages unnecessary tool calls and a query-diversity reward that encourages diverse, well-formed search queries, providing fine-grained feedback on when and what to search. Finetuning Qwen-2.5-VL-7B with SVRL on only 5{,}000 visual question answering examples yields consistent gains in multi-hop VQA generalization and tool efficiency across benchmarks. Overall, SVRL narrows the gap between compact agents and much larger proprietary models while requiring substantially lower training and inference cost.

---


### 322. [BanglaMemeX: Advancing Cultural Metaphoric Image Interpretation in Bangla with a Multimodal Explainable Dataset](https://arxiv.org/abs/2609.08029)

**<font color=#1a73e8>作者：</font>** Md. Sadman Sakib, Zisan Mahmud, Md. Fahim Arefin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision Language Models have achieved strong performance on multimodal benchmarks, yet their ability to reason about culturally grounded and metaphor-rich content remains insufficiently studied. Internet memes present a challenging setting where meaning emerges from implicit interactions between image, overlaid text, sarcasm, and shared socio-cultural knowledge rather than literal visual recognition. This challenge is amplified in low-resource languages such as Bangla, where code-mixing, stylized scripts, and culturally specific symbolism introduce substantial distribution shift. In this work, we introduce BanglaMemeX, a culturally grounded multimodal benchmark comprising 3,000 Bangla memes annotated with multi-dimensional labels (humor, sarcasm, offensiveness, motivational intent, and overall sentiment) and human-written explanations that explicitly describe textual and visual metaphors. We systematically evaluate modern VLMs on both classification and explanation generation, revealing that current models struggle to interpret implicit cultural cues despite reasonable surface-level accuracy. Our results highlight the need for culturally-aware multimodal systems capable of grounded reasoning under linguistic and cultural distribution shift.

---


### 323. [Scaling Multi-Agent Systems with Prospect-State Propagation](https://arxiv.org/abs/2609.08033)

**<font color=#1a73e8>作者：</font>** Zhimei Chen, Mu Chen, Fakhri Karray  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Current LLM-based multi-agent systems (MAS) periodically compress intermediate states to reduce inference-time token consumption, thereby attempting to incorporate more agents. However, naive scaling strategies face challenges. For example, in economic simulations, large-scale MAS typically discard semantically rich economic states, i.e., agent behavioral trajectories, which are key drivers of macroeconomic fluctuations. In this paper, we reveal a phenomenon in which agent heterogeneity gradually decreases during simulation, and propose Prospect-State Propagation for Multi-Agent Systems (PspMAS). Inspired by prospect theory, PspMAS decouples each agent's micro state into a compact Prospect State and an expressive Semantic State. The former records psychological traces through a lightweight, parallelizable propagator and continuously injects heterogeneity into the system. The latter leverages the strong perception, reasoning, planning, and decision-making abilities of LLMs. These two components work complementarily, providing a scalable LLM-based multi-agent simulation solution.

---


### 324. [VEX-Bench: Benchmarking LLM Agents for Assessing Exploitability of Software Supply Chain Vulnerabilities](https://arxiv.org/abs/2609.08040)

**<font color=#1a73e8>作者：</font>** Jiahao Shi, Edward Tsien, Yifeng Di 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The software supply chain has become an increasingly exposed attack surface because of its reliance on intricate yet fragile dependencies. Existing defenses such as GitHub Dependabot often raise many false alerts because their coarse-grained matching cannot determine whether a vulnerable dependency is actually exploitable. Security analysts typically spend substantial time assessing vulnerability exploitability case by case. Recent LLM agents have emerged as promising candidates for this task given their advanced capabilities in coding and cybersecurity, yet no existing benchmark evaluates them on it. Prior benchmarks target zero-day settings, where agents detect and exploit previously unknown vulnerabilities. In contrast, software supply chain security focuses on how known vulnerabilities in upstream dependencies affect downstream projects. This requires agents to reason across repositories and determine whether an upstream vulnerability is exploitable in the downstream project. To address this gap, we introduce VEX-Bench, the first benchmark for evaluating LLM agents' ability to assess the exploitability of software supply chain vulnerabilities. It contains 75 real-world cases mined from GitHub and labeled by security experts, covering Python, Java, and Go. We evaluate nine models across three agent harnesses. While GPT-5.5 and Claude Opus 4.6 reach approximately 80% F1 on binary vulnerability-status classification, only GPT-5.5 surpasses 70% macro-F1 on fine-grained justification classification. This gap highlights the challenge of moving beyond binary exploitability assessment to identifying fine-grained exploitability reasons. Code and data: this https URL

---


### 325. [ResidualAuth: What Authorization State Must Language Agents Preserve under Revocable Delegation?](https://arxiv.org/abs/2609.08062)

**<font color=#1a73e8>作者：</font>** Moonwon Choi, Seokho Jeong, Seunggeun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using language agents can delegate and revoke permissions while acting through external services. We show that two authorization histories can have identical current permissions and identical all-pairs reachability yet require opposite decisions after the same direct-edge revocation. We formalize the information needed to preserve such distinctions as a residual authorization state. We prove that exponentially many future-distinct states can share one fixed transitive closure, and give exact or tight asymptotic bounds on the state required by an exact monitor as delegation redundancy varies. ResidualAuth compiles these constructions into paired language-agent episodes. Across four open-weight models, a fixed 256-token summary solved 0-2/16 pairs, sham reads solved 0/16, and authenticated current-query reads solved 15-16/16. In a separate held-out online-memory diagnostic, exact ledger serializations fit all 128 four-coordinate pairs at both 768 and 1,024 tokens. At either cap, factually supported model-written memories sufficient for every prespecified continuation solved at most 1/128 pairs per model. A hard gate reduced eight observed unauthorized effects to zero without changing the preceding attempts. These results distinguish required authorization state, usable decision information, online state maintenance, and effect mediation.

---


### 326. [Risk-Conditioned Fine-Tuning of Large Language Models](https://arxiv.org/abs/2609.08064)

**<font color=#1a73e8>作者：</font>** Zixuan Liu, Fangzheng Wu, Brian Summa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in settings where rare but severe harmful generations can have significant consequences. Existing Risk-Averse RLHF addresses this issue by optimizing Conditional Value-at-Risk (CVaR), but it trains policies for fixed risk levels and therefore cannot adjust the desired degree of risk aversion at inference time. In this paper, we propose risk-conditioned RLHF, a framework that trains a single policy that provides a continuous risk-control interface, enabling users to select different degrees of risk aversion without retraining or deploying multiple risk-specific models. Experiments across multiple benchmarks demonstrate that a single risk-conditioned policy can adapt to different risk levels at inference time, enabling more flexible and risk-aware LLM deployment.

---


### 327. [Popular Knowledge Propagates More Errors in LLM Knowledge Updating](https://arxiv.org/abs/2609.08067)

**<font color=#1a73e8>作者：</font>** Yuji Zhang, Weibing Wang, Cheng Qian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Updating a language model's knowledge through fine-tuning is essential for keeping its outputs current, yet can also induce factual forgetting and new hallucinations. Prior work shows that long-tail knowledge is harder to acquire and newly memorized long-tail facts are difficult to retain during later fine-tuning. We study a complementary question: among facts that a model has encoded correctly, which are most vulnerable to collateral corruption during other updates? To investigate this question under a realistic factual distribution, we construct a large-scale graph FACTPROP of verified Wikipedia facts by linking triples that share head or tail entities, thereby preserving connections among factual knowledge. We fine-tune models on factual statements and measure correct-to-incorrect facts after each update. Our results reveal a pattern distinct from prior findings on long-tail vulnerability during acquisition and retention: among facts that models already answer correctly, those associated with highly connected entities are more likely to be corrupted by neighboring updates, and updates to such facts propagate errors more broadly. Structural popularity therefore predicts both vulnerability and downstream damage. Inspired by this finding, we propose Popularity-based Anchoring (PopAnchor), a lightweight rehearsal strategy that preserves a small set of popular facts and reduces forgetting.

---


### 328. [Automated Design of Inventory Policy with Large Language Models: An Exploratory Study](https://arxiv.org/abs/2609.08071)

**<font color=#1a73e8>作者：</font>** Fenghua Yang, Preet Baxi, Yi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Firms making inventory decisions have access to operational data, optimization tools, and large language models (LLMs). Typically, data characterize the operating environment, optimization selects parameters within a prespecified inventory policy class, and LLMs support coding and decision analysis. We develop an integrated framework that combines these resources to automate inventory policy design. Given demand data, the framework iteratively uses an LLM to generate parameterized policy classes and an external solver to optimize its parameters within each class. Across 30 lost-sales inventory instances, the mean cost reduction relative to optimized base-stock benchmarks increases from 17.5% after one generation to 30.0% after ten generations. Parameter optimization is central to this performance: an LLM-only variant performs substantially worse, whereas optimization-guided feedback improves policy quality, accelerates search, and directs the LLM toward better policy classes rather than merely better parameter values within a fixed class. The strongest discovered policies are also interpretable: they combine recognizable inventory-control motifs, including capped orders, discounted or weighted pipeline inventory, and threshold-based replenishment logic. The search thereby produces new policy-class functional forms that, to our knowledge, have not previously been studied in the lost-sales inventory literature. These functional forms are not specified ex ante but emerge from the search process. Moreover, after their parameters are re-optimized, three discovered policy classes achieve average cost reductions of 21.75% to 22.60% across 10,064 new inventory instances. Overall, the results show that data-driven parameter optimization can guide LLM-based search over a broad space of inventory policy classes and identify high-performing, interpretable, and transferable decision rules.

---


### 329. [VI-Bench: Benchmarking Prompt Inversion from AIGC Videos](https://arxiv.org/abs/2609.08079)

**<font color=#1a73e8>作者：</font>** Wulin Xie, Rui Zhao, Kecen Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation have made prompt-based control increasingly central to AIGC video generation. Prompts specify what a video should depict and how it should be represented, controlling factors such as visual style or camera behavior. Understanding this recoverability is important both for creative reuse and editing, and for assessing prompt leakage risks. However, existing video understanding benchmarks do not measure this capability: a caption may describe what is visible, but a replayable prompt must recover the generation-relevant controls needed to reproduce the video. To address this gap, we introduce VI-Bench, a benchmark built from 16.1 million real-user prompts and 900 human-verified AIGC videos. VI-Bench spans three progressively harder settings, namely single-shot semantic grounding, control over style and camera behavior, and multi-shot compositional inversion, and evaluates five generation-critical dimensions: subject, action, scene, style, and camera. We evaluate 18 representative VLMs, including 2 proprietary and 16 open-source models on VI-Bench, using an Inversion Score that measures prompt-level alignment with the original prompt and video-level fidelity of the regenerated video. The results reveal substantial limitations: even the strongest model achieves only 0.632 on Inversion Score, performance degrades sharply as samples require richer control and multi-shot reasoning, and models often produce plausible prompts whose regenerated videos deviate from the reference. These findings show that video prompt inversion is a distinct and under-evaluated capability requiring models to transform visual understanding into replay-stable generative control.

---


### 330. [LLM-Based Penetration Testing in the Presence of Honeypots](https://arxiv.org/abs/2609.08093)

**<font color=#1a73e8>作者：</font>** Xinhong Xie, Piyush Nagasubramaniam, Neeraj Karamchandani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly employed for offensive cybersecurity tasks such as automated vulnerability discovery, reconnaissance, and penetration testing. This new capability also threatens one of the defender's most valuable tools: deception. Traditional honeypots rely on realism and obscurity to lure human or script-driven attackers into revealing tactics, techniques, and procedures (TTPs), but LLM-driven attackers can reason about heterogeneous artifacts and use the honeypot suspicion to guide target-selection decisions.
We present a systematic study of honeypot-aware budget allocation for LLM attack agents. We formalize the attacker's problem as a budgeted decision process: an agent interacts with potential targets, consuming LLM execution budget during reconnaissance and exploitation, and must decide whether to (continue exploitation) or (skip) when honeypot suspicion arises.
Our findings show that with the proposed detector-guided policy, LLM agent attackers can effectively allocate budget to compromise hosts in a host pool, highlighting the importance of dynamically allocating budget in a controlled mixed-host testbed. While defenses are beyond our present scope, we discuss implications for future adversarially resilient and adaptive honeypot design.

---


### 331. [CIVI: A Framework for Diagnosing Search Agent Failures in Civic Information](https://arxiv.org/abs/2609.08094)

**<font color=#1a73e8>作者：</font>** Dingying Liu, Yunshun Zhong, Wentao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models are increasingly deployed in public-sector settings, where incorrect guidance can cause irreversible harm. We introduce CIVI, the first framework for diagnosing search agent failures in civic information. Its benchmark instantiation jointly spans cross-national, interjurisdictional government contexts (federal, state, and local) and functional categories from an internationally adopted United Nations standard. We evaluate ten frontier search agents and find that none matches an attentive human baseline. Alongside accuracy, CIVI measures search invocation rate, selective no-search accuracy, and how often agents cite authoritative government sources. To perform this diagnosis, we introduce ARISE, which decomposes agentic search failures into four mutually exclusive modes, isolated via source-injection ablation. ARISE attributes 72.1% of all observed failures to retrieval-bound causes rather than to gaps in the models' parametric knowledge.

---


### 332. [Router Prior Bias: Preserving Base Routing Structure in MoE Post-Training](https://arxiv.org/abs/2609.08115)

**<font color=#1a73e8>作者：</font>** Jaedeok Lee, Keonwoo Kim, Dongyoon Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) pretraining relies on an auxiliary load-balancing loss (LBL) to drive per-expert utilization toward uniformity. Post-training inherits a different situation: the base router already encodes non-uniform expert co-activation structure, which a re-imposed uniformity objective flattens away. We show that downstream performance depends instead on holding this inherited routing softly, a principle we term soft router anchoring, and instantiate it as Router Prior Bias (RPB), a training-time bias that pulls the router logits toward a prior read off the frozen base router while leaving the router itself trainable. On math post-training of Moonlight-16B-A3B, RPB attains 45.77 in-domain accuracy against 31.91 under re-applied LBL and 29.44 under unanchored fine-tuning, and retains more out-of-domain capability than either. The ordering against LBL reproduces on a second model family (Qwen3-30B-A3B-Base), and the advantage over LBL is resolvable on an independently sourced corpus. Anchors defined on the router weights, on its logits, or on its output distribution perform comparably with no consistent ordering, which places the effect in the softness of the constraint rather than in the particular prior RPB supplies. Retained community structure in the expert co-activation graph tracks these gains wherever the base router is non-uniform enough for communities to form, yet enforcing the same prior as a hard assignment preserves that structure while performance falls sharply. Community structure is therefore a footprint of soft anchoring rather than its source, and the practical lesson is that inherited routing should be held softly during post-training, since both flattening it toward uniformity and enforcing it absolutely carry a downstream cost. Our code will be released at this https URL.

---


### 333. [SchemeArena: Factorized Stress Testing of Scheming in LLM Agents](https://arxiv.org/abs/2609.08126)

**<font color=#1a73e8>作者：</font>** Jie Ruan, Inderjeet Nair, Amy Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study scheming in LLM agents, in which agents covertly pursue misaligned goals. Our focus is to understand how scheming arises from the interaction of key factors, such as instrumental goals, environmental affordances, oversight conditions, and perceived consequences. Prior work examines only a small number of scenarios, limiting the ability to isolate how these conditions shape an agent's propensity or capability to scheme. This limited scale and task diversity also restrict coverage of realistic deployment settings and the range of scheming strategies that can be observed. To this end, we introduce SCHEMEARENA, a 400-scenario benchmark for scalable scheming stress testing, constructed through a factorized scenario synthesis framework spanning diverse safety-relevant tool domains, instrumental goals, oversight conditions, and pressure mechanisms. To enable scalable and reliable monitoring, we further propose SCOUT, a scheming monitor that grounds multi-criteria judgments in evidence drawn from agents' reasoning and actions. Across controlled stress tests on five LLM agents, we find that explicit instrumental goals are the strongest driver of scheming propensity. Strategic hints play a distinct role by helping agents translate scheming reasoning into concrete covert behavior. Oversight has mixed effects: in several closed models, action-only monitoring increases scheming, suggesting that partial oversight can act as an optimization constraint rather than a deterrent. CoT is a useful but incomplete monitoring signal: it can reveal latent scheming before execution, yet action-only scheming shows that covert behavior may occur without explicit reasoning evidence. We release the benchmark, code, and monitor at: this https URL.

---


### 334. [Observe Before You Alert: Adaptive Driver Alerting with Vision-Language Models](https://arxiv.org/abs/2609.08130)

**<font color=#1a73e8>作者：</font>** Yuhang Wang, Lingyao Li, Hao Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driver alerting from dashcam video requires sequential decision-making under partial observability: a system must decide not only whether a scene is risky, but also when the evidence is sufficient to warn. Most existing accident anticipation models output a binary risk score, leaving ambiguous scenes to be handled by thresholding. We propose VLAlert, a vision-language alerting framework that casts warning generation as a tri-action policy over SILENT, OBSERVE, and ALERT. The OBSERVE action acts as an internal evidence-gathering decision that delays uncertain warnings and changes the next observation window, creating a lightweight perception-action loop for adaptive alerting. VLAlert uses Qwen3-VL-4B as a safety-evidence generator and pools hidden states from structured belief spans to form compact representations for danger estimation and policy prediction. We evaluate VLAlert on VLAlert-Bench, a unified per-tick benchmark from four real-world dashcam alert datasets, and further test transfer to held-out naturalistic ADAS takeover clips. On VLAlert-Bench validation, VLAlert achieves the highest deployment-oriented utility among tested baselines, with DAUS 0.4878 compared with 0.4752 for Open-BADAS, and improves AUROC, AP_tick, F1_t, and balanced accuracy from 0.610, 0.176, 0.276, and 0.581 to 0.689, 0.195, 0.297, and 0.648, respectively. On 221 held-out ADAS-TO-Critic clips, VLAlert improves R@5s from 74.2% to 88.7% and F1 from 0.585 to 0.686. These results indicate that adaptive observation and safety-focused VLM representations provide measurable gains for driver-facing alert decisions.

---


### 335. [Jacap: Robust KV Cache Eviction via Jacobian-Based Nonlinear Information Capacity Preservation](https://arxiv.org/abs/2609.08131)

**<font color=#1a73e8>作者：</font>** Jiaming Yang, Chenwei Tang, Liangli Zhen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) cache eviction is essential for scaling long-context inference in Large Language Models. However, existing policies predominantly rely on empirical heuristics, lacking a rigorous characterization of token utility under the inherently nonlinear softmax attention mechanism. In this work, we rethink KV cache eviction through the lens of local information geometry, modeling the attention process as a nonlinear Gaussian communication channel. By performing a first-order Taylor expansion of the attention mapping, we derive the Jacobian Information Capacity, a novel objective that explicitly captures query relevance, softmax sensitivity, and structural diversity. Guided by this theory, we introduce Jacap, a capacity-aware eviction method that utilizes softmax-aware importance weighting and statistical leverage scores for subset selection. Extensive experiments across diverse architectures and benchmarks demonstrate that \textsc{Jacap} delivers superior performance in most scenarios, particularly in high-compression regimes.

---


### 336. [ConversationalVoice: Full-Duplex Speech Data from Real Conversations through Source-Faithful Reconstruction and Conversation-Grounded Expansion](https://arxiv.org/abs/2609.08147)

**<font color=#1a73e8>作者：</font>** Richard Yucheng He, Baodong Cao, Chen Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech models require training data that preserves turn-taking, overlap, interruption, and backchannel behavior, yet these signals are entangled across speakers in noisy real-world recordings. We present Conversational Voice, a pipeline that converts real two-speaker excerpts into three complementary training-data artifacts. (1) Separation recovers speaker-specific tracks with stable speaker assignments, a canonical transcript, and naturally observed interaction timing. (2) Reconstruction generates speech in matched voices from a fixed source transcript, reconstructs the source turn order, pauses, and overlaps, and adds word-level alignment and delivery instructions. (3) Expansion generates new dialogue constrained by the source context, speakers, and observed interaction pattern. Automatic speaker-verification metrics remain strong across stages, with same-speaker similarity of 0.983-0.991 and positive discrimination margins of 0.199-0.209. Predicted speech quality (NISQA MOS) is 3.56 for separation, 4.41 for reconstruction, and 4.61 for expansion. A Gemini-based automatic evaluator assigns expansion mean scores of 4.94/5 for contextual coherence and 4.80/5 for dialogue naturalness. Expansion and reconstruction exhibit broadly similar interaction profiles; expansion's turn, overlap-event, backchannel, and interruption rates are 4.6%, 8.0%, 13.2%, and 16.0% lower, respectively. We evaluate data properties only; downstream gains in full-duplex model training remain for future work.

---


### 337. [SciFigure2Code: An AI-Reconstructed Benchmark for Scientific Figure-to-Code](https://arxiv.org/abs/2609.08155)

**<font color=#1a73e8>作者：</font>** Wentao Li, Yibo Wu, Yizhe Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific figures are the interface through which research claims are inspected and reused, but final published panels rarely expose the data or plotting code that produced them. Recovering this hidden provenance from pixels is therefore underdetermined. We introduce SciFigure2Code, an AI-reconstructed benchmark that instead evaluates presentation recovery: generating editable Python programs that preserve how a scientific panel is arranged and read. Role-specialized Codex agents generate, execute, visually refine, and audit silver-standard presentation programs that capture geometry, visual hierarchy, encodings, annotations, and typography without claiming to recover original measurements or author source code. This reconstruction-and-audit protocol turns final published panels into auditable reference packages; the resulting resource contains 6,740 reviewed panels and SciFigureBench, a balanced 337-panel test set across 31 chart subtypes, five domains, and three complexity levels. Across 14 zero-shot models in image-only and caption-assisted settings, execution, multi-component layouts, axes, legends, and scientific labels remain weak. Claude Opus 4.7 achieves the highest image-only Overall score, Claude Opus 4.6 leads caption-assisted reconstruction, and two-stage plan-then-code prompting improves Overall for all four tested models. SciFigure2Code provides an auditable testbed for agents that construct editable, visually faithful scientific figure presentations.

---


### 338. [When Metrics Reward the Worst Translations: Internalizing Cultural Reasoning for Social Media Translation Evaluation](https://arxiv.org/abs/2609.08156)

**<font color=#1a73e8>作者：</font>** Yiwen Qiu, Linjuan Wu, Dingming Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic translation quality metrics trained on general-domain corpora systematically fail on social media content, where communicative intent is encoded in culturally loaded expressions (internet slang, homophonic ciphers, and platform-specific idioms) rather than surface token patterns. We conduct a systematic empirical analysis demonstrating that standard metrics including COMET, XCOMET, and BERTScore exhibit near-zero or negative correlation with human cultural judgments, and even display a severity inversion in which scores increase as translation quality deteriorates. We further show that this failure extends to large language model judges: Qwen3-235B achieves Cohen's kappa of only 0.162, revealing that the bottleneck is not reasoning capacity but cultural grounding: models lack the domain-specific cultural knowledge needed to identify which aspects of a translation require scrutiny. To address this, we propose CuRIL, a reinforcement learning framework that internalizes cultural reasoning: cultural annotations are prepended inside the model's reasoning, excluded from policy gradients via a token-level loss mask, and injected with a probability that decays to zero over training, progressively forcing autonomous cultural judgment. On a 1,444-sample human-annotated social media translation benchmark, Qwen3-8B trained with CuRIL achieves Cohen's kappa 0.370 and Exact Match accuracy of 45.22%, approaching Gemini-3.1-Pro with 30x fewer parameters and surpassing models up to 235B in scale. We further demonstrate that our judge produces reliable reward signals for downstream translation optimization, reducing the low-quality translation rate by over 20 percentage points under independent human evaluation.

---


### 339. [WorldAgen: Unified State-Action Prediction with Test-Time World Model Training](https://arxiv.org/abs/2609.08162)

**<font color=#1a73e8>作者：</font>** Chi Wan, Kangrui Wang, Yuan Si 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How can vision-language-action (VLA) models adapt to new environments where world dynamics shift? While recent research has combined world modeling and action prediction to improve VLA performance, existing methods largely rely on pretraining on static datasets, without mechanisms for active adaptation at deployment time. As a result, these models often fail to generalize when deployed in unseen scenarios with novel object configurations or dynamics. We present WorldAgen, a unified framework that jointly learns world modeling and action prediction while enabling Test-Time Training (TTT) to adapt to new environments. WorldAgen employs a shared Transformer backbone with two heads: (1) a world model head that predicts future states from past state-action trajectories, and (2) an agent model head that predicts actions conditioned on task instructions. We design a Mixed Unidirectional Attention Mask to separate these two models. During test time, WorldAgen samples exploratory actions, collects ground-truth state transitions, and performs lightweight TTT updates to refine its world model. This adaptation improves the model's understanding of the environment and leads to more accurate action predictions. Experiments on the CALVIN and LIBERO benchmarks demonstrate that our baseline model achieves comparable, and in some cases superior, performance to current state-of-the-art approaches. Moreover, with TTT on a small number of samples, our method surpasses existing state-of-the-art models, highlighting the effectiveness of adapting world models at inference time.

---


### 340. [EviSI: An Evaluation Agent for Simultaneous Interpreting](https://arxiv.org/abs/2609.08171)

**<font color=#1a73e8>作者：</font>** Ben Yan, Zongyao Li, Daimeng Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simultaneous speech-to-speech translation requires understanding, translation and spoken delivery while the source stream continues. To support timely delivery and limit accumulated delay, systems adopt reformulation and summarization, which can preserve meaning while departing from written references. BLEU and COMET may not reliably distinguish such variation from semantic loss. We introduce EviSI, a large language model evaluation agent adapting the error analysis and penalty principles of Multidimensional Quality Metrics (MQM). It constructs shared source evidence, assesses semantic fidelity and oral expression, reconciles overlapping errors and scores deterministically. EviSI recovers the aggregate human system ranking for English to Chinese. Mean Kendall agreement with human system rankings within corpora reaches 0.707 for English to Chinese and 0.467 for Chinese to English, exceeding evaluated baselines. An extension across five directions shows positive concordance with COMET without human ratings. Individual output agreement with humans remains mixed.

---


### 341. [Key Path Identification for Resolving Knowledge Conflicts via SAE-based Steering](https://arxiv.org/abs/2609.08173)

**<font color=#1a73e8>作者：</font>** Wenbo Zhang, Zhongxiang Sun, Zhiguang Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoder (SAE)-based steering has been widely used to address knowledge conflicts by guiding LLMs to be more faithful to the contextual knowledge. Existing methods usually perform mass steering, which modifies a large batch of SAE features identified via correlation-based methods. However, due to the inaccurate correlation and the neglected feature interactions, mass steering methods fail to precisely identify the features that play the key roles in steering and introduce a large number of redundant ones, which add noise and weaken the steering effects. Our empirical studies reveal that steering only a small subset of the identified features can achieve comparable or even better performance. Motivated by this finding, we propose Key Path Identification (KPI), a novel method that identifies key steering features characterized by strong causal dependencies with both upstream and downstream features. From these features, KPI constructs key paths and steers through less feature modifications. In this way, KPI advances SAE-based steering from quantity-driven to quality-focused, offering a perspective for more precise and interpretable model editing. Experiments in RAG tasks with knowledge conflicts show that our method improves the accuracy by 18% on average compared to the best baseline of mass steering, effectively filtering redundant features, alleviating side effects and demonstrating the core role of key paths in steering.

---


### 342. [OntologyBench: Can Dense Retrieval Satisfy Structured Biomedical Constraints?](https://arxiv.org/abs/2609.08174)

**<font color=#1a73e8>作者：</font>** Xiao Yu Cindy Zhang, Wyeth Wasserman, Jian Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce OntologyBench, a tiered biomedical retrieval benchmark comprising 471,854 training and 125,744 evaluation query-document relevance pairs across concept grounding, relational retrieval, and compositional phenotype-based retrieval.
Although these tasks can be tractable using ontology-aware reference methods, across task tiers, embedding performance is generally lower on relational and compositional tasks than on concept-grounding tasks. Fine-tuning on ontology-derived supervision improves performance on several relational and compositional tasks, whereas the evaluated reranking and LLM-based candidate-scoring methods provide little or no end-to-end improvement. Errors frequently reflect diseases matching only subsets of the phenotype evidence.
These findings indicate that the evaluated embedding and reranking configurations do not reliably recover the compatibility encoded by the selected ontology relations and phenotype combinations and motivate retrieval systems that better integrate learned representations with structured biomedical knowledge.

---


### 343. [Safe Harness Self-Evolution: A Theoretical Analysis of Feasibility and Limits](https://arxiv.org/abs/2609.08175)

**<font color=#1a73e8>作者：</font>** Qianshu Cai, Yonggang Zhang, Jun Nie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness self-evolution is the process by which an agent modifies its prompts, tools, code, or orchestration in response to task feedback while keeping the underlying language model frozen, with changes persisting across subsequent tasks. We provide a systematic theoretical analysis of the feasibility and limits of safe harness self-evolution, connecting modification generation, finite-data certification and selection, safe adoption, and behavior after an update. Under a fixed user-task distribution, we establish conditions guaranteeing overall expected-reward improvement while controlling changes on retained tasks, characterize the probability of generating qualified modifications, and derive finite-data bounds for safe selection and adoption. Our analysis shows that generation and certification impose distinct constraints: current task performance does not determine the probability of generating qualified modifications, and generating more candidates need not improve the guarantee of a successful update when evaluation is limiting. Stagnation may therefore arise even when improvement opportunities remain. We further show that worst-case evaluation cost for recognizing genuine improvements diverges as expected reward approaches its upper bound. Across successive updates, certified improvement guarantees accumulate over a finite run, but a successful update does not by itself guarantee that further improvement remains possible. These results provide a basis for diagnosing bottlenecks and designing safer self-evolution mechanisms.

---


### 344. [Less Is Personal: Learning Minimal Sufficient User Profiles for Personalized Language Models](https://arxiv.org/abs/2609.08180)

**<font color=#1a73e8>作者：</font>** Minghang Liu, Qiang Qiu, Yuanzhuo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented personalization enables large language models to produce more accurate and preference-aligned outputs using relevant records retrieved from user histories. Personalized language models typically prepend a fixed number of retrieved user records, even when additional history is redundant, harmful, or unrelated to a user's distinctive behavior. We study minimal sufficient personalization: constructing the least costly ordered profile for each input while preserving the utility achievable from a retrieved candidate pool. We introduce ENOUGH, a method that iteratively appends behavioral records or emits STOP to construct profiles with adaptive lengths. Offline, bounded counterfactual search evaluates profile prefixes by jointly considering downstream gains, user specificity, and token costs. The resulting long-horizon targets are distilled into a multi-head value controller with explicit ranking and stopping supervision. At inference, the controller selects and orders records through lightweight decisions, and the frozen generator is invoked once after stopping. Extensive experiments on six personalized tasks demonstrate that ENOUGH consistently outperforms strong heuristic and retrieval-augmented baselines in both effectiveness and efficiency, achieving minimal sufficient profiles that preserve personalization utility while reducing unnecessary context costs.

---


### 345. [Does Deeper Reasoning Compromise Alignment? Revealing and Mitigating of Alignment Collapse in Large Reasoning Models](https://arxiv.org/abs/2609.08186)

**<font color=#1a73e8>作者：</font>** Yu-Hang Wu, Yu-Jie Xiong, Henghua Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The emergence of Chain-of-Thought (CoT) has established a robust foundation for Large Reasoning Models (LRMs). While deep reasoning is widely believed to enhance safety alignment, the stability of alignment mechanisms under extended reasoning remains underexplored. This paper challenges the prevailing view by revealing a critical vulnerability: Deep Reasoning May Induce Alignment Collapse. To rigorously quantify this phenomenon, we propose the Alignment Loss Rate (ALR) metric. Our experiments demonstrate that as reasoning depth increases, ALR rises significantly, indicating a severe degradation in model robustness against external perturbations. Capitalizing on this instability, a novel jailbreaking paradigm, Reasoning Trap (RT), is proposed. RT induces the model into extended reasoning to amplify the impact of adversarial attacks, leading to a sharp decline in safety capabilities. To elucidate the mechanism behind this collapse, we identify Attention Dilution as the root cause, arising from the competition for attention between the extended reasoning process and the original input. To mitigate this, Reasoning Residual Alignment (RRA), a lightweight defense strategy that dynamically re-emphasizes the input via residual connections integrated with the reasoning process.

---


### 346. [Bridging the Semantic-Utility Gap in Multimodal RAG via Generator-in-the-Loop Alignment](https://arxiv.org/abs/2609.08188)

**<font color=#1a73e8>作者：</font>** Zhan-Lun Chang, Dong-Jun Han, Seyyedali Hosseinalipour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) augmented with retrieval-augmented generation (RAG) benefit from access to external evidence. However, standard retrievers and rerankers optimize for semantic similarity rather than answer utility, creating a preference gap: documents that appear relevant may not help the generator produce a correct answer. Motivated by this, we propose a two-stage generator-in-the-loop alignment framework that closes this gap without human document-level relevance annotations. Our framework consists of two stages: in Stage 1, a VLM generates a hypothetical text passage from the image-query pair, which is used as the retrieval query for dense text search, bridging the image-to-text modality gap. In Stage 2, a cross-encoder reranker adapted with low-rank adaptation (LoRA) is fine-tuned using answer-supervised preference pairs mined from the frozen VLM: given the dataset answer label, a candidate document is labeled positive if the VLM produces the correct answer when given that document as context, and negative otherwise. This generator-guided signal is compatible with multiple alignment loss functions, including contrastive (triplet) loss, pairwise direct preference optimization (DPO), and supervised fine-tuning (SFT), and supports periodic re-mining to refresh preference pairs as the reranker improves. Experiments on VQA-X and A-OKVQA with Qwen3.5-2B and Qwen3-VL-4B-Instruct show that our proposed framework consistently outperforms rank-order, random, and REPLUG-style likelihood baselines under various alignment losses and pool size settings, suggesting that answer-level generator feedback is an effective supervision signal for preference alignment.

---


### 347. [Do Dynamic Routers Need Memory? HeRo: History-Aware Routing for Efficient LLM Inference](https://arxiv.org/abs/2609.08189)

**<font color=#1a73e8>作者：</font>** Hongjin Lin, Wentao Wan, Keze Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dynamic layer routing reduces the inference cost of Large Language Models (LLMs) by learning to skip layers for individual tokens. Existing methods, however, treat each routing decision as a local operation conditioned solely on the current hidden state which is a formulation that overlooks the sequential, path-dependent nature of routing across depth: earlier decisions shape the representations seen by downstream routers, and the layer-usage objective couples all decisions jointly. We propose History-Aware Routing (HeRo), a dynamic routing framework that resolves this mismatch by introducing a router memory mechanism to maintain an explicit routing state across model depth. The memory is constructed via linear attention, incrementally aggregating preceding routing scores and their induced residual updates into a compact history representation. At each routed layer, the router conditions jointly on this accumulated state and the current hidden representation to select the executed branch. Instantiated for token-wise FFN routing, HeRo trains only lightweight routers and adapters on a frozen backbone, requiring no modification to pretrained parameters. Across Llama 3.1-8B, Llama 2-7B, and Llama 2-13B, HeRo consistently achieves the highest aggregate performance retention among ten baselines. On Llama 3.1-8B, it bypasses 26.87% of model parameters while achieving 100.24% of dense model performance across seven benchmarks, and retains 97.01% while bypassing 38.82% of model parameters under a tighter computation budget. Ablation studies confirm that removing routing history consistently degrades performance, most notably on multistep reasoning and code generation, validating that explicit routing memory enables more accurate and adaptive dynamic routing than solely conditioning on hidden state.

---


### 348. [Qiushi Engine on AstaBench E2E-Bench-Hard](https://arxiv.org/abs/2609.08196)

**<font color=#1a73e8>作者：</font>** Wenhao Li, Shuxing Yang, Fujia Chen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This report analyzes Qiushi Engine v0.8 across all 40 test tasks in AstaBench E2E-Bench-Hard, a benchmark that requires autonomous agents to carry a research question through experimental design, code implementation, actual execution, result analysis, and report delivery. Qiushi Engine is model-configurable; this evaluation selected DeepSeek deepseek-v4pro-preview as the model backend. The official AstaBench leaderboard records a score of 0.816 and an average benchmark cost of USD 15.209 per task, while the full-precision local recomputation is $81.59 \pm 1.87$. Four tasks satisfied every rubric item, yielding a full-task completion rate of 4/40 = 10% -- 7 percentage points above, and about 3.3 times, the approximately 3% best rate reported for AstaBench's official agents. Across 507 required rubric items, 416 were satisfied (82.1%). Official scoring archives and 40 Meta-Trace records show sustained production and verification of reports, code, and experimental artifacts; the principal gaps lie in repeated runs, external dependencies, specified metrics, and ablation studies. The report explains the benchmark, system workflow, aggregate results, representative cases, and limits of interpretation.

---


### 349. [SIM: Subspace Interaction-based Method for Token-Level Text Anomaly Detection](https://arxiv.org/abs/2609.08200)

**<font color=#1a73e8>作者：</font>** Kehan Yan, Yue Tan, Qingfeng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Token-level text anomaly detection, as an emerging trend of text anomaly detection, moves beyond coarse-grained document-level detection by localizing anomalous tokens within text. By providing fine-grained abnormality prediction, token-level text anomaly detection plays a critical role in various real-world applications, such as spam filtering and fake news detection. However, existing methods still rely on the global distance calculation for scoring, during which the local anomaly signals are severely diluted by numerous redundant normal feature dimensions. Moreover, pre-trained language models used in these methods inevitably smooth out surface anomalies, further limiting their effectiveness in token-level anomaly detection. To address these limitations, we propose a Subspace Interaction-based Method (SIM for short) for token-level text anomaly detection. To prevent local signal dilution, SIM adopts a subspace interaction-based anomaly detector, which decouples high-dimensional token embeddings into multiple low-dimensional ones, amplifying localized anomaly signals hidden within specific dimensions. To counteract the over-smoothing effect, we design a hard pseudo-anomaly generation module to construct pseudo-anomalous tokens, simulating the subtle anomalies obscured by semantic smoothing. Also, a probabilistic boundary loss is developed to standardize anomaly scores into statistical distances, effectively enforcing anomalous instances to deviate significantly from the normal distribution center. Extensive experiments on multiple benchmark datasets verify the effectiveness of SIM and demonstrate its remarkable efficiency, robustness, and interpretability. The source code is available at: this https URL.

---


### 350. [Vision: Data-Centric Anchoring for Robust and Interpretable Agentic AI](https://arxiv.org/abs/2609.08216)

**<font color=#1a73e8>作者：</font>** Arun Vignesh Malarkkan, Xinyuan Wang, Yanjie Fu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems built on large language models fail in two persistent ways that scaling does not fix: they break under distribution shift, and they cannot explain the decisions they make. We argue these are co-symptoms of one structural deficiency in the data lifecycle that governs how agents are trained, evaluated, and deployed. Observational interaction logs record what an agent did, not what it would have done otherwise. They encode spurious correlations without controlled variation, so they lack the counterfactual structure needed to separate causal signal from coincidence or to validate an explanation. No model-centric method can recover invariances the data never contained. We present Data-Centric Anchoring: robustness and interpretability should be engineered into the data environment, not extracted from models after training. Our central contribution is the Data-Centric Agentic Loop, a four-stage framework of Curate, Augment, Constrain, and Attribute. The ordering is structural, not stylistic. Curation precedes augmentation because generative models amplify whatever bias they are trained on. Augmentation precedes constraint because invariance objectives are vacuous without variation across environments to be invariant to. Attribution closes the loop, converting observed failures into targeted data interventions for the next iteration. Each stage manufactures the preconditions of the next, which makes the loop self-correcting rather than merely sequential. We ground the framework in a failure-driven taxonomy that links four core failure modes to the data lifecycle: spurious feature reliance, distribution-shift fragility, uncertainty miscalibration, and explanation unfaithfulness. We close with the limits of this approach and the open problems that stand between it and practical deployment at scale.

---


> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
