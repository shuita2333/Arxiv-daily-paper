# 🧠 大模型相关研究 | 2026年11月11日

> 本类共 **438** 篇论文：已确认 **405** 篇，待复核 **33** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 51. [AutoEMatic: Runtime-Adaptive Mixed-Precision LLM Inference via Automatic Exponent-Mantissa Refinement](https://arxiv.org/abs/2611.10165)

**<font color=#1a73e8>作者：</font>** Akshat Ramachandran, Reena Elangovan, Rangharajan Venkatesan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing LLM post-training quantization techniques determine precision before inference begins, yet the precision a model requires varies dynamically across prompts, layers, and inference phases. We present AutoEMatic, a full-stack co-design that adapts the precision of weights, activations, and the KV cache at runtime. A lightweight policy selects each layer's precision at every prefill and decode step from two runtime signals: the entropy of the next-token distribution and the magnitude of each layer's update to its hidden states. This runtime adaptation is made practical by AutoFP, a multi-scale floating-point format that derives 2-, 4-, and 6-bit precisions from a single NVFP4 base format. We realize AutoEMatic on two targets: GPU kernels that execute AutoFP on NVFP4 Tensor Cores, and an accelerator whose vector MAC datapath executes all AutoFP formats natively. Across reasoning and agentic benchmarks, AutoEMatic improves accuracy by up to 21.7% over NVFP4 and matches group-scaled FP6 accuracy on most benchmarks, using 4.9 bits per weight versus 4.5 for NVFP4. On GB300 GPUs, AutoEMatic retains approximately 90-98% of NVFP4 decode throughput across the evaluated configurations. Furthermore, the AutoEMatic accelerator reduces latency by 1.6-2.3x and energy by 7-23% compared to an accelerator with NVFP4-only datapath at iso-accuracy.

---


### 52. [CXR-CMFA: A Cross-Modal Feature Aggregation Network for Chest X-Ray Pathology Classification](https://arxiv.org/abs/2611.10174)

**<font color=#1a73e8>作者：</font>** Talukder Hasnat Zadid, Jahin Sultana, Felipe Bochini Brisola 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest X-ray (CXR) interpretation remains challenging because subtle pathology can be obscured by overlapping anatomy, image-quality variation, and limited visual evidence in isolated radiographs. Although image-only deep learning models provide useful baselines, they discard the complementary diagnostic context available in radiology reports, while large vision-language models can be computationally expensive for practical deployment. This paper presents CXR-CMFA, a lightweight cross-modal feature aggregation network for binary CXR pathology classification. The proposed framework combines a dual-stream visual encoder, using EfficientNet-B0 for global anatomical representation and DenseNet-121 for local pathological detail, with a TF-IDF-MLP report encoder. Two fusion modules integrate these modalities: the Dual-Modal Spatial Attention Module (DMSAM) uses the report embedding to gate global and local visual features, and the Cross-Modal Gated Feature Fusion (CGFF) module learns per-instance weights for visual and textual contributions. Experiments on the MIMIC-CXR benchmark, using the provided train, validation, and test splits, show that CXR-CMFA achieves 93.45% accuracy, 99.88% precision, 91.8% recall, 95.7% F1-score, and 99.19% AUC on the held-out test set. The model produces only four false positives among 984 normal test cases, supporting its suitability for high-specificity screening workflows. An ablation study further demonstrates a 22.47 percentage-point AUC improvement over the global-image-only variant, confirming the value of adaptive cross-modal fusion. These results indicate that compact report-conditioned fusion can provide strong discriminative performance without relying on large pretrained language models.

---


### 53. [ASCENT: Scale-Complementary External State for Frozen Long-Context Language Models](https://arxiv.org/abs/2611.10175)

**<font color=#1a73e8>作者：</font>** Xingjian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> External state should become more valuable as a reader becomes more capable, yet long-context evaluations measure memory utility at a single model scale. This paper formulates scale complementarity: the absolute gain from external state increases when reader capacity and a compact state budget are jointly scaled. ASCENT realizes this principle with a target-blind causal writer, nested typed state, and a bounded query-conditioned readout; every language model remains frozen. Under log loss, the value of a nested refinement equals its target-relevant conditional information; a full factorial makes the reader-by-state interaction identifiable. Official 16K BABILong experiments show Qwen2.5 accuracy gains of 10.50, 78.88, and 82.63 percentage points at 0.5B, 1.5B, and 3B parameters, with both adjacent directional contrasts significant after family-wise correction. At 7B, Foundation accuracy rises to 33.25% while four-slot ASCENT answers every question, which caps the gain at 66.75 points; the 3B-to-7B accuracy increment is -15.88 points [-20.55, -11.20]. The accuracy-side claim is therefore established from 0.5B to 3B; the 7B conclusion rests on the non-saturated negative-log-likelihood factorial. A three-model by three-state factorial yields co-scaled negative log-likelihood gains of 0.388, 2.099, and 7.406 nats at 1.5B, 3B, and 7B; all interaction and gain contrasts retain positive simultaneous lower bounds. Five public 7B-8B readers obtain 66.75-85.63 point gains, and ASCENT exceeds task-trained retrieval checkpoints at the two larger shared scales. Controls, baselines, systems accounting, matched-hardware reproduction, and a cross-architecture sensitivity analysis accompany the experiments. The results establish scale-complementary external state under the evaluated benchmarks, metrics, and state schema.

---


### 54. [AVCORP: Identifying and Resisting Deception via Communication Theory and Theory of Mind](https://arxiv.org/abs/2611.10176)

**<font color=#1a73e8>作者：</font>** Fardin Saad, Zhe Zhang, Sanjana Cheerla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Today's LLM-based agents are vulnerable to deception by users and other agents. Defending against deception requires Theory of Mind (ToM) reasoning to infer the beliefs and goals of others as well as modeling tactics based on communication theory. To enable training models to detect deception, we adopt the well-known deception game, Avalon. We present a corpus, AVCORP, of 5,000 annotated utterances from 250 games of Avalon. AVCORP includes (1) 37 tactics mapped to a 4x4 behavior matrix, and (2) reasoning traces capturing abductive hypotheses, suspicion levels, and nested ToM beliefs. We train Qwen3-8B on AVCORP and evaluate it on 25 held-out games and 20 games played by humans. On held-out games, our best trained detector outperforms its untrained baseline and frontier models (GPT-5.6 Sol, Gemini 3.1 Pro, DeepSeek-V4-Pro), matching Claude Opus 5.5. On human games, every trained detector exceeds the untrained model in F1 score across all rounds.

---


### 55. [BiMuon: A Geometry-Aware Stochastic Bilevel Optimization Approach](https://arxiv.org/abs/2611.10188)

**<font color=#1a73e8>作者：</font>** Zhen Qin, Zhiyao Zhang, Yingbin Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic bilevel optimization provides a general framework for many machine learning applications, such as hyperparameter learning, data reweighting, language model alignment, and actor-critic reinforcement learning. However, most existing bilevel optimization methods treat matrix-valued gradients as flattened vectors and perform optimization in the resulting vectorized space, ignoring the matrix structures common in modern neural networks. Moreover, the lower-level (LL) problem curvature can induce significant spectral imbalance in the upper-level (UL) geometry. Such limitations of existing bilevel optimization methods motivate us to develop BiMuon, a geometry-aware stochastic bilevel optimization method that integrates implicit hypergradient estimation in bilevel optimization with Muon-style orthogonalized updates at the UL. To our knowledge, BiMuon is the first stochastic BLO method with Muon-style orthogonalized matrix updates and an $O(\epsilon^{-4})$ iteration-complexity guarantee, matching the best-known rates achieved by Muon-type methods based on matrix parameterizations. To improve computational and parallel efficiency for models with multiple matrix parameters, we further study BiMuon for blockwise diagonal matrix approximation and derive a relative stepsize allocation rule based on UL progress and blockwise LL sensitivity. We evaluate BiMuon on representation learning and blockwise bilevel optimization, providing empirical support for our methods.

---


### 56. [Ensemble Routing for Prompt-Adaptive Cost-Aware LLM Inference](https://arxiv.org/abs/2611.10193)

**<font color=#1a73e8>作者：</font>** Saul Urso, Emanuele Carlini, Patrizio Dazzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly support Web-based services that must balance response quality and inference cost across heterogeneous requests. Conventional routing selects one model per prompt, while fixed ensembles cannot adapt their composition and cost to individual requests. We introduce PISA, a prompt-adaptive, cost-aware single-model router, and PISA-E, its extension to ensemble routing. At the core of both methods, PISA combines soft cluster memberships with model-specific predictors to estimate individual model capabilities. Building on these estimates, PISA-E jointly selects ensemble composition and cardinality under an explicit cost--quality preference that can be adjusted at inference time without retraining. A tractable ensemble-success surrogate and efficient candidate selection enable this extension without ensemble-specific training. Across four LLM routing benchmarks under in-distribution (ID) and out-of-distribution (OOD) conditions, PISA achieves the highest macro-average cost--performance hypervolume among the evaluated single-model routers in both settings. Meanwhile, PISA-E achieves the highest macro-average task performance among the evaluated ensemble approaches when prioritizing response quality, surpassing the strongest competitors by 2.09 and 2.87 percentage points under ID and OOD conditions, respectively. At selected lower-cost operating points, it also exceeds the strongest ensemble competitors' macro-average task performance while reducing average inference cost by approximately 36% and 25%, respectively. These results demonstrate the effectiveness of prompt-adaptive capability estimation for both single-model routing and selective ensembling.

---


### 57. [Compact Greek Language Models from Scratch: Pretraining 500M- and 1B-Parameter Decoder-Only Transformers](https://arxiv.org/abs/2611.10209)

**<font color=#1a73e8>作者：</font>** Konstantinos Perifanos, Anne Laure Poite, Giannis Tsilikas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present two compact decoder-only language models trained from scratch exclusively on Greek text: LexisLM-1B (1.09B parameters) and LexisLM-500M (502M parameters). Both use a dedicated 32k byte-level BPE tokenizer and a 22B-token pretraining corpus drawn primarily from Greek Wikipedia and FineWeb2. Both models complete the 22B-token schedule, with best held-out perplexities of 9.77 for LexisLM-1B and 11.31 for LexisLM-500M. Evaluation of both models on Greek-translated ARC, MMLU, and TruthfulQA shows above-chance performance on ARC-Easy, while ARC-Challenge and MMLU remain near chance. We also perform supervised fine-tuning of both models on Greek instruction data, primarily EuroAlpaca, reaching held-out instruction perplexities of 7.12 for LexisLM-500M and 6.37 for LexisLM-1B. The report describes the tokenizer, data preparation, training, and evaluation methods, providing a foundation for further work on compact Greek language models.

---


### 58. [Multi-GPU MoE Inference with Adaptive Expert Offloading](https://arxiv.org/abs/2611.10219)

**<font color=#1a73e8>作者：</font>** William X. Zheng, Zhongjie Chen, Shuo Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern Mixture-of-Experts (MoE) inference is constrained by GPU memory. This constraint is mitigated by expert offloading, which stores part of the model's weight in host memory and executes on demand. Though MoE architecture has computation sparsity, more GPUs are needed for serving increasingly larger frontier models. However, existing expert offloading systems overlook this need and fail to scale performance with additional GPUs. We present AdaOffload, a general and efficient multi-GPU hybrid expert execution framework that effectively handles heterogeneous hardware and workloads. We co-design GPU-CPU parallelism and GPU-CPU co-execution for decode and prefill with online workload observation that adapts to different hardware, workload, and batch size heterogeneity. We evaluated AdaOffload on five different platforms with varying GPU capability (L4, Pro6000, B200), number of GPUs, CPU capability, and NUMA topology on three different frontier open-weight models (284B to 753B). AdaOffload achieves $1.9\times$ to $15.5\times$ throughput speedups across different models over state-of-the-art systems.

---


### 59. [Jais 3: Introducing Arabic-centric Agentic AI](https://arxiv.org/abs/2611.10224)

**<font color=#1a73e8>作者：</font>** Team IFM, Haonan Li, Hadi Abdine 等 55 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Jais 3, a fleet of six open, Arabic-centric agentic language models ranging from 0.9B to 375B parameters. Jais 3 is built to complete tasks for Arabic speakers, not only to answer questions in plain text: it is trained to plan multi-step tasks, call tools and Model Context Protocol (MCP) servers, operate a terminal, search the web, and read, edit, and produce PDF, spreadsheet, and presentation files, while communicating with the user in Arabic. Instead of pretraining from scratch, we adapt each model of the fully open K2 Horizon fleet to Arabic through continual pretraining, followed by supervised fine-tuning (SFT), final token preference optimization (FTPO), and reinforcement learning with verifiable rewards (RLVR). We combine natural Arabic text with translated, transliterated, and synthetic Arabic, and replay the base model's own training data to keep its reasoning, agentic, and English abilities. Jais 3 covers Modern Standard Arabic and the major regional dialects, follows instructions with Arabic-specific constraints, and inherits the 512K-token context window of K2 Horizon (all models except the 0.9B). To our knowledge, its 375B model is the largest open Arabic-centric language model to date. For evaluation, we revisit how Arabic models are assessed, moving to fully generative evaluation on audited Arabic benchmarks. Across model sizes, Jais 3 matches or outperforms open-weight models of comparable size on Arabic and agentic benchmarks, with particularly strong agentic capabilities and Arabic instruction following, and far fewer hallucinations. We release the weights and the checkpoints from every training stage of all six models, together with samples of the training data, the data recipes and training configurations, the training logs, the audited benchmarks, and the evaluation code.

---


### 60. [ScreenProof: Where Is This Screen Wrong? Finding UI Faults Without a Reference](https://arxiv.org/abs/2611.10234)

**<font color=#1a73e8>作者：</font>** Huiming Sun, Yue Li, Kangning Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A phone screen can be wrong in ways that need no reference: a label that runs off the screen, letters that touch, a line that breaks one character before its end, one button with sharp corners among round ones. We ask whether a model can box every such fault on a screenshot, given no target design and no reference image. Such a critic could serve as a cheap first pass over generated pages before a designer reviews them, but only if it stays silent on clean pages. ScreenProof poses this target-free critique over three families of faults: general faults, local style faults (one element breaks the style its page sets) and text layout faults (letter spacing, line height, line breaks). A data engine makes each fault in page code and records the changed element's box, and hard negatives change every sibling alike. No frontier judge is reliable: frontier models flag 18-62% of clean real screenshots and 18-82% of clean generated pages, find 47-72% of text layout faults, and rarely find a foreign icon (5-19%). Our small critic ProofJudge (Qwen3.5-9B with LoRA), trained on code-made pages with one to four faults each and keeping a finding only when it is confident, reaches F1 0.48, the highest of all judges (Gemini 4 Argon 0.37; open models at most 0.15; 0.46 even without the confidence cut), and is the only fault-finding judge within 15% false alarms on clean pages (2% real, 9% generated), the property such a first pass needs, at about a hundredth of Argon's cost. It finds the most general faults (59%) but fewer local style faults than Argon (25% against 41%) and fewer text layout faults than the API judges (43%; Gemini 4 Argon 47%). Against a named brand the task is harder still: models know a design language about as well as its public documentation states it.

---


### 61. [PACE: Keeping the Right Tokens in the KV Cache Is Not Enough for Long-Horizon LLM Agents](https://arxiv.org/abs/2611.10240)

**<font color=#1a73e8>作者：</font>** Suman Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents accumulate sessions of up to millions of tokens, far more key-value (KV) cache than one GPU holds, so serving systems keep a small budget of tokens and evict the rest. Eviction methods differ in which tokens they keep but share one goal: that the tokens a later step needs are still cached. We show this is not enough. In 100K-token coding sessions on Qwen3-8B with a 2,048-token budget, a planner-guided policy that keeps over 99% of the needed tokens resident still fails late steps increasingly often: its accuracy falls from 93% to 64% as the gap between a definition and its use grows from 2K to 90K tokens, at residency 0.996. The needed tokens are resident but unretrievable: what grows is their rotary-position distance to the query. We present PACE (Planner-Aware Context Engine), a KV-cache engine that couples plan-aware retention, in which the agent's planner tells the cache which context future steps will read, with bounded positions, which renumber kept tokens so their rotary distance to the query stays below 8K at any session length. In a pre-registered evaluation on fresh tasks, PACE passes 97% of hidden unit tests at 100K tokens, against 42% for H2O and 3% for SnapKV under the same budget, and needs both components: either alone reaches 63% (the combination beats each, p < 10^-4). The result holds with length: in 1M- and 2M-token sessions on one 24 GB GPU, with definitions written 0.9M and 1.8M tokens before use, PACE passes 99% and 100% of checks and recalls every session fact, while bounded positions without foresight falls from 33% to 13%; PACE holds under 0.7 GB of KV state where the full cache would need 147-295 GB. Renumbering is exact, costs no measurable perplexity, and adds 9% wall time. On Mistral-7B, whose coding ability caps it at 40% even with nothing evicted, PACE stays at that ceiling while retention alone falls below it.

---


### 62. [From Weapons to Events: Evaluating Evidential Support in Multimodal AI for Policing](https://arxiv.org/abs/2611.10245)

**<font color=#1a73e8>作者：</font>** Armin Mustafa, Syed Sameed Husain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer vision (CV) for policing has centred on recognising objects such as seized weapons, while body-worn video (BWV) is still reviewed by people, with existing AI tools using only its audio. Multimodal video AI could make BWV review faster and cheaper. At the object level, we present the KnifeHunter dataset, developed with UK law enforcement, with over 25,000 images of 543 knife classes and a protocol reflecting investigative conditions, and KHNet, a retrieval architecture fusing local and global features, which with about 125,000 distractor images attains 85.7% and 63.4% mean Average Precision (mAP) on the medium and hard protocols. At the event level, we present an evaluation protocol for video understanding pipelines, which describe a video as events and a transcript, that scores transcription, speaker attribution, event detection, temporal localisation and unsupported events. Whether each event is supported by the recording is labelled by a judge validated against blinded human labels. We apply it to complete pipelines, three 2026 omni-modal models and our hybrid NarrativeBridge-PAL-GPT-5 pipeline, on UKBWV-27, a pilot stress-test set of 27 publicly released UK BWV recordings (118 minutes). On this set the hybrid pipeline leads on five of six measures, yet it leaves 13.6% of predicted events unsupported and misattributes 27.7% of utterances, and every pipeline degrades on recordings from edited releases, long recordings and noisy audio. We propose readiness levels separating assistive tasks from those requiring verification of every output.

---


### 63. [FedLoVA: Value-Only Aggregation for Federated LoRA Fine-Tuning of Large Language Models](https://arxiv.org/abs/2611.10248)

**<font color=#1a73e8>作者：</font>** Ensieh Khazaei, Baturalp Buyukates, Dimitrios Hatzinakos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) is a popular parameter-efficient fine-tuning (PEFT) method for fine-tuning of large language models (LLMs), especially in federated learning, due to its strong performance and communication efficiency. In practice, LoRA is applied to the query and value projections of transformer layers without considering the distinct roles of these components. In this work, we analyze the impact of these projections in federated fine-tuning of LLMs using LoRA and observe that the value projection converges significantly faster than the query projection. Motivated by this finding, we propose FedLoVA, a federated fine-tuning framework that trains LoRA adapters on both query and value projections locally while sharing only the value projection with the server. This approach reduces communication overhead while improving convergence efficiency. Experiments on natural language understanding, multilingual sentiment analysis, and generation tasks show that FedLoVA reduces the communication cost by up to $7.8\times$ compared to existing federated LLM fine-tuning baselines while achieving comparable or better performance. The code is available at: this https URL.

---


### 64. [Do large language models rank moral values? A transitivity test of moral competence](https://arxiv.org/abs/2611.10265)

**<font color=#1a73e8>作者：</font>** Katelyn A. Wasson, Kiwon Song, James M. Jennings III 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used to support decisions that require moral consideration. While LLMs perform well on morality benchmarks from psychology and philosophy, producing appropriate outputs on these benchmarks (moral performance) does not establish that an LLM weighs competing moral values at stake in a decision (moral competence). We test a minimal, necessary condition for such weighing: that an ordinal ranking can represent LLM moral choices. Such a ranking requires transitivity. To assess transitivity, we presented LLMs with pairwise trade-offs among moral value violations in vignette choice sets and extracted resulting choice probabilities from first-token distributions. Tested against three stochastic transitive choice models, most choice sets admitted weak or unstable orderings. Aggregating an LLM's responses, a common practice in LLM moral evaluation, produced transitive structure that matched no individual choice set. Evaluations of AI morality should establish that choices are structured before asking whether they are aligned.

---


### 65. [I play of the cello: Evaluating Constructional Bleeding in Multilingual LLMs with CALQUE](https://arxiv.org/abs/2611.10266)

**<font color=#1a73e8>作者：</font>** Toshiki Nakai, Yu-Yin Hsu, Marie-Catherine de Marneffe 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Languages use different morphosyntactic strategies to express the same meaning. Speakers of multiple languages are able to apply strategies from one language to another, either by mistake or intentionally, to produce a literal translation, or calque. Considering that large language models (LLMs) have been shown to generalize crosslingually, despite being predominantly trained on English, we investigate whether they overgeneralize constructional strategies from English to other languages. To test this, we create a dataset of 5583 sentence pairs across seven languages, matching literal translations of strategies from English into other languages, and literal translations of the other languages' strategies into English. We then quantify constructional bleeding by measuring how often strategies from English are assigned a higher probability than native strategies. We find that models often fail to assign higher probabilities to native strategies and tend to prefer English-derived strategies even when evaluating sentences in other languages. Our findings highlight the limitations of the current English-dominant training paradigm.

---


### 66. [Adversarial Evaluation of Large Language Models for Patient-Friendly Radiology Report Summarization](https://arxiv.org/abs/2611.10277)

**<font color=#1a73e8>作者：</font>** Magdalini Paschali, Asad Aali, Arogya Koirala 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Purpose: To develop and validate a scalable adversarial evaluation framework for assessing the robustness of large language models (LLMs) that generate patient-friendly summaries of radiology reports.
Methods: We introduced a clinically grounded adversarial framework that uses controlled term substitutions and impression removals across intensity levels. Using a radiologist-validated adversarial dictionary, we generated adversarial variants of CT and MRI reports. Six LLMs summarized original and adversarial impressions using 2 prompt styles, yielding 18,000 evaluation pairs. Robustness was evaluated with an automated LLM-as-a-judge framework scoring factual faithfulness, sensitivity to adversarial edits, certainty fidelity, and hallucination rate. Failure mode analysis quantified vulnerabilities in incorporating clinical modifiers. Agreement with two radiologists was assessed on 105 cases.
Results: GPT-5-mini achieved the highest factual faithfulness and certainty fidelity under both adversarial edits. Under term substitution, hallucinations occurred in 28.1-30.1% of GPT-5-mini summaries, compared with 35.3-36.4% for Claude Sonnet 4.5 and 41.4-41.9% for MedGemma. Impression-removal edits were handled more robustly than term substitutions. Even for the highest-scoring summarizer, substitutions of anatomical terms were not reflected in 23.7% of summaries, diagnostic certainty in 22.3%, and descriptor terms (e.g., "substantial") in 21.2%. Judge-radiologist agreement (macro-F1: 0.55-0.56) was comparable to inter-radiologist agreement (0.53).
Conclusions: Adversarial evaluation exposes clinically meaningful failure modes, including missed anatomical modifiers, altered diagnostic certainty, and omitted severity descriptors.

---


### 67. [Restoring General and Improving Domain-Specific Safety in Fine-Tuned LLMs Without Retraining](https://arxiv.org/abs/2611.10279)

**<font color=#1a73e8>作者：</font>** Vishnu Kabir Chhabra, Ding Zhu, Zhihui Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-aligned language models are known to suffer degradation in refusal behavior following domain-specific fine-tuning, even when the fine-tuning data is entirely benign. The predominant mitigation strategy, preference optimization on the fine-tuned model, is computationally expensive and requires domain-specific preference data that is often unavailable in practice. We propose SPECTRA, a training-free, weight-level method that restores refusal behavior by transferring the base model's refusal direction into the fine-tuned model's weights via an activation-aware, low-rank update, requiring no gradient-based optimization or domain-specific safety data. The low-rank design restricts the intervention to the subspace most causally active on harmful inputs, leaving benign behavior largely undisturbed by construction. Empirically, SPECTRA substantially improves refusal behavior across a comprehensive safety evaluation, while preserving general coherence, domain-specific knowledge, and producing negligible change in false refusal rates.

---


### 68. [Conformal Fair Decoding for Large Language Model Recommenders](https://arxiv.org/abs/2611.10285)

**<font color=#1a73e8>作者：</font>** Ziwei Wu, Jingrui He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate personalized recommendations without task-specific training, but changing a protected attribute while holding interaction history fixed can alter the semantic content of recommended items. We study fairness control when model weights and full-vocabulary logits are unavailable. We propose Fair- Rec, an item-level decoding framework that uses an offline-calibrated semantic-disparity threshold and controls candidate selection as recommendation lists are generated. A hard variant filters candidates against the threshold; a soft variant trades off candidate likelihood and disparity while adapting a penalty using observed violations. Under an explicit uniform enforceability assumption, we establish a pathwise O(1/T) upper bound on the excess empirical violation rate of the soft decoder. Experiments on MovieLens-1M and Amazon Movies & TV using Qwen3-8B and Llama3.1-8B-Instruct show that the soft variant lowers measured counterfactual disparity relative to zero- =shot recommendation, UP5, and FACTER, while retaining competitive HR@10 and NDCG@10.

---


### 69. [A Clinical Evaluation of Conformal Prediction for Chest Radiograph Report Generation](https://arxiv.org/abs/2611.10288)

**<font color=#1a73e8>作者：</font>** Nikolaos Kontogeorgis, Pascal Krezer, Klaus-Rudolf Kladny 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While multimodal large language models (MLLMs) have improved automated radiology report generation, they remain prone to hallucinations, necessitating clinically meaningful risk-control methods. Conformal prediction (CP) provides statistical guarantees, yet existing CP approaches rely on uncalibrated automated extractors and fail to account for the clinical relevance of errors. We introduce clinical admissibility criteria (CLARITY), a framework for evaluating radiology reports that explicitly distinguishes clinically consequential errors from minor deviations. To eliminate reliance on automatic judges, we collected radiologist annotations of MLLM-generated reports using CLARITY. By benchmarking CP strategies and automatic evaluation metrics against these expert annotations, we demonstrate that commonly used admissibility proxies systematically fail to detect clinically relevant errors. Our findings reveal that automated admissibility judgments are largely decoupled from true clinical admissibility.

---


### 70. [Uncertainty, Not Concealment: A Mechanistic Reappraisal of Sycophancy in Vision-Language Models](https://arxiv.org/abs/2611.10297)

**<font color=#1a73e8>作者：</font>** Mohamed I. Eldagla, Zeyad H. ElShafei, Ahmed M. Anter  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) in medical retrieval-augmented generation must be able to say when a retrieved report contradicts the X-ray, so understanding whether they can detect such conflicts is important for safe deployment. The sycophancy mask hypothesis holds that these models internally detect conflicts but refuse to report them, concealing a detected contradiction. We introduce a three-part diagnostic that separates concealment from uncertainty: representation probing, activation steering, and two-way forced choice. Across four instruction-tuned VLMs on chest X-rays, we confirm behavioral suppression of contradiction and find that a linear probe separates matched from mismatched inputs, beyond what a simple CLIP model achieves. Steering the learned conflict direction never elicits contradiction, and forcing a binary choice does not recover one; instead, cross-modal attention to the image drops on mismatched pairs. We conclude that these models fail to contradict because the mismatch registers as hedged, gated uncertainty rather than concealed knowledge, calling for re-grounding and uncertainty surfacing. Code is available at this https URL.

---


### 71. [Plug-and-Play Verifier for Decoupling Process Reward in Stabilizing Long-Horizon Agentic Reasoning](https://arxiv.org/abs/2611.10305)

**<font color=#1a73e8>作者：</font>** Mingwei Xu, Jieyuan Pei, Binghao Tu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stabilizing long-horizon reasoning requires intelligent agents to sustain useful progress across successive reasoning steps and tool interactions. Such agents are typically trained with reinforcement learning (RL), where actor-critic RL uses a learnable critic network to estimate step advantages, while critic-free methods such as GRPO eliminate critic models and rely mostly on the group variants of sparse outcome-only rewards. Both reward types leave partially useful failed trajectories either implicit or indistinguishable from entirely unproductive ones, and as reasoning horizons grow, it becomes difficult to maintain consistent reasoning trajectories. In this work, we propose a \textit{plug-and-play verifier} framework for stabilizing long-horizon reasoning through explicit verification of intermediate reasoning artifacts. Specifically, the framework decouples process verification through a unified interface that extracts intermediate reasoning artifacts from agent running trajectories, evaluates them using domain-specific verifiers, and aggregates the verification scores as bounded process reward. Then, we combine our dense verified process rewards and the sparse outcome rewards through a two-stage post-training schedule. We showed that with plug-and-play verifiers, we further stabilize the reasoning steps as last-mile self-reflection and self-consistency. Typical evaluation on HotpotQA using Qwen3.5-4B achieves a superior accuracy (60.18\%), outperforming the standard GRPO baseline (57.73\%). Our results suggest that plug-and-play verifiers provide a modular approach to learn more stable and reliable reasoning behaviors over long horizons.

---


### 72. [How Much Is Left Matters: False Positives and False Negatives in Partial-Prompt Contamination Tests](https://arxiv.org/abs/2611.10307)

**<font color=#1a73e8>作者：</font>** Abhishek Anand  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial-prompt completion, where a model receives the first part of a benchmark problem and is checked for whether it reproduces the rest, is a widely used test for benchmark contamination. We audit this test on seven open-weight models using MATH-500 and recent AIME 2025/2026 problems, which serve as true negatives. Memorization flags depend strongly on how much text remains: for every model, problems with at most 8 leftover words are flagged several times more often than problems with at least 25 (31.5% vs. 5.5% for Qwen2.5-7B-Instruct), and half to three-quarters of all ROUGE-based flags come from short leftovers. On true negatives, a ROUGE-L >= 0.75 threshold flags up to 6.7% of problems at a 60% prefix, and at an 80% prefix even exact match flags 8.6% (pooled over models; 6.2% on AIME 2026, which postdates every model), against 0% at 40-60%. The test also misses contamination upstream: models distilled from Qwen2.5-Math, whose base is heavily flagged in prior work, show almost no model-specific recall. Calibrating each model against models from other families removes most flags while isolating a consistent Qwen2.5-specific signal at every prefix length. We recommend length-stratified reporting, prefixes of at most 60%, style-matched post-cutoff controls, and cross-family calibration.

---


### 73. [TripleGrader: A Web-Based Platform Supporting Collaborative Triple Annotation with Quality Grading and Inter-Rater Agreement Assessment](https://arxiv.org/abs/2611.10317)

**<font color=#1a73e8>作者：</font>** Rajan Lamichhane, Songhui Yue  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs need validated relational triples, and gold benchmarks of such triples are often built by several annotators. Most text annotation platforms focus on span tagging and compute agreement on categorical labels. They are not designed for ordinal quality grading of triples that have already been extracted. We present TripleGrader, an open-source web platform for grading subject-predicate-object triples on a 0 to 10 ordinal scale. In TripleGrader, each triple is scored independently, and peer scores stay hidden until the grader has rated it. Graders then discuss entries in threaded comments and propose revisions, which the session owner approves and publishes as new versions. For agreement, the platform computes quadratic-weighted Cohen's kappa for two raters and a quadratic-weighted Fleiss-type kappa for three or more. Graded sessions and the final benchmark are exported in common formats. We evaluated the platform in three ways. We ran 72 automated tests, including 18 workflow scenarios through the REST API. We also injected 10 error types to check whether prescribed corrections could be applied while preserving unaffected triples. On two small corpora with existing gold benchmarks, we then used the platform to curate the triples extracted by four large language models into each benchmark. Only 10% to 32% of the candidate triples could be kept unchanged, and 53% to 71% needed corrections, partly to match the benchmarks' naming conventions. Per model, 11 to 29 missing triples had to be added. On these corpora, the extracted triples therefore needed substantial human review. The source code is available at this https URL.

---


### 74. [Prove What You Can: Hybrid Neurosymbolic Reasoning for Logical Natural Language Inference](https://arxiv.org/abs/2611.10319)

**<font color=#1a73e8>作者：</font>** Ada Canoğlu, Sadiq Qara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Logical reasoning over natural language requires both semantic interpretation and deductive search. Large language models (LLMs) can propose plausible intermediate derivations, but they often fail to compose them into a complete proof and overpredict uncertainty. Neurosymbolic methods improve search by translating an entire problem into first-order logic and handing it to a prover, but a single bad clause can make the whole translation nonexecutable. We present Hybrid Reasoning, a three-stage pipeline that decouples proposing a proof, validating its steps, and deciding a label. An LLM proposes a structured proof tree with a raw verdict; a theorem prover validates each derivation locally, keeping only the subset it can prove; and an uncertainty-gated repair attempts to re-derive the label from the premises plus the validated derivations, when the raw verdict is UNCERTAIN. Across four benchmarks (FOLIO, ProofWriter, ProverQA, PrOntoQA) and five contemporary LLMs, Hybrid Reasoning is the top-performing method on the two hardest datasets, improving on the strongest baseline by 5.3 points on FOLIO and 4.9 on ProverQA, and reaches ceiling-level accuracy on the easiest. The repair stage operates at 78-98% precision, producing 326 correct relabellings against 19 regressions.

---


### 75. [Update Slope Is Bounded by Prior Calibration: A Structural Bound and Its Contingent Empirical Signature](https://arxiv.org/abs/2611.10325)

**<font color=#1a73e8>作者：</font>** Ben Jenkins, Mihaela Cardei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluations of LLM forecasters increasingly measure how forecasts improve as richer evidence is supplied. We identify two confounds in this update-slope metric. First, outcome-aware evidence construction substantially inflates measured responsiveness: on the same models and questions, slopes are roughly four times larger than with resolution-blinded evidence ladders. Second, update slope is a change score with a prior-dependent structural ceiling, so raw comparisons can reflect differences in starting calibration rather than updating behavior. The ceiling defines only a feasible region; whether slope and prior calibration are empirically coupled depends on headroom utilization and varies across our Manifold, ForecastBench, and ACLED pools. Despite this variability, conditioning on prior calibration roughly triples the association between intermediate updating and final Brier score under both blinded and outcome-aware construction. Question identity also explains substantially more variance than model identity across the evaluated pools. We recommend building evidence ladders blind to outcomes, conditioning on prior calibration, and reporting headroom-normalized measures alongside raw slopes.

---


### 76. [Policy Over Purpose: Auditing LLM Content Moderation of Reclaimed Slur Usage](https://arxiv.org/abs/2611.10327)

**<font color=#1a73e8>作者：</font>** Christina Chance, Kai-Wei Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Perspective API is deprecated, platforms are turning to large language models for content moderation, encoding policy as natural language that the model must interpret at inference time. Reclaimed slurs test this design directly. The same term can express in-group pride or target the community that reclaimed it, and misreading it silences the speech moderation is meant to protect. We audit four general-purpose LLMs and four moderation-specific systems, with Perspective API as a legacy baseline, on IYKYK, a corpus of reclaimed and derogatory usage of three slurs annotated by community members. Across the policy, decision, reasoning, disparity, and steering layers of this audit, we find that whether a system was purpose-built for moderation explains little about how it handles reclaimed language. No system reliably agrees with community judgment, and all fail most on language reclaimed within Black communities. What separates systems is instead how their policy is represented. Only systems whose policy is expressed in the prompt can be steered at all, and even then, explicit definitions change how models justify a decision more than how they make it. We argue that policy transparency determines whether moderation failures can be corrected, but that correcting them requires contextual judgment that definitions supplied at inference time cannot provide.

---


### 77. [SIRIS: Can LLMs Tell When Simulation Errors Matter in AI-Driven Systems Research](https://arxiv.org/abs/2611.10329)

**<font color=#1a73e8>作者：</font>** Jinwoo Hwang, Sukmin Cho, Tao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly drive systems research and rely on simulators to evaluate candidate designs at scale. Simulators are imperfect by design: their modeling limitations can distort predictions yet leave the recommended design correct, or change which design should be selected. We introduce Siris to test whether LLMs can tell these cases apart, judging from their systems understanding when a limitation invalidates the simulator's recommendation. By perturbing a simulator, Siris constructs workload pairs with the same candidates, limitation, and simulator recommendation. The perturbation changes predictions on both workloads, yet a reference simulator supports the recommendation on only one. Evaluating thirteen frontier LLMs on LLM serving design problems, we find that identifying a limitation does not ensure a correct choice, and even the strongest models sometimes abandon valid recommendations. Self-correction through a review turn helps these models restore valid choices but introduces new errors in several others. These findings motivate evaluating systems understanding through design decisions under imperfect simulators.

---


### 78. [Reproducible LoRA Inference Through Deterministic Split-K Reduction](https://arxiv.org/abs/2611.10334)

**<font color=#1a73e8>作者：</font>** Dhayaneshwar Balusamy, Ankur Mohan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reproducibility is important for LoRA-adapted language models used in repeated evaluation, auditing, and decision-making. However, Split-K kernels used to introduce parallelism in low-rank LoRA multiplications can have the unintended consequence of numerical nondeterminism when partial results are combined using floating-point atomic additions. We investigate this non-determinism in vLLM across GSM8K mathematical reasoning, MBPP code generation, and Jev-style structured toxicity decisions on Civil Comments and introduce a deterministic Triton Split-K implementation. Under identical-input replay, Atomic Split-K=8 produces different FP32 shrink outputs in 97.61% of comparisons, while our Deterministic Split-K=8 shows no observed variation. Repeated atomic inference changes generated outputs in 17.30% of GSM8K and 14.96% of MBPP comparisons, sometimes altering task correctness. Structured-decision probabilities vary in 81.47% of atomic comparisons, with decision flips. Controlled tracing demonstrates how shrink-output differences propagate into the KV cache and how accumulated cache differences can change token decisions and final answers. Our deterministic Triton Split-K=8 implementation preserves parallelism, achieving 16.8-21.1% latency-based speedup over unsplit reduction with only 1.02-2.62% additional latency relative to Atomic Split-K=8.

---


### 79. [Two-Sided Conformal Evidence Sets for Retrieval-Augmented Generation](https://arxiv.org/abs/2611.10335)

**<font color=#1a73e8>作者：</font>** Ben Jenkins, Mihaela Cardei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) can surface passages that support a claim, contradict it, or fail to address it, yet existing calibrated grounding methods are typically one-sided and model only supporting evidence. We introduce Conformal Evidence Sets (CES), a two-sided framework that returns separate support and refutation sets with finite-sample inclusion coverage of at least $1-\alpha$ on each side under exchangeability; a Bonferroni union yields joint coverage of at least $1-2\alpha$. On labeled candidate pools from the contrastive VitaminC benchmark, CES closely tracks nominal coverage across $\alpha\!\in\!\{0.05,0.10,0.15,0.20,0.30\}$, with maximum deviations of $3.0$ percentage points for support and $5.4$ for refutation, and reaches essentially the same empirical coverage--size frontier as a test-tuned fixed-threshold heuristic without any test exposure. Stress tests mark the boundary of that guarantee: under FEVER distribution shift both sides under-cover, by up to $12.7$ percentage points, and support-side group-stratified recalibration substantially reduces the support gap. Scorer swaps, hard-negative retrieval, cross-dataset transfer, and a live end-to-end pilot expose a clear separation: when exchangeability holds and relevant evidence is retrieved, evidence inclusion remains calibrated even with an imperfect scorer, whereas the support/refute verdict tracks scorer quality directly. Calibrated evidence coverage and reliable verdicts are therefore distinct properties and should be reported separately.

---


### 80. [IdealCache: Rethinking Cache Scheduling in Diffusion Transformers via Ideal Trajectories](https://arxiv.org/abs/2611.10340)

**<font color=#1a73e8>作者：</font>** Shang Xue, Li Zhu, Ping Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Feature caching accelerates Diffusion Transformers by reusing intermediate computations across denoising timesteps, yet existing methods share a fundamental blind spot: they treat the standard reference denoising trajectory as the optimisation target, approximating its per-step states and thus inheriting its output as an implicit quality ceiling. We argue that this target is arbitrary -- what truly matters is the ideal result, not the intermediate path taken to reach it. We propose IdealCache, a training-free framework that abandons step-wise imitation of the reference trajectory. Instead, it anchors caching on a per-input ensemble of ideal trajectories constructed from candidate target results, aggregates their geometry into a single graph, and discovers optimal non-uniform schedules via a constrained shortest path on this graph. By decoupling from the reference process, IdealCache breaks the performance bottleneck of trajectory-approximation; our schedules can attain near-lossless fidelity in generation and even surpass on task-specific metrics (e.g., maintaining higher semantic consistency in image editing). Without retraining, IdealCache achieves 6.35x speedup on Qwen-Image, 5.84x on Qwen-Image-Edit, and 4.32x on HunyuanVideo, with competitive or superior quality across tasks.

---


### 81. [MaRiO: Multi-agent Collaborative Reasoning via Shared Observations in MLLMs](https://arxiv.org/abs/2611.10344)

**<font color=#1a73e8>作者：</font>** Nathaniel Redmond, Fidel Omar Tito Cruz, Devansh Sharma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) show strong visual perception capabilities, but existing evaluations largely focus on single-view or multi-view settings with shared camera parameters, leaving the challenge of multi-agent collaborative scenarios underexplored. In such settings, multiple agents observe a shared environment from independent viewpoints, and reliable decisions require reasoning across these independent observations of the same environment. To study this problem, we introduce MaRiO, a benchmark for evaluating multi-agent collaborative reasoning, and evaluate 23 state-of-the-art MLLMs on it. Our analysis reveals three key findings: (1) tasks governed by static perception are generally easier than tasks that require transformational event sequences; (2) most models struggle to resolve cross-agent correspondences, with errors increasing with scene complexity; and (3) models show limited ability to leverage geometric cues present in the scene. As an initial step toward addressing these challenges, we explore geometry-guided synthetic view augmentation that generates intermediate transition frames between agent observations, providing auxiliary spatial context that improves performance in certain categories. Overall, our results highlight that multi-agent collaborative reasoning remains an open challenge and an important direction for multimodal embodied systems. The code is available on the project page: this https URL.

---


### 82. [SituRecBench: Evaluating Frontier Models as Situated Recommendation Assistants in 3D Environments](https://arxiv.org/abs/2611.10349)

**<font color=#1a73e8>作者：</font>** Jingtong Yang, Dongding Lin, Jian Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recommender systems are transitioning from static retrieval engines into interactive assistants grounded in physical environments. However, current studies largely neglect the combined complexities of spatial navigation, visual grounding, and multi-turn social interaction. To bridge this gap, we introduce SituRecBench, an interactive benchmark for evaluating frontier vision-language models (VLMs) as situated recommendation assistants within high-fidelity 3D environments. We reformulate recommendation as a situated assistance process in which an assistant interacts with a user while sharing the user's egocentric view. Our benchmark simulates real-world shopping environments (e.g., supermarkets and home furnishings stores), requiring assistants to elicit preferences, ground recommendations in the environment, and guide the user to relevant locations through dialogue. The benchmark evaluates dialogue quality, recommendation utility, and navigation effectiveness through a unified interactive protocol. Extensive experiments reveal persistent challenges in spatial grounding and preference elicitation, highlighting limitations in their ability to integrate global contextual information with local observations. SituRecBench provides a rigorous foundation for advancing the development of situated assistants in the real world.

---


### 83. [FEROM: Frontier Endogenous Reveal-Order Marginal Policy Optimization for Masked Diffusion LMs](https://arxiv.org/abs/2611.10369)

**<font color=#1a73e8>作者：</font>** Zian Su, Ziyang Huang, Kaiyuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models generate text by iteratively unmasking positions, with practical samplers often selecting reveal positions from the model's own logits. The reveal order is therefore an endogenous latent variable of the rollout process with an enormous discrete latent space. Policy optimization objectives relying on pre-defined schedules or sampled trajectories introduce either bias or high variance. In this paper, we propose FEROM, Frontier Endogenous Reveal-Order Marginal Policy Optimization, which approximates policy gradients for the rollout-induced marginal response policy of masked diffusion LMs. FEROM derives a Rao-Blackwellized policy-gradient identity over latent reveal orders and expresses the resulting estimator as posterior edge occupancy on a reveal-state DAG. To make marginalization practical, we introduce Frontier Reveal Marginalization, a budgeted estimator that approximates this marginal edge structure by combining CDF-based computation of local probabilities of the endogenous reveal process with frontier expansion of high-mass partial states. Integrated into a GRPO-style objective, FEROM replaces single-path log-scores with a detached token-score surrogate over posterior-relevant reveal edges. Experiments on math and coding tasks show comparable or improved results over existing methods under matched scoring-state budgets. An offline proxy study further shows improved marginal-gradient approximation with increased scoring budgets.

---


### 84. [Vision Language Models for Primary Structure Threat Identification in Wildland Urban Interface Fires](https://arxiv.org/abs/2611.10377)

**<font color=#1a73e8>作者：</font>** Zhangding Liu, Neda Mohammadi, John E. Taylor  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wildland urban interface (WUI) fires increasingly threaten communities and infrastructure, motivating the need for rapid visual assessment. Recent research has focused primarily on detecting fire and assessing post-event damage. However, structure-level fire threat identification during active WUI fire events remains underexplored. This study evaluates Qwen3-VL-8B-Instruct for this active-fire decision using two separately scored tracks: 1,824 synthetic images from 491 designed WUI scenarios and 45 frames from a controlled-burn experiment conducted in collaboration with Columbus Fire & EMS Department. Under zero-shot prompting, the model returned valid target fields for 1,808 synthetic images and 39 controlled-burn frames. Accuracy among valid outputs was 94.0% for the synthetic track and 69.2% for the controlled-burn track, compared with a 16.0% random-selection baseline for the latter. On the synthetic track, the model generally identified the intended target across varied designed WUI scenarios when the relevant fire-spread cues were visually distinct. Controlled-burn performance was well above random selection, but errors showed difficulty interpreting spatial relations in complex scenes. The dual-track protocol provides scalable stress testing in designed scenarios and a controlled-burn reference for assessing model behavior under physical fire conditions. Future work can use the synthetic data for VLM post-training and then evaluate the adapted models on larger and more diverse real WUI fire datasets.

---


### 85. [From Reflection to Co-Evolution: Self-Evolving Agents with Locally Verified Memory](https://arxiv.org/abs/2611.10382)

**<font color=#1a73e8>作者：</font>** Xinxiang Yin, Xinglang Zhang, Haodong Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LLM agents have made impressive progress in coding and mathematical reasoning, motivating growing interest in learning from long-horizon interaction. Memory supports this process, but plausible lessons can be redundant or reinforce inappropriate actions. Can a memory's source decision provide a practical test for whether to retain it? We localize consequential trajectory steps, extract candidate memories, and replay each source decision with and without its candidate under the same context. This reveals two properties: most candidates barely shift the probed distribution, and both successful and failed source actions can be reinforced or suppressed. These observations motivate Anchor, which tests shift magnitude and source-role alignment before retention. Admitted memories guide later trajectories, enabling experience-driven improvement under a frozen policy. On held-out ALFWorld and WebShop tasks, Anchor improves success rate and mean score by up to 19.9% and 17.2%, respectively, relative to the strongest baseline for each backbone. With Qwen3.5-27B, it retains 41% fewer ALFWorld cards than unfiltered retention and outperforms all four WebShop cost-comparison baselines while using fewer tokens.

---


### 86. [Pruning DNA Sequence](https://arxiv.org/abs/2611.10386)

**<font color=#1a73e8>作者：</font>** Faias Satter, Shaker Islam, Aminul Islam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data pruning can substantially reduce training cost by removing examples that contribute little additional learning signal, but it has not been studied for DNA language-model pretraining. We introduce Sequence Pruning (SP), a dynamic pruning framework that removes genomic sequences as they become easy for the model to predict. SP uses per-sequence pretraining accuracy computed directly from the model's forward pass, requiring no separate scoring model or additional pass over the corpus. We evaluate SP across five pretraining settings spanning two corpora, three model families, and both MLM and CLM objectives, with downstream evaluation on five genomic benchmarks. SP reduces pretraining data processing by up to 96% while largely preserving downstream performance. At moderate savings, pruning improves performance by up to 1.2 MCC points over full-data pretraining; at the highest savings, pretraining uses only 4% of the baseline GPU hours with little performance loss. SP also outperforms the dynamic pruning methods InfoBatch and BPAS across most comparisons. Beyond accuracy, our framework supports alternative criteria such as perplexity and EL2N, although accuracy yields the strongest downstream performance at matched savings. These results show that genomic pretraining does not require repeatedly processing all available sequences and that dynamic sequence-level pruning can substantially improve its data and computational efficiency. Code is available at this https URL.

---


### 87. [From Task Affinities to Optimal Allocations: Probabilistic Graphical Modelling for Supervised Finetuning](https://arxiv.org/abs/2611.10389)

**<font color=#1a73e8>作者：</font>** Prateek Chanda, Saral Sureka, Krishnateja Killamsetty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning over a large pool of heterogeneous tasks is often computationally expensive, leading practitioners to train language models on a fixed training budget of carefully chosen SFT tasks. Thus, achieving strong downstream performance hinges on selecting an effective subset of tasks, or equivalently, identifying an optimal task mixture under a fixed budget constraint. In practice, supervised finetuning mixtures are often determined using simple heuristics (e.g., uniform or size-proportional sampling) that ignore task interactions, which can hurt transfer and waste budget on redundant task sources. We introduce TASKMIXPGM, a framework for learning continuous task mixtures through energy-based modelling over SFT tasks. Each task forms a node in a Markov random field, with unary potentials capturing task utility and pairwise potentials modelling inter-task relationships via behavioral divergences between predictive distributions of single-task fine-tuned models. Optimizing this objective yields task mixtures that balance utility, coverage, and redundancy. We further show that the induced set function defined over the set of such tasks is weakly submodular under budget constraints, enabling approximation guarantees for discrete task selection. Empirically, we provide a fixed, benchmark-independent mixture that improves over heuristic mixing across multiple model families and different training budgets. TASKMIXPGM also uncovers interpretable structure in task interactions, revealing complementarities and redundancies that inform effective SFT mixtures.

---


### 88. [A Computational Map of the Disaster Mental Health Research Landscape](https://arxiv.org/abs/2611.10390)

**<font color=#1a73e8>作者：</font>** Soheil Shapouri, Saber Soleymani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When disasters strike, they not only damage infrastructure, buildings, and the economy, but also affect the mental health of affected populations. Research on the mental health effects of disasters has expanded rapidly and has become an important, well-funded area of psychology, public health, and related social sciences. However, the overall structure of this research landscape has not been systematically characterized. Using large language models, we conducted a review of all articles related to terms 'disaster' and 'mental health' indexed in PubMed. 7,859 articles' metadata were retrieved using the NCBI API, and then Claude Sonnet was used to extract structured variables from the abstracts. The results indicated that earthquakes and epidemics were the most commonly studied disasters while many other disasters such as heat and cold waves have received less attention. PTSD, depression, and anxiety were well investigated but many other mental health issues (e.g., aggression, suicide) are relatively ignored. Despite enjoying relatively large sample sizes (median = 452, IQR = 142 - 1,568), the field rarely utilizes machine learning algorithms. Hypothesis significance testing, reviews, qualitative methods, and structural equation modeling are respectively most common methods while agent-based modeling, machine learning, casual inference, and NLP each appear in less than 1% of articles. Studies are limited to a small number of countries, particularly the United States, Japan, and China, while many disaster-prone regions remain substantially underrepresented. This LLM-assisted computational map provides a broad overview of the disaster mental health literature while highlighting important methodological gaps, with particular emphasis on the underutilization of computational methods that could help advance the field.

---


### 89. [Coding or Cheating? An Investigation of Frontier Coding LLMs](https://arxiv.org/abs/2611.10404)

**<font color=#1a73e8>作者：</font>** Yuntao Gui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier agentic LLMs are trained on verifiable rewards in reinforcement learning (RL) environments built from real software repositories. A passing test suite is treated as the reward for solving the task. We show that, on hard problems, frontier models often satisfy these rewards by obtaining the answer instead of deriving it, known as reward hacking. Prior reports document this behavior on public benchmarks. We test its persistence on unseen problems.
In a hardened environment where the answer cannot leak, nearly every model we tested attempted to recover the answer, escalating through tiers of increasingly specialized exploitation: mining the repository history for the upstream fix, inspecting the git object store directly, and sweeping the filesystem for a possible newer copy of the source or hidden tests. These attempts were concentrated on the hardest problems, and the models differed in whether, how often, and how deeply they escalated. Our position is that this behavior is a learned shortcut, acquired in RL environments that leak the answer, not a sign of intelligence. We release agent traces for these models to support further study at this https URL.

---


### 90. [Tail-risk-aware Agent Safety: Constraining Tail Risks Across Multi-step LLM Agent Workflows](https://arxiv.org/abs/2611.10411)

**<font color=#1a73e8>作者：</font>** Shilong Pan, Zhiliang Tian, Zihan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents extend LLMs with tool calls, memory, planning, and retrieval to act in external environments, but they are vulnerable to attacks at different workflow steps. Existing defenses, including prompt engineering and post-training alignment, primarily improve LLM-only safety and often overlook risks that arise from multi-step execution. External verification adds guardrails to check each step separately, but it typically ignores how risks can propagate across steps. We argue that we should consider risk transitions across dependent steps through the agent workflow, rather than separate verification on a single step. In this paper, we propose \textbf{T}ail-risk-aware \textbf{A}gent \textbf{S}afety (TAS), a tail-risk-aware safety framework that models agent workflow safety as a sequence of dependent safety states and constrains the rare but extreme risks (i.e., tail risk) with a shared budget. TAS first models safety-state transitions sequentially along the workflow as an MDP to trace risk propagation, then measures a tail-sensitive risk to target rare but high-cost risks (i.e., tail risk), and constrains the risk with a shared budget to derive a step-wise safety strategy. By constraining tail risk rather than the overall average, TAS suppresses rare high-cost failures while preserving utility in normal cases. Experiments show that TAS achieves better performance compared with eleven baselines across three benchmarks.

---


### 91. [TurnFlow: Benchmarking User-State Reasoning in Multi-Turn LLM Agents via Scene-Guided User Simulation](https://arxiv.org/abs/2611.10412)

**<font color=#1a73e8>作者：</font>** Zhixun Chen, Ming Li, Anjie Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed through conversational interfaces, yet strong single-turn performance does not imply reliability in multi-turn settings. Multi-turn assistance requires a model to maintain an evolving representation of user requirements and to reason over it before complying with later requests. Failures can therefore be subtle: models may fail to recognize a changed constraint or hidden conflict, or recognize it without enforcing it in the final response. Existing benchmarks primarily test fully specified prompts, long-context recall, or controlled domain environments, leaving open-domain requirement reconciliation undermeasured. We introduce TurnFlow, an interactive benchmark for evaluating whether models preserve, revise, and act on user requirements across turns. TurnFlow combines adaptive user simulation with verifiable judging, allowing conversations to unfold naturally while keeping hidden requirements and pass/fail criteria controlled. In our evaluation, nine LLMs achieve overall pass rates from 42.86% to 59.59% on 490 scenarios. Performance varies substantially across challenge types: models perform well on Stateful Multi-Constraint Following but remain considerably less reliable on Scope Creep and Goal Shift. These results reveal persistent limitations in reasoning over evolving user requirements across turns.

---


### 92. [Track or Follow? A Jev-Compatible Multi-Agent Trading System When Web News Lags the Market](https://arxiv.org/abs/2611.10414)

**<font color=#1a73e8>作者：</font>** Yebo Feng, Guangyan Gan, Liangrui Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly trade on the Web news they read, yet much Web news about listed firms is published after, and about, the price move it reports, so a reader can agree with the market by following it instead of reading the event. We ask whether LLM judgments of Web news track the market's reaction to the reported event or follow it. To answer, we built a multi-agent trading system whose agents share only point-in-time stores and answer typed questions through the interface of Jev, a hosted typed decision model; code sets every position under a proved bound on how far text can move it. In a hash-committed test of a Jev-compatible reader built from a pinned LLM's option probabilities, item judgments track announcement-window abnormal returns (weekly Spearman 0.119), also after the LLM's release, and event types agree with the issuers' 8-K filings (AUC 0.833); Jev's judgments of news published after its own release track the reaction as well (descriptive). Exploratory analyses show where the association comes from: 72% of earnings news items appear after the issuer's filing, contributor-written items often report the price move, and from the first trade after publication the association falls to 0.023. At a weekly horizon, the confirmatory test detects no rank information over code-only features. Under attack, decision cards traced 88% of successful attacks to the planted item. We propose that market-graded tests of Web-text readers report the criterion from publication, not only from the event.

---


### 93. [Beyond Query Similarity: Safety-Conditioned Cache Routing for LLM Response Reuse](https://arxiv.org/abs/2611.10418)

**<font color=#1a73e8>作者：</font>** Shilong Pan, Zhiliang Tian, Weiguo Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic response caching reuses a cached response for a semantically similar query to improve LLM inference efficiency. However, query similarity alone can lead to unsafe reuse when safety conditions change. Existing approaches improve cache safety through stricter similarity checks, context-aware validation, or response verification, yet they may still miss safety conflicts between the cached response and the new request or introduce unnecessary verification overhead. We argue that safe and efficient semantic caching requires a reuse policy that makes the cached response's safety conditions explicit and uses them to guide the reuse decision with a balance between safety and utility. In this paper, we propose SafeCache, a safety-aware framework that separates candidate retrieval from safety approval and formulates semantic response reuse as a safety-conditioned routing problem. SafeCache matches each cached-response condition against the new request and aggregates the per-condition mismatches into an overall risk score. A separate contradiction guard prevents explicit conflicts from being diluted by strong matches. It further estimates matching uncertainty and calibrates the routing policy under a required unsafe-reuse target and a verifier-call budget to choose among direct reuse, selective verification, or regeneration. Experiments show that SafeCache achieves the better safety-utility trade-off among the evaluated baselines, enabling safer response reuse at comparable cache utility.

---


### 94. [Mental Imagery That Matters: Curing Latent Collapse in Multimodal Reasoning](https://arxiv.org/abs/2611.10423)

**<font color=#1a73e8>作者：</font>** Mi Luo, Rohan Dugad, Zihui Xue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mental simulation, the ability to reason by constructing and updating internal visual states, is central to flexible human cognition, but remains elusive in current multimodal large language models. Latent multimodal reasoning offers a promising route toward this capability by interleaving text with continuous visual latent blocks, allowing models to maintain internal visual workspaces without decoding them into pixels. In this paper, we ask whether these latent visual states actually matter. Through a direct perturbation analysis across representative latent-reasoning MLLMs, we find that they often do not: dropping, replacing, or shuffling generated visual latents has only minor effects on the model's own final-answer probability, while equivalent perturbations to the linguistic reasoning trace are substantially more damaging. We call this failure mode Mental Simulation Collapse (MSC): the model appears to perform interleaved visual reasoning, but routes most answer-relevant computation through text. We further diagnose that MSC follows naturally from existing training objectives: visual alignment can make generated latents resemble helper-image embeddings, but it does not require the decoder to rely on them; subsequent text-only supervision further leaves the semantic role of the latent pathway unidentifiable. To address this, we introduce AnchorSim (Anchored Mental Simulation), a contrastive distillation framework that trains models to make their generated visual latents consequential. Across multiple visual reasoning benchmarks, AnchorSim improves performance, while diagnostic re-evaluation shows that visual perturbations now meaningfully affect predictions. Our results expose a fundamental failure mode of latent multimodal reasoning and demonstrate that mental simulation must be anchored to model behavior in order to matter.

---


### 95. [Governed Self-Improvement for a Local-First Security Analyzer: Baseline Measurements and a Preregistered Evaluation Protocol for Tantular Cyber](https://arxiv.org/abs/2611.10425)

**<font color=#1a73e8>作者：</font>** Raditio Ghifiardi, Rifny Rachman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Local-first security tools let organizations analyze code without sending it to third-party services, but the small language models they can run locally are weaker than hosted ones and are hard to improve without breaching the privacy guarantee that motivates them. We present Tantular Cyber, an open-source, read-only repository security analyzer that keeps deterministic scanner findings authoritative and confines a locally served language model to advisory explanations in Bahasa Indonesia. We report its measured v0.3.0 baseline on a synthetic, ground-truth benchmark: combining Semgrep with an interprocedural call-graph scanner yields precision 0.843 and recall 0.915 (Semgrep alone: 0.818 and 0.766). The advisory layer is the weak point: 57% of explanations met an evidence-grounding check, against 95% for a different 8B model under identical prompts. A forensic re-scoring of retained outputs shows that every grounding failure cites a code identifier absent from the evidence shown, and that a prompt change which appeared to raise grounding from 0.56 to 0.72 did so partly by citing nothing. We document two evaluation-validity hazards we encountered: silent model-file migration during a run and non-reproducible published figures. Building on these lessons and on constraint-aware evaluation from security operations research, we propose a governed self-improvement loop (code-free feedback, curated data, a cheapest-first intervention ladder from prompts to LoRA and weight-space edits, hard gates, and human release approval) and preregister the protocol by which its first cycle will be judged. We report no results for the loop itself.

---


### 96. [D-REAL: Acceptance-Length Optimization with Unbiased Gradients for Speculative Decoding](https://arxiv.org/abs/2611.10432)

**<font color=#1a73e8>作者：</font>** Meng Wei, Yefei Chen, Antong Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding efficiency depends on the number of consecutively accepted draft tokens, yet token-level training objectives do not directly optimize this quantity. We introduce D-REAL (Drafter Reinforcement of Expected Acceptance Length), a post-training method that directly optimizes expected acceptance length for a fixed decoding context. D-REAL weights position-wise draft-target distributional overlap by prefix survival probabilities along a draft-sampled prefix, faithfully capturing the sequential dependence of verification on earlier proposals. By accounting for the parameter dependence of the proposal distribution, we derive an unbiased gradient estimator for this single-round objective under stochastic verification. We evaluate D-REAL on DSpark and DFlash2 with Qwen3-8B as the target model across ten benchmarks. Starting from baselines whose mean acceptance length has plateaued, one epoch of D-REAL post-training consistently improves the benchmark-averaged mean acceptance length by up to 0.23 tokens across both architectures under greedy (T = 0.0) and stochastic (T = 1.0) sampling, translating into up to a 9.4% end-to-end serving throughput improvement.

---


### 97. [Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent Interaction](https://arxiv.org/abs/2611.10439)

**<font color=#1a73e8>作者：</font>** Yunzhe Wang, Mesut Erhan Unal, Sheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents improve their own skills, memory, and harness code from experience without retraining the base LLM, and group-evolving agents go further by sharing these lessons across agents. Yet most such systems overlook that sharing across users and heterogeneous agents requires deciding who can benefit from each lesson and what information must remain private. We present MixUA, a memory system that distills independent user-agent trajectories into lessons and assigns each lesson to a user-agent pair, user, agent, or global scope according to whom it benefits and what it may disclose. For evaluation, we introduce CrossLearnBench, a mixed-user-agent benchmark that pairs established agent tasks with user preferences and privacy probes that test whether private facts leak into memory other users can read. With five users and seven agents, MixUA raises pass rates by up to 16 points over no memory and 5 over a single global memory, even on tasks previously tried only by other users on other agents. It retains up to 90% of previously stated preferences, and at most 0.02% of privacy probes find a planted private fact in a forbidden scope. We hope MixUA offers a scalable path toward a global system where users and agents co-evolve.

---


### 98. [DiSARM: Diverse and Surprising Association Rule Mining with Large Language Models](https://arxiv.org/abs/2611.10445)

**<font color=#1a73e8>作者：</font>** Lijia Liu, Hisashi Kashima  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Exploratory Data Analysis (EDA) aims to discover informative patterns in large datasets. For transactional data, Association Rule Mining (ARM) is an established approach that facilitates EDA by efficiently generating candidate patterns. Beyond efficient mining, identifying informative rules has also been extensively studied through both objective and subjective interestingness measures. Recent advances in Large Language Models (LLMs) offer new opportunities for assessing subjective interestingness using world knowledge. Nevertheless, relying solely on LLMs raises concerns about scalability and statistical reliability. Building on prior ARM research, we propose a hybrid framework, DiSARM, that leverages the world knowledge of LLMs to assess the subjective interestingness of rules, while maintaining statistical reliability and promoting diversity among the selected rules. Across three transactional datasets, experiments demonstrate that DiSARM effectively combines statistical reliability with surprise and diversity, offering a promising approach to ADE from transactional data.

---


### 99. [The Truth Beneath the Tokens: Prompt-Space Recovery of Knowledge Edits in Language Models](https://arxiv.org/abs/2611.10450)

**<font color=#1a73e8>作者：</font>** Manit Baser, Rachel Yeo Hui Min, Aditya Nawal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model editing provides an efficient way to update factual knowledge in transformer models. Recent approaches reverse edits by modifying, masking, or decomposing model weights, but make recovery dependent on weight-space interventions. We instead show that pre-edit knowledge can be recovered through input-space interventions alone, without modifying the edited model's weights. We introduce Memento, a prompt-space mechanism for auditing residual knowledge that learns a reusable recovery signal to steer an edited model toward its pre-edit response. Memento supports both continuous recovery prefixes and discrete textual prompts for standard text interfaces. Across three LLMs and five editing techniques, Memento recovers 80.07% of held-out edited facts, achieving a 9.58% relative improvement over baselines, suggesting that editing may suppress the facts without fully eliminating their recoverability. We further investigate whether prompt-space recovery extends beyond model editing. On pristine, unedited LLMs, Memento improves average factual recall by 53.9% relative to standard inference. These results demonstrate the potential of prompt-space recovery for auditing residual knowledge in edited models and investigating the gap between factual knowledge and its accessibility during inference. We will release our source code.

---


### 100. [BunshinRL: Splitting Live Agent Workspaces for Memory-Efficient Agentic RL](https://arxiv.org/abs/2611.10453)

**<font color=#1a73e8>作者：</font>** Yutong Huang, Vikranth Srivatsa, Alex Asch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) rollouts interleave model reasoning with tool calls in persistent workspaces. Scaling these rollouts incurs substantial memory costs for concurrent environments, while slow tool calls delay entire rollout batches. We present BunshinRL, an agentic RL rollout system that exploits shared environment state and recurring tool calls through three techniques: memory sharing across environments, tool-prefix caching, and speculative tool execution. These techniques build on BunshinFork, a novel live whole-workspace forking mechanism for containers. BunshinFork reconstructs process trees, shares memory copy-on-write, and preserves file, communication, and GUI state, enabling cached-state reuse and rollback after incorrect speculation. We implement BunshinRL and BunshinFork through Linux kernel module and CRIU modifications. BunshinRL reduces peak memory by up to 43%, total memory consumption by up to 51%, and end-to-end rollout latency by 23%.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
