# 🧠 大模型相关研究 | 2026年04月29日

> 本类共 **215** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-215**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-215**

---

### 201. [Probing CLIP's Comprehension of 360-Degree Textual and Visual Semantics](https://arxiv.org/abs/2604.24642)

**<font color=#1a73e8>作者：</font>** Hai Wang, Xiaochen Yang, Mingzhi Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The dream of instantly creating rich 360-degree panoramic worlds from text is rapidly becoming a reality, yet a crucial gap exists in our ability to reliably evaluate their semantic alignment. Contrastive Language-Image Pre-training (CLIP) models, standard AI evaluators, predominantly trained on perspective image-text pairs, face an open question regarding their understanding of the unique characteristics of 360-degree panoramic image-text pairs. This paper addresses this gap by first introducing two concepts: \emph{360-degree textual semantics}, semantic information conveyed by explicit format identifiers, and \emph{360-degree visual semantics}, invariant semantics under horizontal circular shifts. To probe CLIP's comprehension of these semantics, we then propose novel evaluation methodologies using keyword manipulation and horizontal circular shifts of varying magnitudes. Rigorous statistical analyses across popular CLIP configurations reveal that: (1) CLIP models effectively leverage explicit textual identifiers, demonstrating an understanding of 360-degree textual semantics; and (2) CLIP models fail to robustly preserve semantic alignment under horizontal circular shifts, indicating limited comprehension of 360-degree visual semantics. To address this limitation, we propose a LoRA-based fine-tuning framework that explicitly instills invariance to circular shifts. Our fine-tuned models exhibit improved comprehension of 360-degree visual semantics, though with a slight degradation in original semantic evaluation performance, highlighting a fundamental trade-off in adapting CLIP to 360-degree panoramic images. Code is available at this https URL.

---


### 202. [K-MetBench: A Multi-Dimensional Benchmark for Fine-Grained Evaluation of Expert Reasoning, Locality, and Multimodality in Meteorology](https://arxiv.org/abs/2604.24645)

**<font color=#1a73e8>作者：</font>** Soyeon Kim, Cheongwoong Kang, Myeongjin Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The development of practical (multimodal) large language model assistants for Korean weather forecasters is hindered by the absence of a multidimensional, expert-level evaluation framework grounded in authoritative sources. To address this, we introduce K-MetBench, a diagnostic benchmark grounded in national qualification exams. It exposes critical gaps across four dimensions: expert visual reasoning of charts, logical validity via expert-verified rationales, Korean-specific geo-cultural comprehension, and fine-grained domain analysis. Our evaluation of 55 models reveals a profound modality gap in interpreting specialized diagrams and a reasoning gap where models hallucinate logic despite correct predictions. Crucially, Korean models outperform significantly larger global models in local contexts, demonstrating that parameter scaling alone cannot resolve cultural dependencies. K-MetBench serves as a roadmap for developing reliable, culturally aware expert AI agents. The dataset is available at this https URL .

---


### 203. [DepthKV: Layer-Dependent KV Cache Pruning for Long-Context LLM Inference](https://arxiv.org/abs/2604.24647)

**<font color=#1a73e8>作者：</font>** Zahra Dehghanighobadi, Asja Fischer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context reasoning is a critical capability of large language models (LLMs), enabling applications such as long-document understanding, summarization, and code generation. However, efficient autoregressive inference relies on the key-value (KV) cache, whose memory footprint grows linearly with sequence length, leading to a major memory bottleneck. To mitigate this overhead, KV cache pruning methods discard cached tokens with low attention scores during inference. Most existing methods apply a uniform pruning ratio across layers, implicitly assuming that all layers contribute equally to overall model performance. We show that this assumption is suboptimal, as layers differ significantly in their sensitivity to pruning. We propose DepthKV, a layer-dependent pruning framework that allocates a fixed global KV budget across layers based on their sensitivity, rather than using a uniform allocation. Across multiple models and tasks, DepthKV consistently outperforms uniform pruning at the same global pruning ratio, demonstrating more effective utilization of the KV cache budget through layer-dependent allocation.

---


### 204. [Benchmarking Source-Sensitive Reasoning in Turkish: Humans and LLMs under Evidential Trust Manipulation](https://arxiv.org/abs/2604.24665)

**<font color=#1a73e8>作者：</font>** Sercan Karakaş, Yusuf Şimşek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates whether source trustworthiness shapes Turkish evidential morphology and whether large language models (LLMs) track this sensitivity. We study the past-domain contrast between -DI and -mIs in controlled cloze contexts where the information source is overtly external, while only its perceived reliability is manipulated (High-Trust vs. Low-Trust). In a human production experiment, native speakers of Turkish show a robust trust effect: High-Trust contexts yield relatively more -DI, whereas Low-Trust contexts yield relatively more -mIs, with the pattern remaining stable across sensitivity analyses. We then evaluate 10 LLMs in three prompting paradigms (open gap-fill, explicit past-tense gap-fill, and forced-choice A/B selection). LLM behavior is highly model- and prompt-dependent: some models show weak or local trust-consistent shifts, but effects are generally unstable, often reversed, and frequently overshadowed by output-compliance problems and strong base-rate suffix preferences. The results provide new evidence for a trust-/commitment-based account of Turkish evidentiality and reveal a clear human-LLM gap in source-sensitive evidential reasoning.

---


### 205. [The Price of Agreement: Measuring LLM Sycophancy in Agentic Financial Applications](https://arxiv.org/abs/2604.24668)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhao, Aparna Balagopalan, Adi Agrawal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Given the increased use of LLMs in financial systems today, it becomes important to evaluate the safety and robustness of such systems. One failure mode that LLMs frequently display in general domain settings is that of sycophancy. That is, models prioritize agreement with expressed user beliefs over correctness, leading to decreased accuracy and trust. In this work, we focus on evaluating sycophancy that LLMs display in agentic financial tasks. Our findings are three-fold: first, we find the models show only low to modest drops in performance in the face of user rebuttals or contradictions to the reference answer, which distinguishes sycophancy that models display in financial agentic settings from findings in prior work. Second, we introduce a suite of tasks to test for sycophancy by user preference information that contradicts the reference answer and find that most models fail in the presence of such inputs. Lastly, we benchmark different modes of recovery such as input filtering with a pretrained LLM.

---


### 206. [Benchmarking Pathology Foundation Models for Breast Cancer Survival Prediction](https://arxiv.org/abs/2604.24679)

**<font color=#1a73e8>作者：</font>** Fredrik K. Gustafsson, Constance Boissin, Johan Vallon-Christersson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (PFMs) have recently emerged as powerful pretrained encoders for computational pathology, enabling transfer learning across a wide range of downstream tasks. However, systematic comparisons of these models for clinically meaningful prediction problems remain limited, especially in the context of survival prediction under external validation. In this study, we benchmark widely used and recently proposed PFMs for breast cancer survival prediction from whole-slide histopathology images. Using a standardized pipeline based on patch-level feature extraction and a unified survival modeling framework, we evaluate model representations across three independent clinical cohorts comprising more than 5,400 patients with long-term follow-up. Models are trained on one cohort and evaluated on two independent external cohorts, enabling a rigorous assessment of cross-dataset generalization. Overall, H-optimus-1 achieves the strongest survival prediction performance. More broadly, we observe consistent generational improvements across model families, with second-generation PFMs outperforming their first-generation counterparts. However, absolute performance differences between many recent PFMs remain modest, suggesting diminishing returns from further scaling of pretraining data or model size alone. Notably, the compact distilled model H0-mini slightly outperforms its larger teacher model H-optimus-0, despite using fewer than 8% of the parameters and enabling significantly faster feature extraction. Together, these results provide the first large-scale, externally validated benchmark of PFMs for breast cancer survival prediction, and offer practical guidance for efficient deployment of PFMs in clinical workflows.

---


### 207. [Can LLMs Act as Historians? Evaluating Historical Research Capabilities of LLMs via the Chinese Imperial Examination](https://arxiv.org/abs/2604.24690)

**<font color=#1a73e8>作者：</font>** Lirong Gao, Zeqing Wang, Yuyan Cai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have increasingly assisted in historical tasks such as text processing, their capacity for professional-level historical reasoning remains underexplored. Existing benchmarks primarily assess basic knowledge breadth or lexical understanding, failing to capture the higher-order skills, such as evidentiary reasoning,that are central to historical research. To fill this gap, we introduce ProHist-Bench, a novel benchmark anchored in the Chinese Imperial Examination (Keju) system, a comprehensive microcosm of East Asian political, social, and intellectual history spanning over 1,300 years. Developed through deep interdisciplinary collaboration, ProHist-Bench features 400 challenging, expert-curated questions across eight dynasties, accompanied by 10,891 fine-grained evaluation rubrics. Through a rigorous evaluation of 18 LLMs, we reveal a significant proficiency gap: even state-of-the-art LLMs struggle with complex historical research questions. We hope ProHist-Bench will facilitate the development of domain-specific reasoning LLMs, advance computational historical research, and further uncover the untapped potential of LLMs. We release ProHist-Bench at this https URL.

---


### 208. [Contextual Linear Activation Steering of Language Models](https://arxiv.org/abs/2604.24693)

**<font color=#1a73e8>作者：</font>** Brandon Hsu, Daniel Beaglehole, Adityanarayanan Radhakrishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear activation steering is a powerful approach for eliciting the capabilities of large language models and specializing their behavior using limited labeled data. While effective, existing methods often apply a fixed steering strength to all tokens, resulting in inconsistent steering quality across diverse input prompts. In this work, we introduce Contextual Linear Activation Steering (CLAS), a method that dynamically adapts linear activation steering to context-dependent steering strengths. Across eleven steering benchmarks and four model families, it consistently outperforms standard linear activation steering and matches or exceeds the performance of ReFT and LoRA in settings with limited labeled data. We therefore propose CLAS as a scalable, interpretable, and accurate method for specializing and steering large language models.

---


### 209. [Can Current Agents Close the Discovery-to-Application Gap? A Case Study in Minecraft](https://arxiv.org/abs/2604.24697)

**<font color=#1a73e8>作者：</font>** Zhou Ziheng, Huacong Tang, Jinyuan Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discovering causal regularities and applying them to build functional systems--the discovery-to-application loop--is a hallmark of general intelligence, yet evaluating this capacity has been hindered by the vast complexity gap between scientific discovery and real-world engineering. We introduce SciCrafter, a Minecraft-based benchmark that operationalizes this loop through parameterized redstone circuit tasks. Agents must ignite lamps in specified patterns (e.g., simultaneously or in timed sequences); scaling target parameters substantially increases construction complexity and required knowledge, forcing genuine discovery rather than reliance on memorized solutions. Evaluating frontier models including GPT-5.2, Gemini-3-Pro, and Claude-Opus-4.5 under a general-purpose code agent scaffold, we find that all plateau at approximately 26% success rate. To diagnose these failures, we decompose the loop into four capacities--knowledge gap identification, experimental discovery, knowledge consolidation, and knowledge application--and design targeted interventions whose marginal contributions serve as proxies for corresponding gaps. Our analysis reveals that although the general knowledge application capability still remains as the biggest gap across all models, for frontier models the knowledge gap identification starts to become a major hurdle--indicating the bottleneck is shifting from solving problems right to raising the right problems for current AI. We release SciCrafter as a diagnostic probe for future research on AI systems that navigate the full discovery-to-application loop.

---


### 210. [The Chameleon's Limit: Investigating Persona Collapse and Homogenization in Large Language Models](https://arxiv.org/abs/2604.24698)

**<font color=#1a73e8>作者：</font>** Yunze Xiao, Vivienne J. Zhang, Chenghao Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Applications based on large language models (LLMs), such as multi-agent simulations, require population diversity among agents. We identify a pervasive failure mode we term \emph{Persona Collapse}: agents each assigned a distinct profile nonetheless converge into a narrow behavioral mode, producing a homogeneous simulated population. To quantify persona collapse, we propose a framework that measures how much of the persona space a population occupies (Coverage), how evenly agents spread across it (Uniformity), and how rich the resulting behavioral patterns are (Complexity). Evaluating ten LLMs on personality simulation (BFI-44), moral reasoning, and self-introduction, we observe persona collapse along two axes: (1) Dimensions: a model can appear diverse on one axis yet structurally degenerate on another, and (2) Domains: the same model may collapse the most in personality yet be the most diverse in moral reasoning. Furthermore, item-level diagnostics reveal that behavioral variation tracks coarse demographic stereotypes rather than the fine-grained individual differences specified in each persona. Counter-intuitively, \textbf{the models achieving the highest per-persona fidelity consistently produce the most stereotyped populations}. We release our toolkit and data to support population-level evaluation of LLMs.

---


### 211. [Green Shielding: A User-Centric Approach Towards Trustworthy AI](https://arxiv.org/abs/2604.24700)

**<font color=#1a73e8>作者：</font>** Aaron J. Li, Nicolas Sanchez, Hao Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed, yet their outputs can be highly sensitive to routine, non-adversarial variation in how users phrase queries, a gap not well addressed by existing red-teaming efforts. We propose Green Shielding, a user-centric agenda for building evidence-backed deployment guidance by characterizing how benign input variation shifts model behavior. We operationalize this agenda through the CUE criteria: benchmarks with authentic Context, reference standards and metrics that capture true Utility, and perturbations that reflect realistic variations in the Elicitation of model behavior. Guided by the PCS framework and developed with practicing physicians, we instantiate Green Shielding in medical diagnosis through HealthCareMagic-Diagnosis (HCM-Dx), a benchmark of patient-authored queries, together with structured reference diagnosis sets and clinically grounded metrics for evaluating differential diagnosis lists. We also study perturbation regimes that capture routine input variation and show that prompt-level factors shift model behavior along clinically meaningful dimensions. Across multiple frontier LLMs, these shifts trace out Pareto-like tradeoffs. In particular, neutralization, which removes common user-level factors while preserving clinical content, increases plausibility and yields more concise, clinician-like differentials, but reduces coverage of highly likely and safety-critical conditions. Together, these results show that interaction choices can systematically shift task-relevant properties of model outputs and support user-facing guidance for safer deployment in high-stakes domains. Although instantiated here in medical diagnosis, the agenda extends naturally to other decision-support settings and agentic AI systems.

---


### 212. [Case-Specific Rubrics for Clinical AI Evaluation: Methodology, Validation, and LLM-Clinician Agreement Across 823 Encounters](https://arxiv.org/abs/2604.24710)

**<font color=#1a73e8>作者：</font>** Aaryan Shah, Andrew Hines, Alexia Downs 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective. Clinical AI documentation systems require evaluation methodologies that are clinically valid, economically viable, and sensitive to iterative changes. Methods requiring expert review per scoring instance are too slow and expensive for safe, iterative deployment. We present a case-specific, clinician-authored rubric methodology for clinical AI evaluation and examine whether LLM-generated rubrics can approximate clinician agreement.
Materials and Methods. Twenty clinicians authored 1,646 rubrics for 823 clinical cases (736 real-world, 87 synthetic) across primary care, psychiatry, oncology, and behavioral health. Each rubric was validated by confirming that an LLM-based scoring agent consistently scored clinician-preferred outputs higher than rejected ones. Seven versions of an EHR-embedded AI agent for clinicians were evaluated across all cases.
Results. Clinician-authored rubrics discriminated effectively between high- and low-quality outputs (median score gap: 82.9%) with high scoring stability (median range: 0.00%). Median scores improved from 84% to 95%. In later experiments, clinician-LLM ranking agreement (tau: 0.42-0.46) matched or exceeded clinician-clinician agreement (tau: 0.38-0.43), attributable to both ceiling compression and LLM rubric improvement.
Discussion. This convergence supports incorporating LLM rubrics alongside clinician-authored ones. At roughly 1,000 times lower cost, LLM rubrics enable substantially greater evaluation coverage, while continued clinical authorship grounds evaluation in expert judgment. Ceiling compression poses a methodological challenge for future inter-rater agreement studies.
Conclusion. Case-specific rubrics offer a path for clinical AI evaluation that preserves expert judgment while enabling automation at three orders lower cost. Clinician-authored rubrics establish the baseline against which LLM rubrics are validated.

---


### 213. [Long-Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling](https://arxiv.org/abs/2604.24715)

**<font color=#1a73e8>作者：</font>** Parsa Ashrafi Fashi, Utkarsh Saxena, Mehdi Rezagholizadeh 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hybrid sequence models that combine efficient Transformer components with linear sequence modeling blocks are a promising alternative to pure Transformers, but most are still pretrained from scratch and therefore fail to reuse existing Transformer checkpoints. We study upcycling as a practical path to convert pretrained Transformer LLMs into hybrid architectures while preserving short-context quality and improving long-context capability. We call our solution \emph{HyLo} (HYbrid LOng-context): a long-context upcycling recipe that combines architectural adaptation with efficient Transformer blocks, Multi-Head Latent Attention (MLA), and linear blocks (Mamba2 or Gated DeltaNet), together with staged long-context training and teacher-guided distillation for stable optimization. HyLo extends usable context length by up to $32\times$ through efficient post-training and reduces KV-cache memory by more than $90\%$, enabling up to 2M-token prefill and decoding in our \texttt{vLLM} inference stack, while comparable Llama baselines run out of memory beyond 64K context. Across 1B- and 3B-scale settings (Llama- and Qwen-based variants), HyLo delivers consistently strong short- and long-context performance and significantly outperforms state-of-the-art upcycled hybrid baselines on long-context evaluations such as RULER. Notably, at similar scale, HyLo-Qwen-1.7B trained on only 10B tokens significantly outperforms JetNemotron (trained on 400B tokens) on GSM8K, Lm-Harness common sense reasoning and RULER-64K.

---


### 214. [Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://arxiv.org/abs/2604.24763)

**<font color=#1a73e8>作者：</font>** Zhiheng Liu, Weiming Ren, Xiaoke Huang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models typically rely on pretrained vision encoders and use separate visual representations for understanding and generation, creating misalignment between the two tasks and preventing fully end-to-end optimization from raw pixels. We introduce Tuna-2, a native unified multimodal model that performs visual understanding and generation directly based on pixel embeddings. Tuna-2 drastically simplifies the model architecture by employing simple patch embedding layers to encode visual input, completely discarding the modular vision encoder designs such as the VAE or the representation encoder. Experiments show that Tuna-2 achieves state-of-the-art performance in multimodal benchmarks, demonstrating that unified pixel-space modelling can fully compete with latent-space approaches for high-quality image generation. Moreover, while the encoder-based variant converges faster in early pretraining, Tuna-2's encoder-free design achieves stronger multimodal understanding at scale, particularly on tasks requiring fine-grained visual perception. These results show that pretrained vision encoders are not necessary for multimodal modelling, and end-to-end pixel-space learning offers a scalable path toward stronger visual representations for both generation and perception.

---


### 215. [World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://arxiv.org/abs/2604.24764)

**<font color=#1a73e8>作者：</font>** Weijie Wang, Xiaoxuan He, Youping Gu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video foundation models demonstrate impressive visual synthesis but frequently suffer from geometric inconsistencies. While existing methods attempt to inject 3D priors via architectural modifications, they often incur high computational costs and limit scalability. We propose World-R1, a framework that aligns video generation with 3D constraints through reinforcement learning. To facilitate this alignment, we introduce a specialized pure text dataset tailored for world simulation. Utilizing Flow-GRPO, we optimize the model using feedback from pre-trained 3D foundation models and vision-language models to enforce structural coherence without altering the underlying architecture. We further employ a periodic decoupled training strategy to balance rigid geometric consistency with dynamic scene fluidity. Extensive evaluations reveal that our approach significantly enhances 3D consistency while preserving the original visual quality of the foundation model, effectively bridging the gap between video generation and scalable world simulation.

---


> [!TIP]
> 当前位于：**201-215**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-215**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
