# 🧠 大模型相关研究 | 2026年04月24日

> 本类共 **129** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-129](./part-03.md)

---

### 51. [Continuous Semantic Caching for Low-Cost LLM Serving](https://arxiv.org/abs/2604.20021)

**<font color=#1a73e8>作者：</font>** Baran Atalar, Xutong Liu, Jinhang Zuo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) become increasingly popular, caching responses so that they can be reused by users with semantically similar queries has become a vital strategy for reducing inference costs and latency. Existing caching frameworks have proposed to decide which query responses to cache by assuming a finite, known universe of discrete queries and learning their serving costs and arrival probabilities. As LLMs' pool of users and queries expands, however, such an assumption becomes increasingly untenable: real-world LLM queries reside in an infinite, continuous embedding space. In this paper, we establish the first rigorous theoretical framework for semantic LLM response caching in continuous query space under uncertainty. To bridge the gap between discrete optimization and continuous representation spaces, we introduce dynamic $\epsilon$-net discretization coupled with Kernel Ridge Regression. This design enables the system to formally quantify estimation uncertainty and generalize partial feedback on LLM query costs across continuous semantic query neighborhoods. We develop both offline learning and online adaptive algorithms optimized to reduce switching costs incurred by changing the cached responses. We prove that our online algorithm achieves a sublinear regret bound against an optimal continuous oracle, which reduces to existing bounds for discrete query models. Extensive empirical evaluations demonstrate that our framework approximates the continuous optimal cache well while also reducing computational and switching overhead compared to existing methods.

---


### 52. [Statistics, Not Scale: Modular Medical Dialogue with Bayesian Belief Engine](https://arxiv.org/abs/2604.20022)

**<font color=#1a73e8>作者：</font>** Yusuf Kesmen, Fay Elhassan, Jiayi Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as autonomous diagnostic agents, yet they conflate two fundamentally different capabilities: natural-language communication and probabilistic reasoning. We argue that this conflation is an architectural flaw, not an engineering shortcoming. We introduce BMBE (Bayesian Medical Belief Engine), a modular diagnostic dialogue framework that enforces a strict separation between language and reasoning: an LLM serves only as a sensor, parsing patient utterances into structured evidence and verbalising questions, while all diagnostic inference resides in a deterministic, auditable Bayesian engine. Because patient data never enters the LLM, the architecture is private by construction; because the statistical backend is a standalone module, it can be replaced per target population without retraining. This separation yields three properties no autonomous LLM can offer: calibrated selective diagnosis with a continuously adjustable accuracy-coverage tradeoff, a statistical separation gap where even a cheap sensor paired with the engine outperforms a frontier standalone model from the same family at a fraction of the cost, and robustness to adversarial patient communication styles that cause standalone doctors to collapse. We validate across empirical and LLM-generated knowledge bases against frontier LLMs, confirming the advantage is architectural, not informational.

---


### 53. [Cognitive Alignment At No Cost: Inducing Human Attention Biases For Interpretable Vision Transformers](https://arxiv.org/abs/2604.20027)

**<font color=#1a73e8>作者：</font>** Ethan Knights  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For state-of-the-art image understanding, Vision Transformers (ViTs) have become the standard architecture but their processing diverges substantially from human attentional characteristics. We investigate whether this cognitive gap can be shrunk by fine-tuning the self-attention weights of Google's ViT-B/16 on human saliency fixation maps. To isolate the effects of semantically relevant signals from generic human supervision, the tuned model is compared against a shuffled control. Fine-tuning significantly improved alignment across five saliency metrics and induced three hallmark human-like biases: tuning reversed the baseline's anti-human large-object bias toward small-objects, amplified the animacy preference and diminished extreme attention entropy. Bayesian parity analysis provides decisive to very-strong evidence that this cognitive alignment comes at no cost to the model's original classification performance on in- (ImageNet), corrupted (ImageNet-C) and out-of-distribution (ObjectNet) benchmarks. An equivalent procedure applied to a ResNet-50 Convolutional Neural Network (CNN) instead degraded both alignment and accuracy, suggesting that the ViT's modular self-attention mechanism is uniquely suited for dissociating spatial priority from representational logic. These findings demonstrate that biologically grounded priors can be instilled as a free emergent property of human-aligned attention, to improve transformer interpretability.

---


### 54. [Separable Pathways for Causal Reasoning: How Architectural Scaffolding Enables Hypothesis-Space Restructuring in LLM Agents](https://arxiv.org/abs/2604.20039)

**<font color=#1a73e8>作者：</font>** John Alderete, Sebastian Benthal, Connie Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Causal discovery through experimentation and intervention is fundamental to robust problem solving. It requires not just updating beliefs within a fixed framework but revising the hypothesis space itself, a capacity current AI agents lack when evidence demands representations they have not previously constructed. We extend the blicket detector paradigm from developmental science to test this capacity in AI agents equipped with architectural scaffolding that targets hypothesis-space restructuring. Our compositional architecture has two discrete components: context graphs, which structure exploration as typed state machines, and dynamic behaviors, which monitor for evidence that the current hypothesis space is inadequate and expand it at runtime. Across 1,085 experimental trials, these components make orthogonal contributions: context graphs drive reasoning quality within the post-switch hypothesis space, accounting for 94\% of the accuracy gain, while dynamic behaviors drive reasoning eligibility by detecting regime changes and preventing premature commitment to outdated hypotheses.

---


### 55. [TriEx: A Game-based Tri-View Framework for Explaining Internal Reasoning in Multi-Agent LLMs](https://arxiv.org/abs/2604.20043)

**<font color=#1a73e8>作者：</font>** Ziyi Wang, Chen Zhang, Wenjun Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Explainability for Large Language Model (LLM) agents is especially challenging in interactive, partially observable settings, where decisions depend on evolving beliefs and other agents. We present \textbf{TriEx}, a tri-view explainability framework that instruments sequential decision making with aligned artifacts: (i) structured first-person self-reasoning bound to an action, (ii) explicit second-person belief states about opponents updated over time, and (iii) third-person oracle audits grounded in environment-derived reference signals. This design turns explanations from free-form narratives into evidence-anchored objects that can be compared and checked across time and perspectives. Using imperfect-information strategic games as a controlled testbed, we show that TriEx enables scalable analysis of explanation faithfulness, belief dynamics, and evaluator reliability, revealing systematic mismatches between what agents say, what they believe, and what they do. Our results highlight explainability as an interaction-dependent property and motivate multi-view, evidence-grounded evaluation for LLM agents. Code is available at this https URL.

---


### 56. [Large language models perceive cities through a culturally uneven baseline](https://arxiv.org/abs/2604.20048)

**<font color=#1a73e8>作者：</font>** Rong Zhao, Wanqi Liu, Zhizhou Sha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to describe, evaluate and interpret places, yet it remains unclear whether they do so from a culturally neutral standpoint. Here we test urban perception in frontier LLMs using a balanced global street-view sample and prompts that either remain neutral or invoke different regional cultural standpoints. Across open-ended descriptions and structured place judgments, the neutral condition proved not to be neutral in practice. Prompts associated with Europe and Northern America remained systematically closer to the baseline than many non-Western prompts, indicating that model perception is organized around a culturally uneven reference frame rather than a universal one. Cultural prompting also shifted affective evaluation, producing sentiment-based ingroup preference for some prompted identities. Comparisons with regional human text-image benchmarks showed that culturally proximate prompting could improve alignment with human descriptions, but it did not recover human levels of semantic diversity and often preserved an affectively elevated style. The same asymmetry reappeared in structured judgments of safety, beauty, wealth, liveliness, boredom and depression, where model outputs were interpretable but only partly reproduced human group differences. These findings suggest that LLMs do not simply perceive cities from nowhere: they do so through a culturally uneven baseline that shapes what appears ordinary, familiar and positively valued.

---


### 57. [Bootstrapping Post-training Signals for Open-ended Tasks via Rubric-based Self-play on Pre-training Text](https://arxiv.org/abs/2604.20051)

**<font color=#1a73e8>作者：</font>** Chengyu Huang, Sheng-Yen Chou, Zhengxin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-play has recently emerged as a promising paradigm to train Large Language Models (LLMs). In self-play, the target LLM creates the task input (e.g., ask a question), which it then addresses itself by producing a task output (e.g., give an answer). A reward model evaluates the output, and the rewards are then used to train the LLM, typically via Reinforcement Learning (RL). Self-play incurs minimal supervision costs, and this is especially helpful for post-training LLMs, which require high-quality input-output pairs that traditionally have to be written by humans or expensive proprietary models. However, existing work explores self-play only for verifiable tasks such as math and coding. Instead, we seek to extend it to more realistic open-ended tasks. In particular, we propose POP, a self-play framework that uses the same LLM to synthesize evaluation rubrics, along with input-output pairs, for each example. The rubric is then used to evaluate outputs and train the model. We further ground the framework on a content-rich pretraining corpus to (1) ensure a generation-verification gap and reduce reward hacking, and (2) prevent mode collapse. On Qwen-2.5-7B, POP increases performance of both pretrained and instruction-tuned models, across different tasks ranging from long-form Healthcare QA to creative writing and instruction following.

---


### 58. [Analysis of Nystrom method with sequential ridge leverage scores](https://arxiv.org/abs/2604.20077)

**<font color=#1a73e8>作者：</font>** Daniele Calandriello, Alessandro Lazaric, Michal Valko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale kernel ridge regression (KRR) is limited by the need to store a large kernel matrix K_t. To avoid storing the entire matrix K_t, Nystrom methods subsample a subset of columns of the kernel matrix, and efficiently find an approximate KRR solution on the reconstructed matrix. The chosen subsampling distribution in turn affects the statistical and computational tradeoffs. For KRR problems, recent works show that a sampling distribution proportional to the ridge leverage scores (RLSs) provides strong reconstruction guarantees for the approximation. While exact RLSs are as difficult to compute as a KRR solution, we may be able to approximate them well enough. In this paper, we study KRR problems in a sequential setting and introduce the INK-ESTIMATE algorithm, that incrementally computes the RLSs estimates. INK-ESTIMATE maintains a small sketch of K_t, that at each step is used to compute an intermediate estimate of the RLSs. First, our sketch update does not require access to previously seen columns, and therefore a single pass over the kernel matrix is sufficient. Second, the algorithm requires a fixed, small space budget to run dependent only on the effective dimension of the kernel matrix. Finally, our sketch provides strong approximation guarantees on the distance between the true kernel matrix and its approximation, and on the statistical risk of the approximate KRR solution at any time, because all our guarantees hold at any intermediate step.

---


### 59. [On the Quantization Robustness of Diffusion Language Models in Coding Benchmarks](https://arxiv.org/abs/2604.20079)

**<font color=#1a73e8>作者：</font>** Aarav Gupta, Gururaj Deshpande, Chandreyi Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-regressive Large Language Models (LLMs) achieve strong performance on coding tasks, but incur high memory and inference costs. Diffusion-based language models (d-LLMs) offer bounded inference cost via iterative denoising, but their behavior under post-training quantization (PTQ) has been sparsely explored. We investigate the application and robustness of PTQ techniques, specifically GPTQ and a modified Hessian-Aware Quantization (HAWQ) algorithm, on a diffusion-based coding LLM (CoDA) and observe that these methods applied to CoDA exhibit greater robustness at low bitwidths compared to Qwen3-1.7B, its auto-regressive counterpart, under a standardized evaluation pipeline. We find that in our setup, CoDA exhibits greater robustness at low bitwidths (2-4 bits), with smaller accuracy degradation across HumanEval and MBPP benchmarks. Additionally, mixed-precision configurations derived from HAWQ provide smooth trade-offs across accuracy, latency, and memory. The results suggest that diffusion LLMs may offer advantages for efficient deployment due to more quantization-resilience.

---


### 60. [Differentiable Conformal Training for LLM Reasoning Factuality](https://arxiv.org/abs/2604.20098)

**<font color=#1a73e8>作者：</font>** Nathan Hittesdorf, Marco Salzetta, Lu Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) frequently hallucinate, limiting their reliability in critical applications. Conformal Prediction (CP) addresses this by calibrating error rates on held-out data to provide statistically valid confidence guarantees. Recent work extends CP to LLM factuality to filter out risky claims, ensuring that hallucination rates remain below a user-specified level (e.g., 10%). While prior methods treat claims independently, Coherent Factuality extends to multi-step reasoning by representing outputs as dependency graphs and jointly validating claims with their logical ancestors. A key limitation is that Coherent Factuality is not differentiable, requiring hand-crafted scorers that at high reliability levels remove nearly 60% of true claims. We introduce Differentiable Coherent Factuality (DCF), a fully differentiable relaxation that enables learning improved scorers while provably recovering the original algorithm's guarantees. Experiments on two benchmark reasoning datasets demonstrate DCF achieves up to 141% improvement in claim retention while maintaining reliability guarantees, representing a significant step towards reliable conformal LLM systems.

---


### 61. [Zeitgeist-Aware Multimodal (ZAM) Datasets of Pro-Eating Disorder Short-Form Videos: An Idea Worth Researching](https://arxiv.org/abs/2604.20119)

**<font color=#1a73e8>作者：</font>** Eden Shaveet, Zefan Sramek, Yumi Hamamoto 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Objective: Reliable identification of pro-eating disorder (pro-ED) content online suffers from two pervasive problems: 1) existing methods predominantly rely on text-based signals, failing to capture the inherently multimodal nature of multimedia content; and 2) these methods struggle to keep pace with the rapid evolution of references, memes, terminology, and contextual cues that underlie this content. Together, these limitations point to a gap: the absence of an expert-annotated reference standard capable of supporting real-time research and robust multimodal detection model training for pro-ED content on short-form video platforms. Method: To address this, we propose "zeitgeist-aware" multimodal (ZAM) datasets: continuously curated collections of annotated multimodal pro-ED content with inclusion criteria that evolve alongside the memetic zeitgeist: the variable essence of what is considered pro-ED as new media and references come into the cultural zeitgeist and are absorbed and interpreted in online spaces. Results: We present a rationale for such datasets, define their core characteristics, outline approaches for their curation, and describe our progress toward that end. Discussion: This dataset and pipeline architecture may benefit researchers across several fields who are interested in how pro-ED sentiment is encoded and transmitted through short-form video content across time, including for the purpose of responsive moderation efforts.

---


### 62. [Adaptive Conformal Anomaly Detection with Time Series Foundation Models for Signal Monitoring](https://arxiv.org/abs/2604.20122)

**<font color=#1a73e8>作者：</font>** Natalia Martinez Gil, Fearghal O'Donncha, Wesley M. Gifford 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a post-hoc adaptive conformal anomaly detection method for monitoring time series that leverages predictions from pre-trained foundation models without requiring additional fine-tuning. Our method yields an interpretable anomaly score directly interpretable as a false alarm rate (p-value), facilitating transparent and actionable decision-making. It employs weighted quantile conformal prediction bounds and adaptively learns optimal weighting parameters from past predictions, enabling calibration under distribution shifts and stable false alarm control, while preserving out-of-sample guarantees. As a model-agnostic solution, it integrates seamlessly with foundation models and supports rapid deployment in resource-constrained environments. This approach addresses key industrial challenges such as limited data availability, lack of training expertise, and the need for immediate inference, while taking advantage of the growing accessibility of time series foundation models. Experiments on both synthetic and real-world datasets show that the proposed approach delivers strong performance, combining simplicity, interpretability, robustness, and adaptivity.

---


### 63. [Whose Story Gets Told? Positionality and Bias in LLM Summaries of Life Narratives](https://arxiv.org/abs/2604.20131)

**<font color=#1a73e8>作者：</font>** Melanie Subbiah, Haaris Mian, Nicholas Deas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Increasingly, studies are exploring using Large Language Models (LLMs) for accelerated or scaled qualitative analysis of text data. While we can compare LLM accuracy against human labels directly for deductive coding, or labeling text, it is more challenging to judge the ethics and effectiveness of using LLMs in abstractive methods such as inductive thematic analysis. We collaborate with psychologists to study the abstractive claims LLMs make about human life stories, asking, how does using an LLM as an interpreter of meaning affect the conclusions and perspectives of a study? We propose a summarization-based pipeline for surfacing biases in perspective-taking an LLM might employ in interpreting these life stories. We demonstrate that our pipeline can identify both race and gender bias with the potential for representational harm. Finally, we encourage the use of this analysis in future studies involving LLM-based interpretation of study participants' written text or transcribed speech to characterize a positionality portrait for the study.

---


### 64. [EvoAgent: An Evolvable Agent Framework with Skill Learning and Multi-Agent Delegation](https://arxiv.org/abs/2604.20133)

**<font color=#1a73e8>作者：</font>** Aimin Zhang, Jiajing Guo, Fuwei Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes EvoAgent - an evolvable large language model (LLM) agent framework that integrates structured skill learning with a hierarchical sub-agent delegation mechanism. EvoAgent models skills as multi-file structured capability units equipped with triggering mechanisms and evolutionary metadata, and enables continuous skill generation and optimization through a user-feedback-driven closed-loop process. In addition, by incorporating a three-stage skill matching strategy and a three-layer memory architecture, the framework supports dynamic task decomposition for complex problems and long-term capability accumulation. Experimental results based on real-world foreign trade scenarios demonstrate that, after integrating EvoAgent, GPT5.2 achieves significant improvements in professionalism, accuracy, and practical utility. Under a five-dimensional LLM-as-Judge evaluation protocol, the overall average score increases by approximately 28%. Further model transfer experiments indicate that the performance of an agent system depends not only on the intrinsic capabilities of the underlying model, but also on the degree of synergy between the model and the agent architecture.

---


### 65. [AFMRL: Attribute-Enhanced Fine-Grained Multi-Modal Representation Learning in E-commerce](https://arxiv.org/abs/2604.20135)

**<font color=#1a73e8>作者：</font>** Biao Zhang, Lixin Chen, Bin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal representation is crucial for E-commerce tasks such as identical product retrieval. Large representation models (e.g., VLM2Vec) demonstrate strong multimodal understanding capabilities, yet they struggle with fine-grained semantic comprehension, which is essential for distinguishing highly similar items. To address this, we propose Attribute-Enhanced Fine-Grained Multi-Modal Representation Learning (AFMRL), which defines product fine-grained understanding as an attribute generation task. It leverages the generative power of Multimodal Large Language Models (MLLMs) to extract key attributes from product images and text, and enhances representation learning through a two-stage training framework: 1) Attribute-Guided Contrastive Learning (AGCL), where the key attributes generated by the MLLM are used in the image-text contrastive learning training process to identify hard samples and filter out noisy false negatives. 2) Retrieval-aware Attribute Reinforcement (RAR), where the improved retrieval performance of the representation model post-attribute integration serves as a reward signal to enhance MLLM's attribute generation during multimodal fine-tuning. Extensive experiments on large-scale E-commerce datasets demonstrate that our method achieves state-of-the-art performance on multiple downstream retrieval tasks, validating the effectiveness of harnessing generative models to advance fine-grained representation learning.

---


### 66. [HiPO: Hierarchical Preference Optimization for Adaptive Reasoning in LLMs](https://arxiv.org/abs/2604.20140)

**<font color=#1a73e8>作者：</font>** Darsh Kachroo, Adriana Caraeni, Arjun Prasaath Anbazhagan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) is an effective framework for aligning large language models with human preferences, but it struggles with complex reasoning tasks. DPO optimizes for the likelihood of generating preferred over dispreferred responses in their entirety and lacks the granularity to provide feedback on subsections of many-step solutions typical of reasoning tasks. Existing methods excel at either stable preference learning (e.g., DPO variants like KTO and RSO) or structured reasoning (e.g., ReMA's multi-agent RL framework, Tree of Thoughts), but fail to merge these complementary strengths. We propose HiPO (Hierarchical Preference Optimization), an extension of DPO that separates responses into reasoning segments (query clarification and context, reasoning steps, and answer) and computes loss as a weighted sum of the DPO loss for each segment. Our approach enables segment-specific training while maintaining DPO's computational efficiency and training stability. We demonstrate that for multiple 7B LLMs fine-tuned using HiPO and DPO on the Math Stack Exchange preference dataset, the models trained with HiPO outperform the others on a variety of common math benchmarks and achieve greater organization, logical flow, and consistency as measured by GPT-4.1.

---


### 67. [Meta-Tool: Efficient Few-Shot Tool Adaptation for Small Language Models](https://arxiv.org/abs/2604.20148)

**<font color=#1a73e8>作者：</font>** Sachin Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can small language models achieve strong tool-use performance without complex adaptation mechanisms? This paper investigates this question through Meta-Tool, a controlled empirical study comparing hypernetwork-based LoRA adaptation against carefully designed few-shot prompting. Using a Llama-3.2-3B-Instruct backbone, we evaluate four adaptation mechanisms--few-shot prompting, documentation encoding, hypernetwork-generated LoRA weights, and value-guided beam search--across four diverse benchmarks: Gorilla APIBench, Spider 2.0, WebArena, and InterCode. Our central finding is a well-supported negative result: despite generating non-trivial weight matrices, the 227.8M-parameter hypernetwork provides no measurable improvement over few-shot prompting alone. Comprehensive ablation studies reveal that few-shot examples contribute +21.5% to performance and documentation contributes +5.0%, while the hypernetwork adds 0%. A 3B model with well-designed prompts achieves 79.7% of GPT-5's average performance at $10 \times$ lower latency. Error analysis across 722 failure cases spanning all shot counts (0--5) shows that at the 5-shot configuration (106 failures), failure modes are task-dependent: schema-heavy tasks (Spider 2.0, WebArena) show near-zero format errors with remaining failures semantic, while format errors dominate on Gorilla (100%) and InterCode (70%). These findings redirect practitioners toward prompt engineering and example curation rather than complex adaptation architectures.

---


### 68. [Duluth at SemEval-2026 Task 6: DeBERTa with LLM-Augmented Data for Unmasking Political Question Evasions](https://arxiv.org/abs/2604.20168)

**<font color=#1a73e8>作者：</font>** Shujauddin Syed, Ted Pedersen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the Duluth approach to SemEval-2026 Task 6 on CLARITY: Unmasking Political Question Evasions. We address Task 1 (clarity-level classification) and Task 2 (evasion-level classification), both of which involve classifying question--answer pairs from U.S.\ presidential interviews using a two-level taxonomy of response clarity. Our system is based on DeBERTa-V3-base, extended with focal loss, layer-wise learning rate decay, and boolean discourse features. To address class imbalance in the training data, we augment minority classes using synthetic examples generated by Gemini 3 and Claude Sonnet 4.5. Our best configuration achieved a Macro F1 of 0.76 on the Task 1 evaluation set, placing 8th out of 40 teams. The top-ranked system (TeleAI) achieved 0.89, while the mean score across participants was 0.70. Error analysis reveals that the dominant source of misclassification is confusion between Ambivalent and Clear Reply responses, a pattern that mirrors disagreements among human annotators. Our findings demonstrate that LLM-based data augmentation can meaningfully improve minority-class recall on nuanced political discourse tasks.

---


### 69. [Dual-Cluster Memory Agent: Resolving Multi-Paradigm Ambiguity in Optimization Problem Solving](https://arxiv.org/abs/2604.20183)

**<font color=#1a73e8>作者：</font>** Xinyu Zhang, Yuchen Wan, Boxuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often struggle with structural ambiguity in optimization problems, where a single problem admits multiple related but conflicting modeling paradigms, hindering effective solution generation. To address this, we propose Dual-Cluster Memory Agent (DCM-Agent) to enhance performance by leveraging historical solutions in a training-free manner. Central to this is Dual-Cluster Memory Construction. This agent assigns historical solutions to modeling and coding clusters, then distills each cluster's content into three structured types: Approach, Checklist, and Pitfall. This process derives generalizable guidance knowledge. Furthermore, this agent introduces Memory-augmented Inference to dynamically navigate solution paths, detect and repair errors, and adaptively switch reasoning paths with structured knowledge. The experiments across seven optimization benchmarks demonstrate that DCM-Agent achieves an average performance improvement of 11%- 21%. Notably, our analysis reveals a ``knowledge inheritance'' phenomenon: memory constructed by larger models can guide smaller models toward superior performance, highlighting the framework's scalability and efficiency.

---


### 70. [WildFireVQA: A Large-Scale Radiometric Thermal VQA Benchmark for Aerial Wildfire Monitoring](https://arxiv.org/abs/2604.20190)

**<font color=#1a73e8>作者：</font>** Mobin Habibpour, Niloufar Alipour Talemi, John Spodnik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wildfire monitoring requires timely, actionable situational awareness from airborne platforms, yet existing aerial visual question answering (VQA) benchmarks do not evaluate wildfire-specific multimodal reasoning grounded in thermal measurements. We introduce WildFireVQA, a large-scale VQA benchmark for aerial wildfire monitoring that integrates RGB imagery with radiometric thermal data. WildFireVQA contains 6,097 RGB-thermal samples, where each sample includes an RGB image, a color-mapped thermal visualization, and a radiometric thermal TIFF, and is paired with 34 questions, yielding a total of 207,298 multiple-choice questions spanning presence and detection, classification, distribution and segmentation, localization and direction, cross-modal reasoning, and flight planning for operational wildfire intelligence. To improve annotation reliability, we combine multimodal large language model (MLLM)-based answer generation with sensor-driven deterministic labeling, manual verification, and intra-frame and inter-frame consistency checks. We further establish a comprehensive evaluation protocol for representative MLLMs under RGB, Thermal, and retrieval-augmented settings using radiometric thermal statistics. Experiments show that across task categories, RGB remains the strongest modality for current models, while retrieved thermal context yields gains for stronger MLLMs, highlighting both the value of temperature-grounded reasoning and the limitations of existing MLLMs in safety-critical wildfire scenarios. The dataset and benchmark code are open-source at this https URL.

---


### 71. [From Scene to Object: Text-Guided Dual-Gaze Prediction](https://arxiv.org/abs/2604.20191)

**<font color=#1a73e8>作者：</font>** Zehong Ke, Yanbo Jiang, Jinhao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpretable driver attention prediction is crucial for human-like autonomous driving. However, existing datasets provide only scene-level global gaze rather than fine-grained object-level annotations, inherently failing to support text-grounded cognitive modeling. Consequently, while Vision-Language Models (VLMs) hold great potential for semantic reasoning, this critical data limitations leads to severe text-vision decoupling and visual-bias hallucinations. To break this bottleneck and achieve precise object-level attention prediction, this paper proposes a novel dual-branch gaze prediction framework, establishing a complete paradigm from data construction to model architecture. First, we construct G-W3DA, a object-level driver attention dataset. By integrating a multimodal large language model with the Segment Anything Model 3 (SAM3), we decouple macroscopic heatmaps into object-level masks under rigorous cross-validation, fundamentally eliminating annotation hallucinations. Building upon this high-quality data foundation, we propose the DualGaze-VLM architecture. This architecture extracts the hidden states of semantic queries and dynamically modulates visual features via a Condition-Aware SE-Gate, achieving intent-driven precise spatial anchoring. Extensive experiments on the W3DA benchmark demonstrate that DualGaze-VLM consistently surpasses existing state-of-the-art (SOTA) models in spatial alignment metrics, notably achieving up to a 17.8% improvement in Similarity (SIM) under safety-critical scenarios. Furthermore, a visual Turing test reveals that the attention heatmaps generated by DualGaze-VLM are perceived as authentic by 88.22% of human evaluators, proving its capability to generate rational cognitive priors.

---


### 72. [All Languages Matter: Understanding and Mitigating Language Bias in Multilingual RAG](https://arxiv.org/abs/2604.20199)

**<font color=#1a73e8>作者：</font>** Dan Wang, Guozhao Mo, Yafei Shi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual Retrieval-Augmented Generation (mRAG) leverages cross-lingual evidence to ground Large Language Models (LLMs) in global knowledge. However, we show that current mRAG systems suffer from a language bias during reranking, systematically favoring English and the query's native language. By introducing an estimated oracle evidence analysis, we quantify a substantial performance gap between existing rerankers and the achievable upper bound. Further analysis reveals a critical distributional mismatch: while optimal predictions require evidence scattered across multiple languages, current systems systematically suppress such ``answer-critical'' documents, thereby limiting downstream generation performance. To bridge this gap, we propose \textit{\textbf{L}anguage-\textbf{A}gnostic \textbf{U}tility-driven \textbf{R}eranker \textbf{A}lignment (LAURA)}, which aligns multilingual evidence ranking with downstream generative utility. Experiments across diverse languages and generation models show that LAURA effectively mitigates language bias and consistently improves mRAG performance.

---


### 73. [The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models](https://arxiv.org/abs/2604.20225)

**<font color=#1a73e8>作者：</font>** Yilun Liu, Chunguang Zhao, Mengyao Piao 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating the multilingual and multicultural capabilities of Large Language Models (LLMs) is essential for their global utility. However, current benchmarks face three critical limitations: (1) fragmented evaluation dimensions that often neglect deep cultural nuances; (2) insufficient language coverage in subjective tasks relying on low-quality machine translation; and (3) shallow analysis that lacks diagnostic depth beyond simple rankings. To address these, we introduce GaoYao, a comprehensive benchmark with 182.3k samples, 26 languages and 51 nations/areas. First, GaoYao proposes a unified framework categorizing evaluation tasks into three cultural layers (General Multilingual, Cross-cultural, Monocultural) and nine cognitive sub-layers. Second, we achieve native-quality expansion by leveraging experts to rigorously localize subjective benchmarks into 19 languages and synthesizing cross-cultural test sets for 34 cultures, surpassing prior coverage by up to 111%. Third, we conduct an in-depth diagnostic analysis on 20+ flagship and compact LLMs. Our findings reveal significant geographical performance disparities and distinct gaps between tasks, offering a reliable map for future work. We release the benchmark (this https URL).

---


### 74. [Hybrid Policy Distillation for LLMs](https://arxiv.org/abs/2604.20244)

**<font color=#1a73e8>作者：</font>** Wenhong Zhu, Ruobing Xie, Rui Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) is a powerful paradigm for compressing large language models (LLMs), whose effectiveness depends on intertwined choices of divergence direction, optimization strategy, and data regime. We break down the design of existing KD methods and present a unified view that establishes connections between them, reformulating KD as a reweighted log-likelihood objective at the token level. We further propose Hybrid Policy Distillation (HPD), which integrates the complementary advantages of forward and reverse KL to balance mode coverage and mode-seeking, and combines off-policy data with lightweight, approximate on-policy sampling. We validate HPD on long-generation math reasoning as well as short-generation dialogue and code tasks, demonstrating improved optimization stability, computational efficiency, and final performance across diverse model families and scales. The code related to this work is available at this https URL.

---


### 75. [Memory-Augmented LLM-based Multi-Agent System for Automated Feature Generation on Tabular Data](https://arxiv.org/abs/2604.20261)

**<font color=#1a73e8>作者：</font>** Fengxian Dong, Zhi Zheng, Xiao Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated feature generation extracts informative features from raw tabular data without manual intervention and is crucial for accurate, generalizable machine learning. Traditional methods rely on predefined operator libraries and cannot leverage task semantics, limiting their ability to produce diverse, high-value features for complex tasks. Recent Large Language Model (LLM)-based approaches introduce richer semantic signals, but still suffer from a restricted feature space due to fixed generation patterns and from the absence of feedback from the learning objective. To address these challenges, we propose a Memory-Augmented LLM-based Multi-Agent System (\textbf{MALMAS}) for automated feature generation. MALMAS decomposes the generation process into agents with distinct responsibilities, and a Router Agent activates an appropriate subset of agents per iteration, further broadening exploration of the feature space. We further integrate a memory module comprising procedural memory, feedback memory, and conceptual memory, enabling iterative refinement that adaptively guides subsequent feature generation and improves feature quality and diversity. Extensive experiments on multiple public datasets against state-of-the-art baselines demonstrate the effectiveness of our approach. The code is available at this https URL

---


### 76. [ActuBench: A Multi-Agent LLM Pipeline for Generation and Evaluation of Actuarial Reasoning Tasks](https://arxiv.org/abs/2604.20273)

**<font color=#1a73e8>作者：</font>** Jan-Philipp Schmidt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present ActuBench, a multi-agent LLM pipeline for the automated generation and evaluation of advanced actuarial assessment items aligned with the International Actuarial Association (IAA) Education Syllabus. The pipeline separates four LLM roles by adapter: one agent drafts items, one constructs distractors, a third independently verifies both stages and drives bounded one-shot repair loops, and a cost-optimized auxiliary agent handles Wikipedia-note summarization and topic labelling. The items, per-model responses and complete leaderboard are published as a browsable web interface at this https URL, allowing readers and practitioners to inspect individual items without a repository checkout. We evaluate 50 language models from eight providers on two complementary benchmarks -- 100 empirically hardest multiple-choice items and 100 open-ended items scored by an LLM judge -- and report three headline findings. First, multi-agent verification is load-bearing: the independent verifier flags a majority of drafted items on first pass, most of which the one-shot repair loop resolves. Second, locally-hosted open-weights inference sits on the cost-performance Pareto front: a Gemma~4 model running on consumer hardware and a Cerebras-hosted 120B open-weights model dominate the near-zero-cost region, with the latter within one item of the top of the leaderboard. Third, MCQ and LLM-as-Judge rankings differ meaningfully: the MCQ scaffold inflates the performance ceiling, and Judge-mode evaluation is needed to discriminate at the frontier.

---


### 77. [Multi-Perspective Evidence Synthesis and Reasoning for Unsupervised Multimodal Entity Linking](https://arxiv.org/abs/2604.20283)

**<font color=#1a73e8>作者：</font>** Mo Zhou, Jianwei Wang, Kai Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Entity Linking (MEL) is a fundamental task in data management that maps ambiguous mentions with diverse modalities to the multimodal entities in a knowledge base. However, most existing MEL approaches primarily focus on optimizing instance-centric features and evidence, leaving broader forms of evidence and their intricate interdependencies insufficiently explored. Motivated by the observation that human expert decision-making process relies on multi-perspective judgment, in this work, we propose MSR-MEL, a Multi-perspective Evidence Synthesis and Reasoning framework with Large Language Models (LLMs) for unsupervised MEL. Specifically, we adopt a two-stage framework: (1) Offline Multi-Perspective Evidence Synthesis constructs a comprehensive set of evidence. This includes instance-centric evidence capturing the instance-centric multimodal information of mentions and entities, group-level evidence that aggregates neighborhood information, lexical evidence based on string overlap ratio, and statistical evidence based on simple summary statistics. A core contribution of our framework is the synthesis of group-level evidence, which effectively aggregates vital neighborhood information by graph. We first construct LLM-enhanced contextualized graphs. Subsequently, different modalities are jointly aligned through an asymmetric teacher-student graph neural network. (2) Online Multi-Perspective Evidence Reasoning leverages the power of LLM as a reasoning module to analyze the correlation and semantics of the multi-perspective evidence to induce an effective ranking strategy for accurate entity linking without supervision. Extensive experiments on widely used MEL benchmarks demonstrate that MSR-MEL consistently outperforms state-of-the-art unsupervised methods. The source code of this paper was available at: this https URL.

---


### 78. [X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289)

**<font color=#1a73e8>作者：</font>** Yixiao Zeng, Jianlei Zheng, Chaoda Zheng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time world simulation is becoming a key infrastructure for scalable evaluation and online reinforcement learning of autonomous driving systems. Recent driving world models built on autoregressive video diffusion achieve high-fidelity, controllable multi-camera generation, but their inference cost remains a bottleneck for interactive deployment. However, existing diffusion caching methods are designed for offline video generation with multiple denoising steps, and do not transfer to this scenario. Few-step distilled models have no inter-step redundancy left for these methods to reuse, and sequence-level parallelization techniques require future conditioning that closed-loop interactive generation does not provide. We present X-Cache, a training-free acceleration method that caches along a different axis: across consecutive generation chunks rather than across denoising steps. X-Cache maintains per-block residual caches that persist across chunks, and applies a dual-metric gating mechanism over a structure- and action-aware block-input fingerprint to independently decide whether each block should recompute or reuse its cached residual. To prevent approximation errors from permanently contaminating the autoregressive KV cache, X-Cache identifies KV update chunks (the forward passes that write clean keys and values into the persistent cache) and unconditionally forces full computation on these chunks, cutting off error propagation. We implement X-Cache on X-world, a production multi-camera action-conditioned driving world model built on multi-block causal DiT with few-step denoising and rolling KV cache. X-Cache achieves 71% block skip rate with 2.6x wall-clock speedup while maintaining minimum degradation.

---


### 79. [Odor Maps from the LLM-derived similarity scores](https://arxiv.org/abs/2604.20310)

**<font color=#1a73e8>作者：</font>** Yuki Harada, Manuel Aleixandre, Manabu Okumura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The application of large language models (LLMs) to OdorSpace analysis attracts growing interest. Recent studies have explored the comparison of sensory evaluation spaces derived from LLMs with odor character profiles in the Dravnieks' dataset. In this study, we calculated pairwise distances of odor descriptors using three distance measures and statistically compared these LLM-derived similarities with distances derived from the original data. Next, we extended this approach to odor names (ingredients). Statistical comparison revealed that LLMs can infer odor similarity to some degree, suggesting the potential of odor maps generated from these similarity data. Applying this approach, we generated an odor map of essential oils. It demonstrates that essential oils within the same group are closely located in the odor map, suggesting that the proximity in the odor map corresponds to human evaluation.

---


### 80. [R2IF: Aligning Reasoning with Decisions via Composite Rewards for Interpretable LLM Function Calling](https://arxiv.org/abs/2604.20316)

**<font color=#1a73e8>作者：</font>** Aijia Cheng, Kailong Wang, Ling Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Function calling empowers large language models (LLMs) to interface with external tools, yet existing RL-based approaches suffer from misalignment between reasoning processes and tool-call decisions. We propose R2IF, a reasoning-aware RL framework for interpretable function calling, adopting a composite reward integrating format/correctness constraints, Chain-of-Thought Effectiveness Reward (CER), and Specification-Modification-Value (SMV) reward, optimized via GRPO. Experiments on BFCL/ACEBench show R2IF outperforms baselines by up to 34.62% (Llama3.2-3B on BFCL) with positive Average CoT Effectiveness (0.05 for Llama3.2-3B), enhancing both function-calling accuracy and interpretability for reliable tool-augmented LLM deployment.

---


### 81. [MD-Face: MoE-Enhanced Label-Free Disentangled Representation for Interactive Facial Attribute Editing](https://arxiv.org/abs/2604.20317)

**<font color=#1a73e8>作者：</font>** Xuan Cui, Yunfei Zhao, Bo Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GAN-based facial attribute editing is widely used in virtual avatars and social media but often suffers from attribute entanglement, where modifying one face attribute unintentionally alters others. While supervised disentangled representation learning can address this, it relies heavily on labeled data, incurring high annotation costs. To address these challenges, we propose MD-Face, a label-free disentangled representation learning framework based on Mixture of Experts (MoE). MD-Face utilizes a MoE backbone with a gating mechanism that dynamically allocates experts, enabling the model to learn semantic vectors with greater independence. To further enhance attribute entanglement, we introduce a geometry-aware loss, which aligns each semantic vector with its corresponding Semantic Boundary Vector (SBV) through a Jacobian-based pushforward method. Experiments with ProGAN and StyleGAN show that MD-Face outperforms unsupervised baselines and competes with supervised ones. Compared to diffusion-based methods, it offers better image quality and lower inference latency, making it ideal for interactive editing.

---


### 82. [UniCVR: From Alignment to Reranking for Unified Zero-Shot Composed Visual Retrieval](https://arxiv.org/abs/2604.20318)

**<font color=#1a73e8>作者：</font>** Haokun Wen, Xuemeng Song, Haoyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed image retrieval, multi-turn composed image retrieval, and composed video retrieval all share a common paradigm: composing the reference visual with modification text to retrieve the desired target. Despite this shared structure, the three tasks have been studied in isolation, with no prior work proposing a unified framework, let alone a zero-shot solution. In this paper, we propose UniCVR, the first unified zero-shot composed visual retrieval framework that jointly addresses all three tasks without any task-specific human-annotated data. UniCVR strategically combines two complementary strengths: Multimodal Large Language Models (MLLMs) for compositional query understanding and Vision-Language Pre-trained (VLP) models for structured visual retrieval. Concretely, UniCVR operates in two stages. In Stage I, we train the MLLM as a compositional query embedder via contrastive learning on a curated multi-source dataset of approximately 3.5M samples, bridging the heterogeneous embedding spaces between the MLLM and the frozen VLP gallery encoder. A cluster-based hard negative sampling strategy is proposed to strengthen contrastive supervision. In Stage II, we introduce an MLLM-guided dual-level reranking mechanism that applies adaptive budgeted subset scoring to a small number of top-ranked candidates, and then exploits the resulting relevance signals through a dual-level re-scoring scheme, producing more accurate final rankings with minimal computational overhead. Extensive experiments across five benchmarks covering all three tasks demonstrate that UniCVR achieves cutting-edge performance, validating its effectiveness and generalizability. Our data and code will be released upon acceptance.

---


### 83. [SurgCoT: Advancing Spatiotemporal Reasoning in Surgical Videos through a Chain-of-Thought Benchmark](https://arxiv.org/abs/2604.20319)

**<font color=#1a73e8>作者：</font>** Gui Wang, YongSong Zhou, Kaijun Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained spatiotemporal reasoning on surgical videos is critical, yet the capabilities of Multi-modal Large Language Models (MLLMs) in this domain remain largely unexplored. To bridge this gap, we introduce SurgCoT, a unified benchmark for evaluating chain-of-thought (CoT) reasoning in MLLMs across 7 surgical specialties and 35 diverse procedures. SurgCoT assesses five core reasoning dimensions: Causal Action Ordering, Cue-Action Alignment, Affordance Mapping, Micro-Transition Localization, and Anomaly Onset Tracking, through a structured CoT framework with an intensive annotation protocol (Question-Option-Knowledge-Clue-Answer), where the Knowledge field provides essential background context and Clue provides definitive spatiotemporal evidence. Evaluation of 10 leading MLLMs shows: 1) commercial models outperform open-source and medical-specialized variants; 2) significant gaps exist in surgical CoT reasoning; 3) SurgCoT enables effective evaluation and enhances progressive spatiotemporal reasoning. SurgCoT provides a reproducible testbed to narrow the gap between MLLM capabilities and clinical reasoning demands. Code: this https URL.

---


### 84. [Hybrid Latent Reasoning with Decoupled Policy Optimization](https://arxiv.org/abs/2604.20328)

**<font color=#1a73e8>作者：</font>** Tao Cheng, Shi-Zhe Chen, Hao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) reasoning significantly elevates the complex problem-solving capabilities of multimodal large language models (MLLMs). However, adapting CoT to vision typically discretizes signals to fit LLM inputs, causing early semantic collapse and discarding fine-grained details. While external tools can mitigate this, they introduce a rigid bottleneck, confining reasoning to predefined operations. Although recent latent reasoning paradigms internalize visual states to overcome these limitations, optimizing the resulting hybrid discrete-continuous action space remains challenging. In this work, we propose HyLaR (Hybrid Latent Reasoning), a framework that seamlessly interleaves discrete text generation with continuous visual latent representations. Specifically, following an initial cold-start supervised fine-tuning (SFT), we introduce DePO (Decoupled Policy Optimization) to enable effective reinforcement learning within this hybrid space. DePO decomposes the policy gradient objective, applying independent trust-region constraints to the textual and latent components, alongside an exact closed-form von Mises-Fisher (vMF) KL regularizer. Extensive experiments demonstrate that HyLaR outperforms standard MLLMs and state-of-the-art latent reasoning approaches across fine-grained perception and general multimodal understanding benchmarks. Code is available at this https URL.

---


### 85. [Surrogate modeling for interpreting black-box LLMs in medical predictions](https://arxiv.org/abs/2604.20331)

**<font color=#1a73e8>作者：</font>** Changho Han, Songsoo Kim, Dong Won Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs), trained on vast datasets, encode extensive real-world knowledge within their parameters, yet their black-box nature obscures the mechanisms and extent of this encoding. Surrogate modeling, which uses simplified models to approximate complex systems, can offer a path toward better interpretability of black-box models. We propose a surrogate modeling framework that quantitatively explains LLM-encoded knowledge. For a specific hypothesis derived from domain knowledge, this framework approximates the latent LLM knowledge space using observable elements (input-output pairs) through extensive prompting across a comprehensive range of simulated scenarios. Through proof-of-concept experiments in medical predictions, we demonstrate our framework's effectiveness in revealing the extent to which LLMs "perceive" each input variable in relation to the output. Particularly, given concerns that LLMs may perpetuate inaccuracies and societal biases embedded in their training data, our experiments using this framework quantitatively revealed both associations that contradict established medical knowledge and the persistence of scientifically refuted racial assumptions within LLM-encoded knowledge. By disclosing these issues, our framework can act as a red-flag indicator to support the safe and reliable application of these models.

---


### 86. [X-PCR: A Benchmark for Cross-modality Progressive Clinical Reasoning in Ophthalmic Diagnosis](https://arxiv.org/abs/2604.20350)

**<font color=#1a73e8>作者：</font>** Gui Wang, Zehao Zhong, YongSong Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant progress in Multi-modal Large Language Models (MLLMs), their clinical reasoning capacity for multi-modal diagnosis remains largely unexamined. Current benchmarks, mostly single-modality data, can't evaluate progressive reasoning and cross-modal integration essential for clinical practice. We introduce the Cross-Modality Progressive Clinical Reasoning (X-PCR) benchmark, the first comprehensive evaluation of MLLMs through a complete ophthalmology diagnostic workflow, with two reasoning tasks: 1) a six-stage progressive reasoning chain spanning image quality assessment to clinical decision-making, and 2) a cross-modality reasoning task integrating six imaging modalities. The benchmark comprises 26,415 images and 177,868 expert-verified VQA pairs curated from 51 public datasets, covering 52 ophthalmic diseases. Evaluation of 21 MLLMs reveals critical gaps in progressive reasoning and cross-modal integration. Dataset and code: this https URL.

---


### 87. [Object Referring-Guided Scanpath Prediction with Perception-Enhanced Vision-Language Models](https://arxiv.org/abs/2604.20361)

**<font color=#1a73e8>作者：</font>** Rong Quan, Yantao Lai, Dong Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object Referring-guided Scanpath Prediction (ORSP) aims to predict the human attention scanpath when they search for a specific target object in a visual scene according to a linguistic description describing the object. Multimodal information fusion is a key point of ORSP. Therefore, we propose a novel model, ScanVLA, to first exploit a Vision-Language Model (VLM) to extract and fuse inherently aligned visual and linguistic feature representations from the input image and referring expression. Next, to enhance the ScanVLA's perception of fine-grained positional information, we not only propose a novel History Enhanced Scanpath Decoder (HESD) that directly takes historical fixations' position information as input to help predict a more reasonable position for the current fixation, but also adopt a frozen Segmentation LoRA as an auxiliary component to help localize the referred object more precisely, which improves the scanpath prediction task without incurring additional large computational and time costs. Extensive experimental results demonstrate that ScanVLA can significantly outperform existing scanpath prediction methods under object referring.

---


### 88. [Mitigating Hallucinations in Large Vision-Language Models without Performance Degradation](https://arxiv.org/abs/2604.20366)

**<font color=#1a73e8>作者：</font>** Xingyu Zhu, Junfeng Fang, Shuo Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) exhibit powerful generative capabilities but frequently produce hallucinations that compromise output reliability. Fine-tuning on annotated data devoid of hallucinations offers the most direct solution, while its high computational cost motivates recent representation-based methods, which focus on mitigating hallucinatory components within hidden representations. Though efficient, we empirically observe that these methods degrade general generation capacity due to incomplete extraction of hallucination components and non-selective parameter updates. To address these limitations, we propose MPD, a dual-stage framework for mitigating hallucinations without performance degradation. Specifically, our MPD relies on two essential factors: (1) semantic-aware component disentanglement to extract pure hallucination components, and (2) interpretable parameter updates that selectively modify parameters most relevant to hallucination. Extensive experiments demonstrate that MPD achieves state-of-the-art performance, reducing hallucinations by 23.4\% while maintaining 97.4\% of general generative capability as evaluated on LLaVA-Bench and MME, with no additional computational cost.

---


### 89. [Graph2Counsel: Clinically Grounded Synthetic Counseling Dialogue Generation from Client Psychological Graphs](https://arxiv.org/abs/2604.20382)

**<font color=#1a73e8>作者：</font>** Aishik Mandal, Hiba Arnaout, Clarissa W. Ong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rising demand for mental health support has increased interest in using Large Language Models (LLMs) for counseling. However, adapting LLMs to this high-risk safety-critical domain is hindered by the scarcity of real-world counseling data due to privacy constraints. Synthetic datasets provide a promising alternative, but existing approaches often rely on unstructured or semi-structured text inputs and overlook structural dependencies between a client's cognitive, emotional, and behavioral states, often producing psychologically inconsistent interactions and reducing data realism and quality. We introduce Graph2Counsel, a framework for generating synthetic counseling sessions grounded in Client Psychological Graphs (CPGs) that encode relationships among clients' thoughts, emotions, and behaviors. Graph2Counsel employs a structured prompting pipeline guided by counselor strategies and CPG, and explores prompting strategies including CoT (Wei et al., 2022) and Multi-Agent Feedback (Li et al., 2025a). Graph2Counsel produces 760 sessions from 76 CPGs across diverse client profiles. In expert evaluation, our dataset outperforms prior datasets on specificity, counselor competence, authenticity, conversational flow, and safety, with substantial inter-annotator agreement (Krippendorff's $\alpha$ = 0.70). Fine-tuning an open-source model on this dataset improves performance on CounselingBench (Nguyen et al., 2025) and CounselBench (Li et al., 2025b), showing downstream utility. We also make our code and data public.

---


### 90. [WebGen-R1: Incentivizing Large Language Models to Generate Functional and Aesthetic Websites with Reinforcement Learning](https://arxiv.org/abs/2604.20398)

**<font color=#1a73e8>作者：</font>** Juyong Jiang, Chenglin Cai, Chansung Park 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) excel at function-level code generation, project-level tasks such as generating functional and visually aesthetic multi-page websites remain highly challenging. Existing works are often limited to single-page static websites, while agentic frameworks typically rely on multi-turn execution with proprietary models, leading to substantial token costs, high latency, and brittle integration. Training a small LLM end-to-end with reinforcement learning (RL) is a promising alternative, yet it faces a critical bottleneck in designing reliable and computationally feasible rewards for website generation. Unlike single-file coding tasks that can be verified by unit tests, website generation requires evaluating inherently subjective aesthetics, cross-page interactions, and functional correctness. To this end, we propose WebGen-R1, an end-to-end RL framework tailored for project-level website generation. We first introduce a scaffold-driven structured generation paradigm that constrains the large open-ended action space and preserves architectural integrity. We then design a novel cascaded multimodal reward that seamlessly couples structural guarantees with execution-grounded functional feedback and vision-based aesthetic supervision. Extensive experiments demonstrate that our WebGen-R1 substantially transforms a 7B base model from generating nearly nonfunctional websites into producing deployable, aesthetically aligned multi-page websites. Remarkably, our WebGen-R1 not only consistently outperforms heavily scaled open-source models (up to 72B), but also rivals the state-of-the-art DeepSeek-R1 (671B) in functional success, while substantially exceeding it in valid rendering and aesthetic alignment. These results position WebGen-R1 as a viable path for scaling small open models from function-level code generation to project-level web application generation.

---


### 91. [Fast-then-Fine: A Two-Stage Framework with Multi-Granular Representation for Cross-Modal Retrieval in Remote Sensing](https://arxiv.org/abs/2604.20429)

**<font color=#1a73e8>作者：</font>** Xi Chen, Xu Chen, Xiangyang Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing (RS) image-text retrieval plays a critical role in understanding massive RS imagery. However, the dense multi-object distribution and complex backgrounds in RS imagery make it difficult to simultaneously achieve fine-grained cross-modal alignment and efficient retrieval. Existing methods either rely on complex cross-modal interactions that lead to low retrieval efficiency, or depend on large-scale vision-language model pre-training, which requires massive data and computational resources. To address these issues, we propose a fast-then-fine (FTF) two-stage retrieval framework that decomposes retrieval into a text-agnostic recall stage for efficient candidate selection and a text-guided rerank stage for fine-grained alignment. Specifically, in the recall stage, text-agnostic coarse-grained representations are employed for efficient candidate selection; in the rerank stage, a parameter-free balanced text-guided interaction block enhances fine-grained alignment without introducing additional learnable parameters. Furthermore, an inter- and intra-modal loss is designed to jointly optimize cross-modal alignment across multi-granular representations. Extensive experiments on public benchmarks demonstrate that the FTF achieves competitive retrieval accuracy while significantly improving retrieval efficiency compared with existing methods.

---


### 92. [DialToM: A Theory of Mind Benchmark for Forecasting State-Driven Dialogue Trajectories](https://arxiv.org/abs/2604.20443)

**<font color=#1a73e8>作者：</font>** Neemesh Yadav, Palakorn Achananuparp, Jing Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been shown to possess Theory of Mind (ToM) abilities. However, it remains unclear whether this stems from robust reasoning or spurious correlations. We introduce DialToM, a human-verified benchmark built from natural human dialogue using a multiple-choice framework. We evaluate not only mental state prediction (Literal ToM) but also the functional utility of these states (Functional ToM) through Prospective Diagnostic Forecasting -- probing whether models can identify state-consistent dialogue trajectories solely from mental-state profiles. Our results reveal a significant reasoning asymmetry: while LLMs excel at identifying mental states, most (except for Gemini 3 Pro) fail to leverage this understanding to forecast social trajectories. Additionally, we find only weak semantic similarities between human and LLM-generated inferences. To facilitate reproducibility, the DialToM dataset and evaluation code are publicly available at this https URL.

---


### 93. [CCTVBench: Contrastive Consistency Traffic VideoQA Benchmark for Multimodal LLMs](https://arxiv.org/abs/2604.20460)

**<font color=#1a73e8>作者：</font>** Xingcheng Zhou, Hao Guo, Rui Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Safety-critical traffic reasoning requires contrastive consistency: models must detect true hazards when an accident occurs, and reliably reject plausible-but-false hypotheses under near-identical counterfactual scenes. We present CCTVBench, a Contrastive Consistency Traffic VideoQA Benchmark built on paired real accident videos and world-model-generated counterfactual counterparts, together with minimally different, mutually exclusive hypothesis questions. CCTVBench enforces a single structured decision pattern over each video question quadruple and provides actionable diagnostics that decompose failures into positive omission, positive swap, negative hallucination, and mutual-exclusivity violation, while separating video versus question consistency. Experiments across open-source and proprietary video LLMs reveal a large and persistent gap between standard per-instance QA metrics and quadruple-level contrastive consistency, with unreliable none-of-the-above rejection as a key bottleneck. Finally, we introduce C-TCD, a contrastive decoding approach leveraging a semantically exclusive counterpart video as the contrast input at inference time, improving both instance-level QA and contrastive consistency.

---


### 94. [Video-ToC: Video Tree-of-Cue Reasoning](https://arxiv.org/abs/2604.20473)

**<font color=#1a73e8>作者：</font>** Qizhong Tan, Zhuotao Tian, Guangming Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Video Large Language Models (Video LLMs) struggle with complex video understanding, exhibiting limited reasoning capabilities and potential hallucinations. In particular, these methods tend to perform reasoning solely relying on the pretrained inherent reasoning rationales whilst lacking perception-aware adaptation to the input video content. To address this, we propose \textbf{Video-ToC}, a novel video reasoning framework that enhances video understanding through tree-of-cue reasoning. Specifically, our approach introduces three key innovations: (1) A tree-guided visual cue localization mechanism, which endows the model with enhanced fine-grained perceptual capabilities through structured reasoning patterns; (2) A reasoning-demand reward mechanism, which dynamically adjusts the reward value for reinforcement learning (RL) based on the estimation of reasoning demands, enabling on-demand incentives for more effective reasoning strategies; and (3) An automated annotation pipeline that constructs the Video-ToC-SFT-1k and Video-ToC-RL-2k datasets for supervised fine-tuning (SFT) and RL training, respectively. Extensive evaluations on six video understanding benchmarks and a video hallucination benchmark demonstrate the superiority of Video-ToC over baselines and recent methods. Code is available at this https URL.

---


### 95. [ProMMSearchAgent: A Generalizable Multimodal Search Agent Trained with Process-Oriented Rewards](https://arxiv.org/abs/2604.20486)

**<font color=#1a73e8>作者：</font>** Wentao Yan, Shengqin Wang, Huichi Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training multimodal agents via reinforcement learning for knowledge-intensive visual reasoning is fundamentally hindered by the extreme sparsity of outcome-based supervision and the unpredictability of live web environments. To resolve these algorithmic and environmental bottlenecks, we introduce ProMMSearchAgent, establishing a novel Sim-to-Real training paradigm for multimodal search.
We decouple policy learning into a deterministic, local static sandbox. Crucially, to learn effectively within this constrained environment, we propose an introspective process-oriented reward. By probing the agent's own parametric knowledge boundaries, we generate dense behavioral metadata that explicitly rewards the correct cognitive decision, initiating a multimodal or text search only when visually or factually uncertain. Extensive experiments demonstrate that our locally-trained policy transfers zero-shot to the live Google Search API. ProMMSearchAgent achieves new SOTA performance, outperforming MMSearch-R1 by +5.1% on FVQA-test, +6.3% on InfoSeek, and +11.3% on MMSearch.

---


### 96. [Knowledge Capsules: Structured Nonparametric Memory Units for LLMs](https://arxiv.org/abs/2604.20487)

**<font color=#1a73e8>作者：</font>** Bin Ju, Shenfeng Weng, Danying Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) encode knowledge in parametric weights, making it costly to update or extend without retraining. Retrieval-augmented generation (RAG) mitigates this limitation by appending retrieved text to the input, but operates purely through context expansion, where external knowledge competes as tokens within the attention mechanism. As a result, its influence is indirect and often unstable, particularly in long context and multi hop reasoning scenarios. We propose Knowledge Capsules, structured nonparametric memory units that represent normalized relational knowledge and can be constructed directly from document corpora using a frozen base model. Instead of injecting knowledge as text, we introduce an External Key Value Injection (KVI) framework that compiles capsules into attention-compatible key value representations, enabling external knowledge to directly participate in the model's attention computation. By shifting knowledge integration from context-level augmentation to memory level interaction, the proposed framework consistently outperforms RAG and GraphRAG across multiple QA benchmarks, with improved stability and accuracy in long context and multi hop reasoning, while requiring no parameter updates.

---


### 97. [CHASM: Unveiling Covert Advertisements on Chinese Social Media](https://arxiv.org/abs/2604.20511)

**<font color=#1a73e8>作者：</font>** Jingyi Zheng, Tianyi Hu, Yule Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current benchmarks for evaluating large language models (LLMs) in social media moderation completely overlook a serious threat: covert advertisements, which disguise themselves as regular posts to deceive and mislead consumers into making purchases, leading to significant ethical and legal concerns. In this paper, we present the CHASM, a first-of-its-kind dataset designed to evaluate the capability of Multimodal Large Language Models (MLLMs) in detecting covert advertisements on social media. CHASM is a high-quality, anonymized, manually curated dataset consisting of 4,992 instances, based on real-world scenarios from the Chinese social media platform Rednote. The dataset was collected and annotated under strict privacy protection and quality control protocols. It includes many product experience sharing posts that closely resemble covert advertisements, making the dataset particularly this http URL results show that under both zero-shot and in-context learning settings, none of the current MLLMs are sufficiently reliable for detecting covert this http URL further experiments revealed that fine-tuning open-source MLLMs on our dataset yielded noticeable performance gains. However, significant challenges persist, such as detecting subtle cues in comments and differences in visual and textual this http URL provide in-depth error analysis and outline future research directions. We hope our study can serve as a call for the research community and platform moderators to develop more precise defenses against this emerging threat.

---


### 98. [Toward Cross-Lingual Quality Classifiers for Multilingual Pretraining Data Selection](https://arxiv.org/abs/2604.20549)

**<font color=#1a73e8>作者：</font>** Yassine Turki, Vinko Sabolčec, Bettina Messmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) scale, data curation has shifted from maximizing volume to optimizing the signal-to-noise ratio by performing quality filtering. However, for many languages, native high quality data is insufficient to train robust quality classifiers. This work investigates the idea that quality markers in embedding space may show cross-lingual consistency, which would allow high-resource languages to subsidize the filtering of low-resource ones. We evaluate various filtering strategies, including cross-lingual transfer, third quartile sampling (Q3), and retention rate tuning. Our results demonstrate that massive multilingual pooling frequently outperforms monolingual baselines in both rank stability and aggregate accuracy for a 1B model trained on 103B tokens, delivering gains for high resource languages (1.2% increase in aggregate normalized accuracy for French) and matching or exceeding monolingual baselines for low-resource languages. However, we find that scale alone does not guarantee stability. Furthermore, for high-resource languages like French, we show that refining the decision boundary through third quartile sampling (Q3) or tuning the retention rate is necessary to fully leverage the multilingual signal.

---


### 99. [LayerTracer: A Joint Task-Particle and Vulnerable-Layer Analysis framework for Arbitrary Large Language Model Architectures](https://arxiv.org/abs/2604.20556)

**<font color=#1a73e8>作者：</font>** Yuhang Wu, Qinyuan Liu, Qiuyang Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Currently, Large Language Models (LLMs) feature a diversified architectural landscape, including traditional Transformer, GateDeltaNet, and Mamba. However, the evolutionary laws of hierarchical representations, task knowledge formation positions, and network robustness bottleneck mechanisms in various LLM architectures remain unclear, posing core challenges for hybrid architecture design and model optimization. This paper proposes LayerTracer, an architecture-agnostic end-to-end analysis framework compatible with any LLM architecture. By extracting hidden states layer-by-layer and mapping them to vocabulary probability distributions, it achieves joint analysis of task particle localization and layer vulnerability quantification. We define the task particle as the key layer where the target token probability first rises significantly, representing the model's task execution starting point, and the vulnerable layer is defined as the layer with the maximum Jensen-Shannon (JS) divergence between output distributions before and after mask perturbation, reflecting its sensitivity to disturbances. Experiments on models of different parameter scales show that task particles mainly appear in the deep layers of the model regardless of parameter size, while larger-parameter models exhibit stronger hierarchical robustness. LayerTracer provides a scientific basis for layer division, module ratio, and gating switching of hybrid architectures, effectively optimizing model performance. It accurately locates task-effective layers and stability bottlenecks, offering universal support for LLM structure design and interpretability research.

---


### 100. [LLM StructCore: Schema-Guided Reasoning Condensation and Deterministic Compilation](https://arxiv.org/abs/2604.20560)

**<font color=#1a73e8>作者：</font>** Serhii Zabolotnii  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatically filling Case Report Forms (CRFs) from clinical notes is challenging due to noisy language, strict output contracts, and the high cost of false positives. We describe our CL4Health 2026 submission for Dyspnea CRF filling (134 items) using a contract-driven two-stage design grounded in Schema-Guided Reasoning (SGR). The key task property is extreme sparsity: the majority of fields are unknown, and official scoring penalizes both empty values and unsupported predictions. We shift from a single-step "LLM predicts 134 fields" approach to a decomposition where (i) Stage 1 produces a stable SGR-style JSON summary with exactly 9 domain keys, and (ii) Stage 2 is a fully deterministic, 0-LLM compiler that parses the Stage 1 summary, canonicalizes item names, normalizes predictions to the official controlled vocabulary, applies evidence-gated false-positive filters, and expands the output into the required 134-item format. On the dev80 split, the best teacher configuration achieves macro-F1 0.6543 (EN) and 0.6905 (IT); on the hidden test200, the submitted English variant scores 0.63 on Codabench. The pipeline is language-agnostic: Italian results match or exceed English with no language-specific engineering.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-129](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
