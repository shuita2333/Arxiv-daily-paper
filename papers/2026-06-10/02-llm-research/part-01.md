# 🧠 大模型相关研究 | 2026年06月10日

> 本类共 **331** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-331](./part-07.md)

---

### 1. [TinyJudge: Unverifiable Constraint Alignment via Lightweight Specialist Ensembles](https://arxiv.org/abs/2606.07520)

**<font color=#1a73e8>作者：</font>** Yirong Zeng, Yufei Liu, Xiao Ding 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction Following (IF) is a core capability of LLMs, requiring strict adherence to diverse constraints, ranging from verifiable ones (e.g., output length) to unverifiable ones (e.g., tone). Reinforcement learning with verifiable rewards has emerged as a paradigm for IF tasks, leveraging LLM-as-a-judge to assess unverifiable constraints. However, we empirically find that this approach remains a significant bottleneck, suffering from severe reward hacking and higher computational overhead. In this work, we first analyze the generalization capabilities of unverifiable constraints and discover that specific constraints exhibit distinct, high-generalization patterns. Motivated by this, we propose TinyJudge, a framework that employs an ensemble of specialized tiny language models ($\sim0.6B$) to provide rewards for soft constraints. By distilling expertise from frontier models into these tiny models, it achieves high-precision, lightweight evaluation. Extensive evaluations across five benchmarks demonstrate that TinyJudge outperforms the baselines by $\sim10\%$ in average performance and $12\%$ in reward precision. Crucially, it also achieves a $3\times$ speedup in total training time. Our work provides a scalable and robust path for aligning LLMs with unverifiable human instructions.

---


### 2. [Evaluating Hallucinations in Domain-Adapted Large Language Models](https://arxiv.org/abs/2606.07521)

**<font color=#1a73e8>作者：</font>** Sanchita Porwal, Sai Prasath S, Xingjian Bi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates the phenomenon of hallucinations in domain-adapted Large Language Models (LLMs), focusing on the fine-tuning of the Llama-2 model with the Lamini dataset. Hallucinations, or the generation of nonsensical or unfaithful content by LLMs, pose a significant challenge, especially when these models are fine-tuned with domain-specific data. Our methodology involves a series of experiments testing memorization, recall, and reasoning capabilities of the fine-tuned LLM, comparing its performance on novel question-answer pairs and domain-specific information. We found that while the model shows proficiency in tasks similar to its training data, its capability to accurately reason about and recall new domain-specific information remains limited, leading to instances of hallucination. The model demonstrates a tendency to provide correct answers with extra information, suggesting an inclination toward over-generation. These results suggest important limitations of fine-tuning-only approaches for mitigating hallucinations when adapting LLMs to specialized domains and underscore the need for more robust methods in adapting LLMs to specialized domains. The study also provides insights into the varying performance of LLMs on different types of information, revealing a comparative weakness in handling domain-specific queries.

---


### 3. [Community-Specific Slang and Entity Detection via Semantic Shift in Fine-Tuned Language Models](https://arxiv.org/abs/2606.07522)

**<font color=#1a73e8>作者：</font>** Julia Kruk, Sanchita Porwal, Amitrajit Bhattacharjee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose an unsupervised method of resolving slang, unique entities, and folklore from online communities by isolating words in the lexicon that have the highest magnitude of semantic shift. Semantic shift is defined as the evolution of a word's encoded representation as a result of fine-tuning a pretrained Large Language Model (LLM) on a community-specific text corpus. This value is inversely proportional to the cosine similarity between the base model's encoded representation of a word, and a fine-tuned model's encoded representation. We fine-tune the DistilRoBERTa model on text corpora collected from 3 Reddit subreddits (r/Technology, r/Gaming, r/WorldofWarcraft), model a distribution of cosine similarity over the lexicon, and show that one can successfully resolve words that have unique significance to the community by pulling data in the bottom 10-percentile. In contrast, we show that data in the top 10-percentile consist of words that carry relatively universal semantics.

---


### 4. [Retrieval Augmented Generation Framework for the Nepali Legal Domain Question Answering](https://arxiv.org/abs/2606.07523)

**<font color=#1a73e8>作者：</font>** Samir Wagle, Abiral Adhikari, Reewaj Khanal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal domains in high-resource languages like English have widely adopted artificial intelligence for legal question answering. However, data scarcity in low resource languages such as Nepali has limited the training of large language models on Nepali legal texts. This study presents the first application of a Retrieval Augmented Generation based model for Nepali legal question answering using case laws extracted from the Nepal Kanun Patrika digital archive. Using BM25 on chunked documents, the approach achieved a top precision at one of 91 percent, and up to 75 percent with the multilingual E5 large model. Evaluation of generated answers showed 74 percent groundedness, 85 percent truthfulness according to an automated judge model, and 84 percent human evaluated truthfulness when using BM25 document retrieval, with a 92 percent successful answer generation rate. These results demonstrate that the RAG pipeline can effectively address the gap in legal question answering for low resource languages and provide a foundation for reliable AI systems in the Nepali legal domain.

---


### 5. [ABLE: Representing and Mapping LLMs via Attribution-Based Large-model Embedding](https://arxiv.org/abs/2606.07524)

**<font color=#1a73e8>作者：</font>** Zirui Wang, Yusen Hou, Shaofeng Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The explosive growth of large language models (LLMs) has created a heterogeneous and poorly documented ecosystem, making systematic model comparison increasingly important for provenance auditing, security analysis, and model selection. Existing representation methods struggle to address this setting efficiently. Approaches analyzing internal parameters are powerful when architectures are compatible, but face scalability barriers under structural heterogeneity, while methods relying on external outputs may conflate models with similar behaviors and are difficult to align in richer output spaces across different tokenizers. To bridge this gap, we propose ABLE (Attribution-Based Large-model Embedding), a framework that leverages the interpretability space to construct model representations. By aggregating gradient-based feature attributions via a tokenizer-agnostic word-level alignment, ABLE captures model-specific input-sensitivity patterns rather than only surface-level outputs. Beyond empirical utility, we provide a stability analysis showing that, under standard regularity assumptions for differentiable Transformer-style models, ABLE induces a Lipschitz-continuous parameter-to-embedding map with finite-sample convergence guarantees. Extensive experiments on 239 open-source LLMs demonstrate that our training-free approach achieves competitive or superior performance in relation prediction, model routing, and benchmark score prediction.

---


### 6. [GraphLoRA: Structure-Aware Low-Rank Adaptation for Large Language Model Recommendation](https://arxiv.org/abs/2606.07526)

**<font color=#1a73e8>作者：</font>** Lin Mu, Guoji Wang, Li Ni 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong potential for recommendation (LLMRec) due to their powerful reasoning and generalization abilities. However, effectively aligning the textual semantics modeled by LLMs with the collaborative signals remains a key challenge. Existing methods either translate collaborative information into textual prompts or inject pre-trained embeddings into the LLM, both of which treat structural information as static input and fail to capture high-order relational dependencies. To bridge this gap, we propose GraphLoRA, a novel framework that generalizes low-rank adaptation from independent to structure-aware propagation. GraphLoRA embeds a trainable graph message-passing network within the low-rank adaptation pathway, enabling structural signals to propagate through the parameter space. This design allows collaborative topology to explicitly guide parameter updates, fostering deep integration between graph-structured and textual semantic information. Extensive experiments on multiple benchmarks demonstrate that GraphLoRA not only outperforms state-of-the-art LLM-based recommendation methods but also achieves superior generalization, effectively balancing structural reasoning capability with computational efficiency. Code is available at \href{this https URL}{this https URL}.

---


### 7. [Post-training is (Massive) Supervised Learning](https://arxiv.org/abs/2606.07527)

**<font color=#1a73e8>作者：</font>** Michael Hassid, Yossi Adi, Roy Schwartz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The prevailing paradigm for training LLMs has evolved to rely on a massive post-training phase consisting of SFT and RL. In this position paper, we argue that this methodology effectively marks a reversion to the ``pre-train then fine-tune'' approach of the BERT era, explicitly tailoring models to the desired behaviors and specific benchmarks on which they are evaluated. We begin with a historical overview of LLMs, describing the different phases of the LLM evolution. We argue that the current landscape is remarkably similar to the early days of LLMs, where task performance heavily relied on fitting the models to in-distribution datasets. To empirically demonstrate this, we compare pre-trained models to randomly initialized ones, by fine-tuning both variants on modern reasoning datasets and evaluating them on competitive math and code benchmarks. We show that models post-trained from scratch yield highly non-trivial performance. Our findings suggest that current post-training methodologies function primarily as a distribution-fitting mechanism. We finish by positing that developing generally capable models and systems requires moving beyond extensive post-training for predefined behaviors, shifting instead toward training procedures where models ``learn how to learn''.

---


### 8. [BEACON: Behavioral Entropy Aggregation for Cross-Model Hallucination Detection in Large Language Models](https://arxiv.org/abs/2606.07528)

**<font color=#1a73e8>作者：</font>** Naveen Bera, Pulijala Sai Nikhila, Kondaguduru Abhiram 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination in large language models (LLMs), defined as the generation of factually incorrect or unsupported content, remains a critical barrier to reliable deployment. We present BEACON (Behavioral Entropy Aggregation for Cross-model hallucination detectiON), a black-box hallucination detection framework that operates purely on model outputs without requiring access to internal representations or external knowledge bases. BEACON extracts a 31-dimensional feature vector from structured multi-pass generation, integrating NLI-based semantic entropy, embedding geometry, chain-of-thought consistency, and paraphrase stability signals. A gradient-boosted classifier trained on 7,617 labeled examples across seven benchmarks achieves 0.8123 +/- 0.0102 AUROC (95% CI: 0.7632-0.8251), outperforming standalone semantic entropy (+0.2298) and SelfCheckGPT-style consistency baselines (+0.2457). Feature importance analysis shows that hallucination is inherently multi-dimensional, requiring combined uncertainty signals. An efficient 5-call variant achieves 0.7795 AUROC, enabling practical deployment across black-box LLM APIs.

---


### 9. [CAPruner: Conceptual-Adjacent Scene Graph Pruner for Enhancing 3D Spatial Reasoning of Large Language Models](https://arxiv.org/abs/2606.07529)

**<font color=#1a73e8>作者：</font>** Shengli Zhou, Xiangchen Wang, Guanhua Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently been applied to 3D vision-language (3D-VL) tasks, which require spatial reasoning to identify target objects relative to anchors. Scene graphs are commonly employed to represent such relations, but reasoning over complete graphs incurs high token costs and computational inefficiencies, motivating the need for pruning. Existing pruning methods primarily rely on spatial proximity and often remove task-relevant relations, thereby undermining reliable spatial reasoning. To address these limitations, we derive a key requirement for scene graph pruning: preserving spatial relations that are most pertinent to the specific 3D-VL task. Guided by this insight, we propose the Conceptual-Adjacent Scene Graph Pruner (CAPruner). CAPruner integrates fuzzy semantic relevance with spatial proximity to estimate the importance of relations, enabling the selection of critical relations in a task-specific context. Moreover, to avoid costly relation-level annotations, CAPruner is trained by supervising the aggregated scores of each node's incident edges. Extensive experiments demonstrate that CAPruner effectively preserves relations essential for spatial reasoning, leading to substantial performance improvements of LLMs on 3D-VL tasks. Code is available at this https URL.

---


### 10. [mllm-shap: A Shapley Value Explainability Platform for Text-Audio Multimodal Large Language Models](https://arxiv.org/abs/2606.07531)

**<font color=#1a73e8>作者：</font>** Jakub Muszyński, Paweł Pozorski, Maria Ganzha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce mllm-shap, an open-source Python framework designed to extend Shapley Value (SV) explainability from text-only Large Language Models to Multimodal LLMs (MLLMs) processing joint text and audio inputs. While text-based attribution is well-studied, mllm-shap addresses three critical challenges unique to the multimodal regime:
(1) Modality-aware coalition masking, which manages the interleaved processing of discrete text tokens and dense audio encoder frames.
(2) Multi-turn conversation tracking, utilizing per-token metadata to maintain role and modality context.
(3) Phonetic alignment-based token grouping, a novel technique that reduces the coalition space by 10x to 50x, rendering SV estimation computationally feasible for long-form audio.
The platform implements five SV estimation strategies, including a Complementary Contributions (CC) estimator with Neyman-optimal allocation that demonstrates superior convergence over standard Monte Carlo baselines. mllm-shap is provided as a pip-installable package featuring an interactive web-based GUI for granular attribution visualization. To our knowledge, this is the first publicly available framework providing a complete, reproducible pipeline for SV-based explainability in text-audio MLLMs.

---


### 11. [Principled Agent Debate: Adversarial Arbitration for Sycophancy Reduction in Large Language Models](https://arxiv.org/abs/2606.07532)

**<font color=#1a73e8>作者：</font>** Sam Ryan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> RLHF-trained models are systematically biased toward agreement over accuracy, a structural property of the training process. We present Principled Agent Debate (PAD), a multi-agent architecture that mitigates identity-framed sycophancy by arbitrating between two models tuned to opposing philosophical dispositions, with a pragmatist synthesizer evaluating both arguments blind to their origins. This paper evaluates a prompt-based instantiation of PAD. The key mechanisms are static dispositional tuning, identity stripping before synthesis, single-round independent argumentation, and blind arbitration. We evaluate five instantiations on 200 stratified questions from SycophancyEval. All PAD variants (AnCifer, DeWin, FeynStein, BurGal, Trident) significantly outperform the single-model baseline (18.5%) and instructed-opposition baseline (29.0%), with DeWin achieving 48.5% accuracy (z=6.36, p<0.001 versus both). The variants are not significantly different from each other at n=200. The BurGal variant achieves 53.0% but functions as an architectural validity check; its consensus/heterodox axis structurally favors the heterodox model on every benchmark question. A pre-training floor affects an estimated 40% of questions; fine-tuned disposition models are the identified next step.

---


### 12. [Bridging Traditional Explainability Methods and Multimodal Multilingual Models: An XAI-Based Analysis](https://arxiv.org/abs/2606.07533)

**<font color=#1a73e8>作者：</font>** Paweł Pozorski, Jakub Muszyński, Maria Ganzha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) effectively integrate text and audio to interpret context in complex interactive dialogues. However, the internal mechanisms by which heterogeneous modalities influence model behavior remain opaque. While Shapley Values (SV) provide a robust, model-agnostic framework for local explainability in text-based NLP, their extension to multimodal data is hindered by cross-channel dependencies, intricate dialogue structures, and the prohibitive computational complexity of dense audio representations.
In this work, we formalize a multimodal extension of the Shapley Value framework, treating discrete text tokens and aligned audio segments as cooperative features. To ensure computational feasibility, we deploy a suite of efficient estimation strategies: exact SV computation for low-dimensional inputs and sampling-based approximations - including Monte Carlo permutations and stratified sampling with Neyman-optimal allocation - to minimize variance under constrained computational budgets. To resolve the granularity mismatch between modalities, we propose Spectrogram-Guided Phonetic Alignment (SGPA), a novel preprocessing method that maps high-frequency audio streams to interpretable, word-aligned segments.
Our contribution is twofold: first, we provide an open-source, model-agnostic Python package and a companion GUI for the computation and interactive visualization of multimodal attributions. Second, we evaluate our framework using curated subsets of the VoiceBench and Infinity Instruct datasets across diverse multilingual scenarios. Our experimental results reveal that input modality is a primary driver of attribution volatility and demonstrate that standard syntactic importance proxies often fail to predict model attention in multimodal, cross-lingual contexts.

---


### 13. [Multilingual Refusal Alignment for Safer Large Language Models](https://arxiv.org/abs/2606.07535)

**<font color=#1a73e8>作者：</font>** Aleksandra Krasnodębska, Wojciech Kusa, Aldo Lipani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are deployed globally, ensuring their safety and alignment across multiple languages becomes paramount. However, safety behaviors often vary unpredictably between languages, posing significant challenges for consistent and ethical AI. In this work, we systematically investigate the dynamics of multilingual alignment, exploring whether single-language alignment transfers cross-lingually, how language consistency is preserved during training, and the resulting trade-offs with general knowledge capabilities. We introduce RefusEU, a novel refusal alignment dataset covering 12 European languages, including a dedicated test set for evaluating current state-of-the-art models. Our controlled Direct Preference Optimization (DPO) experiments provide two key insights: aligning models exclusively in English is insufficient to ensure cross-lingual safety, even for the same harm categories, whereas training on multilingual datasets can improve safety without degrading general performance, as measured by the Global MMLU benchmark.

---


### 14. [From Architecture to Output: Structural Origins of Hallucination in Large Language Models and the Amplifying Role of Data](https://arxiv.org/abs/2606.07537)

**<font color=#1a73e8>作者：</font>** Md. Rejaul Korim Sadi, Toufiqur Rahman Tasin, Golam Mostofa Naeem  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models hallucinate--producing fluent, confident, factually wrong outputs--with a consistency that persists across generations and scales. Existing taxonomies classify hallucination by output type, distinguishing intrinsic from extrinsic failures and faithfulness from factuality divergence. These frameworks are descriptively rigorous but do not identify which internal mechanism produced a given instance. This paper analyses hallucination as a structural consequence of three architectural decisions that together form a compound failure system. Self-attention's co-occurrence learning substitutes statistical proximity for semantic meaning and produces entity confusion, fact misattribution, and semantic drift. The maximum likelihood estimation training objective optimises next-token probability without factual constraint, rewarding statistically plausible outputs regardless of their truth value. Autoregressive decoding's permanent left-to-right commitment under exposure bias ensures that a single wrong token cascades forward through the entire output sequence without revision. Dataset pathologies--long-tail deficiencies, training bias, and synthetic pollution--amplify these vulnerabilities but do not independently cause them. We make three contributions. First, we map each mechanism to a specific output category in the Alansari and Luqman taxonomy, locating intrinsic hallucination in self-attention, extrinsic hallucination in MLE, and logical inconsistency in autoregressive decoding. Second, we show that each commonly cited dataset pathology exploits one of these mechanisms rather than originating hallucination independently. Third, we identify the diagnostic limitation of output-type-only classification and contrast it with inference-layer mitigation approaches.

---


### 15. [Finding Hidden Relationships Between Medical Concepts by Leveraging Metamap and Text Mining Techniques](https://arxiv.org/abs/2606.07540)

**<font color=#1a73e8>作者：</font>** Weikang Yang, S M Mazharul Hoque Chowdhury, Wei Jin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text is one of the most common ways to store data in this computerized world. At a glance, it may seem that those data are not interconnected. But in reality, data can have hidden connections. Therefore, in this research, a new model has been presented that can find hidden relationships between two medical concepts by using MetaMap and appropriate text-mining techniques. Specifically, the model creates a new comprehensive index structure and can find cross-document hidden links connecting topics of interest that most existing approaches have ignored. Experiments show the effectiveness of the proposed model in discovering new connections between topics.

---


### 16. [Multimodal Large Language Models as Synthetic Participants in Video-Based Studies: An Evaluation](https://arxiv.org/abs/2606.07541)

**<font color=#1a73e8>作者：</font>** Prabal Shrestha, Bohan Jiang, Haoning Xue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown strong performance on objective tasks such as video understanding and reasoning. However, it remains unclear whether they can approximate subjective human responses, which depend not only on content comprehension but also on individuals' social contexts. To address this gap, we evaluate MLLMs as synthetic participants in an emerging task: assessing perceived sensory engagement with short videos. Grounded in the Perceived Message Sensation Value (PMSV) framework, we compare ratings from recruited human participants and profile-conditioned MLLM simulations (n=673) using a 17-item scale measuring emotional arousal, dramatic impact, and novelty. We find that even leading MLLMs (Gemini 3 Flash and Qwen 3 Omni) show limited agreement with human participants. The models exhibit distinct downward mean-shift and central-tendency biases in their rating distributions. They both introduce and flatten subgroup differences, while showing inconsistent sensitivity to participant profiles. Prompting strategies affect these metrics differently, modestly improving some aspects while worsening others. These results highlight both the challenges and opportunities of developing MLLMs as synthetic participants in video-based research. Data and code: this https URL

---


### 17. [Liberating LLM Capabilities in Full-Duplex Speech Models](https://arxiv.org/abs/2606.07547)

**<font color=#1a73e8>作者：</font>** Luoyuan Zhang, Bokai Xu, Junbo Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-based large language models are typically constrained to spoken replies, which limits their user-facing outputs to what can be verbalized and suppresses text-native capabilities such as code generation, structured analysis, and multi-step reasoning in realtime interaction, for tasks that require persistent, structured, and inspectable intermediate outputs. Existing work improves spoken reasoning or full-duplex turn-taking, but still treats text as a hidden intermediate state or a subordinate modality rather than a first-class output channel. We propose Listen-Write-Speak (LWS), a text-first tri-channel paradigm in which a single autoregressive LLM continuously listens to user audio, writes visible free-form text as its primary output, and speaks a realtime oral response in parallel under a shared causal attention context. This behavior is implemented entirely through a Token Schema, requiring no architectural modifications, and learned via a two-stage data pipeline that synthesizes per-second cognitive annotations consistent with the revealed input timeline. Empirically, LWS demonstrates strong full-duplex interaction on Full-Duplex-Bench, reaches 4.72 on VoiceBench AlpacaEval, achieves 92.6% writing-speaking consistency, and consistently outperforms its internal ablations on URO-Bench. These results suggest that visible writing can serve as a first-class output channel for speech interaction without sacrificing realtime responsiveness. The code and dataset are available on the project page: this https URL.

---


### 18. [PathoSage: Towards Multi-Source Evidence Adjudication in Pathology via Experience-Aware Agentic Workflow](https://arxiv.org/abs/2606.07549)

**<font color=#1a73e8>作者：</font>** Chengyang Zhang, Wenchuan Zhang, Bo Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multimodal Large Language Models (MLLMs) and agent workflows have shown strong promise for computational pathology, yet reliable patch-level reasoning remains challenging. End-to-end pathology MLLMs often hallucinate morphological features, while recent agentic systems usually merge tool outputs and retrieved knowledge into a shared context, making decisions vulnerable to conflicting evidence and context contamination. We propose PathoSage, a three-stage framework that explicitly separates knowledge retrieval, evidence collection, and evidence adjudication for patch-level pathology multimodal reasoning. Its core component, Structured Evidence Deliberation, independently evaluates heterogeneous evidence from tools, performs conflict analysis, and generates the final judgment in a fresh context to reduce anchoring bias. We further introduce a training-free Beta-Bernoulli experience system with continuous credit assignment to model long-term tool reliability and construct similarity-weighted priors for future tool use. Experiments show that PathoSage effectively mitigates VQA hallucinations and classifier disagreement, outperforming strong pathology MLLM and agentic baselines. Our results highlight explicit evidence adjudication and reliability-aware tool modeling as key ingredients for robust pathology agents.

---


### 19. [Symbolic Reasoning Frameworks Modulate LLM Risk Aversion in Multi-Agent Strategic Settings](https://arxiv.org/abs/2606.07552)

**<font color=#1a73e8>作者：</font>** Augustin Chan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit innate behavioral tendencies when deployed as strategic agents -- notably a risk-averse "turtle" bias toward defensive play. We show that symbolic reasoning frameworks, injected as per-round reflective prompts into one agent, differentially modulate this bias and reshape the multi-agent ecosystem to produce framework-specific winner distributions. In a 7-player Warring States Diplomacy variant (41 games, 4 conditions, single-campaign memory accumulation), each framework produces a distinct ecosystem signature: under control, Yan dominates (7/11, 64%); under I-Ching yarrow divination, Yan and Chu co-dominate while Qin is completely suppressed (0/10); under Tarot, Qin dominates (5/10, Fisher vs. pooled p = 0.006); under scrambled-text ablation (incoherent oracle text preserving prompt structure), Qi dominates (5/10, Fisher vs. pooled p = 0.006). The framework-receiving agent (Han) never wins and shows no survival difference across conditions (Fisher p = 1.0), but Tarot consistently elevates Han's peak territory (mean 3.0 SCs vs. 2.1-2.5 others, Kruskal-Wallis p = 0.010). Neither framework's content predicts subsequent actions -- hexagram themes (chi-squared p = 0.95) and Tarot card postures (chi-squared p = 0.69) are both independent of action choice -- suggesting the modulation operates through the reflective process, not content-following. We present this as an observation paper establishing that alignment-framework choice at the agent level produces distinctive system-level consequences in multi-agent settings.

---


### 20. [Phantom transitions in language model fine-tuning](https://arxiv.org/abs/2606.07559)

**<font color=#1a73e8>作者：</font>** Vaibhav Prakash, Jayasri Dontabhaktuni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a language model on contexts whose correct completion has a near-synonym competitor often fails silently. The cross-entropy loss decreases monotonically while the correct token never overtakes the competitor in rank. We study this regime across five transformer architectures spanning two families and a fivefold parameter range, on ten hand-selected near-synonym contexts. We instrument these failures with an order parameter combining the predicted distribution and pairwise embedding overlaps. It decomposes additively into a signal, tracking the model's commitment to the correct token over its nearest competitor, and a background drag, set by how the embedding bulk leaks probability into the score. This isolates two failure modes. In kinematic failure the signal stays small. In structural failure the drag actively worsens as fine-tuning proceeds. We observe sharp catapult-like jumps in the order parameter that resemble a phase transition. A central negative result organises the paper. The transitions are phantoms. The spontaneous-symmetry-breaking interpretation is ruled out by direct measurement. Catapult-like jumps still appear under LoRA fine-tuning with the token embedding matrix exactly unchanged during training, where no geometric phase transition is possible. The discontinuity lives entirely in the softmax readout. A small number of dimensionless quantities organise the trajectory across architectures. One is consistent across all five under full fine-tuning. A second sorts architectures into two classes by bulk embedding distribution and predicts LoRA sufficiency. As a blind test, the framework predicts the critical learning rate of a held-out architecture, not used to fit any parameter, to within 2.1% of a subsequent learning-rate sweep. Findings concern the near-synonym mechanism only and should not be extrapolated without recalibration.

---


### 21. [Function-Vector Heads Are Two Populations: Writers and Cancellers in In-Context Learning](https://arxiv.org/abs/2606.07560)

**<font color=#1a73e8>作者：</font>** Han-yu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Function-vector (FV) heads (Todd et al., 2024) are typically identified by the magnitude of their causal contribution to in-context rule tasks, under the implicit assumption that the top set is a homogeneous functional class. This assumption fails. We replace magnitude-only ranking with a sign-preserving criterion (refined DLA + permutation FDR) and validate each candidate by path patching. The FV head population then splits into two opposing sub-populations: writers push the rule-correct logit up; cancellers push it down. A four-condition canonical verdict holds in $13/15$ cells across three model families and six Pythia scales, and a sign-shuffle rejects homogeneity in $5/6$ main cells. The structure is invisible to magnitude-only ranking: Todd's top-$20$ captures $64\%$ of cancellers but only $4\%$ of writers on the hierarchical task, and $59\%$ of writers but only $8\%$ of cancellers on the modular task. We rule out six artefact accounts on all $27$ canceller (cell, head) pairs: induction overlap, sinks, generic importance, rank-$1$ copy-suppression, V-cascade, and rank-nearest non-FV controls. Zero-ablating cancellers yields $+0.13$ to $+0.29$ nats of logit gain in $6/6$ main cells with a directionally consistent $+2$ to $+7$ pp accuracy effect.

---


### 22. [Enabling KV Caching of Shared Prefix for Diffusion Language Models](https://arxiv.org/abs/2606.07571)

**<font color=#1a73e8>作者：</font>** Younghun Go, Jaehoon Han, Changyong Shin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) caching for shared prefixes is essential for high-throughput large language model (LLM) serving, but it faces critical challenges in emerging diffusion language models (DLMs). In DLMs, bidirectional attention means that updating any token dynamically alters the entire context and its corresponding KVs. Thus, existing caching techniques developed for LLMs, which assume that KVs remain invariant once computed, corrupt the shared prefix KVs. Our experiments show that applying these techniques to DLMs causes model accuracy to collapse to near zero.
To unlock high-throughput DLM serving, we propose bidirectional prefix caching, bicache, the first KV caching technique for shared prefixes in DLMs. bicache is designed based on key observations from our comprehensive analysis: shared prefix KVs remain stable and reusable in shallow layers, while the depth of shallow layers depends on the fraction of shared prefix tokens in each request. Thus, bicache dynamically identifies a safe layer depth for reusing shared prefix KVs and eliminates redundant computation. Evaluations demonstrate that bicache significantly improves serving throughput by 36.3%-98.3% compared to existing techniques without accuracy collapse (only 0-1.8% difference).

---


### 23. [OmniMem: Perturbation-aware Memory Compression for Streaming Audio-Visual LLMs](https://arxiv.org/abs/2606.07577)

**<font color=#1a73e8>作者：</font>** Guangzhi Sun, Yixuan Li, Yudong Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audio-visual large language models (LLMs) hold strong promise for long-form video understanding, yet their long-video inference is fundamentally limited by the linear growth of video tokens and key-value (KV) caches. We present OmniMem, a memory-efficient streaming framework designed specifically for audio-visual LLMs. Unlike existing compression methods that treat all tokens uniformly, OmniMem introduces a modality-aware memory allocation strategy that separately manages visual and audio contexts, addressing the severe token imbalance between the two modalities. OmniMem further preserves informative and non-redundant KV states through perturbation-aware memory selection, enabling compact memory without sacrificing long-range understanding. To strengthen compression under realistic deployment constraints, we also explore budget-aware fine-tuning, which encourages the model to consolidate useful information into retained memory. Experiments on VideoMME Long, LVBench, and LVOmniBench with video-SALMONN 2+ and Qwen-2.5-Omni show that OmniMem consistently improves over strong training-free compression baselines by 2-4% absolute accuracy under the same memory budgets, with an additional 1-2% gain after fine-tuning.

---


### 24. [Training-Inference Kernel Contracts: Bounding Divergence in Post-Training and Deployment](https://arxiv.org/abs/2606.07581)

**<font color=#1a73e8>作者：</font>** Bruce Changlong Xu, Lan Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A modern post-training pipeline often writes one symbol for its policy, pi_theta, while evaluating it through two different programs: a training kernel optimized for autograd and an inference kernel optimized for low-precision, fused, dynamically batched serving. In finite precision, these kernels can induce different distributions at identical weights, with the gap concentrated on slices that aggregate benchmarks under-represent. This paper proposes kernel contracts: a contract-first framework for specifying acceptable divergence between K_train and K_inf. A contract C = (N, S, R, O, Pi) combines numerical, statistical, runtime, and observability clauses with an escalation policy from violations to routing actions. We derive a chain of bounds from logit drift to total-variation distance to bounded reward drift, and specialize it to RL post-training, where per-token importance-ratio drift yields a bound on policy-gradient bias under explicit support and norm assumptions. We also describe a four-stage promotion pipeline, online routing loop, and minimal YAML DSL for contract artifacts. This is a framework and vocabulary paper; we do not report production-scale empirical validation.

---


### 25. [Multimodal Group Emotion Recognition In-the-Wild Towards a Privacy-Safe Non-Individual Approach](https://arxiv.org/abs/2606.07585)

**<font color=#1a73e8>作者：</font>** Anderson Augusma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This thesis addresses group emotion recognition (GER) in-the-wild with a focus on privacy preservation. Unlike traditional emotion recognition methods that rely on individual-level cues such as face, gaze, or voice analysis, this work uses collective audio-video signals to infer emotions at the group level, reducing risks of individual monitoring and surveillance. Two complementary frameworks are proposed. The first is a cross-attention multimodal architecture for audio-video fusion, combined with Frames Attention Pooling (FAP) for temporal aggregation. It is supported by synthetic data augmentation and validated through ablation studies, demonstrating robustness in real-world GER conditions. The second framework, Variational Encoder Multi-Decoder (VE-MD), learns a shared latent space for emotion classification and structural representation prediction, including body and face cues. Two decoding strategies, DETR-based and heatmap-based, are explored to analyze the role of structural representations in group and individual settings. The thesis makes three main contributions: it clarifies the role of multimodality and structural cues in group-level affective computing; introduces two architectures for privacy-preserving multimodal GER; and shows that competitive performance can be achieved without using individual features as input data.

---


### 26. [From Human Guidance to Autonomy: Agent Skill System for End-to-End LLM Deployment on Spatial NPUs](https://arxiv.org/abs/2606.07586)

**<font color=#1a73e8>作者：</font>** Jiajie Li, Erwei Wang, Zhiru Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial neural processing units (NPUs) provide an energy-efficient platform for edge LLM inference, but efficiently deploying an LLM end-to-end on such hardware remains labor-intensive. Although AI coding agents have begun to lower this cost, existing studies have largely focused on single-kernel optimization rather than end-to-end LLM deployment on resource-constrained spatial NPUs.
We present a two-stage methodology, instantiated on the AMD XDNA 2 NPU, that progresses from human-guided development to agent autonomy. In the first stage, we develop a reference deployment of Llama-3.2-1B through human-guided agent assistance. The resulting implementation achieves a speedup of 2.2x on prefill and 4.0x on decode over the hand-optimized baseline, with the optimization trajectory and its lessons recorded as structured documentation throughout. In the second stage, we distill the documentation into an agent skill system consisting of eight phases, orchestrating the optimization and debugging skill sets, with numerical correctness strictly enforced at each phase.
Using our agent skill system, we autonomously deploy eight additional decoder-only LLMs (Llama-3.2-3B, SmolLM2-1.7B, Qwen2.5-{0.5B, 1.5B, 3B}, Qwen3-{0.6B, 1.7B, 4B}) end-to-end on the AMD XDNA 2 NPU using the open-source compiler stack. To our knowledge, these models have not previously been deployed on AMD NPUs via any open-source software stack. Each deployment completes in 0.5-4 hours of agent wall time with almost no human guidance, and passes the numerical-correctness gates, demonstrating functional generalization to previously unencountered LLMs. Three of the eight match or exceed the sustained performance of our Llama-3.2-1B reference deployment, suggesting that the resulting implementations can be competitive without additional model-specific human engineering.

---


### 27. [The Routing Plateau: Understanding and Breaking the Accuracy Limits of LLM Routers](https://arxiv.org/abs/2606.07587)

**<font color=#1a73e8>作者：</font>** Yifan Lu, Qiyue Zhang, Shenrun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM routing has become a popular approach to improve the cost-quality trade-off of LLM services by dynamically selecting a model for each query. Recent work has explored a broad range of routing methods, including clustering-based routers, learned classifiers, pairwise ranking, and confidence-based approaches. Our extensive study of 21 routing methods across five benchmarks reveals a consistent phenomenon that we call the routing plateau: many methods, including kNN, achieve very similar accuracy and converge to a narrow performance range that remains far below the oracle router. Our investigation shows that the plateau is largely caused by a predictability bottleneck: current routers mainly learn global averaged model-performance trends rather than fine-grained query-specific routing signals. As a result, they solve overlapping easy queries but collectively fail on hard queries that require instance-specific routing decisions. We further study how to move beyond the plateau and find that larger training datasets, stronger encoders, and end-to-end fine-tuning can further improve routing accuracy. These findings characterize the common limits of current routing methods and provide insights and actionable directions for the community to build more effective routing systems.

---


### 28. [SlideCheck: Guiding Self-Supervised Pretraining of Pathology Foundation Models via Dataset Distributions](https://arxiv.org/abs/2606.07590)

**<font color=#1a73e8>作者：</font>** Mingyi He, Xinyi Guo, Xitong Ling 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models are pretrained on large streams of WSI-derived patches, while supervision during data construction is often slide-level, sparse, or heterogeneous. This mismatch makes it difficult to understand and control which biological patterns enter the pretraining data. We propose SlideCheck, a lightweight pretraining data guidance tool built on frozen pathology foundation model patch features. Rather than serving as a standalone patch diagnostic model, SlideCheck provides explicit abnormality and malignancy scores for organizing, filtering, and auditing pathology pretraining data. SlideCheck uses a dual-head MLP to separately model broad abnormal morphology and malignant evidence. A regularized feature-space scorer provides a supervised anchor for patch-level evidence estimation, while score-attention agreement combines patch scores with WSI-level MIL attention to mine high-confidence pseudo labels. The same scores are then used to construct broad-positive ViT pretraining subsets, where a patch is selected if either abnormality or malignancy evidence exceeds a threshold. Experiments show that SlideCheck-defined data distributions influence the downstream behavior of self-supervised ViT pretraining, indicating that biological composition is an important controllable factor in pathology foundation model development. Curated subsets can approach full-data performance, suggesting that explicitly scored patch pools may support more efficient and auditable pretraining data construction. These findings position SlideCheck as a data guidance and auditing layer for transforming large, undifferentiated patch pools into controllable and reusable pretraining datasets.

---


### 29. [ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research](https://arxiv.org/abs/2606.07591)

**<font color=#1a73e8>作者：</font>** Wanghan Xu, Shuo Li, Tianlin Ye 等 50 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI coding agents are increasingly used for scientific work, but their end-to-end autonomous research capability remains difficult to verify. We present ResearchClawBench, a benchmark for evaluating autonomous scientific research across 40 tasks from 10 scientific domains. Each task is grounded in a real published paper, provides related literature and raw data, and hides the target paper during evaluation. Expert-curated multimodal rubrics decompose the target scientific artifacts into weighted criteria, enabling evaluation of target-paper-level re-discovery while leaving room for new discovery. We evaluate seven autonomous research (auto-research) agents under a unified protocol and seventeen native LLMs through the lightweight ResearchHarness. Current systems remain far from reliable re-discovery: the strongest autonomous agent, Claude Code, averages 21.5, and the strongest ResearchHarness LLM, Claude-Opus-4.7, averages 20.7, with an LLM frontier mean of only 26.5. Error analysis shows that failures concentrate in experimental protocol mismatch, evidence mismatch, and missing scientific core. ResearchClawBench provides a reproducible evaluation frontier for measuring progress toward autonomous scientific research.

---


### 30. [A Mechanistic Analysis of Adversarial Fine-tuning of Vision Transformers](https://arxiv.org/abs/2606.07593)

**<font color=#1a73e8>作者：</font>** Hannah Gao, Isha Agarwal, Dylan Hadfield-Menell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The widespread use of image classification models in high-risk, real-world situations necessitates making these models robust to slight disturbances or perturbations, such as blurring or sharpening, in the input images. While vision transformers (ViTs) play an integral role in many modern-day multi-modal models like Vision-Language-Models (VLMs) and Vision-Language-Action (VLA) models, they have received a lack of attention in the setting of robustness. In this work, we analyze the effects of adversarial fine-tuning, a popular method for improving model robustness to image perturbations, on a ViT's performance on perturbed and regular images through a mechanistic lens. We adversarially train a ViT on low-frequency and high-frequency image corruptions, and attempt to explain changes in downstream model performance through an examination of the model's attention mechanisms, internal representations, and knowledge evolution. Overall, our results suggest that, while fine-tuning on inputs with common corruptions improves model performance and certainty on new instances of corrupted data, these improvements do not transfer to other classes of corruptions not seen in the training. Additionally, despite observing changes in visual attention and knowledge evolution across layers, we found that adversarial training did not lead to fundamental changes in the sparse representations learned by ViTs.

---


### 31. [Shortcuts in the Tail: Debiasing via Post-Hoc Spectral Compression of Fine-Tuning Updates](https://arxiv.org/abs/2606.07596)

**<font color=#1a73e8>作者：</font>** Edward Sun, Dmitrii Troitskii  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning often introduces spurious correlations alongside task knowledge, causing systematic failures on underrepresented groups. Existing mitigations require retraining, group labels, or curated counterfactual data. We show a simple post-hoc intervention reduces shortcut reliance without any of these: truncating the tail of the SVD of $\Delta W = W_\mathrm{ft} - W_\mathrm{base}$ reduces the spurious-group gap while preserving task accuracy. Across three instruction-tuned models ($0.5$B--$7$B) and four classification benchmarks, top-$k$ truncation reduces the gap on every cell at $<2$ pp accuracy loss, by up to $5\times$ on CivilComments. We propose this works because the shortcut response sits in the tail of the singular ordering of $\Delta W$, a claim about how truncation behaves rather than about the raw singular values, which are broadly distributed and look the same across all four datasets. A controlled boundary case in which fine-tuning has only a shortcut to learn shows the predicted FT-to-base collapse, and bottom-/random-$k$ and matched-rank LoRA controls rule out generic low-rank approximation and rank-constrained training as the explanation. We read this as preliminary evidence that the singular basis of $\Delta W$ is a useful coordinate system for studying what fine-tuning has learned.

---


### 32. [Sample-Efficient Post-Training for LEGO Spatial-Physics Reasoning](https://arxiv.org/abs/2606.07602)

**<font color=#1a73e8>作者：</font>** Yuhuan Yuan, Zhouliang Yu, Minghao Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based LEGO assembly generation requires both semantic grounding and physical feasibility. We identify a data-induced failure mode, PhysHack, in which the assemblies satisfy physical-validity constraints while producing structures that are geometrically misaligned, semantically inconsistent, or poorly calibrated. To address this challenge, we propose a model-based data selection approach that uses only a small fraction of the training data while improving physically grounded LEGO assembly generation. Building on the selected trajectories, we introduce PVPO, a sample-efficient reinforcement learning method that couples physical feasibility with voxel-space geometric rewards. Our results show that physical validity alone is an insufficient proxy for reliable physical reasoning: models can learn to generate valid structures without preserving semantic or geometric fidelity. Experiments across model backbones and test-time scaling settings demonstrate that PVPO improves structural and semantic alignment, physical validity, structural stability, and calibration, while reducing reliance on extensive post-hoc rejection sampling. In particular, results on calibration show that PVPO mitigates PhysHack by making test-time selection more predictive of semantic and structural quality.

---


### 33. [Contribution Weights: A Geometrical Analysis of Self-Attention Transformers](https://arxiv.org/abs/2606.07604)

**<font color=#1a73e8>作者：</font>** Harry Jake Cunningham, Nicola Muca Cirone  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analyzing attention weights has become a standard approach for interpreting the information flow of Large Language Models (LLMs). However, this approach has significant limitations as it neglects the geometric properties of the value vectors being aggregated. To address this gap, we introduce \emph{Contribution Weights}, a projection-based metric that quantifies a token's influence by accounting for it's attention weight, value magnitude, and directional alignment with the layer output. We demonstrate that contribution weights provide a more faithful measure of token importance, consistently outperforming attention-based metrics in identifying semantically critical tokens across different decoder-only models, tasks, and datasets. Further, our metric enables novel mechanistic analysis of \emph{attention sinks}. While previous work characterized sinks as passive repositories for excess attention, we reveal they serve an active functional role, suppressing information through a convex relationship between sink rate and output norm, stabilizing representations by opposing the semantic drift of low-confidence tokens.

---


### 34. [Subtitle-Aligned Fine-Tuning of Whisper for Swiss German ASR: Benchmark Contamination, Convention Mismatch, and an Honest Baseline at 25.6% WER (13.8% cWER)](https://arxiv.org/abs/2606.07608)

**<font color=#1a73e8>作者：</font>** Felix Akeret  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a systematic study of fine-tuning OpenAI's Whisper large-v3 for Swiss German ASR, using 1,367 hours of broadcast speech paired with Standard German subtitles as weak supervision. Through 16 iterative training runs on an NVIDIA DGX Spark (Grace Blackwell, 128 GB unified memory, up to 1 PFLOP FP4), we compare LoRA and full fine-tuning of the 1.55B-parameter model, investigate hallucination root causes, and quantify the effect of data quality, subtitle alignment, and training strategy. Our best model achieves 25.6% measured WER on the All Swiss German Dialects Test Set (ASGDTS) in an honest evaluation on strictly disjoint data. A harmonized error analysis separating genuine errors from valid stylistic variation (tense, word order, Swiss orthography) yields a content WER (cWER) of 13.8%, counting only actual recognition failures. Bias-corrected estimation reduces this to 8.5%, suggesting the true error rate is roughly one third of measured WER.
We demonstrate that published state-of-the-art Swiss German ASR results (17.1-17.5% WER) are inflated by benchmark contamination: a vanilla Whisper model self-trained on the ASGDTS test set with zero Swiss German data achieves 13.88% WER, surpassing all published systems. Experiments with Phi-4-multimodal show an even stronger memorization effect (3.9% WER), revealing that the benchmark primarily measures convention matching rather than dialectal comprehension.
We release two models, a LoRA adapter (25.32% WER, 13.9% cWER) and a full fine-tuned model (25.60% WER, 13.8% cWER), among the few publicly available, honestly evaluated Whisper models for Swiss German, under Apache 2.0 with full reproducibility, requiring no institutional data agreements.

---


### 35. [LEAF: Growing Trees Without Branching for Speech-Aware Large Language Model Post-Training](https://arxiv.org/abs/2606.07610)

**<font color=#1a73e8>作者：</font>** Argyrios Gerogiannis, Yekaterina Yegorova, Mark Hasegawa-Johnson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-art GRPO-style methods for speech-aware large language model post-training suffer from coarse credit assignment, broadcasting the same terminal-reward advantage to every token in a response. This ignores useful structure within rollout batches, where speech-conditioned completions often share prefixes before diverging at important decisions. We propose Low-rank Exploration with Adaptive Forking (LEAF), a retrospective tree-based RL method that recovers this structure without online branching or additional decoding. LEAF samples complete responses, selects high-surprisal boundaries, groups responses by shared prefixes, and assigns span-level advantages using descendant rewards. We theoretically justify LEAF's span-level credit assignment and boundary-selection design. Empirically, LEAF improves over GRPO across speech question answering and speech translation benchmarks under the same rollout and low-rank adaptation budget. Notably, smaller LEAF-trained models outperform current state-of-the-art, full-parameter baselines.

---


### 36. [Can You Trust What You See? Human and AI Detection of Synthetic Legal Evidence](https://arxiv.org/abs/2606.07613)

**<font color=#1a73e8>作者：</font>** Jinzhe Tan, Ali Ekber Cinar, Karim Benyekhlef  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual evidence has long been treated as a reliable form of legal proof, but advances in artificial intelligence (AI) are undermining that assumption. This article asks how well humans and frontier multimodal large language models (MLLMs) can distinguish authentic evidentiary photographs from AI-generated counterparts in the object-centric scenarios typical of civil disputes. We built Synthetic Legal Evidence Detection (SLED-1400), a dataset of 200 authentic evidence images paired with 1,200 synthetic counterparts produced by six contemporary text-to-image generators across ten evidence categories. The same stimuli and response format were used in a controlled web experiment with 136 lay participants and in a standardized evaluation of four MLLMs (GPT-5.1, Gemini-3-Pro, Gemini-3-Flash, Qwen3-VL-235B). Human accuracy was 64.8% overall, and 48.5% and 51.0% on the two strongest generators (Gemini-3-Pro-Image and Flux-2-Max), indistinguishable from chance. MLLMs never misclassified an authentic image (100% specificity), but missed most synthetic outputs from the harder generators, with average MLLM detection at 5.9% on Gemini-3-Pro-Image outputs. Human and MLLM errors were largely uncorrelated, while the four MLLMs were strongly correlated with each other. Neither group is a reliable standalone authenticator. We argue that visual evidence in legal proceedings should be treated as inherently contestable, and that a workable procedural response must combine trained human review, MLLM screening, and provenance infrastructure such as C2PA Content Credentials.

---


### 37. [ScaleSweep: Accurate NVFP4 Post-Training Quantization of LLMs via Block Scale Initialization](https://arxiv.org/abs/2606.07618)

**<font color=#1a73e8>作者：</font>** Li Lin, Xiaojun Wan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> NVFP4 is a recently introduced hardware-supported FP4 format that improves the fidelity of 4-bit quantization through fine-grained block scales. However, existing NVFP4 scale initialization methods still primarily rely on AbsMax initialization, which leaves a noticeable gap to the optimal solution. To address this, we propose ScaleSweep, a simple and efficient scale optimization method that sweeps over feasible block scale candidates and selects the candidate that minimizes a target objective. We further provide a theoretical analysis of NVFP4 quantization and derive both lower and upper bounds for the required sweep range under mean square error (MSE) and weighted mean square error (WMSE) between the original tensor and the quantized reconstructed tensor. The proposed bounds substantially reduce the sweep space while preserving the optimal candidate, enabling negligible overhead compared with the baseline quantization operators. Experiments on Llama and Qwen models demonstrate that ScaleSweep consistently improves quantization performance over existing initialization methods and further narrows the gap to full precision. In particular, under aggressive end-to-end quantization of weights, activations, KV cache, and query states, ScaleSweep preserves more than 93% of the full-precision performance.

---


### 38. [Finite Certificates for In-Context Determinacy and a Threshold Theory of Emergence in Language Models](https://arxiv.org/abs/2606.07623)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Hamdi Alakkad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops a model-theoretic framework for verifying context-conditioned language-model behavior by replacing benchmark labels with finite semantic certificates. The first problem is finite determinacy: when do examples in a context force the answer to a query without changing model parameters? In finite-field linear task families, we prove an exact row-space criterion, compute the residual hypothesis count, derive full and query-local identification curves, and show that extracting a smallest forcing subcontext is NP-complete even for binary outputs. The second problem is threshold emergence: when does an apparent benchmark jump reflect a semantic transition rather than a discontinuity of the scoring map? We prove an anti-mirage theorem separating thresholded metrics from semantic confidence and give a rate-sensitive crossing bound for latent commitments becoming visible above threshold. The common semantic object is a confidence functional on definable events. We show that it is a Boolean probability measure, equivalently a Keisler measure on the relevant type space, whose measure-one formulas form a proper filter and whose Stone-space representation is invariant under definitional expansion. The resulting calculus provides finite context certificates, pair-separator hitting sets, query teaching dimension, prompt-preservation criteria, and scale-limit witnesses. Exact-arithmetic ancillary scripts reproduce the finite-field and threshold calculations and generate the data used by the figures.

---


### 39. [Sequential statistical inference for Large Language Models: Representation, validity, and monitoring](https://arxiv.org/abs/2606.07624)

**<font color=#1a73e8>作者：</font>** Yao Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This discussion argues that sequential statistical inference can naturally contribute to LLM trustworthiness. In deployment, LLM systems are queried repeatedly, conditioned on evolving contexts, and incorporate user or tool feedback, and may exhibit behavioral shifts after model updates or distribution changes. The discussion is organized around three tasks: representation, modeling LLM interactions as dependent stochastic processes rather than isolated prompt--response pairs; validity, developing uncertainty guarantees that remain meaningful under dependence, repeated use, and adaptation; and monitoring, using sequential alarms and change-point detection to identify shifts in calibration, hallucination rates, refusal behavior, fairness, or other task-relevant properties. This perspective complements recent surveys by viewing trustworthy LLM deployment as a problem of statistical process control.

---


### 40. [Large Language Models Should Learn Personalized Rather Than Aggregated Human Preferences](https://arxiv.org/abs/2606.07629)

**<font color=#1a73e8>作者：</font>** Cristina Garbacea  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current approaches to aligning large language models (LLMs) aggregate diverse human preferences into a single reward signal, effectively optimizing for a hypothetical ``average user'' who represents no real person particularly well. This position paper argues that LLMs should learn personalized, individual preferences rather than aggregated ones. We show that aggregation masks critical information about preference diversity, individual values, and contextual dependencies, which is a limitation both theoretically grounded in social choice theory and empirically evident across demographic groups. We analyze the rich structure that human preferences encode, survey technical approaches to personalization, and systematically address counterarguments on scalability, shared standards, and manipulation risk. While personalization introduces genuine safety challenges including filter bubbles, value lock-in, and psychological manipulation, we argue these are manageable through bounded personalization frameworks that preserve universal safety constraints while accommodating legitimate individual variation. We conclude with a concrete research and policy agenda for developing preference-aware models that respect both individual autonomy and collective safety.

---


### 41. [Active Learning with Foundation Model Priors: Efficient Learning under Class Imbalance](https://arxiv.org/abs/2606.07630)

**<font color=#1a73e8>作者：</font>** Jiancheng Zhang, Meiqing Li, Qi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world datasets across image and text domains are often characterized by skewed class distributions and noisy annotations, which jointly degrade model performance, particularly on minority classes. Among existing solutions, active learning offers an effective and efficient paradigm by selectively querying the most informative and balanced samples for annotation. We propose an innovative active learning framework that mitigates class imbalance and selects the most informative samples to annotate. Leveraging foundation model priors, our algorithm enables imbalance-aware co-decisions between foundation model and small model to tackle noisy and imbalanced labels across various domains. We introduce the first study to systematically explore active learning under the dual challenges of label noise and class imbalance across image and text domains. Extensive experiments on imbalanced datasets demonstrate that our method achieves substantial annotation savings-over 50% compared to the best active learning baseline-while preserving performance and robustness to label noise.

---


### 42. [NeuroAlign: Hierarchical Multimodal Fusion of Dynamic and Structural Neuroimaging for MCI Analysis](https://arxiv.org/abs/2606.07635)

**<font color=#1a73e8>作者：</font>** Xiongri Shen, Zhenxi Song, Jiaqi wang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal neuroimaging fusion of functional MRI (fMRI) and diffusion tensor imaging (DTI) provides complementary information for cognitive impairment analysis, but remains challenged by heterogeneous feature spaces and misaligned representations. We propose \textit{NeuroAlign}, a hierarchical framework for structured multimodal fusion. It introduces (1) \textit{Dual-Modal Hierarchical Alignment} (DMHA), which models multi-scale dynamic connectivity and aligns dynamic-static and functional-structural embeddings; and (2) \textit{Dual-Domain Hierarchical Interaction} (DDHI), which enables fine-grained modulation and global interaction between connectivity- and region-level features. To support feature-level inspection, we design \textit{Synergistic Activation Mapping} (SAM), a gradient-free, marker-oriented attribution method for DFC, SFC, ALFF, and FA. Evaluated on GUTCM, ADNI, and OASIS under five-fold validation, NeuroAlign achieves competitive MCI/SCD detection and preliminary cross-dataset transferability. Attribution analyses reveal modality-specific and partially consistent brain patterns, providing model-derived evidence for multimodal representation analysis.

---


### 43. [Readable Yet Unpredictable: Rotated-Outcome Prediction in Vision-Language Models](https://arxiv.org/abs/2606.07641)

**<font color=#1a73e8>作者：</font>** Lexin Wang, Shenghua Liu, Yiwei Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can vision-language models predict what a 180° rotation would reveal from the original image alone? We study this ability through Rotated-Outcome Prediction: given an original image, a model must answer what would be seen or read after a 180° in-plane rotation, without directly observing the rotated target. To isolate this gap, we introduce RotOutBench, a paired diagnostic benchmark spanning open visual cases and controlled text-image rotations. A sharp pattern emerges: many VLMs can recognize the relevant content when directly given either the original or rotated image, yet fail to infer the rotated result from the original image alone. On controlled text-image rotations, predicted-rotation accuracy collapses to near zero even for models with high direct-reading accuracy. A model-level case study further shows that the prediction state can approach a rotated-image reading state, while the final readout still shifts toward the original string. Current VLMs can recognize a transformed visual state when it is shown, but often fail to predict that state from the original view.

---


### 44. [AVI-Bench: Toward Human-like Audio-Visual Intelligence of Omni-MLLMs](https://arxiv.org/abs/2606.07643)

**<font color=#1a73e8>作者：</font>** Yaoting Wang, Ziyi Zhang, Wenming Tu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Omni-Multimodal Large Language Models (Omni-MLLMs) have enabled strong integration of vision, audio, and language. However, their audio-visual intelligence (AVI) remains insufficiently evaluated due to the lack of systematic and comprehensive benchmarks. We introduce AVI-Bench, a cognitively inspired benchmark that evaluates Omni-MLLMs across three stages, perception, understanding, and reasoning, through cross-modal tasks requiring joint audio-visual interpretation. This design enables fine-grained diagnosis of model capabilities and failure modes. To further assess robustness beyond familiar domains, we propose AVI-Bench-PriSe, an extension that probes models' primitive audio-visual sensation using unfamiliar, low-semantic stimuli, testing generalization beyond common training distributions. Extensive experiments on both open-source and closed-source models reveal substantial limitations in current Omni-MLLMs. Based on these findings, we present a four-level AVI taxonomy. Overall, AVI-Bench provides a principled evaluation framework to guide the development of more robust and generalizable AVI. Project website: this https URL

---


### 45. [Steer Where It Matters: Token-Level Visual-Sensitivity Steering for LVLMs Hallucination Mitigation](https://arxiv.org/abs/2606.07647)

**<font color=#1a73e8>作者：</font>** Ruipeng Zhang, Zhihao Li, C. L. Philip Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision language models (LVLMs) have made rapid advancements and are deployed across various applications, yet hallucinations remain a major challenge. Activation steering is appealing due to its minimal training overhead and controllability at inference time. However, we found that during autoregressive decoding, visual conditioning affects token prediction sparsely and locally across decoding steps, and many existing methods that average image-versus-no-image differences over the entire sequence dilute these critical signals, yielding low signal-to-noise ratio steering directions. Additionally, many existing methods apply a fixed steering strength, which misallocates the intervention budget, over-perturbs non-critical tokens, and can cause instability. To address these limitations, we propose Token-Level Visual-Sensitivity Steering (TLVS) for hallucination mitigation. Our approach first extracts token-level steering vectors and refines them, and then applies fine-grained, visual-sensitivity-adaptive steering only where it matters. This lightweight, plug-and-play mechanism requires only minimal training for calibration and can be applied across diverse vision-language models. It modulates the steering strength at each decoding step, selectively suppressing hallucination-prone spans while preserving evidence-grounded content. We evaluate TLVS on several benchmarks, including POPE, AMBER, CHAIR (COCO), MMHal, and HallusionBench, demonstrating consistent improvements over previous steering methods.

---


### 46. [ViMax: Agentic Video Generation](https://arxiv.org/abs/2606.07649)

**<font color=#1a73e8>作者：</font>** Lingxuan Huang, Sizhe He, Hengji Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form video generation requires systematic narrative planning and visual consistency that current short-clip methods cannot provide. Existing methods generate isolated sequences without narrative structure and lack mechanisms for maintaining character and environmental consistency across scenes. We present ViMax, an agentic video generation framework that addresses video creation through coordinated multi-agent collaboration where specialized components negotiate narrative decisions, visual continuity, and production quality. Our framework employs a hierarchical narrative engine with retrieval-augmented generation for global story coherence and a dependency-aware visual consistency mechanism that tracks character and environmental states across temporal boundaries, while VLM-guided agents continuously monitor and refine both narrative coherence and visual fidelity. The framework enables coordinated agent collaboration to generate extended narrative content. This maintains both storytelling integrity and visual coherence across multi-scene timelines.

---


### 47. [A Dataset for Dynamic Human Preferences for Vision Language Models](https://arxiv.org/abs/2606.07653)

**<font color=#1a73e8>作者：</font>** Hannah Gao, Dylan Hadfield-Menell, Rachel Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given the increased adoption of Vision Language Models (VLMs) in human-interactive settings, it is important that we evaluate how well these models can adapt to real-time preferences for different users. While an increasing number of vision-language benchmarks have recently been introduced, they focus largely on evaluating static capabilities and generally-held preferences learned from extensive training data. This work introduces a new benchmark for evaluating the ability of VLMs to understand dynamic human-preferences, i.e. preferences that are passed in-context at inference time. We provide an automated pipeline for generating this benchmark with variations on image dependence, a dynamic multi-modal human-preference dataset, and evaluations of state-of-the-art models on the novel benchmark.

---


### 48. [MM-Matryoshka: Towards Budget-Elastic Visual Document Retrieval via a 2D Multimodal Matryoshka Training Framework](https://arxiv.org/abs/2606.07654)

**<font color=#1a73e8>作者：</font>** Haowen Xiang, Yibo Yan, Jiahao Huo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-vector visual document retrievers achieve strong fine-grained matching by representing each page with multiple vectors from deep Vision-Language Models (VLMs), but this design makes deployment expensive in both storage and computational overhead. Existing efficiency techniques usually optimize only part of this budget, leaving multimodal retrievers without a unified way to trade accuracy for both vector width and encoder depth. Therefore, we propose MM-Matryoshka, a 2D Matryoshka training framework for budget-elastic Visual Document Retrieval (VDR), enabling ColPali-style multi-vector retrieval elastic along both dimension and layer. At inference time, a single retriever can select a 2D selectable budget without training separate models for different budgets. Through comprehensive experiments across multiple representative backbones, we demonstrate that by retaining significantly higher quality than direct truncation baselines while substantially reducing storage and computational overhead, MM-Matryoshka can offer robust budget elasticity for efficient VDR.

---


### 49. [Need We Teach Foundation Models What is a Generative Image? Gradient-Free Generative Artifact Detection via Analytic Spectral Adaptation](https://arxiv.org/abs/2606.07660)

**<font color=#1a73e8>作者：</font>** Qiaoyu Chen, Bing Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting foundation models to detect generative artifacts via gradient-based updates compromises their intrinsic representations. Under optimization on limited samples, models overfit to local domain shortcuts. Fine-tuning massive weights on specialized data introduces erroneous inductive biases, inducing a measurable $\mathcal{L}_2$ norm perturbation in the high-dimensional feature space -- a phenomenon we formalize as anchor drift. Amplified by nonlinear activations, this drift impairs zero-shot forgery detection across unseen this http URL propose a gradient-free methodology reframing detection from binary classification to an out-of-distribution (OOD) anomaly measurement problem. Treating a frozen foundation model as a stable coordinate system, we establish an absolute natural anchor on the real visual manifold by analytically decoupling statistical and semantic deviations, derived from attention-weighted spatial moments and orthogonal projection of perceptual inconsistencies. Evaluated in an extreme zero-shot setting (trained on face forgeries, tested on universal Text-to-Image generations), our method significantly outperforms gradient-optimized paradigms. Backpropagation-free forward passes and linear solvers enable hardware-agnostic, edge-deployable calibration with minimal latency. Furthermore, the Sherman-Morrison formula unlocks instantaneous online learning against novel attacks and enables privacy-preserving federated collaboration via covariance delta transmission.

---


### 50. [PereStruct: Multimodal Semantic Assembly for Robust Historical Document Parsing](https://arxiv.org/abs/2606.07661)

**<font color=#1a73e8>作者：</font>** Maksim Shandybo, Ivan Bespalov, Daniil Yefimov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parsing historical documents with complex, non-standard layouts remains a fundamental bottleneck in large-scale archival digitization. Unlike modern typography, historical newspapers exhibit severe physical degradation and highly irregular page structures that confound even state-of-the-art vision-language models, presenting severe out-of-distribution challenges. We address this gap with an automated pipeline specifically designed for parsing historical newspapers, documents characterized by particularly intricate multi-column layouts. Our approach combines a fine-tuned YOLO architecture for layout analysis and block detection, trained on 1,426 fully human-annotated scanned pages, with a novel semantic assembly module that reconstructs articles by jointly modeling lexical-semantic similarity via TF-IDF, visual embeddings from our fine-tuned YOLO, and geometric layout constraints. This multi-modal integration yields state-of-the-art performance, achieving an F1 score of 0.904 on block-to-article mapping. Notably, end-to-end evaluation against vision-language models (Qwen3.6-35B-A3B and Qwen3.6-Plus) demonstrates that PereStruct achieves substantially higher fidelity (BLEU approximately 0.96 vs 0.34), validating that modular architectures excel where generic VLMs fail on complex historical layouts. To support reproducibility and advance research in this domain, we release both the training corpus of 599 annotated pages and a curated PereStruct benchmark of 93 pages with expert-verified ground-truth block-to-article mappings. This framework establishes a robust foundation for high-fidelity digitization and semantic reconstruction of complex archival materials.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-331](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
