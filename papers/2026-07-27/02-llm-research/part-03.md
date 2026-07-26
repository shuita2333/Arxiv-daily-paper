# 🧠 大模型相关研究 | 2026年07月27日

> 本类共 **153** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-153](./part-04.md)

---

### 101. [ProCap: Prominence-guided Object Rectification for Faithful and Comprehensive Video Captioning](https://arxiv.org/abs/2607.21022)

**<font color=#1a73e8>作者：</font>** Debjyoti Das Adhikary, Aritra Hazra, Partha Pratim Chakrabarti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Improving video captioning quality typically demands retraining large vision-language models, an expensive and often impractical requirement. Existing training-free alternatives instead ground captions in detected objects to curb hallucination, but apply only a single, fixed correction pass without prioritizing which objects matter most, leaving semantically significant content omitted. We propose a prominence-aware, iterative post-hoc rectification framework that overcomes both limitations without modifying the underlying captioning model's parameters: a lightweight scoring mechanism ranks detected objects by spatial saliency, temporal persistence, and relational dynamics, and an iterative, prompt-driven refinement loop uses this ranking to progressively inject missing yet contextually relevant objects into the caption over multiple rounds. We validate the framework on MSVD and MSR-VTT using object-grounded automatic metrics, a 110-participant human study, and qualitative comparison against ChatGPT and Gemini; in human evaluation, the framework raises perceived completeness by up to 48% and reduces hallucination by up to 45% relative to a strong pretrained captioning baseline, all without retraining or reference captions. These results position prominence-guided iterative rectification as a lightweight, scalable, and model-agnostic route to more complete and trustworthy video captioning, with direct relevance to accessibility, retrieval, and other multimedia understanding applications.

---


### 102. [GeoThreat: Transferable Targeted Adversarial Attacks on Large Vision-Language Models for Remote Sensing Image Interpretation](https://arxiv.org/abs/2607.21036)

**<font color=#1a73e8>作者：</font>** Yimin Fu, Yuefeng Bai, Baicheng Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks against large vision-language models (LVLMs) serve as an effective means of assessing their robustness in cross-modal semantic understanding. Existing studies mainly focus on corrupting visual inputs to induce predefined erroneous responses in general vision-language tasks, whereas corresponding investigations in remote sensing fields remain largely underexplored. Compared with natural image understanding, remote sensing image interpretation requires joint reasoning over local discriminative cues and global scene context. This poses additional challenges to achieving transferable semantic manipulation toward specified responses under black-box settings. To tackle these challenges, we propose GeoThreat, a transferable targeted adversarial attack method against LVLMs for remote sensing image interpretation. Specifically, GeoThreat modulates adversarial representations in accordance with the target content at both conceptual and perceptual levels. The class tokens from surrogate image encoders are employed as conceptual representations, while perceptual representations are distilled from patch tokens of the adversarial example through collaborative importance estimation. Beyond merely rolling out attention scores across layers, we incorporate adversarial-target similarity gradients to more faithfully characterize the relevance of local visual cues to the intended semantic manipulation. The perceptual representations are then dynamically aligned with target patch tokens in a cross-attentive manner, facilitating the adaptation of local cues toward designated semantic details. Finally, adversarial perturbations are iteratively updated via ensemble-based joint optimization of conceptual calibration and perceptual adaptation. Extensive experiments across diverse LVLMs demonstrate the superiority of GeoThreat in both transferability and controllability.

---


### 103. [MVEI & EmObserver: Empowering MLLM-Oriented Visual Emotional Intelligence via Emotion Statement Judgement](https://arxiv.org/abs/2607.21061)

**<font color=#1a73e8>作者：</font>** Daiqing Wu, Dongbao Yang, Jiashu Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Affective Image Content Analysis (AICA) aims to recognize and understand emotions elicited by visual content, representing an indispensable step toward Artificial General Intelligence (AGI). However, despite the rapid progress of Multimodal Large Language Models (MLLMs), systematic evaluation of their visual emotional intelligence remains largely absent from recent model releases. We attribute this gap to a structural mismatch between conventional AICA paradigms and the open-ended, instruction-driven nature of MLLMs, where further analysis reveals four major limitations: omission of plausible responses, limited emotion taxonomies, neglect of contextual factors, and labor-intensive annotation. To overcome these barriers, we introduce Emotion Statement Judgement (ESJ), a statement-verification formulation that preserves the expressiveness of the input space while constraining outputs to discriminative judgements. We further develop INSETS, a labor-efficient pipeline that instantiates ESJ at scale by constructing INSETS-462k and supporting MVEI, a rigorously refined benchmark spanning sentiment polarity, emotion interpretation, scene context, and perception subjectivity. Beyond evaluation, we build EmObserver, an emotion-oriented MLLM optimized on ESJ through an elaborate multi-stage recipe. Extensive evaluation of broad-spectrum MLLMs on MVEI reveals fine-grained insights into current artificial visual emotional intelligence, while experiments on multiple AICA benchmarks demonstrate the accuracy, generalization, and reasoning faithfulness of EmObserver. Collectively, these results establish ESJ as a practical formulation, MVEI as a comprehensive benchmark, and EmObserver as an advanced baseline for advancing MLLM-oriented visual emotional intelligence. Code will be released at: this https URL.

---


### 104. [QuantiBias: Benchmarking Quantization-Induced Bias in LLMs](https://arxiv.org/abs/2607.21063)

**<font color=#1a73e8>作者：</font>** Emilio Ferrara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Almost every large language model that reaches a broad audience is quantized: trained in full precision, then compressed for efficiency. This step is assumed harmless and its safety is rarely re-checked. We find its principal side effect is increased bias that standard safety evaluation misses. Holding the model, its training, and the prompts fixed, a quantized model still refuses harmful requests, still avoids over-refusing benign prompts, and still selects the unbiased multiple-choice answer. Yet asked an open-ended question, the same model volunteers stereotypes in all eight languages we probe, in roughly one in four open-ended answers under an independent judge (~24% to ~27% across the compression ladder): it passes every standard check and still reaches users measurably more biased. The selective gap is a robust finding; whether open-ended bias further increases with compression is less certain, sensitive to the judge that scores it. We address both with \textbf{QuantiBias}, a benchmark that pairs a generative, multilingual stereotype probe with the refusal and multiple-choice controls that isolate open-ended generation, contrasts each build with and without reasoning, and rates the content severity of what it generates. Across two backbone models (Qwen and Gemma), a five-family screen, and eight benchmarks, quantizers allocate their extra precision by capability data that carries no bias-prevention signal, and reasoning before answering roughly halves the effect on some families while doing nothing on others. A quantized build must be re-evaluated for open-ended bias, not only on the short-form safeguards it already passes.

---


### 105. [Do Pathology Vision-Language Models Truly See Pathology?](https://arxiv.org/abs/2607.21065)

**<font color=#1a73e8>作者：</font>** Chengyang Zhang, Wenchuan Zhang, Bo Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology vision-language models (VLMs) have recently progressed rapidly and are commonly evaluated by answer accuracy on pathology VQA benchmarks. However, we dig into current evaluations and identify three overlooked issues: 1) Visual evidence is not always necessary. For instance, Gemini-3-Pro achieves 53.5% average accuracy across 5 VQA benchmarks without any visual input. 2) Domain training can improve accuracy without proportional gains in visual binding. Compared with Qwen2.5-VL-7B, Patho-R1-7B exhibits a 5.8-point lower multimodal gain and a 3.7-point lower attention IoU. 3) Entity-level attention is diffuse and weakly query-specific. On PathVG, attention maps remain highly correlated across different entity queries. These issues can lead to substantial misjudgments of pathology VLMs' actual multimodal capabilities. To this end, we present PathBind, a benchmark comprising 2,600 samples: PathBind-VQA with 1,500 questions across six dimensions, PathBind-PTA with 600 questions from a private pathology teaching atlas, and PathBind-Grounding with 500 expert-curated region-level samples. Each component undergoes task-specific automated filtering and expert review to reduce textual shortcuts and improve entity-region correspondence. We evaluate 18 representative VLMs on VQA samples of PathBind and five existing pathology VQA benchmarks, and further evaluate 10 VLMs on PathBind-Grounding and PathVG. Results show that current pathology VLMs still exhibit a substantial gap between answer-side performance and visual-semantic binding.

---


### 106. [PrefReward: Learning User Preference Matrix for Personalized Text Generation](https://arxiv.org/abs/2607.21067)

**<font color=#1a73e8>作者：</font>** Yue Wu, Chengbing Wang, Yimeng Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable ability in generating personalized content by leveraging user histories and contextual cues. However, most existing personalization approaches rely on implicit representations within model parameters, making it difficult to interpret user-specific preferences or effectively handle long-context dependencies. To address these challenges, we propose PrefReward, a novel preference-aware generative framework that explicitly models user styles through a structured preference matrix and integrates it into the decoding process as a reward signal. PrefReward consists of two stages: (1) extracting a user-specific preference matrix that summarizes individual stylistic tendencies, and (2) using the matrix to guide generation via a KL-divergence-based reward function. Experiments on the LongLaMP dataset show that PrefReward outperforms non-personalized and retrieval-based baselines in both generation quality and personalization interpretability.

---


### 107. [Show, Don't Tell: Evaluating Spatial Cognition in Generative Pixels Rather Than LLM Text](https://arxiv.org/abs/2607.21072)

**<font color=#1a73e8>作者：</font>** Xu Wang, Kaixiang Yao, Miao Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence is essential for agents to move from static semantic understanding toward interacting with the physical world. Many spatial tasks are grounded in continuous visual scenes, where locations, regions, and paths are more naturally expressed by pointing, marking, or drawing than by reporting precise coordinates or discrete textual symbols. Yet existing spatial reasoning benchmarks usually require coordinates, options, or text, creating an answer-interface mismatch for image-generation models. This makes it difficult to evaluate image-generation models under the same task semantics as text-output VLMs, despite their ability to externalize spatial judgments directly in pixel space. We propose ProVisE (Protocolized Visual Evaluation), a benchmark-agnostic framework that elicits protocol-constrained visual answers from image-generation models and parses them into structured predictions compatible with original metrics. ProVisE also includes an Agentic builder that constructs and validates task-specific protocols for new benchmarks. We further introduce SpatialGen-Bench, a curated diagnostic benchmark of 470 samples across 14 spatial subtasks, four capability levels, and diverse answer forms. We evaluate representative text-output VLMs and image-generation models in a unified setting and validate Agentic protocol construction on six external spatial benchmarks. Results show that image-generation models are competitive when spatial answers can be externalized directly in pixel space, while text-output VLMs retain a clear advantage in compositional spatial reasoning. These findings reveal complementary strengths of pixel-space expression and text-based reasoning and establish a metric-compatible testbed for studying spatial cognition in image-generation models.

---


### 108. [C-PTQ: Fisher-weighted Channel-wise Sensitivity for Post-training Quantization of MLLMs](https://arxiv.org/abs/2607.21076)

**<font color=#1a73e8>作者：</font>** Jiameng Li, Han Zhou, Matthew B. Blaschko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) require huge memory and computational costs, which limits their practical deployment. Post-training quantization (PTQ) techniques offer an efficient solution for model compression and inference acceleration. Yet, the quantized model faces performance degradation due to outlier channels, which are highly sensitive to quantization and substantially impair activation fidelity and task accuracy. To protect these salient channels during quantization, existing PTQ methods leverage modality- or token-level metrics to guide channel-wise scaling (CWS) of LLM decoders. However, these orthogonal measurements fail to capture channel-wise impacts on task-specific loss, and the misalignment between importance and scaling factors ultimately leads to suboptimal performance. To address this issue, we propose C-PTQ, a unified channel-wise PTQ method that harmonizes task-specific loss perturbation and quantization error. Motivated by second-order derivatives, we design a Fisher-weighted objective as a tractable Hessian approximation, seamlessly injecting task sensitivity into the scaling process. Notably, we achieve state-of-the-art performance without auxiliary modules like LoRA, thereby maintaining high efficiency. Experiments on Qwen2.5VL, InternVL2 and LLaVA-OV across 8 benchmarks demonstrate our effectiveness in both weight-only and weight-activation settings.

---


### 109. [Nipping the Butterfly Effect in the Bud: Self-Output Fine-Tuning for Autoregressive Weather Prediction](https://arxiv.org/abs/2607.21080)

**<font color=#1a73e8>作者：</font>** Yun-Ye Cai, Hsuan-Tien Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon weather forecasting is a fundamental challenge in atmospheric science, for which autoregressive Deep Learning Weather Prediction (DLWP) has emerged as the primary paradigm. Although the autoregressive pipeline is highly scalable and flexible, its prediction errors grow rapidly over long forecasting horizons. In this work, we study this error growth phenomenon from both theoretical and empirical perspectives. Our analysis reveals that the growth is driven by a feedback loop between output errors and input distribution shifts. Specifically, the autoregressive process amplifies small initial output errors, which progressively corrupt subsequent input distributions, echoing the butterfly effect in atmospheric science and ultimately deteriorating forecasting accuracy over longer horizons. Furthermore, we show that this distributional shift originates at the earliest stage of inference, with out-of-distribution signatures detectable as early as the first autoregressive step. To mitigate this issue, we propose \textbf{Self-Output Fine-Tuning (SOFT)}, a plug-and-play strategy that leverages the model's own one-step predictions to calibrate the biased input distribution encountered at the first step. Extensive experiments demonstrate that, despite its simplicity, SOFT achieves state-of-the-art performance on long-horizon forecasting tasks and substantially reduces both prediction errors and distributional discrepancy. The success of SOFT highlights the importance of reexamining the fundamental pipeline of deep learning weather prediction, representing a critical pipeline advance for atmospheric science.

---


### 110. [Geo3R: Mitigating Spatial Reasoning Hallucination in Multimodal Large Language Models](https://arxiv.org/abs/2607.21085)

**<font color=#1a73e8>作者：</font>** Mingyu Wang, Weilin Jin, Wenbo Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite remarkable progress in visual understanding, Multimodal Large Language Models (MLLMs) remain prone to hallucinations when reasoning about spatial relationships, often producing judgments that contradict the true 3D structure of the scene. Though several existing works have proposed to mitigate hallucinations, our analysis indicates that they show limited effectiveness in spatial reasoning, as they fail to bridge the fundamental gap between 2D visual representations and 3D spatial reality. Based on this finding, we define hallucinations arising from insufficient spatial structure modeling as spatial reasoning hallucination, a subcategory of relation hallucination that existing mitigation methods fail to address. We further identify three typical scenarios where such hallucinations frequently occur: perspective effects, object orientation, and viewpoint changes. To this end, we propose Geo3R, a training-free, plug-and-play framework that incorporates geometric evidence and structured 3D reasoning to mitigate spatial reasoning hallucination. Experiments on three benchmarks, covering 18 tasks across all three scenarios, show that Geo3R substantially reduces spatial reasoning hallucination across diverse MLLMs without additional training, outperforming existing models and methods.

---


### 111. [Training Large Language Models for Self-Explanation Faithfulness](https://arxiv.org/abs/2607.21090)

**<font color=#1a73e8>作者：</font>** Yeoktatt Cheah, María Pérez-Ortiz, Noah Y. Siegel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a Reinforcement Learning (RL) method to directly optimize the faithfulness of self-explanations - the extent to which a model's generated reasoning accurately reflects its internal decision-making process. While existing work focuses on evaluating faithfulness or using inference-time prompting frameworks to improve an LLM's self-explanation's tractability, these approaches do not provide a mechanism to directly optimize a model's parameters to generate faithful self-explanations. We bridge this gap by modifying existing faithfulness metrics into an RL training objective. We investigate (1) if models can be trained to accurately detect factors that affect their decisions, and (2) whether RL can directly optimize for the disclosure of these factors thereby improving LLM self-explanations' faithfulness. We experiment with two intervention types: random-word insertions and user-bias insertions, using a per-sample reward derived from the Phi-CCT correlation metric. RL fine-tuned Llama3.1-8B and Qwen3-8B show substantial improvements on the Phi-CCT faithfulness metric, with in-distribution scores rising from near-zero to as high as 0.664, and out-of-distribution scores reaching up to 0.691 on held-out tasks such as StrategyQA. Cross-intervention generalization is weaker but more interesting: a priori we would not expect a model trained only on random word insertions to generalize to user-bias phrases, yet Llama3.1-8B shows non-zero transfer in this direction. The reverse direction and Qwen3-8B do not replicate this, indicating model-dependent and setup-dependent effects we cannot yet explain. Lastly we analyze model behavior to rule out reward gaming behaviors that often plague RL training. Ultimately, we show that models can be trained to implicitly identify influential factors and disclose them, offering a scalable path toward reducing unfaithful reasoning in LLMs.

---


### 112. [HalluScope: Fine-grained Hallucination Diagnosis for Multimodal Large Language Models](https://arxiv.org/abs/2607.21105)

**<font color=#1a73e8>作者：</font>** Weilin Jin, Mingyu Wang, Wenbo Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although Multimodal Large Language Models have achieved strong performance across a wide range of vision-language tasks, they still suffer from hallucinations, where model outputs become inconsistent with the visual content, textual context, or commonsense knowledge. Existing studies primarily address this problem through coarse-grained detection. However, these approaches often provide insufficient diagnostic information for understanding hallucination types and supporting downstream hallucination mitigation. To bridge this gap, we propose fine-grained hallucination diagnosis for MLLMs, a new unified task that jointly performs hallucination detection, classification, and interpretable explanation generation. We develop an automated data generation pipeline and construct HalluScope-30K, a large-scale diagnostic dataset covering eight sources and five task categories. Based on this dataset, we design a multi-granular joint reward function and train two diagnosis models, HalluScope-4B and HalluScope-8B, which achieve state-of-the-art performance on both the MHALO benchmark and our fine-grained hallucination classification benchmark. Notably, detection and classification are mutually beneficial under joint optimization. Furthermore, diagnosis-driven feedback experiments show that the fine-grained diagnostic explanations produced by our model effectively guide target models to correct their hallucinations, with full diagnosis substantially outperforming all baselines on both Qwen3-VL-8B-Instruct and LLaVA-1.5-7B.

---


### 113. [One More Turn, Less Regret: A Regret-Based Multi-Turn Benchmark for LLMs' Clarification Policies](https://arxiv.org/abs/2607.21143)

**<font color=#1a73e8>作者：</font>** Minh Ngoc Ta, My Anh Tran Nguyen, Duong D. Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambiguous user requests make clarification a sequential decision problem for conversational LLM assistants: they must decide whether to ask, what to ask, when to stop, and when to answer. We introduce RegretBench, a multi-turn benchmark that evaluates clarification as policy behavior rather than isolated question quality. RegretBench provides a hidden-intent formulation of ambiguity, supports free-form interaction grounded in semantic-state tracking, and introduces a regret-based objective that measures how much value a model loses relative to a reference clarification policy. Experiments on open-domain QA and product recommendation scenarios show that final success alone is insufficient, as models with similar accuracy can differ substantially in efficiency, robustness to user behaviors, and stopping decisions. By jointly measuring intent resolution, interaction cost, ineffective clarification, and regret, RegretBench reveals whether models clarify usefully and efficiently. Our results show that effective clarification requires more than plausible questions: models must ask the right question at the right time and stop once the user's intended meaning is clear.

---


### 114. [V-DEAL: Diagnosing Video Safety De-Calibration as an Understanding-Refusal Coupling Failure](https://arxiv.org/abs/2607.21151)

**<font color=#1a73e8>作者：</font>** Zhetong Zhang, Honghao Fu, Miao Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Video Large Language Models are increasingly deployed in real-world applications, ensuring their safety alignment has become critical. Counterintuitively, we find that harmful videos paired with benign queries achieve higher attack success rates than the same videos paired with explicitly harmful queries. To understand the underlying mechanism of this vulnerability, we present V-DEAL, a three-level diagnostic framework that jointly analyzes this failure across model behaviour, understanding, and internal representations. By progressively ruling out perception failure and quantifying the model's internal refusal tendency, V-DEAL provides a new diagnostic perspective for analyzing the underlying mechanism of the observed vulnerability. We tested six Video LLMs on three public benchmarks and observed that models correctly recognize harmful video content with over 81\% accuracy, yet the average attack success rate still reaches 48.33\% under the condition pairing harmful videos with benign queries. Hidden-state analysis further shows that visual understanding activates a weaker refusal tendency than textual understanding. Furthermore, we introduce a prompt injection intervention method that reduces attack success rates by an average of 48.24 percentage points and achieves performance comparable to prior fine-tuning-based methods, providing an effective and practical means to address such safety risks in Video LLMs.

---


### 115. [CRAG-MM-Diagnostics: Enabling Stage-Wise Analysis of Knowledge-Intensive VQA](https://arxiv.org/abs/2607.21155)

**<font color=#1a73e8>作者：</font>** Hanseok Oh, Parishad BehnamGhader, Benno Krojer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge-Intensive Visual Question Answering (KI-VQA) benchmarks evaluate Vision-Language Models (VLMs) as multimodal knowledge assistants by requiring external information beyond a provided image to answer questions. KI-VQA involves multiple sub-problems -referring expression understanding, visual grounding, object recognition, knowledge retrieval, and reasoning-yet existing benchmarks typically report only end-task accuracy, obscuring where failures arise. To analyze the full KI-VQA pipeline, we introduce CRAG-MM-Diagnostics, a diagnostic benchmark with stage-wise data annotations that isolate 1) language-based visual grounding, 2) object identification, and 3) knowledge retrieval and reasoning. We evaluate fully parametric and retrieval-augmented VLMs, providing fine-grained analyses using newly collected metadata, such as target ROIs, entity names, and visual complexity scores. Our results point to knowledge retrieval and reasoning as the primary bottleneck, but also highlight issues in the other parts of the KI-VQA pipeline, such as the fact that VLMs struggle with target object identification or that image retrievers struggle to integrate textual cues. These findings expose fundamental limitations in current KI-VQA systems and motivate stage-aware evaluation. We, lastly, leverage these findings to propose a grounded bimodal RAG pipeline that integrates a visual grounding module to crop targets before image retrieval, boosting GPT-5 and Qwen's respective accuracies by 13.3 and 8.5 percentage points.

---


### 116. [Decoupling Cross-Modality Manifold Discrepancy: Leveraging Visible Diffusion Priors for Infrared Super-Resolution](https://arxiv.org/abs/2607.21174)

**<font color=#1a73e8>作者：</font>** Yunpeng Hua, Hongwei Yu, Jiawei Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared image super-resolution (IISR) mitigates the limitations imposed by low spatial resolution. Existing methods have recognized that IISR should preserve consistency in global distribution and structural information while enhancing image clarity. However, these methods are either insufficient or overly intrusive, a problem that becomes even more pronounced in diffusion-based models. To address these issues, we propose a dual-path diffusion-based framework for IISR, termed Shift-IISR. The proposed method is designed to improve the consistency of IISR results while preserving the generative capacity of diffusion models. Specifically, we develop a Global Representation Modulation (GRM) module to extract modality-specific information from infrared imagery and guide the global distribution of the diffusion model toward the ground truth. In addition, we introduce a Local Structure Refinement (LSR) module to encourage the model to focus on structural information at each step of the iterative denoising process. Extensive experiments demonstrate that the proposed method effectively improves distributional and structural consistency while maintaining competitive super-resolution performance. The source code of the proposed Shift-IISR can be available at this https URL.

---


### 117. [Out of Sight, Still in Mind: Token Compression for Omni-LLMs](https://arxiv.org/abs/2607.21179)

**<font color=#1a73e8>作者：</font>** Suho Yoo, Youngjoon Jang, Hyebin Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The goal of this paper is to reduce the input token cost of Omni-modal large language models (Omni-LLMs) at inference time. Omni-LLMs reason jointly over audio, video and text, but the cost of the three streams is highly unbalanced: visual tokens account for the vast majority of the input, and are highly redundant. In this paper, we propose ReMo, a training-free framework that compresses visual tokens by redistributing their information across modalities: a visual token is kept only if its information appears nowhere else. ReMo achieves this in two ways: (i) it aligns audio and video in a common embedding space, and removes visual tokens already explained by the audio or by other visual tokens; and (ii) it replaces object-level visual tokens with compact text proxies, short descriptions of each object and its location, conveying the same content in far fewer tokens. On Qwen2.5-Omni at two model scales, ReMo removes 54% of the input tokens with no loss in accuracy. Indeed, it slightly exceeds the full-token model, reaching 101.2% and 101.3% of its average accuracy over five audio-visual benchmarks.

---


### 118. [Safeguards for Speech2Speech LLM-Assistants: A Case Study in Automotive Applications](https://arxiv.org/abs/2607.21180)

**<font color=#1a73e8>作者：</font>** Gregor Endler, Sebastian Kraus, Lukas Stappen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances have introduced speech-to-speech (S2S) conversational assistants capable of producing natural-sounding interactions, including non-verbal cues like tonality and mood. In the automotive domain, this enables intuitive and humanlike in-car dialogue experiences. However, integrating these end-to-end assistants limits architectural options for programmable domain-specific safeguards. This paper discusses two implementation approaches for S2S guardrails: transcript-based and tool-based. Through an empirical evaluation, we demonstrate that both strategies are insufficient for industrial deployment in most cases due to prohibitive latency (delaying each answer by 0 to 1.4 seconds even for computationally cheap checks) and technical impediments (like potentially non-deterministic tool call behavior). Finally, we outline open challenges for S2S guardrails in the automotive context.

---


### 119. [Exploring the Design Space of LLM-Based Programming Support in CS Education: A Scoping Review through the Lens of Assistance Governance](https://arxiv.org/abs/2607.21257)

**<font color=#1a73e8>作者：</font>** Minsun Kim, S. Moonwara A. Monisha, Zihan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) become integrated into programming education, learner-facing systems increasingly differ in how that assistance is bounded, enacted, and controlled. These governance decisions are often described implicitly, making it difficult to compare systems in educationally meaningful ways. To address this gap, we conduct a scoping review and qualitative synthesis of 90 peer-reviewed LLM-based programming support systems in CS education. We analyze assistance governance through three dimensions, which we refer to collectively as PEA: Policy, capturing what forms of help are allowed or restricted; Enforcement, capturing how those boundaries are operationalized through interaction and system behavior; and Authority, capturing who can configure, adapt, or override them during use. Our findings show that systems often share similar pedagogical goals, but implement those goals through varied enforcement mechanisms. At the same time, authority remains highly centralized in system logic, with fewer systems giving learners or instructors runtime control. This work contributes PEA as a three-dimensional analytic lens, a governance codebook empirically refined within these dimensions, and a map of underexplored configurations in the current design space of LLM-based programming support. By making these explicit and comparable, PEA offers a vocabulary for analyzing existing systems and designing future tools that are pedagogically bounded, configurable, and accountable.

---


### 120. [pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development](https://arxiv.org/abs/2607.21268)

**<font color=#1a73e8>作者：</font>** Chen Zhu, Xiaolu Wang, Weilong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In many social-science research tasks, such as economics, LLM-based agents must produce outputs for which no cheap, task-complete, machine-readable correctness signal exists. This creates a distinctive reliability problem for multi-agent systems: how should generation, critique, coordination, and human judgment be organized when no component can certify the final result? We address this problem through pAI-Econ-claude, a gated, human-in-the-loop multi-agent architecture for AI-assisted economic theory development. Agents coordinate through a shared workspace of inspectable intermediate records; specialized gates diagnose targeted failure modes and recommend loopbacks without certifying correctness; and human checkpoints retain authority over decisions that are costly to reverse. We evaluate the architecture on five matched economic-theory tasks against an ungated baseline. Two evaluators blinded to configuration agreed on all five pairwise rankings, preferring the gated architecture in four tasks and the baseline in one. Mean failure severity fell from 1.58 to 1.16, while overall usefulness rose from 2.60 to 3.10. The largest observed gain occurred when a reality check rejected a false market-structure premise and a proof review prompted revision of a false welfare claim. The negative case shows that scaffolding can also compress an economically important mechanism too aggressively. The results support a bounded claim: gated oversight improves the auditability of AI-assisted economic theory without substituting for formal verification, and the allocation of irreversible human judgment is a more informative design variable than pure agent autonomy. The workflow is publicly available at this https URL.

---


### 121. [The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works](https://arxiv.org/abs/2607.21273)

**<font color=#1a73e8>作者：</font>** Yu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dense per-step supervision is an appealing remedy for sparse-reward, long-horizon LLM agents: reward the agent for predicting its next observation, and memory should follow. We show that under group-normalized RL (GRPO), this recipe does not merely fail -- it destroys the policy. Across Qwen3-1.7B/4B/8B on ALFWorld, a potential-based prediction reward drives every run into a degenerate absorbing state (prediction accuracy -> 1.0, task success -> 0,episode length pinned at the horizon): the "dark room" pathology, built automatically by the optimizer. A single-factor ablation localizes the cause -- removing only GRPO's std normalization turns the same reward from catastrophic (0%) into baseline parity -- and a two-line proposition explains why: in all-fail groups the z-scored advantage is invariant to the shaping coefficient, so bounded rewards become unbounded pressure and annealing cannot help. Our central insight generalizes this: what z-scoring amplifies is a dense signal's within-group variance while all-fail groups dominate, so signals whose variance decays by mastery are structurally this http URL variance-profile criterion retrodicts our collapses, carries preregistered predictions for arms that had not yet run, and is consistent with published reward-channel successes (a compatibility check, not an independent test). Finally, a controlled signal-delivery matrix (identical signal, varying only the consumption mechanism) shows the reward channel is at best neutral while the auxiliary-loss channel gains ~20 points -- and a shuffled-gold placebo matches the true-gold arm, so the gap survives without correct labels. Endpoints are single-seed; seed replication and group-size controls are preregistered and in progress.

---


### 122. [A Comparative Evaluation of Embeddings and LLMs in a Greek Book Publisher Setting - The CUP Dataset](https://arxiv.org/abs/2607.21274)

**<font color=#1a73e8>作者：</font>** Katerina Papantoniou, Panagiotis Papadakos, Theodore Patkos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present CUP, a Greek book retrieval benchmark consisting of 868 catalog records and 104 expert-annotated queries with graded relevance judgments. We evaluate sparse (BM25), dense (sentence-transformers), hybrid, and LLM-assisted retrieval methods in this book-search setting. Multilingual embeddings outperform Greek-specific models, while hybrid retrieval performs best overall. A query-level analysis shows that BM25 excels at named-entity queries, while dense and hybrid methods improve natural-language, noisy, cross-lingual, and concept queries. Field-aware prompting has model-specific effects, while LLM TOC summarization improves TOC-only retrieval and LLM post-filtering improves early-stage retrieval at a high cost. Overall, CUP enables real-world evaluation of Greek retrieval across lexical, semantic, noisy, and cross-lingual queries.

---


### 123. [A Unified Moral-Value Dataset for Instruction Tuning](https://arxiv.org/abs/2607.21279)

**<font color=#1a73e8>作者：</font>** Zhaohui Zeng, Florian Mai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have developed rapidly and become valuable tools in everyday life. However, how to align LLMs to a particular set of human values is still an open problem. Recent studies show that instruction tuning has strong potential for zero-shot tasks and may serve as an effective approach to addressing value alignment. Nevertheless, although many datasets for instruction tuning already exist, they are not specifically designed around moral scenarios and behaviors. We construct a unified moral-value dataset that can be directly used for instruction tuning. This dataset is built upon existing moral-value datasets by merging them into a unified corpus and converting them into an instruction-response format. We show that training on a mixed dataset combining general task datasets with our dataset preserves general-task performance, and we report preliminary observations on how the mixing ratio affects value-oriented task performance. Our work provides a moral-value dataset for instruction tuning and offers a useful resource for further alignment research. The dataset is available at this https URL.

---


### 124. [Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs](https://arxiv.org/abs/2607.21291)

**<font color=#1a73e8>作者：</font>** Yidu Wu, Xiang Wang, Kejie Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong generation and reasoning performance, but the Transformer architecture incurs high inference cost. Existing acceleration methods often rely on task-specific fine-tuning or training from scratch, increasing adaptation cost and limiting cross-task usability. We present an Adaptive Depth Sparse Framework (AdaDSF) that converts off-the-shelf pre-trained LLMs into depth-sparse models without full retraining. Our key insight is that layers contribute unequally to representation transformation, characterized by the cosine similarity between layer input and output hidden states. Based on this, AdaDSF assigns layer-wise token retention ratios from similarity statistics, uses a lightweight router to select informative tokens at each layer, and introduces a feature-preserving alignment objective to match intermediate and final representations between sparse and dense models. On GPT-NeoX and Qwen2.5 over language modeling and commonsense reasoning, AdaDSF substantially reduces inference FLOPs while preserving performance close to dense counterparts. Under comparable sparsity, AdaDSF consistently yields smaller accuracy degradation than strong baselines including MoD, D-LLM, and DLO.

---


### 125. [An LLM-Driven Workflow for Automated Process Control Strategy Generation and Tuning from Dynamic Process Models](https://arxiv.org/abs/2607.21292)

**<font color=#1a73e8>作者：</font>** Ari Luna Rueda, Eike Cramer, Klaus Hellgardt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a structured large-language-model-driven workflow for automated multi-variable control design from dynamic process models. The workflow decomposes the design task into constrained code-generation steps: plant-interface construction, normalization, manipulated-variable controlled-variable (MV-CV) pairing, controller specification, closed loop simulation, scenario generation, performance evaluation and Bayesian-optimization (BO) based tuning. Generated artifacts are executed and validated before downstream tasks proceed, and failed artifacts are repaired using validation feedback. The proposed approach is demonstrated on a nonlinear gas-preheater benchmark with coupled pressure and temperature dynamics. The generated workflow produces a physically consistent decentralized PI (proportional-integral) feedback-feedforward control structure and an executable tuning environment. Bayesian optimization reduces the closed loop performance objective, which aggregates set-point tracking and disturbance-rejection errors for the controlled variables, by approximately 26.5% relative to the initial controller generated by the workflow, mainly through improved pressure-loop transient performance. This figure quantifies the automated tuning stage rather than a comparison against a manually designed controller. The results demonstrate the feasibility of using structured large-language-model-based code generation to construct executable control-design workflows, while also highlighting the need for broader validation on larger plantwide-control benchmarks.

---


### 126. [Unlearning Under Imbalance: Benchmarking Fairness in Multimodal LLM Unlearning](https://arxiv.org/abs/2607.21300)

**<font color=#1a73e8>作者：</font>** Lorenzo Orsingher, Thomas De Min, Massimiliano Mancini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning has emerged as a tool for removing personal data from trained models to comply with recent AI regulations. To evaluate unlearning effectiveness in multimodal large language models (MLLMs), prior works fine-tune models on fictitious identities, simulating unlearning requests on subsets of these IDs, which are typically uniformly distributed. However, in realistic scenarios, people from different demographic groups may request to be unlearned at different frequencies, potentially altering the model's internal beliefs for these groups and leading to biased behaviors. To fill this gap, we propose FAIRGET, the first Visual Question Answering benchmark that evaluates unlearning under unbalanced, realistic, forget requests. These requests are designed to simulate multiple realistic scenarios, ranging from simple to challenging settings, that lead to biased unlearned models if fairness is not accounted for. Additionally, we propose FAUN, the first unlearning algorithm for MLLMs that forgets unlearning data while preserving model fairness. FAUN exploits a bias-aware activation steering mechanism to unlearn identities while accounting for the unbalanced nature of the forget data. Experiments on FAIRGET and the established FIUBench demonstrate our method's superiority both in unlearning quality and fairness.

---


### 127. [GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG](https://arxiv.org/abs/2607.21324)

**<font color=#1a73e8>作者：</font>** Paolo Pedinotti, Enrico Santus  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems increasingly employ multiple LLM agents. Yet, most prior work optimizes components in isolation rather than coordinating improvements across the pipeline. We introduce GRADRAG, a framework for cross-component prompt adaptation that models the RAG pipeline as a computational graph and propagates structured evaluation feedback to update upstream agents. An Evaluator critiques downstream answers and supporting evidence, producing actionable feedback that a Prompt Optimizer uses to iteratively update adaptive agents, such as retrievers, graph constructors, and answerers. The Evaluator also triggers early stopping when the output is deemed satisfactory. We evaluate GRADRAG on the SQUALITY and QMSUM benchmarks under two retrieval paradigms: flat chunk-based retrieval using IRCoT-style query refinement (Trivedi et al., 2023), and graph-based retrieval that constructs and iteratively enriches an entity-relation graph from the document. Across both settings, GRADRAG consistently outperforms one-step refinement baselines that update only the final generator, achieving a 12-15 percentage point net preference margin in LLM-judged pairwise comparisons, with most gains realized within two refinement iterations.

---


### 128. [Capital Markets LLM Reliability Score (CM-LRS): From Plausible to Bankable](https://arxiv.org/abs/2607.21340)

**<font color=#1a73e8>作者：</font>** Prerit Ahuja  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In capital-markets workflows the question is rarely whether a large language model can produce a fluent draft, but whether the draft is bankable: defensible in front of a counter-party or a regulator, with the documents in hand. Existing methods address parts of that gap: open-domain QA benchmarks reward surface accuracy, and finance benchmarks (FinanceBench, FinQA, ConvFinQA) advance document-grounded and numerical QA but evaluate at the question-answer layer rather than the workflow outputs practitioners defend.
We introduce CM-LRS, a Capital Markets LLM Reliability Score, evaluating outputs at the workflow-output layer across seven dimensions: factual accuracy, evidence traceability, numerical consistency, workflow completeness, source discipline, decision usefulness, and reviewability/auditability. Each is scored 0-5 against a rubric anchored on signals reviewers in regulated settings use; the aggregate is tunable to the workflow.
We demonstrate CM-LRS on five workflows (DCM transaction-terms extraction, precedent retrieval, issuer profile synthesis, M&A transaction-comparable reasoning, ECM transaction-terms extraction) over public SEC EDGAR filings, a public UK takeover release, and fictional synthetic supplements, scoring four models against four independent LLM judges spanning three model families.
Three findings. First, the frontier closed-source models cluster within 0.22 points on four-judge averaged CM-LRS (Sonnet 4.6 = 4.31, Opus 4.7 = 4.30, GPT-5.5 = 4.09); all four judges place the open-weights baseline (Llama 3.3 70B = 3.15) last. Second, that gap concentrates on retrieval (2.23) and synthesis (2.15), not extraction (0.84). Third, Decision Usefulness shows the widest cross-model dispersion of any dimension (4.0 points on issuer profiling) and top-tier inter-judge agreement (mean r = 0.52).
Plausibility is cheap. Bankability is the bar.

---


### 129. [M$^3$-Gen: Interpretable Multimodal Generation of Gene Expression Profiles Using Clinical and Imaging Data](https://arxiv.org/abs/2607.21343)

**<font color=#1a73e8>作者：</font>** Francesca Pia Panaccione, Carlo Sgaravatti, Marco Venere  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrating heterogeneous biomedical data, including clinical metadata, histopathology images, and molecular profiles, is crucial for comprehensive disease understanding. However, gene expression data acquisition remains constrained by high costs and privacy concerns, limiting its use in multimodal research and AI-driven applications. We present MultiModal Molecular Generation (M$^3$-Gen), a novel framework for the generation of gene expression profiles by conditioning a Generative Adversarial Network on histopathology images and clinical metadata. M$^3$-Gen learns a unified latent representation from the clinical variables and the images, leveraging contrastive learning, and exploits the embeddings of the two modalities to guide a generative model in producing biologically coherent gene expression profiles. Evaluations on the TCGA dataset demonstrate that M$^3$-Gen generates realistic and functionally meaningful gene expression data. Importantly, by integrating multiple modalities in an attention-based mechanism, M$^3$-Gen provides intrinsic explainability: it allows the identification of which regions of the histopathology images most strongly influenced the generation of specific gene expression profiles, making the model's decisions interpretable by design.

---


### 130. [Regulating autonomous and agentic AI](https://arxiv.org/abs/2607.21345)

**<font color=#1a73e8>作者：</font>** Chris Reed, Alex Austria, Anmol Bharuka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Regulating activities where regulatees use autonomous and agentic AI is challenging. Regulatory assumptions about regulatee knowledge and control no longer hold true; much of that lies elsewhere in the AI supply chain which thus needs to be brought within the scope of regulation. Governance systems for autonomous AI cannot replicate existing governance models, but need a fresh approach. Retrospective supervisory oversight becomes ineffective as a risk management tool, and AI autonomy generates new systemic risks which require new solutions. This paper investigate four regulatory systems: UK regulation of content platforms, data protection, UK financial services, and the EU AI Act\'92s cross-sectoral regime. It analyses the challenges posed by autonomous and agentic AI and proposes potential solutions which regulators might adopt. These will transform regulation from a reactive process to an active one, and assist it in adapting to the challenges of AI autonomy.

---


### 131. [Quality-Aware Multimodal Fusion Reveals Implicit Identity in Valence-Arousal Features](https://arxiv.org/abs/2607.21347)

**<font color=#1a73e8>作者：</font>** Jisu Kim, Benjamin S. Riggan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional face recognition relies on static appearance cues and degrades in unconstrained settings with expression variation, occlusion, and poor lighting. We hypothesize that audiovisual expression dynamics carry identity-discriminative information complementary to static appearance, and that extracting this signal requires multimodal representations robust to the variable input quality of in-the-wild video. To learn such representations, we cast multimodal valence-arousal (VA) estimation as a pretext task and propose Quality-Aware Adaptive Fusion (QAAF), which estimates per-sample, per-modality reliability and adapts each modality's contribution through learned soft gating and a quality-dependent dropout. For the problem of VA estimation, QAAF achieves an average Concordance Correlation Coefficient (CCC) of 0.472 via late fusion ensembling on Aff-wild2, improving over a baseline ensemble under the same setting (0.415) as well as a single-backbone baseline (0.288). Furthermore, the proposed QAAF demonstrates greater resilience to unavailable modalities, with only a 7.5-34.4% relative decrease in CCC when one modality is missing. We then probe whether these VA-trained features encode identity without identity-specific training. On AFEW-VA (67 actors) and YTF (1,595 subjects), VA-trained backbone features rank first among evaluated soft biometric methods, and score-level fusion with ArcFace lowers EER on both datasets (0.022 to 0.021 on AFEW-VA, 0.106 to 0.104 on YTF), correcting 68.2% of ArcFace's false accepts on AFEW-VA. These findings establish multimodal VA estimation as a soft biometric modality complementary to conventional face recognition.

---


### 132. [How Many Bits Can an Adapter Write? Measuring the Capacity and Memorization of Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2607.21351)

**<font color=#1a73e8>作者：</font>** Kaizhen Tan, Heqing Du, Yang Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A LoRA adapter is a few megabytes that almost everyone treats as a skill rather than a record of the data behind it. We put that assumption on a scale. Extending compression-based memorization analysis to the frozen-base setting, we measure directly, in bits, how much a low-rank adapter writes into a model it never changes. The answer is both smaller than full fine-tuning and less lawful than parameter counting would predict. Adapters store a couple of bits per trainable parameter, well short of a full model's budget, but that figure turns less on how many parameters an adapter carries than on where they sit. Move the same parameter budget from attention into the MLP and it holds nearly twice as much; strip the frozen base of its structure and the capacity all but disappears. Applied to realistic fine-tunes of Qwen2.5, the same instrument shows privacy leakage rising with the bits an adapter writes rather than the parameters it nominally has, and it draws a clean line between supervised and reinforcement learning: the secrets that supervised fine-tuning copies down verbatim, an adapter trained on verifiable rewards never records. Measuring what fine-tuning writes, rather than attacking it after the fact, turns a piece of folklore into a quantity one can design against.

---


### 133. [Emergent Misalignment Recruits a Pre-existing Persona Subspace](https://arxiv.org/abs/2607.21356)

**<font color=#1a73e8>作者：</font>** Mohammed Suhail B Nadaf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning an aligned language model on a narrow stream of bad advice can make it broadly misaligned on questions unrelated to the training data, a phenomenon called emergent misalignment. We ask why the narrow lesson generalizes at all, and we find that narrow fine-tuning recruits a persona structure that is present in the model before the fine-tune exists. From a frozen instruction-tuned model (Qwen2.5-14B-Instruct) we extract per-domain persona subspaces by contrastive teacher forcing and find that 4 unrelated domains share one low-rank core at 657x a random-subspace null, with 82% of that core lying outside a style core built at matched diversity. The literal first optimizer step of fine-tuning on insecure code climbs a broad-misalignment margin harder than the same code framed as educational, and forecasts realized margin movement out to 375 steps. Projecting the subspace out of the residual stream throughout fine-tuning prevents broad misalignment (27.7% to 0.0% of judged generations) while a matched-rank random subspace changes nothing; injecting it into the never-fine-tuned model induces misalignment that grows with dose to 45.4%, past the fine-tuned model it is measured against. The same projection applied to the weight gradient is inert, and three post-hoc weight edits leave the disposition in place: the sharpest edit suppresses the behavior rather than removing it, and the ablated structure re-forms inside the subspace the edit cleared. Spreading a fixed budget of bad data across 4 domains produces more broad misalignment than mechanical weight superposition and matched diversity jointly account for. All measurements come from one model at 14B; the extraction is from an aligned instruction-tuned checkpoint, which leaves the structure's provenance open; and the intervention that prevents misalignment also abolishes the narrow trained behavior.

---


### 134. [FedAgentKE: Federated Semantic Knowledge Evolution for Heterogeneous Agents](https://arxiv.org/abs/2607.21361)

**<font color=#1a73e8>作者：</font>** Weihao Li, Jun Bai, Ziyang Song  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents increasingly rely on reasoning, tool use, and iterative execution, yet existing agent frameworks still operate largely in isolation. While recent memory-based agent systems improve individual agents through local retrieval and workflow reuse, local experiences remain fragmented across isolated agent frameworks, limiting cross-framework knowledge transfer and collaborative reasoning evolution. We propose FedAgentKE, a lightweight framework for Federated Semantic Knowledge Evolution across heterogeneous agents. FedAgentKE enables distributed agent frameworks to collaboratively evolve transferable reasoning abstractions through iterative semantic knowledge distillation, aggregation, and adaptation without sharing raw reasoning trajectories. Experiments demonstrate consistent improvements under both cross-framework and cross-task settings, highlighting the potential of federated semantic knowledge evolution for future collaborative agent ecosystems.

---


### 135. [ASTRA-Net: Anatomy-Specific Transfer and Representation Alignment for Drug-Induced Sleep Endoscopy Segmentation](https://arxiv.org/abs/2607.21370)

**<font color=#1a73e8>作者：</font>** Suhua Sun, Yuqiao Wang, Sheng Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative drug-induced sleep endoscopy (DISE) requires reliable airway boundaries at specific anatomical levels. Pixel-level DISE annotations are scarce, and manual contouring limits the scalability of quantitative assessment. To address this limitation, we developed ASTRA-Net for known-plane DISE segmentation with limited real annotations. Stage 1 aligned intermediate ConvNeXt-Base representations from 14,250 unlabeled virtual endoscopy frames derived from computed tomography and real DISE frames. Virtual images were used only for feature alignment. Stage 2 fine-tuned four independent UNet++ decoders on 401 real annotated frames. Structured zero-mask supervision constrained incompatible plane outputs and invalid frames. Six alignment configurations used maximum mean discrepancy, domain adversarial learning, or both objectives. On a hold-out evaluation set of 100 frames, the five-model MMD-only segmentation ensemble achieved a mean Dice of 0.8927, with a 95% image-level bootstrap interval of 0.8631 to 0.9160. The mean intersection over union was 0.8239. A classification- enabled variant of the same alignment configuration reached a restricted four-plane top-1 accuracy of 0.92 on the same hold-out frames. These results indicate that ASTRA-Net can support frame-level, plane-specific DISE boundary delineation when real annotations are limited.

---


### 136. [Multimodal Pretraining for Generalizable EEG Representation Learning](https://arxiv.org/abs/2607.21384)

**<font color=#1a73e8>作者：</font>** Targol Bakhtiarvand, Jugal Kalita, Adham Atyabi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) models used for epilepsy are often limited to specific datasets and tasks. This limited approach can make it challenging to apply these models across different datasets or in various situations. However, recent studies in foundation models and self-supervised learning suggest that an adaptable EEG backbone could support a range of EEG related tasks. In this study, we have developed a multimodal EEG foundation model that combines a raw signal encoder based on the Mamba architecture, a Vision Transformer (ViT)-style encoder for time-frequency data, and a lightweight encoder for text, all within a shared embedding space. The pretraining process relies on several innovative techniques, such as masked modeling, cross-view contrastive alignment, and temporal consistency losses. These methods are designed to create rich, seizure-relevant representations without requiring labeled data. To assess the efficacy and generalization of our pretrained model, we fine-tuned it on the canonical CHB-MIT seizure detection benchmark and additional seizure detection datasets, and conducted extensive experiments comparing different model variants. On the standard CHB-MIT split, our best single model achieved an AUROC of 0.874, and an ensemble variant reached 0.878 AUROC, representing state-of-the-art performance on this benchmark. In addition to standard train-test splits, we evaluated performance under a leave-one-subject-out (LOSO) protocol, which is rarely reported in prior EEG seizure modeling work and highlights the difficulty of patient-independent seizure detection, with a mean LOSO balanced accuracy of 0.558 across 19 subjects. Across datasets and evaluation settings, our multimodal foundation model enabled robust seizure detection and straightforward adaptation to new seizure detection scenarios, while also supporting interpretable seizure localization.

---


### 137. [MSBraM: A Multi-scale Self-supervised Brain Foundation Model for Hierarchical EEG Dynamics Learning](https://arxiv.org/abs/2607.21402)

**<font color=#1a73e8>作者：</font>** Tao Zhou, Jing Han, Lingyu Shu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-supervised foundation models have recently shown strong potential for electroencephalogram (EEG)-based analysis. However, existing approaches struggle to capture the inherently multi-scale temporal structure of EEG signals, where local neural patterns and long-range dependencies jointly encode task-relevant information. This limitation hampers cross-scale representation learning and generalization across diverse downstream tasks. To address this challenge, we propose MSBraM, a Multi-Scale self-supervised Brain foundation Model designed to learn hierarchical EEG representations. MSBraM follows a two-stage pretraining framework. First, a multi-scale neural tokenizer discretizes raw EEG signals into semantic codes at different temporal resolutions via vector-quantized reconstruction. Second, the model is pretrained to predict masked codes using a curriculum multi-scale masking strategy, progressively integrating fine-grained local patterns with global temporal context. We pretrain MSBraM on over 2,400 hours of EEG data and evaluate it across 10 downstream tasks on 12 public datasets. Extensive experiments show that MSBraM achieves superior performance on other state-of-the-art pretrained models, demonstrating strong generalization and transferability. These results indicate that explicitly modeling multi-scale temporal dynamics is critical for effective EEG foundation models.

---


### 138. [Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning via Prolog](https://arxiv.org/abs/2607.21412)

**<font color=#1a73e8>作者：</font>** Bartolomeo Bogliolo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) excel at natural language understanding and generation but remain unreliable for multi-step logical reasoning, especially in safety-critical or compliance-sensitive domains. Recent neuro-symbolic approaches address this gap by coupling neural models with external symbolic engines, yet most integrations are bespoke and lack a standardized interface for tool-augmented agents. This paper presents Euclid-MCP, an open-source MCP server that provides deterministic logical reasoning via SWI-Prolog. Euclid-MCP introduces Euclid-IR, an engine-agnostic intermediate representation for Horn-clause logic that is human-readable, easy for LLMs to generate, and straightforward to compile into Prolog or alternative backends. The server exposes a compact tool interface that supports a translate-run-inspect-repair loop, enabling LLM clients to delegate inference while retaining full access to proof traces and derivation logs. We evaluate Euclid-MCP on a realistic IT security and compliance use case. Results show that while LLMs alone are sufficient on small knowledge bases, they hallucinate systematically on larger problems, whereas Euclid-MCP delivers exact answers with lower latency and more compact outputs. We argue that semantic RAG is fundamentally unsuited for rule enforcement, and that Euclid-MCP can serve as a stable, shared reasoning substrate for both RAG-based assistants and agentic systems.

---


### 139. [PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.21419)

**<font color=#1a73e8>作者：</font>** Yipeng Shi, Zhipeng Ma, Yue Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In long-horizon LLM agent reinforcement learning, weak policies often repeat similar failures, producing uninformative rollout trajectories and limiting effective policy optimization. Existing skill-centric methods improve exploration by optimizing, filtering, or internalizing reusable skills. However, they remain centered on the skills themselves rather than being designed as adaptive training-time support for the evolving policy. To address this, we propose a policy-centric training paradigm that reframes skills as a dynamic training scaffold. Our framework, Pats, converts rollout groups from the latest policy into evidence cards and uses task-specific evaluation to adjust the context used in subsequent rollouts. Concrete guidance helps weak policies to complete challenging tasks. As policy improves, redundant context is revised or removed to reduce reliance on explicit guidance while preserving useful rollout variation. The policy is optimized with environmental rewards using standard RLVR, and the training scaffold is discarded at deployment. On ALFWorld and WebShop, Pats improves over strong baselines by up to 18.6%. Across seven search-augmented QA benchmarks, it remains competitive while using 32.1% fewer prompt tokens than the baseline.

---


### 140. [An Evaluation Framework for Structured Audio Captions Validated by Controlled Perturbations](https://arxiv.org/abs/2607.21424)

**<font color=#1a73e8>作者：</font>** Liang-Yuan Wu, Sripathi Sridhar, Mark Cartwright 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advancements in automated audio captioning (AAC) have shifted from monolithic sentence generation toward structured formats that explicitly disentangle distinct acoustic and semantic properties. However, evaluating this heterogeneous data remains a significant challenge. Existing caption metrics focus on flat textual outputs and fail to reliably assess multimodal attributes. To bridge this gap, we propose a multi-axis evaluation framework tailored for structured audio descriptions. Building on the AudioCards dataset, we evaluate outputs across five orthogonal axes: tag-sets, descriptions, logical reasoning, numeric measurements, and spectral profiles. Our approach combines Large Language Model (LLM) judges to capture semantic nuance with deterministic computational metrics to precisely measure acoustic deviations. To rigorously validate the reliability of this framework, we introduce a controlled perturbation testing protocol that injects typed, graded errors into groundtruth annotations. Our results demonstrate that this framework successfully distinguishes meaning-preserving paraphrases from genuine semantic and acoustic corruptions.

---


### 141. [When Trivia Is Not Trivial: Everyday Knowledge Failures in Multilingual LLMs](https://arxiv.org/abs/2607.21445)

**<font color=#1a73e8>作者：</font>** Anna Mosolova, Djamé Seddah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quiz rooms, trivia nights, and quiz shows challenge human knowledge across a wide range of topics, from canonical facts to everyday culture. In this paper, we examine whether large language models (LLMs) can perform competitively in such settings, using quiz-style questions to test them on both common and niche topics. We introduce TriviaRoomQA, a multilingual benchmark designed to evaluate everyday, culturally grounded, and long-tail knowledge across 288 topics. The benchmark contains 3,300 parallel multiple-choice questions in six European languages and additional 5,340 French-only questions for a more fine-grained case study. We evaluate 30 open-weight LLMs from European, Asian, and North American providers, covering models from 7 to 70B parameters. We find that models are strong on knowledge-intensive topics such as history, geography, and mathematics, but substantially weaker on everyday popular-culture topics such as celebrities, music, movies, and news. Moreover, model performance varies across languages even for the same underlying questions, suggesting that access to factual knowledge is not always language-independent. In sum, our dataset and experiments demonstrate an important knowledge gap which is not captured by existing academic-based saturated benchmarks.

---


### 142. [KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training Quantization of Diffusion Transformers](https://arxiv.org/abs/2607.21446)

**<font color=#1a73e8>作者：</font>** Yann Bouquet, Alireza Khodamoradi, Kristof Denolf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) of diffusion transformers (DiTs) to W4A4 severely degrades output quality, because activations entering each linear layer contain outliers that 4-bit formats cannot represent. The standard fix applies an invertible linear transform to the activations and its inverse to the weights before quantizing both. Normalization layers between blocks force this transform to run online at every denoising step, making its inference computation cost the binding design constraint. Existing options trade quantization quality for inference cost: per-channel scaling (SmoothQuant) is computationally cheap but impacts the magnitude of the channels, which can harm quantization accuracy; fixed Hadamard transforms yield better quantization accuracy but require large block sizes that incur a high online cost; learned full-$d$ invertible transforms calibrate best but entail a prohibitive dense $d \times d$ matrix multiplication (GEMM) per layer per step.
We propose KroQuant, a PTQ method that applies a learned Kronecker-structured invertible transform to each 32-element block of the activation, storing less than half the parameters of per-channel scaling. The block-local structure runs as small tensor-core GEMMs, and on an MI350 GPU the KroQuant quantizer kernel is up to $14\%$ faster than the SmoothQuant kernel. Offline LoRaQ weight calibration then absorbs the residual per-weight quantization error. On PixArt-$\Sigma$, SANA, and FLUX.1-schnell at W4A4 (MXFP4e2), KroQuant produces outputs closer to the FP reference than SVDQuant and LoRaQ on MJHQ-30K and SDCI, while preserving or improving image quality.

---


### 143. [Detecting LLM-Generated Tokens in Human--LLM Coauthored Text](https://arxiv.org/abs/2607.21458)

**<font color=#1a73e8>作者：</font>** Yangjun Lu, Hongyi Zhou, Fabian Spill 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rise of human-AI collaborative writing has created a growing need for fine-grained detection methods that support localizing likely LLM-generated content in mixed-authorship documents. Existing methods for detecting LLM-generated text mainly focus on document-level classification and cannot identify which parts of the text are generated by LLMs. This paper introduces a new method to address this urgent need. Our method operates at the token level, the natural unit of modern language models, and builds on existing token-level detection scores. The key idea is to smooth adjacent token scores to reduce their variability, while using an adaptive Lepski-type rule to select the bandwidth according to the local authorship structure. Our method is simple to implement and does not require token-level labeled data for training. Theoretically, we characterize this trade-off and show that the proposed method achieves favorable mean square error performance in estimating the underlying signal. Empirically, we demonstrate strong performance of our method against a wide range of baselines in both synthetic datasets and a realistic dataset. We deploy a publicly accessible website that implements the methods as well.

---


### 144. [Thinkink: 2D Spatial Ink-native Interaction with LLMs](https://arxiv.org/abs/2607.21468)

**<font color=#1a73e8>作者：</font>** Mohammad Hasan Payandeh, Daniel Vogel, Jian Zhao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People often use handwritten notes and sketches to externalize ideas for ideation. To integrate large language models (LLMs) into this practice, we propose Thinkink. Prompts can be handwritten text or drawn sketches with LLM-generated responses visualized as ink-like text and sketches spatially integrated into a shared canvas. A semantic tree streamlines ink interpretation, and a lightweight UI provides explicit control using a state machine. The tool was designed using a three-stage process. A formative study (N=12) examined current practices with conventional and digital inking methods. The results informed a technical probe for a diagnostic study (N=6) identifying usability and human-LLM interaction challenges. This motivated the design of Thinkink, with a final study (N=10) examining how people incorporate it into their ideation practices. We contribute design implications and a tool for ink-native LLM interaction where the user and LLM write and draw in a shared 2D canvas.

---


### 145. [Finite-Sample Coverage Audits for High-Recall Candidate Generation: Certification and Learning-Theoretic Design](https://arxiv.org/abs/2607.21480)

**<font color=#1a73e8>作者：</font>** Martin Anthony, Kaveh Salehzadeh Nobari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An initial high-recall stage in an empirical pipeline decides which items pass to later review, labelling, or modelling, and relevant items it misses are lost to every subsequent stage. We study how many audit labels are needed to certify, with finite-sample validity, that this missed relevant mass is small, and our main results characterise the label complexity of this problem. We first show that no procedure using only labels from inside the candidate set can certify any non-trivial bound on the missed mass: the audit must sample the excluded pool, the only region where unrecovered relevant items can lie. We then prove a matching finite-corpus lower bound. Any valid audit that certifies fewer than $m$ missed relevant items with high probability when none are present, even if adaptive and permitted to label the entire included pool, must inspect on the order of $N_0/m$ excluded-pool labels. Excluded-pool auditing is therefore minimax rate-optimal, not merely convenient, for missed-mass certification in the zero-miss regime. Building on this characterisation, we develop an exact finite-sample toolkit, using binomial and hypergeometric inversion rather than asymptotic approximation, that certifies missed mass, converts it to recall through a two-pool design, certifies pre-specified families of nested candidate generators simultaneously, and produces stress-test certificates against declared perturbation mechanisms. These certificates can be paired with observable review burden to select the least burdensome pre-specified candidate generator meeting a missed-mass target. Every guarantee holds under one discipline: the candidate generator, or the pre-specified family from which it is selected, and the audit rule are fixed before the certification labels are examined.

---


### 146. [Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks](https://arxiv.org/abs/2607.21482)

**<font color=#1a73e8>作者：</font>** Mack Nixon, Liam Wright, Yevgeniya Kovalchuk 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models. Their adoption in research using personal data is constrained by governance requirements that typically prohibit data transmission to external services. Locally deployable open-weight models offer an alternative since sensitive data never leave the local environment. We introduce an open-source framework for evaluating the efficacy of AI agents powered by open-weight LLMs on one of the most persistent bottlenecks in research on longitudinal population studies: data preparation. The framework comprises: a curated ground-truth dataset (cleaning scripts preparing six sweeps of data from a British cohort study), task definitions encompassing tasks such as category harmonization and multi-wave merging, and automated routines for evaluating the LLM-produced R code and outputted data. We benchmark LLMs across the (consumer grade) deployment spectrum to assess their efficacy in 20 data preparation tasks (creation of 102 variables). Current state-of-the-art, 31-35B parameter models almost saturated our benchmark ("average task completion" up to 87.9%). The performance of open-weight LLMs running on consumer-grade hardware shows promise of a viable path toward AI-assisted data preparation in governance-restricted research settings. Our framework is publicly available at: this https URL.

---


### 147. [Artificial Epanorthosis: Why large language models overuse a classical rhetorical figure, and how to mitigate it](https://arxiv.org/abs/2607.21498)

**<font color=#1a73e8>作者：</font>** Federico Boggia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A rhetorical figure that Cicero and Quintilian catalogued two thousand years ago reappears, systematically, in the text of large language models: epanorthosis, the self-correction of the specimen «This is not a course. It is a journey of transformation». This essay argues that the overuse is a trained disposition, driven mainly by a training distribution rich in promotional prose and by preference tuning (RLHF) that rewards confident, emphatic phrasing; the left-to-right nature of generation is an amplifier rather than the root cause. Building on evidence that models diverge from human rhetorical style, and on Fontanier's classification of epanorthosis as a figure of thought, it sets out a programme that scores the figure against genre-specific human baselines through an Epanorthosis Index (density relative to the human rate). A first measurement, on three sizes of one instruction-tuned model family, finds mis-calibration by register in both directions: the models overshoot in oratory (about twofold, near threefold in Italian, concentrated in the larger tiers) and undershoot in informal question-and-answer writing, while matching humans in argument, journalism, and encyclopedic prose. Three constructive contributions follow: a survey of mitigation techniques centred on lightweight LoRA adapters; a demonstration, in Italian, that a one-line instruction cuts the figure by half to nearly three-quarters and that a supervised-fine-tuning adapter removes it almost entirely, with a scaling coefficient that dials the reduction back onto the human rate; and the argument that the target is calibration to the human rate for each genre, not elimination. It closes on the stakes: the real risk is that we begin to write like the machines.

---


### 148. [Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems](https://arxiv.org/abs/2607.21503)

**<font color=#1a73e8>作者：</font>** Gaurav Dadhich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token cost that grows every turn, producing missing recalls within and across conversations. The incumbent response treats this as a storage-and-retrieval problem. We argue that framing is too narrow. Actively managing what an agent holds in mind is a lifecycle, not merely a store: it spans deciding what to remember, extracting and structuring it, choosing the right store per data type, consolidating and forgetting while preserving provenance, deciding what is relevant now, anticipating what is needed next, and compacting context to a budget without losing what matters. In serious production this operates not over a single user but across an organizational scope hierarchy. We name this discipline Agentic Context Management (ACM) and decompose it into five primitives: architecting, ingesting, scoping, anticipating, and compacting & consolidation. We then make the economic case: naive context accumulation grows token cost quadratically in conversation length, crude summarization buys linear cost at the price of an accuracy cliff, and only validated compaction achieves linear cost with preserved fidelity. We describe a reference implementation, Maximem Synap, that realizes the five primitives as a multi-tenant service and reports 92% on LongMemEval and 93.2% on LoCoMo under the configuration detailed in Section 6. We close with dimensions existing benchmarks do not yet capture, latency, token efficiency, and context-rot resistance, and the frontier of decision-level and organization-level context the category points toward.

---


### 149. [X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy Alignment](https://arxiv.org/abs/2607.21550)

**<font color=#1a73e8>作者：</font>** Dongjie Fu, Di Cao, Xize Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While large audio-language models have achieved remarkable progress in auditory perception, they still lag behind text-based large language models in deep logical reasoning, primarily due to the scarcity of high-quality audio reasoning data. To bridge this gap, we propose X$^3$-OPD, a cross-modal on-policy distillation framework that transfers reasoning capabilities from a powerful text teacher to an audio-language student. During training, the student generates reasoning trajectories conditioned on its own acoustic perception, while the teacher provides token-level guidance using matched textual inputs and verified answers. We further construct a three-tier symmetric corpus covering textual reasoning rendered into speech, audio-event reasoning grounded in complex acoustic scenes, and spoken-dialogue reasoning involving paralinguistic cues. This design extends cross-modal distillation beyond textually recoverable content to reasoning grounded in non-linguistic events, prosody, and conversational context. Experiments on MMSU, MMAU, BIG Bench Audio, and MMAR demonstrate that X$^3$-OPD substantially improves audio-grounded reasoning and chain-of-thought quality while largely preserving the model's existing capabilities under domain shift.

---


### 150. [MIRROR: Learning from the Other View for Multi-Modal Reasoning](https://arxiv.org/abs/2607.21552)

**<font color=#1a73e8>作者：</font>** Wen Ye, Yuxiao Qu, Aviral Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unlike large language models (LLMs) that exhibit strong reasoning capabilities, vision-language models (VLMs) struggle with visual reasoning, even on geometry problems that admit equivalent text, diagram, and combined diagram+text views. We show that these views often elicit different behaviors: a model may solve a problem from text but fail on the corresponding diagram, or succeed visually while failing textually. This inconsistency suggests that different views expose complementary reasoning paths and failure modes that standard multimodal post-training does not fully exploit. To study and exploit this phenomenon, we construct ODA-Data, a high-quality paired multimodal geometry dataset with text-dominant, image-dominant, and combined image+text views of the same problems, together with splits for training and evaluating modality-dependent reasoning behaviors. We then develop Modality-Informed Reciprocal Reasoning Optimization (MIRROR), a reinforcement learning approach for improving multimodal reasoning via self supervision. For each problem, MIRROR evaluates the model under all views, selects the best-performing view as a teacher, and trains other views with a reverse-KL objective towards the teacher. Across reasoning benchmarks that evaluate on geometry problems, MIRROR improves over standard RL and yields more accurate and consistent behavior across modalities

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-153](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
