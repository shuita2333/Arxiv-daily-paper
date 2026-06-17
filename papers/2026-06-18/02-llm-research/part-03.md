# 🧠 大模型相关研究 | 2026年06月18日

> 本类共 **133** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-133**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-133**

---

### 101. [STAR: SpatioTemporal Adaptive Reward Allocation for Text-to-Image RL Post-Training](https://arxiv.org/abs/2606.17979)

**<font color=#1a73e8>作者：</font>** Jinjie Shen, Wei Deng, Xian Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing RL post-training methods for text-to-image generation usually convert the final-image reward into a single scalar advantage and apply it with the same strength to the entire generative trajectory. However, text-to-image generation naturally has temporal and spatial structure: different denoising steps are responsible for different generation stages, and the content that truly determines text alignment often appears only in part of the image. This granularity mismatch makes it difficult for policy updates to focus on the generative components that actually affect the reward. To address this issue, we propose \textbf{SpatioTemporal Adaptive Reward (STAR) Allocation} for RL post-training of text-to-image diffusion and flow models. STAR uses text-image attention inside the generative model and starts from the core content that the user truly cares about in the prompt. It constructs spatial allocation maps that dynamically vary across denoising steps and rollouts, and allocates the same group-relative advantage to more relevant latent regions with almost no additional computational overhead. STAR then applies stronger policy updates to these regions through a spatially resolved policy objective. We use Stable Diffusion 3.5 Medium as the base model and evaluate on three tasks: GenEval, OCR text rendering, and PickScore. Experimental results show that STAR improves compositional semantic alignment, text rendering, and preference optimization without changing the external reward source, achieving $\mathbf{0.9759}$, $\mathbf{0.9757}$, and $\mathbf{23.60}$ on GenEval, OCR, and PickScore, respectively.

---


### 102. [VoidPadding: Let [VOID] Handle Padding in Masked Diffusion Language Models so that [EOS] Can Focus on Semantic Termination](https://arxiv.org/abs/2606.17999)

**<font color=#1a73e8>作者：</font>** Chunyu Liu, Zhengyang Fan, Kaisen Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> MDLMs generate text by denoising a preallocated masked response canvas, making response-length modeling central to instruction tuning. Existing MDLMs often inherit the autoregressive convention of using repeated \texttt{[EOS]} tokens for padding during instruction tuning, giving \texttt{[EOS]} a dual role as both a semantic terminator and a padding token. We show that this dual role is a root cause of \texttt{[EOS]} overflow under large-block decoding. To decouple these roles, we propose VoidPadding, which introduces \texttt{[VOID]} for padding and reserves \texttt{[EOS]} for termination. During inference, the learned \texttt{[EOS]} signal enables early stopping, while the learned \texttt{[VOID]} signal guides adaptive response canvas expansion. On Dream-7B-Instruct, VoidPadding improves the block-size-averaged four-task mean across mathematical reasoning and code generation benchmarks by \(+17.84\) points over the original model and \(+6.95\) points over RainbowPadding, while reducing decoding NFE by 55.7\% on average. Code is available at this https URL.

---


### 103. [Half a Link can Be Enough to Predict a Whole Link: Understanding Generalization in Knowledge Graph Foundation Models](https://arxiv.org/abs/2606.18001)

**<font color=#1a73e8>作者：</font>** Cosimo Gregucci, Obaidah Theeb, Daniel Hernandez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph (KG) foundation models (KGFMs) are zero-shot generalizers: trained once, they can predict links on unseen graphs without retraining. However, understanding when and how they can robustly generalize across KGs is still an open question. In this paper, we shed some light on their generalization mechanisms highlighting how their performance on unseen KGs is not uniform when it comes to partially seen links, which we call half-links. In fact, we show that to predict a test triple $(h,r,t)$ it might suffice in practice to have observed the half-link $(h,r)$ or $(r,t)$ in the inference graph. This yields a taxonomy of four scenarios when combinations of these half-links are observed or not. In a rigorous stratified analysis over these scenarios, we reveal that SoTA KGFMs use seen half links for predictions, while unseen half-links pose different challenges. As such, our finer-grained taxonomy can be a diagnostic protocol for robust KGFM generalization and highlights where novel KGFMs can improve.

---


### 104. [LLM Consumer Behavior Theory: Foundations of a Novel Research Field](https://arxiv.org/abs/2606.18005)

**<font color=#1a73e8>作者：</font>** Manon Reusens, Sofie Goethals, David Martens  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as autonomous agents that make consumption decisions on behalf of users. This shift raises fundamental questions for consumer theory, which has traditionally modeled humans as the primary decision-makers. In this paper, we introduce LLM Consumer Behavior Theory, a new field of study concerned with analyzing consumer behavior in agentic markets. Drawing on classical and behavioral economics alongside recent advances in Natural Language Processing, we formalize how human preferences are reflected and acted upon by LLM-based agents, and how agent-level decisions aggregate into market demand. We unify previously fragmented literature on LLM decision-making, human behavior simulation, and preference elicitation under a common economic lens, highlighting where assumptions, such as rationality and heterogeneity, may fail in agentic markets. Rather than providing empirical validation, this paper outlines the scope of LLM consumer behavior and identifies open research questions related to alignment, preference representation, and market dynamics.

---


### 105. [ParaTutor: LLM Mediated Parent Child Tutoring through Role Separated Scaffolding Interface in Real Time](https://arxiv.org/abs/2606.18030)

**<font color=#1a73e8>作者：</font>** Lan Luo, Anqi Wang, Muzhi Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Parent child tutoring is a collaborative learning setting with asymmetric roles, where parents guide children s problem solving while children engage in understanding and reasoning. However, most LLM based learning systems are designed for either single users or symmetric collaboration, leaving parent child tutoring with distinct instructional roles underexplored. Through a formative study, we find that effective parent child tutoring depends on preserving these distinct roles, with parents guiding the learning process and children remaining actively engaged in reasoning. We also identify recurring challenges when parents struggle to understand problem structure, lack sufficient knowledge to provide support, or encounter communication difficulties that disrupt shared understanding. To address these challenges, we present ParaTutor, a scaffolding system that provides different forms of support to parents and children. ParaTutor supports parents with guidance for tutoring and provides children with visual grounding for problem solving. We evaluate ParaTutor with 23 parent child dyads (children aged 10 to 12) under four tutoring conditions that vary how LLM assistance is delivered. Results show that generic LLM assistance tends to reduce the parent s role in tutoring, whereas ParaTutor better preserves parent led support and sustains children s participation in reasoning. These findings suggest that in multi users learning, the value of LLM support depends not only on model capability but also on how support is distributed across users with different roles. Our work contributes design implications for LLM systems that support family learning.

---


### 106. [When English Isn't the Best Teacher: Source Language Effects in Cross-Lingual In-Context Learning](https://arxiv.org/abs/2606.18033)

**<font color=#1a73e8>作者：</font>** Fred Philippy, Siwen Guo, Jacques Klein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual transfer in multilingual NLP has been widely explored in supervised fine-tuning contexts, where factors like data availability and linguistic similarity largely determine transfer quality. As the field shifts toward few-shot In-Context Learning (ICL), it is often presumed that insights from fine-tuning carry over unchanged. Yet this assumption has not been rigorously evaluated, leaving open the question of how to choose source languages for cross-lingual ICL. We conduct a broad empirical study of cross-lingual transfer in ICL spanning seven tasks, six models, and a typologically diverse set of languages. We further analyze language confusion, a key obstacle for generative tasks in cross-lingual ICL. Our results show that conventional fine-tuning-based expectations do not consistently apply in the ICL regime and point to alternative heuristics for selecting source languages effectively.

---


### 107. [ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents](https://arxiv.org/abs/2606.18037)

**<font color=#1a73e8>作者：</font>** Ander Alvarez, Santhiya Rajan, Samuel Mugel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents increasingly use the Model Context Protocol (MCP) to answer from heterogeneous evidence sources, including search, APIs, databases, clinical records, and formulary tools. Standard factuality metrics usually test whether an answer is supported by pooled evidence, missing a provenance-sensitive failure mode: a claim may be supported somewhere while being attributed to the wrong source. We call this cross-source conflation.
We introduce ProvenanceGuard, a source-aware verifier for MCP-grounded answers. It consumes captured MCP traces with stable tool IDs, source IDs, and raw outputs; decomposes answers into atomic claims; routes claims to source-specific evidence; checks support with NLI and a token-alignment proxy; compares stated attribution with the routed source; and returns per-claim verdicts plus an answer-level allow/block decision. Blocked answers can be repaired with retrieval-augmented answer revision and re-verified.
We evaluate on 281 medical-domain MCP-agent traces. A 266-trace adjudicated subset yields 2,325 LLM-assisted claim labels split by trace; 361 held-out labels are human-verified. On the 40-trace held-out split, ProvenanceGuard achieves block F1 0.802 and source accuracy 0.858 over 260 source-eligible claims, outperforming source-blind baselines that do not emit claim-to-source IDs. On a harder multi-source benchmark it reaches block F1 0.846, while source-plus-relation accuracy drops to 0.229, showing that exact source ownership remains difficult with semantically close sources. Repair-and-reverify resolves all blocked answers in the full trace set, often via conservative fallback. In 50 controlled clinical conflation probes, ProvenanceGuard detects all injected attribution swaps with no retained wrong attribution. These results show that source attribution is an independent axis for factuality verification in MCP-based agents.

---


### 108. [Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose](https://arxiv.org/abs/2606.18051)

**<font color=#1a73e8>作者：</font>** Xueping Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on external skills -- reusable tool specifications -- but real-world tasks often require composing multiple skills, not just selecting one. We formalize this as the Compositional Skill Routing problem: given a complex user query and a large skill library, decompose the query into atomic sub-tasks, retrieve the appropriate skill for each sub-task, and compose an executable plan. We present SkillWeaver, a decompose-retrieve-compose framework combining an LLM task decomposer, a bi-encoder skill retriever with FAISS indexing, and a dependency-aware DAG planner. To support evaluation, we introduce CompSkillBench, a benchmark of 300 compositional queries over 2,209 real MCP server skills spanning 24 functional categories, sourced from the public MCP ecosystem. Our experiments reveal that task decomposition quality is the primary bottleneck: standard LLM decomposition reaches only 34.2% category recall at the step level. To address this, we propose Iterative Skill-Aware Decomposition (SAD), a retrieval-augmented feedback loop that iteratively aligns decomposition with available skills. SAD improves decomposition accuracy from 51.0% to 67.7% (+32.7%, Wilcoxon p < 10^-6) in a single iteration; DA-conditioned analysis confirms that correct granularity is the prerequisite for effective retrieval (CatR@1 rises from 34% to 41% when DA=1). SkillWeaver reduces context window consumption by over 99%, and transfer experiments confirm generalization (+35.6% relative DA gain even when target categories are absent from the retrieval pool).

---


### 109. [PseudoBench: Measuring How Agentic Auto-Research Fuels Pseudoscience](https://arxiv.org/abs/2606.18060)

**<font color=#1a73e8>作者：</font>** Xinyang Liao, Lingyu Li, Huacan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Model based agents enter autonomous scientific research, their ability to resist pseudoscience becomes increasingly important. Otherwise, such systems may rapidly generate plausible yet misleading studies that contaminate academic literature and erode trust in science. We present PseudoBench, an adversarial benchmark for evaluating whether agentic auto-research systems can identify and resist pseudoscientific narratives. PseudoBench contains 200 curated pseudoscientific claim-evidence pairs across five domains and evaluates agents through an end-to-end research pipeline from experiments to writing. Testing seven state-of-the-art agents, we find that current systems readily produce persuasive reports that align with pseudoscientific premises with near-zero refusal rates and the highest resistance of only 27.4%. Stronger agents risk packaging pseudoscience in more sophisticated scientific language, increasing its apparent credibility. These findings reveal an alarming capacity to fuel pseudoscience, calling for scientific alignment before widespread deployment.

---


### 110. [Security and Privacy Prompts in the Wild: What Users Ask LLMs and How LLMs Respond](https://arxiv.org/abs/2606.18062)

**<font color=#1a73e8>作者：</font>** Hobin Kim, Xiaoyuan Wu, Omer Akgul 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used to fulfill users' information needs; users ask LLMs about the weather, pose educational questions, and consult them for legal assistance. One particularly understudied area is digital security and privacy (S&P), where users may seek LLMs' help on how to secure their online accounts or protect their computers from cyber attacks. To the best of our knowledge, no prior study has collected or analyzed the S&P questions users ask LLMs; prior research on LLM response quality relied on expert-authored S&P misconceptions or FAQs rather than user queries. Drawing from WildChat, a dataset of 3.2M user-LLM conversations collected in the wild, our study identifies 14,727 S&P prompts and categorizes them into nine categories covering a wide range of S&P topics. From the S&P prompts, we sampled 450 and performed a thematic analysis to characterize the S&P questions users ask LLMs. Separate from the thematic analysis, we curated 270 advice-seeking S&P prompts, where users ask for recommendations, guidance, or specific S&P information. We measured LLM response quality and consistency when posing the prompt to LLMs 10 times. We found that commercial LLMs outperform open-weight models (GPT 5.5 provided "good enough" responses on 98% of prompts; Llama 4 on 47%). However, among prompts that received high-quality responses on average, commercial models sometimes produce contradictory responses across runs, risking confusing or misleading users.

---


### 111. [When LLMs Analyze Scars: From Images to Clinically-Meaningful Features](https://arxiv.org/abs/2606.18063)

**<font color=#1a73e8>作者：</font>** Ruman Wang, Hangting Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image classification faces a fundamental dilemma: while deep learning models achieve remarkable performance at scale, real-world clinical scenarios often suffer from severe data scarcity due to annotation costs, privacy constraints, and disease rarity. This challenge is particularly pronounced in pathological scar classification, where differentiating keloids from hypertrophic scars requires subtle expert knowledge and labeled images are extremely limited. We propose a novel paradigm that repositions large language models (LLMs) as knowledge-driven feature engineers rather than end-to-end classifiers. We call this framework ScaFE (Scar Feature Engineering). Our key insight is that LLMs encode rich medical knowledge that can be externalized as executable feature extraction code, enabling the transformation of high-dimensional images into low-dimensional, clinically interpretable representations. Specifically, we prompt an LLM with established scar assessment criteria to generate deterministic Python code that extracts features aligned with clinical scoring systems such as the Vancouver Scar Scale. Our approach offers three key advantages: (1) data efficiency, achieving robust performance with limited training samples by decoupling knowledge acquisition from statistical learning; (2) privacy preservation, as raw images are processed locally without exposure to external LLMs; and (3) interpretability, through explicit features grounded in clinical reasoning. Extensive experiments on scar classification demonstrate that our method consistently outperforms end-to-end deep learning baselines or using LLMs as black-box classifiers under limited data conditions, establishing a promising direction for integrating LLMs into data-efficient and clinically transparent medical AI systems.

---


### 112. [NoiseTilt: Noise-Tilted Reverse Kernels for Diffusion Reward Alignment](https://arxiv.org/abs/2606.18066)

**<font color=#1a73e8>作者：</font>** Jisung Hwang, Yunhong Min, Jaihoon Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Noise-Tilted Reverse Kernel (NTRK), a reward-guided diffusion sampler that injects reward gradients through the noise term, leaving the pretrained reverse kernel unchanged and requiring only a single sample per step. Reward-guided sampling at inference time has greatly expanded the versatility of pretrained diffusion models. Yet existing methods face a trade-off. Gradient-based guidance shifts the reverse mean, steering generation but pushing intermediate states outside the region that the model was trained on and degrading quality. Search-based methods preserve quality but gain no gradient signal. No prior method achieves both. NTRK resolves this by keeping the reverse mean fixed and biasing the noise term toward high reward. We introduce a whitening operator, the central mechanism behind NTRK, that makes the reward gradient safe to inject as noise without losing its guiding signal. Across various reward alignment tasks, NTRK outperforms recent state-of-the-art baselines without losing sample quality. Remarkably, on aesthetic generation, NTRK surpasses the reward of the best baseline at 500 NFEs using only 25 NFEs, a 20$\times$ reduction in compute.

---


### 113. [Agentic AI-based Framework for Mitigating Premature Diagnostic Handoff and Silent Hallucination in Healthcare Applications](https://arxiv.org/abs/2606.18068)

**<font color=#1a73e8>作者：</font>** Divyansh Srivastava, Shreya Ghosh, Anshul Verma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) and multi-agent systems have driven the rise of Agentic AI, showing promise for medical reasoning. However, open-ended conversational agents remain prone to two critical failure modes: premature diagnostic handoff and silent clinical hallucinations that may go undetected before reaching the patient. In this work, we propose a multi-agent framework that addresses both issues by replacing ``LLM-as-a-judge'' routing with deterministic orchestration constraints. The framework incorporates two safety mechanisms. First, a neuro-symbolic state-tracking gate enforces completeness of the OLDCARTS clinical protocol (Onset, Location, Duration, Character, Aggravating/Alleviating factors, Radiation, Timing, and Severity) by blocking diagnostic transitions until all required dimensions are collected. Second, an epistemic uncertainty quantification (UQ) gate computes semantic entropy (H) across K=5 independent diagnostic samples to identify and intercept divergent outputs before delivery.
We evaluate the system using simulated patient agents powered by the llama-3.1-70b-instruct model on 150 test cases. The full architecture achieves 49.3% diagnostic precision, representing an absolute improvement of 11.3 percentage points over an unconstrained baseline. Additionally, we observe a statistically significant negative correlation (r = -0.181, p < 0.05) between OLDCARTS completeness (\sigma) and semantic entropy (H), suggesting that structured information gathering is associated with reduced diagnostic uncertainty.

---


### 114. [A Unified Framework for Context-Aware and Relation-Aware Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2606.18075)

**<font color=#1a73e8>作者：</font>** Haoyang Zhong, Yifei Sun, Antong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has emerged as a paradigm for enhancing large language models (LLMs) with external knowledge, yet existing graph-based methods face a fundamental limitation: entity-centric and chunk-centric approaches operate on representations anchored to original text without true knowledge fusion. While entity-centric methods connect logically related content and chunk-centric methods preserve context, both retrieve information separately through similarity search, missing emergent understanding from their synthesis. In this paper, we propose HyGRAG, a hierarchical graph RAG framework that transcends source documents by addressing three core challenges: constructing summaries that genuinely integrate contextual and relational information, leveraging these synthesized representations to access emergent knowledge during retrieval, and efficiently updating hierarchical structures for dynamic corpora. Specifically, we design hierarchical index structures over hybrid graphs with both chunk and entity nodes, then iteratively cluster them and generate LLM-based summaries. Then, we design context and relation-aware retrieval that searches across all abstraction levels while expanding through community membership. Moreover, we enable dynamic knowledge update through attachment-based algorithms with only local re-summarization. Experimental results show that HyGRAG improves the average accuracy of multi-hop reasoning tasks by 9.7%, while maintaining reasonable efficiency.

---


### 115. [From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning](https://arxiv.org/abs/2606.18089)

**<font color=#1a73e8>作者：</font>** Lingjing Kong, Xin Liu, Guangyi Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training pipelines that combine supervised fine-tuning (SFT) with reinforcement learning (RL) have emerged as the key recipe for transforming large language models (LLMs) into robust reasoners. We argue that this combined success is driven by compositional generalization, which we formalize through a hierarchical latent selection model. In this framework, reasoning traces are generated by a cascade of discrete latent selection variables corresponding to reusable atomic modules, including both skills (local operations) and routing mechanisms (how intermediate information is selected, reused, and composed). Within this model, we theoretically show that SFT and RL play asymmetric, complementary roles: SFT supplies the raw module materials in compositional traces, and RL decomposes those traces to identify the latent atomic modules and enable compositional generalization. We design controlled experiments to validate this theory. Our results demonstrate that RL can extract atomic modules from compound traces supplied by SFT and recombine them to solve new configurations. Moreover, we find that training on compound traces yields stronger generalization than training on isolated atomic modules. Finally, we investigate the relationship between SFT and RL data and identify an effective protocol in which SFT ensures coverage of all atomic modules through compositional traces, while RL focuses on novel compositions outside the SFT support to drive exploration.

---


### 116. [IsabeLLM: Automated Theorem Proving Applied to Formally Verifying Consensus](https://arxiv.org/abs/2606.18098)

**<font color=#1a73e8>作者：</font>** Elliot Jones, William Knottenbelt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in Artificial Intelligence (AI) have led AI for Theorem Proving to become a promising means of formally verifying computer systems. Whilst formal verification is traditionally reserved for safety-critical systems due to the required amount of expertise and effort, AI can help to automate a large amount of this workload and make it far more accessible. Blockchain-based systems are becoming increasingly popular and are frequently targeted by malicious actors, often resulting in huge financial losses, highlighting the need to better verify these systems and mitigate vulnerabilities. Arguably the most important component of these systems is the consensus protocol, which allows nodes to agree on decisions in a potentially adversarial environment. In this paper, we improve upon IsabeLLM, the automated theorem proving tool in Isabelle. Namely, we implement a Retrieval-Augmented Generation framework, Error tracing and counterexample generation for improved context supplied to the Large Language Model. Compatibility with the latest version of Isabelle and Sledgehammer is also implemented for improved efficiency. We compare the performance of the two versions of IsabeLLM in their ability to complete the verification of Bitcoin's Proof of Work consensus.

---


### 117. [HistoRAG: Embedding Historical Methodology in Retrieval-Augmented Generation Through Critical Technical Practice](https://arxiv.org/abs/2606.18103)

**<font color=#1a73e8>作者：</font>** Noah J. Kim-Baumann, Torsten Hiltmann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) is the prevailing architecture for grounding language model outputs in external evidence, yet its dominant evaluation paradigms and default configurations remain oriented toward factual question-answering. For interpretive disciplines such as historical studies, RAG embeds assumptions that conflict with scholarly practice. We introduce HistoRAG, a framework that translates historiographical principles into concrete architectural interventions. Separated retrieval and generation decouples source discovery from interpretation, temporal windowing enforces balanced source representation across the research period as a methodological requirement of historical inquiry, and LLM-as-judge evaluation makes relevance judgments transparent and contestable. We evaluate these interventions using SPIEGELragged, applied to 102,189 articles from Der Spiegel (1950-1979). Each intervention addresses a measurable deficiency in standard RAG: era-specific vocabulary retrieves zero chunks from the 1950s when using 1970s terminology, evidence of the temporal skew that motivates windowing; vector similarity and LLM-assessed relevance correlate only weakly (Spearman rho = 0.275), motivating post-retrieval evaluation; and keyword-based and semantic retrieval surface largely disjoint source pools, motivating an architecture in which both operate as complementary retrieval layers under a shared LLM evaluation filter. We also introduce the concept of Zwischentexte (intermediate texts that function as interpretive proposals rather than findings) as a framework for responsible integration of LLM-generated text into scholarly practice. The architecture offers a model for how domain-specific epistemological commitments can be translated into RAG design decisions, and may transfer to other interpretive disciplines working with large corpora.

---


### 118. [HLS-GPT: A Generative Pretrained Transformer (GPT) for Continental-Scale NASA Harmonized Landsat and Sentinel-2 (HLS) Reflectance Reconstruction Across All Bands on Arbitrary Dates](https://arxiv.org/abs/2606.18115)

**<font color=#1a73e8>作者：</font>** Junjie Li, Hankui K. Zhang, David P. Roy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent deep learning methods for Landsat and Sentinel-2 reflectance time series reconstruction remain limited by restricted spectral coverage, limited geographic scalability, or patch-based designs with short temporal contexts. We present HLS-GPT, a large-scale generative pretrained Transformer model for reconstructing NASA Harmonized Landsat Sentinel-2 30 m surface reflectance for all bands, any date, and any pixel location. HLS-GPT uses a hierarchical Transformer architecture to handle the different spectral band configurations of Landsat and Sentinel-2 and operates on single-pixel 12-month time series. To capture geographic and seasonal variability, the model was trained with nine years of HLS time series from more than 0.25 million training pixels across the conterminous United States. A random cropping and masking strategy extracts 12-month periods with varying start dates across epochs, masks 50% of valid observations, and trains the model to reconstruct the masked reflectance values from the remaining observations. Evaluation using more than 62,000 independent test pixels shows robust reconstruction under diverse land surface conditions, including complex crop phenology and sparse, irregular observations. Leave-one-observation-out evaluation achieved reconstruction RMSE below 0.026 for all HLS spectral bands, with relative RMSE below 35% for visible bands and below 13% for other bands. Red-edge band errors were comparable to red and near-infrared errors despite the absence of red-edge bands on Landsat. Sensitivity analyses that randomly masked 10% to 90% of test observations showed only modest degradation when 10% to 50% of observations were masked, with all-band RMSE below 0.028. Image reconstruction over nine independent 109 by 109 km CONUS HLS tiles further demonstrates that HLS-GPT outperforms two conventional methods and the NASA-IBM Prithvi model.

---


### 119. [Predicting Immune Biomarkers with MultiModal Mixture-of-Expert Pathology Foundation Models Empowers Precision Oncology](https://arxiv.org/abs/2606.18123)

**<font color=#1a73e8>作者：</font>** Tianyu Liu, Ziqing Wang, Zhaokang Liang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting immune biomarkers associated with the tumor immune microenvironment (TIME) is critical for advancing precision oncology, yet existing approaches are largely limited to single image modalities and suffer from insufficient resolution and incomplete utilization of complementary clinical and biological information. Here we introduce MixTIME, a multimodal foundation model that leverages a mixture-of-experts (MoE) architecture to integrate pathology foundation models trained across distinct modalities: image only (UNIv2), image text (CONCHv1.5), and image transcriptomic (STPath) representations for pixel-level and slide-level prediction of multiplex immunofluorescence (mIF) protein expression from hematoxylin and eosin (HE) whole-slide images. MixTIME employs a learnable router to dynamically weight expert contributions and is trained with a distribution- and tendency-aware loss function. Benchmarked on two datasets of different scales, MixTIME achieves state-of-the-art performance across 17 protein markers as measured by correlation metrics. The predicted mIF profiles substantially enhance downstream tasks, including spatial domain identification, survival prediction, and AI-assisted pathology report generation validated by expert pathologists from multiple institutes across the world. Furthermore, MixTIME enables longitudinal tracking of protein expression dynamics across clinical time points and reveals protein gene interaction patterns linked to drug resistance and immune suppression in tumor microenvironments. Collectively, MixTIME provides a scalable framework for multimodal biomarker discovery and clinical translation in computational pathology.

---


### 120. [Unintended Effects of Geographic Conditioning in Large Language Models](https://arxiv.org/abs/2606.18124)

**<font color=#1a73e8>作者：</font>** Naz Col, David M. Chan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern conversational AI systems frequently rely on user metadata to localize responses, yet the unintended regional biases introduced by this hidden context remain poorly understood. In this work, we evaluate location leakage: the phenomenon where a model generates geographic references despite receiving a geographically neutral user prompt. Across both creative writing and open-ended Q&A prompts, even state-of-the-art LLMs systematically favor region-specific outputs when exposed to location metadata, with leakage spiking by up to 793 times above baseline (e.g., from 0.04% to 31.7% for Llama 3.1-8B, and 21.3% and 8.8% for Qwen3-8B and Claude Sonnet 4.6, respectively). Our analysis further shows a novel structural conditioning effect: replacing the injected location with the placeholder "Unknown" still elevates leakage by up to 72 times above baseline, demonstrating that the user profile frame itself, independent of any geographic content, acts as a generative conditioning signal.

---


### 121. [Towards Understanding and Measuring COGNITIVE ATROPHY in LLM Behaviour](https://arxiv.org/abs/2606.18129)

**<font color=#1a73e8>作者：</font>** Abeer Badawi, Moyosoreoluwa Olatosi, Negin Baghbanzadeh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent incidents involving LLMs used for mental-health support reveal a critical evaluation gap: surface-level safety scores do not capture how models behave across realistic, emotionally sensitive interactions over time. Existing benchmarks measure knowledge, safety, or static response quality, but miss whether LLM interactions help users keep reflecting, coping, and making decisions themselves. We formalize this missing dimension as COGNITIVE ATROPHY, a process-level behavioural measure in AI-mediated mental-health support distinct from safety and helpfulness. To measure it, we introduce COGNITIVE ATROPHY BENCH, a clinically grounded benchmark built from 1,576 fully human-generated counseling conversations, 15,680 turns, and 42,230 responses from five LLMs. Three clinical and neuropsychology experts developed a 20-attribute schema spanning user context, response behaviour, and global risk flags; six trained clinical reviewers applied it with span-grounded evidence, producing 5,324 reviewer judgments. We further introduce the User-Input Risk Index (UIRI), the Cognitive Atrophy Risk Index (ARI), and trajectory summaries. Across five LLMs, models show a consistent moderate-to-high level of atrophy-aligned behaviour across single and multi-turn settings. While models generally respond to overt safety cues, they adapt less reliably when users seek solutions or decisions. The dominant recurring patterns are directive advice, problem-solving, recommendation responses, topic shifts, and forms of validation that may reinforce dependence rather than reflection. Our work makes COGNITIVE ATROPHY measurable and provides a foundation for auditing model behaviour in sensitive LLM conversations.

---


### 122. [Your AI Travel Agent Would Book You a Bullfight: An Agentic Benchmark for Implicit Animal Welfare in Frontier AI Models](https://arxiv.org/abs/2606.18142)

**<font color=#1a73e8>作者：</font>** Jasmine Brazilek, Oliver Tulio, Joel Christoph 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are moving from advisors to actors, booking travel, planning menus, and running procurement on behalf of users. Existing benchmarks for AI and animal welfare evaluate model text responses to question-answer prompts, leaving open whether the welfare reasoning surfaced in those responses transfers to agentic deployment where the model must take actions with tools. We introduce TAC (Travel Agent Compassion), the first agentic benchmark measuring whether AI agents avoid options involving animal exploitation when acting on behalf of users. TAC presents an AI agent with twelve hand-authored travel booking scenarios across six categories of animal exploitation, augmented to forty-eight samples to control for price, rating, and position confounds. We evaluate seven frontier models from four labs. Every model scores below the chance level of sixty-four percent, with the best performer (Claude Opus 4.7) at fifty-three percent. A single welfare-aware sentence in the system prompt yields gains of forty-seven to sixty-three percentage points in Claude and GPT-5.5, twenty-six points in GPT-5.2, and under twelve points in DeepSeek and Gemini. An auxiliary Inspect Scout audit of 288 base-condition transcripts from the top two performers, using Gemini 2.5 Flash Lite as judge, flags zero transcripts for evaluation awareness, suggesting the below-chance rates do not stem from the models recognising the evaluation. We discuss implications for category-level variation across cultural domains, the limits of text-response welfare benchmarks, and the EU General-Purpose AI Code of Practice systemic risk framework.

---


### 123. [WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning](https://arxiv.org/abs/2606.18147)

**<font color=#1a73e8>作者：</font>** Yuwei Zhang, Tong Xia, Bianca Emmerich 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are remarkably capable at medical question answering, in some cases surpassing the accuracy of general physicians. However, answering questions about wearable health data remains challenging and understudied, as these ubiquitous sensors produce continuous, high-dimensional, and longitudinal data, which is non-trivial to align with text-centric distributions in LLM pretraining. The diversity of sensor modalities and user intents cannot be effectively handled by a fixed reasoning workflow or a single pretrained foundation model. To address these challenges, we propose WEQA, a query-adaptive agent framework that unifies LLM reasoning with specialized wearable analytical and modeling tools. An LLM controller is employed to synthesize execution plans and dynamically route each query to the appropriate combination of sensor analysis and pretrained models, and perform grounded response auditing with external knowledge. We also curate a benchmark spanning four open wearable datasets comprising analytic and predictive tasks in three different health domains. Experiments show that our framework is 24% more accurate than LLM and agentic baselines, and a blinded study with 12 medical experts and 8 users shows substantial gains in usefulness and clinical soundness.

---


### 124. [Learning Cardiac Electrophysiology Digital Twins Through Agentic Discovery of Hybrid Structure](https://arxiv.org/abs/2606.18154)

**<font color=#1a73e8>作者：</font>** Ziqi Zhou, Yubo Ye, Sumeet Atul Vadhavka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building personalized cardiac electrophysiology (EP) digital twins requires identifying the appropriate model structure for each patient, not merely fitting parameters. Traditional methods rely on experts to manually prescribe hybrid physics-neural architectures, which requires deep domain expertise and does not transfer across patients. Recent works have applied large language models (LLMs) to generate or act as hybrid models. However, despite their promising generalization capacity, these LLM-based methods lack the structural priors needed for stable cardiac simulations. Hence, we propose LEADS, a framework that formulates cardiac EP domain knowledge as a structured action space and utilizes an LLM agent to discover hybrid models. The agent follows an iterative reasoning-and-action loop to select, combine, and refine hybrid models, whilst gradient descent handles parameter fitting. The proposed LEADS designs every candidate model towards physically grounded, interpretable, and numerically stable, while allowing open-ended architectural discovery. We validate LEADS on synthetic data with three ground-truth reaction models and on real cardiac EP data, demonstrating that it outperforms both human-designed hybrid models and other LLM-based hybrid modeling.

---


### 125. [EgoCS-400K: An Egocentric Gameplay Dataset for World Models](https://arxiv.org/abs/2606.18180)

**<font color=#1a73e8>作者：</font>** Rongjin Guo, Dong Liang, Yuhao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The shift from video generation to interactive world modeling places new demands on data: beyond captioned videos, world models require temporally aligned video-action-language trajectories grounded in the actions, camera motion, states, and events that drive future scene changes. However, such data is difficult to obtain at scale. Web video datasets offer broad visual coverage but lack executable actions and reliable states; robotic datasets provide action and state supervision but are costly and limited in scene diversity; and existing simulators often lack large-scale human-driven interaction trajectories. In this paper, we introduce EgoCS-400K, a large-scale replay-grounded egocentric Counter-Strike dataset for world models, built from public professional CS and CS2 match demos that preserve human gameplay trajectories and enable parsing, replaying, rendering, and temporal alignment. We extract player states, view directions, movements, keyboard/button inputs, view-angle changes, weapon usage, game events, and round-level context, and render clean first-person videos from the same trajectories. EgoCS-400K contains over 400,000 first-person videos and 10,000 hours of gameplay from more than 1,000 matches and 40,000 rounds, covering 13 maps and 10 player viewpoints per round. It supports a range of interactive visual modeling tasks, including action-conditioned future prediction, state- and event-aware scene rollout, replay-grounded captioning, and agent egocentric action understanding. By connecting visual observations with human actions, camera motion, game states, and events at scale, EgoCS-400K serves as a practical bridge between passive web videos, controllable game simulation, and costly real-world embodied data.

---


### 126. [Learning from the Self-future: On-policy Self-distillation for dLLMs](https://arxiv.org/abs/2606.18195)

**<font color=#1a73e8>作者：</font>** Yifu Luo, Zeyu Chen, Haoyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) has proven effective for post-training large language models (LLMs), yet its application to diffusion LLMs (dLLMs) remains unexplored. Existing OPSD methods are inherently autoregressive-centric. They inject privileged information via left-to-right prefix conditioning with token-level divergence supervision, a design that fundamentally conflicts with the arbitraryorder generation of dLLMs. We introduce d-OPSD, the first OPSD framework tailored for dLLMs. Our approach makes two core contributions. First, we reframe self-teacher construction by using self-generated answers as suffix conditioning, enabling the student model to learn from "self future-experience" rather than privileged prefixes. Second, we shift supervision from token-level to step-level, aligning training with the iterative denoising process of dLLMs. Experiments across four reasoning benchmarks show that d-OPSD consistently outperforms RLVR and SFT baselines with superior sample efficiency, requiring only around 10% of the optimization steps by RLVR and opening a promising pathway for dLLM posttraining. The code is available at this https URL.

---


### 127. [RubricsTree: Scalable and Evolving Open-Ended Evaluation of Personal Health Agents across Health Memory and Medical Skills](https://arxiv.org/abs/2606.18203)

**<font color=#1a73e8>作者：</font>** Weizhi Zhang, Zechen Li, Hamid Palangi 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The LLM-empowered personal health agents with user health (sensor) metrics have offered a promising pathway to alleviate global disparities in healthcare access. However, large-scale clinical deployment remains constrained by an open-ended evaluation bottleneck: physician annotation is reliable but costly and unscalable, while LLM-as-a-judge evaluators are scalable but subjective, inconsistent, and sometimes clinically misaligned. We introduce RubricsTree, a scalable evaluation framework with an expert-aligned hierarchical taxonomy of over 100 atomic, clinically-verifiable Boolean rubrics, evolving from the insights of 4,000 real user queries through an iterative human-in-the-loop curation protocol with an expertise panel led by an experienced physician. A context-aware adaptive router activates only the relevant auto-weighted rubric subset per query, providing the throughput needed for scalable evaluation with expert-aligned quality. Through a systematic meta-evaluation, we show that RubricsTree (i) substantially exceeds a strong large-scale evaluation baseline in expert alignment on challenging open-ended queries; (ii) reliably penalizes contextually degraded responses; and (iii) when used as structured instructions, text feedback, or training rewards for performance optimization, yields up to ~66% relative gains on HealthBench for Gemini, GPT, and Qwen model families. RubricsTree thus provides a scalable, auditable, and evolving evaluation infrastructure required for the continuous optimization of product-level personal healthcare AI.

---


### 128. [Looped World Models](https://arxiv.org/abs/2606.18208)

**<font color=#1a73e8>作者：</font>** Hongyuan Adam Lu, Z.L. Victor Wei, Qun Zhang 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors. We resolve this by introducing Looped World Models (LoopWM), which are the first looped architectures for world modelling. Our method iteratively refines latent environment states through a parameter-shared transformer block. This yield up to 100x parameter efficiency over conventional approaches with adaptive computation that automatically scales depth to match the complexity of each prediction step. Orthogonal to scaling model size and training data, LoopWM establishes iterative latent depth as a new scaling axis for world simulation, which might significantly push the community forward.

---


### 129. [Zone of Proximal Policy Optimization: Teacher in Prompts, Not Gradients](https://arxiv.org/abs/2606.18216)

**<font color=#1a73e8>作者：</font>** Byung-Kwan Lee, Ximing Lu, Shizhe Diao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation transfers a teacher's competence to a small student but is brittle in the small-student regime: forcing the student to imitate logits from a much larger teacher concentrates it on the teacher's sharpest modes, hurting generalization on benchmark families beyond the training corpus. Reinforcement learning (RL) avoids logit imitation by training on the student's own rollouts. However, on questions where every rollout fails-yielding zero advantage and being silently discarded-injecting a stronger teacher's response into the policy gradient breaks the on-policy assumption and induces drift. We introduce Zone of Proximal Policy Optimization (ZPPO), inspired by Vygotsky's zone of proximal development, which keeps the teacher inside the prompt rather than the policy gradient. On hard questions, ZPPO constructs two reformulated prompts: a Binary Candidate-included Question (BCQ) pairs one correct teacher response with one incorrect student response as anonymized candidates the student must discriminate, and a Negative Candidate-included Question (NCQ) aggregates the student's wrong rollouts into a single prompt to surface their shared failure modes. A prompt replay buffer recirculates each hard question until it either graduates-the student's mean rollout accuracy on it reaches half- or is FIFO-evicted under finite capacity, amplifying BCQ and NCQ inside the student's current zone of proximal development. On the Qwen3.5 family at four student scales (0.8B-9B) with a 27B teacher, post-trained as vision-language models and evaluated on a 31-benchmark suite (16 VLM, 10 LLM, 5 Video), ZPPO outperforms off/on-policy distillation and GRPO, with the largest gains at the smallest scale.

---


### 130. [MAJIC: Leveraging Articulatory Motion for Speech-based Emotion Recognition](https://arxiv.org/abs/2606.18228)

**<font color=#1a73e8>作者：</font>** Tanmay Srivastava, Paras Bhavnani, Benjir Alvee Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce MAJIC, a multimodal emotion recognition system that leverages articulatory motion of the jaw and facial muscles for speech-based emotion recognition (SER). While most SER systems perform well on datasets with strongly expressed emotional speech of trained actors, their performance often degrades when emotional expressions become more subtle. We explore this challenge by engineering features from articulatory motion and integrating them with audio features using a multi-task learning framework. Our key insight is that emotion in speech manifests not only through vocal characteristics but also through distinct articulatory motions: jaw movements, facial muscle vibrations, and speech-induced vibrations. While audio captures features such as pitch and prosody, articulatory motion contains complementary information that is not present in audio alone. We evaluate our system on data collected from 20 participants across multiple sessions, 10 languages, and diverse scenarios, including prompted and conversational speech, showing its robustness across users and settings. MAJIC achieves 93% accuracy and 91% F1 score for emotion classification, outperforming strong audio-based baselines on our dataset.

---


### 131. [ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues](https://arxiv.org/abs/2606.18237)

**<font color=#1a73e8>作者：</font>** Shanda Li, Qiuhong Anna Wei, Jingwu Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reproducing research results from papers and released code is central to scientific progress. Existing works have introduced benchmarks to evaluate whether LLM agents can assist with reproducibility, but they are difficult to scale due to their reliance on substantial manual effort for data curation and evaluation. We introduce ReproRepo, a scalable framework for reproducibility evaluation that leverages human-raised GitHub issues as naturally occurring supervision on realistic reproduction blockers. We instantiate ReproRepo on 1,149 recent machine learning papers from major conferences and evaluate four frontier model-agent configurations. Our results show that LLM agents, even without executing code, can identify many real-world reproducibility problems from paper-repository pairs: the best agent in our study, namely Codex with GPT-5.5, surfaces at least one semantically related human-reported blocker for ~90% of papers in the study. Further analysis shows that agents are particularly effective for surfacing visible failures and identifying the right semantic region, but may still be insufficient in exact localization. ReproRepo can serve as a reusable, scalable framework for future evaluations of LLM agents on real-world reproducibility auditing. Our code is released at this https URL.

---


### 132. [Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification](https://arxiv.org/abs/2606.18249)

**<font color=#1a73e8>作者：</font>** Wujian Peng, Lingchen Meng, Yuxuan Cai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Modeling aims to integrate visual understanding and generation within a single system. However, existing approaches typically rely on two disparate visual tokenizers, which splits the representation space and hinders truly unified modeling. We propose UniAR, a unified autoregressive framework where a single discrete visual tokenizer serves as the key bridge between understanding and generation, enabling a shared context in which the model can directly interpret its own generated visual tokens without additional re-encoding. UniAR adapts a pretrained vision encoder with multi-level feature fusion and a lookup-free bitwise quantization scheme, preserving both high-level semantics and low-level details while scaling the effective visual vocabulary at minimal cost. Building on this, the unified autoregressive model adopts parallel-bitwise-prediction to jointly predict spatially grouped, multi-level visual codes, substantially reducing visual sequence length and accelerating generation. Finally, a diffusion-based visual decoder operates on discrete visual tokens to decode high-fidelity images. Through large-scale pre-training, followed by supervised fine-tuning and reinforcement learning, UniAR achieves state-of-the-art performance on image generation and image editing while remaining competitive on multimodal understanding benchmarks. The project page is available at this https URL.

---


### 133. [Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion](https://arxiv.org/abs/2606.18250)

**<font color=#1a73e8>作者：</font>** Nils Morbitzer, Jonathan Evers, Artem Savkin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forecasting the evolution of dynamic environments is crucial for autonomous agents. While generative world models have recently achieved high photorealism in 2D video synthesis by mixing ego-motion and environmental dynamics within the image plane, they exhibit physical inconsistencies, such as morphing or vanishing objects, especially over long time horizons. In this paper, we propose FR3D, a world model that predicts a persistent 3D latent representation for future dynamic 3D reconstruction. Unlike prior works that treat the world as a sequence of image-based features, FR3D explicitly decouples the 3D evolution of the scene from the agent's trajectory, treating the inferred ego-motion as a latent proxy for action. This disentanglement resolves the ambiguities between self-motion and world-motion, ensuring geometric consistency into the future. Furthermore, we introduce a teacher-student distillation strategy that leverages the spatial "common sense" of off-the-shelf foundation models, leading to robust zero-shot generalization. Extensive experiments demonstrate FR3D's strong performance for future dynamic 3D reconstruction from monocular observations across multiple datasets, even 2 seconds into the future. Project page: this https URL.

---


> [!TIP]
> 当前位于：**101-133**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-133**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
