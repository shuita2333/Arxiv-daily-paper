# 🧠 大模型相关研究 | 2026年09月17日

> 本类共 **189** 篇论文：已确认 **180** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-189](./part-04.md)

---

### 51. [Breaking the 1.58-bit Barrier for Ternary LLMs](https://arxiv.org/abs/2609.16338)

**<font color=#1a73e8>作者：</font>** Evangelos Georganas, Alexander Heinecke, Pradeep Dubey  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ternary Large Language Models (LLM) store every weight as one of three symbols $\{-1,0,+1\}$, so the cost of a ternary model is conventionally referenced to the information-theoretic $\log_2 3 \approx 1.585$ bits per weight. The prevailing deployment format packs five ternary weights into one byte (five-trit packing), and due to the power-of-two group sizes used in practice this rounds up to $1.625$ bits per weight. This effective storage bit-width treats the three symbols $\{-1,0,+1\}$ as equiprobable. We measure the actual symbol distribution of 29 ternary LLM models and find that zeros account for up to $51.5\%$ of all weights. Motivated by this finding, we introduce BITCOS, a simple distribution-adaptive layout comprised of a dense presence bitmap plus a compacted sign vector, and costs $2 - z$ bits per weight element given a zero density $z$ in the model's weights. BITCOS stores weights more compactly than the five-trit packing in 26 of the 29 tested models, and reaches $1.485$ bits per weight on the sparsest of them. BITCOS is amenable to efficient unpacking on modern processors and GPUs, and we present optimized unpacking sequences for AVX-512, AVX2 and Intel Xe2 GPUs. Measured against production state-of-the-art ternary matrix-vector multiplication kernels, at the zero densities real-world ternary models exhibit, the realized gain with our proposed layout is up to $1.28\times$. Finally, we illustrate end-to-end LLM inference results on 5 different platforms (client and server CPUs, integrated and discrete Xe2 GPUs) where decode throughput improves by up to $1.18\times$ on CPUs and $1.27\times$ on GPUs.

---


### 52. [StalePO: Anchored Token-Level Preference Optimization using Legacy Post-Edits in Machine Translation](https://arxiv.org/abs/2609.16340)

**<font color=#1a73e8>作者：</font>** Rohit Dhaipule, Sukhdeep Singh Kharbanda, Prasanth Bathala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine translation systems are periodically upgraded to stronger models, but the available preference signal is human post-edits of an older system's outputs, which the newer model may already surpass. Moreover, collecting fresh post-edits for every new model is prohibitively expensive. We call this the Stale Preference problem. Standard DPO can fail in this setting: it may increase the likelihood of inferior post-edits, erode the model's existing quality, and fail to provide the per-token control needed to correct localized errors. We introduce StalePO, an objective derived from three requirements this regime imposes. Likelihood movement must be downward on both responses, the policy must be anchored to its own base response, and the KL constraint must apply at the token level. These requirements are jointly necessary. In ablations, each mechanism in isolation leaves the model's performance indistinguishable from the base model, and only their combination converts stale feedback into gains. On English-to-Hindi and English-to-Turkish localization data, StalePO improves the fraction of segments passing all LLM-as-judge MQM quality checks by 14.9 and 4.6 percentage points, respectively, with gains concentrated on style and fluency. A human evaluation under the same framework confirms these gains on English-to-Hindi, raising the fraction of segments passing all seven human checks by 13.8 percentage points.

---


### 53. [How Humans and LLMs Read Gender into Gender-Neutral Physical Descriptions](https://arxiv.org/abs/2609.16366)

**<font color=#1a73e8>作者：</font>** Yingjia Wan, Lin Lin, Elisa Kreiss  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When foundation models describe people, recent work in AI fairness, accessibility, and ethics recommends avoiding inferred identity labels (e.g., "she", "his") in favor of seemingly "objective" physical descriptions (e.g., "short hair", "a defined jawline"). Yet whether such descriptive language achieves gender-neutral communication remains an open empirical question. To study this, we introduce GAPA (Gender Associations of Physical Attributes), a dataset of 316 common physical attributes drawn from diverse sources, paired with 14,706 gender-association ratings from 304 US-based annotators. Results show that physical descriptions carry structured and graded gender associations among readers, with more consistent and distinctive associations for women and men than for non-binary identities. Next, we evaluate 16 LLMs across model families, sizes, and post-training variants against human ratings. The models partially recover human associations but exhibit systematic alignment biases, including compressed rating distributions, weaker alignment for associations with men, and asymmetric abstention that disproportionately targets the non-binary category. Finally, we release the best-performing proxy model trained to predict humans' gender associations of descriptive language and demonstrate its utility through a sociolinguistic analysis of character descriptions in LitBank. Together, our findings provide the first empirical evidence that seemingly "objective" physical descriptions can retain systematic gender associations in human interpretation, and uncover systematic patterns of model-human misalignment. This challenges the assumption that replacing explicit gender labels with physical descriptions necessarily yields gender-neutral communication, and highlights downstream challenges in using such descriptions to communicate subjective identity categories in human-AI interaction.

---


### 54. [Register Tokens for Bounded-State Reasoning in Diffusion Language Models](https://arxiv.org/abs/2609.16372)

**<font color=#1a73e8>作者：</font>** Albert Ge, Chandan Singh, Yufan Zhuang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (dLLMs) generate text by iteratively denoising masked tokens with bidirectional attention. Extending reasoning across generation chunks normally requires keeping earlier generated text in context. We ask whether a dLLM can instead continue reasoning after that text is cleared, using only a fixed-size carried state. We implement this state as a small number of register tokens: dedicated fixed-position tokens whose continuous hidden states are trained to carry reasoning progress across generation chunks. We post-train dLLMs to decode a chunk of text, clear it while preserving the register values, and continue decoding from the prompt and carried state. In our main comparisons on LLaDA and Dream, registers outperform discrete-text carry on every benchmark, with gains of up to 8.5 points on math and 19.5 points on code. Registers are especially effective for bounded code generation, where correct programs usually span several chunks. Finally, registers can be further refined with reinforcement learning on long-horizon reasoning tasks.

---


### 55. [When a Story Feels Like Mine: How Personalized Narratives and Humor Shape Older Adults' Empathy toward LLM-Generated Peer Health Stories](https://arxiv.org/abs/2609.16374)

**<font color=#1a73e8>作者：</font>** Kexin Quan, Precious Olalere, Smit Desai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Peer stories have been shown to boost self-efficacy in older adults' health behavior change. Despite their effectiveness, peer stories are difficult to deploy in health promotion at scale given the difficulty of matching the diverse health concerns and coping styles of heterogeneous older populations. Large language models (LLMs) have been shown to generate authentic narratives, yet how personalization and narrative affective style, such as humor, jointly shape older adults' responses remains unknown. We developed a theory-driven system that generates first-person peer health narratives varying in personalization and humor through a three-stage LLM pipeline grounded in self-efficacy mechanisms. Thirty-one older adults were invited to participate in a within-subjects lab study. Results showed that personalization increased perceived relatability and relevance of peer stories, especially for older adults with lower humor preference. These findings position individual differences in affective styles as a second dimension in designing personalization for LLM-assisted health communication.

---


### 56. [Attention Mean Fields Predict Average Representation Dynamics and Reveal Context-Specific Computation](https://arxiv.org/abs/2609.16382)

**<font color=#1a73e8>作者：</font>** Micah Adler, John W. Byers, Mark Crovella  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A language model's representation geometry is not predetermined; it evolves as the model runs. A faithful account of that geometry must capture that dynamic process, and so cannot be based solely on model-independent statistics such as co-occurrence. Here we introduce a mean-field analysis of attention. The average attention from one token to another defines a kernel that carries representations layer to layer and can be iterated through the network to model how the geometry is transformed. We condition this average two ways. Conditioned on a whole corpus, the kernel predicts the average-case evolution of representation geometry. Conditioned instead on a single context, it predicts the expected geometry for that context. A head's departure from that prediction, its \emph{mean-field deviation}, isolates the context-specific computation that the mean field misses.
Under the corpus-conditional reading, the kernel yields an open-loop model: from the input embeddings and the frozen weights alone, we can iterate the kernel and the model's own MLPs over token representations, never consulting a measured deviation at any layer. The resulting prediction is highly accurate.
In early training the model and its corpus mean field are indistinguishable. Replace every attention head with its mean field, and the substitution leaves the loss on real text unchanged. Around the onset of induction, the two diverge, and the gap widens as representations become contextualized.
Under the context-conditional reading, deviation from the mean field is a task-agnostic measure of context-specific computation. The residual decomposes additively into unusual attention routing and contextualization of the transported values. Across controlled induction and few-shot settings, greater deviation tracks greater reliance on in-context information.

---


### 57. [Reasoning with Image Generation](https://arxiv.org/abs/2609.16409)

**<font color=#1a73e8>作者：</font>** Nishad Singhi, Hector Garcia Rodriguez, Aditya Arora 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought reasoning has revolutionized natural language processing by enabling large language models (LLMs) to decompose problems into intermediate steps before answering. Yet confining reasoning to the textual domain presents limitations for tasks requiring direct manipulation of visual representations. Recent efforts augment multimodal LLMs with external visual expert tools such as depth estimation or object detection modules, but these remain fundamentally limited by their reliance on narrow, rigid operations that cannot flexibly generate or transform visual content. We propose ReImaGin, which leverages image generation models as a flexible visual reasoning mechanism for multimodal LLMs: unlike fixed-function tools, they accept natural language commands and can perform open-ended visual operations, like removing an occlusion or generating a floorplan from multiple disjoint views of a room. Across six diverse visual reasoning tasks including multi-view spatial reasoning and collision prediction, ReImaGin consistently outperforms both text-only reasoning and specialist vision-tool baselines, with gains of up to 25\%, demonstrating the advantage of flexible, generative visual reasoning.

---


### 58. [ReMova: Fine-tuning LLMs for English to Belarusian translation](https://arxiv.org/abs/2609.16427)

**<font color=#1a73e8>作者：</font>** Mikita Pilinka, Aliaksandr Kliujeŭ, David Samuel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a Belarusian-specific data-cleaning pipeline and fine-tuning for English-Belarusian machine translation. Our cleaning pipeline distinguishes itself from others by employing a correction tool that addresses the issue of the two orthographies of the Belarusian language, noise in the training data, interference from other languages and other misspelling issues common in Belarusian on the internet. A matched ablation on unfiltered training data shows substantial benefits from filtering for all fine-tuned models, with the LLM-based models gaining roughly twice as much from filtering as the dedicated encoder-decoder MT system, supporting the view that for Belarusian MT one of the primary bottlenecks is data quality.

---


### 59. [A light-touch AI literacy intervention helps protect against AI political persuasion](https://arxiv.org/abs/2609.16432)

**<font color=#1a73e8>作者：</font>** Reed Orchinik, David Rand  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversations with large language models (LLMs) can substantially shift beliefs and attitudes, raising concerns about manipulation using AI persuasion. Here we test whether a light-touch AI literacy intervention - a brief warning that LLMs can be prompted to persuade and may present information selectively - helps protect users. Across two experiments (total N = 3,208 Americans) in which participants conversed with an LLM instructed to shift their views about different political topics, the presence of a warning reduced belief change by roughly one-half (-48.1%, 95% CI [-59.5%, -36.8%]) relative to the control. Importantly, the warning did not significantly reduce trust in generative AI more broadly. Light-touch literacy interventions can help protect users against AI political persuasion.

---


### 60. [Evaluating the NIST Bugs Framework Against CWE as a Successor for Automated Vulnerability Classification](https://arxiv.org/abs/2609.16433)

**<font color=#1a73e8>作者：</font>** Md Nazmul Hoque, Shaswata Mitra, Subash Neupane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability classification based on root cause weaknesses is essential for numerous cybersecurity activities, where the Common Weakness Enumeration (CWE) serves as a public repository of such flaws. However, its overlapping entries create a non-orthogonal structure. The result is the same vulnerability being mapped to multiple weaknesses, complicating Root Cause Analysis (RCA) and triage. To address this, NIST Special Publication 800-231 introduces the Bugs Framework (BF), which organizes vulnerabilities into <cause, operation, consequence> triples and links such triples into a causal chain, so that a vulnerability carries its root cause and its sink together instead of a single terminal label. To date, however, BF has been specified but not evaluated regarding its performance against the challenges to automated classification. The evidence required for adoption has not been investigated empirically. We evaluate BF as a classification target and a complement to CWE using a systematically screened corpus of automated Common Vulnerabilities and Exposures (CVEs) linked to CWE research. We assess the reproducibility of CVE-to-BF classification through two evaluations. The first is qualitative: an anonymized inter-rater study in which 2 subject-matter experts (SMEs) independently mapped 13 CVEs onto the four BF axes. Annotators showed strong agreement on the cause and operation axes, while the attribute axis indicated fair agreement. We also tested our automated framework across two large language model (LLM) deployments under different budgets for reproducibility analysis. Despite limitations, such as evidence availability and the absence of retrievable fix commits for closed-source software, our findings support the claim that BF is a more structured and automation-friendly framework than CWE. Our exploration reveals specific gaps in BF, including under-specified guidance on attributes.

---


### 61. [Interpreting and Steering LLM Agents for Social Simulations](https://arxiv.org/abs/2609.16436)

**<font color=#1a73e8>作者：</font>** Jiayue Gaveal Fan, Arul Murugan, Shreyas Krishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulations based on large language models (LLMs) have proven to be powerful for understanding human behavior, making them valuable additions to the social scientific toolkit. However, LLMs are ultimately black boxes based on deep neural networks which limits their value for social science. This is because of a lack of (i) interpretability: i.e. the ability to assign clear mechanisms driving observed behavior; and a lack of (ii) steerability: i.e. the ability to mute or amplify specific theoretically meaningful mechanisms of action to drive specific model behavior. Here, we demonstrate how the black box could be opened up to further enrich LLM-based simulations. Specifically, we compare three types of methods: (1) prompt-based manipulation, (2) SAE-derived feature steering, and (3) probe-based direction steering and examine their utility for LLM-based social scientific simulations. We do so by interpreting and steering two foundational components of human behaviors, namely preferences (risk attitudes, altruism) and capabilities (divergent creativity, product innovation), operationalized using four classic economic and creative tasks implemented as natural-language interactions. Overall, our results show that SAE- and probe-based techniques often outperform basic prompt-based methods for steering LLM agents, although this advantage depends on the specific prompting strategy involved. Together, SAEs and probes constitute an effective pipeline for social scientists seeking to interpret and steer agents in social simulations: SAEs decompose agents' internal representations into human-readable features, after which probes can reliably shift agents' behaviors in specified directions. We discuss implications of these methods for future work using LLM agents for social scientific simulations.

---


### 62. [Early-Bird Decoding: Accelerating Diffusion LLMs with Learnable Block Sizes and Parallel Sampling](https://arxiv.org/abs/2609.16450)

**<font color=#1a73e8>作者：</font>** Lixuan Wei, Wei Zhou, Jianwen Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) offer a promising parallel decoding paradigm as an alternative to autoregressive generation through iterative unmasking. However, dLLMs typically require many steps before token confidence reaches the decoding threshold, resulting in inefficient inference even with block-wise KV caching. To accelerate dLLM inference, we for the first time propose an "early-bird (EB)" decoding framework, motivated by the observation that tokens with similarly low entropy tend to cluster and can be jointly decoded earlier, before reaching the confidence threshold. In particular, our EB-Decode framework integrates two key enablers: (1) a learnable network that adaptively groups tokens with similar uncertainty into variable-length blocks, rather than relying on fixed block sizes; (2) a position-aware sampler that learns to unmask tokens in parallel using fewer decoding steps within predicted variable-length blocks. Both components are developed without modifying pretrained dLLM weights and can therefore be directly deployed as plug-ins during serving, with negligible training and inference overhead. Extensive experiments across three models and four benchmarks consistently validate our observation and the effectiveness of EB-Decode, achieving 3.53-18.76$\times$ higher throughput than the vanilla decoding method and up to 1.58$\times$ higher throughput over the strongest baseline, Fast-dLLM, with comparable accuracy.

---


### 63. [Fine-Tuning Fixes Mode Collapse and Over-Dispersion in LLMs](https://arxiv.org/abs/2609.16454)

**<font color=#1a73e8>作者：</font>** Kirill Skobelev, Eric Fithian, X.Y. Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work by Doshi and Hauser (2024), Bisbee et al. (2024), and Xie et al. (2026) raises concerns that outputs from large language models (LLMs) tend to be under-diverse: they repeat or resemble one another more often than responses from the population they are meant to represent, a phenomenon known as mode collapse. In this work, we show that whether mode-collapse, or its opposite, occurs depends on the specific model and dataset used. Further, with sufficient supervised fine-tuning (SFT) data, LLM output diversity converges toward that of the target distribution from which fine-tuning data are sampled. To quantify this comparison, we measure the probability that two responses sampled independently from the same fixed prompt coincide (collide), or their expected similarity under a kernel. We derive a bias-variance decomposition of the expected gap between the model's and target's collision probabilities, showing that SFT is not inherently biased toward mode collapse or its opposite: finite-sample SFT can leave a model either under- or over-dispersed, depending on the model and dataset. Finally, we show that the absolute gap is bounded by the square root of the Kullback-Leibler (KL) divergence from the target distribution to the model. Consequently, a model sufficiently close to optimal under population cross-entropy cannot exhibit arbitrarily miscalibrated diversity. We test the decomposition and the bound in three experiments: small transformers on synthetic languages, four LLMs fine-tuned on human surveys, and these LLMs fine-tuned on CodeNet, a dataset of human code solutions. More target data moves model diversity toward the human (or synthetic target) level in all experiments, consistent with our theoretical predictions. These results show that diversity miscalibration can arise from finite-sample error and shrink as SFT better approximates the target distribution.

---


### 64. [OPD-Aha: From Linguistic Momentum to Visual Reflection in Multimodal On-Policy Distillation](https://arxiv.org/abs/2609.16459)

**<font color=#1a73e8>作者：</font>** Chenhao Qiu, Dawei Li, Yechao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Privileged on-policy distillation improves multimodal reasoning by allowing a teacher to evaluate student trajectories using rich, training-only visual evidence. Both models score these trajectories while conditioning on the same student-generated prefix. When a student misinterprets an image early in a response, this accumulating erroneous rationale eventually pulls the teacher away from its visual evidence. The teacher and student converge on the same hallucination, causing standard cross-model supervision to collapse precisely where correction is most needed. We find that the teacher's visual corrective preference is not lost under this misleading agreement. Comparing the predictions of the identical teacher given the real image and a visual null reveals that the privileged evidence still pushes the model toward the correct interpretation. We introduce OPD-Aha, which reconstructs the distillation target directly from this isolated visual preference rather than relying on the fragile teacher-student discrepancy. This reconstructed target aggressively suppresses continuations that contradict the image. Trained with this objective, students learn to naturally interrupt their own flawed reasoning with reflection tokens such as wait and actually. After reflection, subsequent generation relies less on the accumulated erroneous text and more on the visual evidence. Correcting these trajectories mid-generation fundamentally alters the reasoning process, yielding broad and consistent improvements across diverse fine-grained perception and complex multimodal reasoning benchmarks. Our code and models are available at this https URL.

---


### 65. [A multimodal large language model for evidence-based autism spectrum disorder screening](https://arxiv.org/abs/2609.16464)

**<font color=#1a73e8>作者：</font>** Jun Chen, Qi Zhao, Yunliang Jiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The clinical management of autism spectrum disorder (ASD) faces a bottleneck in early screening, mainly because trained specialists are scarce and conventional assessment tools are subjective. Here, we introduce ASDchat, a multimodal large language model designed for evidence-based ASD screening, which takes video, audio, and dialogue as input. ASDchat adopts a dual-branch architecture, where the decision branch generates screening probabilities and the evidence branch generates traceable, timestamped behavioral evidence aligned with standardized clinical criteria (ADOS-2). The model was trained and evaluated on a dataset of 1,035 participants from 27 sites in China, which covered typically developing (TD) children, children with ASD, and children with other disorders. For ASD versus TD, ASDchat reached an area under the receiver operating characteristic curve (AUC) of 0.953 $\pm$ 0.021. On 9 held-out sites that were not used for training, the mean AUC was 0.932. Furthermore, unsupervised clustering of the behavioral dimensions split the ASD cases into six subtypes with different phenotypic profiles, and ASDchat suggests an intervention for each subtype. ASDchat provides a feasible path for large-scale, evidence-based early ASD screening in clinical practice.

---


### 66. ["ChatGPT, what am I missing?": Designing AI Workflows around Professional Task Structure to Shape Analytic AI Use](https://arxiv.org/abs/2609.16482)

**<font color=#1a73e8>作者：</font>** Zilin Ma, Suzi Jazmati, Marco Chimenton 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> General-purpose AI lets users choose what support to request, but leaves them to structure the support a professional task requires. We examine how interactive workflows can embed professional task structure without prescribing how users engage with AI. We designed two scaffolded interfaces around the same negotiation scaffold: one presented a completed AI analysis, while the other supported user-directed, incremental development. A four-condition randomized experiment with 800 participants compared these interfaces with no-AI and an AI chat interface. AI-supported conditions improved preparation coverage over unaided work; the scaffolded workflows further improved coverage over chat. Although the scaffolded workflows produced similar coverage, the user-directed workflow elicited a broader repertoire of analytic requests and lower subjective effort. Professional scaffolding therefore depends not only on displayed structure but on how workflows organize users' engagement with it. Effective professional AI must structure how users and AI build analysis together.

---


### 67. [VPRef: A Cross-Domain Benchmark for Referring Remote Sensing Image Segmentation](https://arxiv.org/abs/2609.16486)

**<font color=#1a73e8>作者：</font>** Quanwei Liu, Tao Huang, Jiaqi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid advancements in vision-language models have propelled Referring Remote Sensing Image Segmentation (RRSIS) to the forefront of Earth observation. However, practical deployments suffer severe performance degradation under a coupled dual-drift paradigm: visual domain drift from cross-spatial-resolution mismatches and spectral variations, alongside textual logic drift from unconstrained, variable user-input granularities. To mitigate these bottlenecks, this paper establishes the first cross-domain RRSIS benchmark, designated as the Vaihingen-Potsdam Referring (VPRef) dataset, comprising 46,972 language-image-annotation triplets organized into a three-tier linguistic hierarchy. Building upon this benchmark, we develop a tailored parameter-efficient domain adaptation baseline anchored on the Segment Anything Model (SAM3) via Low-Rank Adaptation (LoRA). Our framework counteracts visual distribution discrepancies through pseudo-label-driven self-training and addresses textual logic drift via random multi-granularity text prompt mixing. Crucially, the distribution of empirical metrics across ablative variants suggests a potential decoupling between cross-modal semantic robustification and visual domain alignment, demonstrating that linguistic variance drives fine-grained semantic invariance while pseudo-label propagation governs macro-scale spatial grid alignment. Extensive benchmarks demonstrate the proposed framework achieves superior cross-domain segmentation boundaries while modifying merely 1.08\% of the foundational parameter footprint, establishing a robust baseline for future multi-modal remote sensing domain adaptation research. The dataset and code will be available at this https URL.

---


### 68. [Skill-based Agentic Evaluation for Real-time Data Science Tasks](https://arxiv.org/abs/2609.16487)

**<font color=#1a73e8>作者：</font>** Aniruddha Tamhane, Raghavendra Addanki, Ayushi Aggarwal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a framework for evaluating data-science agents on live, continuously updated data using executable ground truth and format-agnostic factoid scoring. Consider this example query: "what were last week's audience sizes"---the reference answer changes as the underlying data changes, so static references become outdated and standard LLM-as-a-judge pipelines cannot verify responses against a fixed ground truth. Our central contribution, ground-truth-as-code, encodes each expected answer as an executable reference function that recomputes the answer directly from live data at evaluation time, ensuring the reference remains consistent with the system it describes. We combine this with a factoid-level, format-agnostic judge that decomposes both the agent's response and the computed ground truth into atomic claims and scores precision, recall, and accuracy over them, irrespective of the response format (prose, list, table, HTML, etc.). The approach is applicable to agents whose expected outputs can be expressed as executable data computations. We validate the framework through a human--LLM agreement study on an internally developed machine learning skill deployed in production, using a synthetic database constructed to reproduce production schemas and entity relationships. Relative to a natural-language ground-truth baseline, our method achieves a 29% improvement in the Matthews Correlation Coefficient (MCC)---a class-balanced measure of agreement between expert annotators and LLM-as-a-judge predictions---and a 16% reduction in token consumption per test case, while a self-directed baseline lacking explicit ground truth is anti-correlated with human judgment. Agents that perform multi-source data integration and computation over non-stationary data are routinely deployed in industry; we propose ground-truth-as-code as a practical methodology for their evaluation.

---


### 69. [Beyond the Name: Demographic Leakage in De-Identified Résumés and Evaluation Artifacts in LLM Bias Audits](https://arxiv.org/abs/2609.16501)

**<font color=#1a73e8>作者：</font>** Qiangju Chen, Yang Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> De-identified résumé screening assumes that redacting explicit fields prevents ethnocultural inference; however, recent audits attribute residual leakage to declared languages. We investigate whether eliminating language fields resolves this leakage across nine open-weight models and 620 counterfactual résumés. By holding language attributes strictly identical, we isolate unstructured prose across five ethnocultural conditions and three cue-salience tiers. Target-group recovery averages 0.757 overall and saturates at 1.000 under high salience, demonstrating that non-language prose sustains demographic inference. Crucially, models diverge only under faint cues (0.086-0.690), establishing salience as an essential evaluation axis. Furthermore, pairwise LLM-as-a-judge outcomes are highly sensitive to evaluation design: forbidding ties yields an apparent selection-rate ratio of 0.39 alongside strong position and content effects, whereas permitting ties produces near-universal ties for most models ($\ge94\%$). Downstream scoring shows only very small between-condition differences, highlighting the need to distinguish demographic signals recoverable from résumé content from effects introduced by the evaluation protocol.

---


### 70. [Competence-Preserving Resume Perturbations Expose Presentation Sensitivity in LLM Screening](https://arxiv.org/abs/2609.16517)

**<font color=#1a73e8>作者：</font>** Qiangju Chen, Yang Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Resume screeners must infer job-relevant competence from resumes whose presentation can vary substantially in wording, structure, stylistic polish, and document extraction quality. Ideally, such surface variation should not change decisions when the underlying qualification evidence is unchanged. We introduce a controlled audit of this property, constructing occupation-grounded candidate profiles at controlled competence levels and rendering each profile into multiple resume presentations. A deterministic validation gate excludes variants that alter the underlying evidence before scoring. Across six open instruction-tuned LLM conditions, we find a clear disconnect between screening validity and presentation stability. Llama-3.1-8B with its native chat template achieves the strongest validity ($0.781$) yet reverses $29.6\%$ of matched pairwise decisions under competence-preserving presentation changes; Mistral-7B-v0.3 reaches validity $0.644$ with a $41.4\%$ flip rate. Native chat formatting improves validity for several chat-tuned models but does not remove this instability. These results show that resume-screening evaluations should assess not only whether a system identifies stronger candidates, but also whether those decisions remain stable when the same competence evidence is presented differently.

---


### 71. [AquiLLM: Evaluating Faithfulness in Open-Weight RAG-LLM Systems for Scientific Research](https://arxiv.org/abs/2609.16519)

**<font color=#1a73e8>作者：</font>** Bernie Boscoe, Srinath Saikrishnan, Vikram Seenivasan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific research increasingly relies on large, heterogeneous data sources, motivating interest in retrieval-augmented generation (RAG) systems that provide natural language access to scientific knowledge and research workflows. Researchers are exploring the viability of these systems as natural language interfaces for document search and for generating analysis code and pipeline components. At the same time, concerns about data privacy and control over research infrastructure have motivated interest in open-weight models and open-source deployments hosted within research institutions.
In astronomy, this development follows a long history of computational infrastructure development, from archival databases and SQL-based systems to LLM-assisted research tools. This paper presents a domain-expert evaluation of faithfulness for AquiLLM, an open-weight, offline RAG-LLM platform designed to support scientific research groups in the use and preservation of tacit and formal knowledge.
We define faithfulness as the extent to which generated responses remain grounded in retrieved scientific context without unsupported claims or omissions. We report results from an astronomy case study evaluating AquiLLM across retrieval and scientific analysis tasks. AquiLLM performs most reliably on explicit retrieval-oriented questions grounded in the RAG collection, while faithfulness degrades for queries requiring synthesis or ambiguity resolution. These results highlight both the promise and limitations of open-weight RAG-LLM systems for scientific research and demonstrate the importance of domain-expert evaluation beyond standard benchmark leaderboards.

---


### 72. [Style-Debiased DPO: Updating LLM Knowledge with Factuality-Aware Synthetic Preference Data](https://arxiv.org/abs/2609.16532)

**<font color=#1a73e8>作者：</font>** Takayuki Yamamoto, Daisuke Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continued pretraining (CPT) with data augmentation such as paraphrasing can store inside a large language model (LLM) the knowledge of a small source corpus. The stored knowledge, however, is not always retrieved correctly. We study the eliciting side rather than the storing side: we use preference optimization, which learns from pairs of a preferred (chosen) and a dispreferred (rejected) response, so that the model elicits its stored knowledge more accurately. One proposed approach takes the model's own erroneous response as rejected and the gold answer as chosen, so as to suppress the error. When the target knowledge is partially known, however, most of these rejected responses are factually correct. Using direct preference optimization (DPO) then pushes down rejected responses that contain correct knowledge and differ from the chosen answer only in style, such as length and wording. We propose style-debiased DPO (SD-DPO), which scores whether the rejected response of each pair is factually correct, inverts the preference of such pairs, and weights them so that the learning signal due to differences in style cancels out as a whole. We first test whether, on top of EntiGraph, a representative storing-side method that runs CPT on text synthesized from the corpus, our method adds accuracy efficiently. On QuALITY, the reading-comprehension QA benchmark on which EntiGraph was evaluated, SD-DPO exceeds a baseline we CPT on EntiGraph's synthetic data from the same base model and evaluate with the same procedure. The training tokens this requires are a few dozen times fewer than the additional CPT needed for the same gain. For knowledge updating, the main goal of this work, we use AToKE, a knowledge-editing benchmark for facts that change over time. There, SD-DPO reaches an overall accuracy of 0.982 and answers with the new or the old fact according to the queried period.

---


### 73. [On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models](https://arxiv.org/abs/2609.16540)

**<font color=#1a73e8>作者：</font>** William L. Tong, Aryo Lotfi, Emmanuel Abbe 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) have emerged as a compelling alternative to Transformers, enabling sequence modeling with constant memory and linear compute. Although SSMs exhibit reasonable performance and favorable computational characteristics, they continue to lag behind Transformers on tasks that require in-context learning and precise retrieval, slowing their adoption for large-scale language modeling. In this work, we demonstrate that both the success and failure of SSMs in these domains can be explained by studying the role of the gating mechanism, a prevalent component in modern recurrent networks. Specifically, we show through theory and experiments that this gating mechanism causes SSMs to first learn an in-weights "memorization" solution, while delaying, or even preventing, convergence to a correct in-context learning solution. Importantly, this happens even in cases where there are no fundamental limitations due to the architecture or its memory capacity. On the other hand, we find that gating is often beneficial for improving generalization to long sequence lengths. Our results illuminate the crucial role of the gating mechanism in shaping both the training dynamics and generalization of SSMs, and provide a basis for understanding and improving linear-time models.

---


### 74. [PunGraph: Retrieval-Enhanced Phonetic-Semantic Graph Reasoning for Pun Understanding](https://arxiv.org/abs/2609.16557)

**<font color=#1a73e8>作者：</font>** Yuchen Su, Zijian Huang, Yaotian Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Puns are a challenging form of figurative language that exploit phonetic similarity and semantic ambiguity to convey multiple meanings. Although large language models (LLMs) demonstrate strong language understanding capabilities, they still struggle with pun reasoning due to limited phonetic modeling and uncontrolled end-to-end generation. We propose \textbf{PunGraph}, a retrieval-enhanced knowledge graph framework for pun understanding. PunGraph constructs a phonetic-semantic lexical graph using the Unisyn phonetic dictionary, IPA and G2P representations, and WordNet definitions, and retrieves candidate words or senses to constrain LLM reasoning within a structured candidate space. We further introduce \textbf{WebPun}, a new large-scale dataset containing 5,730 annotated heterographic and homographic puns. Experiments on SemEval-2017 and WebPun show that PunGraph consistently improves the performance of small-scale LLMs and achieves competitive results against strong proprietary models. Further analysis shows that retrieval-guided phonetic and semantic constraints effectively reduce common reasoning errors in pun interpretation, highlighting the benefits of integrating structured knowledge with LLMs. We release our code and dataset at this https URL.

---


### 75. [Query-Aware Source-Risk Triage for Retrieval-Augmented Generation](https://arxiv.org/abs/2609.16564)

**<font color=#1a73e8>作者：</font>** Kainan Zhou, Gangzhen Qian, Chuhong Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) pipelines may omit a source's material relationship to the query. We study a pre-generation triage layer that treats this relationship as query dependent. The method routes canonical query families for enhanced review and assigns retrieved pages to pass, contextualize, exclude, or review. It combines a four-dimension page score, rank-discounted family aggregation, intent-preserving query mutations, and a family-held-out router. A single-coded pilot of 200 real URLs supplies provisional calibration anchors; a 20,000-row scenario with synthetic domain identifiers supports controlled workload analysis. An oracle page gate defines a risk-coverage target for a future learned classifier. The evaluation shows why page-level frequency cannot substitute for family-level exposure and quantifies how calibration changes scenario activation. Annotation reliability remains unmeasured, and synthetic rankings omit real retrieval dynamics. The result is an auditable triage method and validation plan, not an estimate of deployed review workload, live-Web prevalence, or downstream answer-quality gains.

---


### 76. [Do LLMs Have Values? A Quantitative Analysis and Alignment Framework for Values in Large Language Models](https://arxiv.org/abs/2609.16589)

**<font color=#1a73e8>作者：</font>** Keqing Zhang, Jingyu Chen, Yufan Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) increasingly handle complex subjective tasks, aligning their intentions and behaviors with human values has become a critical scientific challenge. However, current efforts are confounded by a striking behavioral paradox: they fluctuate unpredictably under minor wording changes ("swing"), yet stubbornly ignore explicit instructions to correct ingrained biases ("rigidity"). Resolving this duality is critical for reliable AI alignment. To systematically understand and safely steer these latent subjective preferences, our study is structured around three fundamental questions. First, do LLMs possess an intrinsic value system? By projecting responses from 106 LLMs (150,000 queries per model) and 95,000 human survey profiles into a shared sociological space, we empirically confirm that they do. However, they do not mirror human diversity, instead crystallizing into a highly concentrated, idealized value core. Second, how can these values be quantified? We propose the Prior-Environment-Cognition (PEC) framework. This model mathematically defines value expression as the joint outcome of inherent dispositions like parameter weights (Prior), external contexts such as user prompts (Environment), and internal reasoning processes like Chain-of-Thought (Cognition). Finally, how can LLMs' values be aligned toward a desired target? Using PEC diagnostics, we establish an adaptive "Alignment Prescription". Rather than blindly applying resource-intensive training, this method identifies the minimum effective intervention needed for each dimension, ranging from zero-cost prompts to targeted parameter updates. Extensive empirical validation confirms that our approach successfully verifies the presence of LLM values, accurately quantifies their shifts, and achieves more efficient and precise steering than conventional blind training, all without degrading general capabilities.

---


### 77. [Challenges of Auditing: Variability in Outputs of Large Language Models for Health](https://arxiv.org/abs/2609.16590)

**<font color=#1a73e8>作者：</font>** Yuan Pu, Yewon Chang, Furong Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> People increasingly use frontier AI models for health advice, but via different access modes (e.g., ChatGPT, ChatGPT Health, APIs) with varying settings. Here, we find systematic differences across access modes. Because evaluations typically rely on APIs while consumers interact through chatbot interfaces, these discrepancies limit evaluation validity. Our findings underscore an urgent need for model providers to enable faithful replication of consumer experiences and settings for rigorous audits.

---


### 78. [A Framework for Generating Valid Context-Specific Benchmarks through Expert Guidance](https://arxiv.org/abs/2609.16592)

**<font color=#1a73e8>作者：</font>** Kimberly Le Truong, Nari Johnson, Anna Kawakami 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents an end-to-end approach for generating context-specific large language model (LLM) benchmark datasets by combining expert input with synthetic data generation. Existing benchmark construction methods often trade off validity and scalability: datasets designed with domain experts can produce high-quality evaluations but are slow and costly to create, while synthetically generating data may scale efficiently but often results in unrealistic, redundant, or out-of-scope examples. To address this gap, we introduce a schema eliciting key information about the goals, scope, and context of an evaluation task, and use this information to guide synthetic data generation. We further define four criteria grounded in measurement validity for assessing dataset quality: coverage, diversity, content realism, and stylistic realism. Using these criteria, we show how expert-informed scaffolds can guide synthetic data generation toward more valid benchmarks. Through quantitative evaluations and a real-world case study with domain experts, we demonstrate that our approach improves benchmark data quality over existing methods while preserving validity. We additionally analyze how different types of schema information affect different dataset quality criteria, and provide practical guidance on which information to prioritize collecting under resource constraints.

---


### 79. [SAVOR: Self-Aware Visual Grounding via Confidence-Calibrated Reinforcement Learning for Multimodal Hallucination Mitigation](https://arxiv.org/abs/2609.16601)

**<font color=#1a73e8>作者：</font>** Zixiu Ding, Zilin Zhao, Yingjie He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have made strong progress on visual question answering and image captioning, yet they still produce fluent claims about objects, attributes, or relations that are not grounded in the image. Many remedies either modify decoding at test time, which adds latency, or fine tune with preferences such as DPO variants, which teach which answer is preferred but not when the model's own answer is unreliable. We argue that calibrated self assessment is the missing signal. We introduce Savor, a training framework that (i) augments the output schema with token and answer confidence, (ii) optimises the policy with a Group Relative Policy Optimisation (GRPO) objective that penalises calibration error and poor abstention decisions, and (iii) uses the learned confidence at inference time to revisit visual evidence only when the model is uncertain. Experiments on POPE, HallusionBench, AMBER and MMHal-Bench across two recent backbones (InternVL3-8B and Qwen3-VL-8B) show that Savor reduces hallucination while preserving general capability on MME and MMBench, with lower Expected Calibration Error than DPO and decoding baselines.

---


### 80. [EgoPathBench: Evaluating Zero-Shot Egocentric Waypoint Decision-Making in Vision-Language Models](https://arxiv.org/abs/2609.16610)

**<font color=#1a73e8>作者：</font>** Yang Zhao, Zhuo Chen, Xubo Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot waypoint navigation requires vision-language models to select, from the current first-person observation, a sequence of spatial actions that is feasible for the agent and reaches the goal, placing joint demands on the integrated spatial intelligence of today's foundation VLMs. Existing spatial-intelligence benchmarks primarily evaluate isolated judgments of relations, directions, or targets and therefore do not directly measure the integrated navigation ability required to combine target recognition, action-consequence assessment, distance estimation, and path planning. To fill this evaluation gap, we introduce EgoPathBench, a dataset and five-task benchmark for first-person waypoint decision-making. Each question presents an egocentric RGB image, a natural-language goal, and numbered visible waypoints; a model returns traversable candidates or an ordered route. Predictions are evaluated for candidate feasibility, adjacent-edge legality, and goal arrival under point-agent or embodied geometry. EgoPathBench contains 31,852 training, 1,345 validation, and 1,111 benchmark questions and retains at least one geometrically verified reference route for every route question. Across nine VLMs, the highest EgoPath Score is only 28.3. The top-ranked model reaches 35.9% success on Point Path, but only 2.9% and 4.0% on Embodied Path and Intent Path, respectively, showing that current models remain limited in forming complete, goal-consistent routes under embodiment constraints. Beyond the evaluation data, we release the corresponding training resource. Fine-tuning Qwen 3.5 4B on the released training split raises its EgoPath Score from 3.9 to 38.9 and improves all four reported evaluations across three external spatial benchmarks, with gains of 1.4--9.6 points.

---


### 81. [RoleBreak: Benchmarking Long-Horizon Role-Playing Robustness in Spoken Dialogue](https://arxiv.org/abs/2609.16614)

**<font color=#1a73e8>作者：</font>** Yuqi Wang, Fengyuan Liu, Haochen Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-speech dialogue models increasingly support persona control, yet existing spoken role-playing benchmarks remain largely character-centric and short-horizon. This leaves open whether spoken dialogue models can sustain diverse roles over extended interactions, especially beyond predefined fictional characters. We introduce RoleBreak, an open benchmark for long-horizon role-playing robustness in spoken dialogue. RoleBreak contains 310 character-based and user-centered roles, 6,688 human-verified dialogue turns, and 11,743 fine-grained evaluation criteria, with 1,856 turns carrying expressive emotion targets for evaluating vocal emotion. Its scenarios are designed to stress role consistency, interaction quality, safety, and affect over extended conversations. We evaluate nine configurations spanning full-duplex, omni-modal, and cascaded ASR--LLM--TTS paradigms. We find four key patterns. First, current systems are substantially stronger at semantic role adherence than at vocal emotion. Second, semantic robustness remains brittle over long interactions: even the strongest evaluated system encounters its first persona and safety failures after only 10.4 and 11.6 turns on average. Third, scaling the LLM substantially improves semantic robustness and delays failure, but yields little improvement in vocal emotion. Finally, user vocal emotion affects role-playing behavior even when linguistic content is fixed. These findings highlight persistent gaps in both long-horizon robustness and vocal expressiveness in spoken role-playing systems.

---


### 82. [Divergence Timing and Cumulative Disagreement under KV-Cache Eviction](https://arxiv.org/abs/2609.16617)

**<font color=#1a73e8>作者：</font>** Xinyue Luo, Fei Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV-cache eviction perturbs the conditional token distributions governing autoregressive generation. We investigate how first-divergence timing and subsequent token mismatch determine cumulative disagreement. We derive an exact decomposition under a specified stepwise maximal coupling: the expected mismatch fraction equals a first-mismatch contribution plus post-divergence exposure multiplied by its mismatch rate. An explicit construction over unrestricted autoregressive kernel pairs realizes the sharp interval of risks compatible with a finite divergence-aligned observation window. Residual-branch conditional Monte Carlo provides unbiased joint estimates of occurrence, occupation, and window/tail contributions, with per-replicate variance dominance for total token loss. Complete trajectories from Meta-Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct show that SnapKV at 50% retention enters divergence later and less often than SnapKV-512 or recent-token retention with the same 50% prompt-cache budget, while post-divergence total variation (TV) remains high. In an exploratory analysis of 288 documents, post-divergence exposure accounts for 85-90% of four aggregate mismatch gaps. On 288 independent documents at 90% retention, prespecified comparisons show higher branch-aligned TV in the late than in the early window in both models.

---


### 83. [Quantifying Organizational Environmental Action from Web Data and Large Language Models](https://arxiv.org/abs/2609.16627)

**<font color=#1a73e8>作者：</font>** Quinn Reynolds, Daniel Shore, Vianey Leos Barajas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantifying organizational environmental action from publicly available web content remains a challenging environmental data science problem because relevant information can be dispersed across multiple webpages and is primarily communicated through unstructured text. We present a scalable computational framework for transforming organizational web content into structured measures of environmental action and demonstrate the approach using Jewish congregations in the United States. We constructed a national database of 4,964 congregations by integrating multiple geospatial, knowledge-base, directory, and manually reviewed sources. Of these, 2,657 had active websites that were successfully crawled, producing a corpus of 154,454 webpages. We compared three approaches for detecting environmental actions: keyword retrieval followed by large language model (LLM) classification, semantic vector retrieval followed by LLM classification, and direct LLM classification classification without preliminary retrieval. Agreement with an expert human reviewer was lowest for keyword retrieval ($\kappa$ = 0.26), higher for semantic vector retrieval ($\kappa$ = 0.42), and similar for direct LLM classification ($\kappa$ = 0.40). Although semantic retrieval achieved the highest agreement, its retrieval recall was 0.87, indicating loss of relevant content before classification. Applied to the complete corpus, direct LLM classification identified at least one environmental action at 1,398 congregations (53%), providing greater coverage than either retrieval-based approach. These results demonstrate that preliminary retrieval can reduce computational cost but may exclude relevant information before it reaches the classifier. The framework provides a reproducible approach for extracting organization-level environmental information from unstructured web content that can be adapted to other institutions.

---


### 84. [EchoPath: Execution-Level Replayable Memory for GUI Agents](https://arxiv.org/abs/2609.16635)

**<font color=#1a73e8>作者：</font>** Yao Zhao, Aditya Shanmugham, Swastik Roy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents increasingly operate browsers, software, and desktop applications via CLI or API portals, but graphical user interface (GUI) still plays an important role in common industrial production scenarios. GUI agents commonly employ fresh observe-plan-ground-act loops, which is inefficient for enterprise tasks that repeatedly update records, process forms, configure tools, and export reports. We introduce EchoPath, a model-agnostic harness that converts artifact-validated GUI trajectories into standardized, parameter-controlled callable memories, analogous to Model Context Protocol (MCP)-style tool calls rather than unstructured experience records. Each memory stores task-intent keys, application and state preconditions, flexible input parameters, GUI evidence, validation provenance, and lifecycle state, so the host agent invokes a targeted procedure only when it can be deterministically replayed in the current runtime. The core mechanism enabling replay is an image-based target-reaiming algorithm that treats stored coordinates as visual evidence, matches the remembered GUI target against the current screen, and emits corrected operation coordinates before execution. During replay, EchoPath rebinds only declared modifiable inputs and rejects ambiguous or incompatible steps to bounded grounding repair or fresh planning. In experiments with real computer-use tasks, EchoPath reduced median token cost by more than 90% and median execution time by about 60%. These results support a bounded form of enterprise GUI memory: validated execution experience can become a controllable callable asset for recurrent work rather than only context for another reasoning pass.

---


### 85. [ReDraft, Don't Just Distill: Reference-Driven Revision for Continual VLLM Post-Training](https://arxiv.org/abs/2609.16639)

**<font color=#1a73e8>作者：</font>** Zhihao Zhang, Mingqi Wu, Qiaole Dong 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual post-training of large multimodal models should add new capabilities while preserving those from pre-training, and the two goals pull in opposite directions. SFT gives explicit target supervision that learns a task from near-zero accuracy, but its off-policy targets move the model far enough to cause forgetting; on-policy methods such as RLVR and self-distillation preserve policy proximity yet supply little signal when the policy cannot yet solve the task. We introduce ReDraft (Reference-Driven Revision and Fine-Tuning), which obtains both from the model's own failures: using an expert response only as a reference, it has the model revise its own incorrect rollout, keeps the revision only if a verifier accepts it, and fine-tunes on what survives. Each retained target is therefore explicit, yet still close to the current policy. Across Counting, Clock Reading, and Jigsaw on Qwen2.5-VL-3B/7B, two of them with near zero accuracy, ReDraft gains 56.9 points on the target task against SFT's 52.9 while cutting prior-task loss from 16.6 to 1.5 points (11.3x less forgetting), and improves on OPSD along both axes (19.3 gain, 6.2 loss). Data- and parameter-space analyses match the design: revised targets are more probable under the base model, and the updates they induce stay compact and follow SFT's direction more closely than OPSD's. Repairing the model's own output, rather than replacing it with an expert's, is what lets one objective do both.

---


### 86. [What Do Hallucinations Reveal About Multimodal Reasoning? Diagnosing Visual Grounding Failures via Contrastive Decoding Probes](https://arxiv.org/abs/2609.16646)

**<font color=#1a73e8>作者：</font>** Zhipeng Zhao, Wenxu Wang, Peishun Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When strong multimodal models are widely available, progress requires new scientific methodologies beyond benchmark scores---using models as instruments for understanding behavior. We address this by asking: can we use large vision-language models (LVLMs) as experimental instruments for studying their own failure dynamics? Focusing on visual hallucination, we introduce SAFE, a training-free decoding framework that contrasts visually-grounded and vision-ablated generation paths to produce a token-level contrastive grounding score that identifies when the model favors linguistic priors over visual evidence. This signal serves dual roles: as a practical proxy for detecting visually-ungrounded tokens, and as the basis for decoding-time penalties. Our analysis yields three empirical observations: visual dependency decays over generation, hallucinations co-occur in temporal clusters, and early intervention reduces clustering without substantially degrading fluency. On MMHalBench, SAFE substantially outperforms all compared baselines; results elsewhere are more mixed. We argue that designing contrastive probes exemplifies a broader mission: using models as instruments for scientific understanding. Code: this https URL.

---


### 87. [ViD: Vision-Dominant Gender Bias Mitigation for Large Vision-Language Models](https://arxiv.org/abs/2609.16647)

**<font color=#1a73e8>作者：</font>** Zhipeng Zhao, Zhaoqiang Wei, Peishun Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gender bias in large vision-language models (LVLMs) undermines their fairness and reliability, compromising output trustworthiness. Current mitigation methods rely on training-phase adjustments or post-hoc calibration, but face limitations in dynamic visual bias mitigation. These include inability to capture real-time visual-textual incongruence, dependence on predefined gender bias taxonomies, and degraded cross-modal alignment with emergent bias patterns. To address these challenges, we propose ViD, a causally-inspired framework that analyzes attention mechanisms across five distinct patterns, revealing confounding effects from strong language priors. ViD demonstrates that visual-to-language cross-attention effectively suppresses bias while preserving general reasoning capabilities and text generation quality. ViD incorporates dual mechanisms: backdoor adjustment counters strong language priors, while refined token selection in decoding layers optimizes processing. This enhances model robustness and inference efficiency. Our integrated approach significantly mitigates gender bias across multidimensional social attributes in LVLMs, improving visual grounding and output fairness. Cross-benchmark validation shows ViD reduces gender bias by 14.7\% on single-attribute evaluations (FACET) and achieves significant improvements on image captioning tasks (MS COCO), with gender bias score improving from 0.6708 to 0.9978 for LLaVA. Crucially, these improvements require no additional training overhead, making ViD a scalable and practical solution for bias mitigation in LVLMs.

---


### 88. [GrowMTP: Can RL Grow Its Own Draft Head?](https://arxiv.org/abs/2609.16648)

**<font color=#1a73e8>作者：</font>** Minghua He, Lingzhe Zhang, Yuan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training drives the frontier capabilities of large language models, with its wall-clock dominated by autoregressive rollout generation. Speculative decoding is an established remedy for this bottleneck, but existing draft heads must be pretrained or warmed up before RL, introducing substantial training cost outside the RL run to be accelerated. We observe that RL training itself provides both conditions required for online draft-head training: its rollout distribution is far narrower than that of pretraining, and its verification step continuously produces supervision signals aligned with this distribution. Building on these observations, we propose GrowMTP, which uses this supervision to train a draft head from scratch entirely within the RL loop, with all head updates detached from the policy backbone. On Qwen3-4B (no draft head), MiMo-7B-SFT (weak head), and Qwen3.5-4B-Base (strong head), GrowMTP achieves rollout speedups of 2.13x, 1.93x, and 1.36x, and end-to-end speedups of 1.60x, 1.41x, and 1.20x, respectively. GrowMTP therefore serves existing RL training frameworks as a modular component, particularly offering a from-scratch acceleration path for models without pretrained draft heads.

---


### 89. [Rewarding Reasoning, Not Answers: Fixing and Bounding Test-Time Reinforcement Learning on Medical QA](https://arxiv.org/abs/2609.16660)

**<font color=#1a73e8>作者：</font>** Kailong Fan, Anqi Pu, Yichen Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time reinforcement learning adapts a model on its own unlabeled test set using majority-vote pseudo-labels and has shown strong results in mathematics. We show that this recipe collapses on medical multiple-choice QA: accuracy stagnates while output diversity rapidly declines. Through a controlled experiment that keeps the questions, model, and optimizer fixed while changing only the answer space, we trace this failure to answer-space structure rather than domain difficulty. In small answer spaces, incorrect rollouts often collide on the same wrong pseudo-label and reinforce it; in large answer spaces, they disperse and receive little reward. This diagnosis motivates PROSE, Process Reward Guided Self-Training, which rewards reasoning quality instead of answer agreement. PROSE scores each reasoning step with a medical process reward model, assigns the trajectory reward as the minimum score across steps, and enforces answer-format constraints. Without labels, PROSE substantially improves a general Llama model, surpassing purpose-built medical models and matching much larger systems. Because the process signal is internalized into the policy, the adapted model requires no reward model at inference and transfers its gains to unseen datasets. We further show that the minimum aggregation is essential: mean aggregation can be exploited, saturating the proxy reward while degrading accuracy.

---


### 90. [Bridging the Perceptual Gap: Residual-Enhanced Downscaling and Manifold-Aware Perception Alignment Adaptation for NR-IQA](https://arxiv.org/abs/2609.16664)

**<font color=#1a73e8>作者：</font>** Yu Li, Zhengran Shen, Yachun Mi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leveraging Large Vision-Language Models like CLIP has recently set new benchmarks for No-Reference Image Quality Assessment (NR-IQA). However, the contrastive pretraining of CLIP inherently prioritizes semantic invariance, which often suppresses subtle perceptual signals, a phenomenon we term perceptual submergence. Furthermore, standard preprocessing techniques (e.g., cropping and interpolation) further exacerbate the loss of critical high-frequency quality cues. In this paper, we propose the Cross-modal Perception Alignment Adapter (CMPA), a manifold-aware framework designed to disentangle perceptual distortions from dominant semantics. CMPA introduces a Perception-Sensitive Feature Extractor (PFE) that projects CLIP features into a compact, low-dimensional subspace, explicitly magnifying distortion-induced off-manifold deviations. Subsequently, a Cross-Modal Perception Alignment Injector (PAI) aligns these features with quality-aware text anchors and re-injects them into the backbone. To ensure input fidelity, we also devise a Residual-enhanced Perceptual Downscaling strategy that adaptively compensates for resolution-induced information loss using Just Noticeable Difference (JND) guided frequency re-injection. Extensive evaluations on several benchmark datasets demonstrate that our approach significantly outperforms state-of-the-art methods, effectively recovering the perceptual signals submerged in semantic-dense representations.

---


### 91. [ANIMASK: What the Model Contributes to Role Play in Simulated Story Worlds](https://arxiv.org/abs/2609.16667)

**<font color=#1a73e8>作者：</font>** Xiucheng Zhang, Zhuoning Xu, Hanjun Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a language model plays a character, the observed behavior reflects both the assigned persona and the default dispositions of the actor model itself. Existing evaluations test persona fidelity or model defaults in isolation, but neither says, at a specific choice with consequences, what the persona changed and what the model's default kept. We introduce ANIMASK, a simulation framework that freezes books and scripts into story worlds whose characters act on their own motivations and replays each story from its freeze point. We hold out the author's continuation as a human reference, verify through in-story interviews that each persona remains present, and at every decision point compare the character's action with what the model produces when the persona is removed. Across 40 stories, 6 actor models, and 3,846 decision points, the replays converge away from their canons in one shared direction, toward flatter, cooler stories that leave their tensions open. The personas stay present and obeyed throughout. On three choices in four the model's default already falls inside what the persona accepts, and where the two diverge the model is the cautious one, holding where the persona would press. The persona guarantees who the character is, and the model sets how far the character will go.

---


### 92. [little m: An AI Agent for Industrial Process Optimization](https://arxiv.org/abs/2609.16680)

**<font color=#1a73e8>作者：</font>** Yongchao Ye, Xinyu He, Dutliff Boshoff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Manufacturing consumes one third of global energy and still has significant room for improvement in terms of energy efficiency. Optimal process control is essential for this purpose. However, synthesizing mathematical optimization models from messy, real-world industrial specifications requires bridging unstructured natural language and spatial diagrams with rigorous mathematical syntax. This poses a profound challenge for general-purpose Large Language Models (LLMs), which may introduce invalid constraints when tasked with modeling continuous multi-physics dynamics. To address this, we introduce little m, an AI agent designed to assist the formulation of industrial process control models. Combining a domain-specific knowledge repository with LLM-driven interaction, the proposed framework formulates real-world optimization problems as mathematical models. For systematic evaluation, we introduce the Industrial Process Control Benchmark (IPC-Bench), a novel multimodal dataset of 50 canonical scenarios requiring joint reasoning over text and process diagrams. Through comprehensive automated structural assessments and double-blind human evaluation, little m substantially outperforms state-of-the-art LLMs, generating semantically correct models. These evaluations assess formulation quality rather than solver feasibility, formal physical validity, or closed-loop industrial performance. The implementation of little m and the IPC-Bench dataset are available at this https URL.

---


### 93. [MarkSec: Capability-Aware Evaluation of Adversarial Attacks Against LLM Watermarks](https://arxiv.org/abs/2609.16681)

**<font color=#1a73e8>作者：</font>** Kairong Li, Zhikun Zhang, Xiao Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM watermarking helps trace the origin of generated text, but faces stealing attacks that recover watermark information, scrubbing attacks that remove watermark signals, and spoofing attacks that forge text accepted as watermarked. These attacks are often studied in isolation, leaving their connections unclear. Evaluations also often lack shared detector calibration, metric definitions, and reporting protocols. Moreover, measuring attack success and text quality separately makes it difficult to identify attacks that are both effective and quality-preserving.
We propose MarkSec, a general framework that unifies analyses of stealing, scrubbing, and spoofing. We evaluate attacks under a common reporting protocol and introduce a quality-constrained attack success metric to assess effectiveness and text quality jointly. Experiments across representative watermark families, attacks, LLMs, and datasets reveal three findings. First, attacks that appear strongest by watermark removal alone can fall behind general rewriting when success also requires acceptable text quality. Second, general rewriting remains a strong baseline across watermark families, while its advantage over other scrubbers varies by family. Third, in a case study of one watermark family, stealing-based scrubbers often underperform the best general-scrubbing baselines when text quality is required. These results show that apparent attack winners depend on text-quality constraints, attack generality, and capability assumptions.

---


### 94. [Efficient Quantization-Aware Distillation with Cross-Modal Alignment for Edge Vision-Language Models](https://arxiv.org/abs/2609.16689)

**<font color=#1a73e8>作者：</font>** Jinwoo Jeon, GyuYeop Do, Yubin Lim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale vision-language models (VLM) such as CLIP enable strong open-vocabulary reasoning, yet deploying these capabilities on resource-constrained edge devices remains challenging. EdgeVL addresses this problem by distilling CLIP representations into lightweight multi-modal encoders and applying quantization-aware training (QAT) for efficient Open-Vocabulary Classification (OVC) on edge hardware. However, its two-stage optimization applies different objectives for distillation and QAT, and contrastive learning is performed within the quantized student space, which can result in inconsistent optimization and reduced training efficiency. Moreover, identical supervision across RGB and non-RGB modalities may lead to modality imbalance. We propose a unified framework for quantized semantic distillation tailored to edge deployment. By jointly optimizing distillation and quantization within a unified teacher-anchored framework, our method ensures consistent training under quantization, suppressing hard negatives and enlarging decision margins. Additionally, we design a lightweight cross-attention adapter that enhances non-RGB representations through RGB-guided semantic transfer, narrowing the modality gap. Extensive experiments demonstrate consistent improvements on non-RGB modalities while maintaining deployment efficiency.

---


### 95. [Toward Secure AI-Powered Penetration Testing Agents: Security Threats, Guardrails, and Architectural Perspectives](https://arxiv.org/abs/2609.16694)

**<font color=#1a73e8>作者：</font>** Rahul Dev T Y, Hiran V Nath  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-powered autonomous agents are transforming the penetration testing space with dynamic, multi-step offensive security workflows that require minimal supervision by humans. These agents leverage sophisticated reasoning abilities and external security tools to independently carry out reconnaissance, identify vulnerabilities, devise exploitation plans, and perform post-exploitation operations. But the ability to have persistent memory, to take actions in the real world, and to do long-horizon reasoning raises qualitatively different security concerns than traditional chat-based LLM systems. Existing guardrail mechanisms for conversational AI may not be sufficient to secure autonomous AI pentesting agents accordingly.
To address these issues, we carry out a comprehensive security analysis on autonomous AI-penetration testing agents. We systematically analyse representative agent architectures, characterise their trust boundaries and attack surfaces and propose a threat taxonomy that is aligned with the lifecycle and covers LLM lifecycle attacks, agent-architecture attacks and cross-cutting behavioural attacks. We analyse the limitations of existing guardrail mechanisms, identify key research gaps, and discuss future research directions for developing specialised, context-aware, and architecture-aware guardrails to secure next-generation AI-driven offensive security systems.

---


### 96. [VideoMM: Adaptive Macro-Micro Inference for Efficient Video MLLMs](https://arxiv.org/abs/2609.16722)

**<font color=#1a73e8>作者：</font>** Haoyu Guo, Yuan Feng, Junlin Lv 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling Multimodal Large Language Models (MLLMs) to long-form video understanding is bottlenecked by the explosion of visual tokens, which saturates context windows and incurs prohibitive costs. Current solutions predominantly rely on auxiliary models for token reduction but face a fundamental dilemma: lightweight encoder-driven approaches often overlook critical semantic information, whereas heavyweight MLLM-driven reduction negates the efficiency gains. {In this work, we identify a more fundamental inefficiency underlying this dilemma: while fine-grained visual details are essential for detailed understanding, they are largely redundant for the preliminary task of selecting semantically relevant regions. } Motivated by this, we introduce \textbf{VideoMM}, which marks a paradigm shift from model-centric downsizing to adaptive perceptual granularity. Specifically, our framework {decouples selection from reasoning} by executing semantic filtering on a cost-effective \textit{Macro Proxy} (derived from downscaled frames), and projecting the selected regions onto high-fidelity \textit{Micro Tokens} for detailed understanding only when necessary. Extensive evaluations show that VideoMM significantly outperforms existing solutions. It achieves a 6.13$\times$ speedup and a 7.4\% accuracy gain over full-context baselines on LongVideoBench, and further accelerates inference by 2.73$\times$ over current leading methods, establishing a highly scalable paradigm for long-video understanding. Our code is available at: this https URL.

---


### 97. [Japanese Stroke LLM Evaluation: A Conversational Benchmark for Safe Stroke Care in Japanese Using Large Language Models](https://arxiv.org/abs/2609.16739)

**<font color=#1a73e8>作者：</font>** Keisuke Masuda, Kazutaka Yatsushiro, Hirohumi Iwamoto 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Large language models (LLMs) have achieved physician-comparable performance on multiple-choice medical knowledge examinations, but their capabilities in clinical history taking, urgency assessment, and safety remain insufficiently evaluated. We proposed Japanese Stroke LLM Evaluation, a multi-turn conversational benchmark for stroke care in Japanese, and evaluated LLM performance and safety under practice-oriented conditions. Methods: We created 10 stroke and related-condition cases and evaluated LLMs in multi-turn Japanese conversations. The LLM acted as physician, while a board-certified neurosurgeon acted as simulated patient and evaluator. Each case comprised history-taking and action phases scored using pre-specified criteria. Errors that could directly threaten life were defined as critical mistakes. The safety threshold was at least 80% overall with zero critical mistakes. Eighteen models were evaluated in October 2025 and June 2026. Results: Claude Fable 5 achieved the highest score (87.4%) with zero critical mistakes, followed by Claude Opus 4.7 (80.3%) and GLM-5.2 (75.6%). Two leaders met the safety threshold. Eleven models made 17 critical mistakes, including failure to confirm laboratory results or blood glucose before t-PA, surgery before airway stabilization, omission of cervical vascular evaluation, and t-PA outside its indication. History-taking question count correlated with history-taking score (r = 0.648, p = 0.007). Conclusions: Japanese Stroke LLM Evaluation provides a benchmark for LLM performance under practice-oriented conditions, including a cap on history-taking questions. Cases and evaluations were created by neurosurgical specialists rather than using an LLM-as-judge approach. Performance improved across cloud-based and on-premise models in 2026, with some exceeding the safety threshold. Further evaluation using real-world cases is required.

---


### 98. [TIAO: Token Importance-Aware Policy Optimization for Text Summarization](https://arxiv.org/abs/2609.16748)

**<font color=#1a73e8>作者：</font>** Qixiu Li, Chenlong Bao, Xiang Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text summarization requires models to condense content while preserving key qualities such as consistency and coherence. Large language models (LLMs) have shown strong performance on this task and can be further improved through reinforcement learning (RL). However, most existing methods apply reward signals directly to undifferentiated token sequences, overlooking the varying importance of individual tokens to word and sentence level quality in summarization. In this paper, we propose Token Importance-Aware Policy Optimization (TIAO), a novel reinforcement learning strategy that explicitly leverages token-importance awareness. Specifically, TIAO identifies core tokens based on token dependency and reweights a trajectory's advantage according to its overall dependencies. Experiments on the real world dataset show that our TIAO achieves highly competitive results, and that a 7B foundation model enhanced by TIAO performs comparably to GPT-4 and GPT-5-nano. Code is available at this https URL

---


### 99. [TAME: Token Attribution and Masking for Emergent misalignment](https://arxiv.org/abs/2609.16754)

**<font color=#1a73e8>作者：</font>** Md Rayhanul Masud, Md Rizwan Parvez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning an aligned language model on narrow, flawed data can induce harmful behavior far outside the training domain, known as emergent misalignment (EM). Prior work has localized EM in model weights, activations, and training documents, but it remains unclear which training tokens carry the relevant fine-tuning signal. We introduce TAME (Token Attribution and Masking for Emergent Misalignment), a three-stage framework: token attribution scores how strongly the fine-tuning update raises each response token's likelihood, using forward passes through a released LoRA adapter; signal characterization finds patterns among high-attribution tokens; and causal validation tests them by attribution-guided loss masking. On released EM organisms and a 6,849-example medical-advice split, attribution is concentrated (the top 5% of tokens hold 32% of the mass) and, in Llama, depleted for medical vocabulary but enriched for a register of unwarranted certainty, even after controlling for token rarity. Masking high-attribution tokens during fresh fine-tuning cuts EM by 23x in Llama and 36x in Qwen, with the perplexity cost concentrated on the targeted register rather than on medical content; an equal random mask leaves EM unchanged. In Llama, the attribution pattern suggests that EM-relevant signal lies more in how confidently flawed content is expressed than in its domain vocabulary; the causal masking effect itself holds across both model families.

---


### 100. [Turn-level Multiscale Density Ratio Estimation for LLM Agents](https://arxiv.org/abs/2609.16760)

**<font color=#1a73e8>作者：</font>** Zishuo Zhao, Kai Chen, Ao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid development of Large language model (LLM), agent systems enhanced by LLMs show huge potential in being able to deal with complex tasks, especially involving multi-step thinking or interaction with tools. For applying LLM techniques with a well-designed agent paradigm, post-training of LLM in multiple agent scenarios is necessary to achieve better performance. Among the variable post-training techniques, alignment methods such as PPO, DPO, DIL, and GRPO become popular because many papers show a significant positive impact on the model's performance by punishing negative samples while keeping acceptable training complexity. However, most alignment methods address simple single-turn tasks, and there remains room for improvement for complex multi-turn tasks. We propose Turn-level Multiscale Density Ratio Estimation (tlm-DRE), which assigns different weights on corresponding turns and proposes asymmetric token-level training based on the positive-negative space gaps across multiple turns of tasks. The results of the experiment on a wide range of agent benchmarks show that the proposed method performs competitively compared to traditional alignment methods. The proposed training method enables LLMs to perform robustly in multi-turn reasoning tasks with both in-domain and out-of-domain conditions.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
