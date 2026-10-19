# 🧠 大模型相关研究 | 2026年10月20日

> 本类共 **258** 篇论文：已确认 **247** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-258](./part-06.md)

---

### 101. [COMET: Decoupled Distillation, Routing, and Capacity Control for Task-Agnostic Continual Vision--Language Learning](https://arxiv.org/abs/2610.22907)

**<font color=#1a73e8>作者：</font>** Seungyoon Woo, Keonhee Park, Gunhee Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) such as CLIP retain zero-shot recognition ability, but their open-world use often requires task-agnostic continual learning: tasks arrive sequentially, past data are unavailable, task identity is unknown, and the backbone cannot be retrained. We argue that this setting fails VLMs through three coupled pressures beyond the stability-plasticity tradeoff: (1) modal-consistency drift, (2) representation-space interference, and (3) per-task capacity shortfall. We propose COMET (Collaborative Mixture-of-Expert Transfer) to resolve these three issues respectively as follows. A frozen teacher provides only a feature reference on a shared image-text pool; Tri-Affinity Distillation preserves image-image, text-text, and image-text geometry; and Student-Aware Cross-Expert Distillation aligns new experts with compatible prior experts so routing errors degrade gracefully. We design COMET to keep capacity and inference separate: a contextual bandit keeps or merges full per-task experts using post-training signals, while a reconstruction router selects sparse experts at test time without teacher semantics. On the X-TAIL benchmark, we show that each proposed component improves continual learning performance. COMET shows that continual vision-language adaptation can preserve multimodal geometry, coordinate accumulated experts, and allocate capacity jointly when feature reference, expert shaping, routing, and capacity control are separated by construction.

---


### 102. [Where's the Indirect Evidence? Investigating Grammatical Generalization with Influence Functions](https://arxiv.org/abs/2610.22919)

**<font color=#1a73e8>作者：</font>** William Dai, Zhenghao Herbert Zhou, Maya Viswanathan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models generalize beyond their training corpus to learn linguistic phenomena (Patil et al., 2024; Misra and Mahowald, 2024), showing that there exists indirect evidence driving learning. Prior work has inferred that indirect evidence exists without identifying its character or considered specific hypotheses about what it might be. We explore an alternative bottom-up method for identifying indirect evidence. We use influence functions (Koh and Liang, 2017) to measure how individual training sentences affect model predictions in 15 grammatical phenomena from BLiMP (Warstadt et al., 2020). We filter out a phenomenon's direct evidence using hand-constructed rules and take the 60,000 most influential remaining sentences as indirect evidence. This indirect evidence substantially affects learning: retraining without it lowers held-out accuracy more than removing a matched random group for every phenomenon across five models (by a median of 12 points). We characterize the indirect evidence by its similarity to our direct evidence filters: it (partially) meets the filters' structural conditions at a median of 4.7 times the rate of a matched random group. Finally, clustering phenomena by indirect-evidence overlap recovers three of the five BLiMP categories that include multiple phenomena, suggesting that this method can reveal linguistic relationships.

---


### 103. [Sep-Latent: Separator Tokens as Natural Compression Anchors for Implicit Reasoning](https://arxiv.org/abs/2610.22924)

**<font color=#1a73e8>作者：</font>** Yinlong Xu, Jianfeng Huang, Zhengdong Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable success in complex reasoning through explicit Chain-of-Thought (CoT), but the associated computational overhead and token verbosity remain significant barriers to efficiency. While implicit reasoning in continuous latent spaces offers a promising alternative, existing methods like Coconut and CODI often rely on fixed-length latent sequences and suffer from representational collapse. In this paper, we propose Sep-Latent, an adaptive implicit reasoning framework that utilizes separator tokens as structural semantic anchors. By introducing an Attention-Decay mechanism, we force the model to aggregate and compress reasoning logic into these anchors during training. We then align explicit and implicit pathways through multi-level distillation across all layers to ensure logical consistency. Crucially, Sep-Latent enables dynamic reasoning depth by adaptively terminating the latent thinking phase based on query complexity. Experimental results on the GSM8k-Aug benchmark show that Sep-Latent achieves an accuracy of 56.8\% with an average of only 5.4 tokens, significantly outperforming prior fixed-length implicit models in efficiency while narrowing the performance gap with explicit CoT. Further analysis via PCA and symbolic variant testing confirms that our method ensures semantic grounding and exhibits superior robustness to perturbations.

---


### 104. [DICL-Qwen3VL: Decoupled Confidence Calibration for Interpretable Workwear Detection](https://arxiv.org/abs/2610.22929)

**<font color=#1a73e8>作者：</font>** Meng Wang, Wu Zeng, Mei Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Poor illumination and occlusion obscure clothing cues in indoor work sites, while diverse clothing styles complicate workwear compliance judgments. Although vision-language models (VLMs) support localization and semantic reasoning, their predictions often lack explicit supporting evidence, and a single confidence score cannot distinguish visual uncertainty from ambiguity in compliance judgments. We propose DICL-Qwen3VL, a decoupled interpretable VLM that integrates structured workwear detection, evidence generation, and separate visual and reasoning confidence estimates. First, low-rank adaptation (LoRA) adapts Qwen3-VL to localize visible upper-body clothing and identify workwear. Second, decoupled calibration separates visual observations from compliance reasoning and assigns a confidence score to each. Token entropy and sensitivity to image perturbations provide supervision for visual confidence, linking confidence estimation to the generated observations and their dependence on image content. Finally, group relative policy optimization (GRPO) jointly optimizes detection accuracy, output validity, and confidence calibration. Experiments on the company-collected Indoor Construction Site Workwear Dataset (ICSWD) and the web-collected Indoor Construction Workwear Dataset (WICWD) yield mAP@50 values of 0.730 and 0.753, respectively, outperforming the evaluated LoRA-adapted VLM baselines, including Qwen3-VL. The framework also provides explicit evidence and separate confidence scores to support manual review in industrial safety monitoring. WICWD is publicly available at this https URL.

---


### 105. [ASR-Style Transcript Normalization Removes Useful Pragmatic Signal for Dialogue Act Classification](https://arxiv.org/abs/2610.22934)

**<font color=#1a73e8>作者：</font>** Lucky Onyekwelu-Udoka, Md Shafiqul Islam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) pipelines often normalize transcripts by removing filled pauses and punctuation and expanding colloquial forms, potentially discarding cues useful for dialogue act classification. We evaluate nine transcript conditions across six classifiers (TF-IDF logistic regression, RoBERTa, BERT, ALBERT, GPT-2, and BiLSTM) and three conversational corpora (Switchboard, ICSI MRDA, and SLUE-HVB), supplemented by multi-seed experiments, normalization controls, and real-ASR evaluations. Across five random seeds, heavy normalization reduces Macro-F1 in all 15 neural model-corpus combinations under the original preprocessing protocols. Removal using the original filler and backchannel lexicon consistently degrades performance on MRDA and SLUE-HVB but produces mixed effects on Switchboard. Punctuation-aware TF-IDF experiments show that punctuation removal reduces Macro-F1 by 0.036 on Switchboard and 0.078 on MRDA, demonstrating that the original linear baseline's apparent insensitivity resulted from tokenization. Restricting filler removal to um, uh, and erm preserves degradation on MRDA but largely eliminates the SLUE-HVB effect, where the original lexicon removes class-defining backchannel expressions. These findings demonstrate that normalization effects depend on preprocessing definitions, feature extraction, and conversational context, supporting task-dependent rather than indiscriminate transcript normalization.

---


### 106. [Many Biases, One Circuit: Post-Training Tunes a Pretrained Cue-Routing Mechanism](https://arxiv.org/abs/2610.22937)

**<font color=#1a73e8>作者：</font>** Prakhar Gupta, Terry Jingchen Zhang, Zhijing Jin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models often abandon a correct answer when the prompt contains a cue, a hint toward a wrong option such as "I think the answer is B." Sycophancy and related biases show this failure. They are often studied separately and blamed on alignment. We test this view causally, tracing the attention heads behind these biases through the stages of two post-training pipelines. In multiple-choice tests on most models, four cue types rely largely on the same few heads, a shared circuit already present in pretrained models. Most base models follow cues in plain text. Fine-tuning a base model on about 200 generic assistant examples without cues activates these heads in chat format, so cue-following can be a side effect of assistant tuning. The final reinforcement learning (RL) stage strengthens the effect of cues in almost every comparison. In Tulu-3-8B and OLMo-2-7B, we swap the attention patterns of six middle layers between the RL checkpoint and its predecessor. For suggested-answer cues, this shifts each checkpoint's cue effect most of the way to the other's level. Post-training thus seems to change when and how strongly models use this circuit. Mitigation for these multiple-choice biases could target this circuit.

---


### 107. [Beyond Surface Cues: Robust LLM-Generated Korean Text Detection](https://arxiv.org/abs/2610.22940)

**<font color=#1a73e8>作者：</font>** SungHo Kim, SangKeun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) generate increasingly fluent text, the need for reliable detection of LLM-generated content has grown substantially. However, existing research remains heavily English-centric, leaving Korean largely underexplored. Moreover, current evaluations of Korean text detection often rely on superficial cues, leading to overly optimistic estimates of detection performance. To address these limitations, we introduce \textsc{KoLing}, a bias-controlled adversarial benchmark comprising 50.9k instances that suppresses superficial shortcuts while preserving semantic content and separately evaluates LLM-generated and LLM-modified text detection. We further propose KoLingProbe, an interpretable detector grounded in theoretical linguistics that models Korean-specific properties across multiple linguistic levels. Experiments show that KoLingProbe substantially outperforms strong baselines on all detection tasks while remaining robust to adversarial attacks. Our analyses further reveal that integrating complementary linguistic features across multiple levels yields both improved performance and interpretability.

---


### 108. [Aligning Language Models Towards Counterfactual Invariance](https://arxiv.org/abs/2610.22942)

**<font color=#1a73e8>作者：</font>** Basar Demir, Emily Shen, Ksheeraj Sai Vepuri 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small variations in prompt characteristics can meaningfully alter the semantics, tone, and contextual assumptions of large language model outputs. Such characteristics can involve group variables such as demographics or other sensitive latent attributes. Sensitivity to such input variables is undesirable when demographic information is causally irrelevant to the task, but might still be relevant for generation of semantically coherent responses. This makes the task of enforcing counterfactual invariance while preserving model utility difficult. To study this problem, we first show that standard model alignment recipes (such as reinforcement learning) increase differences in response quality across demographics, while improving overall response quality, ultimately amplifying what is known as counterfactual bias. To address this, we develop a policy gradient technique involving a group-level reward function that operates on matched pairs of counterfactual prompts. For completeness, we build a dataset of controlled counterfactual prompt pairs and design an evaluation that separately measures cases where demographic information is causally relevant to the answer. Finally, we validate our findings on several fairness benchmarks. We demonstrate that our methods reduce counterfactual differences while preserving overall response quality and that the models continue to adapt appropriately when such sensitive information is relevant.

---


### 109. [When Core-Network Elements Become Reachable: Field-Level Exploitability Analysis in Diameter](https://arxiv.org/abs/2610.22943)

**<font color=#1a73e8>作者：</font>** Wei Yi, Changlong Han, Xue Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing exposure of cellular core-network elements to public networks has turned Diameter signaling interfaces into a practical attack surface. While large language models (LLMs) show promise for protocol exploitability analysis, we find that their judgments on Diameter can be unreliable because they may deviate from the tacit analysis discipline followed by security experts and reach conclusions without considering complete protocol evidence. To address this challenge, we present LENS, an LLM-based system for reliable field-level Diameter exploitability analysis. LENS guides LLMs using both exploitability-analysis discipline and the protocol evidence needed for analysis. It infers analysis discipline from existing exploit writeups and evidence-collection guidance from exploitability-analysis failures, enabling systematic evidence collection, exploitability assessment, and proof-of-concept (PoC) attack generation when applicable. Our experiments show that LENS performs reliable analysis across four LLMs and repeated runs, achieving mean recall of 94.00% to 98.00%, precision of 78.73% to 88.94%, and accuracy of 84.00% to 92.00%. We find that more than 25% of field paths in the S6a and Cx interfaces are exploitable under the considered threat model. We further assess their impact on practical implementations and uncover 95 previously unknown vulnerabilities, including 17 in open-source EPC/IMS implementations and 78 in commercial deployments, causing service disruption, information leakage, subscriber tracking, and accelerated battery depletion. Applying LENS to 16 additional protocols spanning cellular, network, industrial, and host-internal systems uncovers 118 previously unknown vulnerabilities, demonstrating its strong generalizability.

---


### 110. [Large Diffusion Models Need More Than EMA](https://arxiv.org/abs/2610.22945)

**<font color=#1a73e8>作者：</font>** Chuyu Hu, Huanran Chen, Shitong Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale diffusion models are commonly trained with a constant learning rate (LR) and exponential moving average (EMA), despite the strong performance of LR decay and Schedule-Free optimization in training large language models. We study whether EMA is uniquely suited to diffusion training, or whether stronger alternatives have been underexplored. Our theory shows that averaging a constant-step trajectory has an inherent optimization limitation, whereas LR decay and Schedule-Free optimization admit vanishing stationarity guarantees under standard nonconvex assumptions. Empirically, LR decay and EMA provide complementary benefits: combining decay with EMA further improves the standard baseline at most tested starting points, although the gain remains sensitive to when decay begins. Schedule-Free avoids this timing requirement and consistently outperforms EMA with a constant LR across training stages, achieving both lower fixed-evaluation objectives and better generation quality. Our analysis further shows that all three strategies substantially reduce parameter variability, yet stronger stabilization is not always better: EMA with a constant LR retains comparatively higher parameter variability, while aggressive decay combined with EMA achieves the lowest checkpoint variability but also weakens continued optimization. Schedule-Free substantially reduces parameter variability while preserving more late-stage progress, providing a better balance between parameter stability and continued optimization. Finally, the benefits of Schedule-Free extend beyond pretraining to ReFL and generator-side DMD, demonstrating its transferability across distinct diffusion optimization settings. Overall, our results suggest that large diffusion models need more than parameter averaging alone: effective optimization requires balancing variance reduction with continued optimization.

---


### 111. [Recognizing Atari and Assessing Sente: Controlled Evaluation Tasks for Language-Based Go Agents](https://arxiv.org/abs/2610.22953)

**<font color=#1a73e8>作者：</font>** Taiyi Chen, Iskar Deng, Amandalynne Paullada  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Domain terminology provides concise descriptions of game states and strategic relationships, but whether game-playing language models can accurately recognize these concepts and relate them to move evaluation remains unclear. We construct a controlled evaluation set centered on atari and its relationship to sente in Go, examining terminology recognition under local board changes and move evaluation under different strategic conditions. We conduct our tests on LoGos, a Go language model, after fine-tuning it with terminology and commentary supervision. The model struggles to recognize changes in the atari relationship and assess its strategic implications. Its terminology predictions are associated with move preferences even when those preferences contradict the reference evaluation. Our controlled tests provide a framework for examining whether language-based Go agents connect domain terminology with precise board relationships and strategic move values.

---


### 112. [Query-adaptive Recurrent Tokenization](https://arxiv.org/abs/2610.22957)

**<font color=#1a73e8>作者：</font>** Bavesh Balaji, Pranav Gopinath, Pouya Sadeghi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual information worth extracting from an image and the token budget it warrants depend on the text query. Yet modern vision and vision-language models largely encode images independently of the query and allocate a fixed visual token budget to every input. We introduce the Query-Adaptive Recurrent Tokenizer (QART), a backbone-agnostic module that makes visual representations both query-steerable and budget-adaptive. QART steers the visual representation toward query-relevant evidence while adapting its token budget to the amount of information required. Its key principle is simple. Additional tokens are allocated until the visual features relevant to the query are represented with sufficient fidelity. Starting from frozen encoder features, QART recurrently constructs a compact representation and uses reconstruction quality over the query-relevant visual support to control token allocation. On Visual7W and VQAv2, QART achieves 81.96% and 76.37% accuracy using only about 29 visual tokens, reducing token counts by 20-25x relative to dense VLM inputs. It further reaches 92.0% P@1 on CORE and 36.3% PR-AUC on PODS, outperforming SteerViT on PODS by 8.4%. Together, these results show that visual representations need not be fixed in either content or capacity and can instead adapt to what each query requires.

---


### 113. [SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval](https://arxiv.org/abs/2610.22959)

**<font color=#1a73e8>作者：</font>** Haoming Li, Dingyi Kang, Xu Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on persistent memory to support long-term reasoning and personalized interactions. However, information collected from external sources can introduce security risks when untrusted claims (i.e., atomic statements) are later treated as authorized preferences, policies, or permissions. Existing defenses typically rely on content-based filtering or coarse-grained provenance tracking, which either fail to prevent unauthorized memory use or block legitimate information, sacrificing memory utility. To address these limitations, we propose SAFE-Mem, a fine-grained memory governance framework that improves security while preserving legitimate memory use. First, SAFE-Mem annotates each claim with three governance labels (i.e., kind, authority, and scope) to capture its provenance and permitted use. Second, governance-aware retrieval matches query requirements with claim permissions to block unauthorized influence while retaining legitimate information. Third, a governance-enabled memory graph connects source sentences, claims, and entities to support provenance tracking and efficient retrieval. Across four LLM backbones on MPBench and LoCoMo, SAFE-Mem attains the lowest attack success among defenses that retain legitimate memory, at least 77% below the strongest of them, and the highest answer accuracy of all evaluated defenses, improving it by up to 15%. The code is available at this https URL.

---


### 114. [What Shapes Brain Alignment of Large Language Models during Dialogue? Insights from Language Production and Comprehension](https://arxiv.org/abs/2610.22961)

**<font color=#1a73e8>作者：</font>** Yuko Nakagi, Yuya Chiba, Yasue Kishino  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Brain alignment of large language models (LLMs) offers a way to investigate representational similarities between LLMs and the human brain during language processing. While previous studies have mainly focused on passive language comprehension, little is known about such alignment during dialogue, in which speakers engage in both language production and comprehension. In this study, using fMRI data collected during dialogue, we examine brain alignment during language production and comprehension across LLM layers and brain regions. We assess its association with the intrinsic dimension (ID) of LLM representations and the contributions of several interpretable linguistic and communicative features. Our results reveal distinct patterns of brain alignment between production and comprehension, as well as strong associations with ID in brain regions associated with each processing mode. Furthermore, we show that the contributions of linguistic and communicative features also vary across processing modes, LLM layers, and brain regions.

---


### 115. [ANCHOR: Audio-Visually Grounded Chain-of-Thought Reasoning Benchmark](https://arxiv.org/abs/2610.22964)

**<font color=#1a73e8>作者：</font>** Joel Julin, Souraja Kundu, Liza Dahiya 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) perform well on audio-visual question answering, but correct answers do not necessarily imply that their stated reasoning is grounded in relevant perceptual evidence. Existing benchmarks mainly evaluate final-answer accuracy, offering limited insight into whether model-generated rationales correctly identify visual regions, temporal intervals, and audio events supporting predictions. We introduce ANCHOR, a benchmark and evaluation framework for measuring grounded-rationale alignment in multimodal reasoning, comprising 2,319 videos and 8,272 question-answer pairs with structured reasoning traces, temporal evidence, spatial bounding boxes, and salient audio cues, including a human-refined test set of 224 videos and 975 question-answer pairs. We separately measure answer correctness, hallucination, logical divergence, and conciseness, with direct spatial and temporal grounding measurements on a focused subset. Across the full benchmark, twelve contemporary MLLMs show a substantial alignment gap: models with comparable answer performance can differ markedly in whether their explanations are supported by annotated evidence. On a matched subset of 100 videos and 446 question-answer pairs, rankings remain highly stable across human-refined, Gemini-generated, and GPT-generated references (mean Pearson r=0.99), providing evidence against model-reference circularity within this subset. Grounding-cue ablations of three MLLMs on the full human-refined test set reveal a consistent modality hierarchy: removing video reduces accuracy by 38.4-41.8 points, while removing bounding boxes (3.2-7.7 points) and audio (4.2-5.6 points) causes smaller, complementary, model-dependent drops. These findings show answer-only evaluation obscures important grounding failures and position ANCHOR as a testbed for evaluating accurate and evidence-aligned audio-visual reasoning.

---


### 116. [Towards Hyperparameter Transfer for Differentially Private Optimization](https://arxiv.org/abs/2610.22976)

**<font color=#1a73e8>作者：</font>** Tianze Wang, Zhiqi Bu, Linjun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws and hyperparameter tuning remain central challenges in training large-scale models, particularly under differential privacy (DP), where optimization is further complicated by noise injection and per-sample gradient clipping. While Maximal Update Parametrization ($\mu$P) allows for zero-shot hyperparameter transfer in standard training, we show that it fails under DP constraints due to the distinct spectral properties of high-dimensional noise versus low-rank gradients. In this work, we introduce DP-$\mu$P, a theoretically grounded framework that extends $\mu$P to the privacy-preserving setting. By analyzing the interaction between gradient clipping, noise injection, and feature learning, we derive a Signal-to-Noise Ratio (SNR) condition that governs layer-wise learning rate scaling. Combining this with our proposed spectral scaling formulation, we provide specific scaling rules for DP-SGD, DP-Adam, and DP-Muon optimizers. Empirically, we demonstrate that DP-$\mu$P enables effective zero-shot transfer of learning rates across model widths on diverse architectures (MLP, ViT, GPT-2), matching or exceeding the performance of individually tuned baselines while significantly reducing computational costs.

---


### 117. [KiranaBench: Can a Language Model Run a Neighbourhood Shop?](https://arxiv.org/abs/2610.22980)

**<font color=#1a73e8>作者：</font>** Bhuvan Arora, Ankita Karmakar, Chaitanya Jain 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly evaluated on long-horizon tasks, including autonomously running a business. Existing benchmarks for this setting are almost exclusively English-language, Western in retail context, and single-agent, with the agent observing the business directly. We study how these results transfer to a multi-agent Indic setting. We introduce KiranaBench, a simulated Indian general store in which four roles (manager, cashier, helper, and bookkeeper) are each played by a separate LLM agent. Interactions with customers and suppliers occur in English, Hindi, or Hinglish, and product demand is calibrated to India's national Household Consumption Expenditure Survey. Evaluating four open-weight LLMs, we find that all fall far short of a fixed-rule shopkeeper baseline: the best model earns only one-eighth of the baseline's profit, and two models finish below an unmanaged shop. Performance is also consistently lower for Hindi and Hinglish than for English supplier communication. KiranaBench offers evidence that current LLM agents are not yet reliable for autonomously operating small businesses in India, and provides a testbed for developing agents suited to settings that are long-horizon, collaborative, and multilingual.

---


### 118. [How Murky Before a VLM Knows It Cannot See? Accuracy, Confidence and Abstention on a Physical Visibility Axis](https://arxiv.org/abs/2610.22981)

**<font color=#1a73e8>作者：</font>** Mochamad Rizal Fauzan, Irgi Surya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robustness studies of vision-language models (VLMs) grade degradation on nominal severity scales ("level 1-5") that carry no physical units, and they rarely ask whether a model's confidence follows the loss of visibility. We measure accuracy, internal (token-probability) confidence, verbalized confidence and an explicit abstain option on a visibility axis in metres: fog follows the Koschmieder model, an underwater arm scales the absorption spectrum of pure water, both are applied with a monocular metric depth map, and the visibility range V is swept over eight log-spaced levels from 250 m to 1.95 m. On 1000 COCO scenes and five small open VLMs (2-5 B parameters), accuracy on a boxed-object identification task falls from near its clean value to chance within a narrow band (half-way visibility V_acc of 12.1-15.9 m in fog and 20.5-38.6 m under water) while, for the four models that are confident on clean images, the confidence stays high: at V=1.95 m in fog their accuracy is at chance but their mean internal confidence is 0.68-0.84 and their verbalized confidence 0.61-1.00, a blind-spot width W=log10(V_acc/V_aware) of at least 0.79 decades, i.e. a factor of 6.2 in visibility. The remaining model is under-confident throughout and its internal confidence follows accuracy. An explicit abstain option follows accuracy when it names the reason (W from -0.21 to -0.06 in fog) but, for one model, lags with a generic "I don't know" (W up to 0.18). ImageNet-C fog severities 1-5 correspond to only 55-110 m of physical visibility, outside the failure band, and leave the accuracy of the models within 5 percentage points of its clean value. Blank-image and shuffled-image controls, a prior-matched answer set and a 200-image pilot that preceded the study are reported. Findings are descriptive: one draw of 1000 images, depth of assumed scale, and models of 2-5 B parameters.

---


### 119. [UniField++: A Unified Agentic Framework with Loop Reasoning for MRI Field-Strength Enhancement](https://arxiv.org/abs/2610.22982)

**<font color=#1a73e8>作者：</font>** Yiyang Lin, Chenhui Wang, Tianliang Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MRI field-strength enhancement seeks to combine the accessibility of low-field scanners with the image quality of high-field scanners. Yet, existing methods remain prone to anatomical hallucinations, as uniform processing leaves difficult brain regions insufficiently examined and scarce paired data limit their learning of how tissue contrast and anatomical visibility change across field strengths. To address these challenges, we propose UniField++, a two-agent framework that unifies enhancement tasks across multiple field-strength transitions, including 64mT-to-3T and 3T-to-7T. Unified learning allows both the VLM-based planner and the flow-matching-based enhancer to draw on field-dependent image characteristics observed across tasks, rather than relying on a single transition. Trained with radiologists' annotations of hallucination-prone regions and corresponding correction plans, the planner predicts regional risk and formulates targeted restoration strategies. Guided by these plans, the enhancer performs loop reasoning along the flow-matching trajectory, repeatedly processing high-risk regions for additional refinement. Together, cross-transition learning and risk-guided refinement support anatomically faithful enhancement across field strengths. Across the evaluated tasks, UniField++ improves PSNR by an average of 2.74 dB and SSIM by 14.05 percentage points over comparison methods, with corresponding gains of 3.97 dB and 13.92 percentage points over the ablation baseline. It also maintains enhancement quality on an external cohort with an unseen field strength and improves downstream whole-brain segmentation Macro Dice by an average of 0.1457 over the original low-field images. Code is available at this https URL.

---


### 120. [Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them](https://arxiv.org/abs/2610.22984)

**<font color=#1a73e8>作者：</font>** Weixiang Zhao, Yichen Zhang, Yanyan Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Experience-driven self-evolution offers a promising path for large language model (LLM) agents to continually improve through interaction. Yet existing approaches often rely on successful trajectories or external evaluation signals, leaving unclear whether agents can evolve when such positive anchors are unavailable. We study this question through Cold-Start Failure-Only Evolution (CFOE), where agents start without accumulated experience and learn only from failed interactions without privileged guidance. Across three self-evolving paradigms, multiple LLM backbones, and four interactive environments, we uncover a consistent repair-generalization gap: failure-derived experience can help repair previously failed tasks, but rarely yields sustained improvements on unseen tasks. Further analysis shows that agents often misinterpret failures, while even verified-correct experience remains difficult to transfer. Relaxing CFOE reveals that verifier feedback and additional interaction provide limited gains, whereas successful trajectories substantially improve transfer. These findings suggest that current self-evolving agents are better at repairing observed failures than building generalizable capabilities from failure.

---


### 121. [Prism Attention: Proposal-Refined Index Sharing Mechanism for Efficient LLMs Inference](https://arxiv.org/abs/2610.22985)

**<font color=#1a73e8>作者：</font>** Zhenxu Tian, Kebin Liu, Zhengwu Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context decoding in large language models (LLMs) is increasingly bottlenecked by the memory and computation required to attend over an ever-growing Key-Value (KV) cache at each autoregressive step. Although token-level sparse attention reduces this burden by restricting computation to a small subset of relevant past tokens, its practical gains are often offset by repeatedly recomputing layer-wise sparse indices as the context grows. A common remedy is to share sparse indices across layers by computing them only at designated anchor layers, but such static reuse ignores the layer-wise evolution of attention patterns, causing the reused indices to progressively deviate from the layer-specific optima and incur substantial attention loss. By revisiting cross-layer sparsity from the perspective of attention dynamics, we find that inter-layer salient token shift is highly localized: although the exact top-$\kappa$ indices differ across layers, the core high-attention tokens remain stable, with changes concentrated near the expanded boundary of previously selected regions. Motivated by this, we propose Prism Attention, a proposal-refined sparse attention framework. It replaces rigid cross-layer index reuse with a coarse-to-fine strategy, preserving layer-wise adaptability while retaining the efficiency benefits of cross-layer sharing. Extensive experiments show that Prism Attention achieves state-of-the-art performance among mainstream sparse attention methods on both reasoning and long-context benchmarks, while attaining a $3.4\times$ end-to-end decoding speedup over FlashAttention at 128K context length.

---


### 122. [From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents](https://arxiv.org/abs/2610.22987)

**<font color=#1a73e8>作者：</font>** Xianglin Yang, Yechao Zhang, Jiahao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents use execution harnesses to constrain the consequences of prompt injection by enforcing permission boundaries. These systems deterministically intercept any out-of-sandbox action and prompt the user for approval. To reduce approval fatigue, users can approve allow-rules proposed by the agent, after which any future action matching the rule is allowed without a prompt. In this work, we show that this mechanism introduces a new risk: untrusted context can influence the permissions presented for approval, with consequences extending beyond the immediate task. We investigate privilege escalation targeting this permission-update process. Specifically, adversarial context planted in a repository can reliably steer an agent performing a routine task into requesting a plausibly justified, yet dangerously broad allow-rule. If the user approves the request, the saved rule can effectively blind the harness, enabling adversaries to execute malicious actions that would otherwise require approval, without triggering human oversight. Across production platforms, including Claude Code and Codex CLI, we demonstrate that agents successfully elicit the target allow-rules in 58% of experimental instances. Once acquired, these rules exhibit a massive semantic blast radius, covering 56.9% of category-specific capability test cases. To further quantify the downstream risk, we show that conditional on rule approval, our exploit achieves verified, silent goal completion in 47 of the 58 eligible instances (81.0%), undermining the safety promise of human-in-the-loop oversight.

---


### 123. [Surprise Masking: Private Data Filtering with Model Likelihoods](https://arxiv.org/abs/2610.22988)

**<font color=#1a73e8>作者：</font>** Riya Tyagi, Sahra Ghalebikesabi, Vinnie Monaco 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data useful for language model (LM) training can contain private or unwanted information that is at risk of being learned or memorized. We propose Surprise Masking (SM), a simple form of perplexity filtering that uses a publicly available reference model to identify unwanted spans and suppress learning from them while preserving the rest of each example. On synthetic code benchmarks, we show SM improves the privacy-utility tradeoff over standard masking methods and PII filtering. In fine-tuning experiments, SM reduces approximate extraction of private values from revealed prefixes from 66.3% to 2.3% and the reproduction of stylistic coding quirks from 23.6% to 1.3%, both while preserving performance on the evaluated coding tasks. We also evaluate SM for sanitizing datasets by directly removing unwanted content. Here, SM outperforms DePA, a perplexity-based defense for detecting poisoned dead code, while specialized detectors perform better on broader credential and PII benchmarks. Across eleven settings, we find that SM's downstream success is predictable from the separation of unwanted and useful content in the distribution, and it is particularly useful with code data. Ultimately, SM is an inexpensive, adaptable method to preserve valuable examples while reducing the learning of unwanted information.

---


### 124. [PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas](https://arxiv.org/abs/2610.22990)

**<font color=#1a73e8>作者：</font>** Haoming Li, Defu Cao, Xu Hu 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) are commonly evaluated against fixed task specifications, but users may omit requirements, add constraints, or require approval before consequential actions. Completing the benchmark instruction does not guarantee serving the person who asked. We introduce PersonaCUABench, which holds 74 tasks across 11 domains fixed and varies only who asks. A persona agent, playing one of 44 personas in four groups, rewrites each instruction in that user's own words and answers the CUA's questions, while the CUA sees only the dialogue, never the profile or the original instruction. Across nine backbones (3,330 runs), mean task completion falls by 36% relative to the original requests. The losses have two sources: in 59.9% of cells that lose points, the agent engages with what the user asked for and still gets it wrong, and 11.2% are stops the user requested that the checker scores as failures. Even when a persona request is fully completed, the user gives the top satisfaction rating in only 62.7% of cells, against 84.1% for the original requests. CUAs should therefore be evaluated not only on task completion but also on whether they meet the requirements and constraints users express. Code: this https URL. Project page: this https URL

---


### 125. [Controlling the Diversity-Quality Trade-Off of LLMs by Merging Models Before and After Alignment](https://arxiv.org/abs/2610.22999)

**<font color=#1a73e8>作者：</font>** Yasuaki Sumita, Tomoharu Iwata, Toshiyuki Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Alignment is known to change the output characteristics of large language models (LLMs). Base models tend to generate more diverse outputs, whereas aligned models tend to produce higher-quality outputs. The appropriate balance between the two depends on the task. Existing methods either require costly fine-tuning or, like temperature sampling, mainly improve lexical diversity rather than semantic diversity. We introduce a depth-aware FrankenMerging approach for controlling the diversity--quality trade-off between an aligned model and its base model without additional training. This approach combines the lower layers of an aligned model with the higher layers of its base model based on the hypothesis that lexical diversity is more closely associated with lower layers and semantic diversity with higher layers. Experiments showed that varying the number of layers taken from each model adjusts both diversity and quality. In most cases, the merged models exhibited higher semantic diversity than the aligned model, and at some split positions, they showed higher lexical diversity than both original models. They also demonstrated a better diversity--quality trade-off than temperature sampling in most settings. A supporting ablation, in which we reversed the merging order, yielded results largely consistent with the hypothesis.

---


### 126. [Efficient CPU-GPU collaborative MoE inference via Adaptive Expert Assignment](https://arxiv.org/abs/2610.23006)

**<font color=#1a73e8>作者：</font>** Wenhui Lv, Yunming Liao, Hongli Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models reduce inference computation through sparse expert activation, but their large expert memory footprint often exceeds GPU capacity, making expert offloading necessary for memory-constrained inference. However, existing systems typically handle GPU-missed experts by either transferring them to the GPU, incurring substantial PCIe transfer latency, or executing them on the CPU, making the slower CPU computation the bottleneck. To address these limitations, we present \method, a CPU-GPU collaborative MoE inference system that adaptively assigns these missed experts to the CPU or GPU for efficient execution. By exploiting differences in expert token-loads, \method selectively transfers high-load experts to the GPU while executing low-load experts on the CPU. To minimize inference latency, \method adaptively adjusts expert assignments to balance the CPU computation path against the GPU transfer-and-computation path, allowing both execution paths to complete as early as possible. Extensive experiments on three representative MoE LLMs show that \method improves prefill speed by up to 51.9\% and decode throughput by up to 39.5\% over the strongest baseline across the evaluated batch sizes, with consistent gains under different GPU-memory budgets.

---


### 127. [Adaptation of Computer Use Agents to New Software with User Manuals](https://arxiv.org/abs/2610.23012)

**<font color=#1a73e8>作者：</font>** Chulhoon Yoon, Kyungri Park, Jinyeong Yun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal foundation models have significantly improved the ability to operate real-world software through graphical user interfaces (GUIs) using visual observations and natural language instructions. However, maintaining strong performance on unseen applications remains challenging, as practical tasks often require long-horizon procedural knowledge and application-specific operation patterns. In addition, constructing executable tasks and collecting corresponding trajectories for training still heavily rely on human-annotated data, incurring substantial cost. In this paper, we propose MAGE (Manual-augmented computer use AGent Execution and learning), a framework that leverages user manuals as a scalable source of procedural knowledge to improve both inference and training. During execution, MAGE retrieves task-relevant manual content and uses a planner to generate explicit procedural guidance for CUAs. To further account for the discrepancies between manuals and actual GUI environments, such as version differences or user settings, MAGE also adapts the agent policy through environment interaction. During training, MAGE converts manuals into executable task-plan pairs and uses the plans to guide environment rollouts toward task-relevant states; the resulting trajectories are then used to optimize the policy without human-authored demonstrations. This unified design enables effective utilization of manuals for both task execution and training, reducing reliance on human-authored training data. Experimental results across six applications demonstrate improvements in task success rates over strong baselines, highlighting the effectiveness of manual-guided planning and policy adaptation in new software environments. We provide the code and reproduction scripts at this https URL.

---


### 128. [Causal Value Attribution of Marketing Labels in LLM-Generated Ads: A Deconfounder Approach](https://arxiv.org/abs/2610.23025)

**<font color=#1a73e8>作者：</font>** Danhong You, Wei Jiang, Zhiqiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI-generated content becomes commoditized, economic value increasingly shifts from final artifacts to the upstream expertise used to specify inputs that steer LLM generation. Yet organizations lack methods for valuing this expertise and identifying which individual skills or configurations causally improve performance. This study examines generative marketing, where structured expert labels serve as skill primitives conditioning LLM-generated advertisements. Estimating their causal effects is difficult because outcomes reflect stochastic LLM mediation, high-dimensional label interactions, and multimodal confounding. This study proposes D-VAE (Deconfounder Variational Autoencoder), a counterfactual-inference framework integrating a multi-treatment deconfounder with causal representation learning. D-VAE recovers causally disentangled expert-labeling logic and derives PAC-based bounds on omitted-variable bias from single-treatment confounders. Applied to 29,177 foundation-makeup ad creatives, D-VAE outperforms state-of-the-art benchmarks. A field experiment shows that recommended configurations increase engagement by 32.7% and perform statistically indistinguishably from human experts, while a simulation study confirms causal attribution under complex confounding and treatment interactions. Overall, the study shifts value assessment from AI-generated products to skills, providing a foundation for pricing and optimizing AI-augmented skill portfolios.

---


### 129. [Towards Looped Models Done Right, Part I: Topology, Input Injection, Recurrent-State Design](https://arxiv.org/abs/2610.23036)

**<font color=#1a73e8>作者：</font>** Benhao Huang, Chufan Shi, Junlin Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models reuse physical Transformer blocks across logical depth, but established architectures entangle recurrence placement, input injection, and recurrent state organization. We isolate these axes in models trained from scratch at matched parameter scale, logical depth, and token budgets, and then test whether the resulting design principles transfer to resident- and active-parameter-matched Mixture-of-Experts (MoE) models. The prelude-recurrent block-coda sandwich architecture consistently improves performance on context extraction and reasoning-intensive tasks. Input injection primarily enhances knowledge retrieval and context utilization, whereas random initialization and separate H/L recurrent states provide mixed or negative returns. Taken together, these results favor the Huginn-style design: at the 730M-parameter and 336B-token scale, the complete Huginn architecture outperforms Ouro across all ten benchmarks. The advantages of Huginn over Ouro transfer to MoE models. At the 8BA0.8B (32BA3B when unrolled) scale trained on 500B tokens, Huginn outperforms Ouro on nearly all benchmarks spanning knowledge, reasoning, and coding, while also exhibiting more balanced expert routing. Under matched training and inference FLOPs, the Huginn-style model uses 75% fewer resident parameters than a 112-layer feedforward MoE baseline. Despite its smaller physical parameters, it outperforms the feedforward baseline on DROP and GSM8K, matches it on MATH500, and remains competitive on the other benchmarks.

---


### 130. [Where Research Ideation Begins: Forward-Citation Supervision for Actionable Limitation Generation](https://arxiv.org/abs/2610.23038)

**<font color=#1a73e8>作者：</font>** Liyang Zhao, Yong Cao, Haibin Ling  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated research ideation has advanced rapidly, with multi-agent workflows that generate whole research ideas end to end. These frameworks leave largely unexamined the step that seeds a good idea: identifying an actionable limitation from literature. In this paper, we focus on this first step in the research ideation pipeline. Starting from a pilot study, we find that as large language models (LLMs) scale from 0.6B to 32B parameters, they become far better at recognizing which limitation later work addressed, but no better at generating one, suggesting that the bottleneck lies in the supervision signal rather than model capacity. We therefore construct ActLim-Bench from forward citations, yielding 18,279 evidence-linked supervision triples with human verification. On this signal, we propose a three-stage post-training pipeline: supervised fine-tuning, verifier-filtered rejection-sampling fine-tuning, and reinforcement learning with the verifier as an online dense reward. Experimental results show that our method achieves the highest recall score compared to existing methods among all frontier models. We further show that our generated limitations are preferred in 64.9% of non-tied human comparisons and improve downstream ideation systems. We will release our data and code upon publication.

---


### 131. [GR-OPD: Group-Relative Sequence Credit for On-Policy Distillation](https://arxiv.org/abs/2610.23042)

**<font color=#1a73e8>作者：</font>** Yushu Wang, Renkai Yang, Jingcao Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) provides token-level teacher feedback, yet common sampled-token updates assign credit locally and omit the effects of earlier actions on subsequent feedback. We introduce \method{} (Group-Relative On-Policy Distillation), which decouples feedback computation from credit assignment by aggregating token feedback into calibrated sequence-level credit. We establish a theoretical basis for this approach by showing that, under ideal on-policy assumptions, broadcasting raw summed feedback to every response token yields an unbiased estimate of the negative gradient of the sequence-level reverse-KL objective. To support effective learning in practice, \method{} discounts later feedback that may become less reliable under distribution shift and uses same-prompt rollout groups to calibrate teacher guidance. It preserves relative response preferences while retaining a controlled fraction of the group mean, which we term collective teacher pressure. Across five Qwen3 teacher--student settings and six mathematical reasoning benchmarks, \method{} outperforms vanilla OPD in macro Avg@K in every setting, including gains of 10.9 and 11.5 percentage points in two settings with matched thinking patterns. It also maintains stable training under mismatched thinking patterns, where vanilla OPD collapses. Ablations show that retaining an appropriate amount of collective teacher pressure can improve learning, while excessive collective teacher pressure or an unrestricted feedback horizon can destabilize training.

---


### 132. [Where Does the Performance Go? Understanding and Recovering Performance Regressions in C-to-Rust Translation](https://arxiv.org/abs/2610.23044)

**<font color=#1a73e8>作者：</font>** Zhiqiang Yuan, Chong Wang, Zhenhao Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rust is increasingly adopted as a memory-safe successor to C, and transpilers such as \crust{} can migrate entire C projects while preserving their behavior. Preserving behavior, however, does not guarantee preserving performance. We study this gap on 20 real-world C projects and their \crust{} translations. On the eight projects used for analysis, the translated Rust is more than 3\% slower than the original C on 12 of 19 operations, by up to 62.2\%. By comparing execution-cost profiles, optimized LLVM IR, and compiler optimization remarks across each C--Rust pair, we trace these slowdowns to nine recurring performance issues, spanning residual runtime work, missed compiler optimizations, and C-style source patterns, and derive an optimization direction for each. We then present \ourtool{}, an LLM-based approach that encodes these issues as reusable optimization rules to recover the performance of translated Rust. \ourtool{} profiles each project to locate hot functions and matches them against rule-specific patterns. The LLM then checks each rule's rewrite preconditions against the project context before rewriting, and a rewrite is kept only if it passes both functional and performance validation. On 41 operations from twelve held-out projects, \ourtool{} preserves C outputs on all tested workloads and speeds up 40 operations over the \crust{} translations, 18 of which end up faster than the original C. It outperforms the general-purpose coding agent \codex{} on 31 of the 37 operations where both preserve C outputs, and outperforms its own variant without rule guidance on 34 of the 41 operations.

---


### 133. [Agentic In-Context Learning: What Algorithms Can Transformers Learn in Closed-Loop Interaction?](https://arxiv.org/abs/2610.23051)

**<font color=#1a73e8>作者：</font>** Shiguang Wu, Yaqing Wang, Quanming Yao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The learning algorithm view of in-context learning (ICL) studies how fixed-parameter Transformers learn from supplied examples. Language model agents extend this setting through interaction: their actions determine what evidence enters context next. We call this regime Agentic In-Context Learning (Agentic ICL). Existing studies largely depend on externally supplied contexts or reward-bearing interaction histories, while work on general tool-using agents lacks a learning algorithm view. We represent an interactive learner by its state, update, and decision rule, covering active learning, bandits, and online reinforcement learning (RL). For expressivity, we construct causal Transformers that approximate these algorithms over a finite horizon, and bound the resulting loss in return. For training, we characterize when optimizing process rewards preserves behavior that maximizes the final outcome. Distillation experiments show that Transformers can learn to execute three representative recursions. We then train models from outcome or process rewards without oracle action or state targets, as in RL post-training. Different rewards yield distinct decision policies. Improving the alignment of process supervision with outcome-optimal action preferences shifts learned decisions accordingly. Such behavioral differences persist in a pretrained language model across textual paraphrases.

---


### 134. [Thought Blocks: Non-Autoregressive Latent Communication for Multi-Agent Systems via Trajectory-to-State Compilation](https://arxiv.org/abs/2610.23056)

**<font color=#1a73e8>作者：</font>** Zhenhan Guan, Xiaolong Liu, Hengwei Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems typically communicate through text, incurring repeated generation and re-encoding costs. Although latent communication removes explicit verbalization, constructing latent messages may still require autoregressive latent trajectories. We therefore distinguish message representation from message construction and ask whether agents can directly construct useful continuation states without executing the trajectories that normally produce them. We formulate this problem as trajectory-to-state compilation and introduce Thought Blocks, fixed-size blocks of latent key--value (KV) continuation memory constructed in one shot. Thought Blocks achieve a 2.5 times average latency speedup over autoregressive latent communication. Compared with text-based multi-agent communication, Thought Blocks reduce text tokens by 45.7% and autoregressive steps by 84.8%, achieving an 8.6 times average latency speedup. These results demonstrate that trajectory-to-state compilation enables efficient inter-agent latent communication without sequential latent rollouts at inference.

---


### 135. [Same Person, Different Advice: Auditing LLM Financial Advice with Repeated Risk-Tolerance Responses](https://arxiv.org/abs/2610.23060)

**<font color=#1a73e8>作者：</font>** Soovadeep Bakshi, Apurba Bose, Aishwarya Bose 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI financial advisers set a client's stock allocation largely from one stated-risk question, yet people do not answer it the same way twice: in a national US panel, 41% of households chose a different answer two years later, and in a laboratory retest a third of people moved two or more points on a 0-10 scale after six months. Seven large language models from five providers gave one-turn allocation advice for 800 real household profiles in which only the risk answer changed. The recommended stock share moved by 10 to 16 percentage points on average, and by 24 to 35 when the answer changed, against 0.6 to 4.2 points for the same prompt asked twice; in the laboratory retest the rating alone moved advice by 11 to 18 points. Without any note, the models respond to the answer about as strongly as when told that it is very reliable (less so for the two Claude models). If that instructed response is how each model maps attitude to advice, discounting the answer for its measured reliability, as classical test theory prescribes, would cut the swings by a factor of 2.4 to 3.3. The swing is largest for clients under 40. A note that the answer is noisy steadies some models, but shifts their weight to the client's age and pulls cautious clients towards a generic middle allocation: clients unwilling to take any risk are advised 22% stocks instead of 4%. Three extra money questions reduce the swing for some models, with no statistically detectable change relative to how much advice differs across people. In a scripted test, one clarifying question removes nearly all of the swing from an answer the client then corrects (33.5 points to 1.9 on average) while keeping the response to a change the client confirms. We argue that same-person retest audits should be a standard check for AI advisers, and that what to do with an unreliable answer is a question of client autonomy as well as of statistics.

---


### 136. [ParetoChat: An LLM-Based Interface for Interactive Multi-Objective Optimization](https://arxiv.org/abs/2610.23062)

**<font color=#1a73e8>作者：</font>** Gokhan Ceyhan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-objective optimization models are often deployed in settings where decision makers (DMs) must balance some conflicting criteria. In practice, however, stakeholders must translate their qualitative preferences between different criteria into numerical weights, priorities, or reference points required by optimization methods, which can be difficult to specify and interpret. This paper proposes \emph{ParetoChat}, an LLM (large language model)-based expert-agent interface for interactive multi-objective optimization. The agent translates natural-language user input into structured scalarization parameters, invokes an optimization system, presents candidate solutions, and iteratively elicits feedback. We describe a multi-agent architecture that separates input processing, multi-criteria decision-making (MCDM) expertise, solution presentation, and feedback processing. We then present a simulation study using an LLM-based DM agent and benchmark ParetoChat against interactive methods implemented in DESDEO, including reference-point and NIMBUS methods. The computational experiments on multi-objective binary knapsack and set-partitioning instances show that ParetoChat can guide the search efficiently toward solutions that match the DM's preferences. An application to historical courier-order assignment instances illustrates how users can explore objective extremes and intermediate trade-offs through natural-language requests. The results indicate that LLM agents may provide a practical interaction layer between business stakeholders and optimization tools.

---


### 137. [Before Retrieval Begins: Safety and Tool-Use Decisions in LLM Agents](https://arxiv.org/abs/2610.23071)

**<font color=#1a73e8>作者：</font>** Aditya Nawal, Manit Baser, Mohan Gurusamy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly act as agents that call external tools, yet most tool-safety research examines only what follows a tool call. The prior decision of whether to call the tool remains largely unexamined and can influence downstream safety. Across the seven open-weight models, the unweighted model-average harm rate after admitted harmful requests is 74.5%. To identify what governs this decision, we apply a factorial intervention to the input request. Within our generated construction, neutralizing the requested-operation component produces the largest admission contrast (19 pp). A linear direction estimated from this contrast influences held-out admission in four of seven models; effects on operation-neutralized requests in some models show that it is not an operation-specific mechanism. We then test whether written refusal is behaviorally and representationally coupled to the same decision. Written refusal accompanies 33.6% of admitted harmful calls. Plain-text refusal training reduces unsafe admission in models that retain benign tool use, showing that response-level safety training can transfer to the call decision. Together, these results establish a partial, model-dependent relation between written refusal and tool admission. They motivate direct evaluation and supervision of tool admission rather than treating text refusal as its proxy.

---


### 138. [When Approval Becomes Execution: Authorization-Grounded Workflow Attacks on Tool-Using Agents](https://arxiv.org/abs/2610.23077)

**<font color=#1a73e8>作者：</font>** Chenggong Shi, Hongmei Mou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using language-model agents increasingly rely on local services for document access, approval management, and enterprise workflow execution. This paper studies an authorization-grounded workflow attack in the OpenClaw Agent Security Attack Competition, a controlled benchmark derived from SeClaw-style security task synthesis. Rather than using explicit policy-override instructions, the attack guides the agent through a locally coherent approval workflow: a protected document request is denied, the agent requests a normal approval token from the local approval service, and the returned token is supplied to the document service through authorized_by. Official submission traces show this pattern succeeding on three Enterprise OA document targets. We also conducted 23 controlled local validation experiments in the official OpenClaw execution environment: the original configuration reached the approval-token transition in 9/9 reruns and completed the exact target operation in 8/9 reruns, while single-component variants remained successful on the three document targets. The results provide concrete case evidence of an authorization-context gap: token possession can be treated as sufficient authorization even when requester identity, approver authority, resource scope, action type, destination or recipient, and business purpose are not jointly enforced. We present the attack pattern, controlled trace analysis, and defensive implications for context-bound tokens, service-side policy binding, agent-side authorization checks, and trace-aware benchmark design.

---


### 139. [The Ethics of Prompt Engineering](https://arxiv.org/abs/2610.23082)

**<font color=#1a73e8>作者：</font>** Federico Germani, Giovanni Spitale  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Prompt engineering is commonly understood as a technical practice aimed at eliciting useful, accurate, and appropriately structured outputs from large language models (LLMs). Yet prompts do more than optimize model performance: they shape what information is elicited, which assumptions are introduced, and which perspectives are privileged. In this paper, we argue that prompting should therefore be understood as an epistemic and normative act. We distinguish between two conceptions of prompting: knowledge generation, in which the model is implicitly treated as an epistemic authority, and knowledge injection, in which users provide relevant knowledge, evidence, and context that the model can organize, articulate, and extend. We contend that the latter provides a more appropriate model for responsible LLM use, since prompting cannot substitute for subject-matter expertise or the critical evaluation of model outputs. At the same time, prompts inevitably inject values, intentions, and assumptions into the generation process. Building on these premises, we propose five principles for responsible prompting: epistemic humility, explicit engagement with uncertainty and epistemic underdetermination, source sensitivity, avoidance of deceptive framing, and recognition of model limitations and appropriate task allocation. We further argue that responsibility for AI-generated outputs is distributed across users, developers, institutions, and societies, and that some applications cannot be rendered ethical through better prompting alone.

---


### 140. [Disentangling Language Effects on Tool Admission and Post-Retrieval Safety](https://arxiv.org/abs/2610.23093)

**<font color=#1a73e8>作者：</font>** Aditya Nawal, Manit Baser, Mohan Gurusamy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly use retrieval tools across languages, yet their safety evaluation remains English-centric. It remains unclear whether language affects tool admission, post-retrieval generation, or both. We independently vary request, retrieved-page, and required response languages in a controlled URL-retrieval setting across ten models and seven languages. We identify Safety Loss through Interlingual Processing (SLIP). Non-English harmful requests increase mean tool admission from 46.9% to 67.4%, with a positive mean change in every model. This pattern also persists in an autonomous retrieval setup across all four models tested in this setting. Requiring answers in the page language increases pooled harmfulness on matched tool calls from 50.3% to 57.4% across four closed-weight models, mainly in Chinese and Hindi. Translating pages alone produces no consistent harm increase in eight models with comparable inference settings. Automated audits show that a non-harmful response may be a genuine safety refusal, a deflection citing language difficulties, or an unusable answer. Harmfulness labels alone cannot distinguish these outcomes. Multilingual safety evaluations should therefore measure tool admission and response harmfulness separately and distinguish refusal from capability failure.

---


### 141. [WebCoder: Scaling General Frontend Development with Artifact-Grounded Agentic Reinforcement Learning](https://arxiv.org/abs/2610.23104)

**<font color=#1a73e8>作者：</font>** Zijun Dou, Zhen Yang, Xijun Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world frontend development requires agents to compose reproduction, generation, modification, and repair over an evolving application state. Learning a general policy for this process requires translating heterogeneous execution feedback into task-aligned rewards and effective credit assignment across long sequences of interdependent actions. We introduce WebCoder, a general frontend development agent trained with artifact-grounded agentic reinforcement learning. Our key idea is to assess diverse development activities through their effects on a shared executable artifact and its satisfaction of task requirements. We build Webdev-World, an executable environment that integrates code editing, application execution, browser inspection, and on-demand skills while preserving project state across interactions. An independent verifier evaluates the final application against task requirements to provide terminal rewards, while changes in intermediate artifact progress redistribute the resulting rollout advantage across development segments. Context compaction and message-tree sample construction support training on trajectories beyond a single context window while avoiding repeated loss computation on shared generated history. We further introduce Webdev-Bench to evaluate composed development requirements within a single project. On Webdev-Bench, WebCoder-27B raises requirement satisfaction from 64.8 for its Qwen3.8-27B base model to 72.8, exceeding Claude-Opus-4.8 (65.1) and GPT-5.4 (59.6); on Vision2Web, it improves the average visual and functional score from 41.1 to 62.4, on par with Claude-Opus-4.8. Ablation studies confirm the contributions of artifact-grounded credit assignment and long-horizon training.

---


### 142. [Domain-specific language alignment of multimodal embeddings towards explainable predictions](https://arxiv.org/abs/2610.23110)

**<font color=#1a73e8>作者：</font>** Gabrielė Tijūnaitytė, Thijs L. van der Plas, Mohamed-Bachir Belaid 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal data are commonly fused into latent representations that improve downstream task performance but are not interpretable, limiting their application in domains that require explainable model decisions. Vision-language alignment has made image embeddings interpretable through language, but requires vast image-caption training data. However, captioned data are typically not available for multimodal embeddings, as relevant features cannot directly be observed and annotated from embeddings alone. Here, we propose a framework to language-align any embedding space that can be linked to interpretable auxiliary data. Captioning functions convert auxiliary data into partial captions; a soft contrastive loss weights pairs by the similarity of their properties that each caption describes; and a rank-based concept retrieval task evaluates alignment against the auxiliary data rather than the captions. We apply this framework to multimodal Earth embeddings to facilitate explainable predictions for two species distribution modelling tasks: S2BMS and SatBird. AlphaEarth embeddings beat previous state-of-the-art models on 6/7 metrics, while our framework language-aligns domain-specific concepts of the embedding space, outperforming previous Earth observation vision-language models on average concept retrieval for both datasets. Finally, aligned concepts recover species-habitat associations ($\rho$=0.44) and relate habitat descriptions to species predictions, showing that abstract embeddings can be interrogated in the language of domain experts.

---


### 143. [LED: Improving Masked Diffusion Language Models by Lookahead Editing](https://arxiv.org/abs/2610.23122)

**<font color=#1a73e8>作者：</font>** Yuyan Zhou, Zeyuan Yang, Yuxuan Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) have emerged as a promising alternative to autoregressive language models, enabling non-autoregressive text generation through parallel decoding. Existing dLLMs can be broadly categorized into two families: masked diffusion models (MDMs) and uniform diffusion models (UDMs) In this work, we theoretically show that MDMs are easier to optimize due to their mask-based transition schedule but have lower computational expressivity, whereas UDMs enable iterative state revision and greater expressivity but are substantially harder to train. This trade-off raises a natural question: can we obtain the expressivity of iterative revision without giving up the simple, easy-to-optimize transition schedule of MDMs? Motivated by this analysis, we propose Lookahead Editing (\ours{}), which augments masked diffusion decoding with a rewritable proposal state. At each decoding step, the model performs several lookahead updates to iteratively refine future predictions in this proposal state before committing tokens to the masked sequence. This design introduces a rewritable proposal that uses additional compute to improve expressivity while keeping the simple mask-based transition schedule of MDMs. We fine-tune Qwen2.5-7B and Qwen3-8B to obtain LED-\texttt{7B} and LED-\texttt{8B}, respectively. Across eight benchmarks, LED SFT yields average gains of $+11.4$ and $+7.7$ points over standard MDM SFT. Moreover, using SFT alone, LED-\texttt{8B} outperforms LLaDA2.1-16B Q-mode, which is trained with continued pre-training, supervised fine-tuning, and reinforcement learning.

---


### 144. [MetaCurate: Evolving Curation Filters for High-Quality Agentic Coding Data](https://arxiv.org/abs/2610.23134)

**<font color=#1a73e8>作者：</font>** Donghoon Kim, Seunghyuk Oh, Kevin Galim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning on agent trajectories is an effective way to improve coding agents, but selecting useful training examples requires more than identifying successful runs. A resolved patch may follow inefficient reasoning or unnecessary tool use, while a failed run may still contain useful intermediate steps. Training pipelines therefore rely on rules and qualitative assessments to filter trajectories, yet designing these filters typically requires substantial human expertise, and validating improvements through repeated training and evaluation is expensive. We introduce MetaCurate, a training-free framework that evolves executable trajectory curation filters using pairwise LLM judgments. Disagreements between the filter's rankings and the judge's preferences provide targeted feedback for jointly revising its rules, rubric, and aggregation policy. The resulting filter scores trajectories independently, so pairwise comparisons are required only during search. Starting from a blank filter, MetaCurate autonomously discovers a curation strategy that achieves competitive downstream performance without task-specific handwritten criteria. We validate downstream utility through controlled SFT experiments on our uncurated trajectory pool and the Nemotron v3 SWE dataset, with random selection and hand-authored filtering as baselines. In our experiments, MetaCurate achieves the highest mean SWE-Verified score among the compared methods, including hand-authored rule-based filtering and a training-loop baseline whose search costs 3.5x as much.

---


### 145. [LexPilot: Benchmarking the Proactive Interaction Ability of Legal LLMs with Laypeople in Chinese Civil Case Consultation](https://arxiv.org/abs/2610.23141)

**<font color=#1a73e8>作者：</font>** Wenbin Zhang, ShangZhan Li, Bingxiang He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have greatly assisted legal professionals. However, our empirical studies reveal that, when faced with underspecified consultations from non-experts, current LLMs often produce irresponsible responses with limited utility despite lacking sufficient case details for definitive conclusions. To better assist laypeople, legal LLMs must identify focal points of dispute and proactively elicit crucial context from users. Unfortunately, existing data resources often focus on interaction and response quality, offering limited insight into how proactive interaction affects LLMs' downstream claim-level judgment prediction in actual civil cases. To address this gap, we introduce \textbf{LexPilot}, a benchmark linking proactive legal interaction to claim-level verdict prediction using authentic Chinese civil judgments. Constructed from 432 real-world judgments across 36 common causes of action, LexPilot comprises expert-reviewed pairs of complete and underspecified consultation histories with corresponding court verdicts. Experiments reveal that current LLMs struggle with proactive legal interactions in underspecified consultations, with downstream judgment prediction substantially underperforming that in the fully specified consultation setup (-23.84% on average). Further analysis identifies critical bottlenecks hindering these capabilities. Our work highlights the urgent need for more user-centered legal AI to better serve the public.

---


### 146. [From GAN-Based Models to GPT-5: A Taxonomy-Guided Study of Human Performance in Detecting Deepfake Face Images](https://arxiv.org/abs/2610.23144)

**<font color=#1a73e8>作者：</font>** Zhiqing Guo, Lixin Jia, Luning Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models for deepfakes have rapidly evolved from GAN-based architectures to diffusion models and multimodal large language models (MLLMs). However, empirical research on human performance in detecting deepfake face images has not kept pace. It remains unclear if (and how) detection performance varies across generative models and whether model-specific training improves detection more effectively than general-purpose training. In this paper, we propose the \emph{Deepfake Face Artifact Taxonomy} (DFAT), a cross-model taxonomy of human-recognizable visual artifacts in deepfake face images, based on which we build both general-purpose and model-specific training materials. Through an online experiment ($n = 524$), we examined human performance in detecting deepfake face images and evaluated training efficacy across five representative generative models: three GAN-based, one diffusion-based, and one MLLM (GPT-5). Our results show that participants' detection accuracy was strongly model-dependent and that images generated by more recent and advanced models were not necessarily harder to detect. After training, participants achieved significant performance gains across most conditions, and their improvement varied by model. Notably, model-specific training generally yielded greater numerical gains than general-purpose training. In a five-month follow-up test ($n = 342$), we observed no significant decline in detection accuracy and no significant increase in perceived stress. Overall, our findings provide actionable insights for designing effective, sustainable, and targeted training programs to counter the growing threat posed by deepfakes.

---


### 147. [Local proxies for memory-efficient training](https://arxiv.org/abs/2610.23145)

**<font color=#1a73e8>作者：</font>** Wu S. Zihan, Brian A. Yuan, Guillaume Bellec  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local learning algorithms can reshape resource requirements of artificial intelligence. The memory bottleneck of standard end-to-end backpropagation lies in the need to store all network activations until the loss gradient has been propagated back through. Local learning avoids this, but typically at a cost in accuracy. We study how to achieve accurate and memory efficient local learning in transformers. For each transformer block, we train a local proxy network to predict the global network output via distillation. Gradients can be independently propagated through this local proxy while estimating well the backpropagation gradients. In theory, this approach is exact for deep linear networks; in non-linear residual models, the gradient error can be bounded when using the appropriate residual proxy. We verify this numerically and demonstrate that optimizing the distillation loss improves gradient estimation. Evaluating the performance of proxy propagation on CIFAR-100 in vision transformers, we find that it achieves a better accuracy/memory trade-off compared to other local algorithms. Finally, we show that the method is further relevant for fine-tuning large language models on a small memory budget. Our method trains faster and achieves higher performance than memory-efficient zeroth-order learning algorithms with comparable memory cost.

---


### 148. [Grounded Credit Assignment in Reinforcement Learning for Multi-Turn Search Agents](https://arxiv.org/abs/2610.23148)

**<font color=#1a73e8>作者：</font>** Qirui Liu, Hao Chen, Yi Wen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outcome-reward reinforcement learning such as GRPO gives every token of a search-agent rollout the same advantage, although the rollout exercises two capabilities: finding evidence and using it. We show that accuracy improves without grounding: Search-R1 raises accuracy on all seven QA benchmarks, yet on Bamboogle the evidence-supported share of correct answers falls from 84.0% to 42.9%. We attribute this to GRPO's credit assignment: rollouts that retrieve answer-bearing evidence are favoured in aggregate only in proportion to their accuracy gain over the rest, a grounding gap that answering from memory or misusing evidence shrinks or reverses. To address this, we propose Grounded Credit Assignment (GCA), which uses verifiable sub-outcomes (evidence retrieval and answer correctness) to correct search and answer credit separately: a wrong answer is blamed more than the search that found the evidence, and a correct answer that bypasses retrievable evidence is credited less. Never negative on evidence-finding search, the correction does not shrink with the grounding gap; capped at 10% of each token's advantage, it never overrides the outcome signal. Without extra models, rollouts, or training stages, GCA improves average EM over Search-R1 by 5.7 (Qwen2.5-3B) and 6.3 points (Qwen3-30B-A3B) and raises this share from 76.9% to 93.4%.

---


### 149. [Cross-Centaur: Modeling Individual Decision-Making Across Psychological Tasks with Language Models](https://arxiv.org/abs/2610.23157)

**<font color=#1a73e8>作者：</font>** Hikaru Asano, Hidezo Suganuma, Ryutaro Mori 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as computational models of human behavior. Recent models such as Centaur have advanced this goal by fine-tuning LLMs on trial-by-trial decisions from psychological experiments. However, existing large-scale behavioral datasets do not link the same participants across different tasks, so these models learn population-level regularities but are not trained to model individual-level regularities across tasks. We introduce Cross-Psych-101, a dataset of 591 participants and 261{,}551 valid decisions across 12 Bandit, Tradeoff, Structure, and Social tasks. We train Cross-Centaur to predict a participant's target-task actions from a target-task description and the source-task description paired with the same participant's source-task behavior. Cross-Centaur outperforms off-the-shelf LLMs and Centaur on held-out participants, both within and across tasks. Probing analyses suggest that its hidden states encode participant-level behavioral tendencies that transfer across tasks. These results highlight the potential of cross-task individual-level data for predicting human decision-making with language models. Cross-Pysch-101 is available at this https URL.

---


### 150. [Explaining Chess and Go in Natural Language](https://arxiv.org/abs/2610.23166)

**<font color=#1a73e8>作者：</font>** Ori Press, Alexander Golubev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern chess engines play far beyond human ability, often choosing moves whose underlying ideas are difficult for humans to understand. We propose an automatic metric for evaluating chess explanations, grounded in chess-engine evaluations. Evaluating state-of-the-art language models using this metric, we find that they perform surprisingly poorly, often relying on surface-level board observations rather than robust, transferable chess concepts. We then introduce BinProp, a training-free method that enables these same models to discover reusable chess concepts and use them to explain moves in natural language. BinProp improves explainability for every model tested, nearly tripling the average score compared with direct prompting. Beyond chess, the same method discovers useful concepts in Go, draughts, and shogi without additional tuning.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-258](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
