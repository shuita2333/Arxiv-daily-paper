# 🧠 大模型相关研究 | 2026年06月12日

> 本类共 **128** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-128**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-128**

---

### 101. [A Controlled Study of Decoding-Time Truthfulness Methods on Instruction-Tuned LLMs](https://arxiv.org/abs/2606.12160)

**<font color=#1a73e8>作者：</font>** Ao Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce CHAIR (Classifier of Hallucination As ImproveR), a supervised framework for detecting hallucinations by analyzing internal logits from each layer of every token. Our method extracts a compact set of features such as maximum, minimum, mean, standard deviation, and slope-from the token logits across all layers, enabling effective hallucination detection without overfitting. Experiments on TruthfulQA and MMLU datasets demonstrate that CHAIR significantly improves detection accuracy, particularly in zero-shot scenarios, showcasing its robustness and generalizability. Beyond hallucination detection, CHAIR highlights the potential of using internal representations for designing advanced decoding strategies. By leveraging patterns in logits, we suggest that more sophisticated models and adaptive decoding methods could further reduce hallucinations and enhance text completion quality. CHAIR not only offers a practical solution for detecting hallucinations but also lays the groundwork for exploring richer representations in LLMs to improve their factuality and coherence.

---


### 102. [OpenMedReason: Scientific Reasoning Supervision for Medical Vision-Language Models](https://arxiv.org/abs/2606.12169)

**<font color=#1a73e8>作者：</font>** Negin Baghbanzadeh, Pritam Sarkar, Michael Colacci 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-stakes clinical use of large vision-language models (LVLMs) requires reasoning that is grounded in visual evidence and clinical knowledge, not just correct final answers. We introduce OpenMedReason, a large-scale, open multimodal medical reasoning corpus comprising approximately 450K image-question-answer instances whose reasoning traces are primarily derived from curated biomedical, human-authored scientific articles. OpenMedReason provides high-fidelity supervision beyond synthetic chains of thought, covering diverse medical domain vision modalities such as radiological scans, microscopic images, visible light photographs, charts, and others. We complement it with OpenMedReason-Bench, a held-out benchmark that allows fine-grained evaluation of LVLMs along three complementary axes of capability, including perception, medical knowledge, and rationale, enabling diagnostic evaluation beyond final-answer accuracy. OpenMedReason is a rich training resource that exhibits its effectiveness in both supervised fine-tuning (SFT) and reinforcement-based alignment. Training with OpenMedReason yields a 20% average improvement in VQA accuracy over the base model and achieves performance within 4.2% of the strongest comparable-scale medical LVLMs. Fine-grained performance analysis confirms that the gains are not concentrated in any single axis: OpenMedReason improves perception, medical knowledge, and rationale jointly, and its reasoning traces are preferred over those of the base model in 86.1% of pairwise comparisons. We release the code and dataset at this http URL.

---


### 103. [Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application](https://arxiv.org/abs/2606.12191)

**<font color=#1a73e8>作者：</font>** Jiachun Li, Zhuoran Jin, Tianyi Men 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Environments serve as interactive systems for large language model (LLM) based agents across diverse scenarios and play a crucial role in driving the continual evolution of model capabilities. Despite this importance, existing work lacks a systematic categorization and deep analysis. This paper systematically studies current researches on agentic environments from the perspective of the environment engineering lifecycle, covering their modeling, synthesis, evaluation and application. Specifically, the paper first introduces representative environments from the perspectives of eight attributes and eight domains, providing detailed analyses of their development paths and highlighting their core capabilities. Second, for automated environment synthesis, two paradigms are introduced, such as symbolic synthesis and neural synthesis. This paper also shows different environment evaluation methods in each paradigm. Thirdly, the corresponding environment applications from the perspective of agent-environment co-evolution are discussed. In specific, the paper characterizes the primary pathways for agent evolution in dynamic environments from four complementary perspectives: memory-centric experience evolution, orchestration-centric workflow evolution, trajectory-centric offline evolution, and exploration-centric online evolution. And three paradigms of environment evolution are identified, namely neural-driven, difficulty-driven, and scaling-driven approaches. At last, several promising future directions are discussed, including Environment-as-a-Service, Multi-agent Environments, and Neural-Symbolic Environments.

---


### 104. [InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning](https://arxiv.org/abs/2606.12195)

**<font color=#1a73e8>作者：</font>** Ziang Yan, Sheng Xia, Jiashuo Yu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in foundation models has shifted toward agentic behavior involving multi-step reasoning and tool use. However, open-source efforts largely focus on text-dominant settings, leaving long-horizon multimodal tasks underexplored. This gap is evident in video tasks requiring sustained temporal understanding and iterative interaction. We present InternVideo3, a framework enhancing these capabilities via Multimodal Contextual Reasoning (MCR). MCR treats understanding as a closed-loop process over a shared, evolving context containing observations, instructions, reasoning, tool actions, and memory. This frames long-video understanding as evidence accumulation and verification. To ensure efficiency, we introduce Multimodal Multi-head Latent Attention (M^2LA), a token-preserving reparameterization compressing KV-cache states while retaining the full token stream. Our staged training includes continued pretraining, short-to-long supervised fine-tuning, rule-based reinforcement learning, and on-policy distillation. Experiments show InternVideo3 achieves strong performance on benchmarks like Video-MME, MLVU, and EgoSchema. We further instantiate the model as a video agent with retrieval tools, demonstrating robust evidence-grounded behavior. Our results suggest that efficient context handling and closed-loop reasoning are vital for adapting open multimodal models toward long-horizon visually grounded agency.

---


### 105. [Adaptive Multi-Resolution Procedural Knowledge Compression for Large Language Models](https://arxiv.org/abs/2606.12203)

**<font color=#1a73e8>作者：</font>** Changyue Wang, Weihang Su, Qingyao Ai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used to tackle complex tasks with autonomous workflows. Recently, reusable natural language skills have emerged as a popular paradigm to inject procedural knowledge into LLM applications. Since popular skills are often invoked repeatedly, placing their full text in every context significantly increases prefill cost and latency. While text compression techniques have the potential to solve this problem, most existing methods are designed to compress factual knowledge in documents instead of procedural knowledge, making them insufficient for skill compression. In this paper, we argue that an effective skill compression method should: 1) preserve logical dependencies among workflows and tool protocols, 2) enable lightweight, offline compression for frequently updated community skills, and 3) be adaptable to varying complexities across skills. To address this, we present SKIM (SKIll coMpression), an adaptive multi-resolution soft token compression framework for procedural skills. Depending on the complexity of each skill, SKIM creates different numbers of soft tokens that not only improve the efficiency of LLM inference, but also preserve the effectiveness of skill usage. Experiments indicate that SKIM compresses skills to 30 to 60 percent of their original token length while preserving task performance better than existing compression this http URL have released our code at this https URL .

---


### 106. [Adapting Prithvi-EO for Fallow Detection for Food-Water Nexus: ViT-Adapter Necks and Parameter-Efficient Backbone tuning of Geospatial Foundation Model](https://arxiv.org/abs/2606.12218)

**<font color=#1a73e8>作者：</font>** Sk Muhammad Asif, Orhun Aydin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding spatial distribution of fallow land is important for optimizing the food-water (FW) nexus, given fallowing's role in crop rotation and water conservation. Fallow is a low accuracy class in USDA Cropland Data Layer (CDL). Geospatial foundation model (GFM), Prithvi-EO has shown strong transferability across computer vision tasks. However, its Vision Transformer (ViT) backbone produces features at a single spatial scale that are ill-suited for the multi-scale features required by object detection heads. Existing approaches synthesise multi-scale pyramids through scaling of single stride tokens, sacrificing spatial heterogeneity, and full backbone fine-tuning is computationally prohibitive for GFMs. We evaluate a fallow detection pipeline combining two parameter-efficient fine tuning (PEFT) schemes: Low-Rank Adaptation (LoRA) and a hybrid PEFT, with three neck designs: pseudo multi-scale, Lite ViT-Adapter, and Full ViT-Adapter. Our best configuration, Lite ViT-Adapter with a one-stage head, achieves a mAP@50 of 0.9479 with the Diou loss, suggesting the effectiveness of center-aware localization for irregular fallow field detection. ViT-Adapter free one-stage detection under LoRA improves the adapter-free anchor-based approach by 6.42%, and the best configuration improves baseline adapter-free anchor-based approach by 25.70%. These results demonstrate that lightweight spatial prior fusion and selective backbone unfreezing enable Prithvi-EO to capture local fallow patterns more effectively, outperforming approaches that rely on reshaped single-stride ViT tokens.

---


### 107. [Re-evaluating Confidence Remasking in Masked Diffusion Language Models](https://arxiv.org/abs/2606.12232)

**<font color=#1a73e8>作者：</font>** Stipe Frkovic, Metod Jazbec, Dan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (dLLMs) have recently emerged as a competitive alternative to autoregressive language models, with the promise of faster inference via parallel token generation. A notable limitation of the masked formulation, however, is that once a token has been unmasked it can no longer be revised, leaving dLLMs vulnerable to early sampling mistakes. To address this, a growing body of work has sought to extend masked dLLMs with self-correcting (remasking) capabilities. One appealing subset of these methods does so in a training-free, post-hoc manner based on token confidences, with encouraging early reported results. In this work, we revisit the empirical evaluation of a representative post-hoc remasking method, WINO [Hong et al., 2026], and find that under standard decoding settings (shorter block lengths) it brings little-to-no benefit over confidence-based unmasking alone [Wu et al., 2025]. Extending the evaluation to non-greedy decoding, we find that while confidence-based remasking can mitigate errors introduced by increased stochasticity to some extent, it also exacerbates the diversity collapse previously reported for confidence-based unmasking. Overall, our results show that the benefits of post-hoc confidence-based remasking are highly setting-dependent, underscoring the need for a more comprehensive evaluation framework.

---


### 108. [On The Effectiveness-Fluency Trade-Off In LLM Conditioning: A Systematic Study](https://arxiv.org/abs/2606.12234)

**<font color=#1a73e8>作者：</font>** Iuri Macocco, Pau Rodríguez, Arno Blaas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Controlling the output of Large Language Models (LLMs) is a central challenge for their reliable deployment, yet a clear understanding of the involved trade-offs remains elusive. Current approaches to conditioning are often evaluated with a narrow focus on their effectiveness at injecting or removing a target concept, neglecting generation quality. We systematically investigate a range of conditioning methods in both injection and removal scenarios. We find that efficient steering methods frequently achieve conditioning at a steep cost to fluency. Furthermore, we identify a critical yet previously overlooked interaction with the training paradigm: activation steering methods are far less effective on instruction-tuned models than on their base counterparts. Simple prompting and full-fledged supervised fine-tuning, on the other hand, are viable options for concept injection, but are not as good at concept removal. Finally, cheaply computed textual metrics highly correlate to costly LLM-as-judge scores, and provide insights on the behavior of conditioning methods.

---


### 109. [Multi-Rate Mixture of Experts for Accelerating Liquid Neural Network Training](https://arxiv.org/abs/2606.12240)

**<font color=#1a73e8>作者：</font>** Shilong Zong, Almuatazbellah Boker, Hoda Eldardiry  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time-series data often exhibit complex temporal dependencies, irregular sampling, and heterogeneous dynamics across multiple time scales, making accurate sequence modeling particularly challenging. Traditional recurrent neural networks (RNNs), such as Long Short-Term Memory (LSTM) networks, operate in discrete time and may struggle to effectively capture continuous and irregular temporal behaviors. Liquid Neural Networks (LNNs) address some of these limitations through continuous-time dynamics, but standard LNN architectures typically rely on a single dynamical system, limiting their ability to model heterogeneous temporal patterns. To address these challenges, we propose a Multi-Rate Mixture-of-Experts (MR-MoE) framework built on top of Liquid Neural Networks. In the proposed architecture, multiple LNN-based experts operate at distinct time scales, enabling the model to explicitly separate fast-changing dynamics from slow-evolving temporal trends. A gating network further enables adaptive expert specialization based on input conditions. In addition, we incorporate both feature-level and temporal attention mechanisms to improve robustness, interpretability, and long-range dependency modeling. Feature-level attention suppresses noisy or irrelevant variables, while temporal attention selectively focuses on informative historical states. We evaluate the proposed framework on a complex multivariate time-series prediction task and compare it against strong baselines, including LSTM, monolithic LNN, and standard MoE models. Experimental results demonstrate that the proposed MR-MoE framework consistently achieves improved AUROC and AUPRC performance while maintaining favorable computational efficiency. These results highlight the effectiveness of combining continuous-time dynamics, multi-scale expert decomposition, and adaptive attention mechanisms for time-series modeling.

---


### 110. [Reassessing High-Performing LLMs on Polish Medical Exams: True Competence or Bias-Driven Performance?](https://arxiv.org/abs/2606.12250)

**<font color=#1a73e8>作者：</font>** Antoni Lasik, Jakub Pokrywka, Łukasz Grzybowski 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) in medicine are mainly evaluated using multiple-choice question answering (MCQA), which can overestimate real clinical ability due to guessing strategies and answer biases. To address these limitations, we introduce an expanded and more challenging benchmark based on Polish medical exams, adding over 15,000 questions, two new domains, and four structural modifications that reduce MCQA-specific artifacts and better test reasoning. We evaluate 21 LLMs and show that evaluation design strongly affects results. Under our harder setup, the best model (Qwen3.5-122B) drops by 28.4 and 31 pp on English and Polish exams, respectively. Despite low evidence of data contamination, standard MCQA scores do not reliably reflect true medical competence. To facilitate further research, we make our benchmark publicly available.

---


### 111. [Beyond Fully Random Masking: Attention-Guided Denoising and Optimization for Diffusion Language Models](https://arxiv.org/abs/2606.12273)

**<font color=#1a73e8>作者：</font>** Jia Deng, Junyi Li, Wayne Xin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) offer an efficient alternative to autoregressive models through parallel decoding, yet existing post-training methods largely rely on random masking strategies that overlook intrinsic token dependencies. In this work, we present an empirical analysis of attention in dLLMs and show that tokens attending more strongly to unmasked context exhibit greater generation stability and play a critical role in reasoning. Motivated by these findings, we propose AGDO, an attention-guided denoising and optimization framework that aligns both training and optimization with attention-derived dependencies. AGDO determines the denoising order based on attention structure and emphasizes attention-critical tokens during supervised fine-tuning and reinforcement learning. Experiments on mathematical and coding benchmarks demonstrate that AGDO consistently improves reasoning performance, outperforming state-of-the-art post-training methods for dLLMs.

---


### 112. [Holding the FP8 Quality Ceiling at 8-Bit Weights and Activations: INT8 and GGUF Post-Training Quantization of Ideogram 4.0 for Consumer GPUs](https://arxiv.org/abs/2606.12280)

**<font color=#1a73e8>作者：</font>** Deep Gandhi, Ali Asaria, Tony Salomone  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization lets large text-to-image diffusion transformers run on consumer GPUs, yet the hardware-specific trade-offs are seldom measured directly. We quantize Ideogram 4.0 - a 9.3B flow-matching diffusion transformer (DiT), shipped as two separate-weight copies of a single-stream 34-layer backbone for classifier-free guidance and conditioned by a Qwen3-VL-8B encoder - for Ampere RTX 3090 GPUs, which lack FP8 tensor cores. Our INT8 W8A8 recipe (per-channel weights, per-token dynamic activations, SmoothQuant, and mixed-precision protection of a small high-fragility layer set) holds the FP8 quality ceiling: on a 200-prompt benchmark the paired same-seed bootstrap CI for INT8-FP8 includes zero on both Pick and CLIP, while INT8 improves on NF4 by $+1.9$ CLIP (95% CI $[+1.21,+2.64]$, excluding zero). A per-category OCR analysis, to our knowledge unreported for this model class, confirms text legibility is preserved, and an ablation isolates protection of the FFN down-projections as the dominant quality lever. Our GGUF Q4_K quantization beats NF4 at equal on-disk size and is the Pareto winner on the quality-memory frontier, with paired confidence intervals excluding zero (Q8_0 is quality neutral). Finally, we characterize where 8-bit quantization helps and where it does not: INT8's weights match FP8's footprint rather than shrink it, so a speed gain on Ampere awaits a fused INT8 kernel.

---


### 113. [Measuring Epistemic Resilience of LLMs Under Misleading Medical Context](https://arxiv.org/abs/2606.12291)

**<font color=#1a73e8>作者：</font>** Hongjian Zhou, Xinyu Zou, Jinge Wu 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) now reach expert-level scores on medical licensing exams, encouraging the assumption that high scores imply safe medical judgment while patients increasingly use them for health advice. We show this assumption is fragile: when misleading context is injected into questions that LLMs originally answer correctly, they abandon the correct answer. We call the ability to maintain correct judgment under adversarial context epistemic resilience, and introduce MedMisBench to measure it. MedMisBench contains 10,932 medical question items and 48,889 misleading context-option pairs spanning medical reasoning, agentic capability, and patient-journey evaluation. Across 11 model configurations, mean accuracy falls from 71.1% on original questions to 38.0% under focused misleading context, with 51.5% attack success. The most damaging injections are formal, rule-like fabrications: authority-framed falsehoods reach 69.5% attack success and exception-poisoning claims reach 64.1%. A 14-member clinical panel from 7 countries identified serious potential harm in 38.2% of reviewed cases. MedMisBench exposes a structural blind spot in LLM evaluation in medical settings: existing benchmarks measure what models know, but not whether they preserve correct medical judgment under misleading context.

---


### 114. [Bridging the Modality Gap in Forensic Image Retrieval](https://arxiv.org/abs/2606.12294)

**<font color=#1a73e8>作者：</font>** Ricardo González-Gazapo, Annette Morales-González, Yoanna Martínez-Díaz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated image retrieval plays an increasingly critical role in modern forensic analysis, supporting investigative workflows that rely on efficient comparison of visual evidence. While prior work has focused primarily on developing and optimizing multimodal retrieval systems, limited attention has been paid to evaluating the forensic applicability of these technologies across diverse real-world scenarios. In this study, we present a unified retrieval framework adapted to four key forensic tasks: (1) tattoo image retrieval given a tattoo query image; (2) tattoo retrieval guided by human-expert textual descriptions, modelling the common situation where a witness verbally describes a tattoo; (3) tattoo retrieval from hand-drawn sketches; and (4) face retrieval from forensic face sketches. Our system leverages a multimodal large language model (MLLM) to automatically generate structured textual descriptions for all queries and gallery images, followed by sentence-transformer embedding for text-based comparison. We evaluate retrieval using visual-only embeddings, text-only embeddings and a multimodal fusion strategy that combines text- and image-based similarity scores derived from state-of-the-art visual feature extractors relevant to each task. The fusion of modalities consistently improves retrieval precision and robustness, especially in scenarios where visual information is limited or noisy (e.g., sketches, partial tattoos, or fragmented witness statements). This work highlights the forensic value of a unified multimodal retrieval pipeline and demonstrates how modern MLLMs can operationalize challenging forensic tasks that traditionally rely on manual expert analysis. Our results position multimodal retrieval as a promising tool for supporting investigative workflows involving tattoos, facial composites, and witness descriptions.

---


### 115. [From 2D Grids to 1D Tokens: Reforming Shared Representations for Multimodal Image Fusion](https://arxiv.org/abs/2606.12303)

**<font color=#1a73e8>作者：</font>** Yuchen Xian, Yunqiu Xu, Yang He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal image fusion aims to integrate complementary information from different modalities into a fused image that preserves rich local details while maintaining globally consistent appearance. Existing approaches build shared representations on 2D feature grids, which excel at modeling local structures but offer limited leverage over image-level global appearance factors. To balance these objectives, we introduce a compact 1D token interface based on a frozen pretrained image tokenizer for modeling non-local appearance/base factors. Rather than using the tokenizer as a reconstruction backbone, our design uses the 1D token space as a global carrier while retaining the 2D spatial pathway for local structure restoration. Specifically, we introduce Selective Token Editing (STE), which sparsely updates/replaces a small set of critical tokens, providing a lightweight mechanism to steer global appearance coherence while keeping the fusion backbone unchanged and avoiding extra losses. Experiments on four commonly used benchmarks show that our method achieves the best overall performance, with consistent, multi-metric improvements in both global coherence and local fidelity. Project page: this https URL

---


### 116. [Slots, Transitions, Loops: Learning Composable World Models for ARC](https://arxiv.org/abs/2606.12316)

**<font color=#1a73e8>作者：</font>** Gege Gao, Bernhard Schölkopf, Andreas Geiger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> ARC tests in-context rule induction: given a few input-output demonstrations, a model must infer the hidden rule and apply it to a new query. While many approaches express ARC rules through language, code, or symbolic programs, ARC itself is visual-symbolic: rules appear as grid transitions over objects, colors, shapes, and spatial relations. We introduce Loop-OWM, an object-centric world-modeling architecture that learns these rules as composable transitions over structured states. It combines color-prototype slots, demonstration-conditioned task summaries, and a looped transition model with dense propagation and slot-conditioned correction. On both ARC-1 and ARC-2, Loop-OWM outperforms non-looped and looped baselines with comparable or fewer parameters. These results suggest that ARC rules can be learned not only as language descriptions or searched programs, but also as transitions over visual-symbolic world states.

---


### 117. [Harness In-Context Operator Learning with Chain of Operators](https://arxiv.org/abs/2606.12318)

**<font color=#1a73e8>作者：</font>** Minghui Yang, Ling Guo, Liu Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators approximate mappings between function spaces, but often generalize poorly to other operators and usually require fine-tuning or retraining. In-Context Operator Networks (ICON) addresses this issue by prompting the model with numerical context so that the model learns specific operators from prompts and adapt to different operators without fine-tuning. However, ICON may still fail to generalize to out-of-distribution (OOD) operator tasks. Inpired by the success of harness engineering of Large Language models (LLMs), we introduce Chain of Operators (CHOP), a framework that harness a frozen ICON to OOD operator tasks without updating its parameters. Specifically, CHOP constructs a chain of operators consisting of explicit elementary transformations and the frozen ICON. Experiments on a scalar conservation law and a mean-field control problem show that CHOP reduces relative inference error over direct ICON evaluation, while each operator in the chain remains interpretable and in closed form. A chain constructed on one PDE family further generalizes to a different family, indicating shared mechanisms across harness systems.

---


### 118. [ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing](https://arxiv.org/abs/2606.12342)

**<font color=#1a73e8>作者：</font>** Chirag Chawla, Pratinav Seth, Vinay Kumar Sankarapu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Domain fine-tuning degrades the safety of large language models: fine-tuned specialists readily comply with harmful prompts framed in domain language. Existing inference-time defenses that mix logits from a safe anchor model require both models to share a vocabulary, which rules them out for the cross-family specialists where safety is most degraded. We present ALIGNBEAM, a training-free method that lifts this restriction by translating anchor logits into the target model's vocabulary token-by-token at each decoding step; a small LLM judge then selects the safest among K candidate continuations. No weights are changed, and the safety-utility trade-off can be tuned at deployment without retraining. Across both cross-vocabulary and same-vocabulary evaluation pairs, ALIGNBEAM substantially raises refusal on adversarial benchmarks while keeping task accuracy and inference overhead within practical bounds. The results show that safety alignment can be transferred between model families at inference time, without touching either model's weights.

---


### 119. [Anatomy of Post-Training: Using Interpretability to Characterize Data and Shape the Learning Signal](https://arxiv.org/abs/2606.12360)

**<font color=#1a73e8>作者：</font>** Leon Bergen, Usha Bhalla, Sidharth Baskaran 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model post-training is the main stage at which model behavior is shaped, yet it still largely involves optimization of scalar rewards that summarize diverse desiderata. This abstraction gives practitioners little visibility into what their data actually teaches models, allowing spurious correlations to be learned by a model and inducing undesirable behaviors such as over-stylization and sycophancy. To address this problem, we ask: can we inspect a preference dataset before optimization and decide, at the level of concepts, which behaviors a model should be allowed to learn? Motivated by this, we introduce a data-centric post-training pipeline that uses interpretability protocols to develop statistical hypotheses for the latent concepts separating preferred from dispreferred generations, making them explicit for fine-grained user feedback. Building on this view, we unify several interpretability-based training protocols as ways of shaping rewards via feature or data interventions. Empirically, we show that our pipeline diagnoses undesirable signals in existing preference data, mitigates off-target learning, and can also help amplify or shape desired properties such as safeguards and model personality. More broadly, our results suggest that interpretability can turn post-training from optimizing opaque proxy rewards into a process of auditing and sculpting the learning signal itself.

---


### 120. [Latent World Recovery for Multimodal Learning with Missing Modalities](https://arxiv.org/abs/2606.12362)

**<font color=#1a73e8>作者：</font>** Hui Wang, Tianyu Ren, Joseph Butler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study multimodal learning under missing modalities, with particular motivation from bioscience applications in which heterogeneous modalities are often only partially available when decisions need to be made. We propose Latent World Recovery (LWR), a framework built on two key ideas: (i) modality-specific embeddings from different modalities are aligned in a shared latent space, and (ii) a unified representation is constructed by fusing only the embeddings of the modalities that are actually available at both training and inference time. Rather than imputing missing modalities or requiring a fixed modality set, LWR treats each modality as a partial perception of an underlying latent state and performs availability-aware representation learning directly from the observed modalities. This combination of neighbor-based latent alignment and availability-aware modality fusion enables robust multimodal prediction under partial observation, while avoiding error propagation from explicit reconstruction of missing modalities. We evaluate the proposed framework on real-world incomplete multi-omics benchmarks and demonstrate that it provides an effective approach to downstream tasks such as cancer phenotype classification and survival prediction.

---


### 121. [On Subquadratic Architectures: From Applications to Principles](https://arxiv.org/abs/2606.12364)

**<font color=#1a73e8>作者：</font>** Anamaria-Roberta Hartl, Levente Zólyomi, David Stap 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers dominate modern sequence modeling, but their quadratic attention incurs substantial computational cost. Subquadratic architectures offer a scalable alternative. However, it remains unclear which designs yield the most effective sequence models. We compare three leading approaches: xLSTM, Mamba-2, and Gated DeltaNet. We evaluate these models on tasks with complex dependencies: (1) code-model pre-training, (2) distillation of code models from large language models, and (3) pre-training of time-series foundation models. Across these settings, xLSTM delivers the strongest overall performance. To explain xLSTM's advantage, we present a unified formulation and analyze the underlying architectural mechanisms, focusing on state tracking and memory dynamics. Our results show that xLSTM enables more flexible and stable memory correction via its gating scheme. We corroborate these findings on controlled synthetic length-generalization tasks. Overall, our findings indicate that xLSTM's gains on complex tasks stem from robust state tracking and accumulation.

---


### 122. [Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling](https://arxiv.org/abs/2606.12370)

**<font color=#1a73e8>作者：</font>** Yucheng Li, Huiqiang Jiang, Yang Xu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a key component in modern large language models, yet the rollout stage remains the key bottleneck in RL training pipelines. Although Multi-Token Prediction (MTP) offers a natural solution to accelerate rollouts through speculative decoding, many studies have observed that MTP acceptance rates degrade significantly during RL training, leading to limited speedup performance. To address this bottleneck, we present Bebop, a systematic study of MTP in LLM post-training, and offer practical recipes to integrate MTP into large-scale RL pipelines. First, we reveal that the MTP acceptance rate is fundamentally bounded by the fluctuation of model entropy, which demonstrates a clear negative linear relationship with the rise of entropy in the RL stage. Second, we show that probabilistic rejection sampling largely alleviates the disturbance introduced by entropy in RL compared to greedy draft sampling. We further identify that the conventional MTP training objectives (cross-entropy or KL) are suboptimal in such settings, and therefore we propose a novel end-to-end TV loss that directly optimizes multi-step rejection sampling acceptance rate, yielding ~10% acceptance rate improvements, achieving up to 95% acceptance rates and up to 25% extra inference throughput gains across mathematical reasoning, code generation, and agentic tasks. Third, we test various online MTP training strategies during RL and show that pre-RL MTP training with e2e TV loss and rejection sampling achieves a consistent acceptance rate and speedup throughout the entire RL, eliminating the need for costly online MTP updating. We provide extensive experiments and analysis that validate our findings. Experimental results show our method achieves up to 1.8x end-to-end acceleration in async RL training of Qwen3.5, Qwen3.6, and Qwen3.7 models.

---


### 123. [Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization](https://arxiv.org/abs/2606.12373)

**<font color=#1a73e8>作者：</font>** Hao Xiang, Qiaoyu Tang, Le Yu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) with verifiable environments has emerged as a powerful approach for enhancing the reasoning capabilities of Large Language Models (LLMs). While prior research demonstrates that scaling environment quantity improves RL performance, existing manual or individual construction methods suffer from linear scaling limits, thereby hindering scalable reasoning generalization. This paper introduces RACES (\textbf{R}ecursive \textbf{A}utomated \textbf{C}omposition for \textbf{E}nvironment \textbf{S}caling), a framework that conceptualizes verifiable environments as composable building blocks that can be recursively assembled. The key insight is that when the codomain (output type) of one environment matches the domain (input type) of another, they can be automatically fused into a new verifiable environment, enabling recursive composition. RACES is implemented with 300 individual environments and defines a set of composition operators (\textsc{SEQUENTIAL}, \textsc{PARALLEL}, \textsc{SORT}, and \textsc{SELECT}) that induce diverse reasoning patterns. Extensive experiments show that RL training on these composite environments consistently enhances reasoning generalization. Specifically, RACES improves DeepSeek-R1-Distill-Qwen-14B by an average of 3.1 points (from 48.2 to 51.3) and boosts Qwen3-14B performance from 58.8 to 61.1 on six benchmarks, which are unseen during the construction of training environments. Moreover, RACES achieves performance comparable to training on 300 individual environments using only 50 base environments, demonstrating significant efficiency in environment utilization.

---


### 124. [APPO: Agentic Procedural Policy Optimization](https://arxiv.org/abs/2606.12384)

**<font color=#1a73e8>作者：</font>** Xucong Wang, Ziyu Ma, Yong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in agentic Reinforcement Learning (RL) have substantially improved the multi-turn tool-use capabilities of large language model agents. However, most existing methods assign credit over coarse heuristic units, such as tool-call boundaries or fixed workflows, making it difficult to identify which intermediate decisions influence downstream outcomes. In this work, we study agentic RL from two perspectives: \textit{where to branch and how to assign credit after branching}. Our pilot analysis shows that influential decision points are broadly distributed throughout the generated sequence rather than concentrated at tool calls, while token entropy alone does not reliably reflect their impact on final outcomes. Motivated by these observations, we propose \textbf{Agentic Procedural Policy Optimization (APPO)}, which shifts branching and credit assignment from coarse interaction units to fine-grained decision points in the sequence. APPO selects branching locations using a Branching Score that combines token uncertainty with policy-induced likelihood gains of subsequent continuations, enabling more targeted exploration while filtering out spurious high-entropy positions. It further introduces procedure-level advantage scaling to better distribute credit across branched rollouts. Experiments on 13 benchmarks show that APPO consistently improves strong agentic RL baselines by nearly 4 points, while keeping efficient tool-calls and maintaining behavior interpretability.

---


### 125. [Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs](https://arxiv.org/abs/2606.12385)

**<font color=#1a73e8>作者：</font>** Sanjay Adhikesaven, Haoxiang Sun, Sewon Min  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern LLM training pipelines increasingly rely on other models to generate data, filter corpora, judge outputs, and guide development decisions. These dependencies are recursive: a model may depend on an upstream artifact whose own dependencies are documented only in separate releases and artifacts. As a result, the full dependency structure is fragmented across heterogeneous public artifacts, with complexity and recursive depth far outpacing humans' ability to trace. We introduce ModSleuth, an agentic system that recursively reconstructs LLM dependency graphs from public artifacts with source-grounded evidence. We find that the primary challenge is no longer information extraction, but defining what constitutes a dependency and reconciling artifact references across inconsistent documentation. We address these challenges through a formalization that distinguishes direct and indirect dependencies, represents heterogeneous pipeline roles through operation-centered relationships, and resolves artifact identities across names, versions, and repositories. Applying ModSleuth to four public-artifact-rich LLM releases, we recover 1,060 source-verified dependencies and construct large-scale dependency graphs of modern LLM development. These graphs reveal multi-hop license obligations, train-evaluation coupling, discrepancies between released and training-time artifacts, and documentation inconsistencies that would otherwise be difficult to uncover. We release ModSleuth and the resulting dependency graphs to support transparent analysis of the increasingly complex ecosystems underlying modern LLMs.

---


### 126. [System Report for CCL25-Eval Task 5: New Dataset and LoRA-Fine-Tuned Qwen2.5](https://arxiv.org/abs/2606.12392)

**<font color=#1a73e8>作者：</font>** Haotao Xie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recently, large language models (LLMs) have achieved promising progress in the fields of classical Chinese translation and the generation of classical poetry. However, domain-specific research on precise translation and affective-semantic understanding of classical poetry remains limited. The main challenge is that most studies treat the poetic appreciation task as a general-domain problem, neglecting the distinctive features of poetic appreciation, while high-quality and domain-specific datasets are extremely limited. To address this limitation, we decompose the task into three subtasks: term interpretation, semantic interpretation, and emotional inference. Based on multiple open-source datasets, we perform data cleansing and alignment to construct the Classical Chinese Poetry Instruction Pair Dataset (CCPoetry-49K), which comprises 49,404 high-quality instruction-response pairs explicitly optimized for this domain. We then propose a domain-specialized LLM, called PoetryQwen, by applying Low-Rank Adaptation (LoRA) to fine-tune the Qwen2.5-14B model. Experimental results on the CCL25-Eval Task 5 benchmark demonstrate that PoetryQwen achieves a score of 0.757, representing a 9.7% improvement over the Qwen2.5-14B-Instruct baseline (0.690). These findings clearly indicate that PoetryQwen significantly enhances performance in precise translation and emotional understanding of classical poetry. We present new dataset and methodological considerations intended to support the domain-specific optimization of LLMs.

---


### 127. [How Seemingly Inconsequential Design Choices Dictate Performance of LLMs in Pathology](https://arxiv.org/abs/2606.12407)

**<font color=#1a73e8>作者：</font>** Kian R. Weihrauch, Thomas A. Buckley, William Lotter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General-purpose large language models (LLMs) are routinely used as baselines when evaluating specialized pathology models on whole-slide images (WSIs). Because WSIs exceed contemporary model context limits, LLM baselines routinely use small, high-magnification patches processed independently via majority voting, without systematic evaluation of seemingly inconsequential design choices such as patch size, patch count, and magnification. Generalist LLMs have consistently underperformed specialized systems, reinforcing the perception that domain-specific training or architectural adaptation is necessary for pathology tasks involving WSIs. Here, we conduct a systematic factorial analysis of four input design factors: inference mode, patch size, magnification, and patch count. We demonstrate that prior studies have overstated the gap between specialized models and general-purpose LLMs by choosing non-optimized input configurations. On the MultiPathQA benchmark, switching to a single balanced configuration (large patches at lower magnification, processed jointly) raises GPT-5 from 15.1% to 39.5% on cancer-type classification (TCGA) and from 38.1% to 62.9% on organ classification (GTEx). Per-task optimization yields further gains up to 43.9% (TCGA) and 71.6% (GTEx). The same configuration generalizes to two other models and to a fully held-out CPTAC cohort, where it improves Gemini 3 Flash by 23.4 percentage points without any task-specific tuning.

---


### 128. [Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models](https://arxiv.org/abs/2606.12412)

**<font color=#1a73e8>作者：</font>** Cheng-Yu Yang, Shao-Yuan Lo, Yu-Lun Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) project images into hundreds to thousands of visual tokens, making decoder inference expensive in both attention computation and KV-cache memory. Existing visual-token reduction methods largely follow a rank-and-remove paradigm: they score visual tokens, keep a compact subset, and permanently discard the rest. We show that this irreversible action is fragile because visual-token importance changes across decoder depth; tokens ranked low at one stage may become relevant in later layers, especially for grounding-sensitive queries. We propose Reroute, a training-free plug-in that replaces removal with recoverable routing. At each routing stage, selected vision tokens pass through decoder blocks, while deferred tokens bypass the stage and re-enter the candidate pool at the next routing decision. Reroute reuses existing attention-score ranking rules and stage-wise schedules, preserving the theoretical TFLOPs and KV-cache budget class of the pruning method it augments. Across FastV, PDrop, and Nüwa variants on LLaVA-1.5 and Qwen backbones, reroute improves grounding under aggressive token reduction while maintaining general VQA performance. These results suggest that VLM token reduction should not be viewed only as irreversible pruning, but also as recoverable routing. The code can be found here: this https URL

---


> [!TIP]
> 当前位于：**101-128**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-128**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
