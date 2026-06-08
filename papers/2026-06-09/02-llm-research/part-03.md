# 🧠 大模型相关研究 | 2026年06月09日

> 本类共 **114** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-114**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-114**

---

### 101. [A Comprehensive Anatomy of Human and DeepSeek-R1 LLM Mathematical Reasoning](https://arxiv.org/abs/2606.07410)

**<font color=#1a73e8>作者：</font>** Yuxiang Chen, Jun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The emergence of "Aha moments" in large language models, particularly DeepSeek-R1-0120, has raised the question of whether these systems genuinely reason or merely imitate the appearance of reasoning. We conduct a comprehensive empirical comparison between model and human reasoning across all 30 problems from AIME 2025, exhaustively annotating 10,247 reasoning steps into five functional categories: Analysis, Inference, Branch, Backtrace, and Reflection. We find a clear structural difference. Human solutions maintain a compact alternation between analysis and deduction, whereas DeepSeek-R1 frequently revisits intermediate results, performs shallow and often unnecessary verification, and loops through local checks without meaningful logical progress. We describe this as topological mimicry: reproducing the surface form of reasoning without its functional role. Despite this, we identify two signals of genuine reasoning. First, successful traces exhibit stable use of branching and backtracking, while failed traces either underuse or overuse exploratory actions. Second, reflection is only effective when placed within deductive inference; reflections trapped in analysis loops focus on local numerical details while missing global logical errors. These findings suggest that current long-CoT models may be rewarded more for the appearance of reasoning than for genuine deductive progress. We discuss directions for improving evaluation and training, including measuring cross-trace stability, penalising "spinning-wheel" traces, encouraging deeper logical correction, and reallocating inference-time compute toward deduction and backtracking. Overall, reasoning quality depends not simply on how much reflection occurs, but on whether reflection appears consistently and at the appropriate logical scale.

---


### 102. [The Masked Advantage: Uncovering Local-Language Access to Cultural Knowledge in LLMs](https://arxiv.org/abs/2606.07422)

**<font color=#1a73e8>作者：</font>** Yang Zhang, Xiao Fei, Amr Mohamed 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to answer culturally grounded questions across languages, yet it remains unclear whether local cultural knowledge is better accessed through English or the local language. Existing evaluations face two key limitations: many rely on parallel template-based questions that may not reflect how cultural knowledge naturally appears, and raw accuracy conflates general language proficiency with language-conditioned knowledge access. We address these issues with a controlled framework built on real-world cultural questions collected from regional benchmarks and local sources. By crossing question type (culture-agnostic vs. culture-specific) with query language (English vs. local language), and estimating ability with a shared 1PL item response theory model, we separate proficiency from localized knowledge access. Across 13 locales and roughly 80 models, we find a consistent English advantage on culture-agnostic questions, indicating stronger English proficiency. However, after accounting for this proficiency gap, local languages show a positive knowledge-access advantage in nearly all locale-model settings. This advantage is often masked in raw accuracy but becomes more visible for frontier, regionally aligned, or language-adapted models. Our results suggest that weaker local-language performance does not necessarily imply weaker cultural knowledge; rather, local cultural knowledge may be more accessible through the local language but hidden by limited language proficiency.

---


### 103. [Watch, Remember, Reason: Human-View Video Understanding with MLLMs](https://arxiv.org/abs/2606.07433)

**<font color=#1a73e8>作者：</font>** Jiahao Meng, Yue Tan, Qi Xu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding is being rapidly transformed by multimodal large language models (MLLMs), as research moves from short clips to long, multimodal, and knowledge-intensive video scenarios. These scenarios require models to handle sparse evidence, long-range dependencies, multimodal alignment, and reliable inference under limited computational budgets. This work presents a human-view perspective on LLM-based video understanding, organized around three functional abilities: watching, remembering, and reasoning. Rather than treating video tasks as isolated benchmarks, this view provides a unified structure for analyzing how video MLLMs acquire evidence, preserve context, and produce grounded outputs. We introduce a formulation that characterizes video understanding systems by their perceptual representations, memory states, reasoning traces, and final predictions. Based on this formulation, we identify challenges in spatio-temporal perception, efficient long-video processing, memory modeling, streaming understanding, and faithful reasoning. Representative methods are organized by their roles in video MLLM systems. Watching covers fine-grained, comprehensive, audio-visual, and efficient perception. Remembering includes offline and streaming memory, while reasoning covers text-only reasoning and thinking with videos. We further examine application domains such as egocentric, sports, instructional, medical, and narrative videos, and cover training datasets and evaluation benchmarks across task types, supervision formats, modalities, and capability dimensions. Finally, we outline open problems and future directions for scalable, memory-aware, and evidence-grounded video intelligence. Related works will be continuously traced at this https URL.

---


### 104. [Skill-3D: Evolving Scene-Aware Skills for Agentic 3D Spatial Reasoning](https://arxiv.org/abs/2606.07436)

**<font color=#1a73e8>作者：</font>** Haoyuan Li, Zhengdong Hu, Jun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper explores agentic 3D spatial understanding, i.e., MLLM agents performing 3D reasoning through tool use. Existing methods often misuse tools and exhibit biased tool preferences under 3D scenarios, leaving the agentic paradigm with only marginal gains over non-agentic strategies. We reveal that 3D spatial reasoning tasks are heterogeneous across scenes, while these agents apply a uniform tool-use strategy to all scenes rather than selecting tools according to the specific scene and task. To address this, we propose Skill-3D, a framework that learns self-evolving scene-aware skills. Specifically, Skill-3D identifies the task scene and records the agent's tool-use trajectory into a Scene Memory, where successful trajectories from similar scenes are aggregated and distilled into a reusable scene-aware skill, with failed ones attached to the skill as lessons. During training, once a similar scene recurs, the corresponding skill is injected to guide the agent, producing new trajectories whose successes and failures further refine the skill, forming a loop in which the memory and the skill library co-evolve. Experiments show that Skill-3D substantially improves tool utilization in 3D spatial reasoning (from 39% to 78% on VSI-Bench), driving the agent toward correct and sufficient tool use. For instance, it improves Gemini-3-Flash by 67% on MMSI-Bench. Furthermore, we conduct agentic post-training over skill-guided trajectories, which boosts Qwen3-VL-8B by 43% on VSI-Bench.

---


### 105. [Sycophantic Praise: Evaluating Excessive Praise in Language Models](https://arxiv.org/abs/2606.07441)

**<font color=#1a73e8>作者：</font>** Daniel Vennemeyer, Phan Anh Duong, Meryl Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sycophancy in language models is typically studied as excessive agreement or validation, while explicit praise and flattery have received comparatively little attention. We argue that sycophantic praise is a distinct alignment problem that cannot be reliably measured using current methods. We introduce a parameterized framework that measures whether praise is excessive relative to contribution quality and expected user ability. We show that our framework substantially outperforms generic LLM judges in agreement with human annotations, and that sycophantic praise occurs far more frequently in social and interpretive domains than in objective reasoning settings. Together, these findings position praise calibration as a distinct alignment challenge.

---


### 106. [TEVI: Text-Conditioned Editing of Visual Representations via Sparse Autoencoders for Improved Vision-Language Alignment](https://arxiv.org/abs/2606.07451)

**<font color=#1a73e8>作者：</font>** Sweta Mahajan, Sukrut Rao, Jiahao Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models such as CLIP are highly useful for diverse tasks due to their shared image-text embedding space. Despite this, the image and text embeddings are often poorly aligned, affecting downstream performance. Recent work has shown that this can be attributed to an information imbalance: images contain more information than their captions describe. In this work, we propose TEVI, a framework that uses captions as a signal for what to retain from image embeddings. Specifically, we use sparse autoencoders to disentangle image embeddings and train a masking module to selectively reconstruct the embedding based on a given caption. In a controlled setup with synthetic captions, we show that TEVI is effective at preserving caption-described attributes while discarding others. By applying TEVI to CLIP models trained on natural images, we further achieve improved retrieval performance across coarse-grained short-caption (MS COCO, Flickr) and fine-grained long-caption (IIW, DOCCI) benchmarks, with stronger gains on richer captions, and improved robustness on the RoCOCO benchmark.

---


### 107. [Time series Foundation Models based on Physics-Informed Synthetic Histories for Cold-Start Photovoltaic Forecasting](https://arxiv.org/abs/2606.07457)

**<font color=#1a73e8>作者：</font>** Lorenzo Longarini, Alessandro Rongoni, Simone Silenzi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> At commissioning time, Photovoltaic (PV) operators must forecast production before target-site observations are available, limiting the direct use of standard supervised forecasters. This cold-start setting is addressed with a zero-shot pipeline that generates a synthetic production history from plant metadata and meteorological covariates, enabling time-series foundation models (TSFMs) to forecast through inference-time conditioning. Five TSFMs are benchmarked against classical baselines under strict Cold-Start Baseline, Real Feedback, and Self-Forecast Feedback strategies. The evaluation spans $440$ PV sites across four datasets and diverse climate regimes. Covariate-aware foundation models outperform baselines by approximately $1.7-2\times$: TabPFN-TS achieves the lowest error under Real Feedback (MAE $0.514$, RMSE $0.721$ $kWh$ ${kWp}^{-1}$ ${d}^{-1}$), while Chronos-2 is most robust under Self-Forecast Feedback. Performance is largely insensitive to the synthetic-history source, indicating that accuracy is driven more by the availability of plausible temporal context than by the specific generator.

---


### 108. [Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle](https://arxiv.org/abs/2606.07462)

**<font color=#1a73e8>作者：</font>** Jiayu Wang, Weijiang Lv, Bowen Fu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As foundation models advance and agent scaffolding becomes increasingly sophisticated, agents have demonstrated remarkable proficiency in complex, long-horizon coding tasks and even autonomous experiment execution. Despite their evolution from research assistants into autonomous research agents, these systems still exhibit significant limitations in field sensitivity, research ethics, and nuanced scientific judgment. Consequently, frontier agents remain unable to fully replace human researchers. To bridge this gap, we conceptualize the AARR (Act As a Real Researcher) benchmark series. Unlike existing benchmarks that primarily assess macro-level execution capabilities, AARR focuses on whether agents can emulate the professionalism, thoroughness, and nuanced reasoning that characterize human researchers in granular research scenarios. In this work, we propose AARRI-Bench (Act As a Real Research Intern), the first benchmark in this series. We conduct extensive experiments across frontier models and agentic systems, revealing that even the best-performing configuration (Mini-SWE-Agent with Claude Opus 4.7) achieves only 68.3\% success rate, frequently overlooking subtle yet critical details that are obvious to real human researchers. Our results indicate that developing researcher-like AI requires further exploration of research behavior, rather than merely complex scaffolding. Our data is released at this https URL.

---


### 109. [Graph Neural Network leveraging Higher-order Class Label Connectivity for Heterophilous Graphs](https://arxiv.org/abs/2606.07475)

**<font color=#1a73e8>作者：</font>** Takuto Takahashi, Itsuki Nakayama, Takahiro Mitani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Node classification in graph neural networks (GNNs) has been widely applied in various fields of graph analysis. GNNs achieve high-accuracy node classification in homophilous graphs, where nodes with the same class label tend to be connected. However, their performance remains limited in heterophilous graphs, where nodes with different class labels are more likely to be connected. In particular, current GNNs derived from graph convolutional networks cannot capture higher-order class label connectivity, which is frequently observed in real-world heterophilous graphs. To address this issue, we propose a novel classifier, Label Context Classifier (LCC), designed to capture higher-order class label connectivity in directed graphs. LCC estimates the class label of a target node by leveraging label context embeddings that are generated through four distinct types of walks. In addition, our approach allows the integration of LCC and any GNN by adaptively learning their importance. Experimental results demonstrate that GNNs integrated with LCC outperform SOTA methods and the label context embeddings improve the node classification performance in heterophilous directed graphs.

---


### 110. [Supervision versus Demonstration-Based In-Context Learning for Multiword Expression Classification](https://arxiv.org/abs/2606.07479)

**<font color=#1a73e8>作者：</font>** Sercan Karakaş, Yusuf Şimşek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Turkish idiomatic light verb constructions (LVCs) are challenging for multiword expression processing because they often share the same surface form as fully literal verb-object combinations while functioning as a single, partially idiomatic predicate. We frame Turkish LVC detection as a binary classification task (literal meaning vs. idiomatic meaning) and evaluate on a manually created controlled set (N=147) with matched negatives: out-of-domain random sentences and in-domain literal controls (NLVC), alongside LVC positives. We compare a supervised Turkish encoder baseline (BERTurk with a classifier head) to three instruction-tuned LLMs from different families under zero-shot, one-shot, and few-shot prompting, and analyze how demonstrations shift error profiles. In zero-shot, LLMs perform well on negatives but show very low LVC recall. One-shot prompting sharply improves LVC detection but can induce strong, model-specific biases, leading models to overpredict or underpredict LVCs. A richer few-shot prompt improves calibration and yields robust overall performance for GPT-OSS-20B and Qwen 2.5-14B. Overall, the results highlight substantial prompt sensitivity in Turkish metalinguistic classification: the supervised baseline remains competitive, while prompted LLMs can match or exceed it on LVCs with carefully constructed demonstrations.

---


### 111. [Sparse Subspace-to-Expert Sharing for Task-Agnostic Continual Learning](https://arxiv.org/abs/2606.07500)

**<font color=#1a73e8>作者：</font>** Fatema Siddika, Md Anwar Hossen, Tanwi Mallick 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning in Large Language Models (LLMs) is hindered by the plasticity-stability dilemma, where acquiring new capabilities often leads to catastrophic forgetting of previous knowledge. Existing methods typically treat parameters uniformly, failing to distinguish between specific task knowledge and shared capabilities. We introduce Mixture of Sparse Experts for Task Agnostic Continual Learning (SETA), a framework that resolves the plasticity-stability conflict through adaptive sparse subspace decomposition into task-specific expert modules. Unlike standard updates, where tasks compete for the same parameters, SETA separates knowledge into unique experts, designed to isolate task-specific patterns, and shared experts, responsible for capturing common features. This structure is maintained through adaptive elastic anchoring and a routing-aware regularization that jointly protect shared knowledge at both the weight and routing levels and enable a unified gating network to automatically retrieve the correct expert combination during inference. Extensive experiments across diverse domain-specific benchmarks demonstrate that SETA achieves competitive or superior overall performance relative to state-of-the-art continual learning baselines, with particularly strong retention of early-task knowledge and improved backward transfer on LLaMA-2 7B and Qwen3-4B.

---


### 112. [Your UnEmbedding Matrix is Secretly a Feature Lens for Text Embeddings](https://arxiv.org/abs/2606.07502)

**<font color=#1a73e8>作者：</font>** Songhao Wu, Zhongxin Chen, Yuxuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit impressive zero-shot capabilities across a wide range of downstream tasks. However, they struggle to function as off-the-shelf embedding models, leading to suboptimal performance on massive text embedding benchmarks. In this paper, we identify a potential cause underlying this deficiency. Our motivation stems from an unexpected observation: text embeddings tend to align with frequent but uninformative tokens when projected onto the vocabulary space. We argue that this excessive expression of high-frequency tokens suppresses the model's ability to capture nuanced semantics. To address this, we introduce EmbedFilter, a simple linear transformation designed to refine text embeddings derived from LLMs directly. Specifically, we uncover that the unembedding matrix within LLMs encodes a latent space that is actively writing these frequent tokens into embedding space. By filtering out this subspace, EmbedFilter suppress the influence of high-frequency tokens, thereby enhancing semantic representations. As a compelling byproduct, this enables an inherent dimensionality reduction, lowering index storage and speedup retrieval while fully preserving the refined embedding quality. Our experiments across multiple LLM backbones demonstrate that LLMs equipped with EmbedFilter achieve superior zero-shot downstream performance even with significantly reduced embedding dimensions. We hope our findings provide deeper insights into the mechanisms of LLM-based representations and inspire more principled designs to improve text embeddings training. Our code is available at this https URL.

---


### 113. [MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism](https://arxiv.org/abs/2606.07512)

**<font color=#1a73e8>作者：</font>** Cong Chen, Guo Gan, Kaixiang Ji 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current Vision-Language Models struggle with hours-long videos because processing full-length visual sequences induces prohibitive token explosion and attention dilution. To overcome this, we introduce MemDreamer to decouple perception and reasoning, shifting long-video understanding into an agentic exploration process. As a plug-and-play framework, it incrementally streams videos to construct a Hierarchical Graph Memory, a top-down three-tier architecture for semantic abstraction, anchored by a foundational graph capturing spatiotemporal and causal relations. During inference, the reasoning model employs agentic tool-augmented retrieval, navigating hierarchies, searching nodes, and traversing logical edges via an Observation-Reason-Action loop. Experiments show MemDreamer achieves SOTA results across four mainstream benchmarks, narrowing the gap with human experts to only 3.7 points. It constrains the reasoning context window to merely 2% of full-context ingestion while delivering a 12.5 point absolute accuracy gain. Furthermore, statistical analysis uncovers a strong positive linear correlation between an VLM's performance on logic reasoning and long-video understanding benchmarks, establishing agentic capability scaling as a new paradigm for multimodal comprehension.

---


### 114. [How reliable are LLMs when it comes to playing dice?](https://arxiv.org/abs/2606.07515)

**<font color=#1a73e8>作者：</font>** Luca Avena, Gianmarco Bet, Bernardo Busoni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the probabilistic reasoning capabilities of large language models through a controlled benchmarking study on discrete probability problems. We constructed two datasets, respectively a set of standard exercises and a set of counterintuitive exercises, designed to trigger heuristic reasoning, and evaluated 8 state-of-the-art models, each tested with and without Chain-of-Thought prompting. Models achieve an average accuracy of 0.96 on standard problems but only 0.59 on counterintuitive ones. We further provide empirical evidence of token bias: performance drops by over 20% when canonical formulations are replaced by disguised variants. Embedding misleading suggestions in the prompt reduces performance by up to 34%, with no model proving immune. Taken together, the reported findings suggest that current LLMs are not yet genuine probabilistic reasoners, despite their success in advanced mathematical problems.

---


> [!TIP]
> 当前位于：**101-114**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-114**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
