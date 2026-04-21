# 🧠 大模型相关研究 | 2026年04月22日

> 本类共 **353** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**351-353**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-353**

---

### 351. [When Can LLMs Learn to Reason with Weak Supervision?](https://arxiv.org/abs/2604.18574)

**<font color=#1a73e8>作者：</font>** Salman Rahman, Jingyan Shen, Anna Mordvina 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models have achieved significant reasoning improvements through reinforcement learning with verifiable rewards (RLVR). Yet as model capabilities grow, constructing high-quality reward signals becomes increasingly difficult, making it essential to understand when RLVR can succeed under weaker forms of supervision. We conduct a systematic empirical study across diverse model families and reasoning domains under three weak supervision settings: scarce data, noisy rewards, and self-supervised proxy rewards. We find that generalization is governed by training reward saturation dynamics: models that generalize exhibit a prolonged pre-saturation phase during which training reward and downstream performance climb together, while models that saturate rapidly memorize rather than learn. We identify reasoning faithfulness, defined as the extent to which intermediate steps logically support the final answer, as the pre-RL property that predicts which regime a model falls into, while output diversity alone is uninformative. Motivated by these findings, we disentangle the contributions of continual pre-training and supervised fine-tuning, finding that SFT on explicit reasoning traces is necessary for generalization under weak supervision, while continual pre-training on domain data amplifies the effect. Applied together to Llama3.2-3B-Base, these interventions enable generalization across all three settings where the base model previously failed.

---


### 352. [Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs](https://arxiv.org/abs/2604.18576)

**<font color=#1a73e8>作者：</font>** Kevin Murphy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present BLF (Bayesian Linguistic Forecaster), an agentic system for binary forecasting that achieves state-of-the-art performance on the ForecastBench benchmark. The system is built on three ideas. (1) A Bayesian linguistic belief state: a semi-structured representation combining numerical probability estimates with natural-language evidence summaries, updated by the LLM at each step of an iterative tool-use loop. This contrasts with the common approach of appending all retrieved evidence to an ever-growing context. (2) Hierarchical multi-trial aggregation: running $K$ independent trials and combining them using logit-space shrinkage with a data-dependent prior. (3) Hierarchical calibration: Platt scaling with a hierarchical prior, which avoids over-shrinking extreme predictions for sources with skewed base rates.
On 400 backtesting questions from the ForecastBench leaderboard, BLF outperforms all the top public methods, including Cassi, GPT-5, Grok~4.20, and Foresight-32B. Ablation studies show that the structured belief state is as impactful as web search access, and that shrinkage aggregation and hierarchical calibration each provide significant additional gains.
In addition, we develop a robust back-testing framework with a leakage rate below 1.5\%, and use rigorous statistical methodology to compare different methods while controlling for various sources of noise.

---


### 353. [MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval](https://arxiv.org/abs/2604.18584)

**<font color=#1a73e8>作者：</font>** Shaden Alshammari, Kevin Wen, Abrar Zainal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical problem solving remains a challenging test of reasoning for large language and multimodal models, yet existing benchmarks are limited in size, language coverage, and task diversity. We introduce MathNet, a high-quality, large-scale, multimodal, and multilingual dataset of Olympiad-level math problems together with a benchmark for evaluating mathematical reasoning in generative models and mathematical retrieval in embedding-based systems. MathNet spans 47 countries, 17 languages, and two decades of competitions, comprising 30,676 expert-authored problems with solutions across diverse domains. In addition to the core dataset, we construct a retrieval benchmark consisting of mathematically equivalent and structurally similar problem pairs curated by human experts.
MathNet supports three tasks: (i) Problem Solving, (ii) Math-Aware Retrieval, and (iii) Retrieval-Augmented Problem Solving. Experimental results show that even state-of-the-art reasoning models (78.4% for Gemini-3.1-Pro and 69.3% for GPT-5) remain challenged, while embedding models struggle to retrieve equivalent problems. We further show that retrieval-augmented generation performance is highly sensitive to retrieval quality; for example, DeepSeek-V3.2-Speciale achieves gains of up to 12%, obtaining the highest scores on the benchmark. MathNet provides the largest high-quality Olympiad dataset together with the first benchmark for evaluating mathematical problem retrieval, and we publicly release both the dataset and benchmark at this https URL.

---


> [!TIP]
> 当前位于：**351-353**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-353**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
