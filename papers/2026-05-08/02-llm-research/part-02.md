# 🧠 大模型相关研究 | 2026年05月08日

> 本类共 **126** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-126](./part-03.md)

---

### 51. [RaguTeam at SemEval-2026 Task 8: Meno and Friends in a Judge-Orchestrated LLM Ensemble for Faithful Multi-Turn Response Generation](https://arxiv.org/abs/2605.04523)

**<font color=#1a73e8>作者：</font>** Ivan Bondarenko, Roman Derunets, Oleg Sedukhin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present our winning system for Task~B (generation with reference passages) in SemEval-2026 Task~8: MTRAGEval. Our method is a heterogeneous ensemble of seven LLMs with two prompting variants, where a GPT-4o-mini judge selects the best candidate per instance. We ranked 1st out of 26 teams, achieving a conditioned harmonic mean of 0.7827 and outperforming the strongest baseline (gpt-oss-120b, 0.6390). Ablations show that diversity in model families, scales, and prompting strategies is essential, with the ensemble consistently beating any single model. We also introduce Meno-Lite-0.1, a 7B domain-adapted model with a strong cost--performance trade-off, and analyse MTRAGEval, highlighting annotation limitations and directions for improvement. Our code is publicly available: this https URL

---


### 52. [YOTOnet: Zero-Shot Cross-Domain Fault Diagnosis via Domain-Conditioned Mixture of Experts](https://arxiv.org/abs/2605.04528)

**<font color=#1a73e8>作者：</font>** Zesen Wang, Zihao Wu, Yue Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanical equipment forms the critical backbone of modern industrial production, yet domain shift severely limits the generalization of deep learning based fault diagnosis models across different equipment and operating this http URL by the success of foundation models in achieving zero-shotgeneralization, we propose YOTOnet (You Only Train Once), a novel architecture specifically designed for cross-domain fault diagnosis in mechanical this http URL comprises three core components: (1) a physics-aware Invariant Feature Distiller that extracts domain-agnostic representations using multi-scale dilated convolutions and FFT-based time-frequency fusion,(2) Domain-Conditioned Sparse Experts (DC-MoE) that adaptively route inputs to specialized processors via learned gating without external meta-data, and (3) a dual-head classification system with auxiliary this http URL validation on five public bearing datasets (CWRU, MFPT, XJTU,OTTAWA, HUST) through 30 cross-dataset protocols demonstrates the superiority of YOTOnet compared with other state-of-the-art methods. Critically, we observe a clear scaling effect-average test F1 improves from 0.5339(1 training dataset) to 0.705 (4 datasets), with a clear gain when moving from 3 to 4 datasets. These findings provide empirical evidence that foundation model principles can enable robust, train-once deployment for industrial fault diagnosis.

---


### 53. [Reward-Guided Semantic Evolution for Test-time Adaptive Object Detection](https://arxiv.org/abs/2605.04531)

**<font color=#1a73e8>作者：</font>** Lihua Zhou, Mao Ye, Xiatian Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary object detection with vision-language models (VLMs) such as Grounding DINO suffers from performance degradation under test-time distribution shifts, primarily due to semantic misalignment between text embeddings and shifted visual embeddings of region proposals. While recent test-time adaptive object detection methods for VLM-based either rely on costly backpropagation or bypass semantic misalignment via external memory, none directly and efficiently align text and vision in a training-free manner. To address this, we propose Reward-Guided Semantic Evolution (RGSE), a training-free framework that directly refines the text embeddings at test time. Inspired by evolutionary search, RGSE treats text embedding adaptation as a semantic search process: it perturbs text embeddings as candidate variants, evaluates them via cosine similarity with current and historical high-confidence visual proposals as a reward signal, and fuses them into a refined embedding through reward-weighted averaging. Without any backpropagation, RGSE achieves state-of-the-art performance across multiple detection benchmarks while adding minimal computational overhead. Our code will be open source upon publication.

---


### 54. [Characterizing Students' LLM Usage Behaviors and Their Association with Learning in Critical Thinking Tasks](https://arxiv.org/abs/2605.04534)

**<font color=#1a73e8>作者：</font>** Minju Park, Ivan Orozco Vasquez, Cristina Conati  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are becoming increasingly embedded in students' learning practices, yet much of what is known about how students use LLMs and how this usage impacts learning comes from problem-solving domains or constrained experimental settings. We present an analysis of data on LLM usage collected during two offerings of a research-oriented course where students learn to read, reason about, and critique academic papers. Without restrictions on whether or how to use LLMs, students reported their LLM usage practices when asked to do these activities as a series of homework assignments during the course. This paper extends prior work done on data from a single offering of the same course by presenting a refined bottom-up categorization of LLM usage types, cross-labeled by the extent of student initiative these usages entail. Furthermore, we examine how LLM use impacts student learning, measured by performance on three midterms, looking at factors such as frequency and type of usage.

---


### 55. [RLearner-LLM: Balancing Logical Grounding and Fluency in Large Language Models via Hybrid Direct Preference Optimization](https://arxiv.org/abs/2605.04539)

**<font color=#1a73e8>作者：</font>** Qiming Bao, Juho Leinonen, Paul Denny 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO), the efficient alternative to PPO-based RLHF, falls short on knowledge-intensive generation: standard preference signals from human annotators or LLM judges exhibit a systematic verbosity bias that rewards fluency over logical correctness. This blindspot leaves a logical alignment gap -- SFT models reach NLI entailment of only 0.05-0.22 despite producing fluent text. We propose RLearner-LLM with Hybrid-DPO: an automated preference pipeline that fuses a DeBERTa-v3 NLI signal with a verifier LLM score, removing human annotation while overcoming the "alignment tax" of single-signal optimization. Evaluated across five academic domains (Biology, Medicine, Law) with three base architectures (LLaMA-2-13B, Qwen3-8B, Gemma 4 E4B-it), RLearner-LLM yields up to 6x NLI improvement over SFT, with NLI gains in 11 of 15 cells and consistent answer-coverage gains. On Gemma 4 E4B-it (4.5B effective params), Hybrid-DPO lifts NLI in four of five domains (+11.9% to +2.4x) with faster inference across all five, scaling down to compact base models without losing the alignment-tax mitigation. Our Qwen3-8B RLearner-LLM wins 95% of pairwise comparisons against its own SFT baseline; GPT-4o-mini in turn wins 95% against our concise output -- alongside the 69% win the same judge gives a verbose SFT over our DPO model, this replicates verbosity bias on a frontier comparator and motivates logic-aware metrics (NLI, ACR) over LLM-as-a-judge for knowledge-intensive generation.

---


### 56. [Power Distribution Bridges Sampling, Self-Reward RL, and Self-Distillation](https://arxiv.org/abs/2605.04542)

**<font color=#1a73e8>作者：</font>** Akiyoshi Tomihari, Issei Sato  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent analyses question whether reinforcement learning (RL) is responsible for strong reasoning in large language models (LLMs). At the same time, distillation and inference-time sampling, including power sampling, have emerged as effective ways to improve LLM performance. However, the relationship among RL, distillation, and sampling remains unclear. In this study, we focus on the power distribution, the target distribution of power sampling, and show that the power distribution bridges sampling, self-reward KL-regularized RL, and self-distillation. From the sampling perspective, we show that inexpensive local approximations cannot reproduce sequence-level power without information about possible suffixes. From the RL perspective, the power distribution is the closed-form optimizer of KL-regularized RL when the model's sequence-level log-probabilities are used as the reward. This identification leads to power self-distillation, an offline distillation surrogate that shares the same target distribution and amortizes the cost of power sampling into supervised training on teacher samples. We further show that power self-distillation can achieve self-reward sharpening, while improvement in a downstream true reward is governed by the covariance between true reward and self-reward under the power distribution. Experiments on reasoning tasks support our analysis: power sampling raises self-reward, true-reward gains depend on alignment with self-reward, and power self-distillation can match or exceed the performance of power sampling at much lower inference cost.

---


### 57. [Open-Source Image Editing Models Are Zero-Shot Vision Learners](https://arxiv.org/abs/2605.04566)

**<font color=#1a73e8>作者：</font>** Wei Liu, Jiaxin Lin, Rui Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent studies have shown that large generative models can solve vision tasks they were not explicitly trained for. However, existing evidence relies on closed-source models~(Veo~3, Nano Banana Pro) or requires task-specific instruction tuning, leaving open whether publicly available image-editing models possess zero-shot vision abilities out of the box.
We conduct a systematic evaluation of three open-source image-editing models -- Qwen-Image-Edit, FireRed-Image-Edit, and LongCat-Image-Edit -- on dense visual prediction tasks \emph{without any fine-tuning}. We benchmark monocular depth estimation on NYUv2 and DIODE, surface normal estimation on NYUv2, and semantic segmentation on Cityscapes, covering both geometric and semantic scene understanding.
Results show that open-source image-editing models exhibit non-trivial zero-shot visual understanding. On NYUv2 surface normals, FireRed-Image-Edit achieves a mean angular error of $17.69^\circ$, surpassing the fine-tuned Marigold ($20.86^\circ$) and matching the instruction-tuned Vision Banana ($17.78^\circ$) without any task-specific training. On NYUv2 depth estimation, LongCat-Image-Edit obtains $\delta_1{=}0.822$ with affine alignment, and Qwen-Image-Edit leads on DIODE Indoor ($\delta_1{=}0.868$). On Cityscapes semantic segmentation, Qwen-Image-Edit reaches 25.7 mIoU at the 19-class level and 49.5 mIoU at a coarser 7-category level. By comparing three independently trained editors, we test whether zero-shot vision ability is an emergent property of image-editing pretraining rather than a model-specific artifact. Code, evaluation scripts, and all results are publicly released to serve as a reproducible baseline for future work.

---


### 58. [From Parameter Dynamics to Risk Scoring : Quantifying Sample-Level Safety Degradation in LLM Fine-tuning](https://arxiv.org/abs/2605.04572)

**<font color=#1a73e8>作者：</font>** Xiao Wang, Yifei Zhang, YongKang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment of Large Language Models (LLMs) is extremely fragile, as fine-tuning on a small number of benign samples can erase safety behaviors learned from millions of preference examples. Existing studies attempt to explain this phenomenon by comparing parameters and hidden states before and after fine-tuning, but overlook their dynamic evolution during fine-tuning. In this paper, we uncover a critical mechanism underlying safety degradation by analyzing parameter dynamics, where benign fine-tuning causes parameters to cumulatively drift toward danger-aligned directions, progressively undermining the model's safety. This finding suggests that samples contributing more to this drift has greater fine-tuning risks. Based on this insight, we propose a method of Sample-Level Quantification of Safety Degradation (SQSD), which quantifies the influence of each training sample on safety degradation. Specifically, SQSD computes continuous risk scores to samples by measuring their induced parameter updates' projection difference between danger and safety directions. Extensive experiments across multiple models and datasets demonstrate that SQSD effectively quantifies sample-level fine-tuning risks and exhibits strong transferability across model architectures, parameter scales, and parameter-efficient methods.

---


### 59. [IntenBot: Flexible and Imprecise Multimodal Input for LLMs to Understand User Intentions for Casual and Human-Like HRI](https://arxiv.org/abs/2605.04585)

**<font color=#1a73e8>作者：</font>** Yen-Ting Liu, Chiu-Hsuan Wang, TzuLing Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In natural human-to-human communication, multimodal user input is typically used to supplement explicit and complement implicit voice commands, with casualness allowing for flexible input modality combinations and tolerance for imprecise input data. For example, saying "I want that." with a casual glance at a bottle of water is clear enough in human-to-human communication as an implicit voice command accompanied by gaze and/or gestures, rather than an explicit one. To enable such a human-like interaction in human-robot interaction (HRI), we propose a system, IntenBot, to understand user intentions from flexible and imprecise multimodal input, including voice, gaze, and finger-pointing, in XR. The disambiguation capability of large language models (LLMs) is used to filter out irrelevant input modalities and imprecise input data, generating potential instructions for user confirmation. The flexible and imprecise multimodal input enables casual, human-like interaction with robots, reducing time, effort, and attention, and could also be used as non-voice input. We conducted an informative user behavior study in a simulated environment to understand users' natural be- havior in flexibly interacting with a robot using multimodal input and to obtain appropriate angle range parameters for gaze and finger-pointing. An XR study was then performed to evaluate the performance of IntenBot, compared with other methods. We also deployed IntenBot on a physical robot to showcase its real-world applications.

---


### 60. [A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints](https://arxiv.org/abs/2605.04595)

**<font color=#1a73e8>作者：</font>** Chengyi Nie, Nian Si, Zijie Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of large language models (LLMs) has created significant challenges for efficient inference at scale. Unlike traditional workloads, LLM inference is constrained by both computation and the memory overhead of key-value (KV) caching, which accelerates decoding but quickly exhausts GPU memory. In this paper, we introduce the first queueing-theoretic framework that explicitly incorporates both computation and GPU memory constraints into the analysis of LLM inference. Based on this framework, we derive rigorous stability and instability conditions that determine whether an LLM inference service can sustain incoming demand without unbounded queue growth. This result offers a powerful tool for system deployment, potentially addressing the core challenge of GPU provisioning. By combining an estimated request arrival rate with our derived stable service rate, operators can calculate the necessary cluster size to avoid both costly over-purchasing and performance-violating under-provisioning. We further validate our theoretical predictions through extensive experiments in real GPU production environments. Our results show that the predicted stability conditions are highly accurate, with deviations typically within 10%.

---


### 61. [Advancing Aesthetic Image Generation via Composition Transfer](https://arxiv.org/abs/2605.04609)

**<font color=#1a73e8>作者：</font>** Kai Zou, Zhiwei Zhao, Bin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composition is a cornerstone of visual aesthetics, influencing the appeal of an image. While its principles operate independently of specific content, in practice, composition is often coupled with semantics. As a result, existing methods often enhance composition either through implicit learning or by semantics-based layout control, rather than explicitly modeling composition itself. To address this gap, we introduce Composer, a framework rooted in aesthetic theory, designed to model composition in a semantic-agnostic manner. First, it supports composition transfer by extracting key composition-aware representations from a reference image and leveraging a tailored conditional guidance module to control composition based on pre-trained diffusion models. Second, when users specify only text themes without a composition reference, Composer supports theme-driven composition retrieval by leveraging the in-context learning capabilities of Large Vision-Language Models (LVLMs), achieving explicit composition planning. To enhance composition in a reference-free mode, we conduct text-to-composition fine-tuning on the trained control module to enable implicit composition planning. Furthermore, we curated a high-quality dataset comprising 2 million image-text pairs using state-of-the-art generative models to support model training. Experimental results demonstrate that Composer significantly enhances aesthetic quality in text-to-image tasks and facilitates personalized composition control and transfer, offering users precision and flexibility in the creative process.

---


### 62. [Gradients with Respect to Semantics Preserving Embeddings Tell the Uncertainty of Large Language Models](https://arxiv.org/abs/2605.04638)

**<font color=#1a73e8>作者：</font>** Mingda Li, Rundong Lv, Xinyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification (UQ) is an important technique for ensuring the trustworthiness of LLMs, given their tendency to hallucinate. Existing state-of-the-art UQ approaches for free-form generation rely heavily on sampling, which incurs high computational cost and variance. In this work, we propose the first gradient-based UQ method for free-form generation, SemGrad, which is sampling-free and computationally efficient. Unlike prior gradient-based methods developed for classification tasks that operates in parameter space, we propose to consider gradients in semantic space. Our method builds on the key intuition that a confident LLM should maintain stable output distributions under semantically equivalent input perturbations. We interpret the stability as the gradients in semantic space and introduce a Semantic Preservation Score (SPS) to identify embeddings that best capture semantics, with respect to which gradients are computed. We further propose HybridGrad, which combines the strengths of SemGrad and parameter gradients. Experiments demonstrate that both of our methods provide efficient and effective uncertainty estimates, achieving superior performance than state-of-the-art methods, particularly in settings with multiple valid responses.

---


### 63. [Cognitive Alignment Drives Attention: Modeling and Supporting Socially Shared Regulation in Pair Programming](https://arxiv.org/abs/2605.04639)

**<font color=#1a73e8>作者：</font>** Anahita Golrang, Kshitij Sharma  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Grounded in socially shared regulation of learning (SSRL), this paper investigates how joint mental effort (JME) and joint visual attention (JVA) serve as process-level indicators of shared regulation in pair programming and how AI-driven adaptive feedback can strengthen these processes.
We present three eye-tracking studies involving 182 dyads engaged in collaborative debugging tasks. Study 1 examines natural collaboration and shows that high-performing dyads exhibit significantly higher JME and JVA, a greater prevalence of productive high-JME-high-JVA episodes, and a stable causal relationship in which JME predicts JVA. Study 2 evaluates reactive adaptive feedback based on real-time deviations in JME and/or JVA. Results show that combined feedback targeting both dimensions yields the strongest improvements in performance, regulatory coherence, and cognitive-to-attentional causality, outperforming single-channel feedback. Study 3 introduces proactive, forecast-based feedback using machine-learning predictions of future collaboration states. Proactive support further enhances performance and sustains shared regulation by anticipating breakdowns before they manifest.
Across studies, causal modeling reveals that cognitive alignment systematically drives attentional coordination in successful collaboration, while mismatches between effort and attention characterize unproductive regulation. Methodologically, this work integrates dual eye-tracking, pupillometry, episode-based analysis, and causal inference to capture SSRL as a dynamic, emergent process. Conceptually, the findings position AI not as an automated controller, but as an intelligence-augmenting co-regulator that supports learners' capacity to coordinate effort, attention, and understanding together.

---


### 64. [CAST: Mitigating Object Hallucination in Large Vision-Language Models via Caption-Guided Visual Attention Steering](https://arxiv.org/abs/2605.04641)

**<font color=#1a73e8>作者：</font>** Qiming Li, Zekai Ye, Xiaocheng Feng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although Large Vision-Language Models (LVLMs) have demonstrated remarkable performance on downstream tasks, they frequently produce contents that deviate from visual information, leading to object hallucination. To tackle this, recent works mostly depend on expensive manual annotations and training cost, or decoding strategies which significantly increase inference time. In this work, we observe that LVLMs' attention to visual information is significantly enhanced when answering caption queries compared to non-caption queries. Inspired by this phenomenon, we propose Caption-guided Visual Attention Steering (CAST), a training-free, plug-and-play hallucination mitigation method that leverages the attention activation pattern corresponding to caption queries to enhance LVLMs' visual perception capability. Specifically, we use probing techniques to identify attention heads that are highly sensitive to caption queries and estimate optimized steering directions for their outputs. This steering strengthens LVLM's fine-grained visual perception capabilities, thereby effectively mitigating object hallucination. CAST reduced object hallucination by an average of 6.03% across five widely used LVLMs and five benchmarks including both discriminative and generative tasks, demonstrating state-of-the-art performance while adding little inference cost and preserving other foundational capabilities.

---


### 65. [Graph-Augmented LLMs for Swiss MP Ideology Prediction](https://arxiv.org/abs/2605.04643)

**<font color=#1a73e8>作者：</font>** Yifei Yuan, Luis Salamanca, Sophia Schlosser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Approximating the ideological position of Members of Parliament (MPs) is a fundamental task in political science, helping researchers understand legislative behavior, party alignment, and policy preferences. While Large Language Models (LLMs) have shown promising results in estimating MPs' ideological stances, there are more actors and elements in the parliamentary system, and relations between them, that could provide a wider and more informative picture. However, due to the complexity of integrating them in the prediction task, these additional elements are generally ignored. In this work, we propose an LLM framework, PG-RAG, that implements a retrieval-augmented generation pipeline: it first queries a political knowledge graph (KG) and then integrates the resulting graph-structured information into the context. This allows for capturing both textual semantics and inter-MP relationships, another relevant information source in any parliamentary system. We evaluate the approach on the task of ideology prediction, using data from a Swiss parliamentary dataset. When comparing graph-augmented models against several state-of-the-art baselines, the results demonstrate that incorporating this enriched information, which encodes information about different entities and relations, improves prediction performance. These results help to highlight the value of domain-specific relational information in modeling political behavior.

---


### 66. [Paraphrase-Induced Output-Mode Collapse: When LLMs Break Character Under Semantically Equivalent Inputs](https://arxiv.org/abs/2605.04665)

**<font color=#1a73e8>作者：</font>** Aofan Liu, Jingxiang Meng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When the substantive content of a request is rewritten, do large language models still answer in the format the original task asked for? We find that they often do not, even at temperature zero. On a 150-query evaluation over five compact 2025-era LLMs and four task types, we observe a systematic failure mode we call prompt-variant output-mode collapse: when a closed-form prompt asks for a bare label or a single choice token, content-preserving prompt variants can push the model into conversational prose, the requested format dissolves, and exact-match evaluation pipelines silently misjudge the result. To make this measurable, we release PARACONSIST, a 900-prompt benchmark of 150 base queries with five lexical, syntactic, and semantic-expansion prompt variants each, and a Semantic Consistency Score that decomposes prompt-variant robustness into answer consistency, sentence-BERT semantic similarity, and length stability. Under a whole-word answer-set match, only ~22% of closed-form variant responses preserve the ground-truth label inside their output, while ~78% drift away from the answer space entirely. In our pool, the dominant predictor of collapse is task structure rather than model identity, with model differentiation jointly carried by answer consistency and length stability. Robustness audits should therefore track response-mode preservation as a first-class reliability target alongside answer accuracy.

---


### 67. [AISSA: Implementation and Deployment of an AI-based Student Slides Analysis tool for Academic Presentations](https://arxiv.org/abs/2605.04729)

**<font color=#1a73e8>作者：</font>** Alvaro Becerra, Diego Gomez, Ruth Cobos  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Providing timely and actionable feedback on oral presentation slides is challenging in higher education, particularly in large classes where teachers cannot realistically deliver detailed formative feedback before students present. This paper introduces AISSA (AI-based Student Slides Analysis tool), a web-based system that combines large language models (LLMs) and Learning Analytics dashboards to support scalable, rubric-based feedback on presentation slides. AISSA allows students to upload their slide decks prior to an oral presentation and automatically receive quantitative scores and qualitative feedback based on teacher-defined evaluation rubrics. The system analyzes both slide-level features and slide content, generates structured feedback through an LLM (ChatGPT 5.2), and presents the results through interactive dashboards for students and teachers. We tested AISSA on a pilot deployment with 46 undergraduate students in a real academic setting. The results indicate that AISSA is technically reliable, economically feasible, and perceived by students as useful for iterative slide improvement. These findings suggest that combining LLM-based analysis with Learning Analytics dashboards is a promising approach for supporting formative feedback on presentation slides at scale.

---


### 68. [Reward-Decomposed Reinforcement Learning for Immersive Video Role-Playing](https://arxiv.org/abs/2605.04733)

**<font color=#1a73e8>作者：</font>** Miao Wang, Yuling Shi, Yijiang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-based role-playing models can imitate character styles, yet they often fail to reflect a scene's atmosphere and evolving tension, both essential for immersive applications such as Virtual Reality (VR) games and interactive narratives. We study video-grounded role-playing dialogue and introduce EBM-RL (Eye-Brain-Mouth Reinforcement Learning), a decoupled GRPO-based framework that explicitly separates observation ([perception]), reasoning ([think]), and utterance ([answer]). This structure promotes human-like sensory grounding by compelling the model to first attend to visual cues, then form internal interpretations, and finally generate context-appropriate dialogue.
EBM-RL integrates four complementary rewards: (i) CLIP-based scene-text alignment to improve ambiance and emotion; (ii) a Perceptual-Cognitive reward that encourages [perception] and [think] processes that increase the likelihood of the reference response; (iii) answer accuracy to ensure faithfulness; and (iv) a dense format reward to enforce the desired structured output.
Extensive experiments demonstrate that EBM-RL substantially outperforms text-only role-playing baselines and larger-scale vision-language models on our immersive role-playing benchmark, delivering simultaneous gains in visual-atmosphere consistency and character authenticity. Beyond the role-playing domain, EBM-RL also exhibits strong zero-shot generalization: without any additional fine-tuning, it consistently improves performance on out-of-domain VideoQA benchmarks. We additionally release an open-source dataset for video-grounded role-playing dialogue.

---


### 69. [OSAQ: Outlier Self-Absorption for Accurate Low-bit LLM Quantization](https://arxiv.org/abs/2605.04738)

**<font color=#1a73e8>作者：</font>** Zhikai Li, Zhen Dong, Xuewen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities. However, their massive parameter scale leads to significant resource consumption and latency during inference. Post-training weight-only quantization offers a promising solution by reducing model size and accelerating token generation through alleviating the memory-bound issue. Nevertheless, the presence of inherent systematic outliers in weights continues to be a major obstacle. While existing methods, such as scaling and rotation, attempt to address this issue, the performance remains unsatisfactory. In this paper, we propose Outlier Self-Absorption Quantization (OSAQ), which performs additive weight suppression guided by the second-order low-rank property for low-bit weight-only quantization of LLMs. Specifically, we observe that the Hessian exhibits low-rank consistency across different inputs, with certain directions consistently showing vanishing curvature. Leveraging this property, we identify a stable null space of the Hessian and then construct an additive weight transformation by linearly combining the vectors within this null space, thereby suppressing weight outliers without affecting the task loss. This additive transformation can be absorbed into the weights offline, requiring no inter-layer transformations and introducing no inference overhead. Moreover, the construction is efficiently achieved by a closed-form solution, without resource-intensive training or iterative procedures. Extensive experiments demonstrate that OSAQ effectively suppresses outliers and enhances low-bit quantization performance. For instance, in 2-bit quantization, OSAQ, when integrated with GPTQ, achieves over 40% lower perplexity compared to vanilla GPTQ.

---


### 70. [AICoFe: Implementation and Deployment of an AI-Based Collaborative Feedback System for Higher Education](https://arxiv.org/abs/2605.04740)

**<font color=#1a73e8>作者：</font>** Alvaro Becerra, Alejandra Palma, Ruth Cobos  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective peer feedback is essential for developing critical reflection in higher education, yet its impact is often limited by the inconsistent quality of student-generated comments. This paper presents the implementation and deployment of AICoFe (AI-based Collaborative Feedback), a system designed to bridge this gap through a human-centered AI approach. We describe a modular architecture that orchestrates a multi-LLM pipeline, utilizing GPT-4.1-mini, Gemini 2.5 Flash, and Llama 3.1, to synthesize quantitative rubric data and qualitative observations into coherent, actionable feedback. Key to the system is a "teacher-in-the-loop" mediation workflow, where educators use specialized Learning Analytics dashboards to curate and refine AI-generated drafts before delivery. Furthermore, we detail the underlying data infrastructure, which employs a hybrid SQL and MongoDB strategy to ensure traceability and manage semi-structured feedback versions.

---


### 71. [AxMoE: Characterizing the Impact of Approximate Multipliers on Mixture-of-Experts DNN Architectures](https://arxiv.org/abs/2605.04754)

**<font color=#1a73e8>作者：</font>** Omkar B Shende, Marcello Traiola, Gayathri Ananthanarayanan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural network (DNN) inference at the edge demands simultaneous improvements in accuracy, computational efficiency, and energy consumption. Approximate computing and Mixture-of-Experts (MoE) architectures have each been studied as independent routes towards efficient inference, the former by replacing exact arithmetic with low-power approximate multipliers, the latter by routing inputs through specialized expert sub-networks to enable conditional computation. However, their interaction remains entirely unexplored. This paper presents AxMoE, the first study of the impact of approximate multiplication on MoE DNN architectures. We evaluate three MoE variants: Hard MoE, Soft MoE, and Cluster MoE against dense baselines across three CNN architectures (ResNet-20, VGG11_bn, VGG19_bn) on CIFAR-100 and a Vision Transformer (ViT-Small) on Tiny ImageNet-200 dataset, using eight 8-bit signed multipliers (including one exact baseline) from the EvoApproxLib library. Results show that, without retraining, the Dense baseline is the most resilient topology across all CNN architectures, whereas on ViT-Small, all topologies degrade at comparable rates regardless of routing strategy. After approximate-aware retraining, recovery varies substantially across architectures, topologies, and multipliers. ResNet-20 achieves full recovery across the entire multiplier range, whereas VGG architectures recover at moderate multipliers but fail irreversibly at aggressive ones for all topologies except Cluster MoE on VGG11_bn; on ViT-Small, Hard MoE outperforms Dense under aggressive approximation at equal normalized inference cost. These results pave the way for future approximate MoE hardware-software co-design strategies.

---


### 72. [Gyan: An Explainable Neuro-Symbolic Language Model](https://arxiv.org/abs/2605.04759)

**<font color=#1a73e8>作者：</font>** Venkat Srinivasan, Vishaal Jatav, Anushka Chandrababu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer based pre-trained large language models have become ubiquitous. There is increasing evidence to suggest that even with large scale pre-training, these models do not capture complete compositional context and certainly not, the full human analogous context. Besides, by the very nature of the architecture, these models hallucinate, are difficult to maintain, are not easily interpretable and require enormous compute resources for training and inference. Here, we describe Gyan, an explainable language model based on a novel non-transformer architecture, without any of these limitations. Gyan achieves SOTA performance on 3 widely cited data sets and superior performance on two proprietary data sets. The novel architecture decouples the language model from knowledge acquisition and representation. The model draws on rhetorical structure theory, semantic role theory and knowledge-based computational linguistics. Gyan's meaning representation structure captures the complete compositional context and attempts to mimic humans by expanding the context to a 'world model'. AI model adoption critically depends on trust and transparency especially in mission critical use cases. Collectively, our results demonstrate that it is possible to create models which are trustable and reliable for mission critical tasks. We believe our work has tremendous potential for guiding the development of transparent and trusted architectures for language models.

---


### 73. [Cognitive Twins: Investigating Personalized Thinking Model Building and Its Performance Enhancement with Human-in-the-Loop](https://arxiv.org/abs/2605.04761)

**<font color=#1a73e8>作者：</font>** Wu-Yuin Hwang, Nur Alif Ilyasa, Muhammad Irfan Luthfi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents the Personalized Thinking Model (PTM), a hierarchical and interpretable learner representation designed for AI supported education. PTM organizes evidence from learner journals into a five-layer structure covering behavioral instances, behavioral patterns, cognitive routines, metacognitive tendencies, and self-system values. PTM is grounded in Marzano's New Taxonomy of Educational Objectives and tries to clone learner's thinking model and build cognitive twin. It was constructed using a pipeline that combines large language model inference (Gemini 2.5 Pro), sentence embeddings, dimensionality reduction, and consensus clustering. This paper evaluates PTM fidelity through three methods applied to 40 participants in a seven-week study. First, automatic evaluation using atomic information point matching yielded an overall F1 score of 74.57% before human-in-the-loop (HITL) refinement and 75.48% after refinement. Second, user evaluation using a Likert scale produced mean ratings of 4.26 and 4.30 on a five-point scale for pre and post-HITL conditions respectively. Third, semantic alignment verification showed that topic coherence increased from 0.436 at the behavioral layer to 0.626 at the core value layer, while lexical overlap with journal vocabulary decreased from 0.114 to 0.007 across those same layers. These results suggest that the PTM produces outputs with acceptable fidelity, was generally perceived by users as reflecting their thinking, and showed a pattern consistent with semantic abstraction across layers.

---


### 74. [Elicitation Matters: How Prompts and Query Protocols Shape LLM Surrogates under Sparse Observations](https://arxiv.org/abs/2605.04764)

**<font color=#1a73e8>作者：</font>** Ge Lei, Samuel J. Cooper  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as surrogate models for low-data optimization, but their optimizer-facing prediction and its uncertainty remain poorly understood. We study the surrogate belief elicited from an LLM under sparse observations, showing that it depends strongly on prompt text and query protocol. We introduce an uncertainty-alignment criterion that measures whether model uncertainty tracks residual ambiguity among sample-consistent functions. Across controlled inference tasks and Bayesian optimization studies, we find that structural prompts act as effective priors, POINTWISE and JOINT querying induce different beliefs, and sequential evidence leads to non-monotonic, order-sensitive confidence updates. These effects change downstream acquisition decisions and regret, showing that elicitation protocol is part of the LLM surrogate specification, not a formatting detail.

---


### 75. [Lightweight Cross-Spectral Face Recognition via Contrastive Alignment and Distillation](https://arxiv.org/abs/2605.04769)

**<font color=#1a73e8>作者：</font>** Anjith George, Sebastien Marcel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Heterogeneous Face Recognition (HFR) aims at matching face images captured across different sensing modalities, such as thermal-to-visible or near-infrared-to-visible, enhancing the usability of face recognition systems in challenging real-world conditions. Although recent HFR methods have achieved significant improvements in performance, many rely on computationally expensive models, making them impractical for deployment on resource-limited edge devices. In this work, we introduce a lightweight yet effective HFR framework by adapting a hybrid CNN-Transformer model originally developed for RGB homogeneous face recognition. Our approach enables efficient end-to-end training with only a small amount of paired heterogeneous data, while still maintaining strong performance on standard RGB face recognition benchmarks. This makes it suitable for both homogeneous and heterogeneous settings. Comprehensive experiments on several challenging HFR and face recognition benchmarks show that our method achieves state-of-the-art or competitive performance while keeping computational requirements low.

---


### 76. [MIRAGE: Retrieval and Generation of Multimodal Images and Texts for Medical Education](https://arxiv.org/abs/2605.04772)

**<font color=#1a73e8>作者：</font>** Miguel Diaz Benito, Cecilia Diana Albelda, Alvaro Garcia Martin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Access to diverse, well-annotated medical images with interactive learning tools is fundamental for training practitioners in medicine and related fields to improve their diagnostic skills and understanding of anatomical structures. While medical atlases are valuable, they are often impractical due to their size and lack of interactivity, whereas online image search may provide mislabeled or incomplete material. To address this, we propose MIRAGE, a multimodal medical text and image retrieval and generation system that allows users to find and generate clinically relevant images from trustworthy sources by mapping both text and images to a shared latent space, enabling semantically meaningful queries. The system is based on a fine-tuned medical version of CLIP (MedICaT-ROCO), trained with the ROCO dataset, obtained from PubMed Central. MIRAGE allows users to give prompts to retrieve images, generate synthetic ones through a medical diffusion model (Prompt2MedImage) and receive enriched descriptions from a large language model (Dolly-v2-3b). It also supports a dual search option, enabling the visual comparison of different medical conditions. A key advantage of the system is that it relies entirely on publicly available pretrained models, ensuring reproducibility and accessibility. Our goal is to provide a free, transparent and easy-to-use didactic tool for medical students, especially those without programming skills. The system features an interface that enables interactive and personalized visual learning through medical image retrieval and generation. The system is accessible to medical students worldwide without requiring local computational resources or technical expertise, and is currently deployed on Kaggle: this http URL

---


### 77. [Bridging Perception and Action: A Lightweight Multimodal Meta-Planner Framework for Robust Earth Observation Agents](https://arxiv.org/abs/2605.04777)

**<font color=#1a73e8>作者：</font>** Jinghui Xu, Boyi Shangguan, Mengke Zhu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous Earth Observation (EO) agents are transitioning from passive perception to complex, multi-step task execution. However, current architectures that integrate planning and execution within a single model often struggle with combinatorial complexity and reasoning errors in dynamic EO scenarios. To resolve these challenges, we propose the Lightweight Multimodal Meta-Planner (LMMP) framework. LMMP incorporates a dual-awareness mechanism that grounds strategic plans in both multimodal image features and high-level task semantics. Crucially, we introduce a Meta Task Library to inject remote sensing expert knowledge directly into the workflow, which standardizes domain logic and ensures plans are physically feasible. We further implement a two-stage training pipeline, initializing the Meta-Planner via expert-distilled Supervised Fine-Tuning and refining it through Direct Preference Optimization based on execution feedback. Extensive experiments on a dataset derived from EarthBench and ThinkGeo demonstrate that LMMP significantly improves tool-calling accuracy and task success rates. Moreover, the framework exhibits strong ``plug-and-play'' versatility, consistently enhancing the performance of diverse executor backbones across previously unseen EO missions.

---


### 78. [AgentTrust: Runtime Safety Evaluation and Interception for AI Agent Tool Use](https://arxiv.org/abs/2605.04785)

**<font color=#1a73e8>作者：</font>** Chenglin Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern AI agents execute real-world side effects through tool calls such as file operations, shell commands, HTTP requests, and database queries. A single unsafe action, including accidental deletion, credential exposure, or data exfiltration, can cause irreversible harm. Existing defenses are incomplete: post-hoc benchmarks measure behavior after execution, static guardrails miss obfuscation and multi-step context, and infrastructure sandboxes constrain where code runs without understanding what an action means.
We present AgentTrust, a runtime safety layer that intercepts agent tool calls before execution and returns a structured verdict: allow, warn, block, or review. AgentTrust combines a shell deobfuscation normalizer, SafeFix suggestions for safer alternatives, RiskChain detection for multi-step attack chains, and a cache-aware LLM-as-Judge for ambiguous inputs.
We release a 300-scenario benchmark across six risk categories and an additional 630 independently constructed real-world adversarial scenarios. On the internal benchmark, the production-only ruleset achieves 95.0% verdict accuracy and 73.7% risk-level accuracy at low-millisecond end-to-end latency. On the 630-scenario benchmark, evaluated under a patched ruleset and not claimed as zero-shot, AgentTrust achieves 96.7% verdict accuracy, including about 93% on shell-obfuscated payloads. AgentTrust is released under the AGPL-3.0 license and provides a Model Context Protocol server for MCP-compatible agents.

---


### 79. [OpenWatch: A Multimodal Benchmark for Hand Gesture Recognition on Smartwatches](https://arxiv.org/abs/2605.04791)

**<font color=#1a73e8>作者：</font>** Pietro Bonazzi, Youssef Ahmed, Daniel Eckert 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite widespread adoption of smartwatches worldwide, open-benchmarks for wrist-based gesture recognition remain surprisingly limited. In this work, we intro- duce the first open-access multi-modal benchmark, OpenWatch, for wrist-based gesture recognition using synchronized inertial and physiological sensing on a com- mercial smartwatch. It contains over 10 hours of Inertial Measurement Unit (IMU) and Photoplethysmography (PPG) data across 50 participants and a vocabulary of 59 labelled gesture sequences. Furthermore, we present a subject-independent evaluation protocol including traditional and deep learning methods for time-series classification. On top of this, we develop two novel methodologies for hand-gesture recognition: (i) MixToken, a task-specific mixture-of-experts that fuses per-channel IMU filterbank features with cross-channel statistical tokens through learned logit mixing, and (ii) NormWear-Lora, a low-rank adaptation module for smartwatch foundation models. Our benchmarking results reveal that PPG signals carries a sub- stantial predictive benefit (+12.5% F1-score) for foundational smartwatch models. In addition, we show that task-specific architectures (i.e. MixToken) substantially outperforms finetuned smartwatch foundation models in terms of accuracy (F1- score=90% vs 66%) and memory efficiency (223k vs 136M parameters). Finally, we also provide clear empirical guidance on the trade-offs between specialized architecture design, modality fusion, data augmentations, and foundation-model adaptation for resource-constrained wearable sensing.

---


### 80. [Improving FMQA via Initial Training Data Design Considering Marginal Bit Coverage in One-Hot Encoding](https://arxiv.org/abs/2605.04825)

**<font color=#1a73e8>作者：</font>** Taiga Hayashi, Yuya Seki, Kotaro Terada 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Factorization machine with quadratic-optimization annealing (FMQA) is a black-box optimization method that combines a factorization machine (FM) surrogate with QUBO-based search by an Ising machine. When FMQA is applied to integer or discretized continuous variables via one-hot encoding, uniform random initial sampling can leave many binary variables never active in the initial training data, and the corresponding FM parameters receive no direct gradient updates from the observed responses. We address this by designing the initial training data to achieve complete marginal bit coverage, namely, ensuring that every binary variable obtained by one-hot encoding takes the value one at least once. We use two space-filling sampling methods, Latin hypercube sampling (LHS) and the Sobol' sequence, yielding LHS-FMQA and Sobol'-FMQA. On the human-powered aircraft wing-shape optimization benchmark with 17 and 32 design variables, both proposed methods achieved numerically higher mean final cruising speeds than the baseline FMQA, with the advantage more pronounced on the 32-variable problem.

---


### 81. [Bridging Input Feature Spaces Towards Graph Foundation Models](https://arxiv.org/abs/2605.04834)

**<font color=#1a73e8>作者：</font>** Moshe Eliasof, Krishna Sri Ipsit Mantri, Beatrice Bevilacqua 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlike vision and language domains, graph learning lacks a shared input space, as input features differ across graph datasets not only in semantics, but also in value ranges and dimensionality. This misalignment prevents graph models from generalizing across datasets, limiting their use as foundation models. In this work, we propose ALL-IN, a simple and theoretically grounded method that enables transferability across datasets with different input features. Our approach projects node features into a shared random space and constructs representations via covariance-based statistics, thus eliminating dependence on the original feature space. We show that the computed node-covariance operators and the resulting node representations are invariant in distribution to permutations of the input features. We further demonstrate that the expected operator exhibits invariance to general orthogonal transformations of the input features. Empirically, ALL-IN achieves strong performance across diverse node- and graph-level tasks on unseen datasets with new input features, without requiring architecture changes or retraining. These results point to a promising direction for input-agnostic, transferable graph models.

---


### 82. [RTMS: A Real-Time Multimodal Scaffolding System for Improving Debugging in Computing Education](https://arxiv.org/abs/2605.04848)

**<font color=#1a73e8>作者：</font>** Anahita Golrang, Kshitij Sharma  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Debugging is a demanding aspect of programming yet guidance on how to teach it effectively remains limited. Novices often struggle to recognize impasses regulate their problem solving and manage cognitive load and stress. This study investigates whether real time multimodal feedback triggered by indicators of cognitive load and physiological stress can improve debugging performance narrow expert novice gaps and reduce the influence of prior programming experience on success. We conducted a between subjects experiment with 120 undergraduate computer science students who debugged a medium sized Python program. Participants were assigned to one of four conditions no feedback cognitive load triggered feedback stress triggered feedback or combined trigger feedback. Eye tracking and heart rate variability data were used to detect moments of struggle and automatically deliver brief context sensitive hints. All three feedback conditions significantly improved debugging success and efficiency compared with the control group. Cognitive load triggered feedback produced stronger gains than stress triggered feedback and the combined trigger condition yielded the largest improvements. Programming expertise predicted performance only in the control condition and in all feedback conditions the novice expert gap was markedly reduced. Adaptive feedback that responds to learners cognitive and affective states can help manage debugging demands and reduce performance differences linked to prior experience highlighting opportunities for physiologically aware adaptive learning environments.

---


### 83. [VTAgent: Agentic Keyframe Anchoring for Evidence-Aware Video TextVQA](https://arxiv.org/abs/2605.04870)

**<font color=#1a73e8>作者：</font>** Haibin He, Maoyuan Ye, Jing Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video text-based visual question answering (Video TextVQA) aims to answer questions by reasoning over visual textual content appearing in videos. Despite the strong multimodal video understanding capabilities of recent Video-LLMs, their performance on existing Video TextVQA benchmarks remains limited. To better understand this gap, we conduct an upper-bound analysis through frame-wise question answering, counting a sample as correct if any frame yields the right answer, which significantly outperforms direct video-based inference and reveals a substantial performance gap. The results suggest that the primary bottleneck lies in the localization of key question-relevant evidence, rather than in reasoning capacity itself. Building on this insight, we propose a question-guided agent framework that explicitly anchors the relevant keyframes before answering. The approach operates effectively in a training-free setting and consistently surpasses direct video inference. With additional supervised fine-tuning (SFT) and reinforcement learning (RL), it achieves an average improvement of +12.12 in accuracy and +11.15 in ANLS across benchmarks, establishing new state-of-the-art results. Our study underscores the critical role of explicit keyframe anchoring for advancing Video TextVQA. The code will be publicly released.

---


### 84. [Uncertainty-Aware Exploratory Direct Preference Optimization for Multimodal Large Language Models](https://arxiv.org/abs/2605.04874)

**<font color=#1a73e8>作者：</font>** Huatian Zhang, Zhendong Mao, Lei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) has proven to be an effective solution for mitigating hallucination in Multimodal Large Language Models (MLLMs) by learning from preference pairs. One of its key challenges lies in how to transfer the sequence-level preference into fine-grained supervision on visual fidelity. To safeguard vision-related tokens that are prone to hallucination, existing methods typically allocate training emphasis according to the model's self-assessed visual sensitivity signals. However, such sensitivity, estimated by a model still under training, introduces self-referential bias: reinforcing already well-learned visual cues while neglecting hard-to-perceive but critical details, thereby limiting deeper alignment. In this work, we propose an Uncertainty-aware Exploratory Direct Preference Optimization (UE-DPO) method for MLLMs, which enables the model to uncover its cognitive deficiencies and actively explore for self-correction, guided by token-level epistemic uncertainty. Specifically, we first quantify the uncertainty from the model's failure to ground token predictions in the given image. Then, based on an uncertainty-aware exploration intensity, we encourage more learning pressure on visually deficient tokens in preferred samples, and alleviate the over-penalization of beneficial knowledge in dispreferred samples. Further, we provide a theoretical justification for our method, and extensive experiments demonstrate its effectiveness and robustness.

---


### 85. [Anticipating Innovation Using Large Language Models](https://arxiv.org/abs/2605.04875)

**<font color=#1a73e8>作者：</font>** Enrico Maria Fenoaltea, Filippo Santoro, Giordano De Marzo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Forecasting innovation, intended as the emergence of new technological combinations, is a fundamental challenge for science and policy. We show that forthcoming combinations leave an early trace in the collective language of patents, with predictive signals detectable even decades in advance. We show that signal is not attributable to any single inventor, but emerges as a collective shift in how technologies are described across thousands of patents. To this end, we introduce TechToken, a transformer-based model that treats technologies, classified by International Patent Classification codes, as words in its vocabulary, learning the language of technologies by embedding these codes during fine-tuning. We define context similarity between code embeddings as a measure of linguistic convergence and show that it accurately predicts first technological combinations. TechToken also improves general representation quality, outperforming state-of-the-art models across different patent-related tasks.

---


### 86. [A Harmonic Mean Formulation of Average Reward Reinforcement Learning in SMDPs](https://arxiv.org/abs/2605.04880)

**<font color=#1a73e8>作者：</font>** Erel Shtossel, Alicia Vidler, Uri Shaham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent research has revived and amplified interest in algorithms for undiscounted average reward reinforcement learning in infinite-horizon, non-episodic (continuing) tasks. Semi-Markov decision processes (SMDPs) are of particular interest. In SMDPs, discrete actions stochastically generate both rewards and durations, and the objective is to optimize the average reward rate. Existing algorithms approach this by optimizing the ratio of rewards to durations. However, when rewards and durations are non-stationary (in the infinite horizon), this can be incorrect. This paper presents a novel modified harmonic mean operator that correctly computes reward rates even under such conditions. This yields model-free learning algorithms that can work with SMDPs, while maintaining robustness to non-stationary reward and duration distributions over time. We prove theoretical properties of the modified harmonic mean operator, and empirically demonstrate its efficacy in comparison to existing algorithms.

---


### 87. [FairEnc: A Fair Vision-Language Model with Fair Vision and Text Encoders for Glaucoma Detection](https://arxiv.org/abs/2605.04882)

**<font color=#1a73e8>作者：</font>** Mohamed Elhabebe, Ayman El-Baz, Qing Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated glaucoma detection is critical for preventing irreversible vision loss and reducing the burden on healthcare systems. However, ensuring fairness across diverse patient populations remains a significant challenge. In this paper, we propose FairEnc, a fair pretraining method for vision-language models (VLMs) that enables simultaneous debiasing across multiple sensitive attributes. FairEnc jointly mitigates biases in both textual and visual modalities with respect to multiple sensitive attributes, including race, gender, ethnicity, and language. Specifically, for the textual encoder, we leverage a large language model to generate synthetic clinical descriptions with varied sensitive attributes while preserving disease semantics, and employ a contrastive alignment objective to encourage demographic-invariant representations. For the visual encoder, we propose a dual-level fairness strategy that combines mutual information regularization to reduce statistical dependence between learned features and demographic groups, with multi-discriminator adversarial debiasing. Comprehensive experiments on the publicly available Harvard-FairVLMed dataset demonstrate that FairEnc effectively reduces demographic disparity as measured by DPD and DEOdds while achieving strong diagnostic performance under both zero-shot and linear probing evaluations. Additional experiments on the private FairFundus dataset show that FairEnc consistently preserves fairness advantages under cross-domain and cross-modality settings and maintains diagnostic performance within a competitive range. These results highlight FairEnc's ability to generalize fairness under distribution shifts, supporting its potential for more equitable deployment in real-world clinical settings. Our codebase and synthetic clinical notes are available at this https URL

---


### 88. [BenCSSmark: Making the Social Sciences Count in LLM Research](https://arxiv.org/abs/2605.04886)

**<font color=#1a73e8>作者：</font>** Arnault Chatelain, Étienne Ollion, Qianwen Guan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This position paper argues that the under-representation of social science tasks in contemporary LLM benchmarks limits advances in both LLM evaluation and social scientific inquiry. Benchmarks -- standardized tools for assessing computational systems -- are pivotal in the development of artificial intelligence (AI), including large language models (LLMs). Benchmarks do more than measure progress -- they actively structure it, shaping reputations, research agendas, and commercial outcomes. Despite this central role, the social sciences are largely absent from mainstream evaluation frameworks, even though scholars in these fields generate dozens of rigorously annotated, context-sensitive datasets each year. Integrating this work into benchmark design could significantly improve the generalization and robustness of AI models. In turn, models trained on social scientific tasks would likely yield better performance on classic and contemporary tasks in disciplines as diverse as history, sociology, political science or economics. This is all the more pressing as these disciplines are quickly turning to LLMs for assistance. To address this gap, we introduce BenCSSmark, a benchmark composed of datasets annotated by computational social scientists. By integrating social scientific perspectives into benchmarking, BenCSSmark seeks to promote more robust, transparent, and socially relevant AI systems and to foster efficient collaboration.

---


### 89. [Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall](https://arxiv.org/abs/2605.04897)

**<font color=#1a73e8>作者：</font>** Joshua Adler, Guy Zehavi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extraction at ingestion is the wrong primitive for agent memory: content discarded before the query is known cannot be recovered at retrieval time. We propose True Memory, a six-layer architecture that shifts the center of the system from a storage schema to a multi-stage retrieval pipeline operating over events preserved verbatim. The full system runs as a single SQLite file on commodity CPU with no external database, vector index, graph store, or GPU. On LoCoMo (1,540 questions across 10 multi-session conversations), True Memory Pro reaches 93.0% accuracy (3-run mean) against 61.4% for Mem0, 65.4% for Supermemory, approximately 71% for Zep, and 94.5% for EverMemOS under a matched gpt-4.1-mini answer model. On LongMemEval (500 questions), True Memory Pro reaches 87.8% (3-run mean). On BEAM-1M (700 questions at the 1-million-token scale), True Memory Pro reaches 76.6% (3-run mean), above the prior published result of 73.9% for Hindsight. A 56-configuration ablation shows a 1.3-percentage-point spread within the top-performing configuration family.

---


### 90. [A geometric relation of the error introduced by sampling a language model's output distribution to its internal state](https://arxiv.org/abs/2605.04899)

**<font color=#1a73e8>作者：</font>** Albert F. Modenbach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GPT-style language models are sensitive to single-token changes at generation points where the predicted probability distribution is spread across multiple tokens. Viewing this sensitivity as a geometric property, we derive an $\mathfrak{so}(n)$-valued 1-form that depends only on the geometry of the token embeddings. Despite this purely geometric origin, we show that its curvature is semantically meaningful: On chess reasoning tasks, the curvature couples to the world model of an off-the-shelf instruction-tuned model, with transformations clustering by board region and respecting piece importance. Our findings suggest that token space geometry directly reflects how models internally represent problems.

---


### 91. [Delta-Based Neural Architecture Search: LLM Fine-Tuning via Code Diffs](https://arxiv.org/abs/2605.04903)

**<font color=#1a73e8>作者：</font>** Santosh Premi Adhikari, Radu Timofte, Dmitry Ignatov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show strong potential for neural architecture generation, yet existing approaches produce complete model implementations from scratch -- computationally expensive and yielding verbose code. We propose Delta-Code Generation, where fine-tuned LLMs generate compact unified diffs (deltas) to refine baseline architectures rather than synthesizing entire models. Our pipeline iteratively fine-tunes the LLM via LoRA on curated architectures from the LEMUR dataset, with MinHash-Jaccard novelty filtering for structural diversity. We evaluate three 7B-class LLMs -- DeepSeek-Coder-7B, Qwen2.5-Coder-7B, and Mistral-7B -- across six datasets (CIFAR-10, CIFAR-100, MNIST, SVHN, ImageNette, CelebA) using a 22-cycle protocol (1,100 candidates per LLM). All three substantially surpass the full-generation baseline (50.6% valid rate, 42.3% mean first-epoch accuracy): DeepSeek-Coder reaches 75.3% valid rate and 65.8% mean accuracy; Qwen2.5-Coder 72.1%/64.6%; Mistral 66.6%/66.1%. On CIFAR-10, best first-epoch accuracies reach 85.5% (Mistral), 85.2% (DeepSeek), 80.6% (Qwen) -- well above 63.98% full generation and 71.5% for the concurrent approach of Gu et al. Output lengths are 30-50 lines versus 200+ for full generation (75-85% reduction). A 50-epoch study confirms the 1-epoch proxy preserves rankings (Mistral: Spearman $\rho$ = 0.926). Delta-based generation is a token-efficient, multi-domain, LLM-agnostic alternative to full-model synthesis for LLM-driven NAS.

---


### 92. [Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games](https://arxiv.org/abs/2605.04906)

**<font color=#1a73e8>作者：</font>** Yidong He, Yutao Lai, Pengxu Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) excel in certain reasoning tasks, they struggle in multi-agent games where the final outcome depends on the joint strategies of all agents. In multi-agent games, the non-stationarity of other agents brings significant challenges on the evaluation of the reasoning process and the credit assignment over multiple reasoning steps. Existing single-agent reinforcement learning (RL) approaches and their multi-agent extensions fail to address these challenges as they do not incorporate other agents in the reasoning process. In this work, we propose Strat-Reasoner, a novel RL-based framework that improves LLMs' strategic reasoning ability in multi-agent games. We introduce a novel recursive reasoning paradigm where an agent's reasoning also integrates other agents' reasoning processes. To provide effective reward signals for the intermediate reasoning sequences, we employ a centralized Chain-of-Thought (CoT) comparison module to evaluate the reasoning quality. Finally, we compute an accurate hybrid advantage and develop a group-relative RL approach to optimize the LLM policy. Experimental results show that Strat-Reasoner substantially improves strategic abilities of underlying LLMs, achieving 22.1\% average performance improvements across various multi-agent games.

---


### 93. [Curated AI beats frontier LLMs at pharma asset discovery](https://arxiv.org/abs/2605.04908)

**<font color=#1a73e8>作者：</font>** Łukasz Kidziński, Kevin Thomas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose LLMs with web search are increasingly used to scout the competitive landscape of pharmaceutical pipelines. We benchmark Gosset -- an AI platform with a chat interface backed by curated target-, modality-, and indication-level drug-asset annotations -- against four frontier systems with web access (Claude Opus 4.7, GPT 5.5, Gemini 3.1 Pro, Perplexity sonar-pro) on ten niche oncology/immunology targets where most of the pipeline lives in the long tail of preclinical and Asian-developed assets. All five systems receive the same natural-language query and the same JSON output schema. Across 10 targets Gosset returns 3.2x more verified drugs per query than the best frontier system, at perfect precision and 100% recall against the cross-system union of verified drugs. The same curated index is exposed as a Gosset MCP server that any frontier model can call as a tool, suggesting that each of these systems can close most of the recall gap by swapping generic web search for a curated index behind the same chat interface.

---


### 94. [Breaking the Quality-Privacy Tradeoff in Tabular Data Generation via In-Context Learning](https://arxiv.org/abs/2605.04911)

**<font color=#1a73e8>作者：</font>** Xinyan Han, Yan Lu, Xiaoyu Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data synthesis aims to generate high-quality data while preserving privacy. However, we find that existing tabular generative models exhibit a clear tradeoff in the small-data regime: improving data quality typically comes at the cost of increased memorization of training samples, thereby weakening privacy protection. This tradeoff arises because small training sets make it difficult for dataset-specific generative models to distinguish generalizable structure from sample-specific patterns. To address this, we propose DiffICL, which formulates tabular data generation as an in-context learning problem. Instead of fitting each dataset from scratch,DiffICL leverages pretrained structural priors learned from a large collection of datasets, enabling it to infer data distributions from limited context rather than memorizing individual samples. We evaluate DiffICL on 14 real-world datasets. Results show that DiffICL improves both data quality and privacy, and generate synthetic data that provides effective data augmentation. Our findings suggest that the quality-privacy tradeoff can be improved through better training paradigms.

---


### 95. [Rethinking Local Learning: A Cheaper and Faster Recipe for LLM Post-Training](https://arxiv.org/abs/2605.04913)

**<font color=#1a73e8>作者：</font>** Hengyu Shi, Tianyang Han, Peizhe Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM post-training typically propagates task gradients through the full depth of the model. Although this end-to-end structure is simple and general, it couples task adaptation to full-depth activation storage, long-range backward dependencies and direct task-gradient access to pretrained representations. We argue that this full-depth backward coupling can be unnecessarily expensive and intrusive, particularly when post-training supervision is much narrower than pre-training. To this end, we propose \textbf{LoPT}: Local-Learning Post-Training, a simple post-training strategy that makes gradient reach an explicit design choice. LoPT places a single gradient boundary at the transformer midpoint: the second-half block learns from the task objective, while the first-half block is updated by a lightweight feature-reconstruction objective to preserve useful representations and maintain interface compatibility. LoPT shortens the task-induced backward path while limiting direct interference from narrow task gradients on early-layer representations. Extensive experiments demonstrate that LoPT achieves competitive performance with lower memory cost, higher training efficiency and better retention of pretrained capabilities. Our code is available at: this https URL

---


### 96. [A Foundation Model for Zero-Shot Logical Rule Induction](https://arxiv.org/abs/2605.04916)

**<font color=#1a73e8>作者：</font>** Yin Jun Phua  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inductive Logic Programming (ILP) learns interpretable logical rules from data. Existing methods are transductive: their learned parameters are bound to specific predicates and require retraining for each new task. We introduce Neural Rule Inducer (NRI), a pretrained model for zero-shot rule induction. Rather than encoding literal identities, NRI represents literals using domain-agnostic statistical properties such as class-conditional rates, entropy, and co-occurrence, which generalize across variable identities and counts without retraining. The model consists of a statistical encoder and a parallel slot-based decoder. Parallel decoding preserves the permutation invariance of logical disjunction; an autoregressive decoder would instead impose an arbitrary clause order. Product T-norm relaxation makes rule execution differentiable, allowing end-to-end training on prediction accuracy alone. We evaluate NRI on rule recovery, robustness to label noise and spurious correlations, and zero-shot transfer to real-world benchmarks, and we believe this work opens up the possibility of foundation models for symbolic reasoning. Code and the reference checkpoint are available at this https URL.

---


### 97. [DART: A Vision-Language Foundation Model for Comprehensive Rope Condition Monitoring](https://arxiv.org/abs/2605.04943)

**<font color=#1a73e8>作者：</font>** Anju Rani, Daniel Ortiz-Arroyo, Petar Durdevic  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The condition monitoring (CM) of synthetic fibre ropes (SFRs) used in offshore, maritime, and industrial settings demands more than a classifier: inspectors need continuous severity estimates, maintenance recommendations, anomaly flags, deterioration timelines, and automated reports, all from a single inspection image. We present DART (Damage Assessment via Rope Transformer), a vision-language foundation model that addresses the full rope inspection workflow through a unified multi-task architecture. DART extends the Joint-Embedding Predictive Architecture (JEPA) to the cross-modal domain by coupling a Vision Transformer (ViT-H/14) with Llama-3.2-3B-Instruct via a Severity-Conditioned Cross-Modal Fusion (SC-CMF) module. Three architectural innovations drive the model's versatility: (1) HD-MASK, a saliency-guided masking strategy that focuses self-supervised reconstruction on damage-dense patches; (2) per-class learnable severity gates that adaptively weight language grounding by damage category; and (3) a Contrastive Damage Disentanglement (CDD) loss that shapes the embedding space to simultaneously encode damage type, severity ordering, and cross-modal semantics. Trained once on 4,270 images spanning 14 fine-grained rope damage classes, the frozen DART backbone supports downstream tasks without any task-specific fine-tuning: damage classification (93.22 % accuracy, 91.04 % macro-F1, +38.5 pp over a vision-only baseline), continuous severity regression (Spearman rho = 0.94, within-1-ordinal accuracy 99.6 %), few-shot recognition (89.2 % macro-F1 at 20 shots). These results demonstrate that DART functions as a general-purpose CM backbone that goes well beyond classification, providing actionable inspection intelligence from a single shared representation.

---


### 98. [Adapting Large Language Models to a Low-Resource Agglutinative Language: A Comparative Study of LoRA and QLoRA for Bashkir](https://arxiv.org/abs/2605.04948)

**<font color=#1a73e8>作者：</font>** Mullosharaf K. Arabov, Svetlana S. Khaybullina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a comparative study of parameter-efficient fine-tuning (PEFT) methods, including LoRA and QLoRA, applied to the task of adapting large language models to the Bashkir language, a low-resource agglutinative language of the Turkic family. Experimental evaluation is conducted on a Bashkir text corpus of 71k documents (46.9M tokens) using models of various architectures: DistilGPT2, GPT-2 (base, medium), Phi-2, Qwen2.5-7B, DeepSeek-7B, and Mistral-7B. To improve the reliability of results, each configuration was trained with three different random seeds.
The lowest perplexity on the test set was obtained for GPT-2 medium with full fine-tuning (3.34). Meanwhile, QLoRA applied to Mistral-7B (3.79) and Phi-2 (3.81) achieved comparable quality with over 40 times fewer trainable parameters. However, we also observed cases of significant quality degradation when using PEFT for certain architectures (e.g., DeepSeek-7B with rank 8, perplexity = 129.55), indicating that the outcome depends critically on the choice of the base model and its tokenizer.
Additionally, a qualitative analysis of generated texts based on Bashkir prompts revealed that models with the best perplexity do not necessarily produce the most coherent outputs: QLoRA-tuned models generated monolingual Bashkir continuations, whereas the fully fine-tuned model with the lowest perplexity frequently switched to English. The results suggest that QLoRA on 7B-scale models offers an effective compromise between quality and computational cost for Bashkir. To ensure reproducibility, open data, code, and trained adapters will be released upon acceptance.

---


### 99. [KernelBench-X: A Comprehensive Benchmark for Evaluating LLM-Generated GPU Kernels](https://arxiv.org/abs/2605.04956)

**<font color=#1a73e8>作者：</font>** Han Wang, Jintao Zhang, Kai Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based Triton kernel generation has attracted significant interest, yet a fundamental empirical question remains unanswered: where does this capability break down, and why? We present KernelBench-X, a benchmark designed to answer this question through category-aware evaluation of correctness and hardware efficiency across 176 tasks in 15 categories. Our systematic comparison of five representative methods yields three main findings. First, task structure determines correctness more than method design. Category explains nearly three times more variance in semantic correctness than method (9.4% vs 3.3% explained deviance), and 72% of Fusion tasks fail across all five methods while Math tasks are solved consistently. Second, iterative refinement improves correctness, but not performance. Across GEAK iterations, compile rate rises from 52.3% to 68.8% while average speedup declines from $1.58\times$ to $1.44\times$; newly rescued kernels consistently underperform persistently correct ones ($1.16\times$ vs $1.58\times$ speedup in round~0$\to$1). Third, correctness does not imply efficiency. 46.6% of correct kernels are slower than the PyTorch eager baseline, and cross-hardware speedup variance reaches $21.4\times$. Besides, quantization remains completely unsolved (0/30 successes) despite non-trivial compilation rates, revealing systematic misunderstanding of numerical computation contracts rather than surface-level syntax errors. These findings suggest that future progress depends on handling global coordination, explicitly modeling numerical precision, and incorporating hardware efficiency into generation. The code is available at this https URL

---


### 100. [Why Expert Alignment Is Hard: Evidence from Subjective Evaluation](https://arxiv.org/abs/2605.04972)

**<font color=#1a73e8>作者：</font>** Tzu-Mi Lin, Wataru Hirota, Tatsuya Ishigaki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning large language models with expert judgment is especially difficult in subjective evaluation tasks, where experts may disagree, rely on tacit criteria, and change their judgments over time. In this paper, we study expert alignment as a way to understand this difficulty. Using expert evaluations and follow-up questionnaires, we examine how different forms of expert information affect alignment and what this reveals about subjective judgment. Our findings show four consistent patterns. First, alignment difficulty varies substantially across experts, suggesting that expert evaluation styles differ widely in their distance from a model's prior behavior. Second, explicit criteria and reasoning do not always improve alignment, indicating that expert judgment is not fully captured by verbalized rules. Third, editing is sensitive to both the number and the identity of examples, with small numbers of edits providing useful but unstable gains. Fourth, alignment difficulty differs across evaluation dimensions: dimensions grounded more directly in proposal content are easier to align, while dimensions requiring external knowledge or value-based judgment remain harder. Taken together, these results suggest that expert alignment is difficult not only because of model limitations, but also because subjective evaluation is inherently heterogeneous, partly tacit, dimension-dependent, and temporally unstable.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-126](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
