# 🧠 大模型相关研究 | 2026年09月14日

> 本类共 **153** 篇论文：已确认 **145** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-153](./part-04.md)

---

### 101. [From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development](https://arxiv.org/abs/2609.11493)

**<font color=#1a73e8>作者：</font>** Reza Amirmoshiri, Faryad Sahneh, Yasser Jangjou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chemistry, Manufacturing and Controls (CMC) process development generates an enormous body of technical information across a multi-stage, knowledge-intensive continuum from drug discovery to commercial manufacturing. This knowledge is traditionally fragmented across functions and heterogeneous formats, causing traceability gaps and significant knowledge-management costs during technology transfer and regulatory filing. We present a modular agentic-AI platform that converts a heterogeneous corpus of process-development documents into a queryable, dual-layer knowledge graph. A base knowledge layer builds a lexical graph with a Document-Section-Chunk hierarchy through lossless ingestion of digital, scanned, handwritten, and multilingual documents, while an intelligence layer extracts ontology-aligned entities and bridges cross-document concepts through a provenance-anchored domain graph. LLM agents operate across both layers, selecting the retrieval path best suited to each question. We evaluate the lexical layer with a novel three-tier protocol measuring the deployment-fidelity of a retrieval-augmented generation (RAG) system on proprietary data, demonstrated on 505 questions curated from 38 development reports of a Sanofi small-molecule program. Tier-1 multiple-choice accuracy of 95% signals strong platform reliability; the stricter Tier-2 LLM-judge pass rate of 85%, which degrades on comparative and corpus-wide questions, reveals a failure taxonomy that Tier-1 accuracy alone fails to capture. A router agent selects between layers according to question type. We anticipate this protocol will enable future designers of agentic platforms to assess their systems against nonpublic databases, and that graph-based architectures will see broader adoption in pharma as a means of transforming fragmented document repositories into structured process intelligence.

---


### 102. [Combining Synthetic and Real Data for Low-Resource Historical OCR: A Manchu Case Study](https://arxiv.org/abs/2609.11495)

**<font color=#1a73e8>作者：</font>** Yan Hon Michael Chung, Hanlin Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Manchu, now critically endangered, was one of the principal languages of the Qing empire (1636-1912), and its extensive archival record is increasingly digitized but remains difficult to search and analyze at scale. Previous work showed that vision-language models (VLMs) trained only on synthetic Manchu word images can reach 87.4% word accuracy on real Qing manuscripts and prints, leaving a substantial synthetic-to-real gap. This study examines how synthetic and real historical training data should be combined for low-resource OCR. Using 60,000 synthetic and 20,306 real historical word images, we evaluate three pretrained VLMs and a compact convolutional recurrent neural network (CRNN) under four regimes: synthetic-only, real-only, joint synthetic-real, and sequential synthetic-to-real training, following a common checkpoint-selection and archival evaluation protocol. Introducing real training images raises the leading configurations to between 95.09% and 96.28% word accuracy, while no synthetic-only configuration exceeds 87.92%. Synthetic supplementation substantially improves all three VLMs, whereas its marginal effect for the CRNN is sensitive to the training objective. Joint and sequential training yield broadly similar archival accuracy under the tested practical pipelines. A compact CRNN also reaches the leading performance range once real images are available, showing that model scale alone does not determine recognition accuracy. Finally, complementary errors among strong recognizers allow voting to raise accuracy to 98.27% without additional training, while an eighteenth-century Manchu dictionary provides a principled rule for adjudicating disagreements.

---


### 103. [ActMap: Single-Pass Uncertainty Quantification from Generation-Time Activation Maps](https://arxiv.org/abs/2609.11498)

**<font color=#1a73e8>作者：</font>** Jacopo Dardini, Roberta Calegari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Practical uncertainty quantification (UQ) for large language models must decide,
from a single generation, whether a specific answer should be trusted. Existing
methods either sample multiple generations, read only output-token probabilities,
or reduce the model's internal computation to a single hidden state. We introduce
ActMap, a white-box representation that compresses the generation-time hidden-
state trajectory (every layer, every generated token) into a fixed $12 \times 32
\times 128$ tensor of temporal-statistic channels that preserves structure across
transformer depth and pooled hidden coordinates. The map is captured during the
generation pass with no measurable overhead, has a fixed shape across model
depths and hidden sizes, and occupies 96 KiB: a compact artifact that can be
retained for audit-relevant generations and probed directly, with occlusion
analysis localizing the classifier's signal to mid-depth regions of the map. A
lightweight classifier, instantiated as a compact Vision Transformer, reads an
estimated correctness probability from each map in a fraction of a millisecond;
capacity-matched MLPs perform comparably, indicating the representation itself
carries the result. Trained and evaluated in-domain on short-answer QA, direct-
answer math, and summarization factuality with three instruction-tuned 7-8B
models, ActMap consistently outperforms sampling, token-probability, attention,
and embedding baselines, and matches ACT-ViT, a detector trained on dense
activation tensors $67 \times$ larger, at essentially the same mean AUROC with
lower calibration error on ten of twelve pairs. The resulting score supports
abstention, routing, and selective verification from a single generation, making
it a practical primitive for scalable oversight of deployed models.

---


### 104. [Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs](https://arxiv.org/abs/2609.11499)

**<font color=#1a73e8>作者：</font>** Zhiqi Li, Yuxuan Liao, Bo Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Code world models represent worlds as executable programs, but this representation alone does not determine how to construct a complex world. We introduce Recursive Code World Models (RCWM), a framework for reconstructing complex 3D worlds in code from a single reference image. RCWM couples a Recursive Scene Program (RSP) representation with a construction solver that recursively calls itself. An RSP represents the executable world as compositional scene code, while each solver call follows the same complete process: establish the whole, recursively reconstruct unresolved parts, and revisit the whole to refine their composition. This global-local-global recursion gives fine-scale structures their own perception-and-editing loops while preserving scene-wide geometry and relationships. Reference-aligned views propagate a shared camera projection across levels, while parent revisitation addresses boundaries, spatial relations, and shared errors that emerge after local refinement. A vision-language coding agent directly compares reference images with scene renders to guide refinement, recursive descent, and return. Across complex scenes, RCWM outperforms prior code-based image-to-scene reconstruction methods. Ablation studies further support the benefits of recursive construction and suggest that deeper calls can improve finer-scale reconstruction. RCWM provides a recursive construction principle for building complex executable worlds from visual evidence.

---


### 105. [Design Reflections on Transition to LLM-Aided Novel Visualizations](https://arxiv.org/abs/2609.11503)

**<font color=#1a73e8>作者：</font>** Richard Brath  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examines data visualization design evolution over 12.5 years, reflecting on the impact of Large Language Models over the last 3.75 years. Using a longitudinal corpus of 55 visualizations from a single-subject design record, the study identifies how LLMs have aided design-space exploration: reducing coding effort, enabling new design opportunities, shock, excitement, accomplishments, and shifts to the design process.

---


### 106. [Structural priors for data-efficient language learning](https://arxiv.org/abs/2609.11505)

**<font color=#1a73e8>作者：</font>** Yana Veitsman, Jonas Mayer Martins, Jonathan Lautenschlager 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efficient language learning requires methods to reduce the reliance on large data and computational resources. We investigate structural transfer: First training models on non-language data to induce useful priors for natural language. This approach is a form of weight initialization for multilingual language modeling. We evaluate transfer via next-token-prediction loss, weight shifts in the model, and downstream linguistic benchmarks. Several symbolic data types - notably music, probabilistic grammars, and cellular automata - yield lower language-modeling loss than random initialization. These gains coincide with smaller weight shifts during subsequent language training, suggesting that structural transfer positions models in a more favorable region of the parameter space. However, a lower loss does not translate consistently into better downstream linguistic performance, and transfer from non-language data is less efficient than additional language data. We conclude that non-language data can serve as a partial substitute for language data for the training objective of next-token prediction but does not reliably support broader linguistic generalization.

---


### 107. [Ethics Training Agents: Facilitating Group-Based Ethics Education with Role-Playing and Discussion for Ethical Reflection and Exploration](https://arxiv.org/abs/2609.11529)

**<font color=#1a73e8>作者：</font>** Youngseok Seo, Sueun Jang, Hyesoo Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Group-based ethics training for Science, Technology, Engineering and Mathematics (STEM) students is a complex challenge, requiring substantial resources and expertise. While activity-based teaching methods, such as role-playing and discussions, are commonly employed to simulate real-world scenarios, current practices are often manual and lack integration with effective online platforms for supporting group-based ethical discussions. In this work, we propose Ethics Training Agents, a group discussion system that leverages multiple LLM participants embodying distinct ethical orientations, along with a moderator agent, to enable structured human-AI group ethical discussions for collaborative reflection. We conduct a user study with 45 undergraduate STEM students to evaluate the learning outcomes and user experience. The results show that our system supports engagement, coordination, and perspective-taking in group discussions and has a positive influence on ethical sensitivity. We also discuss practical design strategies for integrating multiple LLM agents into multi-human group settings to facilitate ethics training for STEM students.

---


### 108. [Prompt Revision as a Source of Cultural Bias in Text-to-Image Systems](https://arxiv.org/abs/2609.11532)

**<font color=#1a73e8>作者：</font>** Aleksandra Urman, Elsa Lichtenegger, Salima Jaoua 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Commercial text-to-image systems silently revise user prompts before generating images, a step users typically cannot disable or even see. Yet, existing audits of cultural bias examine only the final images and treat generation as a single pipeline, so they cannot tell where the bias originates. We introduce WORLDVIEW, a multilingual benchmark of 8,960 prompts across 15 languages and 31 language-context pairings. Using it, we audit the revision layer in three systems (DALL-E-3, Imagen-4, GPT-Image-1.5) through a three-step analysis of how heavily it marks each cultural context, whether it flattens that context into a narrow vocabulary, and whether that vocabulary is stereotypical. Relative to a no-context English baseline, the US is the least-marked context, while non-Western and non-Anglophone contexts are marked far more heavily, flattened into narrow vocabularies applied across topically diverse prompts, and reduced to recognizable cultural stereotypes. Comparing images from original versus revised prompts on models without a revision layer, we identify the layer itself as a previously undocumented, causal source of this stereotyping. To locate cultural bias, and fix it, we must audit the system as deployed, not the model alone.

---


### 109. [Characterizing Job Power Elasticity for Power-Flexible AI Training](https://arxiv.org/abs/2609.11542)

**<font color=#1a73e8>作者：</font>** Philip Colangelo, Charles Dawson, Shayan Sengupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) training is among the fastest-growing sources of electricity demand in modern data centers, and power availability is a primary bottleneck to continued AI infrastructure growth. Making the power consumption of these workloads flexible could unlock additional power for AI growth, limit increases in electricity prices, and improve the utilization of existing grid infrastructure. However, to realize this flexibility, we must first understand how the performance of training workloads changes when GPU power is reduced.
This paper presents the first systematic characterization of \emph{job power elasticity} (the sensitivity of throughput to power reductions) in LLM training. To quantify elasticity, we introduce the \emph{Power Flexibility Index (PFI)}, a normalized metric that quantifies the performance cost of power reductions and provides a control primitive for SLA-aware power flexibility.
We collect data from 131 LLM training runs on H200 (plus 24 H200 validation runs and 34 matched H100 runs), including both dense and mixture-of-experts models, pretraining and fine-tuning tasks, and up to 32 GPUs. We find that LLM training jobs exhibit substantial but variable power elasticity, and we identify telemetry signals that predict PFI at runtime. Finally, we demonstrate that PFI-aware power allocation maximizes total tokens/second throughput under power constraints. Under a 30\% power reduction, PFI-aware power allocation recovers ~1.5k tokens/s per job, 63\% of the performance gap between an equal-weight allocation and an oracle with perfect information. Our results establish power elasticity as a measurable property of training jobs and provide a foundation for power-aware, grid-responsive AI infrastructure.

---


### 110. [Enabling Knowledge Graph Understanding at Scale with the EXplore Your Graphs ENgine (EXYGEN)](https://arxiv.org/abs/2609.11569)

**<font color=#1a73e8>作者：</font>** Harshdeep Singh, Yurui Zhu, Giovanni Colavizza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present EXYGEN (EXplore Your Graphs ENgine), a framework for knowledge graph (KG) understanding that enables conversational access to KGs at scale. We address two questions in sequence. First, how effectively can LLMs perform text-to-SPARQL generation given only automatically derived structured metadata and small graph samples, rather than task-specific fine-tuning? We integrate VoID descriptions and ShEx schemas into a retrieval-augmented generation (RAG) pipeline and ablate KG-derived context on the SciQA benchmark. Our best configuration -- combining ShEx schemas, retrieved triples, and example question-query pairs -- reaches an exact match of 0.419 on execution results without any LLM fine-tuning. We further find that lexical metrics such as F1 poorly predict query correctness, and that larger general-purpose LLMs can outperform smaller code-specialized ones once given sufficient context. Second, we ask how to generate the structured metadata that this method relies on from very large KGs, where KG metadata generation becomes computationally intractable. We introduce a predicate-coverage-aware parallel graph sampling strategy that preserves structural diversity while remaining computationally tractable. On OpenCitations Meta and GESIS, it retains high predicate coverage with minimal triple loss and reduces runtime by over 80x; on ORKG, sampling is not just faster but the only tractable path to obtain complete metadata. Together, these results show that structured schema context and lightweight prompting can substantially reduce reliance on fine-tuning for scalable conversational access to KGs, though closing the remaining gap to fully fine-tuned approaches will likely require reducing dependence on curated question-query exemplars -- whether through synthetic generation or an execution-feedback-driven approach -- and validating these findings beyond a single benchmark.

---


### 111. [OmniKVQuant: KV Cache Quantization for Omni-LLMs](https://arxiv.org/abs/2609.11582)

**<font color=#1a73e8>作者：</font>** Suho Yoo, Hyunjong Ok, Jongmin Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As Omni-modal large language models (Omni-LLMs) take in audio, video and text together, their KV cache memory cost grows. KV cache quantization is the de facto approach in text-only LLMs, but its application to Omni-LLMs remains unexplored. In this paper, we analyze how TurboQuant, a representative rotation-based KV cache quantization method, behaves on multimodal caches and identify two critical issues: temporal key drift and heterogeneous value geometry. To address these, we propose OmniKVQuant, a training-free framework that (i) sets the key quantization range over each short window of the input stream; and (ii) rotates values separately per modality. On Qwen2.5-Omni and Qwen3-Omni, OmniKVQuant enables 2-bit KV caches while substantially preserving performance across seven audio-visual benchmarks. We further provide a fused Triton decode kernel that unpacks the 2-bit cache during attention, so no dense FP16 cache is ever built. Code: this https URL

---


### 112. [Making Alternative Data Work: Context-Augmented LLMs for Financial Forecasting](https://arxiv.org/abs/2609.11607)

**<font color=#1a73e8>作者：</font>** Jihoon Kwon, Lawrence Liu, Daekyung Park 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When forecasting a firm's future financial performance, alternative data - data collected from non-traditional sources such as consumer transactions, web traffic, and prediction markets - can provide timely signals about firms' operating activities and broader market conditions. These signals may reveal information that is not captured by traditional public sources and can therefore provide complementary information for forecasting firms' future financial performance. However, firm-level alternative data often have limited historical coverage, are relevant only to specific prediction targets or subsets of firms, and are distributed across numerous heterogeneous channels, making them difficult to incorporate flexibly into conventional forecasting approaches. Meanwhile, large language models (LLMs) can interpret instructions, learn from in-context examples, and generate predictions by combining heterogeneous information without task-specific parameter updates. Motivated by this potential flexibility, we investigate whether an LLM can forecast firm performance by integrating alternative data with other financial information through in-context learning. We propose a two-agent framework that first identifies the firms for which each alternative data channel is likely to be informative and then predicts revenue using firm- and channel-specific context. We evaluate the framework across four commercial alternative data channels. In our experiments, adding alternative data in context alongside other financial information improves the LLM's forecasting relative to either source alone, and these forecasts are more accurate than those of standard forecasting baselines. These findings suggest that LLMs provide a flexible and practical approach to integrating alternative data with heterogeneous financial information.

---


### 113. [A Training-Free, Alignment-Free Approach to Corporate Intelligence: Application to SEC Filings](https://arxiv.org/abs/2609.11620)

**<font color=#1a73e8>作者：</font>** Jean-François Delpech  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-dimensional dense text embeddings and large language models face real obstacles in financial-disclosure analysis: context-window limits, hallucination risk, high computational cost, and the arbitrary rotation of vector spaces across independently trained models. We present a training-free, alignment-free framework for corporate intelligence built on deterministic sparse seed vectors. Hashing word strings into a fixed high-dimensional basis places all documents and all temporal epochs in a common coordinate system by construction, removing any need for training or alignment. Accumulating these seed vectors across sentence contexts yields corpus-specific semantic signatures that compose linearly, supporting sub-second document comparison, issuer fingerprinting, tracking of how an issuer's vocabulary shifts between filings, and thematic sentence extraction, all on ordinary CPU hardware. Demonstrating the approach on a multi-year corpus of SEC filings (10-K, 10-Q, 8-K), we show how material corporate events, among them Boeing's 737 MAX crisis, Intel's supply-chain disruptions, and Bunge's acquisition of Viterra, emerge as distinct, interpretable semantic profiles, each traceable to the exact source sentences that produced it, with no domain-specific training and no LLM inference.

---


### 114. [MAPLE: Memory-Augmented Planning with Language and Evolution](https://arxiv.org/abs/2609.11636)

**<font color=#1a73e8>作者：</font>** Kesheng Chen, Yamin Hu, Wenjian Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Domain practitioners understand their business constraints but may lack operations-research expertise or dedicated support. LLM-based optimization agents translate natural-language requirements into models or solver programs that established optimization tools can execute. This progress makes optimization more accessible, but real-world operations are dynamic: changing demand, resources, and priorities require updates to data, constraints, and objectives. Methods centered on isolated requests offer limited support for rapid adaptation that preserves earlier decisions and reuses useful search results. We introduce MAPLE (Memory-Augmented Planning with Language and Evolution), an agent for maintaining optimization problems through successive natural-language requests. MAPLE combines language-based problem construction with mathematical programming and evolutionary search. It retains the optimization program, accepted plans, earlier updates, and candidate solutions for subsequent requests. We introduce NLDO, a benchmark of 15 trajectories and 180 updates spanning selection, scheduling, rostering, routing, and cloud-resource placement. In the main evaluation, MAPLE completes all trajectories and achieves online scalar quality of 0.951 and a Pareto hypervolume ratio of 0.875. Controlled comparisons further show that maintaining executable state improves update validity and can preserve useful search information across substantial revisions.

---


### 115. [Musec: MomentUm SpEctral Clipping for Stable Muon-type Training](https://arxiv.org/abs/2609.11655)

**<font color=#1a73e8>作者：</font>** Zhuanghua Liu, Menglian Wang, Luo Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has emerged as a highly effective optimizer for large language model training, often achieving superior convergence and performance compared with the widely adopted Adam and AdamW optimizers. Nevertheless, Muon is prone to training instability due to its spectral flattening, manifested by loss spikes and unbounded growth of model weights. Existing approaches primarily rely on weight or attention-logit clipping, which require architecture-specific modifications and do not directly address instability across all model components. We propose MomentUm SpEctral Clipping (Musec), which replaces Muon's spectral flattening with spectral clipping: rather than setting all singular values of the momentum matrix to approximately one, Musec clips singular values that exceed a threshold while preserving the underlying spectral structure of the momentum. Our strategy provides an optimizer-level, architecture-agnostic mechanism for stabilizing Muon training. We further develop Soft Musec, an efficient implementation that uses a smooth spectral saturation function approximated by coupled Newton-Schulz iterations. Theoretically, we establish convergence guarantees for Musec in nonconvex nonsmooth stochastic optimization. To the best of our knowledge, this is the first convergence guarantee for Muon-type methods in the nonconvex nonsmooth setting. We provide empirical studies to show that Soft Musec consistently improves training stability over existing Muon variants across a wide range of learning rates and model sizes. Notably, Soft Musec remains stable in settings where existing Muon variants diverge, while matching their performance under well-tuned configurations.

---


### 116. [Geospatial AI, Dataverse Metadata, and the Study of Place-Based Government](https://arxiv.org/abs/2609.11674)

**<font color=#1a73e8>作者：</font>** Danny EBanks, Devika Jain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harvard Dataverse hosts over 150,000 research datasets, but the geographic information those datasets carry is entered as free text by depositors and has never been assembled into a searchable structure. We construct a knowledge graph from the repository's public data and metadata, organizing 102,650 datasets within a 215,985-node network of 528,003 edges linking datasets to keywords, publications, subjects, journals, and locations. Of those datasets, 43,991 (42.9 percent) carry at least one geospatial field, geographic coverage, geographic unit, or a bounding box and 96.9 percent of all nodes sit in a single connected component, so datasets remain reachable from one another even when their geospatial metadata share nothing in common. A conservative keyword search identifies 7,654 geospatially tagged datasets (17.4 percent) as directly policy-relevant, with elections and legislatures the largest cluster, followed by government administration, health policy, transportation, and education. Five datasets illustrate how this metadata behaves across policy domains and spatial scales, and an extended use case shows how community language models, stance detection with geographic aggregation, and partisan language bridging tools can attach discourse to place. The central obstacle is place resolution: the same location appears as many disconnected nodes. We argue that the graph provides a concrete setting for developing AI-driven metadata enrichment and entity resolution, and we document its coverage skew toward American, city-level data.

---


### 117. [COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization](https://arxiv.org/abs/2609.11682)

**<font color=#1a73e8>作者：</font>** Pingchen Lu, Xiangyi Wang, Xiang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can benefit from reusable skills distilled from prior task experience, yet existing skill optimization methods often rely on costly execution-based evaluation and substantial task data. We introduce \textbf{COBRA-Skills}, an efficient framework that formulates skill optimization as budgeted sequential optimization over a dynamically evolving candidate space. COBRA-Skills couples contextual-bandit-guided prioritization with evidence-grounded skill evolution, selectively allocating evaluations to promising or informative candidates while continually refining the skill population from execution feedback. Across six heterogeneous agent benchmarks and three target models, COBRA-Skills consistently achieves the strongest average performance among compared methods, while reducing optimization cost by 55--58\% relative to SkillOpt and using only 50 unique optimization examples per benchmark. Further analyses show that COBRA-Skills remains robust to changes in the agent harness and performs effectively when the target model itself is used for skill generation and refinement.

---


### 118. [Structured Transforms for Low-Overhead Quantization of Language Models](https://arxiv.org/abs/2609.11687)

**<font color=#1a73e8>作者：</font>** Daria Cherniuk, Alexander Rudikov, Boris Kashin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We revisit Kashin-decomposition-based weight quantization for large language models and propose an improved algorithm with stronger convergence properties and structured, efficient orthogonal transforms. The method retains the core factorization of each weight into two components -- one with bounded infinity norm and the other with bounded infinity norm after an orthogonal transformation -- but replaces the dense random orthogonal matrix with a sign-randomized Discrete Cosine Transform (DCT), reducing the per-iteration cost from $\mathcal{O}(N^2)$ to $\mathcal{O}(N \log N)$. The proposed greedy algorithm with alternating updates guarantees the four-peak distribution required for stable 2-bit clustering of each factor and admits closed-form initialization of cluster centers, removing the multi-restart k-means bottleneck of prior work. Composed with OPTQ-style sequential error compensation and QuIP-style incoherence preprocessing, the resulting JAX pipeline is competitive with OPTQ, QuIP, QuIP-RG and a fine-tuning- and vector-quantization-free variant of QuIP# at 4-bit per channel on OPT, Llama-2 and Pythia, with favorable wall-clock scaling. The bounded-$\ell_\infty$ factorization is also notably robust: on stress configurations where QuIP variants diverge to four-digit perplexity (Pythia-6.9B) or abort with NaNs in LDL back-substitution (Mistral-7B), Kashin-DCT remains numerically stable and stays close to FP16 baseline. At inference time, each weight decomposes into two 2-bit factor codes per channel that are structurally suited to native-2-bit hardware.

---


### 119. [Negative Self-Distillation: Learning to Reason by Avoiding Flaws](https://arxiv.org/abs/2609.11699)

**<font color=#1a73e8>作者：</font>** Rongcan Pei, Zhepei Wei, Shuyao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-Policy Self-Distillation (OPSD) has emerged as a popular paradigm for large language model (LLM) self-improvement, allowing models to act as their own teachers by leveraging privileged information such as ground-truth solutions. However, recent findings indicate that OPSD can severely degrade the performance of LLMs on complex reasoning tasks: By forcing the student to imitate an artificially confident reasoning trace conditioned on privileged information, OPSD inadvertently suppresses expressions of uncertainty and penalizes the exploratory, self-corrective behaviors required to solve challenging problems. To address this, we introduce Negative Self-Distillation (NSD), a new framework that optimizes LLMs by diverging from flawed reasoning rather than imitating privileged solutions. Instead of relying on ground-truth answers or external supervision, NSD uses the model itself to generate a question-specific negative condition (eg, acting as a ``careless reasoner'') and pushes the student's distribution away from this self-generated negative teacher. Naively applying unlearning objectives to achieve this divergence is problematic, as flawed reasoning tokens are confounded with basic linguistic tokens; indiscriminately penalizing both risks catastrophically degrading the model's foundational language capabilities. We resolve this by designing a dynamic gating mechanism that automatically identifies and isolates reasoning-critical tokens, ensuring gradient updates target only behavioral flaws while preserving the model's linguistic priors. Empirically, NSD consistently outperforms OPSD and other label-free, self-bootstrapping reinforcement learning (RL) baselines.

---


### 120. [Language-Augmented Semantic Priors for B-Spline Surface Fitting](https://arxiv.org/abs/2609.11708)

**<font color=#1a73e8>作者：</font>** Yunzhong Lou, Yusheng Luo, Jiahao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The use of B-splines and Non-Uniform Rational B-Splines surfaces constitutes the mathematical foundation of contemporary computer-aided design (CAD) systems. Despite long-term progress, geometric kernels in traditional CAD still rely heavily on predetermined heuristic initialization for surface fitting and parameterization. Meanwhile, the procedural semantics and design intent encoded in modeling histories are largely ignored during geometry generation. This disconnect creates a gap between high-level design intent and solver-executable geometric configuration, often leading to suboptimal and semantically inconsistent fitting results. To bridge this gap, we introduce LASP, a Language-Augmented Semantic Priors framework that leverages large language models (LLMs) to infer structured, solver-usable B-spline priors from procedural modeling histories. Rather than modifying the geometric kernel itself, LASP operates as a semantic reasoning layer above existing solvers. It first translates modeling histories into rich textual descriptions that capture design intent, geometric context, and functional relationships, and then uses a fine-tuned LLM to predict structured B-spline prior parameters. LASP is trained through a two-stage scheme that combines local geometric regularities with long-range contextual dependencies, producing priors that are both interpretable and semantically coherent. This approach furnishes inductive signals that direct the conventional B-spline fitting process toward solutions that more accurately encapsulate the intended design objectives and demonstrate heightened semantic coherence. Compared to traditional machine learning schemes, the experiments demonstrate that language-driven reasoning can serve as a powerful inductive bias for geometric solving, establishing a new paradigm of language-guided geometric optimization in modern CAD systems.

---


### 121. [When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for Multi-Agent Collective Decision-Making](https://arxiv.org/abs/2609.11709)

**<font color=#1a73e8>作者：</font>** Ken Chen, Wei Wang, Sachith Seneviratne 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When multiple LLM agents yield conflicting answers, the decision-making process dictates whether agent diversity improves performance or merely compounds shared errors. Existing collective decision-making methods, including voting, electoral rules, and LLM judges, rely on forward reasoning: they map evidence to labels in one direction. Although these methods can combine diverse forward traces, they still aggregate estimates that share this evidence-to-label factorization and can inherit correlated errors within the forward pool. We therefore construct a reverse posterior for each instance through Bayesian backward reasoning from an explicit likelihood. The forward and reverse posteriors provide differently factorized approximations of the underlying posterior. Because estimates from different factorizations may tend to share the same error less often, we use Jensen-Shannon divergence to rank agents by cross-path consistency. This cross-path consistency signal underlies three strategies: hard selection (MinJS), soft reweighting (FwdJS), and log-linear fusion (LogLin). Evaluated on DDXPlus across five LLM backbones, our proposed strategies show consistent improvements: MinJS outperforms random selection across all backbones, FwdJS generally improves over the strongest baseline, and LogLin achieves the best performance among the evaluated methods, with its largest gains on the subset where the agents disagree. Despite its weaker standalone accuracy, the reverse posterior serves as a more useful anchor than forward-only alternatives, providing complementary information for collective decision-making. When labeled data are available, a lightweight two-stage calibration can further refine the reverse anchor and improve aggregation performance.

---


### 122. [Why Does Post-Training Quantization Work?](https://arxiv.org/abs/2609.11716)

**<font color=#1a73e8>作者：</font>** Yuxiang Chen, Michael Beyer, Jun Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization compresses large language models (LLMs) by storing their weights at reduced precision, and each quantized weight introduces an error into the hidden states. Naively, these errors should accumulate with depth and corrupt next-token prediction; randomly initialized models accumulate these discrepancies rapidly, whereas quantized pretrained models accumulate much less hidden-state error and largely maintain downstream task performance, even though they were never trained with quantization noise. This raises the question we address: why does post-training quantization work? Comparing full-precision and quantized forward passes, we identify two mechanisms that characterize pretrained quantization robustness. First, the error a layer newly introduces tends to oppose the error it inherits from the layer's input. The two cancel partially such that the discrepancy between full-precision and quantized passes grows slowly. This counteracting residual interaction develops during pretraining. Our quantitative analysis identifies it as a major factor slowing hidden-error growth. Second, LM-head geometry preferentially preserves the scores and probabilities of high-ranked tokens, which typically represent the model's most confident predictions. Together, these mechanisms explain why quantization error that passes through numerous layers can still produce only small output changes, and we verify the findings across models and quantization settings.

---


### 123. [The Eloquence submission for Task 2 of the Interspeech 2026 MLC-SLM challenge](https://arxiv.org/abs/2609.11724)

**<font color=#1a73e8>作者：</font>** Jordi Luque, Lorenzo Concina, Marco Matassoni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper details the Eloquence team's approach to Task 2 of the 2nd MLC-SLM challenge at Interspeech 2026, which involves multilingual Multiple-Choice Question Answering (MCQA) across 21 languages. Three approaches are explored. First, we fine-tune Voxtral-Mini-3B via LoRA with cross-lingual data augmentation, ASR transcript augmentation and timestamp-aware audio cropping, achieving 0.72 macro-accuracy on evaluation Phase 2. Second, we apply multimodal in-context learning (ICL) to the frozen Voxtral-24B model to correct a strong label bias, reaching 0.81, our best result. Third, a training-free retrieval system based on a three-layer voice-anchored memory combining acoustic identity, semantic content, and a knowledge graph achieves 0.68. All three systems substantially outperform the official baseline.

---


### 124. [ORCH: Organizational Principles Enable Collective Intelligence in Embodied AI](https://arxiv.org/abs/2609.11737)

**<font color=#1a73e8>作者：</font>** Zhengran Ji, Jonathan Hyun, Boyuan Chen  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Collective intelligence depends not only on the capabilities of individual members, but also on how those members are organized. Yet artificial multi-agent systems are typically assembled using fixed organizational structures, even when the physical tasks they perform impose fundamentally different coordination requirements. Here we show that principles from human organization theory can be operationalized to organize large, heterogeneous collectives of embodied artificial agents. We introduce ORCH (Organizing Roles and Coordination Hierarchies), which constructs task-specific hierarchical organizations by combining pooled interdependence for work that can proceed concurrently with sequential interdependence for work governed by prerequisite relationships. Across 25 wildfire-response missions spanning reconnaissance, rescue, transportation, resource management, containment and suppression, we evaluated teams of up to 50 heterogeneous agents using eight large language models. Organizations constructed using these principles consistently outperformed four representative embodied multi-agent approaches across mission outcome, execution efficiency, exploration and computational resource use. Human-designed ORCH organizations improved final score by 63.97% and execution efficiency by 74.29% on average relative to the four prior frameworks. Organizations generated automatically by language models improved these measures by 43.63% and 52.53%, respectively. These advantages persisted across missions and underlying language models. Notably, collective performance was not monotonically determined by model scale. Analysis of long-horizon missions showed that hierarchical organization enabled teams to preserve concurrent activity within specialized groups while coordinating ordered transitions between mission phases.

---


### 125. [LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation](https://arxiv.org/abs/2609.11739)

**<font color=#1a73e8>作者：</font>** Dongfang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model serving costs scale directly with output sequence length, yet standard preference alignment often inflates response verbosity without improving utility. We study whether the parameterization of post-training updates affects generation length: low-rank subspaces alter sequence length without modifying the alignment loss. We present LOCUS, a method that selects a task-aware low-rank adaptation subspace to minimize output-token cost subject to a utility constraint. Within this subspace, post-training retains the native preference objective with a frozen backbone. Across Anthropic HH-RLHF dialogue preferences, we evaluate two $\sim$3B decoder backbones, Pythia-2.8B and Qwen2.5-3B, against protocol-matched full-parameter DPO and DrDPO branches and the released SamPO checkpoint. LOCUS reduces continuation length by up to 39.84\% on Pythia-2.8B and by 14.87--17.58\% on Qwen2.5-3B while updating only 0.24--0.28\% of model parameters, with no material change in the internal preference diagnostic.

---


### 126. [SIRF: A Spec-Internalized Risk Foundation Model for Industrial Content Risk Control](https://arxiv.org/abs/2609.11752)

**<font color=#1a73e8>作者：</font>** Suwan Wu, Yumeng Lin, Pengcheng Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For industrial content risk control, the real deployment constraint is not average accuracy but how much risk can be auto-handled under high precision and second-level latency. We present SIRF (Spec-Internalized Risk Foundation Model), which internalizes a platform's complex policies, synthesized without additional human annotation via EntiGraph, MAGA rewriting and account-level chain-of-thought (CoT), into the weights via continued pretraining (CPT), so rules are applied at high precision under an ultra-low-latency, verdict-only deployment. A controlled same-source comparison (Qwen3-8B-SFT vs. SIRF-8B-SFT, identical policy injection and verdict-only output form, differing only in policy-grounded CPT) attributes the gain to internalization: SIRF-8B-SFT reaches 71.3% Black Recall@P95, +15.1pp over the baseline, using only ~70M CPT tokens without harming general ability, and among included, logprob-available models under this interface it matches or exceeds far larger systems. SIRF is deployed as a tree-model adjudication layer (20% more mis-penalized samples recovered) and transfers to a freezing scenario at low cost (~70% relative mis-penalization reduction).

---


### 127. [Signing the Transaction but Not the Decision: Whisper Attacks and a Binding Defense for AP2](https://arxiv.org/abs/2609.11757)

**<font color=#1a73e8>作者：</font>** Yedidel Louck, Amit Dvir, Ariel Stulman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software agents are beginning to shop and pay on a person's behalf. Agent payment protocols such as AP2 produce cryptographically valid signatures for completed purchases, yet do not constrain the decisions that lead to them. Consequently, ordinary product-description text can steer a shopping agent into forming a cart that passes every protocol check but no longer matches the user's request. In this paper, we show that this vulnerability enables three related attacks. In the first attack, the agent is steered into fetching another user's payment credentials. In the second, it assembles a cryptographically valid cart whose contents do not match what the user was shown. In the third, a single factual claim about stock or product lineage moves the agent from the cheaper displayed item to a more expensive one, while the resulting cart remains fully consistent with the listing. In experiments using the Gemini Flash-Lite models that AP2's sample agents specify by default, the three attacks succeeded at rates of 90%, 56%, and 73.3%, respectively. The same vulnerability appears across seventeen Google models, three unrelated agent frameworks, two cross-vendor anchors, and Google's own consumer assistant. To address this attack vector, we introduce A-VIP (AP2 Verified-Intent Protection), a protocol-layer defense that treats the signed intent as a capability grant rather than judging the merchant's description. The defense binds every credential lookup to the session that requested it and every cart line to the listing seen, while flagging unauthorized spending. The first two attacks leave structural traces that these bindings block with zero false positives. The third attack leaves no trace, so A-VIP surfaces unauthorized spending for user confirmation. Finally, we release the A-VIP code, machine-checked invariants, and AP2-WhisperBench, a suite of 1,544 evaluation scenarios.

---


### 128. [Component-Aware Differential Privacy for Federated Multilingual Speech-LLMs](https://arxiv.org/abs/2609.11762)

**<font color=#1a73e8>作者：</font>** Jordi Luque, Fernando López, Aleix Sant  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Per-layer differential privacy (DP) clipping improves gradient fidelity in federated learning by allocating per-matrix clipping budgets proportional to parameter count. We show that this recipe breaks for speech large language models (speech-LLMs), when the acoustic encoder and the language decoder differ by an order of magnitude in update norm. Single-pool per-layer methods suffer \emph{cross-component budget collapse}, dragging word error rate (WER) far from flat global clipping or collapsing training entirely. When the norm imbalance is milder, adaptive single-pool methods partially recover, confirming that collapse severity scales with the inter-component norm ratio. We empirically diagnose the root cause across six per-layer methods and three speech-LLM architectures. We then propose \emph{$\alpha$-split}, a two-pool allocation that normalises encoder and LLM parameters into independent pools, and show that joint $\ell_2$ sensitivity and the original $(\varepsilon,\delta)$-DP guarantee are unchanged. At architecture-calibrated $\alpha$, our method recovers WER utility compared to flat DP, while granting the encoder $4.47{\times}$ tighter per-component noise protection against speaker voice-based gradient-inversion attacks at only $+2.6\%$ LLM noise overhead.

---


### 129. [A Unified Per-Token Gating Family for On-Policy Distillation: FKL/RKL Mixing with Multi-Channel and Bias Coefficients](https://arxiv.org/abs/2609.11768)

**<font color=#1a73e8>作者：</font>** Suwan Wu, Yumeng Lin, Pengcheng Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Per-token gating of forward/reverse KL losses has become a standard technique for on-policy knowledge distillation (OPD), but existing methods such as EOPD (Jin et al., 2026) and ToDi (Jung et al., 2025) each fix a single gating signal and a single gating direction, and the two have never been compared directly. We introduce a four-coefficient parameterization lambda_t = sigma(a * h_t + b * u(x) + c + d * gap_t) in which direction-aligned proxies of EOPD and ToDi appear as one-dimensional (1D) restrictions, and which adds multi-channel composition and an explicit bias as further degrees of freedom. On TweetEval (Barbieri et al., 2020) emotion and hate, with a Qwen3-32B teacher and a Qwen3-4B student, configurations in the full family reach higher accuracy than the matched-magnitude single-channel (entropy-only / gap-only) 1D restrictions in 33 of 36 comparable cells, and a 26-cell mean-match isolation experiment places dynamic gating ahead of effective-KL-matched static baselines in 19 of 26 cells. Because cells share training data, models, and parameter substructure, we report both counts as exploratory aggregate directional evidence rather than as independent hypothesis tests. Targeted three-seed paired replications of the nine headline comparisons singled out by that sweep -- including a third task, offensive -- are directionally consistent, but individually smaller than the single-seed estimates and not significant at n=3. We therefore present the parameterization primarily as a shared coordinate system for comparing per-token gating designs in short-output classification OPD.

---


### 130. [Recognizing Is Not Reversing: A Controlled Inversion Test of Fact-Preserving News Framing](https://arxiv.org/abs/2609.11769)

**<font color=#1a73e8>作者：</font>** Yi Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to analyze and rewrite news, yet current framing studies mainly evaluate generation, detection, or whether rewritten text appears more neutral. They do not directly show whether a model can undo a known framing transformation while keeping the facts fixed. We introduce a controlled inversion test over three established textual realizations of framing: evaluative lexis, agency realization, and information salience. Across 60 news articles and three intervention strengths, this yields 540 paired variants with preserved atomic facts and recorded edits. Across Qwen, DeepSeek, and Kimi, factual preservation remains near 0.84, whereas intervention reversal is 0.044--0.068. Even when both framing type and direction are recognized correctly, pooled reversal reaches 0.071. These results reveal a clear separation between factual fidelity, framing recognition, and framing inversion: recognizing how an article is framed does not imply that the framing can be undone.

---


### 131. [The widening evaluation gap in medical large language model research 2023 to 2026](https://arxiv.org/abs/2609.11770)

**<font color=#1a73e8>作者：</font>** Raad Bin Tareaf, Murad Al-Rajab, Samia Loucif  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are superseded every few quarters; clinical evidence takes years. We asked whether medical research is keeping pace with the systems it evaluates. PubMed returned 11,628 records for January 2023 to June 2026 across fourteen clinical domains, growing 45-fold; 2.5% used a randomised, controlled or prospective design. Evaluation lag, from a study's newest named model release to its own publication, widened from 1.33 to 6.08 quarters. Because discontinued models age mechanically, we benchmarked this against a counterfactual holding model composition fixed: migration to newer systems offset only 56% of the drift (95% CI 50-65). Randomised trials evaluated models a median 4.6 quarters older than other designs (P = 3 x 10^-19), yet among studies naming a model still under development no design differed from any other; 62% of randomised trials evaluated a discontinued family. Rigour and currency are in tension, and that tension reflects model selection rather than research timelines.

---


### 132. [Beyond Word Error Rate: A Switch Aware Evaluation of ASR and Audio Language Models on English Yoruba Code-Switched Speech](https://arxiv.org/abs/2609.11786)

**<font color=#1a73e8>作者：</font>** Chibuzor Okocha, Christan Earl Grant  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems and audio language models (audio LMs) now report low error rates on monolingual benchmarks, but their behavior on code switched speech in low resource, diacritic rich languages remains poorly characterized. We present a switch aware evaluation of eleven modern systems (six ASR models and five audio LMs) on English Yoruba code-switched speech, using a deterministic 2000 utterance evaluation set and a shared scoring pipeline. Beyond word error rate (WER), we report switch localized diagnostics: a switch entry token error rate (SETER), windowed switch point error rates, language specific error rates, and a diacritic insensitive WER. Our central finding is that aggregate WER hides code switching behavior. The best system by WER (an ASR model) is statistically indistinguishable from a leading audio LM on WER, yet the audio LM is significantly better on every switch localized metric. Across faithful systems, Yoruba token recognition collapses (error 0.97 for almost all systems) while English tokens are recognized far better, and errors concentrate sharply at switches into Yoruba. Several generative audio LMs fail as exact transcribers, producing translation, verbosity, and prompt leakage that are strongly prompt dependent. We release manifests, metric implementations, and evaluation scripts to support reproducible, switch aware benchmarking for African code switched speech.

---


### 133. [Dynamic language model representations for multi-objective reaction optimisation](https://arxiv.org/abs/2609.11790)

**<font color=#1a73e8>作者：</font>** Joshua W. Sin, David Ming Segura, Bojana Ranković 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimising chemical reactions across multiple objectives, such as yield, selectivity, and safety, is central to chemical synthesis, and model-driven approaches depend critically on how reaction components are represented. Established featurisations are either chemically uninformative, as with one-hot encodings, or, as with molecular descriptors, do not readily extend across chemically distinct components. For structurally and functionally diverse components, it is therefore unclear what a shared representation should contain. Constructing such a representation is itself a challenging research undertaking that must be revisited for each new reaction system. Here we bypass this step by learning the reaction representation dynamically from text. Textual descriptions of reaction conditions are encoded by a fine-tuned language model trained jointly with Gaussian process surrogates, yielding task-adaptive representations within a multi-objective Bayesian optimisation loop. Across nickel- and palladium-catalysed cross-couplings in both sequential and parallel experimentation regimes, this approach reaches optimisation convergence in fewer experiments than descriptor libraries or one-hot encoding. Applied prospectively to a palladium-catalysed cyanation spanning mixed ligand denticity and heterogeneous additives, and to a three-objective asymmetric hydrogenation across chiral iridium and ruthenium catalyst families, two rounds of high-throughput experimentation (192 reactions, under 3% of each design space) delivered conditions translating directly to gram scale in 94% and 84% isolated yield, the latter at 99.6% enantiomeric excess.

---


### 134. [Atlas: Efficient Verifiable Semantic Search](https://arxiv.org/abs/2609.11841)

**<font color=#1a73e8>作者：</font>** Nikolay Avramov, Hidde Lycklama, Alexander Viand 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Semantic search is a core primitive of modern applications, powering recommender systems, web search, and retrieval-augmented generation for language models. The provider controls the index and query execution, leaving clients to trust that results come from the right algorithm over the intended index. A provider may truncate search to cut cost, bias results, or otherwise deviate from the specified execution undetected. Verifiability can remove this trust assumption by proving that results follow the agreed algorithm over a committed index. Realizing this efficiently is hard, as retrieval at scale relies on HNSW, a graph-based algorithm whose data-dependent traversal maps poorly onto the fixed constraint systems of zero-knowledge proofs. Prior verifiable systems therefore target regular, cluster-based indices that are easier to encode, sacrificing the recall of graph-based search. We present Atlas, a system that lets a provider prove a query was answered correctly against its committed index without revealing the index. At its core is a new zero-knowledge proof for HNSW search, built on three techniques: preprocessing that shifts all database-dependent cost offline, so per-query proving scales with the traversal rather than the database; a restructuring of HNSW into a fixed-size-state procedure that we prove returns the same result; and a timestep-tagged batching that merges the per-step arguments of the entire traversal into one. Atlas is the first to demonstrate verifiable graph-based search at scale, proving a query in under a second on the SIFT1M benchmark and in 2.0 seconds at 100 million vectors, while maintaining the recall of plaintext HNSW and revealing nothing about the index beyond the result. In a complete RAG pipeline, Atlas' proven retrieval preserves end-to-end answer quality, and reaches higher quality at lower proving cost than all prior verifiable retrieval systems.

---


### 135. [BlueSTAR: Tiered Agentic Architecture for Autonomous Cyber Defense](https://arxiv.org/abs/2609.11852)

**<font color=#1a73e8>作者：</font>** Simona Boboila, Xavier Cadet, Edward Koh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber attacks are increasingly automated, narrowing the time available for human analysts to detect, reason about, and respond to intrusions. Large language models (LLMs) offer a promising foundation for autonomous cyber defense because they can correlate heterogeneous evidence and reason about previously unseen threats. However, directly applying LLMs to operational security telemetry is impractical: raw logs arrive faster than current models can process them, individual events are often ambiguous, and unconstrained LLM actions can introduce significant operational risk. We present BlueSTAR, a tiered agentic architecture for autonomous cyber defense in enterprise IT/OT networks. BlueSTAR first transforms high-volume security telemetry into compact indicators of compromise. We further introduce a resilience metric that jointly captures attacker reach, impact on mission-critical assets, and disruption caused by defensive actions. We evaluate BlueSTAR on two live enterprise IT/OT cyber ranges using seven attack chains based on real-world intrusion techniques. Across attack chains, BlueSTAR retains the fast containment of deterministic response for known threats while successfully defending against attacks requiring contextual and cross-cycle reasoning, including credential theft, repeated compromise, concurrent attackers, and attacks against physical processes.

---


### 136. [From Parameters to Answers: How LLMs Retrieve and Use Their Internal Knowledge](https://arxiv.org/abs/2609.11859)

**<font color=#1a73e8>作者：</font>** Wenkang Wei, Yuan Fang, Renhe Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How does a language model's dependence on query-routing information and target knowledge change as it answers a question? We study this question through layerwise interventions on the hidden state at the end of the question. Across Qwen, Llama, and Gemma, we compare country-continent questions with noun, adjective, and code answers while keeping several fitted measurements distinct. A pair-conditioned request direction describes which country is queried in natural single-country questions; a global request direction describes first- versus second-country requests in paired questions; separate selection candidates test control among contents already available in the hidden state. A diagnostic reanalysis of frozen Qwen natural-question states shows that the pair-conditioned direction grows stronger before interventions on it begin to alter later fitted knowledge, with this causal window opening while answer-supporting content is still forming. The paired three-model trajectories are not uniform: Gemma shows a partially overlapping mid-layer routing-content profile, whereas Llama has no sustained routing-effect window under the same gates. In the paired protocol, dependence on the global request direction decreases from fixed earlier to later layer sets while dependence on fitted content persists. A matched Qwen comparison shows that the pair-conditioned direction retains a late effect, so this operational handoff concerns the global fitted direction rather than all request information. These results separate early readability, natural strength, causal steering, and later content dependence.

---


### 137. [Explainability Assistant: A Conversational XAI Interface for Interpreting Energy Consumption Models](https://arxiv.org/abs/2609.11860)

**<font color=#1a73e8>作者：</font>** Rodion Krjutškov, Eduard Barbu, Nikos Sakkas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Energy consumption forecasting relies on increasingly complex machine learning (ML) models, such as Genetic Programming-based symbolic regressors, whose predictions can be difficult for facility managers and building operators to interpret. Explainable Artificial Intelligence (XAI) techniques address this opacity, but traditional XAI dashboards require substantial technical expertise and provide limited flexibility for dynamic, context-aware inquiry. Conversational XAI systems offer a promising alternative; however, previous approaches, such as TalkToModel, were constrained by rigid custom grammars and achieved only 76.8% intent-parsing accuracy. This paper introduces the Explainability Assistant, an open-source conversational XAI system that leverages the function-calling capabilities of modern Large Language Models (LLMs) to overcome these limitations. The system achieves 94% intent-parsing accuracy, supports flexible natural language interaction, and adapts to different ML problem types without task-specific fine-tuning. We present the system's architecture and report results from a comparative evaluation conducted with energy domain specialists, contrasting the Explainability Assistant with a traditional XAI dashboard. The evaluation suggests improved usability and consistent task accuracy, with all experts unanimously preferring the conversational interface for practical use.

---


### 138. [Augustinian BabyLM: What Ostensive Definition Can and Cannot Teach a Small Language Model](https://arxiv.org/abs/2609.11870)

**<font color=#1a73e8>作者：</font>** Lisa Bylinina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model normally begins training with random word embeddings: whatever 'banana' means must be learned from training corpora. I implement St. Augustine's picture of word learning, meaning by ostension, for a small masked language model (DeBERTa) trained on 10M words: before training, visually grounded tokens receive embeddings derived from the image regions they label; other tokens start random. Visual initialization leaves a measurable imprint that lasts until the end of training. At the same time, the effect remains invisible under most BabyLM benchmarks, which probe abstract grammatical knowledge: visual initialization does not affect performance there. The only zero-shot exception is object-property knowledge (COMPS, Misra et al. 2023), where seeding helps in every configuration. To follow up on this result, I build a corpus-tailored version of the Visual-Property Swap benchmark (Lin et al., 2026), which tests color, material, size, and shape knowledge, with per-item training frequency and seeded status. Here, vision-seeded models have a persistent, seed- replicated advantage, confined to the seeded words. As a causal test, I show that synthetic grounding of previously unseeded words transfers the advantage to exactly those words. Function words and abstract vocabulary also receive strong visual seeds and retain them throughout training, and the training objective draws on them: held-out mask-prediction loss falls for these words in every seed. However, no benchmark I run registers this. What evaluation would pick this up remains an open question.

---


### 139. [The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement](https://arxiv.org/abs/2609.11873)

**<font color=#1a73e8>作者：</font>** Yi Duan, Ying Liu, Zirui Tang 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) enables AI systems to turn experience and feedback into persistent changes that improve both their capabilities and the process of future improvement. We first use the Headroom-Closed Index (HCI) to reveal the problems of existing LLMs, then introduce the RSI concept and its development roadmap: from improvement-execution autonomy, improvement-strategy autonomy, experience-acquisition autonomy, and environment-adaptation autonomy, to recursive meta-improvement. Next we examine RSI across scenarios (e.g., scientific discovery, embodied intelligence, software engineering), highlighting their distinct requirements and development speeds. Drawing on diverse industry practices and preliminary empirical evidence, we connect RSI research with practical systems and identify key challenges to achieving genuine RSI.

---


### 140. [Domain-Specific Hallucination Detection in Large Language Models](https://arxiv.org/abs/2609.11878)

**<font color=#1a73e8>作者：</font>** Varun Teja Chundru, Debasmita Biswas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models generate fluent text that can contain unfaithful claims -- a phenomenon known as hallucination. We present a multi-signal detection pipeline combining fine-tuned DeBERTa-v3 classification, Monte Carlo (MC) Dropout uncertainty quantification, and temperature-scaled calibration for response-level hallucination detection. Evaluated on the HaluEval benchmark, our pipeline achieves F1=0.915 and AUROC=0.977 on general-domain tasks, with per-task F1 scores of 0.97 (QA), 0.96 (Summarization), and 0.82 (Dialogue). MC Dropout inference further improves accuracy to 93.2%. A context ablation study confirms the model performs genuine entailment reasoning rather than exploiting surface patterns, with summarization F1 dropping 24% when knowledge context is removed. Learning curve analysis reveals that 25% of training data captures 77% of full-data performance. Beyond detection, we apply Direct Preference Optimization (DPO) to a Qwen2.5-0.5B generator, reducing its hallucination rate from 85.5% to 37.7% (55.9% relative reduction) as measured by our detector. Cross-domain evaluation on the SciFact biomedical benchmark shows that general-domain training transfers poorly (F1=0.52), motivating domain-specific fine-tuning. PubMedBERT fine-tuned on SciFact achieves F1=0.63 and AUROC=0.81, demonstrating that domain-matched pre-training is the strongest adaptation strategy. Code and models are available at this https URL

---


### 141. [Nuha-Speech: Building General-Purpose Arabic Speech-LLMs](https://arxiv.org/abs/2609.11892)

**<font color=#1a73e8>作者：</font>** Yingzhi Wang, Reem Alhazzani, Muhammad Alqurishi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Speech Large Language Models (speech-LLMs) become increasingly multilingual, Arabic remains significantly underrepresented, highlighting the need for dedicated infrastructure to train and evaluate Arabic speech-LLMs.
To address this gap, we introduce Nuha-Speech, a comprehensive initiative to develop general-purpose Arabic speech-LLMs spanning dataset construction, model training, and systematic evaluation. Specifically, we constructed a large-scale Arabic Speech Question-Answering (SQA) corpus comprising over 1.5 million training samples to allow instruction tuning over a broad range of core speech tasks. Then, the corpus was used for supervised fine-tuning based on Qwen-Omni model variants at different scales. Finally, we designed an evaluation framework featuring diverse tasks and tailored metrics. Through this work, we aim to establish foundational infrastructures for Arabic Speech-LLMs under constraints imposed by limited Arabic speech resources.

---


### 142. [Caption-once, Frames-on-Demand: Visual-Need Routing for Budget-Aware Agentic Long Video Understanding](https://arxiv.org/abs/2609.11899)

**<font color=#1a73e8>作者：</font>** Weitong Cai, Hang Zhang, Yukai Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video understanding on edge devices must reason over hours of content under tight compute and bandwidth budgets. Subsampling visual tokens loses temporal structure, while text-only video memories lose fine-grained visual attributes. We observe a visual-textual duality: language memories carry long-range temporal structure better than dense frames, while pixels remain decisive for attribute-level perception. Building on this insight, we propose Caption-once, Frames-onDemand (CFD), a budget-aware edge-cloud agentic framework. The edge runs a single offline captioning pass that builds a dual-track narrative index, an event-level story skeleton plus a clip-level micro-log, cached and reused across queries without re-captioning. At query time, a cloud-side MLLM reasons over the index in a story-first loop centered on a lightweight Visual-Need Router: a per-query gating module that triggers bounded keyframe retrieval only for perceptual questions (appearance, on-screen text, attribute disambiguation) and keeps temporal-structural questions in language space. The router turns visual access into a first-class, query-conditioned cost, capping per-query frame consumption regardless of video length. Experiments on long-video benchmarks demonstrate strong accuracy-efficiency trade-offs while substantially reducing online visual processing.

---


### 143. [MindTopo: Can Foundation Models Reason in Topological Space?](https://arxiv.org/abs/2609.11900)

**<font color=#1a73e8>作者：</font>** Yunfei Ge, Anbang Liu, Qineng Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant under continuous deformation. Cognitive science identifies these relations as foundational to spatial understanding, yet foundation-model evaluations largely focus on metric or viewpoint-dependent relations. We introduce MindTopo, a benchmark of topological intuition across five properties grounded in cognitive science and formal topology: continuity, separation, order, enclosure, and knots. MindTopo evaluates each property at two cognitive levels. Reasoning asks a model to identify topological relations or infer how they change. Planning instantiates a foundation model as a closed-loop agent whose policy selects environment actions. MindTopo contains 11,030 instances across 13 procedurally generated task types with controllable difficulty. We benchmark 14 MLLMs and study agent configurations augmented with image and video generation, including 3 video generative models in planning settings. Every MLLM performs better on reasoning than on planning, and the best-performing model remains far below observed human performance. On Qwen3-VL-2B-Instruct, supervised fine-tuning and reinforcement learning improve reasoning more than planning. Generated observations retain local cues and reach plausible endpoints, but audited rollouts do not reliably follow environment dynamics or preserve topology across transitions. Our website is at this https URL

---


### 144. [Can Edge-Deployable Vision-Language Models Identify Species?](https://arxiv.org/abs/2609.11916)

**<font color=#1a73e8>作者：</font>** William Zhou, Mayukha Siripuram, Xiao Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Camera traps often run in the field on edge hardware with limited or no connectivity, making small, locally-deployable vision-language models (VLMs) -- not frontier-scale ones -- the practically relevant class to evaluate for species identification. We test whether models in this deployment-relevant 2--8B range carry genuine taxonomic knowledge, evaluating four such VLMs (Qwen3-VL 2B/4B/8B, Gemma3 4B) against the domain-specific specialist BioCLIP (300M parameters) on a 96-species task, comparing clean iNaturalist photographs against camera-trap imagery from 6 this http URL collections, on two independently-sampled evaluation sets. All models identify species far above chance, but every model -- general-purpose or specialist -- degrades sharply on field imagery (domain gaps of 9.6--26.6 percentage points, consistent across taxonomic levels and both evaluation sets), indicating the degradation reflects general image legibility rather than fine-grained discrimination failure. BioCLIP substantially outperforms every VLM tested (by 33.2--59.2 percentage points across an expanded 200-image sample for every model) despite its far smaller size, suggesting the gap reflects specialized training data rather than model scale; yet BioCLIP's own domain gap (18.0 points) is statistically indistinguishable from the best VLM's (22.3 points), suggesting the clean-to-field degradation itself is a property of the image-quality shift rather than a general-purpose-model weakness. Under open-set prompting, 5.9--9.6% of responses are syntactically valid but taxonomically nonexistent species names; the relative fabrication-rate ranking across models replicates exactly across both evaluation sets, a more robust finding than any single point estimate.

---


### 145. [Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data](https://arxiv.org/abs/2609.11917)

**<font color=#1a73e8>作者：</font>** Atindra Jha, Margaret Li, Jure Leskovec 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data. Prior work has studied data repetition for densely activated Transformers, but the effects of data repetition remains largely unexplored for recently dominant sparse architectures such as Mixture-of-Experts (MoE), despite their increased compute efficiency. We vary data repetition rates across single- and multi-domain data mixes, and across MoE settings, including expert count and granularity. We consistently find, for models ranging from 80M to 1B active (8.5B total) parameters, that MoEs degrade more rapidly under data repetition. This effect increases with sparsity, dictated by total rather than active parameters. While 80M dense models can repeat data over 8x with minimal degradation, MoEs instead begin to suffer at 4x, and deteriorate rapidly, ceding their performance benefits in all-unique data settings to underperform dense models after 32x. We experiment with existing regularization methods as a potential remedy. We find that some methods, such as dropout, can mitigate overfitting. In particular, with strong masking-based regularization, MoEs are able to outperform dense models even when data is repeated more than 64 times. However, no method fully matches the performance of all-unique training data. Finally, we analyze internal mechanisms correlated with MoE overfitting in high repetition regimes, and find that MoE routing universally stabilizes early in training, and that expert specialization correlates with overfitting to repeated data. In sum, our work addresses the adverse interactions between sparsity and data repetition: we present evidence for the core mechanisms of overfitting and its potential remediation, and suggest promising avenues for future methods to reduce over-specialization in model parameters by disrupting memorization patterns.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 146. [Black-Box Membership Inference via Word-Level Probability Estimation](https://arxiv.org/abs/2609.10611)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shengjie Niu, Yeheng Ge, Jian Huang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Membership inference attacks (MIAs) have emerged as critical tools for auditing privacy risks in large language models (LLMs), aiming to determine whether a given text was included in a model's training corpus. However, most existing MIAs require access to per-token logits or probabilities, making them inapplicable in practice to proprietary LLMs that expose only textual continuations. To address this underexplored setting, we propose Word-level Probability MIA (WPMIA), a statistically principled MIA for strict black-box privacy auditing. WPMIA estimates word-level generation probabilities via Monte Carlo sampling with local kernel smoothing, then aggregates these estimates into a sequence-level likelihood estimator. Furthermore, WPMIA constructs the likelihood conditioned on different prefixes, thereby amplifying the distributional differences between members and non-members. We evaluate WPMIA across various open-source LLMs and find that it consistently outperforms existing black-box baselines. Importantly, we also evaluate WPMIA on modern proprietary LLMs, including GPT-5-Chat, Gemini-2.5-Flash, and Claude-4.5-Haiku, achieving an average TPR@5\%FPR of 42.0 across these models. These results offer a sound foundation for future research on strict black-box membership inference. Code is available at \href{this https URL}{this https URL}.

---


### 147. [ToxicRAG: Compromising Retrieval-Augmented Generation Systems via Single-Shot Knowledge Poisoning Attacks](https://arxiv.org/abs/2609.11082)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haozhe Lu, Jiaqi Li, Xinyuan Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) can ground large language model (LLM) outputs in external evidence, but it also exposes the system to knowledge poisoning. Representative attacks use multiple injected documents or templates that directly assert a target answer. We present ToxicRAG, a one-document-per-target attack that expresses misinformation as a coherent knowledge-update narrative. The generated document first acknowledges the previously accepted answer, introduces fabricated events that appear to invalidate it, and then attributes the attacker-selected answer to a set of purported authorities. An answer-focused self-validation loop optionally revises a candidate when a surrogate language model does not reproduce the target answer. We evaluate the attack on 100 target questions from each of Natural Questions, HotpotQA, and MS-MARCO, using four victim LLMs and four dense retrievers. In the sampled-corpus setting reported in this paper, ToxicRAG obtains ASRs between 0.61 and 0.91 across the twelve dataset--model combinations. It matches or exceeds the strongest evaluated baseline in every combination, with margins ranging from 0 to 11 percentage points. These results show that narrative-form poisoned documents can remain influential under the evaluated RAG configurations and motivate further study of factual consistency and source provenance in RAG systems.

---


### 148. [KuaiRP Series Role-playing Models Technical Report](https://arxiv.org/abs/2609.11127)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yipeng Wang, Ziwei Zhang, Jiahui Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces the complete technical solution for the KuaiRP series of role-playing models. We aim to achieve four core objectives for a dedicated role-playing model: simplified prompt engineering, highly stable output quality, built-in domain world knowledge, and high-efficiency deployment with a small parameter size. However, effectively injecting deep domain knowledge often leads to a severe catastrophic forgetting of the model's general agent capabilities. To overcome this trade-off, we propose a multi-stage training pipeline. First, we design a standardized character template and construct an SFT data pipeline based on user behavior simulation and reverse profile filtering. Next, we utilize a rule-based composite reward function during the Reinforcement Learning (RL) phase to eliminate common degradation phenomena like length expansion and repetitive generation. Finally, to recover the general capabilities compromised during SFT and RL, we propose a novel self-distillation paradigm using Two-stage On-Policy Distillation (OPD) equipped with Cumulative-Divergence Decay (CDD). By using the domain-adapted model as the teacher and the original base model as the student, we effectively balance deep domain knowledge injection with the preservation of general agent capabilities. Experimental results demonstrate that the KuaiRP models not only match the current state-of-the-art proprietary models in role-playing fidelity within our target domains, but also successfully recover general agent capabilities, maintaining extremely low deployment costs.

---


### 149. [Autonomous Chemical Mechanistic Discovery through Agentic Reasoning and Validation](https://arxiv.org/abs/2609.11147)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dong Li, Sixuan Mi, Zihao Ye 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unraveling reaction mechanisms is central to modern chemistry, yet automating these investigations remains challenging because computational workflows still rely heavily on expert intervention. Here we introduce ARCHE, an autonomous agentic system that integrates a general-purpose reasoning model, a domain-specialized computational chemistry model, and a structured tool registry to transform mechanistic inquiry into a scalable, self-validating process. ARCHE interprets scientific questions, generates and prioritizes mechanistic hypotheses, orchestrates computational workflows, and iteratively refines conclusions based on computed evidence within a closed loop. We validate its capabilities across three increasingly demanding scenarios: reconstructing stereocontrolling transition states and validating the corresponding reaction mechanism in a previously reported asymmetric catalytic reaction; proposing and validating a plausible radical pathway through iterative hypothesis refinement for a recently discovered but unpublished $\alpha$-iodoboronate C-I cleavage reaction; and identifying a chemically interpretable descriptor that governs selectivity in nickel-catalysed migratory cross-coupling reactions. By coupling agentic reasoning with rigorous computational validation, ARCHE advances autonomous mechanistic discovery and establishes a foundation for broader machine-assisted chemical research. The code for ARCHE is publicly available at this https URL.

---


### 150. [SpecGuard: Inference-Time Backdoor Detection For Free](https://arxiv.org/abs/2609.11799)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rui Wen, Ahmed Salem, Andrew Paverd 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are often fine-tuned, shared, or downloaded from third parties, so a deployed model may carry a hidden backdoor that behaves normally on benign inputs but switches to attacker-controlled behavior when a secret trigger appears. While backdoors can be audited before deployment, runtime monitoring remains important for models that are frequently updated. The challenge is that LLM serving is latency-sensitive: existing inference-time detectors either rely on assumptions about the trigger form, which can fail on stealthy attacks, or require extra model computation, such as input perturbations or an additional generation pass.
We introduce SpecGuard, an inference-time backdoor detector that repurposes speculative decoding at zero added model-computation cost. Speculative decoding speeds up inference by using a small draft model to propose tokens and a target model to verify them. We observe that this verification process already exposes a useful signal: when a backdoor is triggered, the target model shifts toward the attacker's behavior, while a clean draft model does not predict this shift, causing the draft-token acceptance rate to change.
We formalize when this signal appears and show that an attacker who suppresses it must also weaken the backdoor. Across diverse backdoor types and model families, SpecGuard reliably detects triggered behavior, including stealthy cases where input-level filters are blind, while avoiding the extra generation cost of existing runtime detectors. Speculative decoding therefore doubles as a free, always-on signal for detecting backdoored LLM behavior.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-153](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
